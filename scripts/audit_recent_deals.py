import json
import urllib.request
import urllib.error
import ssl
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'ro-RO,ro;q=0.9,en;q=0.8'
}

with open(r'C:\Users\Eugen\Desktop\Proiecte\website turism\data\deals.json', 'r', encoding='utf-8') as f:
    deals = json.load(f)

print("=" * 80)
print("🔍 AUDIT DETALIAT PE CELE MAI RECENTE 12 LISTĂRI")
print("=" * 80)

now = datetime.now()

for idx, d in enumerate(deals[:12]):
    deal_id = d.get('id')
    slug = d.get('slug')
    title = d.get('title')
    price = d.get('priceTotalPerPerson')
    fl = d.get('flight', {})
    ho = d.get('hotel', {})
    accs = d.get('accommodationOptions', [])
    alts = d.get('alternativeDates', [])
    dep_date_str = d.get('departureDate', '')
    ret_date_str = d.get('returnDate', '')
    
    # Check date freshness
    is_future = False
    try:
        dep_dt = datetime.strptime(dep_date_str, '%Y-%m-%d')
        is_future = dep_dt > now
        days_ahead = (dep_dt - now).days
    except Exception as e:
        days_ahead = -999

    fl_price = fl.get('price', 0)
    ho_price = ho.get('pricePerPerson', 0)
    expected_total = fl_price + ho_price
    price_ok = (expected_total == price)
    
    # Agoda link check
    agoda_link = None
    agoda_name = None
    for a in accs:
        if 'agoda.com' in a.get('link', ''):
            agoda_link = a.get('link')
            agoda_name = a.get('name')
            break
            
    print(f"\n[{idx+1}] {deal_id} — {title[:60]}")
    print(f"    🔗 Slug: /oferta/{slug}/")
    print(f"    📅 Plecare: {dep_date_str} -> {ret_date_str} ({days_ahead} zile în viitor: {'✓ OK' if is_future else '⚠️ TRECUT'})")
    print(f"    💰 Preț: {price} € (Zbor: {fl_price} € + Cazare: {ho_price} €) -> {'✓ Calcul corect' if price_ok else f'⚠️ DISCREPANȚĂ ({expected_total})'}")
    print(f"    ✈️ Ruta zbor: {fl.get('route')} ({fl.get('airline')})")
    print(f"    🏨 Hotel: {ho.get('name')} ({ho.get('rating')}★)")
    print(f"    🏷️ Agoda: {agoda_name[:40]} -> {'✓ cid=1980047 prezent' if agoda_link and 'cid=1980047' in agoda_link else '⚠️ LIPSĂ CID'}")
    print(f"    🗓️ Date alternative: {len(alts)} perioade disponibile")
