import json

ro_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/romania_deals.json"
with open(ro_path, "r", encoding="utf-8") as f:
    ro_deals = json.load(f)

# Verificam daca exista deja oferte de schi
existing_ids = [d["id"] for d in ro_deals]

ski_deals = [
    {
        "id": "ro-007",
        "slug": "weekend-schi-poiana-brasov-alpin-resort",
        "title": "Weekend la Schi în Poiana Brașov: 2 nopți la Alpin Resort Hotel 4★ cu Piscină & Spa",
        "destination": "Poiana Brașov (Masivul Postăvaru)",
        "county": "Brașov",
        "region": "Transilvania",
        "category": "Schi & Pârtii",
        "badge": "🎿 Masivul Postăvaru (24 km pârtii)",
        "image": "https://images.unsplash.com/photo-1551524559-8af4e6624178?auto=format&fit=crop&w=1200&q=80",
        "priceTotalPerPerson": 110,
        "priceRoomTotal": 220,
        "minNights": 2,
        "capacity": "2 persoane",
        "voucherAccepted": True,
        "amenities": [
            "Shuttle gratuit direct la telegondolă și pârtii",
            "Depozit încălzit pentru schiuri și clăpari",
            "Piscină semi-olimpică încălzită & zonă Vitarium Spa",
            "Mic dejun bogat inclus",
            "Acceptă tichete & carduri de vacanță"
        ],
        "description": "Bucură-te de cel mai extins domeniu schiabil din România! Pârtia Drumul Roșu, Sulinar și Kanzel cu zăpadă excelentă, urmate de relaxare la piscina caldă și saunele de la Alpin Resort.",
        "bookingUrl": "https://www.booking.com/hotel/ro/aparthotel-alpin.ro.html?checkin=2027-01-15&checkout=2027-01-17&group_adults=2&no_rooms=1",
        "featured": True,
        "publishedAt": "2026-11-06T18:00:00Z"
    },
    {
        "id": "ro-008",
        "slug": "weekend-schi-sinaia-cota-2000-hotel-cerbul",
        "title": "Schi la Altitudine în Sinaia: 2 nopți la Hotel Cerbul 3★ lângă Telegondolă (Cota 2000)",
        "destination": "Sinaia (Valea Prahovei)",
        "county": "Prahova",
        "region": "Muntenia",
        "category": "Schi & Pârtii",
        "badge": "🎿 Pârtii la Cota 2000",
        "image": "https://images.unsplash.com/photo-1565992441121-4367c2967103?auto=format&fit=crop&w=1200&q=80",
        "priceTotalPerPerson": 59,
        "priceRoomTotal": 118,
        "minNights": 2,
        "capacity": "2 persoane",
        "voucherAccepted": True,
        "amenities": [
            "La 500m de Telegondola Sinaia spre Cota 1400/2000",
            "Pârtiile Valea Dorului, Valea Soarelui și Drumul de Vară",
            "Spațiu securizat depozitare echipament schi",
            "Amplasare centrală aproape de Parcul Dimitrie Ghica",
            "Card de vacanță Sodexo/Edenred/Pluxee acceptat"
        ],
        "description": "Sinaia oferă cel mai spectaculos domeniu schiabil alpin din țară la peste 2.000m altitudine. Zăpadă naturală din plin în Valea Soarelui și peisaje montane alpine unice.",
        "bookingUrl": "https://www.booking.com/hotel/ro/rina-cerbul.ro.html?checkin=2027-01-22&checkout=2027-01-24&group_adults=2&no_rooms=1",
        "featured": True,
        "publishedAt": "2026-11-06T17:45:00Z"
    },
    {
        "id": "ro-009",
        "slug": "ski-in-ski-out-straja-vila-alpin-nocturna",
        "title": "Zăpadă Garantată & Ski-in / Ski-out la Straja: 2 nopți la Vila Alpin 3★ chiar pe Pârtie",
        "destination": "Stațiunea Straja (Lupeni)",
        "county": "Hunedoara",
        "region": "Transilvania",
        "category": "Schi & Pârtii",
        "badge": "🎿 Ski-in / Ski-out pe Pârtie",
        "image": "https://images.unsplash.com/photo-1482867996988-29ec3a0f1aac?auto=format&fit=crop&w=1200&q=80",
        "priceTotalPerPerson": 65,
        "priceRoomTotal": 130,
        "minNights": 2,
        "capacity": "2 persoane",
        "voucherAccepted": True,
        "amenities": [
            "Ieși direct cu schiurile din cabană pe pârtie (Ski-in / Ski-out)",
            "Nocturnă zilnică pe pârtia Constantinescu & Canal",
            "26 km de pârtii amenajate cu zăpadă garantată",
            "Mic dejun inclus la restaurantul cabanei",
            "Vouchere de vacanță acceptate"
        ],
        "description": "Straja este renumită pentru stratul gros de zăpadă și atmosfera de après-ski! Ieși din cameră direct pe pârtie, schiezi până seara sub reflectoare pe nocturnă și te bucuri de mâncare caldă la ceaun.",
        "bookingUrl": "https://www.booking.com/hotel/ro/vila-alpin.ro.html?checkin=2027-01-29&checkout=2027-01-31&group_adults=2&no_rooms=1",
        "featured": True,
        "publishedAt": "2026-11-06T17:30:00Z"
    },
    {
        "id": "ro-010",
        "slug": "weekend-schi-paltinis-arena-platos-hotel-cindrel",
        "title": "Schi & Distracție la Păltiniș: 2 nopți la Hotel Cindrel 4★ cu Piscină lângă Arena Platoș",
        "destination": "Păltiniș & Arena Platoș",
        "county": "Sibiu",
        "region": "Transilvania",
        "category": "Schi & Pârtii",
        "badge": "🎿 Arena Platoș (Snowpark & Familie)",
        "image": "https://images.unsplash.com/photo-1546955870-9fc65ba8f7f1?auto=format&fit=crop&w=1200&q=80",
        "priceTotalPerPerson": 75,
        "priceRoomTotal": 150,
        "minNights": 2,
        "capacity": "2 persoane",
        "voucherAccepted": True,
        "amenities": [
            "La 3 minute de Arena Platoș (școală de schi & snowpark)",
            "Piscină interioară încălzită și saună uscată",
            "Cameră uscare & depozit schiuri și snowboard",
            "Mic dejun tradițional ardelenesc inclus",
            "Carduri de vacanță acceptate"
        ],
        "description": "Păltiniș este cea mai veche și mai înaltă stațiune montană din România (1.442m). Arena Platoș oferă cele mai moderne instalații de zăpadă artificială, pârtii prietenoase pentru începători și copii, plus evenimente de après-ski.",
        "bookingUrl": "https://www.booking.com/hotel/ro/cindrel.html?checkin=2027-02-05&checkout=2027-02-07&group_adults=2&no_rooms=1",
        "featured": False,
        "publishedAt": "2026-11-06T17:15:00Z"
    }
]

for d in ski_deals:
    if d["id"] not in existing_ids:
        ro_deals.append(d)

with open(ro_path, "w", encoding="utf-8") as f:
    json.dump(ro_deals, f, indent=2, ensure_ascii=False)

print(f"[SUCCES] Am adaugat cele 4 oferte de schi in romania_deals.json! Total oferte Romania: {len(ro_deals)}")
