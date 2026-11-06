"""
Panou de Control & Sincronizare Oferte — PonturiVacanțe
Permite adăugarea manuală, scanarea automată și publicarea instantă pe Telegram.
"""
import json
import os
import sys
from datetime import datetime

# Asigurare encoding UTF-8 pentru consola Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from config import ORIGIN_AIRPORTS, TELEGRAM_BOT_TOKEN
from telegram_bot import trimite_alerta_telegram

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "deals.json")

def incarca_oferte():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def salveaza_oferte(deals):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(deals, f, indent=2, ensure_ascii=False)
    print(f"[SUCCES] Salvat {len(deals)} oferte în {DATA_PATH}!")

def adauga_oferta_manual():
    print("\n--- ADĂUGARE OFERTĂ NOUĂ (DIY) ---")
    destinatie = input("Destinație (ex: Roma): ").strip()
    tara = input("Țară (ex: Italia): ").strip()
    flag = input("Emoji steag (ex: 🇮🇹): ").strip() or "✈️"
    
    print("\nAlege orașul de plecare:")
    for idx, a in enumerate(ORIGIN_AIRPORTS, 1):
        print(f" {idx}. {a['city']} ({a['code']})")
    opt = int(input("Alegere (1-6): ").strip() or "1")
    aeroport_ales = ORIGIN_AIRPORTS[opt - 1]
    
    dates = input("Perioadă (ex: 10 – 13 Iunie 2026): ").strip()
    nopti = int(input("Număr nopți (ex: 3): ").strip() or "3")
    companie = input("Companie aeriană (Wizz Air / Ryanair etc.): ").strip() or "Wizz Air"
    pret_zbor = float(input("Preț bilet zbor dus-întors în EUR (ex: 35): ").strip())
    
    hotel_nume = input("Nume hotel (ex: Hotel Central 3★): ").strip()
    hotel_rating = float(input("Notă hotel pe Booking (ex: 8.4): ").strip() or "8.4")
    cazare_total = float(input("Preț total cameră dublă EUR (ex: 120): ").strip())
    cazare_persoana = round(cazare_total / 2, 2)
    pret_final = round(pret_zbor + cazare_persoana)
    
    categorie = input("Categorie (City Break / Mare & Soare / Weekend): ").strip() or "City Break"
    badge = input("Badge (🔥 Chilipir / 🏖️ Plajă / ⭐ Recomandat): ").strip() or "🔥 Chilipir"
    imagine = input("URL Imagine (Unsplash etc.): ").strip() or "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80"
    
    link_zbor = input("Link zbor (Kiwi / Wizz): ").strip() or "https://wizzair.com"
    link_hotel = input("Link cazare (Booking.com): ").strip() or "https://booking.com"
    
    slug_oras = aeroport_ales['city'].lower().replace(' ', '-')
    slug_dest = destinatie.lower().replace(' ', '-')
    slug = f"vacanta-{slug_dest}-din-{slug_oras}-{pret_final}-euro"
    
    deal_nou = {
        "id": f"deal-{int(datetime.now().timestamp())}",
        "slug": slug,
        "title": f"Escapadă la {destinatie}: {nopti} nopți + Zbor din {aeroport_ales['city']}",
        "destination": destinatie,
        "country": tara,
        "flag": flag,
        "originCity": aeroport_ales["city"],
        "originCode": aeroport_ales["code"],
        "destinationCode": "",
        "dates": dates,
        "nights": nopti,
        "category": categorie,
        "badge": badge,
        "image": imagine,
        "priceTotalPerPerson": pret_final,
        "flight": {
            "airline": companie,
            "route": f"{aeroport_ales['code']} – {destinatie} (Direct)",
            "price": pret_zbor,
            "link": link_zbor
        },
        "hotel": {
            "name": hotel_nume,
            "rating": hotel_rating,
            "reviewsCount": 500,
            "distance": "Central",
            "amenities": ["Baie privată", "WiFi Gratuit", "Aer condiționat"],
            "priceTotal": cazare_total,
            "pricePerPerson": cazare_persoana,
            "link": link_hotel
        },
        "description": f"Pachet complet DIY la {destinatie} din {aeroport_ales['city']}. Zbor direct și cazare verificată cu recenzii foarte bune.",
        "publishedAt": datetime.now().isoformat() + "Z"
    }
    
    oferte = incarca_oferte()
    oferte.insert(0, deal_nou)
    salveaza_oferte(oferte)
    
    print(f"\n[SUCCES] Oferta a fost adăugată cu succes! Preț: {pret_final}€ / persoană.")
    
    trimite = input("Vrei să trimiți alerta și pe canalul de Telegram acum? (y/n): ").strip().lower()
    if trimite == 'y':
        trimite_alerta_telegram(deal_nou)

def meniu():
    while True:
        print("\n========================================")
        print("   VACANȚEDIY — CENTRU DE CONTROL")
        print("========================================")
        print("1. Listează ofertele active")
        print("2. Adaugă o ofertă nouă manual")
        print("3. Retrimite o ofertă pe Telegram")
        print("4. Rulează un build de test (npm run build)")
        print("5. Ieșire")
        
        opt = input("\nAlege o opțiune (1-5): ").strip()
        if opt == "1":
            oferte = incarca_oferte()
            print(f"\n--- Total: {len(oferte)} oferte active ---")
            for i, d in enumerate(oferte, 1):
                print(f"{i}. [{d['originCity']} -> {d['destination']}] {d['priceTotalPerPerson']}€ | {d['dates']} ({d['slug']})")
        elif opt == "2":
            adauga_oferta_manual()
        elif opt == "3":
            oferte = incarca_oferte()
            for i, d in enumerate(oferte, 1):
                print(f"{i}. {d['destination']} ({d['originCity']}) - {d['priceTotalPerPerson']}€")
            nr = int(input("Numărul ofertei: ").strip())
            trimite_alerta_telegram(oferte[nr - 1])
        elif opt == "4":
            os.system("npm run build")
        elif opt == "5":
            break

if __name__ == "__main__":
    meniu()
