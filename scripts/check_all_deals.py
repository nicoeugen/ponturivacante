import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json', 'r', encoding='utf-8') as f:
    deals = json.load(f)

print(f"Total deals: {len(deals)}")

has_options = 0
agoda_first = 0
booking_first = 0
no_options = 0

for i, d in enumerate(deals):
    opts = d.get('accommodationOptions', [])
    if opts:
        has_options += 1
        first_prov = opts[0].get('providerId', '')
        if first_prov == 'agoda':
            agoda_first += 1
        elif first_prov == 'booking':
            booking_first += 1
    else:
        no_options += 1

print(f"Deals with accommodationOptions: {has_options}")
print(f"  - Agoda first: {agoda_first}")
print(f"  - Booking first: {booking_first}")
print(f"Deals with NO accommodationOptions: {no_options}")
