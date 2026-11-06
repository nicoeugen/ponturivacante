import json

cruises_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/cruises.json"
with open(cruises_path, "r", encoding="utf-8") as f:
    cruises = json.load(f)

for c in cruises:
    slug = c.get("slug")
    if "world-europa" in slug:
        c["flight"]["link"] = "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/BCN/2027-01-08/2027-01-15/2/0/0/null"
        c["cruiseDetails"]["link"] = "https://www.logitravel.com/croaziere/msc-cruises-msc-world-europa"
    elif "msc-opera" in slug:
        c["flight"]["link"] = "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-05-07&dateIn=2027-05-14&isConnectedFlight=false&isReturn=true&discount=0&originIata=OTP&destinationIata=ATH&tpAdults=2"
        c["cruiseDetails"]["link"] = "https://www.cruisedirect.com/cruise-line/msc-cruises/msc-opera"
    elif "costa-toscana" in slug:
        c["flight"]["link"] = "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/AUH/2026-12-11/2026-12-18/2/0/0/null"
        c["cruiseDetails"]["link"] = "https://www.logitravel.com/croaziere/costa-cruises-costa-toscana"
    elif "msc-euribia" in slug:
        c["flight"]["link"] = "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-05-14&dateIn=2027-05-21&isConnectedFlight=false&isReturn=true&discount=0&originIata=OTP&destinationIata=HAM&tpAdults=2"
        c["cruiseDetails"]["link"] = "https://www.cruisedirect.com/cruise-line/msc-cruises/msc-euribia"

with open(cruises_path, "w", encoding="utf-8") as f:
    json.dump(cruises, f, indent=2, ensure_ascii=False)

print("[SUCCES] cruises.json actualizat cu linkuri directe de zbor si nava!")
