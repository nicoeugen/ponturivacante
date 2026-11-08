import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Inspect data/romania_deals.json
print("=== AUDIT ROMANIA DEALS ===")
with open(r'C:\Users\Eugen\Desktop\Proiecte\website turism\data\romania_deals.json', 'r', encoding='utf-8') as f:
    romania_deals = json.load(f)

print(f"Total Romania deals: {len(romania_deals)}")
for rd in romania_deals:
    slug = rd.get('slug')
    name = rd.get('name')
    burl = rd.get('bookingUrl', '')
    print(f"[{slug}] {name}")
    print(f"  bookingUrl: {burl}")

# 2. Inspect data/cruises.json
print("\n=== AUDIT CRUISES ===")
with open(r'C:\Users\Eugen\Desktop\Proiecte\website turism\data\cruises.json', 'r', encoding='utf-8') as f:
    cruises = json.load(f)

print(f"Total Cruises: {len(cruises)}")
for cr in cruises:
    slug = cr.get('slug')
    title = cr.get('title')
    fl = cr.get('flight', {})
    cd = cr.get('cruiseDetails', {})
    print(f"[{slug}] {title}")
    print(f"  flight.link: {fl.get('link')}")
    print(f"  flight.kiwiLink: {fl.get('kiwiLink')}")
    print(f"  cruiseDetails.link: {cd.get('link')}")
    print(f"  bookingUrl: {cr.get('bookingUrl')}")


print("\n=== AUDIT TEMPLATES ===")
templates = [
    r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\romania\index.astro',
    r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\romania\[slug].astro',
    r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\croaziere\index.astro',
    r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\croaziere\[slug].astro',
    r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\index.astro',
    r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\components\Footer.astro',
]

for t in templates:
    with open(t, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"\n--- {t.split('/')[-1].split(chr(92))[-1]} ---")
    for line in c.splitlines():
        if '/go/' in line or 'booking' in line.lower() or 'asigurari' in line.lower():
            if 'href' in line:
                print(" ", line.strip()[:140])
