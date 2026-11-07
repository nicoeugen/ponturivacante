import json
import re
import urllib.parse

DEALS_PATH = r"C:\Users\Eugen\Desktop\Proiecte\website turism\data\deals.json"

with open(DEALS_PATH, "r", encoding="utf-8") as f:
    deals = json.load(f)

updated_count = 0

for deal in deals:
    hotel = deal.get("hotel", {})
    hotel_name = hotel.get("name", "")
    hname_clean = re.sub(r"\s*\d+★|\s*★|\s*⭐", "", hotel_name).strip()
    dest_clean = re.sub(r"[\(\)]", "", deal.get("destination", "")).split("&")[0].strip()
    
    agoda_query = f"{hname_clean} {dest_clean}".strip()
    encoded_agoda_query = urllib.parse.quote_plus(agoda_query)
    dep = deal.get("departureDate", "")
    ret = deal.get("returnDate", "")
    
    agoda_hotel_url = (
        f"https://www.agoda.com/ro-ro/search?text={encoded_agoda_query}"
        f"&checkIn={dep}&checkOut={ret}&rooms=1&adults=2&cid=1980047"
    )
    
    # Direct Booking URL (already fixed and canonical)
    booking_hotel_url = hotel.get("link", "")
    
    amenities = hotel.get("amenities", [])
    amenities_text = " • ".join(amenities[:2]) if amenities else "Cameră Dublă Confort"
    
    # Build the 2 prominent verified options
    agoda_option = {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "★ Partener Oficial",
        "name": hotel_name,
        "rating": hotel.get("rating", 8.6),
        "priceTotal": hotel.get("priceTotal", 150),
        "pricePerPerson": hotel.get("pricePerPerson", 75),
        "type": f"{amenities_text} (Agoda)",
        "link": agoda_hotel_url
    }
    
    booking_option = {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "Alternativă Booking.com",
        "name": hotel_name,
        "rating": hotel.get("rating", 8.6),
        "priceTotal": hotel.get("priceTotal", 150),
        "pricePerPerson": hotel.get("pricePerPerson", 75),
        "type": f"{amenities_text} (Booking)",
        "link": booking_hotel_url
    }
    
    deal["accommodationOptions"] = [agoda_option, booking_option]
    updated_count += 1

with open(DEALS_PATH, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {updated_count} deals with Active Agoda + Booking options!")
