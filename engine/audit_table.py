import json, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

deals = json.load(open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json', encoding='utf-8'))
print(f"{'#':2} | {'Destination':<28} | {'Dates':<20} | {'Flight':<8} | {'Hotel (p/p)':<12} | {'Total':<6} | {'Airline':<18}")
print("-" * 105)
for i, d in enumerate(deals):
    dest = d['destination']
    dates = f"{d['departureDate']} -> {d['returnDate']}"
    fl_price = f"{d['flight']['price']} EUR"
    h_price = f"{d['hotel']['pricePerPerson']} EUR"
    tot = f"{d['priceTotalPerPerson']} EUR"
    airline = d['flight']['airline']
    print(f"{i+1:2d} | {dest:<28} | {dates:<20} | {fl_price:<8} | {h_price:<12} | {tot:<6} | {airline:<18}")
