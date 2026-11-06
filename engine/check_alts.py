import json, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

deals = json.load(open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json', encoding='utf-8'))
for d in deals:
    alts = d.get('alternativeDates', [])
    if alts:
        print(f"Deal: {d['slug']}")
        for a in alts:
            print(f"   -> dates: {a.get('dates')} | price: {a.get('price')} | link: {a.get('link')}")
