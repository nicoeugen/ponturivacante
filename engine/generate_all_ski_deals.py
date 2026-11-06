import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DEALS_PATH = "data/deals.json"
all_deals = json.load(open(DEALS_PATH, encoding="utf-8"))

# Păstrăm ofertele non-schi existente
base_deals = [d for d in all_deals if not d["id"].startswith("deal-ski-")]

ski_deals = [
  # ==========================================
  # BULGARIA — FĂRĂ AVION (TRANSPORT PROPRIU)
  # ==========================================
  {
    "id": "deal-ski-001",
    "slug": "vacanta-schi-bansko-bulgaria-transport-propriu-110-euro",
    "title": "Schi la Bansko: 4 nopți la Green Life Ski & Spa Resort 4★ cu Piscină & Spa (Transport Propriu)",
    "destination": "Bansko (Munții Pirin)",
    "country": "Bulgaria",
    "flag": "🇧🇬",
    "originCity": "București",
    "originCode": "AUTO",
    "destinationCode": "BANSKO",
    "dates": "5 – 9 Februarie 2027",
    "departureDate": "2027-02-05",
    "returnDate": "2027-02-09",
    "nights": 4,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🎿 75 km Pârtii + Spa",
    "image": "https://images.unsplash.com/photo-1551524559-8af4e6624178?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 110,
    "discountPercent": 48,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (cu mașina personală)",
      "airlineCode": "CAR",
      "route": "București → Giurgiu → Ruse → Sofia → Bansko (~530 km, 5h30 pe drum asfaltat / autostradă)",
      "price": 0,
      "baggageInfo": "Portbagaj nelimitat: schiuri, clăpari, bețe și bagaje personale în mașină (fără taxe de cală)",
      "link": "https://www.google.com/maps/dir/Bucuresti/Bansko,+Bulgaria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Bansko,+Bulgaria",
      "isConnecting": False
    },
    "hotel": {
      "name": "Green Life Ski & Spa Resort Bansko 4★",
      "provider": "Booking.com",
      "rating": 8.6,
      "reviewsCount": 1850,
      "distance": "La 300m de pârtii și telegondola Bansko (shuttle gratuit inclus)",
      "amenities": [
        "Piscină interioară încălzită",
        "Centru Spa & Saună finlandeză",
        "Depozit gratuit schi & clăpari",
        "Shuttle gratuit la telegondolă"
      ],
      "priceTotal": 220,
      "pricePerPerson": 110,
      "link": "https://www.booking.com/hotel/bg/green-life-ski-spa-resort.ro.html?checkin=2027-02-05&checkout=2027-02-09&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Resort Spa & Ski",
        "name": "Green Life Ski & Spa Resort 4★",
        "rating": 8.6,
        "priceTotal": 220,
        "pricePerPerson": 110,
        "type": "Studio cu vedere la munte",
        "link": "https://www.booking.com/hotel/bg/green-life-ski-spa-resort.ro.html?checkin=2027-02-05&checkout=2027-02-09&group_adults=2&no_rooms=1"
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Grand Hotel Bansko 4★",
        "rating": 8.7,
        "priceTotal": 240,
        "pricePerPerson": 120,
        "type": "Cameră Dublă Deluxe",
        "link": "https://www.agoda.com/ro-ro/grand-hotel-bansko/hotel/bansko-bg.html?checkIn=2027-02-05&checkOut=2027-02-09&rooms=1&adults=2"
      }
    ],
    "alternativeDates": [
      {
        "dates": "22 – 26 Ianuarie 2027",
        "price": 105,
        "departureDate": "2027-01-22",
        "returnDate": "2027-01-26",
        "link": "https://www.google.com/maps/dir/Bucuresti/Bansko,+Bulgaria"
      },
      {
        "dates": "12 – 16 Februarie 2027",
        "price": 119,
        "departureDate": "2027-02-12",
        "returnDate": "2027-02-16",
        "link": "https://www.google.com/maps/dir/Bucuresti/Bansko,+Bulgaria"
      }
    ],
    "description": "Cea mai populară și avantajoasă stațiune de schi din Balcani! Peste 75 km de pârtii amenajate pe versantul muntelui Todorka (2.600m), telegondolă modernă și relaxare la centrul spa cu piscine încălzite al resortului 4★ Green Life. Fără bătăi de cap cu zborul: vii direct cu mașina și echipamentul în portbagaj.",
    "featured": True,
    "publishedAt": "2026-11-06T18:00:00.000Z"
  },
  {
    "id": "deal-ski-005",
    "slug": "vacanta-schi-borovets-bulgaria-hotel-rila-135-euro",
    "title": "Ski-in / Ski-out la Borovets: 4 nopți la Hotel Rila 4★ chiar la Baza Pârtiilor (Transport Propriu)",
    "destination": "Borovets (Munții Rila)",
    "country": "Bulgaria",
    "flag": "🇧🇬",
    "originCity": "București",
    "originCode": "AUTO",
    "destinationCode": "BOROVETS",
    "dates": "29 Ianuarie – 2 Februarie 2027",
    "departureDate": "2027-01-29",
    "returnDate": "2027-02-02",
    "nights": 4,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "⛷️ Ski-in / Ski-out & Spa",
    "image": "https://images.unsplash.com/photo-1546948630-1149ea60dc86?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 135,
    "discountPercent": 44,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (cu mașina personală)",
      "airlineCode": "CAR",
      "route": "București → Giurgiu → Ruse → Samokov → Borovets (~460 km, doar 4h30 - cea mai apropiată mare stațiune din BG)",
      "price": 0,
      "baggageInfo": "Echipament complet în mașină, parcare privată disponibilă la hotel",
      "link": "https://www.google.com/maps/dir/Bucuresti/Borovets,+Bulgaria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Borovets,+Bulgaria",
      "isConnecting": False
    },
    "hotel": {
      "name": "Hotel Rila Borovets 4★",
      "provider": "Booking.com",
      "rating": 8.9,
      "reviewsCount": 3100,
      "distance": "La 50m de telescaunul Martinovi Baraki și 200m de telegondola Borovets",
      "amenities": [
        "Acces direct pe pârtie (Ski-to-door)",
        "Piscină interioară semiolimpică (25m)",
        "Zonă termală cu saune și jacuzzi",
        "Depozit clăpari încălzit & închirieri schi"
      ],
      "priceTotal": 270,
      "pricePerPerson": 135,
      "link": "https://www.booking.com/hotel/bg/rila.ro.html?checkin=2027-01-29&checkout=2027-02-02&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Hotel Emblemă Borovets",
        "name": "Hotel Rila 4★",
        "rating": 8.9,
        "priceTotal": 270,
        "pricePerPerson": 135,
        "type": "Cameră Dublă Superioară",
        "link": "https://www.booking.com/hotel/bg/rila.ro.html?checkin=2027-01-29&checkout=2027-02-02&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "15 – 19 Ianuarie 2027",
        "price": 129,
        "departureDate": "2027-01-15",
        "returnDate": "2027-01-19",
        "link": "https://www.google.com/maps/dir/Bucuresti/Borovets,+Bulgaria"
      },
      {
        "dates": "19 – 23 Februarie 2027",
        "price": 139,
        "departureDate": "2027-02-19",
        "returnDate": "2027-02-23",
        "link": "https://www.google.com/maps/dir/Bucuresti/Borovets,+Bulgaria"
      }
    ],
    "description": "Ieși din hotel direct pe schiuri! Hotelul Rila 4★ este amplasat legendar la baza pârtiei Martinovi Baraki din Borovets. Domeniul oferă 58 km de pârtii printre pădurile maiestuoase de pini ale munților Rila, nocturnă spectaculoasă și o piscină semiolimpică de 25m cu vedere la zăpadă.",
    "featured": True,
    "publishedAt": "2026-11-06T18:02:00.000Z"
  },
  {
    "id": "deal-ski-006",
    "slug": "vacanta-schi-pamporovo-bulgaria-apartamente-98-euro",
    "title": "Schi & Relaxare la Pamporovo: 4 nopți la Grand Monastery 4★ pe Pârtia Studenets",
    "destination": "Pamporovo (Munții Rodopi)",
    "country": "Bulgaria",
    "flag": "🇧🇬",
    "originCity": "București",
    "originCode": "AUTO",
    "destinationCode": "PAMPOROVO",
    "dates": "19 – 23 Februarie 2027",
    "departureDate": "2027-02-19",
    "returnDate": "2027-02-23",
    "nights": 4,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "☀️ 120 Zile cu Soare & Pârtii Lungi",
    "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 98,
    "discountPercent": 50,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (cu mașina personală)",
      "airlineCode": "CAR",
      "route": "București → Ruse → Byala → Stara Zagora → Plovdiv → Asenovgrad → Pamporovo (~490 km, 6h)",
      "price": 0,
      "baggageInfo": "Spațiu amplu în mașină, acces ușor chiar până la parcarea complexului",
      "link": "https://www.google.com/maps/dir/Bucuresti/Pamporovo,+Bulgaria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Pamporovo,+Bulgaria",
      "isConnecting": False
    },
    "hotel": {
      "name": "Grand Monastery Private Apartments 4★",
      "provider": "Booking.com",
      "rating": 8.7,
      "reviewsCount": 1420,
      "distance": "Direct la telescaunul Studenets și pârtia principală Snezhanka",
      "amenities": [
        "Acces direct la pârtie (Ski-to-door)",
        "Șemineu pe lemne în apartament",
        "Piscină interioară încălzită & Spa",
        "Bucătărie utilată complet & parcare"
      ],
      "priceTotal": 196,
      "pricePerPerson": 98,
      "link": "https://www.booking.com/hotel/bg/grand-monastery-private-apartments.ro.html?checkin=2027-02-19&checkout=2027-02-23&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Apartament cu Șemineu",
        "name": "Grand Monastery Apartments 4★",
        "rating": 8.7,
        "priceTotal": 196,
        "pricePerPerson": 98,
        "type": "Apartament cu 1 dormitor și șemineu",
        "link": "https://www.booking.com/hotel/bg/grand-monastery-private-apartments.ro.html?checkin=2027-02-19&checkout=2027-02-23&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "5 – 9 Februarie 2027",
        "price": 95,
        "departureDate": "2027-02-05",
        "returnDate": "2027-02-09",
        "link": "https://www.google.com/maps/dir/Bucuresti/Pamporovo,+Bulgaria"
      }
    ],
    "description": "Cea mai însorită stațiune montană din Europa, faimoasă pentru cele peste 120 de zile cu soare și pârtii largi excelente pentru familii și începători. Apartamentele Grand Monastery sunt dotate cu șemineu pe lemne și oferă acces direct la telescaunul Studenets.",
    "featured": False,
    "publishedAt": "2026-11-06T18:03:00.000Z"
  },

  # ==========================================
  # AUSTRIA — FĂRĂ AVION (TRANSPORT PROPRIU)
  # ==========================================
  {
    "id": "deal-ski-003",
    "slug": "vacanta-schi-tirol-innsbruck-austria-hotel-maximilian-260-euro",
    "title": "Schi în Tirolul Austriac: 5 nopți la Hotel Maximilian 4★ în Centrul Istoric Innsbruck (Transport Propriu)",
    "destination": "Tirol & Innsbruck (Austria)",
    "country": "Austria",
    "flag": "🇦🇹",
    "originCity": "București / România",
    "originCode": "AUTO",
    "destinationCode": "INNSBRUCK",
    "dates": "28 Ianuarie – 2 Februarie 2027",
    "departureDate": "2027-01-28",
    "returnDate": "2027-02-02",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🏔️ 13 Domenii Schiabile & Ghețar",
    "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 260,
    "discountPercent": 42,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (mașină personală sau tren ÖBB Nightjet)",
      "airlineCode": "CAR",
      "route": "România → Budapesta → Viena → Salzburg → Innsbruck (drum 100% autostradă)",
      "price": 0,
      "baggageInfo": "Echipament schi complet în portbagaj, parcare securizată în Innsbruck",
      "link": "https://www.google.com/maps/dir/Bucuresti/Innsbruck,+Austria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Innsbruck,+Austria",
      "isConnecting": False
    },
    "hotel": {
      "name": "Hotel Maximilian - Stadthaus Penz 4★",
      "provider": "Booking.com",
      "rating": 8.8,
      "reviewsCount": 2380,
      "distance": "În centrul vechi din Innsbruck, lângă Acoperișul de Aur și stația telegondolei Nordkette",
      "amenities": [
        "Mic dejun tirolez inclus",
        "Depozit schi securizat cu uscător clăpari",
        "Acces rapid Nordkette & ghețarul Stubai",
        "Ski bus gratuit cu Ski Pass"
      ],
      "priceTotal": 520,
      "pricePerPerson": 260,
      "link": "https://www.booking.com/hotel/at/hotel-maximilian.ro.html?checkin=2027-01-28&checkout=2027-02-02&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Hotel Boutique 4★",
        "name": "Hotel Maximilian - Stadthaus Penz 4★",
        "rating": 8.8,
        "priceTotal": 520,
        "pricePerPerson": 260,
        "type": "Cameră Dublă Confort",
        "link": "https://www.booking.com/hotel/at/hotel-maximilian.ro.html?checkin=2027-01-28&checkout=2027-02-02&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "4 – 9 Februarie 2027",
        "price": 270,
        "departureDate": "2027-02-04",
        "returnDate": "2027-02-09",
        "link": "https://www.google.com/maps/dir/Bucuresti/Innsbruck,+Austria"
      },
      {
        "dates": "18 – 23 Februarie 2027",
        "price": 280,
        "departureDate": "2027-02-18",
        "returnDate": "2027-02-23",
        "link": "https://www.google.com/maps/dir/Bucuresti/Innsbruck,+Austria"
      }
    ],
    "description": "Capitala mondială a sporturilor de iarnă! Innsbruck îmbină eleganța unui oraș imperial tirolez cu accesul la 13 domenii schiabile prin Olympia SkiWorld și zăpada impecabilă de pe ghețarul Stubai (3.210m). Telegondola futuristă Nordkette pleacă chiar din inima orașului.",
    "featured": True,
    "publishedAt": "2026-11-06T18:10:00.000Z"
  },
  {
    "id": "deal-ski-007",
    "slug": "vacanta-schi-zell-am-see-kaprun-austria-285-euro",
    "title": "Zăpadă Garantată la Zell am See & Kaprun: 5 nopți la Grand Hotel Zell am See 4★ pe Lac",
    "destination": "Zell am See & Kaprun (Austria)",
    "country": "Austria",
    "flag": "🇦🇹",
    "originCity": "București / România",
    "originCode": "AUTO",
    "destinationCode": "ZELLAMSEE",
    "dates": "20 – 25 Ianuarie 2027",
    "departureDate": "2027-01-20",
    "returnDate": "2027-01-25",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "❄️ Ghețar Kitzsteinhorn 3.029m",
    "image": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 285,
    "discountPercent": 40,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (mașină personală)",
      "airlineCode": "CAR",
      "route": "România → Viena → Salzburg → Zell am See (drum autostradă, vignietă Austria obligatorie)",
      "price": 0,
      "baggageInfo": "Bagaje și schiuri fără restricții în mașină",
      "link": "https://www.google.com/maps/dir/Bucuresti/Zell+am+See,+Austria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Zell+am+See,+Austria",
      "isConnecting": False
    },
    "hotel": {
      "name": "Grand Hotel Zell am See 4★ Superior",
      "provider": "Booking.com",
      "rating": 8.9,
      "reviewsCount": 2890,
      "distance": "Pe propria peninsulă pe malul lacului Zell, la 5 min de telecabina CityXpress",
      "amenities": [
        "Rooftop Panorama Spa cu vedere la lac",
        "Piscină interioară și saune alpine",
        "Acces la 138 km pârtii Zell am See - Kaprun",
        "Ghețarul Kitzsteinhorn cu schi la peste 3.000m"
      ],
      "priceTotal": 570,
      "pricePerPerson": 285,
      "link": "https://www.booking.com/hotel/at/grand-hotel-zell-am-see.ro.html?checkin=2027-01-20&checkout=2027-01-25&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Grand Hotel Iconic",
        "name": "Grand Hotel Zell am See 4★",
        "rating": 8.9,
        "priceTotal": 570,
        "pricePerPerson": 285,
        "type": "Cameră Dublă Confort cu vedere la lac",
        "link": "https://www.booking.com/hotel/at/grand-hotel-zell-am-see.ro.html?checkin=2027-01-20&checkout=2027-01-25&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "27 Ianuarie – 1 Februarie 2027",
        "price": 295,
        "departureDate": "2027-01-27",
        "returnDate": "2027-02-01",
        "link": "https://www.google.com/maps/dir/Bucuresti/Zell+am+See,+Austria"
      }
    ],
    "description": "Una din cele mai spectaculoase panorame din Alpii Austrieci! Lacul Zell înghețat și ghețarul Kitzsteinhorn (3.029m) garantează zăpadă 100% din toamnă până în primăvară târzie. Domeniul reunește 138 km de pârtii impecabile și conexiune modernă 3K K-onnection.",
    "featured": True,
    "publishedAt": "2026-11-06T18:12:00.000Z"
  },
  {
    "id": "deal-ski-008",
    "slug": "vacanta-schi-kitzbuhel-alpi-austria-295-euro",
    "title": "Schi Legendă la Kitzbühel: 5 nopți la Q! Hotel Maria Theresia 4★ lângă Telegondola Hahnenkamm",
    "destination": "Kitzbühel & Alpii Tirolezi (Austria)",
    "country": "Austria",
    "flag": "🇦🇹",
    "originCity": "București / România",
    "originCode": "AUTO",
    "destinationCode": "KITZBUHEL",
    "dates": "12 – 17 Februarie 2027",
    "departureDate": "2027-02-12",
    "returnDate": "2027-02-17",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🏆 Pârtia Streif & 233 km Pârtii",
    "image": "https://images.unsplash.com/photo-1544085311-11a028465b03?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 295,
    "discountPercent": 38,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (mașină personală)",
      "airlineCode": "CAR",
      "route": "România → Budapesta → Viena → Kufstein → Kitzbühel",
      "price": 0,
      "baggageInfo": "Schiuri și clăpari în mașină, fără bătăi de cap cu avioanele",
      "link": "https://www.google.com/maps/dir/Bucuresti/Kitzbuhel,+Austria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Kitzbuhel,+Austria",
      "isConnecting": False
    },
    "hotel": {
      "name": "Q! Hotel Maria Theresia Kitzbühel 4★",
      "provider": "Booking.com",
      "rating": 8.7,
      "reviewsCount": 1640,
      "distance": "În centrul stațiunii Kitzbühel, la 400m de telegondola Hahnenkammbahn",
      "amenities": [
        "Centru Spa & Saune tiroleze",
        "Lounge cu șemineu și après-ski elegant",
        "Depozit schi modern cu uscător clăpari",
        "Acces direct la domeniul KitzSki (233 km)"
      ],
      "priceTotal": 590,
      "pricePerPerson": 295,
      "link": "https://www.booking.com/hotel/at/q-hotel-maria-theresia.ro.html?checkin=2027-02-12&checkout=2027-02-17&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Boutique Alpin Kitzbühel",
        "name": "Q! Hotel Maria Theresia 4★",
        "rating": 8.7,
        "priceTotal": 590,
        "pricePerPerson": 295,
        "type": "Cameră Dublă Standard Alpină",
        "link": "https://www.booking.com/hotel/at/q-hotel-maria-theresia.ro.html?checkin=2027-02-12&checkout=2027-02-17&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "19 – 24 Februarie 2027",
        "price": 310,
        "departureDate": "2027-02-19",
        "returnDate": "2027-02-24",
        "link": "https://www.google.com/maps/dir/Bucuresti/Kitzbuhel,+Austria"
      }
    ],
    "description": "Legenda mondială a schiului alpin! Aici se desfășoară cea mai faimoasă cursă de coborâre din lume pe pârtia Streif. Domeniul KitzSki pune la dispoziție 233 km de pârtii excelente, 57 de instalații pe cablu ultra-moderne și o atmosferă après-ski de neegalat.",
    "featured": False,
    "publishedAt": "2026-11-06T18:14:00.000Z"
  },
  {
    "id": "deal-ski-009",
    "slug": "vacanta-schi-schladming-dachstein-austria-240-euro",
    "title": "Schi pe 4 Munți Conectați la Schladming: 4 nopți la TUI BLUE Schladming 3★ lângă Telegondola Planai",
    "destination": "Schladming - Dachstein (Stiria, Austria)",
    "country": "Austria",
    "flag": "🇦🇹",
    "originCity": "București / România",
    "originCode": "AUTO",
    "destinationCode": "SCHLADMING",
    "dates": "15 – 19 Ianuarie 2027",
    "departureDate": "2027-01-15",
    "returnDate": "2027-01-19",
    "nights": 4,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "⛷️ 4 Munți Conectați & 230 km Pârtii",
    "image": "https://images.unsplash.com/photo-1546948630-1149ea60dc86?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 240,
    "discountPercent": 45,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (mașină personală)",
      "airlineCode": "CAR",
      "route": "România → Budapesta → Graz / Liezen → Schladming (~1.050 km, cea mai apropiată mare stațiune austriacă)",
      "price": 0,
      "baggageInfo": "Echipament complet în mașină",
      "link": "https://www.google.com/maps/dir/Bucuresti/Schladming,+Austria",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Schladming,+Austria",
      "isConnecting": False
    },
    "hotel": {
      "name": "TUI BLUE Schladming 3★ Superior",
      "provider": "Booking.com",
      "rating": 8.8,
      "reviewsCount": 2100,
      "distance": "Chiar vizavi de stația de plecare a telegondolei Planai",
      "amenities": [
        "SkySauna pe acoperiș cu vedere la Planai",
        "Depozit securizat de schi cu uscător",
        "Amplasare imbatabilă la 50m de gondolă",
        "Acces la leagănul celor 4 munți (Hauser Kaibling, Planai, Hochwurzen, Reiteralm)"
      ],
      "priceTotal": 480,
      "pricePerPerson": 240,
      "link": "https://www.booking.com/hotel/at/tui-blue-schladming.ro.html?checkin=2027-01-15&checkout=2027-01-19&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Design Hotel Planai",
        "name": "TUI BLUE Schladming 3★",
        "rating": 8.8,
        "priceTotal": 480,
        "pricePerPerson": 240,
        "type": "Cameră Dublă DUO",
        "link": "https://www.booking.com/hotel/at/tui-blue-schladming.ro.html?checkin=2027-01-15&checkout=2027-01-19&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "22 – 26 Ianuarie 2027",
        "price": 249,
        "departureDate": "2027-01-22",
        "returnDate": "2027-01-26",
        "link": "https://www.google.com/maps/dir/Bucuresti/Schladming,+Austria"
      }
    ],
    "description": "Cea mai accesibilă destinație austriacă din România! Schladming leagă 4 munți într-un singur leagăn de schi cu peste 230 km de pârtii. Hotelul TUI BLUE este amplasat chiar lângă telegondola Planai și oferă o saună panoramică pe acoperiș.",
    "featured": False,
    "publishedAt": "2026-11-06T18:16:00.000Z"
  },

  # ==========================================
  # ITALIA — CU ZBOR DIRECT LOW-COST INCLUS
  # ==========================================
  {
    "id": "deal-ski-002",
    "slug": "vacanta-schi-dolomiti-val-di-fassa-din-bucuresti-289-euro",
    "title": "Schi în Dolomiți & Sellaronda: 5 nopți în Val di Fassa la Hotel Il Caminetto 3★ cu Spa + Zbor Milano",
    "destination": "Dolomiți (Val di Fassa & Canazei)",
    "country": "Italia",
    "flag": "🇮🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "BGY",
    "dates": "22 – 27 Ianuarie 2027",
    "departureDate": "2027-01-22",
    "returnDate": "2027-01-27",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "⛷️ Dolomiti Superski & Sellaronda",
    "image": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 289,
    "discountPercent": 48,
    "transportType": "flight",
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – BGY (Direct Milano Bergamo)",
      "price": 49,
      "baggageInfo": "Rucsac gratuit 40×20×25 cm inclus (echipament sportiv opțional)",
      "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-22&dateIn=2027-01-27&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY",
      "directAirlineLink": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-22&dateIn=2027-01-27&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BGY%20on%202027-01-22%20returning%202027-01-27&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/bgy/270122/270127/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/bgy/2027-01-22/2027-01-27?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-BGY/2027-01-22/2027-01-27/2adults",
      "isConnecting": False
    },
    "alternativeAirlines": [
      {
        "name": "Wizz Air",
        "price": 55,
        "route": "OTP – BGY (Direct)"
      }
    ],
    "hotel": {
      "name": "Hotel Il Caminetto Sport Canazei 3★",
      "provider": "Booking.com",
      "rating": 8.4,
      "reviewsCount": 1240,
      "distance": "În Canazei, la 700m de telecabina Canazei-Pecol (acces direct Sellaronda)",
      "amenities": [
        "Centru Wellness & Piscină",
        "Saună tiroleză & Baie turcească",
        "Depozit clăpari încălzit",
        "Ski bus chiar în fața hotelului"
      ],
      "priceTotal": 480,
      "pricePerPerson": 240,
      "link": "https://www.booking.com/hotel/it/il-caminetto-sport-canazei.ro.html?checkin=2027-01-22&checkout=2027-01-27&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Hotel Wellness Canazei",
        "name": "Hotel Il Caminetto Sport 3★",
        "rating": 8.4,
        "priceTotal": 480,
        "pricePerPerson": 240,
        "type": "Cameră Dublă Clasică",
        "link": "https://www.booking.com/hotel/it/il-caminetto-sport-canazei.ro.html?checkin=2027-01-22&checkout=2027-01-27&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "15 – 20 Ianuarie 2027",
        "price": 295,
        "departureDate": "2027-01-15",
        "returnDate": "2027-01-20",
        "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-15&dateIn=2027-01-20&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY"
      }
    ],
    "description": "Experiența supremă la schi pe tărâmul munților Dolomiți (patrimoniu UNESCO)! Ai acces direct la legendarul circuit Sellaronda cu 4 trecători alpine și 1.200 km de pârtii în Dolomiti Superski, combinate cu preparate culinare italiene și relaxare la spa.",
    "featured": True,
    "publishedAt": "2026-11-06T18:05:00.000Z"
  },
  {
    "id": "deal-ski-010",
    "slug": "vacanta-schi-livigno-duty-free-italia-din-bucuresti-309-euro",
    "title": "Schi & Shopping Duty-Free la Livigno: 5 nopți la Hotel Piccolo Tibet 3★ + Zbor Milano",
    "destination": "Livigno (Alpii Italieni)",
    "country": "Italia",
    "flag": "🇮🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "BGY",
    "dates": "20 – 25 Ianuarie 2027",
    "departureDate": "2027-01-20",
    "returnDate": "2027-01-25",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🛍️ Zonă Duty-Free & 115 km Pârtii",
    "image": "https://images.unsplash.com/photo-1551524559-8af4e6624178?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 309,
    "discountPercent": 42,
    "transportType": "flight",
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – BGY (Direct Milano Bergamo) + Transfer Livigno",
      "price": 49,
      "baggageInfo": "Rucsac gratuit 40×20×25 cm inclus",
      "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-20&dateIn=2027-01-25&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY",
      "directAirlineLink": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-20&dateIn=2027-01-25&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BGY%20on%202027-01-20%20returning%202027-01-25&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/bgy/270120/270125/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/bgy/2027-01-20/2027-01-25?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-BGY/2027-01-20/2027-01-25/2adults",
      "isConnecting": False
    },
    "hotel": {
      "name": "Hotel Piccolo Tibet 3★",
      "provider": "Booking.com",
      "rating": 8.9,
      "reviewsCount": 980,
      "distance": "În Livigno, la 200m de zona pietonală duty-free și de telescaunul Doss",
      "amenities": [
        "Saună finlandeză și zonă relaxare",
        "Mic dejun bogat cu produse locale din Valtellina",
        "Depozit clăpari încălzit",
        "Ski bus gratuit la 50m"
      ],
      "priceTotal": 520,
      "pricePerPerson": 260,
      "link": "https://www.booking.com/hotel/it/hotel-piccolo-tibet.ro.html?checkin=2027-01-20&checkout=2027-01-25&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Alpin Livigno",
        "name": "Hotel Piccolo Tibet 3★",
        "rating": 8.9,
        "priceTotal": 520,
        "pricePerPerson": 260,
        "type": "Cameră Dublă Confort",
        "link": "https://www.booking.com/hotel/it/hotel-piccolo-tibet.ro.html?checkin=2027-01-20&checkout=2027-01-25&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "3 – 8 Februarie 2027",
        "price": 319,
        "departureDate": "2027-02-03",
        "returnDate": "2027-02-08",
        "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-02-03&dateIn=2027-02-08&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY"
      }
    ],
    "description": "Supranumit «Micul Tibet» datorită altitudinii de peste 1.800m și a zăpezii pudră impecabile, Livigno este un paradis unic: 115 km de pârtii, cele mai bune snowpark-uri din Europa și statut complet de zonă scutită de taxe (Duty-Free) pentru cumpărături.",
    "featured": False,
    "publishedAt": "2026-11-06T18:18:00.000Z"
  },
  {
    "id": "deal-ski-011",
    "slug": "vacanta-schi-cortina-dampezzo-dolomiti-din-bucuresti-320-euro",
    "title": "Schi Olimpic la Cortina d'Ampezzo: 5 nopți la Hotel Meublé Oasi 3★ + Zbor Veneția/Treviso",
    "destination": "Cortina d'Ampezzo (Dolomiți, Italia)",
    "country": "Italia",
    "flag": "🇮🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "TSF",
    "dates": "26 – 31 Ianuarie 2027",
    "departureDate": "2027-01-26",
    "returnDate": "2027-01-31",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "👑 Perla Dolomiților & Tofana",
    "image": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 320,
    "discountPercent": 40,
    "transportType": "flight",
    "flight": {
      "airline": "Ryanair",
      "airlineCode": "FR",
      "route": "OTP – TSF (Direct Veneția Treviso) + Cortina Express",
      "price": 45,
      "baggageInfo": "Rucsac gratuit 40×20×25 cm inclus",
      "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-26&dateIn=2027-01-31&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=TSF",
      "directAirlineLink": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-26&dateIn=2027-01-31&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=TSF",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20TSF%20on%202027-01-26%20returning%202027-01-31&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/tsf/270126/270131/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/tsf/2027-01-26/2027-01-31?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-TSF/2027-01-26/2027-01-31/2adults",
      "isConnecting": False
    },
    "hotel": {
      "name": "Hotel Meublé Oasi 3★",
      "provider": "Booking.com",
      "rating": 9.1,
      "reviewsCount": 840,
      "distance": "La 300m de Corso Italia și aproape de telecabina Freccia nel Cielo (Tofana)",
      "amenities": [
        "Vedere panoramică spre masivul Tofane",
        "Mic dejun italian excelent inclus",
        "Depozit schi securizat",
        "Parcare gratuită"
      ],
      "priceTotal": 550,
      "pricePerPerson": 275,
      "link": "https://www.booking.com/hotel/it/meuble-oasi.ro.html?checkin=2027-01-26&checkout=2027-01-31&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Hotel Panoramic Cortina",
        "name": "Hotel Meublé Oasi 3★",
        "rating": 9.1,
        "priceTotal": 550,
        "pricePerPerson": 275,
        "type": "Cameră Dublă cu vedere la munte",
        "link": "https://www.booking.com/hotel/it/meuble-oasi.ro.html?checkin=2027-01-26&checkout=2027-01-31&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "9 – 14 Februarie 2027",
        "price": 335,
        "departureDate": "2027-02-09",
        "returnDate": "2027-02-14",
        "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-02-09&dateIn=2027-02-14&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=TSF"
      }
    ],
    "description": "Perla absolută a Dolomiților și viitoarea gazdă a Jocurilor Olimpice de Iarnă 2026! Pârtiile legendare de pe Tofana, Faloria și Cristallo oferă cele mai dramatice peisaje alpine din lume, completate de rafinamentul unui orășel montan celebru.",
    "featured": False,
    "publishedAt": "2026-11-06T18:20:00.000Z"
  },

  # ==========================================
  # SLOVACIA — TRANSPORT PROPRIU / FĂRĂ AVION
  # ==========================================
  {
    "id": "deal-ski-004",
    "slug": "vacanta-schi-jasna-chopok-slovacia-hotel-jasna-195-euro",
    "title": "Schi la Jasná Nízke Tatry: 5 nopți la Hotel Jasná 3★ la Baza Muntelui Chopok (Transport Propriu)",
    "destination": "Jasná Chopok (Munții Tatra, Slovacia)",
    "country": "Slovacia",
    "flag": "🇸🇰",
    "originCity": "București / Satu Mare / Cluj",
    "originCode": "AUTO",
    "destinationCode": "JASNA",
    "dates": "12 – 17 Februarie 2027",
    "departureDate": "2027-02-12",
    "returnDate": "2027-02-17",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🏂 50 km Pârtii + Băi Termale Tatralandia",
    "image": "https://images.unsplash.com/photo-1546948630-1149ea60dc86?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 195,
    "discountPercent": 42,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (cu mașina personală)",
      "airlineCode": "CAR",
      "route": "România (Oradea/Satu Mare) → Debrecen → Miskolc → Košice → Poprad → Jasná (acces facil 6h din nord-vestul RO)",
      "price": 0,
      "baggageInfo": "Spațiu nelimitat în portbagaj pentru echipament și schiuri",
      "link": "https://www.google.com/maps/dir/Bucuresti/Jasna,+Slovakia",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Jasna,+Slovakia",
      "isConnecting": False
    },
    "hotel": {
      "name": "Hotel Jasná 3★",
      "provider": "Booking.com",
      "rating": 8.5,
      "reviewsCount": 970,
      "distance": "La poalele muntelui Chopok, la 800m de instalația Grand Jet Jasná",
      "amenities": [
        "Restaurant tradițional slovac",
        "Saună uscată & depozit echipament",
        "Shuttle pârtie inclus",
        "Reducere intrare Aquapark Tatralandia"
      ],
      "priceTotal": 390,
      "pricePerPerson": 195,
      "link": "https://www.booking.com/hotel/sk/hotel-jasna.ro.html?checkin=2027-02-12&checkout=2027-02-17&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Hotel la Pârtie",
        "name": "Hotel Jasná 3★",
        "rating": 8.5,
        "priceTotal": 390,
        "pricePerPerson": 195,
        "type": "Cameră Dublă Standard",
        "link": "https://www.booking.com/hotel/sk/hotel-jasna.ro.html?checkin=2027-02-12&checkout=2027-02-17&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "19 – 24 Februarie 2027",
        "price": 205,
        "departureDate": "2027-02-19",
        "returnDate": "2027-02-24",
        "link": "https://www.google.com/maps/dir/Bucuresti/Jasna,+Slovakia"
      }
    ],
    "description": "Cea mai modernă stațiune de schi din Europa Centrală! 50 km de pârtii impecabile deservite de telegondole ultra-rapide Doppelmayr Funitel pe ambii versanți ai muntelui Chopok. După schi, te relaxezi la celebrele bazine termale exterioare de la Tatralandia sau Bešeňová.",
    "featured": False,
    "publishedAt": "2026-11-06T18:15:00.000Z"
  },
  {
    "id": "deal-ski-012",
    "slug": "vacanta-schi-tatranska-lomnica-slovacia-180-euro",
    "title": "Schi la Înălțime în Tatra Mare: 4 nopți la Horizont Resort 4★ cu Spa la Tatranská Lomnica",
    "destination": "Vysoké Tatry (Munții Tatra Mare, Slovacia)",
    "country": "Slovacia",
    "flag": "🇸🇰",
    "originCity": "București / Nord-Vest RO",
    "originCode": "AUTO",
    "destinationCode": "TATRY",
    "dates": "5 – 9 Februarie 2027",
    "departureDate": "2027-02-05",
    "returnDate": "2027-02-09",
    "nights": 4,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🏔️ Diferență Nivel 1.300m & Spa Cedru",
    "image": "https://images.unsplash.com/photo-1551524559-8af4e6624178?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 180,
    "discountPercent": 40,
    "transportType": "car",
    "flight": {
      "airline": "Transport propriu (cu mașina personală)",
      "airlineCode": "CAR",
      "route": "România → Košice → Poprad → Stará Lesná / Tatranská Lomnica",
      "price": 0,
      "baggageInfo": "Echipament schi în portbagaj",
      "link": "https://www.google.com/maps/dir/Bucuresti/Tatranska+Lomnica,+Slovakia",
      "directAirlineLink": "https://www.google.com/maps/dir/Bucuresti/Tatranska+Lomnica,+Slovakia",
      "isConnecting": False
    },
    "hotel": {
      "name": "Horizont Resort 4★",
      "provider": "Booking.com",
      "rating": 9.0,
      "reviewsCount": 1870,
      "distance": "La 2 km de pârtiile din Tatranská Lomnica (shuttle gratuit hotel)",
      "amenities": [
        "Mountain Wellness Center din lemn de cedru",
        "Piscină interioară cu bar acvatic",
        "Vedere panoramică spre vârfurile Tatra Mare",
        "Depozit gratuit schi și uscător"
      ],
      "priceTotal": 360,
      "pricePerPerson": 180,
      "link": "https://www.booking.com/hotel/sk/horizont-resort.ro.html?checkin=2027-02-05&checkout=2027-02-09&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Wellness Resort 4★",
        "name": "Horizont Resort 4★",
        "rating": 9.0,
        "priceTotal": 360,
        "pricePerPerson": 180,
        "type": "Cameră Standard cu vedere la munte",
        "link": "https://www.booking.com/hotel/sk/horizont-resort.ro.html?checkin=2027-02-05&checkout=2027-02-09&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "12 – 16 Februarie 2027",
        "price": 189,
        "departureDate": "2027-02-12",
        "returnDate": "2027-02-16",
        "link": "https://www.google.com/maps/dir/Bucuresti/Tatranska+Lomnica,+Slovakia"
      }
    ],
    "description": "Aici se află pârtia cu cea mai abruptă cădere și cea mai mare diferență de nivel din Carpați: 1.300 metri de la șaua Lomnické sedlo (2.190m) până în vale! Horizont Resort oferă un centru spa spectaculos construit din lemn de cedru și vedere la crestele alpine.",
    "featured": False,
    "publishedAt": "2026-11-06T18:22:00.000Z"
  },

  # ==========================================
  # FRANȚA — CU ZBOR DIRECT GENEVA INCLUS
  # ==========================================
  {
    "id": "deal-ski-013",
    "slug": "vacanta-schi-val-thorens-trei-vai-franta-din-bucuresti-350-euro",
    "title": "Schi în Cel Mai Mare Domeniu Schiabil din Lume: 5 nopți la Résidence Le Chamois d'Or în Val Thorens + Zbor Geneva",
    "destination": "Val Thorens & Les 3 Vallées (Franța)",
    "country": "Franța",
    "flag": "🇫🇷",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "GVA",
    "dates": "13 – 18 Ianuarie 2027",
    "departureDate": "2027-01-13",
    "returnDate": "2027-01-18",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "👑 600 km Pârtii & Cota 2.300m",
    "image": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 350,
    "discountPercent": 46,
    "transportType": "flight",
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – GVA (Direct Geneva) + Shuttle Alpi Val Thorens",
      "price": 65,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/GVA/2027-01-13/2027-01-18/2/0/0/null",
      "directAirlineLink": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/GVA/2027-01-13/2027-01-18/2/0/0/null",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20GVA%20on%202027-01-13%20returning%202027-01-18&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/gva/270113/270118/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/gva/2027-01-13/2027-01-18?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-GVA/2027-01-13/2027-01-18/2adults",
      "isConnecting": False
    },
    "hotel": {
      "name": "Résidence Le Chamois d'Or 3★",
      "provider": "Booking.com",
      "rating": 8.6,
      "reviewsCount": 1150,
      "distance": "Direct pe pârtiile din Val Thorens (altitudine 2.300m, ski-in/ski-out)",
      "amenities": [
        "Acces direct la 600 km de pârtii (Les 3 Vallées)",
        "Bucătărie utilată și balcon cu vedere alpină",
        "Supermarket și magazin de închirieri schi în clădire",
        "Cea mai înaltă stațiune din Europa (zăpadă garantată)"
      ],
      "priceTotal": 570,
      "pricePerPerson": 285,
      "link": "https://www.booking.com/hotel/fr/residence-le-chamois-d-or.ro.html?checkin=2027-01-13&checkout=2027-01-18&group_adults=2&no_rooms=1"
    },
    "accommodationOptions": [
      {
        "provider": "Booking.com",
        "providerId": "booking",
        "badge": "🏨 Ski-to-door Val Thorens",
        "name": "Résidence Le Chamois d'Or 3★",
        "rating": 8.6,
        "priceTotal": 570,
        "pricePerPerson": 285,
        "type": "Studio cu balcon și chicinetă",
        "link": "https://www.booking.com/hotel/fr/residence-le-chamois-d-or.ro.html?checkin=2027-01-13&checkout=2027-01-18&group_adults=2&no_rooms=1"
      }
    ],
    "alternativeDates": [
      {
        "dates": "20 – 25 Ianuarie 2027",
        "price": 365,
        "departureDate": "2027-01-20",
        "returnDate": "2027-01-25",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/GVA/2027-01-20/2027-01-25/2/0/0/null"
      }
    ],
    "description": "Visul oricărui schior: cel mai vast domeniu schiabil din lume (Les 3 Vallées — 600 km de pârtii legate) și stațiunea situată la cea mai mare altitudine din Europa (2.300m). Cazarea la Résidence Le Chamois d'Or oferă acces direct pe pârtie (ski-in/ski-out) din ușa clădirii.",
    "featured": True,
    "publishedAt": "2026-11-06T18:25:00.000Z"
  }
]

final_deals = base_deals + ski_deals

with open(DEALS_PATH, "w", encoding="utf-8") as f:
    json.dump(final_deals, f, indent=2, ensure_ascii=False)

print(f"Salvat deals.json cu succes! Total oferte: {len(final_deals)} (din care {len(ski_deals)} oferte de schi internationale)")
