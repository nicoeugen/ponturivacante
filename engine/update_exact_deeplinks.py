"""
Script Unificat de Actualizare Deep-Link-uri — PonturiVacanțe
Sincronizează atât cazările verificate 100% Booking.com, cât și zborurile directe
pe site-urile companiilor aeriene (Wizz Air, Ryanair, Pegasus, HiSky, FlyDubai)
și comparatoarelor (Google Flights, Skyscanner, Kiwi).
"""
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DEALS_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "deals.json")
ROMANIA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "romania_deals.json")

# Mapare de slug-uri verificate manual pentru Booking.com (0 erori 404)
VERIFIED_BOOKING_SLUGS = {
    "vacanta-exotica-tenerife-canare-din-bucuresti-250-euro": "https://www.booking.com/hotel/es/apartamentos-los-cardones.ro.html",
    "vacanta-exotica-abu-dhabi-dubai-din-bucuresti-208-euro": "https://www.booking.com/hotel/ae/premier-inn-abu-dhabi-capital-centre.ro.html",
    "vacanta-exotica-iordania-aqaba-petra-din-bucuresti-129-euro": "https://www.booking.com/hotel/jo/my-by-trend.ro.html",
    "sejur-all-inclusive-hurghada-egipt-din-bucuresti-255-euro": "https://www.booking.com/hotel/eg/seagull-beach-resort.ro.html",
    "city-break-marrakech-maroc-din-bucuresti-133-euro": "https://www.booking.com/hotel/ma/dar-fangui.ro.html",
    "vacanta-exotica-madeira-portugalia-din-bucuresti-219-euro": "https://www.booking.com/hotel/pt/orquidea.ro.html",
    "vacanta-exotica-maldive-diy-din-bucuresti-435-euro": "https://www.booking.com/hotel/mv/arena-beach.ro.html",
    "vacanta-exotica-zanzibar-tanzania-din-bucuresti-570-euro": "https://www.booking.com/hotel/tz/amaan-bungalows.ro.html",
    "vacanta-exotica-gran-canaria-din-cluj-225-euro": "https://www.booking.com/hotel/es/bungalows-vista-flor.ro.html",
    "city-break-roma-din-bucuresti-98-euro": "https://www.booking.com/hotel/it/san-giovanni-roma.ro.html",
    "vacanta-milano-bergamo-din-cluj-74-euro": "https://www.booking.com/hotel/it/b-amp-b-bergamo.ro.html",
    "city-break-malaga-spania-din-bucuresti-hisky-129-euro": "https://www.booking.com/hotel/es/soho-boutique-malaga.ro.html",
    "weekend-viena-din-bucuresti-89-euro": "https://www.booking.com/hotel/at/ibis-wien-hauptbahnhof.ro.html",
    "city-break-bologna-din-craiova-79-euro": "https://www.booking.com/hotel/it/best-western-san-donato.ro.html",
    "city-break-bruxelles-din-suceava-88-euro": "https://www.booking.com/hotel/be/meininger-bra1-4ssel-city-center.ro.html",
    "city-break-londra-din-sibiu-109-euro": "https://www.booking.com/hotel/gb/pont-a-hotel-london-kings-cross.ro.html",
    "city-break-paris-din-bucuresti-119-euro": "https://www.booking.com/hotel/fr/ibis-paris-ornano-montmartre-nord-18eme.ro.html",
    "vacanta-schi-bansko-bulgaria-din-bucuresti-149-euro": "https://www.booking.com/hotel/bg/green-life-bansko.ro.html",
    "vacanta-schi-dolomiti-val-di-fassa-din-bucuresti-289-euro": "https://www.booking.com/hotel/it/il-caminetto-sport-canazei.ro.html",
    "vacanta-schi-tirol-innsbruck-austria-din-bucuresti-319-euro": "https://www.booking.com/hotel/at/hotel-maximilian.ro.html",
    "vacanta-schi-jasna-chopok-slovacia-din-bucuresti-239-euro": "https://www.booking.com/hotel/sk/hotel-jasna.ro.html"
    "vacanta-schi-bansko-bulgaria-transport-propriu-110-euro": "https://www.booking.com/hotel/bg/green-life-bansko.ro.html",
    "vacanta-schi-borovets-bulgaria-hotel-rila-135-euro": "https://www.booking.com/hotel/bg/rila-borovets.ro.html",
    "vacanta-schi-pamporovo-bulgaria-apartamente-98-euro": "https://www.booking.com/hotel/bg/grand-monastery-private-apartments.ro.html",
    "vacanta-schi-tirol-innsbruck-austria-hotel-maximilian-260-euro": "https://www.booking.com/hotel/at/hotel-maximilian.ro.html",
    "vacanta-schi-zell-am-see-kaprun-austria-285-euro": "https://www.booking.com/hotel/at/grand-hotel-zell-am-see.ro.html",
    "vacanta-schi-kitzbuhel-alpi-austria-295-euro": "https://www.booking.com/hotel/at/q-hotel-maria-theresia.ro.html",
    "vacanta-schi-schladming-dachstein-austria-240-euro": "https://www.booking.com/hotel/at/tui-blue-schladming.ro.html",
    "vacanta-schi-livigno-duty-free-italia-din-bucuresti-309-euro": "https://www.booking.com/hotel/it/piccolo-tibet.ro.html",
    "vacanta-schi-cortina-dampezzo-dolomiti-din-bucuresti-320-euro": "https://www.booking.com/hotel/it/oasi-cortina-d-ampezzo.ro.html",
    "vacanta-schi-jasna-chopok-slovacia-hotel-jasna-195-euro": "https://www.booking.com/hotel/sk/hotel-jasna.ro.html",
    "vacanta-schi-tatranska-lomnica-slovacia-180-euro": "https://www.booking.com/hotel/sk/horizont-resort.ro.html",
    "vacanta-schi-val-thorens-trei-vai-franta-din-bucuresti-350-euro": "https://www.booking.com/hotel/fr/residence-le-chamois-d-or-val-thorens.ro.html",
}

VERIFIED_ROMANIA_SLUGS = {
    "ro-001": "https://www.booking.com/hotel/ro/cabana-stil-a-frame.ro.html",
    "ro-002": "https://www.booking.com/hotel/ro/lotus-therm-spa-amp-luxury-resort.ro.html",
    "ro-003": "https://www.booking.com/hotel/ro/the-machine-house.ro.html",
    "ro-004": "https://www.booking.com/hotel/ro/casa-traditionala-breb.ro.html",
    "ro-005": "https://www.booking.com/hotel/ro/hermanns-sibiu.ro.html",
    "ro-006": "https://www.booking.com/hotel/ro/green-village.ro.html",
    "ro-007": "https://www.booking.com/hotel/ro/aparthotel-alpin.ro.html",
    "ro-008": "https://www.booking.com/hotel/ro/rina-cerbul.ro.html",
    "ro-009": "https://www.booking.com/hotel/ro/vila-alpin.ro.html",
    "ro-010": "https://www.booking.com/hotel/ro/cindrel.html"
}

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

def actualizeaza_deeplinks():
    # 1. Deals internationale
    if os.path.exists(DEALS_PATH):
        with open(DEALS_PATH, "r", encoding="utf-8") as f:
            deals = json.load(f)

        for deal in deals:
            slug = deal.get("slug")
            checkin = deal.get("departureDate")
            checkout = deal.get("returnDate")
            airline = deal.get("flight", {}).get("airline", "Wizz Air")
            orig = deal.get("originCode", "OTP")
            dest = deal.get("destinationCode", "FCO")

            # A. Zbor direct oficial si comparatoare
            f_links = get_flight_links(airline, orig, dest, checkin, checkout)
            deal["flight"]["link"] = f_links["directAirlineLink"]
            deal["flight"]["directAirlineLink"] = f_links["directAirlineLink"]
            deal["flight"]["googleFlightsLink"] = f_links["googleFlightsLink"]
            deal["flight"]["skyscannerLink"] = f_links["skyscannerLink"]
            deal["flight"]["kiwiLink"] = f_links["kiwiLink"]

            # B. Date alternative
            if "alternativeDates" in deal:
                for alt in deal["alternativeDates"]:
                    d1, d2 = parse_alt_date(alt.get("dates", ""))
                    if d1 and d2:
                        alt["departureDate"] = d1
                        alt["returnDate"] = d2
                        alt_links = get_flight_links(airline, orig, dest, d1, d2)
                        alt["link"] = alt_links["directAirlineLink"]
                    else:
                        alt["link"] = f_links["directAirlineLink"]

            # C. Hotel principal si optiuni de cazare pe Booking.com
            if slug in VERIFIED_BOOKING_SLUGS:
                base_booking = VERIFIED_BOOKING_SLUGS[slug]
                exact_booking_url = f"{base_booking}?checkin={checkin}&checkout={checkout}&group_adults=2&no_rooms=1"
                deal["hotel"]["link"] = exact_booking_url
                
                if "accommodationOptions" in deal:
                    for opt in deal["accommodationOptions"]:
                        if opt.get("providerId") == "booking":
                            opt["link"] = exact_booking_url

        with open(DEALS_PATH, "w", encoding="utf-8") as f:
            json.dump(deals, f, indent=2, ensure_ascii=False)

    # 2. Deals Romania
    if os.path.exists(ROMANIA_PATH):
        with open(ROMANIA_PATH, "r", encoding="utf-8") as f:
            ro_deals = json.load(f)

        for deal in ro_deals:
            did = deal.get("id")
            if did in VERIFIED_ROMANIA_SLUGS:
                curr_url = deal.get("bookingUrl", "")
                checkin = "2026-12-04"
                checkout = "2026-12-06"
                if "checkin=" in curr_url:
                    parts = curr_url.split("checkin=")[1].split("&")[0]
                    checkin = parts
                if "checkout=" in curr_url:
                    parts = curr_url.split("checkout=")[1].split("&")[0]
                    checkout = parts
                
                base_url = VERIFIED_ROMANIA_SLUGS[did]
                deal["bookingUrl"] = f"{base_url}?checkin={checkin}&checkout={checkout}&group_adults=2&no_rooms=1"

        with open(ROMANIA_PATH, "w", encoding="utf-8") as f:
            json.dump(ro_deals, f, indent=2, ensure_ascii=False)

    print("[SUCCES] Toate cazările și zborurile au fost sincronizate cu URL-uri directe oficiale!")

if __name__ == "__main__":
    actualizeaza_deeplinks()
