import json, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

cruises = json.load(open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/cruises.json', encoding='utf-8'))
for c in cruises:
    print(f"Cruise: {c['title']} | Price: {c['priceFrom']} EUR | Ship: {c['ship']}")
    print(f"  BookingUrl: {c.get('bookingUrl')}")
