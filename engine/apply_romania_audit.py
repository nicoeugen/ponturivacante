import json

ro_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/romania_deals.json"
with open(ro_path, "r", encoding="utf-8") as f:
    ro_deals = json.load(f)

for d in ro_deals:
    if d.get("id") == "ro-002":
        d["priceTotalPerPerson"] = 149
        d["priceRoomTotal"] = 298
        d["title"] = "Răsfăț Termal & Spa: 2 nopți la Lotus Therm 5★ cu Aquapark & Piscine Încălzite în Băile Felix"

with open(ro_path, "w", encoding="utf-8") as f:
    json.dump(ro_deals, f, indent=2, ensure_ascii=False)

print("[SUCCES] romania_deals.json actualizat cu tarifele oficiale Booking.com!")
