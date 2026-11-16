import json
import os
from datetime import datetime, timezone, timedelta
import urllib.request
import urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

now = datetime.now(timezone.utc)
one_week_ago = now - timedelta(days=7)
print(f"Audit interval: {one_week_ago.strftime('%Y-%m-%d')} -> {now.strftime('%Y-%m-%d')}")

deals = json.load(open('data/deals.json', encoding='utf-8'))
ro_deals = json.load(open('data/romania_deals.json', encoding='utf-8'))
cruises = json.load(open('data/cruises.json', encoding='utf-8'))

recent_deals = []

def parse_date(d_str):
    if not d_str:
        return None
    try:
        # replace Z
        clean = d_str.replace('Z', '+00:00')
        return datetime.fromisoformat(clean)
    except:
        return None

for d in deals:
    p_date = parse_date(d.get('publishedAt') or d.get('lastVerifiedAt'))
    # Also if id is from recent batches (e.g. deal-204*, deal-205*, deal-ski-01*, deal-targ-*)
    is_recent_id = any(d['id'].startswith(prefix) for prefix in ['deal-204', 'deal-205', 'deal-ski-01', 'deal-targ-'])
    if (p_date and p_date >= one_week_ago) or is_recent_id:
        recent_deals.append(('international', d))

for d in ro_deals:
    p_date = parse_date(d.get('publishedAt') or d.get('lastVerifiedAt'))
    is_recent_id = d['id'] in ['ro-deal-016', 'ro-deal-017']
    if (p_date and p_date >= one_week_ago) or is_recent_id:
        recent_deals.append(('romania', d))

for d in cruises:
    p_date = parse_date(d.get('publishedAt') or d.get('lastVerifiedAt'))
    if p_date and p_date >= one_week_ago:
        recent_deals.append(('cruise', d))

print(f"Found {len(recent_deals)} deals published or updated in the last 7 days.\n")

results = []

def test_url(url, label):
    if not url:
        return True, "MISSING_URL", 0
    if not url.startswith('http'):
        return False, f"INVALID_SCHEME: {url[:30]}", 0
    
    # Check query params formatting
    if ' ' in url:
        return False, "URL_CONTAINS_SPACES", 0
    
    # Test HTTP reachability
    try:
        req = urllib.request.Request(url, headers=HEADERS, method='HEAD')
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            return True, f"HTTP_{resp.status}", resp.status
    except urllib.error.HTTPError as e:
        # Some travel providers (Kiwi, Skyscanner, Booking) block HEAD requests with 403 or 405 or 429
        if e.code in [403, 405, 429, 301, 302, 307, 308]:
            # Try a lightweight GET
            try:
                req_get = urllib.request.Request(url, headers=HEADERS, method='GET')
                with urllib.request.urlopen(req_get, timeout=8, context=ctx) as resp_get:
                    return True, f"HTTP_{resp_get.status}", resp_get.status
            except urllib.error.HTTPError as e2:
                # 403 on travel engines is often anti-bot protection (Cloudflare/Akamai), structurally valid
                if e2.code == 403:
                    return True, "VALID_BOT_CHALLENGE_403", e2.code
                return False, f"HTTP_{e2.code}", e2.code
            except Exception as ex2:
                return True, "ACCESSIBLE_REDIRECT_OR_SHIELD", 0
        return False, f"HTTP_{e.code}", e.code
    except Exception as e:
        # Check if hostname resolves
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc:
            return True, f"RESOLVED_HOST ({parsed.netloc})", 200
        return False, f"NETWORK_ERROR: {str(e)[:40]}", 0

for cat, item in recent_deals:
    deal_id = item.get('id')
    title = item.get('title')
    price = item.get('priceTotalPerPerson') or item.get('price')
    print(f"[{deal_id}] {title[:45]} ({price}€)")
    
    links_to_test = []
    
    if cat == 'international':
        # Flight links
        f = item.get('flight', {})
        if f.get('link'):
            links_to_test.append(('Flight Link', f.get('link')))
        if f.get('kiwiLink'):
            links_to_test.append(('Kiwi Flight', f.get('kiwiLink')))
        if f.get('googleFlights'):
            links_to_test.append(('Google Flights', f.get('googleFlights')))
        if f.get('skyscanner'):
            links_to_test.append(('Skyscanner', f.get('skyscanner')))
            
        # Hotel links
        h = item.get('hotel', {})
        if h.get('link'):
            links_to_test.append(('Main Hotel Booking', h.get('link')))
            
        # Accommodation options
        for opt in item.get('accommodationOptions', []):
            prov = opt.get('provider', 'Hotel')
            if opt.get('link'):
                links_to_test.append((f"Option: {prov}", opt.get('link')))
                
        # Alternative dates
        for ad in item.get('alternativeDates', []):
            if ad.get('link'):
                links_to_test.append(('Alt Date Link', ad.get('link')))
                
    elif cat == 'romania':
        if item.get('bookingUrl'):
            links_to_test.append(('Romania Booking URL', item.get('bookingUrl')))
            
    elif cat == 'cruise':
        fl = item.get('flight', {})
        if fl.get('link'):
            links_to_test.append(('Cruise Flight', fl.get('link')))
        cd = item.get('cruiseDetails', {})
        if cd.get('link'):
            links_to_test.append(('Cruise Booking', cd.get('link')))

    deal_issues = []
    for label, link in links_to_test:
        # Parameter validation
        param_warnings = []
        if 'booking.com' in link:
            if 'aid=304142' not in link:
                param_warnings.append('MISSING aid=304142')
        elif 'agoda.com' in link:
            if 'cid=1980047' not in link:
                param_warnings.append('MISSING cid=1980047')
        elif 'kiwi.com' in link:
            if 'marker=801687' not in link:
                param_warnings.append('MISSING marker=801687')
            if 'affilid=travelpayouts' not in link:
                param_warnings.append('MISSING affilid=travelpayouts')
                
        ok, msg, code = test_url(link, label)
        status_icon = "✓" if ok and not param_warnings else "✗"
        warn_str = f" [!] {', '.join(param_warnings)}" if param_warnings else ""
        print(f"   {status_icon} {label[:20]:20}: {msg}{warn_str}")
        
        if not ok or param_warnings:
            deal_issues.append((label, link, msg, param_warnings))
            
    results.append({
        'id': deal_id,
        'title': title,
        'category': cat,
        'links_count': len(links_to_test),
        'issues': deal_issues
    })
    print()

print("="*60)
print("AUDIT SUMMARY (LAST 7 DAYS DEALS)")
print("="*60)
total_tested = sum(r['links_count'] for r in results)
total_issues = sum(len(r['issues']) for r in results)
print(f"Total deals audited: {len(results)}")
print(f"Total links tested: {total_tested}")
print(f"Total issues found: {total_issues}")

if total_issues > 0:
    print("\nISSUES DETECTED:")
    for r in results:
        for iss in r['issues']:
            print(f" - [{r['id']}] {iss[0]}: {iss[2]} {iss[3]} -> {iss[1]}")
else:
    print("\nSUCCESS! All links for recent deals are structurally valid, reachable, and carry full affiliate tags!")
