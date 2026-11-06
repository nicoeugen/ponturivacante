import json, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

deals = json.load(open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json', encoding='utf-8'))
for d in deals[:4]:
    print(f"Slug: {d['slug']}")
    print(f"  Airline: {d['flight']['airline']}")
    print(f"  DirectLink: {d['flight']['link']}")
    print(f"  GoogleFlights: {d['flight']['googleFlightsLink']}")
    print(f"  Skyscanner: {d['flight']['skyscannerLink']}")
    if d.get('alternativeDates'):
        for a in d['alternativeDates']:
            print(f"     Alt: {a['dates']} -> {a['link']}")
