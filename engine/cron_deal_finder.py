"""
Cron Job / Script Automat de Scanare și Curățare Oferte — PonturiVacanțe
Poate fi rulat automat la fiecare 6 sau 12 ore.
1. Curăță ofertele expirate (unde data plecării a trecut deja)
2. Scanează zboruri noi prin Kiwi Tequila API
3. Calculează prețul per persoană și construiește pachetele
4. Salvează în deals.json și trimite automat pe Telegram
"""
import json
import os
import sys
import requests
from datetime import datetime, timedelta

# Asigurare encoding UTF-8 pentru consola Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from config import (
    TEQUILA_API_KEY, 
    ORIGIN_AIRPORTS, 
    MAX_FLIGHT_PRICE_EUR, 
    DEFAULT_DOUBLE_ROOM_NIGHT,
    TELEGRAM_BOT_TOKEN
)
from telegram_bot import trimite_alerta_telegram

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "deals.json")
TEQUILA_URL = "https://api.tequila.kiwi.com/v2/search"

# Galerie de imagini reprezentative Unsplash pe destinații populare
DESTINATION_PHOTOS = {
    "Roma": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
    "Milano": "https://images.unsplash.com/photo-1513581166391-887a96ddeafd?auto=format&fit=crop&w=1200&q=80",
    "Barcelona": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
    "Viena": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?auto=format&fit=crop&w=1200&q=80",
    "Larnaca": "https://images.unsplash.com/photo-1580835239846-5bb9ce03c8c3?auto=format&fit=crop&w=1200&q=80",
    "Malta": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?auto=format&fit=crop&w=1200&q=80",
    "Londra": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
    "Paris": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
    "Atena": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1200&q=80",
    "Bruxelles": "https://images.unsplash.com/photo-1517732306149-e8f829eb588a?auto=format&fit=crop&w=1200&q=80",
    "DEFAULT": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80"
}

COUNTRY_FLAGS = {
    "Italy": "🇮🇹", "Italia": "🇮🇹",
    "Spain": "🇪🇸", "Spania": "🇪🇸",
    "Austria": "🇦🇹",
    "Cyprus": "🇨🇾", "Cipru": "🇨🇾",
    "Malta": "🇲🇹",
    "United Kingdom": "🇬🇧",
    "France": "🇫🇷", "Franța": "🇫🇷",
    "Greece": "🇬🇷", "Grecia": "🇬🇷",
    "Belgium": "🇧🇪", "Belgia": "🇧🇪",
    "Germany": "🇩🇪", "Germania": "🇩🇪"
}

def incarca_oferte():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def salveaza_oferte(deals):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(deals, f, indent=2, ensure_ascii=False)

def curata_oferte_expirate(deals):
    """Elimină ofertele unde data de plecare a trecut."""
    azi = datetime.now().strftime("%Y-%m-%d")
    valabile = []
    expirate_count = 0
    for d in deals:
        data_plecare = d.get("departureDate", "2099-12-31")
        if data_plecare >= azi:
            valabile.append(d)
        else:
            expirate_count += 1
    if expirate_count > 0:
        print(f"[CURĂȚARE] Au fost arhivate/eliminate {expirate_count} oferte cu date depășite.")
    return valabile

def ruleaza_sincronizare_automata():
    print("=" * 60)
    print("   VACANȚEDIY — CRON SCANNER & PRUNER AUTOMAT")
    print("=" * 60)
    
    oferte = incarca_oferte()
    oferte = curata_oferte_expirate(oferte)
    
    # ID-uri și combinații existente pentru a evita duplicatele
    combinatii_existente = {
        f"{d['originCode']}-{d.get('destinationCode', d['destination'])}-{d['dates']}"
        for d in oferte
    }

    if TEQUILA_API_KEY == "DEMO_TEQUILA_KEY" or not TEQUILA_API_KEY:
        print("[INFO] Cheia Tequila API este în mod DEMO. Salvez ofertele curățate.")
        salveaza_oferte(oferte)
        print(f"[FINALIZAT] Oferte active în baza de date: {len(oferte)}")
        return

    headers = {"apikey": TEQUILA_API_KEY}
    data_start = (datetime.now() + timedelta(days=10)).strftime("%d/%m/%Y")
    data_final = (datetime.now() + timedelta(days=120)).strftime("%d/%m/%Y")
    
    oferte_noi = 0

    for aeroport in ORIGIN_AIRPORTS:
        code = aeroport["code"]
        city = aeroport["city"]
        print(f"[SCANARE] Caut zboruri ieftine din {city} ({code})...")

        params = {
            "fly_from": code,
            "fly_to": "europe",
            "date_from": data_start,
            "date_to": data_final,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 4,
            "flight_type": "round",
            "price_to": MAX_FLIGHT_PRICE_EUR,
            "curr": "EUR",
            "max_stopovers": 0,
            "limit": 8,
            "sort": "price"
        }

        try:
            r = requests.get(TEQUILA_URL, headers=headers, params=params, timeout=12)
            if r.status_code == 200:
                data = r.json().get("data", [])
                for zbor in data:
                    dest_city = zbor.get("cityTo")
                    dest_code = zbor.get("flyTo")
                    country = zbor.get("countryTo", {}).get("name", "Europa")
                    plecare = zbor.get("local_departure")[:10]
                    intoarcere = zbor.get("route", [{}])[-1].get("local_departure", "")[:10]
                    dates_str = f"{plecare} – {intoarcere}"
                    
                    cheie = f"{code}-{dest_code}-{dates_str}"
                    if cheie in combinatii_existente:
                        continue # Evită duplicatele
                    
                    pret_zbor = float(zbor.get("price", 40))
                    nopti = int(zbor.get("nightsInDest", 3))
                    cazare_total = nopti * DEFAULT_DOUBLE_ROOM_NIGHT
                    cazare_pers = cazare_total / 2
                    pret_final = round(pret_zbor + cazare_pers)
                    
                    img = DESTINATION_PHOTOS.get(dest_city, DESTINATION_PHOTOS["DEFAULT"])
                    flag = COUNTRY_FLAGS.get(country, "✈️")
                    
                    slug = f"city-break-{dest_city.lower().replace(' ', '-')}-din-{city.lower().replace(' ', '-')}-{pret_final}-euro"
                    
                    # Link Booking exact cu datele de check-in / check-out
                    booking_link = f"https://www.booking.com/searchresults.html?ss={dest_city}&checkin={plecare}&checkout={intoarcere}&group_adults=2&no_rooms=1"
                    
                    deal = {
                        "id": f"deal-{int(datetime.now().timestamp())}-{dest_code}",
                        "slug": slug,
                        "title": f"Escapadă la {dest_city} din {city}: {nopti} nopți + Zbor",
                        "destination": dest_city,
                        "country": country,
                        "flag": flag,
                        "originCity": city,
                        "originCode": code,
                        "destinationCode": dest_code,
                        "dates": dates_str,
                        "departureDate": plecare,
                        "returnDate": intoarcere,
                        "nights": nopti,
                        "category": "City Break" if nopti <= 3 else "Mare & Soare",
                        "badge": "🔥 Chilipir",
                        "image": img,
                        "priceTotalPerPerson": pret_final,
                        "discountPercent": 50,
                        "flight": {
                            "airline": zbor.get("airlines", ["LowCost"])[0],
                            "route": f"{code} – {dest_code} (Direct)",
                            "price": pret_zbor,
                            "link": zbor.get("deep_link")
                        },
                        "hotel": {
                            "name": f"Hotel 3★ central în {dest_city}",
                            "rating": 8.3,
                            "reviewsCount": 850,
                            "distance": "Zonă centrală",
                            "amenities": ["Baie privată", "WiFi Gratuit", "Aer condiționat"],
                            "priceTotal": cazare_total,
                            "pricePerPerson": cazare_pers,
                            "link": booking_link
                        },
                        "description": f"Zbor direct din {city} și cazare selectată în {dest_city} pentru un City Break fără bătăi de cap.",
                        "publishedAt": datetime.now().isoformat() + "Z"
                    }
                    
                    oferte.insert(0, deal)
                    combinatii_existente.add(cheie)
                    oferte_noi += 1
                    
                    # Notificare automată Telegram pentru oferta nouă
                    if TELEGRAM_BOT_TOKEN:
                        trimite_alerta_telegram(deal)
        except Exception as e:
            print(f"[EROARE API {code}]: {e}")

    salveaza_oferte(oferte)
    print(f"\n[SUCCES] Scanare finalizată! S-au adăugat {oferte_noi} oferte noi.")
    print(f"[TOTAL] Oferte active în site: {len(oferte)}")

if __name__ == "__main__":
    ruleaza_sincronizare_automata()
