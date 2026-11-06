"""
Generator Masiv de Oferte Curate — PonturiVacanțe
Include o colecție bogată de Vacanțe Exotice & Soare de Iarnă (Decembrie – Februarie),
alături de City Break-uri și destinații europene populare.
"""
import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "deals.json")

BULK_DEALS = [
  # ========================================================
  # VACANȚE EXOTICE & SOARE DE IARNĂ (DECEMBRIE – FEBRUARIE)
  # ========================================================

  # E1. Tenerife din București (Wizz Air)
  {
    "id": "deal-exo-001",
    "slug": "vacanta-exotica-tenerife-canare-din-bucuresti-250-euro",
    "title": "Soare de iarnă în Tenerife: 7 nopți la ocean în Insulele Canare + Zbor direct",
    "destination": "Tenerife (Insulele Canare)",
    "country": "Spania",
    "flag": "🇪🇸",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "TFS",
    "dates": "15 – 22 Ianuarie 2027",
    "departureDate": "2027-01-15",
    "returnDate": "2027-01-22",
    "nights": 7,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🌴 Canare 24°C",
    "image": "https://images.unsplash.com/photo-1544085311-11a028465b03?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 250,
    "discountPercent": 56,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – TFS (Direct)",
      "price": 110,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "alternativeAirlines": [
      { "name": "Ryanair", "price": 125, "route": "OTP – TFS (via Bergamo/Madrid)" }
    ],
    "hotel": {
      "name": "Apartamentos Los Cardones Costa Adeje 3★",
      "provider": "Booking.com",
      "rating": 8.5,
      "reviewsCount": 2100,
      "distance": "La 300m de plajă în Playa de las Américas",
      "amenities": ["Piscină exterioară", "Grădină tropicală", "Bucătărie utilată"],
      "priceTotal": 280,
      "pricePerPerson": 140,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Resort Piscină",
        "name": "Apartamentos Los Cardones 3★",
        "rating": 8.5,
        "priceTotal": 280,
        "pricePerPerson": 140,
        "type": "Apartament cu terasă",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Adeje Ocean View Residence",
        "rating": 8.7,
        "priceTotal": 252,
        "pricePerPerson": 126,
        "type": "Apartament cu vedere ocean",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Surferi",
        "name": "Tenerife Surf & Yoga Hostel",
        "rating": 9.2,
        "priceTotal": 140,
        "pricePerPerson": 20,
        "type": "Pat dormitor pe plajă",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "22 – 29 Ianuarie 2027", "price": 259 },
      { "dates": "5 – 12 Februarie 2027", "price": 265 }
    ],
    "description": "Fugi de frigul iernii la 24°C în Tenerife! Zbor direct din București și o săptămână întreagă de relaxare la ocean, palmieri și vulcanul El Teide.",
    "featured": True,
    "publishedAt": "2026-11-06T16:00:00Z"
  },

  # E2. Abu Dhabi & Dubai din București (Wizz Air)
  {
    "id": "deal-exo-002",
    "slug": "vacanta-exotica-abu-dhabi-dubai-din-bucuresti-208-euro",
    "title": "Soare și zgârie-nori în Emirate: 5 nopți în Abu Dhabi & Dubai + Zbor direct",
    "destination": "Abu Dhabi & Dubai",
    "country": "Emiratele Arabe Unite",
    "flag": "🇦🇪",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "AUH",
    "dates": "10 – 15 Decembrie 2026",
    "departureDate": "2026-12-10",
    "returnDate": "2026-12-15",
    "nights": 5,
    "category": "Exotic & Soare de Iarnă",
    "badge": "☀️ 28°C în Decembrie",
    "image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 208,
    "discountPercent": 52,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – AUH (Direct)",
      "price": 98,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "alternativeAirlines": [
      { "name": "HiSky", "price": 140, "route": "OTP – DXB (Dubai Direct)" }
    ],
    "hotel": {
      "name": "Premier Inn Abu Dhabi Capital Centre 3★",
      "provider": "Booking.com",
      "rating": 8.6,
      "reviewsCount": 4500,
      "distance": "Lângă faleza Corniche",
      "amenities": ["Piscină acoperiș", "Sală fitness", "Baie privată"],
      "priceTotal": 220,
      "pricePerPerson": 110,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Piscină Acoperiș",
        "name": "Premier Inn Capital Centre 3★",
        "rating": 8.6,
        "priceTotal": 220,
        "pricePerPerson": 110,
        "type": "Cameră dublă modernă",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Apartament Agoda",
        "name": "Corniche View Luxury Suite",
        "rating": 8.8,
        "priceTotal": 196,
        "pricePerPerson": 98,
        "type": "Apartament cu vedere mare",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Capsulă",
        "name": "Abu Dhabi Traveler Pods",
        "rating": 8.7,
        "priceTotal": 115,
        "pricePerPerson": 23,
        "type": "Capsulă privată futuristă",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "14 – 19 Ianuarie 2027", "price": 215 },
      { "dates": "4 – 9 Februarie 2027", "price": 220 }
    ],
    "description": "Vreme perfectă de plajă la 27-28°C în mijlocul iernii! Zbor direct din București spre Abu Dhabi. Vizitează Moscheea Sheikh Zayed, Louvre Abu Dhabi și Burj Khalifa din Dubai.",
    "featured": True,
    "publishedAt": "2026-11-06T15:45:00Z"
  },

  # E3. Iordania & Marea Roșie din București (Ryanair)
  {
    "id": "deal-exo-003",
    "slug": "vacanta-exotica-iordania-aqaba-petra-din-bucuresti-129-euro",
    "title": "Aventură în Iordania: 4 nopți la Marea Roșie (Aqaba) & Petra + Zbor direct",
    "destination": "Aqaba & Petra",
    "country": "Iordania",
    "flag": "🇯🇴",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "AQJ",
    "dates": "18 – 22 Ianuarie 2027",
    "departureDate": "2027-01-18",
    "returnDate": "2027-01-22",
    "nights": 4,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🐪 Marea Roșie & Petra",
    "image": "https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 129,
    "discountPercent": 60,
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – AQJ (Direct)",
      "price": 54,
      "baggageInfo": "Geantă mică 40×25×20 cm inclusă",
      "link": "https://www.ryanair.com"
    },
    "alternativeAirlines": [
      { "name": "Wizz Air", "price": 59, "route": "OTP – AQJ (Direct)" }
    ],
    "hotel": {
      "name": "My Hotel Aqaba 3★",
      "provider": "Booking.com",
      "rating": 8.6,
      "reviewsCount": 1890,
      "distance": "În centrul orașului Aqaba lângă plajă",
      "amenities": ["Piscină pe acoperiș", "Mic dejun inclus", "Baie privată"],
      "priceTotal": 150,
      "pricePerPerson": 75,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Piscină Acoperiș",
        "name": "My Hotel Aqaba 3★",
        "rating": 8.6,
        "priceTotal": 150,
        "pricePerPerson": 75,
        "type": "Cameră dublă cu mic dejun",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Aqaba Red Sea Suites",
        "rating": 8.7,
        "priceTotal": 136,
        "pricePerPerson": 68,
        "type": "Studio privat",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Scufundări",
        "name": "Darna Divers Village Aqaba",
        "rating": 9.0,
        "priceTotal": 72,
        "pricePerPerson": 18,
        "type": "Cameră sat scufundări",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "25 – 29 Ianuarie 2027", "price": 135 },
      { "dates": "1 – 5 Februarie 2027", "price": 139 }
    ],
    "description": "Una dintre cele mai spectaculoase oferte posibile: zbor direct la Marea Roșie! Snorkeling printre corali la 24°C, noapte în deșertul roșu Wadi Rum și minunea antică Petra.",
    "featured": True,
    "publishedAt": "2026-11-06T15:30:00Z"
  },

  # E4. Hurghada (Egipt) din București
  {
    "id": "deal-exo-004",
    "slug": "sejur-all-inclusive-hurghada-egipt-din-bucuresti-255-euro",
    "title": "Egipt la Soare: 6 nopți la Resort 4★ cu All Inclusive + Zbor dus-întors",
    "destination": "Hurghada (Marea Roșie)",
    "country": "Egipt",
    "flag": "🇪🇬",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "HRG",
    "dates": "12 – 18 Februarie 2027",
    "departureDate": "2027-02-12",
    "returnDate": "2027-02-18",
    "nights": 6,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🍹 All Inclusive 25°C",
    "image": "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 255,
    "discountPercent": 50,
    "flight": {
      "airline": "Pegasus Airlines",
      "airlineCode": "PC",
      "route": "OTP – HRG (Conexiune rapidă)",
      "price": 125,
      "baggageInfo": "Geantă mică 40×30×15 cm inclusă",
      "link": "https://www.flypgs.com"
    },
    "hotel": {
      "name": "Seagull Beach Resort 4★ All Inclusive",
      "provider": "Booking.com",
      "rating": 8.4,
      "reviewsCount": 3800,
      "distance": "Pe plaja privată la Marea Roșie",
      "amenities": ["All Inclusive complet", "Aqua park propriu", "Plajă privată"],
      "priceTotal": 260,
      "pricePerPerson": 130,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 All Inclusive 4★",
        "name": "Seagull Beach Resort 4★",
        "rating": 8.4,
        "priceTotal": 260,
        "pricePerPerson": 130,
        "type": "Cameră dublă All Inclusive",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Hurghada Coral Beach Resort",
        "rating": 8.5,
        "priceTotal": 240,
        "pricePerPerson": 120,
        "type": "Bungalow pe plajă All Inclusive",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Buget",
        "name": "Bedouin Lodge Hurghada",
        "rating": 8.6,
        "priceTotal": 108,
        "pricePerPerson": 18,
        "type": "Cameră privată pe faleză",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "19 – 25 Februarie 2027", "price": 265 }
    ],
    "description": "6 nopți întregi de răsfăț All Inclusive la Marea Roșie! Mâncare și băuturi nelimitate, plajă privată cu șezlonguri, palmieri și soare cald în plină iarnă.",
    "featured": True,
    "publishedAt": "2026-11-06T15:15:00Z"
  },

  # E5. Marrakech (Maroc) din București
  {
    "id": "deal-exo-005",
    "slug": "city-break-marrakech-maroc-din-bucuresti-133-euro",
    "title": "Aromele Orientului în Marrakech: 4 nopți în Riad Tradițional + Zbor",
    "destination": "Marrakech",
    "country": "Maroc",
    "flag": "🇲🇦",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "RAK",
    "dates": "14 – 18 Ianuarie 2027",
    "departureDate": "2027-01-14",
    "returnDate": "2027-01-18",
    "nights": 4,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🕌 Riad Tradițional",
    "image": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 133,
    "discountPercent": 54,
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – RAK (Zbor combinat)",
      "price": 78,
      "baggageInfo": "Geantă mică 40×25×20 cm inclusă",
      "link": "https://www.ryanair.com"
    },
    "hotel": {
      "name": "Riad Dar Fangor Marrakech",
      "provider": "Booking.com",
      "rating": 8.9,
      "reviewsCount": 650,
      "distance": "În Medina istorică lângă Piața Jemaa el-Fna",
      "amenities": ["Curte interioară cu fântână", "Mic dejun marocan inclus", "Terasă pe acoperiș"],
      "priceTotal": 110,
      "pricePerPerson": 55,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Riad Autentic",
        "name": "Riad Dar Fangor",
        "rating": 8.9,
        "priceTotal": 110,
        "pricePerPerson": 55,
        "type": "Cameră dublă tradițională",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Medina Jasmine Suites",
        "rating": 8.8,
        "priceTotal": 98,
        "pricePerPerson": 49,
        "type": "Suită cu terasă",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo Hostel",
        "name": "Rooftop Hostel Marrakech",
        "rating": 9.1,
        "priceTotal": 48,
        "pricePerPerson": 12,
        "type": "Pat dormitor în Riad",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "21 – 25 Ianuarie 2027", "price": 139 }
    ],
    "description": "Descoperă misterul Pieței Jemaa el-Fna, Grădinile Majorelle ale lui Yves Saint Laurent și palatele orientale din Marrakech la 21°C în miezul iernii.",
    "featured": False,
    "publishedAt": "2026-11-06T15:00:00Z"
  },

  # E6. Madeira din București (Wizz Air)
  {
    "id": "deal-exo-006",
    "slug": "vacanta-exotica-madeira-portugalia-din-bucuresti-219-euro",
    "title": "Insula Eternei Primăveri: 5 nopți în Madeira (Funchal) + Zbor direct",
    "destination": "Madeira (Funchal)",
    "country": "Portugalia",
    "flag": "🇵🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "FNC",
    "dates": "19 – 24 Ianuarie 2027",
    "departureDate": "2027-01-19",
    "returnDate": "2027-01-24",
    "nights": 5,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🌺 Insula Florilor",
    "image": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 219,
    "discountPercent": 48,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – FNC (Direct)",
      "price": 119,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "hotel": {
      "name": "Hotel Orquidea Funchal 3★",
      "provider": "Booking.com",
      "rating": 8.5,
      "reviewsCount": 2400,
      "distance": "În centrul orașului Funchal",
      "amenities": ["Terasă panoramică cu vedere la ocean", "Mic dejun inclus", "Baie privată"],
      "priceTotal": 200,
      "pricePerPerson": 100,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Vedere Ocean",
        "name": "Hotel Orquidea 3★",
        "rating": 8.5,
        "priceTotal": 200,
        "pricePerPerson": 100,
        "type": "Cameră dublă cu mic dejun",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Apartament Agoda",
        "name": "Funchal Old Town Studio",
        "rating": 8.6,
        "priceTotal": 180,
        "pricePerPerson": 90,
        "type": "Studio cu bucătărie",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Natură",
        "name": "Santa Maria Hostel Funchal",
        "rating": 9.4,
        "priceTotal": 90,
        "pricePerPerson": 18,
        "type": "Pat dormitor boutique",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "26 – 31 Ianuarie 2027", "price": 225 }
    ],
    "description": "Vegetație subtropicală luxuriantă, drumeții de neuitat pe 'levadas' și stânci spectaculoase în Oceanul Atlantic la 21°C tot timpul anului.",
    "featured": False,
    "publishedAt": "2026-11-06T14:30:00Z"
  },

  # E7. Insulele Maldive (DIY via Abu Dhabi)
  {
    "id": "deal-exo-007",
    "slug": "vacanta-exotica-maldive-diy-din-bucuresti-435-euro",
    "title": "Paradisul din Maldive pe cont propriu: 7 nopți pe insulă de corali + Zbor dus-întors",
    "destination": "Maldive (Maafushi)",
    "country": "Maldive",
    "flag": "🇲🇻",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "MLE",
    "dates": "22 – 30 Ianuarie 2027",
    "departureDate": "2027-01-22",
    "returnDate": "2027-01-30",
    "nights": 7,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🏝️ Maldive DIY 30°C",
    "image": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 435,
    "discountPercent": 70,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – AUH – MLE (Conexiune Low-Cost)",
      "price": 295,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "hotel": {
      "name": "Arena Beach Hotel Maafushi 4★",
      "provider": "Booking.com",
      "rating": 8.7,
      "reviewsCount": 3200,
      "distance": "Chiar pe plaja Bikini Beach",
      "amenities": ["Plajă privată cu nisip alb", "Mic dejun inclus", "Excursii cu rechini balenă"],
      "priceTotal": 280,
      "pricePerPerson": 140,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Chiar pe Plajă",
        "name": "Arena Beach Hotel 4★",
        "rating": 8.7,
        "priceTotal": 280,
        "pricePerPerson": 140,
        "type": "Cameră dublă Deluxe pe plajă",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Kaani Palm Beach Maafushi",
        "rating": 8.8,
        "priceTotal": 266,
        "pricePerPerson": 133,
        "type": "Cameră cu vedere la ocean",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Guesthouse Buget",
        "name": "Maafushi Village Guesthouse",
        "rating": 8.9,
        "priceTotal": 175,
        "pricePerPerson": 25,
        "type": "Cameră privată cu mic dejun",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "5 – 13 Februarie 2027", "price": 449 }
    ],
    "description": "Secretul vacanței în Maldive fără să plătești 2.000€ la agenție! Zbor combinat low-cost și cazare la un hotel superb pe plaja cu nisip alb de pe insula locală Maafushi. Apă turcoaz de 29°C și recife de corali.",
    "featured": True,
    "publishedAt": "2026-11-06T16:15:00Z"
  },

  # E8. Zanzibar din București
  {
    "id": "deal-exo-008",
    "slug": "vacanta-exotica-zanzibar-tanzania-din-bucuresti-570-euro",
    "title": "Visul Tropical din Zanzibar: 8 nopți în Bungalow pe plaja Nungwi + Zbor",
    "destination": "Zanzibar (Tanzania)",
    "country": "Tanzania",
    "flag": "🇹🇿",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "ZNZ",
    "dates": "3 – 11 Februarie 2027",
    "departureDate": "2027-02-03",
    "returnDate": "2027-02-11",
    "nights": 8,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🌊 Oceanul Indian 31°C",
    "image": "https://images.unsplash.com/photo-1586861635167-e5223aadc9fe?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 570,
    "discountPercent": 65,
    "flight": {
      "airline": "FlyDubai",
      "airlineCode": "FZ",
      "route": "OTP – DXB – ZNZ (Conexiune lină)",
      "price": 420,
      "baggageInfo": "Bagaj de cală 20 kg + cabină inclus",
      "link": "https://www.flydubai.com"
    },
    "hotel": {
      "name": "Amaan Beach Bungalows Nungwi 3★",
      "provider": "Booking.com",
      "rating": 8.6,
      "reviewsCount": 2100,
      "distance": "Pe cea mai frumoasă plajă din Nungwi",
      "amenities": ["Piscină pe stânci", "Mic dejun tropical inclus", "Plajă fără reflux"],
      "priceTotal": 300,
      "pricePerPerson": 150,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Bungalow Plajă",
        "name": "Amaan Beach Bungalows 3★",
        "rating": 8.6,
        "priceTotal": 300,
        "pricePerPerson": 150,
        "type": "Bungalow cu terasă și mic dejun",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Nungwi Ocean View Suites",
        "rating": 8.7,
        "priceTotal": 270,
        "pricePerPerson": 135,
        "type": "Cameră pe faleza Nungwi",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Backpackers",
        "name": "Zanzibar Backpackers Lodge",
        "rating": 8.8,
        "priceTotal": 144,
        "pricePerPerson": 18,
        "type": "Cameră privată simplă",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "10 – 18 Februarie 2027", "price": 585 }
    ],
    "description": "Nisip alb ca pudra, ape de un turcoaz ireal și apusuri de film în Nungwi. 8 nopți de evadare tropicală completă în Oceanul Indian la 31°C.",
    "featured": True,
    "publishedAt": "2026-11-06T16:30:00Z"
  },

  # E9. Gran Canaria din Cluj-Napoca (Ryanair/Wizz Air)
  {
    "id": "deal-exo-009",
    "slug": "vacanta-exotica-gran-canaria-din-cluj-225-euro",
    "title": "Dunele Maspalomas & Oceanul: 7 nopți în Gran Canaria din Cluj-Napoca",
    "destination": "Gran Canaria (Insulele Canare)",
    "country": "Spania",
    "flag": "🇪🇸",
    "originCity": "Cluj-Napoca",
    "originCode": "CLJ",
    "destinationCode": "LPA",
    "dates": "23 – 30 Ianuarie 2027",
    "departureDate": "2027-01-23",
    "returnDate": "2027-01-30",
    "nights": 7,
    "category": "Exotic & Soare de Iarnă",
    "badge": "🏖️ Canare 23°C",
    "image": "https://images.unsplash.com/photo-1582298538104-fe2e74c27f59?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 225,
    "discountPercent": 55,
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "CLJ – LPA (Zbor conexiune scurtă)",
      "price": 95,
      "baggageInfo": "Geantă mică 40×25×20 cm inclusă",
      "link": "https://www.ryanair.com"
    },
    "hotel": {
      "name": "Bungalows Vistaflor Maspalomas 3★",
      "provider": "Booking.com",
      "rating": 8.4,
      "reviewsCount": 1800,
      "distance": "Lângă faimoasele dune din Maspalomas",
      "amenities": ["Piscină mare exterioară", "Terasă proprie", "Bucătărie utilată"],
      "priceTotal": 260,
      "pricePerPerson": 130,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Duplex Maspalomas",
        "name": "Bungalows Vistaflor 3★",
        "rating": 8.4,
        "priceTotal": 260,
        "pricePerPerson": 130,
        "type": "Duplex complet utilat",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Playa del Inglés Resort",
        "rating": 8.5,
        "priceTotal": 238,
        "pricePerPerson": 119,
        "type": "Apartament cu piscină",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Surferi",
        "name": "Mojo Surf House Gran Canaria",
        "rating": 9.2,
        "priceTotal": 140,
        "pricePerPerson": 20,
        "type": "Pat dormitor aproape de mare",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "6 – 13 Februarie 2027", "price": 239 }
    ],
    "description": "O săptămână completă în Insulele Canare cu plecare din Cluj! Nisip auriu în rezervația naturală a dunelor Maspalomas, ocean și temperaturi ideale de primăvară în ianuarie.",
    "featured": False,
    "publishedAt": "2026-11-06T15:20:00Z"
  },

  # ========================================================
  # CITY BREAK-URI EUROPENE & DESTINAȚII POPULARE
  # ========================================================

  # 1. Roma din București (Wizz Air)
  {
    "id": "deal-001",
    "slug": "city-break-roma-din-bucuresti-98-euro",
    "title": "Weekend la Roma: 3 nopți în Orașul Etern + Zbor dus-întors",
    "destination": "Roma",
    "country": "Italia",
    "flag": "🇮🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "FCO",
    "dates": "20 – 23 Noiembrie 2026",
    "departureDate": "2026-11-20",
    "returnDate": "2026-11-23",
    "nights": 3,
    "category": "City Break",
    "badge": "🔥 Chilipir",
    "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 98,
    "discountPercent": 55,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – FCO (Direct)",
      "price": 38,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "alternativeAirlines": [
      { "name": "Ryanair", "price": 42, "route": "OTP – CIA (Direct)" },
      { "name": "TAROM", "price": 99, "route": "OTP – FCO (Cu bagaj cală 23kg inclus)" }
    ],
    "hotel": {
      "name": "Hotel San Giovanni Roma 3★",
      "provider": "Booking.com",
      "rating": 8.4,
      "reviewsCount": 1420,
      "distance": "1.8 km de Colosseum",
      "amenities": ["Baie privată", "WiFi Gratuit", "Aer condiționat", "Aproape de metrou"],
      "priceTotal": 120,
      "pricePerPerson": 60,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Recomandat 3★",
        "name": "Hotel San Giovanni Roma 3★",
        "rating": 8.4,
        "priceTotal": 120,
        "pricePerPerson": 60,
        "type": "Cameră dublă cu baie privată",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Apartament / Studio",
        "name": "Colosseum View Suite",
        "rating": 8.6,
        "priceTotal": 110,
        "pricePerPerson": 55,
        "type": "Studio privat cu chicinetă",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Ultra-Buget",
        "name": "The YellowSquare Rome Hostel",
        "rating": 8.9,
        "priceTotal": 66,
        "pricePerPerson": 22,
        "type": "Pat în dormitor comun (ideal solo)",
        "link": "https://www.hostelworld.com"
      }
    ],
    "alternativeDates": [
      { "dates": "27 – 30 Noiembrie 2026", "price": 104 }
    ],
    "description": "Una dintre cele mai accesibile escapade la Roma! Zbor direct din București cu orar convenabil de weekend și cazare la un hotel de 3 stele cu recenzii foarte bune.",
    "featured": True,
    "publishedAt": "2026-11-06T12:00:00Z"
  },

  # 2. Milano / Bergamo din Cluj (Ryanair)
  {
    "id": "deal-002",
    "slug": "vacanta-milano-bergamo-din-cluj-74-euro",
    "title": "Escapadă la Milano & Lacul Como din Cluj-Napoca",
    "destination": "Milano & Bergamo",
    "country": "Italia",
    "flag": "🇮🇹",
    "originCity": "Cluj-Napoca",
    "originCode": "CLJ",
    "destinationCode": "BGY",
    "dates": "27 – 30 Noiembrie 2026",
    "departureDate": "2026-11-27",
    "returnDate": "2026-11-30",
    "nights": 3,
    "category": "City Break",
    "badge": "⚡ Cel mai mic preț",
    "image": "https://images.unsplash.com/photo-1513581166391-887a96ddeafd?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 74,
    "discountPercent": 62,
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "CLJ – BGY (Direct)",
      "price": 28,
      "baggageInfo": "Geantă mică 40×25×20 cm inclusă",
      "link": "https://www.ryanair.com"
    },
    "hotel": {
      "name": "B&B Bergamo Central",
      "provider": "Booking.com",
      "rating": 8.7,
      "reviewsCount": 890,
      "distance": "Central în Bergamo Basso",
      "amenities": ["Baie privată", "Mic dejun inclus", "WiFi rapid"],
      "priceTotal": 92,
      "pricePerPerson": 46,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Recomandat 3★",
        "name": "B&B Bergamo Central",
        "rating": 8.7,
        "priceTotal": 92,
        "pricePerPerson": 46,
        "type": "Cameră dublă cu mic dejun",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Specială",
        "name": "Bergamo City Loft",
        "rating": 8.5,
        "priceTotal": 84,
        "pricePerPerson": 42,
        "type": "Apartament cu bucătărie",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Buget",
        "name": "Central Bergamo Hostel",
        "rating": 8.4,
        "priceTotal": 54,
        "pricePerPerson": 18,
        "type": "Pat dormitor comun",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Zbori la Bergamo cu doar 28€ dus-întors cu Ryanair! Cu trenul ajungi în 50 de minute fie în centrul Milano, fie pe malul celebrului Lac Como.",
    "featured": True,
    "publishedAt": "2026-11-06T10:30:00Z"
  },

  # 3. Malaga din București (HiSky)
  {
    "id": "deal-003",
    "slug": "city-break-malaga-spania-din-bucuresti-hisky-129-euro",
    "title": "Andaluzia & Malaga din București cu HiSky: 3 nopți + Zbor direct",
    "destination": "Malaga (Costa del Sol)",
    "country": "Spania",
    "flag": "🇪🇸",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "AGP",
    "dates": "3 – 6 Decembrie 2026",
    "departureDate": "2026-12-03",
    "returnDate": "2026-12-06",
    "nights": 3,
    "category": "Mare & Soare",
    "badge": "✈️ Companie HiSky",
    "image": "https://images.unsplash.com/photo-1543783207-ec64e4d95325?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 129,
    "discountPercent": 46,
    "flight": {
      "airline": "HiSky",
      "airlineCode": "H4",
      "route": "OTP – AGP (Direct)",
      "price": 59,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm (8 kg inclus)",
      "link": "https://hisky.aero"
    },
    "hotel": {
      "name": "Hotel Soho Boutique Málaga 3★",
      "provider": "Booking.com",
      "rating": 8.6,
      "reviewsCount": 1650,
      "distance": "În centrul istoric Soho",
      "amenities": ["Baie privată", "WiFi Gratuit", "La 500m de plajă"],
      "priceTotal": 140,
      "pricePerPerson": 70,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Hotel Boutique",
        "name": "Hotel Soho Boutique Málaga 3★",
        "rating": 8.6,
        "priceTotal": 140,
        "pricePerPerson": 70,
        "type": "Cameră dublă elegantă",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Apartament Agoda",
        "name": "Malaga Beachfront Living",
        "rating": 8.7,
        "priceTotal": 126,
        "pricePerPerson": 63,
        "type": "Studio la plajă",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Tineri",
        "name": "Oasis Backpackers' Hostel Malaga",
        "rating": 9.1,
        "priceTotal": 60,
        "pricePerPerson": 20,
        "type": "Pat dormitor comun cu terasă",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Zbor direct București - Malaga cu HiSky (8 kg bagaj inclus)! Temperaturi de 18-20°C în decembrie, plimbări pe faleză și tapas autentice.",
    "featured": True,
    "publishedAt": "2026-11-06T14:00:00Z"
  },

  # 4. Viena din București (Ryanair)
  {
    "id": "deal-008",
    "slug": "weekend-viena-din-bucuresti-89-euro",
    "title": "Weekend la Viena din București: Piețele de Crăciun & Palatele Imperiale",
    "destination": "Viena",
    "country": "Austria",
    "flag": "🇦🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "VIE",
    "dates": "28 – 30 Noiembrie 2026",
    "departureDate": "2026-11-28",
    "returnDate": "2026-11-30",
    "nights": 2,
    "category": "Weekend",
    "badge": "🎄 Piețe de Crăciun",
    "image": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 89,
    "discountPercent": 50,
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – VIE (Direct)",
      "price": 35,
      "baggageInfo": "Geantă mică 40×25×20 cm inclusă",
      "link": "https://www.ryanair.com"
    },
    "hotel": {
      "name": "Ibis Wien Hauptbahnhof 3★",
      "provider": "Booking.com",
      "rating": 8.5,
      "reviewsCount": 4200,
      "distance": "Gara Centrală Viena",
      "amenities": ["Baie privată", "Metrou direct spre Stephansplatz"],
      "priceTotal": 108,
      "pricePerPerson": 54,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Lanț Ibis 3★",
        "name": "Ibis Wien Hauptbahnhof",
        "rating": 8.5,
        "priceTotal": 108,
        "pricePerPerson": 54,
        "type": "Cameră dublă standard",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Vienna Central Apartments",
        "rating": 8.6,
        "priceTotal": 98,
        "pricePerPerson": 49,
        "type": "Apartament cu chicinetă",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo Hostel",
        "name": "Wombat's City Hostel Vienna",
        "rating": 9.1,
        "priceTotal": 44,
        "pricePerPerson": 22,
        "type": "Pat dormitor central",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Un weekend rapid și elegant la Viena! Prinde atmosfera magică din fața Primăriei Rathaus și palatele Schönbrunn și Hofburg.",
    "featured": True,
    "publishedAt": "2026-11-05T14:20:00Z"
  },

  # 5. Bologna din Craiova (Wizz Air)
  {
    "id": "deal-010",
    "slug": "city-break-bologna-din-craiova-79-euro",
    "title": "Capitala Gastronomică a Italiei: 3 nopți în Bologna din Craiova",
    "destination": "Bologna",
    "country": "Italia",
    "flag": "🇮🇹",
    "originCity": "Craiova",
    "originCode": "CRA",
    "destinationCode": "BLQ",
    "dates": "5 – 8 Decembrie 2026",
    "departureDate": "2026-12-05",
    "returnDate": "2026-12-08",
    "nights": 3,
    "category": "City Break",
    "badge": "🍝 Gurmand",
    "image": "https://images.unsplash.com/photo-1549880338-65ddcdfd017b?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 79,
    "discountPercent": 58,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "CRA – BLQ (Direct)",
      "price": 29,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "hotel": {
      "name": "Hotel San Donato Bologna 3★",
      "provider": "Booking.com",
      "rating": 8.3,
      "reviewsCount": 1150,
      "distance": "În centrul istoric lângă Due Torri",
      "amenities": ["Baie privată", "WiFi gratuit"],
      "priceTotal": 100,
      "pricePerPerson": 50,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Central 3★",
        "name": "Hotel San Donato Bologna",
        "rating": 8.3,
        "priceTotal": 100,
        "pricePerPerson": 50,
        "type": "Cameră dublă centrală",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Apartament Agoda",
        "name": "Bologna Center Suites",
        "rating": 8.5,
        "priceTotal": 90,
        "pricePerPerson": 45,
        "type": "Studio privat cu chicinetă",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Buget",
        "name": "Dopa Hostel Bologna",
        "rating": 9.3,
        "priceTotal": 54,
        "pricePerPerson": 18,
        "type": "Pat dormitor confortabil",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Zbor direct din Craiova către Bologna, cel mai celebru oraș culinar din Italia. Savurează paste proaspete tagliatelle al ragù.",
    "featured": False,
    "publishedAt": "2026-11-06T11:00:00Z"
  },

  # 6. Bruxelles din Suceava (Wizz Air)
  {
    "id": "deal-015",
    "slug": "city-break-bruxelles-din-suceava-88-euro",
    "title": "Bruxelles & Bruges din Suceava: 3 nopți în inima Europei",
    "destination": "Bruxelles & Bruges",
    "country": "Belgia",
    "flag": "🇧🇪",
    "originCity": "Suceava",
    "originCode": "SCV",
    "destinationCode": "CRL",
    "dates": "5 – 8 Decembrie 2026",
    "departureDate": "2026-12-05",
    "returnDate": "2026-12-08",
    "nights": 3,
    "category": "City Break",
    "badge": "🍫 Ciocolată & Bere",
    "image": "https://images.unsplash.com/photo-1517732306149-e8f829eb588a?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 88,
    "discountPercent": 52,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "SCV – CRL (Direct)",
      "price": 32,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "hotel": {
      "name": "Meininger Hotel Bruxelles City Center 3★",
      "provider": "Booking.com",
      "rating": 8.5,
      "reviewsCount": 5100,
      "distance": "Pe malul canalului lângă Grand Place",
      "amenities": ["Baie privată", "Design modern", "Metrou aproape"],
      "priceTotal": 112,
      "pricePerPerson": 56,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Design Hotel 3★",
        "name": "Meininger Hotel Bruxelles",
        "rating": 8.5,
        "priceTotal": 112,
        "pricePerPerson": 56,
        "type": "Cameră dublă modernă",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Apartament Agoda",
        "name": "Grand Place Historic Suites",
        "rating": 8.6,
        "priceTotal": 104,
        "pricePerPerson": 52,
        "type": "Studio în centru",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo Hostel",
        "name": "Sleep Well Youth Hostel",
        "rating": 8.9,
        "priceTotal": 57,
        "pricePerPerson": 19,
        "type": "Pat dormitor cu mic dejun",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Zbor direct din Suceava spre Belgia! Vizitează Grand Place, savurează vafe fierbinți belgiene și fă o excursie de o zi în Bruges.",
    "featured": False,
    "publishedAt": "2026-11-04T12:00:00Z"
  },

  # 7. Londra din Sibiu (Wizz Air)
  {
    "id": "deal-011",
    "slug": "city-break-londra-din-sibiu-109-euro",
    "title": "Escapadă la Londra din Sibiu: 3 nopți în metropola britanică",
    "destination": "Londra",
    "country": "Marea Britanie",
    "flag": "🇬🇧",
    "originCity": "Sibiu",
    "originCode": "SBZ",
    "destinationCode": "LTN",
    "dates": "12 – 15 Decembrie 2026",
    "departureDate": "2026-12-12",
    "returnDate": "2026-12-15",
    "nights": 3,
    "category": "City Break",
    "badge": "👑 Metropolă",
    "image": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 109,
    "discountPercent": 48,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "SBZ – LTN (Direct)",
      "price": 39,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com"
    },
    "hotel": {
      "name": "Point A Hotel London Kings Cross 3★",
      "provider": "Booking.com",
      "rating": 8.3,
      "reviewsCount": 3800,
      "distance": "5 min de gara Kings Cross",
      "amenities": ["Baie privată", "WiFi rapid", "Metrou la 2 minute"],
      "priceTotal": 140,
      "pricePerPerson": 70,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Kings Cross 3★",
        "name": "Point A Hotel Kings Cross",
        "rating": 8.3,
        "priceTotal": 140,
        "pricePerPerson": 70,
        "type": "Cameră dublă compactă",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Studio Agoda",
        "name": "London City Flat",
        "rating": 8.2,
        "priceTotal": 130,
        "pricePerPerson": 65,
        "type": "Apartament privat",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo / Hostel",
        "name": "Generator London",
        "rating": 8.6,
        "priceTotal": 69,
        "pricePerPerson": 23,
        "type": "Pat dormitor central",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Zbor direct din Sibiu la Londra! Vizitează Muzeul Britanic, Big Ben, London Eye și spectacolele de pe West End.",
    "featured": False,
    "publishedAt": "2026-11-05T16:00:00Z"
  },

  # 8. Paris din București (Ryanair)
  {
    "id": "deal-012",
    "slug": "city-break-paris-din-bucuresti-119-euro",
    "title": "Weekend romantic la Paris din București: 3 nopți + Zbor direct",
    "destination": "Paris",
    "country": "Franța",
    "flag": "🇫🇷",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "BVA",
    "dates": "11 – 14 Decembrie 2026",
    "departureDate": "2026-12-11",
    "returnDate": "2026-12-14",
    "nights": 3,
    "category": "City Break",
    "badge": "🗼 Romantic",
    "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 119,
    "discountPercent": 48,
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – BVA (Direct)",
      "price": 45,
      "baggageInfo": "Geantă mică 40×25×20 cm inclusă",
      "link": "https://www.ryanair.com"
    },
    "hotel": {
      "name": "Ibis Paris Montmartre 3★",
      "provider": "Booking.com",
      "rating": 8.4,
      "reviewsCount": 2900,
      "distance": "În cartierul boem Montmartre",
      "amenities": ["Baie privată", "Metrou la 200m", "Aproape de Sacré-Cœur"],
      "priceTotal": 148,
      "pricePerPerson": 74,
      "link": "https://www.booking.com"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Montmartre 3★",
        "name": "Ibis Paris Montmartre",
        "rating": 8.4,
        "priceTotal": 148,
        "pricePerPerson": 74,
        "type": "Cameră dublă confort",
        "link": "https://www.booking.com"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Studio Agoda",
        "name": "Parisian Artist Loft",
        "rating": 8.5,
        "priceTotal": 136,
        "pricePerPerson": 68,
        "type": "Studio cu bucătărie",
        "link": "https://www.agoda.com"
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Solo Hostel",
        "name": "St Christopher's Inn Paris Canal",
        "rating": 8.8,
        "priceTotal": 66,
        "pricePerPerson": 22,
        "type": "Pat dormitor pe malul canalului",
        "link": "https://www.hostelworld.com"
      }
    ],
    "description": "Turnul Eiffel, Muzeul Luvru, croazieră pe Sena și croissante proaspete în Montmartre. Zbor direct din București la un preț imbatabil.",
    "featured": False,
    "publishedAt": "2026-11-06T08:00:00Z"
  }
]

def genereaza_catalog():
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(BULK_DEALS, f, indent=2, ensure_ascii=False)
    print(f"[SUCCES] Am populat catalogul cu {len(BULK_DEALS)} oferte (inclusiv colecția exotică de iarnă) în {OUTPUT_PATH}!")

if __name__ == "__main__":
    genereaza_catalog()
