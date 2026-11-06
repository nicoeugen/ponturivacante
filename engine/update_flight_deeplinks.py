import json, re

deals_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json"
with open(deals_path, "r", encoding="utf-8") as f:
    deals = json.load(f)

# Mapare luni in romana pentru date alternative
LUNI = {
    "ianuarie": "01", "februarie": "02", "martie": "03", "aprilie": "04",
    "mai": "05", "iunie": "06", "iulie": "07", "august": "08",
    "septembrie": "09", "octombrie": "10", "noiembrie": "11", "decembrie": "12"
}

def parse_alt_date(text):
    # Ex: "22 – 29 Ianuarie 2027" -> 2027-01-22, 2027-01-29
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

def get_flight_links(airline, orig, dest, dep, ret):
    orig_u = orig.upper()
    dest_u = dest.upper()
    orig_l = orig.lower()
    dest_l = dest.lower()
    
    dep_yy = dep[2:4] + dep[5:7] + dep[8:10]
    ret_yy = ret[2:4] + ret[5:7] + ret[8:10]
    skyscanner_link = f"https://www.skyscanner.ro/transport/zboruri/{orig_l}/{dest_l}/{dep_yy}/{ret_yy}/?adultsv2=2"
    google_flights_link = f"https://www.google.com/travel/flights?q=Flights%20to%20{dest_u}%20from%20{orig_u}%20on%20{dep}%20through%20{ret}"
    kiwi_link = f"https://www.kiwi.com/ro/search/results/{orig_l}/{dest_l}/{dep}/{ret}?adults=2"
    
    airline_norm = airline.lower()
    if "wizz" in airline_norm:
        direct_link = f"https://www.wizzair.com/ro-ro/booking/select-flight/{orig_u}/{dest_u}/{dep}/{ret}/2/0/0/null"
    elif "ryanair" in airline_norm:
        direct_link = f"https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut={dep}&dateIn={ret}&isConnectedFlight=false&isReturn=true&discount=0&originIata={orig_u}&destinationIata={dest_u}&tpAdults=2"
    elif "pegasus" in airline_norm:
        direct_link = f"https://web.flypgs.com/booking?from={orig_u}&to={dest_u}&date={dep}&returnDate={ret}&adult=2"
    elif "hisky" in airline_norm:
        direct_link = f"https://www.google.com/travel/flights?q=Zboruri%20HiSky%20de%20la%20{orig_u}%20la%20{dest_u}%20din%20{dep}%20pana%20in%20{ret}"
    elif "flydubai" in airline_norm:
        direct_link = f"https://www.google.com/travel/flights?q=Zboruri%20FlyDubai%20de%20la%20{orig_u}%20la%20{dest_u}%20din%20{dep}%20pana%20in%20{ret}"
    else:
        direct_link = google_flights_link
        
    return {
        "directAirlineLink": direct_link,
        "googleFlightsLink": google_flights_link,
        "skyscannerLink": skyscanner_link,
        "kiwiLink": kiwi_link
    }

for deal in deals:
    airline = deal.get("flight", {}).get("airline", "Wizz Air")
    orig = deal.get("originCode", "OTP")
    dest = deal.get("destinationCode", "FCO")
    dep = deal.get("departureDate")
    ret = deal.get("returnDate")
    
    links = get_flight_links(airline, orig, dest, dep, ret)
    
    # Set direct airline link as default
    deal["flight"]["link"] = links["directAirlineLink"]
    deal["flight"]["directAirlineLink"] = links["directAirlineLink"]
    deal["flight"]["googleFlightsLink"] = links["googleFlightsLink"]
    deal["flight"]["skyscannerLink"] = links["skyscannerLink"]
    deal["flight"]["kiwiLink"] = links["kiwiLink"]
    
    # Process alternative dates
    if "alternativeDates" in deal:
        for alt in deal["alternativeDates"]:
            d1, d2 = parse_alt_date(alt.get("dates", ""))
            if d1 and d2:
                alt["departureDate"] = d1
                alt["returnDate"] = d2
                alt_links = get_flight_links(airline, orig, dest, d1, d2)
                alt["link"] = alt_links["directAirlineLink"]
            else:
                alt["link"] = links["directAirlineLink"]

with open(deals_path, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print(f"[SUCCES] Am actualizat zborurile pentru toate cele {len(deals)} oferte cu linkuri directe catre companiile aeriene oficiale si comparatoare!")
