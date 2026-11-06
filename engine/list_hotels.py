import json, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

deals = json.load(open('C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json', encoding='utf-8'))
for i, d in enumerate(deals):
    slug = d.get('slug')
    dest = d.get('destination')
    hotel = d.get('hotel', {}).get('name')
    h_link = d.get('hotel', {}).get('link')
    accs = [a for a in d.get('accommodationOptions', []) if a.get('providerId') == 'booking']
    acc_name = accs[0]['name'] if accs else ''
    acc_link = accs[0]['link'] if accs else ''
    print(f"{i+1:2d}. {slug} | {dest} | Hotel: {hotel} | AccBooking: {acc_name}")
    print(f"    HotelLink: {h_link}")
    print(f"    AccLink:   {acc_link}")
