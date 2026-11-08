import json
import sys
import urllib.request
import urllib.parse
import time

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Eugen\Desktop\Proiecte\website turism\data\deals.json', 'r', encoding='utf-8') as f:
    deals = json.load(f)

print(f"Testing links for {len(deals)} deals...")

results = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

for i, d in enumerate(deals):
    slug = d.get('slug')
    title = d.get('title')
    hotel = d.get('hotel', {})
    accs = d.get('accommodationOptions', [])
    flight = d.get('flight', {})
    
    agoda_link = None
    booking_link = hotel.get('link')
    for a in accs:
        if 'agoda.com' in a.get('link', ''):
            agoda_link = a.get('link')
            break
            
    # Check Agoda link
    agoda_status = 'N/A'
    if agoda_link:
        try:
            req = urllib.request.Request(agoda_link, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                agoda_status = str(r.status)
        except urllib.error.HTTPError as e:
            agoda_status = f"ERR {e.code}"
        except Exception as e:
            agoda_status = f"EXC: {str(e)[:30]}"
            
    # Check Booking link
    booking_status = 'N/A'
    if booking_link:
        try:
            req = urllib.request.Request(booking_link, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as r:
                booking_status = str(r.status)
        except urllib.error.HTTPError as e:
            booking_status = f"ERR {e.code}"
        except Exception as e:
            booking_status = f"EXC: {str(e)[:30]}"
            
    print(f"[{i+1}/{len(deals)}] {slug[:35]:35} | Agoda: {agoda_status:8} | Booking: {booking_status:8}")
    results.append({
        'slug': slug,
        'agoda_link': agoda_link,
        'agoda_status': agoda_status,
        'booking_link': booking_link,
        'booking_status': booking_status
    })
    time.sleep(0.1)

print("\n=== SUMMARY OF FAILED LINKS ===")
failed = [r for r in results if 'ERR' in r['agoda_status'] or 'ERR' in r['booking_status']]
print(f"Total failures: {len(failed)}")
for f in failed:
    print(f" - {f['slug']}: Agoda={f['agoda_status']}, Booking={f['booking_status']}")


print("\n=== TESTING ROMANIA DEALS ===")
with open(r'C:\Users\Eugen\Desktop\Proiecte\website turism\data\romania_deals.json', 'r', encoding='utf-8') as f:
    r_deals = json.load(f)

for i, d in enumerate(r_deals):
    slug = d.get('slug')
    url = d.get('bookingUrl')
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            status = str(r.status)
    except urllib.error.HTTPError as e:
        status = f"ERR {e.code}"
    except Exception as e:
        status = f"EXC: {str(e)[:30]}"
    print(f"[{i+1}/{len(r_deals)}] {slug[:35]:35} -> {status}")
