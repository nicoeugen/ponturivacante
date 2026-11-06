import json, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

deals = json.load(open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json', encoding='utf-8'))
for i, d in enumerate(deals):
    f = d.get('flight', {})
    airline = f.get('airline')
    orig = d.get('originCode')
    dest = d.get('destinationCode')
    dep = d.get('departureDate')
    ret = d.get('returnDate')
    link = f.get('link')
    print(f"{i+1:2d}. {d.get('slug')}")
    print(f"    Airline: {airline} | {orig} -> {dest} ({dep} to {ret})")
    print(f"    Link: {link}")
