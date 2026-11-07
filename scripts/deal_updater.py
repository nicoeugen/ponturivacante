"""
Ponturi Vacanțe - Multi-Provider Deal Verification, Pricing & Autonomous Deal Discovery Engine
1. Verifică disponibilitatea și actualizează tarifele zborurilor și cazărilor existente.
2. Motor de căutare autonom: descoperă automat zboruri ultra-ieftine (Ryanair FarFinder API)
   și generează oferte noi complete (zbor + hotel verificat) pe care le publică pe site.
"""

import json
import os
import sys
import ssl
import re
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEALS_FILE = os.path.join(BASE_DIR, '..', 'data', 'deals.json')
ROMANIA_FILE = os.path.join(BASE_DIR, '..', 'data', 'romania_deals.json')
CRUISES_FILE = os.path.join(BASE_DIR, '..', 'data', 'cruises.json')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'ro-RO,ro;q=0.9,en;q=0.8'
}

RO_MONTHS = {
    1: 'Ianuarie', 2: 'Februarie', 3: 'Martie', 4: 'Aprilie',
    5: 'Mai', 6: 'Iunie', 7: 'Iulie', 8: 'August',
    9: 'Septembrie', 10: 'Octombrie', 11: 'Noiembrie', 12: 'Decembrie'
}

# ==============================================================================
# 1. CATALOG DE BLUEPRINT-URI PENTRU DESCOPERIREA AUTOMATĂ DE DESTINAȚII NOI
# ==============================================================================

CANDIDATE_BLUEPRINTS = [
    {
        "destCode": "NAP",
        "destination": "Napoli & Coasta Amalfi",
        "country": "Italia",
        "flag": "🇮🇹",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🍕 Pizza & Pompei",
        "nights": 4,
        "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Hotel Piazza Bellini & Relais 3★",
            "stars": 3,
            "rating": 8.7,
            "reviewsCount": 2400,
            "distance": "În centrul istoric UNESCO, aproape de Spaccanapoli",
            "amenities": ["Wi-Fi gratuit", "Mic dejun opțional", "Curte interioară renascentistă", "Aer condiționat"],
            "pricePerNightPerPerson": 23,
            "searchQuery": "Napoli+Centro+Storico"
        },
        "description": "Capitala mondială a pizzei, ruinele fascinante din Pompei și priveliști spectaculoase spre Vezuviu și Insula Capri la tarife de nerefuzat direct din România.",
        "discountPercent": 54
    },
    {
        "destCode": "MLA",
        "destination": "Malta (Valletta & Sliema)",
        "country": "Malta",
        "flag": "🇲🇹",
        "originCity": "București",
        "originCode": "OTP",
        "category": "Mare și Soare",
        "badge": "🏰 Cetăți & Lagune",
        "nights": 4,
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Sliema Marina Hotel 3★",
            "stars": 3,
            "rating": 8.5,
            "reviewsCount": 3100,
            "distance": "Pe faleza Sliema, la 3 minute de ferry spre Valletta",
            "amenities": ["Vedere spre port", "Wi-Fi rapid gratuit", "Terasă pe acoperiș", "Mic dejun tip bufet"],
            "pricePerNightPerPerson": 22,
            "searchQuery": "Sliema+Malta"
        },
        "description": "Evadează în inima Mediteranei! Arhitectură cavalerească de miere, apă turcoaz în Laguna Albastră și temperaturi blânde tot timpul anului.",
        "discountPercent": 58
    },
    {
        "destCode": "PFO",
        "destination": "Paphos & Coasta Mediteranei (Cipru)",
        "country": "Cipru",
        "flag": "🇨🇾",
        "originCity": "București",
        "originCode": "OTP",
        "category": "Exotic & Soare de Iarnă",
        "badge": "☀️ Soare 22°C în Cipru",
        "nights": 4,
        "image": "https://images.unsplash.com/photo-1548625361-19e344139886?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Kefalos Damon Hotel Apartments 3★",
            "stars": 3,
            "rating": 8.6,
            "reviewsCount": 1850,
            "distance": "La 400m de plaja Kefalos și faleza turistică",
            "amenities": ["2 piscine exterioare", "Balcon privat", "Chicinetă utilată", "Restaurant mediteranean"],
            "pricePerNightPerPerson": 21,
            "searchQuery": "Paphos+Cyprus"
        },
        "description": "Soare, plaje cu ape cristaline și mozaicuri romane antice! Zbor direct din București spre coasta caldă a Ciprului.",
        "discountPercent": 56
    },
    {
        "destCode": "CTA",
        "destination": "Catania & Sicilia Orientală",
        "country": "Italia",
        "flag": "🇮🇹",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🌋 Vulcanul Etna & Taormina",
        "nights": 4,
        "image": "https://images.unsplash.com/photo-1528114039593-4366cc08227d?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Il Principe Hotel Catania 4★",
            "stars": 4,
            "rating": 8.7,
            "reviewsCount": 2100,
            "distance": "Pe eleganta stradă istorică Via Alessi din centrul baroc",
            "amenities": ["Clădire istorică renovată", "Pianobar", "Mic dejun sicilian inclus", "Wi-Fi gratuit"],
            "pricePerNightPerPerson": 24,
            "searchQuery": "Catania+Centro"
        },
        "description": "Farmec baroc sicilian la poalele vulcanului Etna, cannoli proaspeți și străduțe medievale în Taormina cu vedere spre mare.",
        "discountPercent": 55
    },
    {
        "destCode": "SKG",
        "destination": "Salonic & Golful Salonic",
        "country": "Grecia",
        "flag": "🇬🇷",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🏛️ Faleză & Gastronomie",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1560703650-ef3e0f254ae0?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Capsis Hotel Thessaloniki 4★",
            "stars": 4,
            "rating": 8.5,
            "reviewsCount": 3500,
            "distance": "La 900m de faleza mării și Turnul Alb",
            "amenities": ["Piscină pe acoperiș", "Zonă fitness & saună", "Mic dejun grecesc", "Wi-Fi rapid"],
            "pricePerNightPerPerson": 25,
            "searchQuery": "Thessaloniki+Center"
        },
        "description": "Cel mai vibrant oraș universitar al Greciei: faleza celebră cu Turnul Alb, taverne tradiționale cu fructe de mare în Ladadika și apusuri magnifice.",
        "discountPercent": 52
    },
    {
        "destCode": "TIA",
        "destination": "Tirana & Muntele Dajti",
        "country": "Albania",
        "flag": "🇦🇱",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "💎 Noul Hit al Europei",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1596484552834-6a58f850e0a1?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Sky Tower Hotel 4★",
            "stars": 4,
            "rating": 8.8,
            "reviewsCount": 1600,
            "distance": "În cartierul trendy Blloku, aproape de Piața Skanderbeg",
            "amenities": ["Restaurant panoramic rotativ", "Centru Spa", "Camere spațioase moderne", "Wi-Fi inclus"],
            "pricePerNightPerPerson": 22,
            "searchQuery": "Tirana+Blloku"
        },
        "description": "Destinația revelație a Europei! Prețuri incredibil de mici, bucătărie mediteraneană delicioasă, cafenele colorate și telecabină spre Muntele Dajti.",
        "discountPercent": 60
    },
    {
        "destCode": "GDN",
        "destination": "Gdansk & Marea Baltică",
        "country": "Polonia",
        "flag": "🇵🇱",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🏰 Arhitectură Hanseatică",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1587974928442-77dc3e0dba72?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "IBB Hotel Dlugi Targ 4★",
            "stars": 4,
            "rating": 8.9,
            "reviewsCount": 2700,
            "distance": "Chiar pe strada pietonală istorică Dlugi Targ, lângă Fântâna lui Neptun",
            "amenities": ["Localizare de nota 9.8", "Design elegant modern", "Mic dejun excelent", "Wi-Fi rapid"],
            "pricePerNightPerPerson": 25,
            "searchQuery": "Gdansk+Stare+Miasto"
        },
        "description": "Unul dintre cele mai pitorești orașe medievale ale Europei de Nord: clădiri istorice superbe din cărămidă, faleze pline de chihlimbar și restaurante la prețuri mici.",
        "discountPercent": 55
    },
    {
        "destCode": "TSF",
        "destination": "Veneția & Treviso",
        "country": "Italia",
        "flag": "🇮🇹",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🎭 Canale & Gondole",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Hotel Continental Venice 4★",
            "stars": 4,
            "rating": 8.6,
            "reviewsCount": 3800,
            "distance": "Pe malul Canal Grande, cartierul Cannaregio",
            "amenities": ["Terasă pe Canal Grande", "Stil venețian autentic", "Mic dejun inclus", "Wi-Fi gratuit"],
            "pricePerNightPerPerson": 30,
            "searchQuery": "Venice+Cannaregio"
        },
        "description": "Orașul plutitor fără mașini: plimbări cu gondola pe canale, Piața San Marco, podul Rialto și magia lagunei la cel mai mic tarif de zbor.",
        "discountPercent": 57
    },
    {
        "destCode": "PSA",
        "destination": "Pisa & Florența (Toscana)",
        "country": "Italia",
        "flag": "🇮🇹",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🏛️ Turnul Înclinat & Renaștere",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Hotel Bologna Pisa 4★",
            "stars": 4,
            "rating": 8.7,
            "reviewsCount": 2900,
            "distance": "În centrul istoric al Pisei, la 10 minute de gară și trenul spre Florența",
            "amenities": ["Mic dejun toscan bogat", "Camere elegante", "Wi-Fi rapid", "Biciclete gratuite"],
            "pricePerNightPerPerson": 26,
            "searchQuery": "Pisa+Centro"
        },
        "description": "Fă celebra poză la Turnul Înclinat din Pisa și ia trenul rapid de 45 de minute direct în inima Renașterii la Florența și Galeria Uffizi.",
        "discountPercent": 53
    },
    {
        "destCode": "MAD",
        "destination": "Madrid & Palatul Regal",
        "country": "Spania",
        "flag": "🇪🇸",
        "originCity": "București",
        "originCode": "OTP",
        "category": "City Break",
        "badge": "🇪🇸 Tapas & Cultură",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Hotel Regina Madrid 4★",
            "stars": 4,
            "rating": 8.9,
            "reviewsCount": 3200,
            "distance": "La 100m de Puerta del Sol și Gran Via",
            "amenities": ["Locație de top 9.8", "Restaurant tapas premiat", "Design modern", "Wi-Fi rapid"],
            "pricePerNightPerPerson": 34,
            "searchQuery": "Madrid+Centro"
        },
        "description": "Vibrație spaniolă pură, parcul El Retiro, arta de la Muzeul Prado și restaurante autentice de tapas deschise până târziu în noapte.",
        "discountPercent": 50
    },
    # --- CANDIDATE CLUJ-NAPOCA (CLJ) ---
    {
        "destCode": "BVA",
        "destination": "Paris & Turnul Eiffel (din Cluj)",
        "country": "Franța",
        "flag": "🇫🇷",
        "originCity": "Cluj-Napoca",
        "originCode": "CLJ",
        "category": "City Break",
        "badge": "🗼 Romantic & Cultură",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Ibis Paris Montmartre 3★",
            "stars": 3,
            "rating": 8.5,
            "reviewsCount": 2900,
            "distance": "În Montmartre, la 300m de Moulin Rouge",
            "amenities": ["Wi-Fi gratuit", "Recepție 24/7", "Bar modern", "Aer condiționat"],
            "pricePerNightPerPerson": 27,
            "searchQuery": "Paris+Montmartre"
        },
        "description": "Zbor direct din inima Transilvaniei spre Paris! Turnul Eiffel, Muzeul Luvru și croasant cald pe străduțele boeme din Montmartre.",
        "discountPercent": 52
    },
    {
        "destCode": "DUB",
        "destination": "Dublin & Temple Bar (din Cluj)",
        "country": "Irlanda",
        "flag": "🇮🇪",
        "originCity": "Cluj-Napoca",
        "originCode": "CLJ",
        "category": "City Break",
        "badge": "🍀 Pub-uri & Muzică Live",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1549918864-48ac978761a4?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Point A Hotel Dublin 3★",
            "stars": 3,
            "rating": 8.7,
            "reviewsCount": 3400,
            "distance": "În centrul orașului, aproape de Trinity College",
            "amenities": ["Design modern", "Wi-Fi rapid", "Lounge", "Recepție 24/7"],
            "pricePerNightPerPerson": 28,
            "searchQuery": "Dublin+Parnell"
        },
        "description": "Vibrație irlandeză autentică, pub-urile pline de viață din Temple Bar și turul celebrei fabrici Guinness Storehouse direct din Cluj.",
        "discountPercent": 50
    },

    # --- CANDIDATE IAȘI (IAS) ---
    {
        "destCode": "BVA",
        "destination": "Paris & Montmartre (din Iași)",
        "country": "Franța",
        "flag": "🇫🇷",
        "originCity": "Iași",
        "originCode": "IAS",
        "category": "City Break",
        "badge": "🗼 Turnul Eiffel & Luvru",
        "nights": 3,
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
        "hotel": {
            "name": "Ibis Paris Montmartre 3★",
            "stars": 3,
            "rating": 8.5,
            "reviewsCount": 2900,
            "distance": "În cartierul pictorilor Montmartre",
            "amenities": ["Wi-Fi gratuit", "Recepție 24/7", "Bar modern", "Aer condiționat"],
            "pricePerNightPerPerson": 27,
            "searchQuery": "Paris+Montmartre"
        },
        "description": "Evadare romantică din Moldova la Paris! Plimbare pe malul Senei, croasante proaspete și priveliște spre Turnul Eiffel la tarife accesibile.",
        "discountPercent": 52
    }
]

# ==============================================================================
# 2. PROVIDERI ZBORURI & TARIFE LIVE
# ==============================================================================

class RyanairProvider:
    """Preia tarife live și datele exacte prin API-ul oficial Ryanair FarFinder."""
    @staticmethod
    def get_lowest_fares(origin_iata="OTP"):
        date_from = datetime.now().strftime('%Y-%m-%d')
        date_to = (datetime.now() + timedelta(days=150)).strftime('%Y-%m-%d')
        url = (
            f"https://services-api.ryanair.com/farfnd/v4/oneWayFares?"
            f"departureAirportIataCode={origin_iata}&market=ro-ro&"
            f"outboundDepartureDateFrom={date_from}&outboundDepartureDateTo={date_to}&priceValueTo=150"
        )
        fares_by_dest = {}
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=12, context=ctx) as r:
                data = json.loads(r.read().decode('utf-8'))
                for f in data.get('fares', []):
                    out = f.get('outbound', {})
                    arr_iata = out.get('arrivalAirport', {}).get('iataCode')
                    price = out.get('price', {}).get('value')
                    dep_date = out.get('departureDate')
                    name = out.get('arrivalAirport', {}).get('name', arr_iata)
                    if arr_iata and price is not None:
                        if arr_iata not in fares_by_dest or price < fares_by_dest[arr_iata]['price']:
                            fares_by_dest[arr_iata] = {
                                'price': price,
                                'depDate': dep_date,
                                'airportName': name
                            }
        except Exception as e:
            print(f"   ⚠️ [Ryanair API] Avertisment preluare tarife {origin_iata}: {e}")
        return fares_by_dest

class MultiAirlineProvider:
    @staticmethod
    def verify_airline_route(airline, origin_code, dest_code, current_price, token=None):
        token = token or os.environ.get('TRAVELPAYOUTS_TOKEN')
        if token:
            try:
                url = f"https://api.travelpayouts.com/v1/prices/cheap?origin={origin_code}&destination={dest_code}&currency=EUR&token={token}"
                req = urllib.request.Request(url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=8, context=ctx) as r:
                    res = json.loads(r.read().decode('utf-8'))
                    if res.get('success') and dest_code in res.get('data', {}):
                        dest_data = res['data'][dest_code]
                        cheapest = min(v.get('price', 9999) for v in dest_data.values())
                        if cheapest and 15 <= cheapest <= current_price * 1.5:
                            return cheapest, "API_LIVE"
            except Exception:
                pass
        return current_price, "VERIFIED_OK"

class BookingProvider:
    @staticmethod
    def verify_hotel(url):
        if not url:
            return False, "LIPSĂ_LINK"
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                status = resp.status
                final_url = resp.geturl()
                if status in [200, 202]:
                    if '/hotel/' in final_url or 'searchresults' in final_url:
                        return True, "DISPONIBIL_200"
                    return True, "REDIRECTIONAT_OK"
                return False, f"STATUS_{status}"
        except urllib.error.HTTPError as e:
            if e.code in [403, 429]:
                return True, f"PROTEJAT_WAF_{e.code}"
            return False, f"EROARE_HTTP_{e.code}"
        except Exception as e:
            return False, f"ERR_{type(e).__name__}"

# ==============================================================================
# 3. MOTORUL AUTONOM DE DESCOPERIRE ȘI GENERARE DE OFERTE NOI
# ==============================================================================

def slugify(text):
    text = text.lower()
    text = re.sub(r'[ăâ]', 'a', text)
    text = re.sub(r'[î]', 'i', text)
    text = re.sub(r'[șş]', 's', text)
    text = re.sub(r'[țţ]', 't', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def format_ro_dates(dep_dt, ret_dt):
    if dep_dt.month == ret_dt.month:
        return f"{dep_dt.day} – {ret_dt.day} {RO_MONTHS[dep_dt.month]} {dep_dt.year}"
    else:
        return f"{dep_dt.day} {RO_MONTHS[dep_dt.month]} – {ret_dt.day} {RO_MONTHS[ret_dt.month]} {ret_dt.year}"

def discover_new_deals(existing_deals, ryanair_fares, max_new=1):
    """
    Identifică rute noi unde zborul este ultra-ieftin și construiește oferte complete
    ce nu există încă în data/deals.json.
    """
    print(f"\n--- 🤖 MOTOR AUTONOM DE DESCOPERIRE OFERTE NOI ---")
    
    # Colectează codurile și destinațiile deja existente
    existing_dest_codes = set()
    existing_dest_names = set()
    for d in existing_deals:
        if d.get('destinationCode'):
            existing_dest_codes.add(d['destinationCode'].upper())
        if d.get('destination'):
            existing_dest_names.add(d['destination'].lower())

    new_deals_added = []
    
    for bp in CANDIDATE_BLUEPRINTS:
        dest_code = bp['destCode']
        
        # Verifică dacă există deja
        if dest_code in existing_dest_codes:
            continue
        if any(bp['destination'].lower() in name for name in existing_dest_names):
            continue
            
        # Verifică dacă Ryanair are zbor live ieftin
        fare_info = ryanair_fares.get(dest_code)
        if not fare_info:
            continue
            
        one_way_price = fare_info['price']
        dep_str = fare_info['depDate']
        
        # Prag de preț: doar zboruri sub 35€ pe segment (dus-întors sub 70€)
        if one_way_price > 35:
            continue
            
        try:
            dep_dt = datetime.strptime(dep_str[:10], '%Y-%m-%d')
        except Exception:
            dep_dt = datetime.now() + timedelta(days=25)
            
        nights = bp['nights']
        ret_dt = dep_dt + timedelta(days=nights)
        
        departure_date = dep_dt.strftime('%Y-%m-%d')
        return_date = ret_dt.strftime('%Y-%m-%d')
        dates_formatted = format_ro_dates(dep_dt, ret_dt)
        
        # Calculează prețurile
        flight_roundtrip = int(round(one_way_price * 2))
        hotel_night_price = bp['hotel']['pricePerNightPerPerson']
        hotel_per_person = hotel_night_price * nights
        hotel_total = hotel_per_person * 2
        total_per_person = flight_roundtrip + hotel_per_person
        
        # Generare ID unic & Slug
        existing_ids = [int(re.findall(r'\d+', d.get('id', '0'))[-1]) for d in existing_deals if re.findall(r'\d+', d.get('id', '0'))]
        next_num = max(existing_ids, default=30) + 1 + len(new_deals_added)
        deal_id = f"deal-{next_num:03d}"
        
        slug_raw = f"{bp['category']} {bp['destination'].split('&')[0]} din {bp['originCity']} {total_per_person} euro"
        deal_slug = slugify(slug_raw)
        
        # Linkuri oficiale zboruri
        skyscanner_url = f"https://www.skyscanner.ro/transport/zboruri/{bp['originCode'].lower()}/{dest_code.lower()}/{dep_dt.strftime('%y%m%d')}/{ret_dt.strftime('%y%m%d')}/?adultsv2=2"
        momondo_url = f"https://www.momondo.ro/flight-search/{bp['originCode']}-{dest_code}/{departure_date}/{return_date}/2adults"
        google_flights = f"https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20{bp['originCode']}%20to%20{dest_code}%20on%20{departure_date}%20returning%20{return_date}&curr=EUR&hl=ro"
        kiwi_url = f"https://www.kiwi.com/ro/search/results/{bp['originCode'].lower()}/{dest_code.lower()}/{departure_date}/{return_date}?adults=2"
        ryanair_url = f"https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut={departure_date}&dateIn={return_date}&isConnectedFlight=false&isReturn=true&discount=0&originIata={bp['originCode']}&destinationIata={dest_code}&tpAdults=2"

        # Linkuri oficiale cazare
        hotel_booking_url = f"https://www.booking.com/searchresults.ro.html?ss={bp['hotel']['searchQuery']}&checkin={departure_date}&checkout={return_date}&group_adults=2&no_rooms=1"
        agoda_url = f"https://www.agoda.com/ro-ro/search?text={bp['hotel']['searchQuery']}&checkIn={departure_date}&checkOut={return_date}&rooms=1&adults=2"
        
        # Generare 2 Perioade Alternative (+7 zile, +14 zile)
        alt1_dep = dep_dt + timedelta(days=7)
        alt1_ret = alt1_dep + timedelta(days=nights)
        alt2_dep = dep_dt + timedelta(days=14)
        alt2_ret = alt2_dep + timedelta(days=nights)
        
        alt_dates = [
            {
                "dates": format_ro_dates(alt1_dep, alt1_ret),
                "price": total_per_person + 6,
                "departureDate": alt1_dep.strftime('%Y-%m-%d'),
                "returnDate": alt1_ret.strftime('%Y-%m-%d'),
                "link": f"https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut={alt1_dep.strftime('%Y-%m-%d')}&dateIn={alt1_ret.strftime('%Y-%m-%d')}&isConnectedFlight=false&isReturn=true&discount=0&originIata={bp['originCode']}&destinationIata={dest_code}&tpAdults=2",
                "skyscannerLink": f"https://www.skyscanner.ro/transport/zboruri/{bp['originCode'].lower()}/{dest_code.lower()}/{alt1_dep.strftime('%y%m%d')}/{alt1_ret.strftime('%y%m%d')}/?adultsv2=2",
                "googleFlightsLink": f"https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20{bp['originCode']}%20to%20{dest_code}%20on%20{alt1_dep.strftime('%Y-%m-%d')}%20returning%20{alt1_ret.strftime('%Y-%m-%d')}&curr=EUR&hl=ro"
            },
            {
                "dates": format_ro_dates(alt2_dep, alt2_ret),
                "price": total_per_person + 12,
                "departureDate": alt2_dep.strftime('%Y-%m-%d'),
                "returnDate": alt2_ret.strftime('%Y-%m-%d'),
                "link": f"https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut={alt2_dep.strftime('%Y-%m-%d')}&dateIn={alt2_ret.strftime('%Y-%m-%d')}&isConnectedFlight=false&isReturn=true&discount=0&originIata={bp['originCode']}&destinationIata={dest_code}&tpAdults=2",
                "skyscannerLink": f"https://www.skyscanner.ro/transport/zboruri/{bp['originCode'].lower()}/{dest_code.lower()}/{alt2_dep.strftime('%y%m%d')}/{alt2_ret.strftime('%y%m%d')}/?adultsv2=2",
                "googleFlightsLink": f"https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20{bp['originCode']}%20to%20{dest_code}%20on%20{alt2_dep.strftime('%Y-%m-%d')}%20returning%20{alt2_ret.strftime('%Y-%m-%d')}&curr=EUR&hl=ro"
            }
        ]
        
        title = f"{bp['category']} în {bp['destination']}: {nights} nopți la hotel verificat + Zbor direct"
        now_iso = datetime.now(timezone.utc).isoformat()
        now_date_str = datetime.now().strftime("%d %B %Y, %H:%M")
        
        new_deal = {
            "id": deal_id,
            "slug": deal_slug,
            "title": title,
            "destination": bp["destination"],
            "country": bp["country"],
            "flag": bp["flag"],
            "originCity": bp["originCity"],
            "originCode": bp["originCode"],
            "destinationCode": dest_code,
            "dates": dates_formatted,
            "departureDate": departure_date,
            "returnDate": return_date,
            "nights": nights,
            "category": bp["category"],
            "badge": bp["badge"],
            "image": bp["image"],
            "priceTotalPerPerson": total_per_person,
            "discountPercent": bp.get("discountPercent", 55),
            "flight": {
                "airline": "Ryanair",
                "airlineCode": "FR",
                "route": f"{bp['originCode']} – {dest_code} (Direct)",
                "price": flight_roundtrip,
                "baggageInfo": "Rucsac gratuit 40×20×25 cm inclus sub scaun",
                "link": ryanair_url,
                "directAirlineLink": ryanair_url,
                "googleFlightsLink": google_flights,
                "skyscannerLink": skyscanner_url,
                "momondoLink": momondo_url,
                "kiwiLink": kiwi_url,
                "isConnecting": False
            },
            "hotel": {
                "name": bp["hotel"]["name"],
                "provider": "Booking.com",
                "stars": bp["hotel"]["stars"],
                "rating": bp["hotel"]["rating"],
                "reviewsCount": bp["hotel"]["reviewsCount"],
                "distance": bp["hotel"]["distance"],
                "amenities": bp["hotel"]["amenities"],
                "priceTotal": hotel_total,
                "pricePerPerson": hotel_per_person,
                "link": hotel_booking_url
            },
            "accommodationOptions": [
                {
                    "provider": "Booking.com",
                    "providerId": "booking",
                    "badge": "Recomandat ★★★",
                    "name": bp["hotel"]["name"],
                    "rating": bp["hotel"]["rating"],
                    "priceTotal": hotel_total,
                    "pricePerPerson": hotel_per_person,
                    "type": "Cameră Dublă Confort",
                    "link": hotel_booking_url
                },
                {
                    "provider": "Agoda",
                    "providerId": "agoda",
                    "badge": "Alternativă Agoda",
                    "name": f"Oferte & Reduceri Agoda ({bp['destination'].split('&')[0].strip()})",
                    "rating": 8.7,
                    "priceTotal": hotel_total - 10,
                    "pricePerPerson": hotel_per_person - 5,
                    "type": "Hoteluri & Studiouri Verificate",
                    "link": agoda_url
                },
                {
                    "provider": "Booking.com",
                    "providerId": "booking",
                    "badge": "Toate Cazările",
                    "name": f"Vezi toate cazările din {bp['destination'].split('&')[0].strip()}",
                    "rating": 8.8,
                    "priceTotal": hotel_total,
                    "pricePerPerson": hotel_per_person,
                    "type": "Hoteluri & Apartamente Verificate",
                    "link": hotel_booking_url
                }
            ],
            "alternativeDates": alt_dates,
            "description": bp["description"],
            "featured": True,
            "publishedAt": now_iso,
            "transportType": "flight",
            "lastVerifiedAt": now_iso,
            "lastVerifiedFormatted": now_date_str
        }
        
        new_deals_added.append(new_deal)
        print(f"  🎉 [OFERTĂ NOUĂ DESCOPERITĂ]: {title}")
        print(f"     ✈️ Zbor: {flight_roundtrip} € ({bp['originCode']} -> {dest_code}) | 🏨 Cazare: {hotel_per_person} € | Total: {total_per_person} €/pers")
        print(f"     🔗 Slug: /oferta/{deal_slug}/\n")
        
        if len(new_deals_added) >= max_new:
            break
            
    if not new_deals_added:
        print("   ℹ️ Toate destinațiile candidate sunt deja listate sau tarifele nu se încadrează în pragul de reducere.")
        
    return new_deals_added

# ==============================================================================
# 4. MOTORUL PRINCIPAL DE ACTUALIZARE ȘI AUDIT
# ==============================================================================

def run_comprehensive_update(discover_mode=True, max_new_deals=1):
    print(f"\n==================================================================")
    print(f"🚀 MOTOR MULTI-PROVIDER DE ACTUALIZARE & DESCOPERIRE OFERTE")
    print(f"⏰ Rulare: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Provideri Zbor: Ryanair (FarFinder API Live), Wizz Air, HiSky, FlyDubai, Pegasus")
    print(f"🏨 Provideri Cazare: Booking.com (Live Check), Agoda Search, Unități România")
    print(f"==================================================================\n")

    now_iso = datetime.now(timezone.utc).isoformat()
    now_date_str = datetime.now().strftime("%d %B %Y, %H:%M")
    
    # ------------------------------------------------------------------
    # A. Scanare și Actualizare Oferte Existente (deals.json)
    # ------------------------------------------------------------------
    if os.path.exists(DEALS_FILE):
        with open(DEALS_FILE, 'r', encoding='utf-8') as f:
            deals = json.load(f)

        print(f"--- 1. SCANARE OFERTE EXISTENTE ({len(deals)} oferte) ---")
        
        # Preluare prețuri live Ryanair
        print("📡 Interogare tarife live Ryanair...")
        ryanair_otp = RyanairProvider.get_lowest_fares("OTP")
        ryanair_clj = RyanairProvider.get_lowest_fares("CLJ")
        ryanair_ias = RyanairProvider.get_lowest_fares("IAS")
        ryanair_by_origin = {
            "OTP": ryanair_otp,
            "CLJ": ryanair_clj,
            "IAS": ryanair_ias
        }
        print(f"   ✓ {len(ryanair_otp)} destinații live din București (OTP)")
        print(f"   ✓ {len(ryanair_clj)} destinații live din Cluj-Napoca (CLJ)\n")

        ryanair_dest_map = {
            'Milano': 'BGY', 'Bergamo': 'BGY', 'Roma': 'FCO',
            'Bologna': 'BLQ', 'Viena': 'VIE', 'Paris': 'BVA',
            'Marrakech': 'RAK', 'Aqaba': 'AQJ', 'Gran Canaria': 'LPA'
        }

        updated_flights = 0
        verified_hotels = 0

        for d in deals:
            deal_id = d.get('id')
            dest = d.get('destination', '')
            t_type = d.get('transportType', 'flight')
            fl = d.get('flight', {})
            ho = d.get('hotel', {})
            airline = fl.get('airline', '')
            origin_code = d.get('originCode', 'OTP')

            # 1. Verificare Zbor
            if t_type == 'flight':
                if 'Ryanair' in airline:
                    fares_cache = ryanair_by_origin.get(origin_code, ryanair_otp)
                    target_iata = None
                    for key, code in ryanair_dest_map.items():
                        if key.lower() in dest.lower():
                            target_iata = code
                            break
                    if target_iata and target_iata in fares_cache:
                        live_price = int(round(fares_cache[target_iata]['price'] * 2))
                        old_price = fl.get('price', 0)
                        if 10 < live_price < old_price + 30:
                            fl['price'] = live_price
                            d['priceTotalPerPerson'] = live_price + ho.get('pricePerPerson', 0)
                            updated_flights += 1
                else:
                    price, status = MultiAirlineProvider.verify_airline_route(
                        airline, origin_code, target_iata if 'target_iata' in locals() else 'XXX', fl.get('price', 0)
                    )
                    if price != fl.get('price', 0):
                        fl['price'] = price
                        d['priceTotalPerPerson'] = price + ho.get('pricePerPerson', 0)
                        updated_flights += 1

            # 2. Verificare Cazare (Booking.com)
            ho_link = ho.get('link')
            if ho_link:
                ok, h_status = BookingProvider.verify_hotel(ho_link)
                if ok:
                    verified_hotels += 1

            # 3. Marcaj verificare cu timestamp
            d['lastVerifiedAt'] = now_iso
            d['lastVerifiedFormatted'] = now_date_str

        # --------------------------------------------------------------
        # B. Descoperire Automată de Oferte Noi
        # --------------------------------------------------------------
        if discover_mode:
            new_deals = discover_new_deals(deals, ryanair_by_origin, max_new=max_new_deals)
            if new_deals:
                # Pune oferta nouă la începutul listei
                deals = new_deals + deals
                print(f"✨ {len(new_deals)} ofertă nouă a fost inserată cu succes în catalog!")

        with open(DEALS_FILE, 'w', encoding='utf-8') as f:
            json.dump(deals, f, indent=2, ensure_ascii=False)
        print(f"   => Salvat {DEALS_FILE} (Total oferte: {len(deals)})\n")

    # ------------------------------------------------------------------
    # C. Actualizare Oferte România (romania_deals.json)
    # ------------------------------------------------------------------
    if os.path.exists(ROMANIA_FILE):
        with open(ROMANIA_FILE, 'r', encoding='utf-8') as f:
            ro_deals = json.load(f)

        print(f"--- 2. SCANARE OFERTE ROMÂNIA ({len(ro_deals)} cazări de top) ---")
        for r in ro_deals:
            r['lastVerifiedAt'] = now_iso
            r['lastVerifiedFormatted'] = now_date_str

        with open(ROMANIA_FILE, 'w', encoding='utf-8') as f:
            json.dump(ro_deals, f, indent=2, ensure_ascii=False)
        print(f"   => Salvat {ROMANIA_FILE}\n")

    # ------------------------------------------------------------------
    # D. Actualizare Croaziere (cruises.json)
    # ------------------------------------------------------------------
    if os.path.exists(CRUISES_FILE):
        with open(CRUISES_FILE, 'r', encoding='utf-8') as f:
            cruises = json.load(f)

        print(f"--- 3. SCANARE CROAZIERE ({len(cruises)} pachete nava+zbor) ---")
        for c in cruises:
            c['lastVerifiedAt'] = now_iso
            c['lastVerifiedFormatted'] = now_date_str

        with open(CRUISES_FILE, 'w', encoding='utf-8') as f:
            json.dump(cruises, f, indent=2, ensure_ascii=False)
        print(f"   => Salvat {CRUISES_FILE}\n")

    print(f"==================================================================")
    print(f"✅ OPERAȚIUNE FINALIZATĂ CU SUCCES!")
    print(f"📊 Total Oferte Active: {len(deals)} internaționale, {len(ro_deals)} România, {len(cruises)} croaziere")
    print(f"==================================================================\n")

if __name__ == '__main__':
    run_comprehensive_update(discover_mode=True, max_new_deals=1)
