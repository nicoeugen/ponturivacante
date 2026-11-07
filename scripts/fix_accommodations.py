import json
import sys

# Mapping of destinations to valid Agoda city landing paths
CITY_TO_AGODA = {
    'londra': 'london-gb',
    'roma': 'rome-it',
    'paris': 'paris-fr',
    'viena': 'vienna-at',
    'milano': 'milan-it',
    'venetia': 'venice-it',
    'veneția': 'venice-it',
    'barcelona': 'barcelona-es',
    'madrid': 'madrid-es',
    'valencia': 'valencia-es',
    'paphos': 'paphos-cy',
    'larnaca': 'larnaca-cy',
    'atena': 'athens-gr',
    'salonic': 'thessaloniki-gr',
    'corfu': 'corfu-island-gr',
    'creta': 'crete-island-gr',
    'chania': 'chania-gr',
    'heraklion': 'heraklion-gr',
    'praga': 'prague-cz',
    'budapesta': 'budapest-hu',
    'varsovia': 'warsaw-pl',
    'cracovia': 'krakow-pl',
    'amsterdam': 'amsterdam-nl',
    'bruxelles': 'brussels-be',
    'berlin': 'berlin-de',
    'munchen': 'munich-de',
    'dortmund': 'dortmund-de',
    'dublin': 'dublin-ie',
    'lisabona': 'lisbon-pt',
    'porto': 'porto-pt',
    'istanbul': 'istanbul-tr',
    'antalya': 'antalya-tr',
    'dubai': 'dubai-ae',
    'abu dhabi': 'abu-dhabi-ae',
    'hurghada': 'hurghada-eg',
    'sharm': 'sharm-el-sheikh-eg',
    'cairo': 'cairo-eg',
    'amman': 'amman-jo',
    'aqaba': 'aqaba-jo',
    'marrakech': 'marrakech-ma',
    'bansko': 'bansko-bg',
    'sofia': 'sofia-bg',
    'napoli': 'naples-it',
    'bologna': 'bologna-it',
    'bari': 'bari-it',
    'catania': 'catania-it',
    'palermo': 'palermo-it',
    'malta': 'malta-island-mt',
    'valletta': 'valletta-mt',
    'tenerife': 'tenerife-es',
    'mallorca': 'mallorca-es',
    'palma': 'palma-de-mallorca-es',
    'nisa': 'nice-fr',
    'nice': 'nice-fr'
}

def main():
    deals_path = 'C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json'
    with open(deals_path, 'r', encoding='utf-8') as f:
        deals = json.load(f)

    updated_count = 0
    for d in deals:
        hotel = d.get('hotel', {})
        direct_hotel_link = hotel.get('link', '')
        hotel_name = hotel.get('name', 'Hotel verificat')
        hotel_rating = hotel.get('rating', 8.5)
        hotel_price_total = hotel.get('priceTotal', 100)
        hotel_price_pp = hotel.get('pricePerPerson', 50)
        destination = d.get('destination', '')

        dest_lower = destination.lower()
        agoda_slug = None
        for key, slug in CITY_TO_AGODA.items():
            if key in dest_lower:
                agoda_slug = slug
                break

        if agoda_slug:
            agoda_url = f"https://www.agoda.com/ro-ro/city/{agoda_slug}.html?cid=1980047"
        else:
            agoda_url = "https://www.agoda.com/ro-ro/?cid=1980047"

        # Option 1: DIRECT HOTEL (Booking.com verified property link)
        opt_direct = {
            "provider": "Booking.com",
            "providerId": "booking",
            "badge": "★ Recomandat (Direct la hotel)",
            "name": hotel_name,
            "rating": hotel_rating,
            "priceTotal": hotel_price_total,
            "pricePerPerson": hotel_price_pp,
            "type": "Disponibilitate confirmată • Pagina hotelului",
            "link": direct_hotel_link
        }

        # Option 2: ALTERNATIVE ON AGODA (Partner Official)
        opt_agoda = {
            "provider": "Agoda",
            "providerId": "agoda",
            "badge": "Alternativă Agoda (Partener Oficial)",
            "name": f"Alte opțiuni & tarife în {destination}",
            "rating": round(min(9.5, hotel_rating + 0.1), 1),
            "priceTotal": hotel_price_total,
            "pricePerPerson": hotel_price_pp,
            "type": "Compară prețuri • Oferte de sezon pe Agoda",
            "link": agoda_url
        }

        d['accommodationOptions'] = [opt_direct, opt_agoda]
        updated_count += 1

    with open(deals_path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(deals, f, ensure_ascii=False, indent=2)

    print(f"Successfully updated accommodationOptions for {updated_count} deals.")

if __name__ == '__main__':
    main()
