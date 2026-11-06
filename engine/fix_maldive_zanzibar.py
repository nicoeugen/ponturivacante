import json, urllib.parse

deals_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json"
with open(deals_path, "r", encoding="utf-8") as f:
    deals = json.load(f)

LUNI = {
    "ianuarie": "01", "februarie": "02", "martie": "03", "aprilie": "04",
    "mai": "05", "iunie": "06", "iulie": "07", "august": "08",
    "septembrie": "09", "octombrie": "10", "noiembrie": "11", "decembrie": "12"
}

def parse_alt_date(text):
    text_clean = text.lower().replace("–", "-").replace("—", "-")
    parts = text_clean.split("-")
    if len(parts) == 2:
        day1 = parts[0].strip()
        rest = parts[1].strip().split()
        if len(rest) >= 2:
            day2 = rest[0].strip()
            luna = rest[1].strip()
            an = rest[2].strip() if len(rest) > 2 else "2027"
            m = LUNI.get(luna, "01")
            d1 = f"{int(day1):02d}"
            d2 = f"{int(day2):02d}"
            return f"{an}-{m}-{d1}", f"{an}-{m}-{d2}"
    return None, None

def get_flight_bundle(slug, airline, orig, dest, dep, ret):
    orig_u = orig.upper()
    dest_u = dest.upper()
    orig_l = orig.lower()
    dest_l = dest.lower()
    
    # 1. Google Flights cu query standard in engleza recunoscut de Google
    q_str = f"Round trip flights from {orig_u} to {dest_u} on {dep} returning {ret}"
    google_flights = f"https://www.google.com/travel/flights?q={urllib.parse.quote(q_str)}&curr=EUR&hl=ro"
    
    # 2. Momondo (format Aventurescu)
    momondo = f"https://www.momondo.ro/flight-search/{orig_u}-{dest_u}/{dep}/{ret}/2adults"
    
    # 3. Skyscanner
    dep_yy = dep[2:4] + dep[5:7] + dep[8:10]
    ret_yy = ret[2:4] + ret[5:7] + ret[8:10]
    skyscanner = f"https://www.skyscanner.ro/transport/zboruri/{orig_l}/{dest_l}/{dep_yy}/{ret_yy}/?adultsv2=2"
    
    # 4. Kiwi
    kiwi = f"https://www.kiwi.com/ro/search/results/{orig_l}/{dest_l}/{dep}/{ret}?adults=2"
    
    # 5. Link direct oficial unde e zbor direct real
    is_connecting = False
    
    if "maldive" in slug:
        is_connecting = True
        direct_link = momondo
    elif "zanzibar" in slug:
        is_connecting = True
        direct_link = momondo
    elif "madeira" in slug:
        is_connecting = True
        direct_link = momondo
    elif "hurghada" in slug:
        is_connecting = True
        direct_link = momondo
    elif "wizz" in airline.lower():
        direct_link = f"https://www.wizzair.com/ro-ro/booking/select-flight/{orig_u}/{dest_u}/{dep}/{ret}/2/0/0/null"
    elif "ryanair" in airline.lower():
        direct_link = f"https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut={dep}&dateIn={ret}&isConnectedFlight=false&isReturn=true&discount=0&originIata={orig_u}&destinationIata={dest_u}&tpAdults=2"
    elif "hisky" in airline.lower():
        direct_link = f"https://hisky.aero/ro"
    else:
        direct_link = momondo

    return {
        "primaryLink": direct_link,
        "isConnecting": is_connecting,
        "googleFlightsLink": google_flights,
        "momondoLink": momondo,
        "skyscannerLink": skyscanner,
        "kiwiLink": kiwi
    }

for deal in deals:
    slug = deal.get("slug")
    orig = deal.get("originCode", "OTP")
    dest = deal.get("destinationCode", "FCO")
    dep = deal.get("departureDate")
    ret = deal.get("returnDate")
    
    # Corectie specifica de companii pentru zboruri cu escala
    if "maldive" in slug:
        deal["flight"]["airline"] = "FlyDubai / Qatar Airways"
        deal["flight"]["route"] = "OTP – DXB / DOH – MLE (Zbor cu escală)"
        deal["flight"]["isConnecting"] = True
    elif "zanzibar" in slug:
        deal["flight"]["airline"] = "FlyDubai"
        deal["flight"]["route"] = "OTP – DXB – ZNZ (Zbor cu escală în Dubai)"
        deal["flight"]["isConnecting"] = True
    elif "madeira" in slug:
        deal["flight"]["airline"] = "Wizz Air + TAP / EasyJet"
        deal["flight"]["route"] = "OTP – LIS / BCN – FNC (Zbor cu escală)"
        deal["flight"]["isConnecting"] = True
    elif "hurghada" in slug:
        deal["flight"]["airline"] = "Pegasus Airlines / HiSky"
        deal["flight"]["route"] = "OTP – SAW – HRG (Zbor cu escală)"
        deal["flight"]["isConnecting"] = True
    else:
        deal["flight"]["isConnecting"] = False
        
    airline = deal.get("flight", {}).get("airline", "Wizz Air")
    bundle = get_flight_bundle(slug, airline, orig, dest, dep, ret)
    
    deal["flight"]["link"] = bundle["primaryLink"]
    deal["flight"]["googleFlightsLink"] = bundle["googleFlightsLink"]
    deal["flight"]["momondoLink"] = bundle["momondoLink"]
    deal["flight"]["skyscannerLink"] = bundle["skyscannerLink"]
    deal["flight"]["kiwiLink"] = bundle["kiwiLink"]
    
    # Actualizare date alternative
    if "alternativeDates" in deal:
        for alt in deal["alternativeDates"]:
            d1, d2 = parse_alt_date(alt.get("dates", ""))
            if d1 and d2:
                alt["departureDate"] = d1
                alt["returnDate"] = d2
                alt_bundle = get_flight_bundle(slug, airline, orig, dest, d1, d2)
                alt["link"] = alt_bundle["primaryLink"]
                alt["momondoLink"] = alt_bundle["momondoLink"]
                alt["googleFlightsLink"] = alt_bundle["googleFlightsLink"]
            else:
                alt["link"] = bundle["primaryLink"]

with open(deals_path, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print("[SUCCES] Am corectat Maldive, Zanzibar, Madeira și am generat linkuri valide Momondo + Google Flights + Skyscanner!")
