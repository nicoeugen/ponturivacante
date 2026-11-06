import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 1. Actualizare data/deals.json
deals_path = "data/deals.json"
deals = json.load(open(deals_path, encoding="utf-8"))

slug_replacements = {
    # Bansko
    "https://www.booking.com/hotel/bg/green-life-ski-spa-resort.ro.html": "https://www.booking.com/hotel/bg/green-life-bansko.ro.html",
    # Borovets
    "https://www.booking.com/hotel/bg/rila.ro.html": "https://www.booking.com/hotel/bg/rila-borovets.ro.html",
    # Livigno
    "https://www.booking.com/hotel/it/hotel-piccolo-tibet.ro.html": "https://www.booking.com/hotel/it/piccolo-tibet.ro.html",
    # Cortina d'Ampezzo
    "https://www.booking.com/hotel/it/meuble-oasi.ro.html": "https://www.booking.com/hotel/it/oasi-cortina-d-ampezzo.ro.html",
    # Val Thorens
    "https://www.booking.com/hotel/fr/residence-le-chamois-d-or.ro.html": "https://www.booking.com/hotel/fr/residence-le-chamois-d-or-val-thorens.ro.html"
}

modified_deals = 0
for d in deals:
    # hotel link
    hl = d.get("hotel", {}).get("link", "")
    for old_url, new_url in slug_replacements.items():
        if old_url in hl:
            d["hotel"]["link"] = hl.replace(old_url, new_url)
            modified_deals += 1
            print(f"Fixed hotel.link for {d['id']}: {new_url}")
    
    # accommodationOptions links
    for opt in d.get("accommodationOptions", []):
        ol = opt.get("link", "")
        for old_url, new_url in slug_replacements.items():
            if old_url in ol:
                opt["link"] = ol.replace(old_url, new_url)
                print(f"Fixed opt.link for {d['id']}: {new_url}")

with open(deals_path, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print(f"Updated deals.json (modified {modified_deals} deals)")

# 2. Actualizare engine/update_exact_deeplinks.py
dl_path = "engine/update_exact_deeplinks.py"
dl_content = open(dl_path, "r", encoding="utf-8").read()
for old_url, new_url in slug_replacements.items():
    if old_url in dl_content:
        dl_content = dl_content.replace(old_url, new_url)
open(dl_path, "w", encoding="utf-8").write(dl_content)
print("Updated engine/update_exact_deeplinks.py")

# 3. Actualizare src/pages/go/[type].astro pentru a elimina dummy aid '000000'
go_path = "src/pages/go/[type].astro"
go_content = open(go_path, "r", encoding="utf-8").read()

go_content = go_content.replace("BOOKING_AID: '000000'", "BOOKING_AID: ''")
go_content = go_content.replace("AGODA_CID: '000000'", "AGODA_CID: ''")
go_content = go_content.replace("HOSTELWORLD_AID: '000000'", "HOSTELWORLD_AID: ''")
go_content = go_content.replace("TRAVELPAYOUTS_MARKER: '123456'", "TRAVELPAYOUTS_MARKER: ''")

# Asiguram ca se seteaza doar daca exista aid real
old_aid_code = "u.searchParams.set('aid', CONFIG.BOOKING_AID);"
new_aid_code = "if (CONFIG.BOOKING_AID && CONFIG.BOOKING_AID !== '000000') u.searchParams.set('aid', CONFIG.BOOKING_AID);"
if old_aid_code in go_content:
    go_content = go_content.replace(old_aid_code, new_aid_code)

old_marker_code = "u.searchParams.set('marker', CONFIG.TRAVELPAYOUTS_MARKER);"
new_marker_code = "if (CONFIG.TRAVELPAYOUTS_MARKER && CONFIG.TRAVELPAYOUTS_MARKER !== '123456') u.searchParams.set('marker', CONFIG.TRAVELPAYOUTS_MARKER);"
if old_marker_code in go_content:
    go_content = go_content.replace(old_marker_code, new_marker_code)

open(go_path, "w", encoding="utf-8").write(go_content)
print("Updated src/pages/go/[type].astro (removed dummy 000000 affiliate parameters)")
