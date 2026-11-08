import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\oferta\[slug].astro'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

old_script_tag = '<script is:inline define:vars={{ duoPrice: deal.priceTotalPerPerson, soloPrice, duoHotel: deal.hotel.pricePerPerson, soloHotel: deal.hotel.priceTotal }}>'
new_script_tag = '<script is:inline define:vars={{ duoPrice: deal.priceTotalPerPerson, soloPrice, duoHotel: deal.hotel.pricePerPerson, soloHotel: deal.hotel.priceTotal, dealFlightPrice: (deal.transportType === \'car\' ? 0 : deal.flight.price), dealHotelTotal: deal.hotel.priceTotal, dealNights: deal.nights }}>'

old_block = '''    // --- 🧮 CALCULATOR INTERACTIV DE BUGET ---
    let calcPax = 2;
    const baseFlight = 0;
    const dealFlightPrice = 0;
    const dealHotelTotal = {deal.hotel.priceTotal};
    const dealNights = {deal.nights};'''

new_block = '''    // --- 🧮 CALCULATOR INTERACTIV DE BUGET ---
    let calcPax = 2;'''

if old_script_tag in c:
    c = c.replace(old_script_tag, new_script_tag, 1)
    print('Replaced script tag')
else:
    print('Script tag not found')

if old_block in c:
    c = c.replace(old_block, new_block, 1)
    print('Replaced block')
else:
    print('Block not found')

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print('Written successfully')
