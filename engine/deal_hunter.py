"""
Motorul 'Deal Hunter' — Scanează zboruri ieftine și construiește pachete de vacanță DIY
"""
import json
import os
import requests
from datetime import datetime, timedelta
from config import TEQUILA_API_KEY, ORIGIN_AIRPORTS, MAX_FLIGHT_PRICE_EUR

TEQUILA_URL = "https://api.tequila.kiwi.com/v2/search"

def scaneaza_zboruri(origini=None, max_pret=MAX_FLIGHT_PRICE_EUR, zile_inainte=90):
    """
    Interoghează Kiwi Tequila API pentru zboruri directe dus-întors din România.
    """
    if origini is None:
        origini = [a["code"] for a in ORIGIN_AIRPORTS]

    data_start = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
    data_final = (datetime.now() + timedelta(days=zile_inainte)).strftime("%d/%m/%Y")

    headers = {"apikey": TEQUILA_API_KEY}
    rezultate = []

    for aeroport in origini:
        params = {
            "fly_from": aeroport,
            "fly_to": "europe",
            "date_from": data_start,
            "date_to": data_final,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 4,
            "flight_type": "round",
            "price_to": max_pret,
            "curr": "EUR",
            "max_stopovers": 0,
            "limit": 10,
            "sort": "price"
        }

        try:
            print(f"[HUNTER] Scanez plecări din {aeroport}...")
            r = requests.get(TEQUILA_URL, headers=headers, params=params, timeout=15)
            if r.status_code == 200:
                data = r.json().get("data", [])
                for zbor in data:
                    rezultate.append({
                        "origine_oras": zbor.get("cityFrom"),
                        "origine_cod": zbor.get("flyFrom"),
                        "destinatie_oras": zbor.get("cityTo"),
                        "destinatie_tara": zbor.get("countryTo", {}).get("name"),
                        "destinatie_cod": zbor.get("flyTo"),
                        "pret_zbor": zbor.get("price"),
                        "plecare": zbor.get("local_departure")[:10],
                        "intoarcere": zbor.get("route", [{}])[-1].get("local_departure", "")[:10],
                        "nopti": zbor.get("nightsInDest"),
                        "companie": zbor.get("airlines", ["LowCost"])[0],
                        "link": zbor.get("deep_link")
                    })
            else:
                print(f"[AVERTISMENT] API {aeroport} a răspuns cu codul {r.status_code}")
        except Exception as e:
            print(f"[EROARE] Nu am putut interoga API-ul pentru {aeroport}: {e}")

    return rezultate

def genereaza_oferta_diy(zbor, cost_noapte_hotel=60):
    """
    Aplică formula DIY: Preț = Zbor + (Cazare_Total / 2)
    """
    nopti = zbor["nopti"]
    cazare_total = nopti * cost_noapte_hotel
    cazare_persoana = cazare_total / 2
    pret_final = round(zbor["pret_zbor"] + cazare_persoana)

    slug = f"city-break-{zbor['destinatie_oras'].lower().replace(' ', '-')}-din-{zbor['origine_oras'].lower().replace(' ', '-')}-{pret_final}-euro"

    return {
        "id": f"deal-{int(datetime.now().timestamp())}",
        "slug": slug,
        "title": f"Escapadă la {zbor['destinatie_oras']} din {zbor['origine_oras']}: {nopti} nopți + Zbor",
        "destination": zbor["destinatie_oras"],
        "country": zbor["destinatie_tara"],
        "originCity": zbor["origine_oras"],
        "originCode": zbor["origine_cod"],
        "destinationCode": zbor["destinatie_cod"],
        "dates": f"{zbor['plecare']} – {zbor['intoarcere']}",
        "nights": nopti,
        "priceTotalPerPerson": pret_final,
        "flight": {
            "airline": zbor["companie"],
            "price": zbor["pret_zbor"],
            "link": zbor["link"]
        },
        "hotel": {
            "name": f"Hotel 3★ central în {zbor['destinatie_oras']}",
            "rating": 8.3,
            "priceTotal": cazare_total,
            "pricePerPerson": cazare_persoana,
            "link": f"https://www.booking.com/searchresults.html?ss={zbor['destinatie_oras']}"
        }
    }

if __name__ == "__main__":
    print("=== MOTORUL DE CĂUTARE VACANȚE DIY ===")
    if TEQUILA_API_KEY == "DEMO_TEQUILA_KEY":
        print("[INFO] Cheia Tequila API nu este configurată încă.")
        print("[INFO] Obține o cheie gratuită de pe https://tequila.kiwi.com/")
    else:
        zboruri = scaneaza_zboruri()
        print(f"[SUCCES] Am găsit {len(zboruri)} zboruri sub pragul stabilit!")
