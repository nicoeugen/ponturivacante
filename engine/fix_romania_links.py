import json

# Actualizare data/romania_deals.json
romania_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/romania_deals.json"
with open(romania_path, "r", encoding="utf-8") as f:
    ro_deals = json.load(f)

# Slugs oficiale verificate Booking.com
ro_slug_map = {
    "ro-001": "https://www.booking.com/hotel/ro/cabana-stil-a-frame.ro.html?checkin=2026-12-04&checkout=2026-12-06&group_adults=2&no_rooms=1",
    "ro-002": "https://www.booking.com/hotel/ro/lotus-therm-spa-amp-luxury-resort.ro.html?checkin=2026-12-11&checkout=2026-12-13&group_adults=2&no_rooms=1",
    "ro-003": "https://www.booking.com/hotel/ro/the-machine-house.ro.html?checkin=2026-12-04&checkout=2026-12-06&group_adults=2&no_rooms=1",
    "ro-004": "https://www.booking.com/hotel/ro/casa-traditionala-breb.ro.html?checkin=2026-12-10&checkout=2026-12-13&group_adults=2&no_rooms=1",
    "ro-005": "https://www.booking.com/hotel/ro/hermanns-sibiu.ro.html?checkin=2026-11-28&checkout=2026-11-30&group_adults=2&no_rooms=1",
    "ro-006": "https://www.booking.com/hotel/ro/green-village.ro.html?checkin=2027-05-14&checkout=2027-05-17&group_adults=2&no_rooms=1"
}

for deal in ro_deals:
    deal_id = deal.get("id")
    if deal_id in ro_slug_map:
        deal["bookingUrl"] = ro_slug_map[deal_id]

with open(romania_path, "w", encoding="utf-8") as f:
    json.dump(ro_deals, f, indent=2, ensure_ascii=False)

print("[SUCCES] romania_deals.json actualizat cu succes!")
