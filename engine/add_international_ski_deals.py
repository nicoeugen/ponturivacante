import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DEALS_PATH = "data/deals.json"
deals = json.load(open(DEALS_PATH, encoding="utf-8"))

existing_ids = {d["id"] for d in deals}

new_ski_deals = [
  {
    "id": "deal-ski-001",
    "slug": "vacanta-schi-bansko-bulgaria-din-bucuresti-149-euro",
    "title": "Schi la Bansko: 4 nopți la Green Life Ski & Spa Resort 4★ cu Piscină & Spa + Zbor Sofia",
    "destination": "Bansko (Munții Pirin)",
    "country": "Bulgaria",
    "flag": "🇧🇬",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "SOF",
    "dates": "5 – 9 Februarie 2027",
    "departureDate": "2027-02-05",
    "returnDate": "2027-02-09",
    "nights": 4,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🎿 75 km Pârtii + Spa",
    "image": "https://images.unsplash.com/photo-1551524559-8af4e6624178?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 149,
    "discountPercent": 52,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – SOF (Direct)",
      "price": 39,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus (echipament schi la cală opțional)",
      "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/SOF/2027-02-05/2027-02-09/2/0/0/null",
      "directAirlineLink": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/SOF/2027-02-05/2027-02-09/2/0/0/null",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20SOF%20on%202027-02-05%20returning%202027-02-09&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/sof/270205/270209/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/sof/2027-02-05/2027-02-09?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-SOF/2027-02-05/2027-02-09/2adults",
      "isConnecting": False
    },
    "alternativeAirlines": [
      {
        "name": "Ryanair",
        "price": 45,
        "route": "OTP – SOF (Direct)"
      }
    ],
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
      },
      {
        "provider": "Hostelworld",
        "providerId": "hostelworld",
        "badge": "🎒 Budget Ski Lodge",
        "name": "Bansko Ski Hostel Lodge",
        "rating": 8.5,
        "priceTotal": 90,
        "pricePerPerson": 45,
        "type": "Pat în cameră comună",
        "link": "https://www.hostelworld.com/pwa/wds/hosteldetails.php/Bansko/Bulgaria"
      }
    ],
    "alternativeDates": [
      {
        "dates": "22 – 26 Ianuarie 2027",
        "price": 145,
        "departureDate": "2027-01-22",
        "returnDate": "2027-01-26",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/SOF/2027-01-22/2027-01-26/2/0/0/null",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-SOF/2027-01-22/2027-01-26/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20SOF%20on%202027-01-22%20returning%202027-01-26&curr=EUR&hl=ro"
      },
      {
        "dates": "12 – 16 Februarie 2027",
        "price": 159,
        "departureDate": "2027-02-12",
        "returnDate": "2027-02-16",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/SOF/2027-02-12/2027-02-16/2/0/0/null",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-SOF/2027-02-12/2027-02-16/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20SOF%20on%202027-02-12%20returning%202027-02-16&curr=EUR&hl=ro"
      }
    ],
    "description": "Cea mai avantajoasă vacanță la schi din Europa! Peste 75 km de pârtii amenajate pe versantul muntelui Todorka (2.600m), telegondolă modernă și relaxare totală la centrul spa cu piscine încălzite al resortului 4★ Green Life.",
    "featured": True,
    "publishedAt": "2026-11-06T18:00:00.000Z"
  },
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
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Residence Lores Canazei",
        "rating": 8.5,
        "priceTotal": 450,
        "pricePerPerson": 225,
        "type": "Apartament Alpin cu chicinetă",
        "link": "https://www.agoda.com/ro-ro/residence-lores/hotel/canazei-it.html?checkIn=2027-01-22&checkOut=2027-01-27&rooms=1&adults=2"
      }
    ],
    "alternativeDates": [
      {
        "dates": "15 – 20 Ianuarie 2027",
        "price": 295,
        "departureDate": "2027-01-15",
        "returnDate": "2027-01-20",
        "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-15&dateIn=2027-01-20&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-BGY/2027-01-15/2027-01-20/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BGY%20on%202027-01-15%20returning%202027-01-20&curr=EUR&hl=ro"
      },
      {
        "dates": "29 Ianuarie – 3 Februarie 2027",
        "price": 310,
        "departureDate": "2027-01-29",
        "returnDate": "2027-02-03",
        "link": "https://www.ryanair.com/ro/ro/trip/flights/select?adults=2&teens=0&children=0&infants=0&dateOut=2027-01-29&dateIn=2027-02-03&isConnectedFlight=false&isReturn=true&originIata=OTP&destinationIata=BGY",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-BGY/2027-01-29/2027-02-03/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BGY%20on%202027-01-29%20returning%202027-02-03&curr=EUR&hl=ro"
      }
    ],
    "description": "Experiența supremă la schi pe tărâmul munților Dolomiți (patrimoniu UNESCO)! Ai acces direct la legendarul circuit Sellaronda cu 4 trecători alpine și 1.200 km de pârtii în Dolomiti Superski, combinate cu preparate culinare italiene și relaxare la spa.",
    "featured": True,
    "publishedAt": "2026-11-06T18:05:00.000Z"
  },
  {
    "id": "deal-ski-003",
    "slug": "vacanta-schi-tirol-innsbruck-austria-din-bucuresti-319-euro",
    "title": "Schi în Tirolul Austriac: 5 nopți la Hotel Maximilian 4★ în Centrul Istoric Innsbruck + Zbor Direct",
    "destination": "Tirol & Innsbruck (Austria)",
    "country": "Austria",
    "flag": "🇦🇹",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "FMM",
    "dates": "28 Ianuarie – 2 Februarie 2027",
    "departureDate": "2027-01-28",
    "returnDate": "2027-02-02",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🏔️ 13 Domenii Schiabile & Ghețar",
    "image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 319,
    "discountPercent": 45,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – FMM (Direct Memmingen / Allgäu - Poarta Tirolului)",
      "price": 59,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/FMM/2027-01-28/2027-02-02/2/0/0/null",
      "directAirlineLink": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/FMM/2027-01-28/2027-02-02/2/0/0/null",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20FMM%20on%202027-01-28%20returning%202027-02-02&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/fmm/270128/270202/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/fmm/2027-01-28/2027-02-02?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-FMM/2027-01-28/2027-02-02/2adults",
      "isConnecting": False
    },
    "alternativeAirlines": [
      {
        "name": "Ryanair (Zbor Viena + ÖBB Railjet)",
        "price": 65,
        "route": "OTP – VIE (Direct)"
      }
    ],
    "hotel": {
      "name": "Hotel Maximilian - Stadthaus Penz 4★",
      "provider": "Booking.com",
      "rating": 8.8,
      "reviewsCount": 2380,
      "distance": "În centrul vechi din Innsbruck, lângă Acoperișul de Aur și stația telegondolei Nordkette",
      "amenities": [
        "Mic dejun tirolez inclus",
        "Depozit schi securizat",
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
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Hotel Central Innsbruck 4★",
        "rating": 8.5,
        "priceTotal": 490,
        "pricePerPerson": 245,
        "type": "Cameră Standard Dublă",
        "link": "https://www.agoda.com/ro-ro/hotel-central/hotel/innsbruck-at.html?checkIn=2027-01-28&checkOut=2027-02-02&rooms=1&adults=2"
      }
    ],
    "alternativeDates": [
      {
        "dates": "4 – 9 Februarie 2027",
        "price": 329,
        "departureDate": "2027-02-04",
        "returnDate": "2027-02-09",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/FMM/2027-02-04/2027-02-09/2/0/0/null",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-FMM/2027-02-04/2027-02-09/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20FMM%20on%202027-02-04%20returning%202027-02-09&curr=EUR&hl=ro"
      },
      {
        "dates": "18 – 23 Februarie 2027",
        "price": 339,
        "departureDate": "2027-02-18",
        "returnDate": "2027-02-23",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/FMM/2027-02-18/2027-02-23/2/0/0/null",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-FMM/2027-02-18/2027-02-23/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20FMM%20on%202027-02-18%20returning%202027-02-23&curr=EUR&hl=ro"
      }
    ],
    "description": "Capitala mondială a sporturilor de iarnă! Innsbruck îmbină eleganța unui oraș imperial tirolez cu accesul la 13 domenii schiabile prin Olympia SkiWorld și zăpada impecabilă de pe ghețarul Stubai (3.210m). Telegondola futuristă Nordkette pleacă chiar din inima orașului.",
    "featured": True,
    "publishedAt": "2026-11-06T18:10:00.000Z"
  },
  {
    "id": "deal-ski-004",
    "slug": "vacanta-schi-jasna-chopok-slovacia-din-bucuresti-239-euro",
    "title": "Schi la Jasná Nízke Tatry: 5 nopți la Hotel Jasná 3★ la baza muntelui Chopok + Zbor",
    "destination": "Jasná Chopok (Munții Tatra, Slovacia)",
    "country": "Slovacia",
    "flag": "🇸🇰",
    "originCity": "București",
    "originCode": "OTP",
    "destinationCode": "BUD",
    "dates": "12 – 17 Februarie 2027",
    "departureDate": "2027-02-12",
    "returnDate": "2027-02-17",
    "nights": 5,
    "category": "Schi & Sporturi de Iarnă",
    "badge": "🏂 50 km Pârtii + Băi Termale Tatralandia",
    "image": "https://images.unsplash.com/photo-1546948630-1149ea60dc86?auto=format&fit=crop&w=1200&q=80",
    "priceTotalPerPerson": 239,
    "discountPercent": 46,
    "flight": {
      "airline": "Wizz Air",
      "airlineCode": "W6",
      "route": "OTP – BUD (Direct Budapesta - Transfer rapid Tatra)",
      "price": 44,
      "baggageInfo": "Rucsac gratuit 40×30×20 cm inclus",
      "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/BUD/2027-02-12/2027-02-17/2/0/0/null",
      "directAirlineLink": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/BUD/2027-02-12/2027-02-17/2/0/0/null",
      "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BUD%20on%202027-02-12%20returning%202027-02-17&curr=EUR&hl=ro",
      "skyscannerLink": "https://www.skyscanner.ro/transport/zboruri/otp/bud/270212/270217/?adultsv2=2",
      "kiwiLink": "https://www.kiwi.com/ro/search/results/otp/bud/2027-02-12/2027-02-17?adults=2",
      "momondoLink": "https://www.momondo.ro/flight-search/OTP-BUD/2027-02-12/2027-02-17/2adults",
      "isConnecting": False
    },
    "alternativeAirlines": [
      {
        "name": "Ryanair",
        "price": 49,
        "route": "OTP – VIE (Direct Viena)"
      }
    ],
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
      },
      {
        "provider": "Agoda",
        "providerId": "agoda",
        "badge": "⚡ Ofertă Agoda",
        "name": "Wellness Hotel Chopok 4★",
        "rating": 9.1,
        "priceTotal": 480,
        "pricePerPerson": 240,
        "type": "Cameră Confort cu acces Wellness",
        "link": "https://www.agoda.com/ro-ro/wellness-hotel-chopok/hotel/demanovska-dolina-sk.html?checkIn=2027-02-12&checkOut=2027-02-17&rooms=1&adults=2"
      }
    ],
    "alternativeDates": [
      {
        "dates": "19 – 24 Februarie 2027",
        "price": 245,
        "departureDate": "2027-02-19",
        "returnDate": "2027-02-24",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/BUD/2027-02-19/2027-02-24/2/0/0/null",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-BUD/2027-02-19/2027-02-24/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BUD%20on%202027-02-19%20returning%202027-02-24&curr=EUR&hl=ro"
      },
      {
        "dates": "26 Februarie – 3 Martie 2027",
        "price": 229,
        "departureDate": "2027-02-26",
        "returnDate": "2027-03-03",
        "link": "https://www.wizzair.com/ro-ro/booking/select-flight/OTP/BUD/2027-02-26/2027-03-03/2/0/0/null",
        "momondoLink": "https://www.momondo.ro/flight-search/OTP-BUD/2027-02-26/2027-03-03/2adults",
        "googleFlightsLink": "https://www.google.com/travel/flights?q=Round%20trip%20flights%20from%20OTP%20to%20BUD%20on%202027-02-26%20returning%202027-03-03&curr=EUR&hl=ro"
      }
    ],
    "description": "Cea mai modernă stațiune de schi din Europa Centrală! 50 km de pârtii impecabile deservite de telegondole ultra-rapide Doppelmayr Funitel pe ambii versanți ai muntelui Chopok. După schi, te relaxezi la celebrele bazine termale exterioare de la Tatralandia sau Bešeňová.",
    "featured": True,
    "publishedAt": "2026-11-06T18:15:00.000Z"
  }
]

added = 0
for d in new_ski_deals:
    if d["id"] not in existing_ids:
        deals.append(d)
        added += 1

with open(DEALS_PATH, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print(f"Adaugate cu succes: {added} oferte schi internationale. Total deals acum: {len(deals)}")
