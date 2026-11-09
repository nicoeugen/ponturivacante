import json
import os
import re
import sys
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r'C:\Users\Eugen\Desktop\Proiecte\website turism'
DATA_DIR = os.path.join(BASE_DIR, 'data')

print("=" * 70)
print("🔍 AUDIT INTEGRAL LINKURI — PONTURIVACANȚE")
print("=" * 70)

# Load data files
with open(os.path.join(DATA_DIR, 'deals.json'), 'r', encoding='utf-8') as f:
    deals = json.load(f)

with open(os.path.join(DATA_DIR, 'romania_deals.json'), 'r', encoding='utf-8') as f:
    romania_deals = json.load(f)

with open(os.path.join(DATA_DIR, 'cruises.json'), 'r', encoding='utf-8') as f:
    cruises = json.load(f)

with open(os.path.join(DATA_DIR, 'blog_articles.json'), 'r', encoding='utf-8') as f:
    blogs = json.load(f)

print(f"Dataset încărcat:")
print(f" - Oferte internaționale: {len(deals)}")
print(f" - Cazări România: {len(romania_deals)}")
print(f" - Croaziere: {len(cruises)}")
print(f" - Articole Blog: {len(blogs)}")
print("-" * 70)

deal_slugs = {d['slug'] for d in deals if 'slug' in d}
romania_slugs = {r['slug'] for r in romania_deals if 'slug' in r}
cruise_slugs = {c['slug'] for c in cruises if 'slug' in c}
blog_slugs = {b['slug'] for b in blogs if 'slug' in b}

errors = []
warnings = []
stats = {
    'total_urls_checked': 0,
    'flight_links': 0,
    'hotel_links': 0,
    'agoda_links': 0,
    'kiwi_links': 0,
    'google_flight_links': 0,
    'skyscanner_links': 0,
    'alternative_date_links': 0,
    'blog_links': 0,
    'romania_links': 0,
    'cruise_links': 0
}

def validate_url(url, context, require_https=True):
    stats['total_urls_checked'] += 1
    if not url or not isinstance(url, str):
        errors.append(f"[{context}] URL lipsă sau invalid (tip: {type(url)})")
        return False
    
    url = url.strip()
    if ' ' in url:
        errors.append(f"[{context}] Conține spații necodate: {url}")
        return False
    
    if any(bad in url for bad in ['undefined', 'null', 'NaN', '[object', 'None']):
        errors.append(f"[{context}] Conține șir invalid: {url}")
        return False
        
    try:
        parsed = urlparse(url)
        if require_https and parsed.scheme not in ('http', 'https'):
            errors.append(f"[{context}] Schemă URL invalidă ({parsed.scheme}): {url}")
            return False
        if not parsed.netloc:
            errors.append(f"[{context}] Domeniu lipsă: {url}")
            return False
    except Exception as e:
        errors.append(f"[{context}] Excepție parsare: {e}")
        return False

    return True

# -------------------------------------------------------------------------
# 1. Audit Deals Internaționale
# -------------------------------------------------------------------------
print("\n1. Verificare Oferte Internaționale (deals.json)...")
for d in deals:
    slug = d.get('slug', 'fara-slug')
    ttype = d.get('transportType', 'flight')
    fl = d.get('flight', {})
    ho = d.get('hotel', {})
    accs = d.get('accommodationOptions', [])
    alts = d.get('alternativeDates', [])

    # Transport type
    if ttype == 'flight':
        stats['flight_links'] += 1
        link = fl.get('link')
        validate_url(link, f"Deal {slug} -> flight.link")
        
        # Google Flights
        gf = fl.get('googleFlightsLink')
        if gf:
            stats['google_flight_links'] += 1
            validate_url(gf, f"Deal {slug} -> googleFlightsLink")
            
        # Skyscanner
        sk = fl.get('skyscannerLink')
        if sk:
            stats['skyscanner_links'] += 1
            validate_url(sk, f"Deal {slug} -> skyscannerLink")
            
        # Kiwi
        kw = fl.get('kiwiLink')
        if kw:
            stats['kiwi_links'] += 1
            if validate_url(kw, f"Deal {slug} -> kiwiLink"):
                if 'marker=801687' not in kw:
                    warnings.append(f"Deal {slug} -> kiwiLink lipsește marker=801687 ({kw})")

    # Hotel
    h_link = ho.get('link')
    stats['hotel_links'] += 1
    validate_url(h_link, f"Deal {slug} -> hotel.link")

    # Accommodation options
    if not accs:
        warnings.append(f"Deal {slug} nu are accommodationOptions")
    for idx, a in enumerate(accs):
        prov = a.get('provider', f'acc-{idx}')
        a_link = a.get('link')
        stats['hotel_links'] += 1
        if validate_url(a_link, f"Deal {slug} -> acc[{idx}] ({prov})"):
            if 'agoda.com' in a_link:
                stats['agoda_links'] += 1
                if 'cid=1980047' not in a_link:
                    warnings.append(f"Deal {slug} -> Agoda missing cid=1980047 ({a_link})")
                if a_link.strip().endswith('agoda.com/') or a_link.strip().endswith('agoda.com/ro-ro/'):
                    warnings.append(f"Deal {slug} -> Agoda link este homepage generic ({a_link})")

    # Alternative dates
    for a_idx, alt in enumerate(alts):
        stats['alternative_date_links'] += 1
        alt_link = alt.get('link')
        if alt_link:
            validate_url(alt_link, f"Deal {slug} -> altDate[{a_idx}].link")
        alt_gf = alt.get('googleFlightsLink')
        if alt_gf:
            validate_url(alt_gf, f"Deal {slug} -> altDate[{a_idx}].googleFlightsLink")
        alt_sk = alt.get('skyscannerLink')
        if alt_sk:
            validate_url(alt_sk, f"Deal {slug} -> altDate[{a_idx}].skyscannerLink")

# -------------------------------------------------------------------------
# 2. Audit Cazări România
# -------------------------------------------------------------------------
print("2. Verificare Cazări România (romania_deals.json)...")
for rd in romania_deals:
    slug = rd.get('slug', 'fara-slug')
    stats['romania_links'] += 1
    burl = rd.get('bookingUrl')
    validate_url(burl, f"Romania {slug} -> bookingUrl")
    if burl and 'booking.com' in burl:
        if 'aid=' not in burl:
            warnings.append(f"Romania {slug} -> Booking URL fără parametru aid")

# -------------------------------------------------------------------------
# 3. Audit Croaziere
# -------------------------------------------------------------------------
print("3. Verificare Croaziere (cruises.json)...")
for cr in cruises:
    slug = cr.get('slug', 'fara-slug')
    stats['cruise_links'] += 1
    fl = cr.get('flight', {})
    cd = cr.get('cruiseDetails', {})
    
    validate_url(fl.get('link'), f"Cruise {slug} -> flight.link")
    validate_url(cd.get('link'), f"Cruise {slug} -> cruiseDetails.link")

# -------------------------------------------------------------------------
# 4. Audit Blog Articles & Related Deals
# -------------------------------------------------------------------------
print("4. Verificare Articole Blog (blog_articles.json)...")
for b in blogs:
    slug = b.get('slug', 'fara-slug')
    stats['blog_links'] += 1
    # Check relatedDeals
    rels = b.get('relatedDeals', [])
    for rd in rels:
        if rd not in deal_slugs and rd not in romania_slugs and rd not in cruise_slugs:
            errors.append(f"Blog {slug} -> relatedDeal '{rd}' nu există în baza de date!")

# -------------------------------------------------------------------------
# 5. Audit Template Internal Links (HTML / Astro)
# -------------------------------------------------------------------------
print("5. Verificare Linkuri Interne din Șabloane Astro...")
pages_dir = os.path.join(BASE_DIR, 'src', 'pages')
components_dir = os.path.join(BASE_DIR, 'src', 'components')

href_regex = re.compile(r'href=["\']([^"\']+)["\']')
all_internal_links = set()

for root, _, files in os.walk(os.path.join(BASE_DIR, 'src')):
    for file in files:
        if file.endswith('.astro'):
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            for m in href_regex.finditer(content):
                target = m.group(1).strip()
                # Exclude expressions like {deal.slug} or variables
                if '{' in target or '$' in target:
                    continue
                if target.startswith('/') and not target.startswith('//'):
                    all_internal_links.add((target, file))

# Known static routes
known_routes = {
    '/', '/despre/', '/intrebari-frecvente/', '/termeni-si-conditii/',
    '/politica-confidentialitate/', '/blog/', '/croaziere/', '/romania/',
    '/go/flight/', '/go/hotel/', '/rss.xml',
    '/categorie/1-decembrie/', '/categorie/targuri-craciun/', '/categorie/revelion/',
    '/categorie/exotice/', '/categorie/schi/', '/categorie/city-break/',
    '/categorie/mare-si-soare/', '/categorie/weekend/',
    '/plecari/bucuresti/', '/plecari/cluj-napoca/', '/plecari/timisoara/',
    '/plecari/iasi/', '/plecari/sibiu/', '/plecari/craiova/',
    '/plecari/suceava/', '/plecari/constanta/'
}

for route, source_file in all_internal_links:
    norm_route = route if route.endswith('/') or '.' in route or '#' in route or '?' in route else route + '/'
    base_route = norm_route.split('?')[0].split('#')[0]
    if base_route in known_routes:
        continue
    if base_route.startswith('/oferta/'):
        sl = base_route.replace('/oferta/', '').strip('/')
        if sl not in deal_slugs:
            errors.append(f"Internal link '{base_route}' din {source_file} pointează spre o ofertă inexistentă ({sl})")
    elif base_route.startswith('/romania/'):
        sl = base_route.replace('/romania/', '').strip('/')
        if sl not in romania_slugs:
            errors.append(f"Internal link '{base_route}' din {source_file} pointează spre o cazare România inexistentă ({sl})")
    elif base_route.startswith('/croaziere/'):
        sl = base_route.replace('/croaziere/', '').strip('/')
        if sl not in cruise_slugs:
            errors.append(f"Internal link '{base_route}' din {source_file} pointează spre o croazieră inexistentă ({sl})")
    elif base_route.startswith('/blog/'):
        sl = base_route.replace('/blog/', '').strip('/')
        if sl not in blog_slugs:
            errors.append(f"Internal link '{base_route}' din {source_file} pointează spre un articol blog inexistent ({sl})")
    elif base_route.startswith('/categorie/') or base_route.startswith('/plecari/'):
        if base_route not in known_routes:
            errors.append(f"Internal link necunoscut: '{base_route}' din {source_file}")

# -------------------------------------------------------------------------
# Rezumat Raport
# -------------------------------------------------------------------------
print("\n" + "=" * 70)
print("📊 REZUMAT STATISTICI AUDIT")
print("=" * 70)
print(f"Total URL-uri externe analizate în date: {stats['total_urls_checked']}")
print(f" - Zboruri: {stats['flight_links']}")
print(f" - Cazări Booking: {stats['hotel_links']}")
print(f" - Partener Agoda: {stats['agoda_links']}")
print(f" - Kiwi Affiliate: {stats['kiwi_links']}")
print(f" - Google Flights: {stats['google_flight_links']}")
print(f" - Skyscanner: {stats['skyscanner_links']}")
print(f" - Perioade alternative: {stats['alternative_date_links']}")
print(f" - Unități România: {stats['romania_links']}")
print(f" - Croaziere: {stats['cruise_links']}")
print(f" - Articole blog: {stats['blog_links']}")
print(f"Total link-uri interne Astro verificate: {len(all_internal_links)}")

print("\n" + "=" * 70)
if errors:
    print(f"❌ S-AU GĂSIT {len(errors)} ERORI CRITICE:")
    for err in errors:
        print("  - ", err)
else:
    print("✅ 0 ERORI CRITICE! Toate URL-urile sunt valide structural, au schemă corectă și fără spații/undefined.")

if warnings:
    print(f"\n⚠️  {len(warnings)} AVERTISMENTE DE AFILIERE / CALITATE:")
    for w in warnings[:25]:
        print("  - ", w)
    if len(warnings) > 25:
        print(f"  ... și încă {len(warnings) - 25} avertismente.")
else:
    print("✅ 0 Avertismente.")
print("=" * 70)
