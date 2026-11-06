import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, '..', 'data', 'blog_articles.json')

with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

existing_ids = {a['id'] for a in articles}

new_articles = [
    {
        "id": "post-005",
        "slug": "ghid-vacanta-schi-pe-cont-propriu-bansko-austria-jasna-costuri",
        "title": "Ghid Vacanță de Schi pe Cont Propriu: Bansko vs. Alpii Austrieci vs. Jasná (Slovacia)",
        "excerpt": "Află cum organizezi o vacanță completă la schi fără agenție: costuri comparate la skipass, cele mai bune opțiuni ski-in/ski-out și cum transporți echipamentul cu mașina sau avionul.",
        "category": "Ghiduri Schi & Iarnă",
        "tag": "Sezon Schi",
        "image": "https://images.unsplash.com/photo-1551524559-8af4e6624178?auto=format&fit=crop&w=1200&q=80",
        "readTime": "8 min citire",
        "author": "Echipa PonturiVacanțe",
        "publishedAt": "2026-11-06T19:00:00Z",
        "content": [
            {
                "type": "p",
                "text": "Vacanțele la schi au reputația de a fi extrem de costisitoare, în special dacă apelezi la pachete rigide oferite de agențiile tradiționale de turism. În realitate, dacă îți organizezi escapada pe cont propriu — rezervând separat cazarea verificată în apropierea telegondolei și achiziționând skipass-ul online din timp — poți reduce costul total cu peste 50% față de ofertele standard."
            },
            {
                "type": "h2",
                "text": "1. Bansko și Borovets (Bulgaria): Campionii accesibilității"
            },
            {
                "type": "p",
                "text": "Pentru schiorii din sudul și estul României, Bulgaria rămâne destinația numărul unu ca raport calitate/preț. Bansko oferă 75 km de pârtii moderne situate la altitudini de până la 2.600m, deservite de instalații moderne Leitner și Doppelmayr. Plecând cu mașina personală din București sau Craiova, drumul durează doar 6-7 ore (aproximativ 450-500 km), fără costuri de bilete de avion sau taxe de bagaj voluminos. Un sejur de 4-5 nopți la Bansko sau Borovets, incluzând cazare confortabilă cu spa și acces la piscină încălzită, pornește de la doar 98€ - 135€ de persoană."
            },
            {
                "type": "h2",
                "text": "2. Jasná și Munții Tatra (Slovacia): Nivel alpin la preț de Europa Centrală"
            },
            {
                "type": "p",
                "text": "Dacă locuiești în Cluj, Oradea, Timișoara sau Satu Mare, stațiunea Jasná Chopok din Slovacia este la doar 6-8 ore de condus lejer. Jasná este adesea numită perla ascunsă a Europei de Est: 50 km de pârtii impecabile, zăpadă garantată din decembrie până în aprilie datorită tunurilor de zăpadă automate de ultimă generație și o viață de noapte apres-ski energică. Prețurile la skipass sunt cu 35% mai mici decât în Alpi, iar cazările moderne cu acces ski-in/ski-out oferă un confort remarcabil."
            },
            {
                "type": "h2",
                "text": "3. Alpii Austrieci (Tirol & Zell am See): Domenii uriașe și ghețari de 3.000m"
            },
            {
                "type": "p",
                "text": "Pentru schiorii avansați care visează la sute de kilometri de pârtii legate fără întrerupere, Austria este destinația supremă. Domenii precum Innsbruck-Olympiaworld, Kitzbühel sau Zell am See - Kaprun (cu ghețarul Kitzsteinhorn la 3.029m) garantează zăpadă perfectă chiar și în anii cu ierni blânde. Cel mai eficient mod de a ajunge acolo pe cont propriu este un zbor direct către Viena, Salzburg sau München (bilete adesea sub 50€ dus-întors cu Ryanair sau Wizz), urmat de un tren direct OBB sau o mașină închiriată direct din aeroport."
            },
            {
                "type": "h2",
                "text": "4. Transportul echipamentului sportiv: Mașină vs. Avion"
            },
            {
                "type": "p",
                "text": "Dacă mergi cu mașina, un suport de schiuri pe plafon sau o cutie portbagaj îți permite să transporți gratuit clăparii și schiurile pentru întreaga familie. Dacă zbori cu avionul, companiile low-cost taxează echipamentul sportiv cu aproximativ 40€ - 60€ per segment. De aceea, pentru zborurile spre Alpi este adesea mai avantajos și mai comod să închiriezi echipament de top (Atomic, Fischer, Head) direct de la centrele de la baza pârtiei, rezervat online cu reducere de 15-20% înainte de plecare."
            },
            {
                "type": "h2",
                "text": "5. Trucul skipass-ului: Cumpără online din timp"
            },
            {
                "type": "p",
                "text": "Majoritatea marilor stațiuni europene folosesc acum tarifare dinamică pentru cartelele de schi (similar biletelor de avion). Dacă achiziționezi skipass-ul de pe site-ul oficial al stațiunii (de ex. Gopass pentru Slovacia sau Snowpass pentru Austria) cu 2-3 săptămâni înainte, plătești cu 20% până la 30% mai puțin decât la casa de bilete fizică din dimineața primei zile de schi!"
            }
        ]
    },
    {
        "id": "post-006",
        "slug": "top-destinatii-exotice-soare-iarna-buget-redus",
        "title": "Top 5 Destinații Exotice cu Soare și Plajă în Plină Iarnă (Sub 300€ Zbor + Cazare)",
        "excerpt": "Unde evadezi la 25°C când în România ninge? Descoperă destinațiile calde la ocean și mare, cu zboruri directe ieftine și cazare la soare.",
        "category": "Destinații Exotice",
        "tag": "Plajă Iarna",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "readTime": "7 min citire",
        "author": "Echipa PonturiVacanțe",
        "publishedAt": "2026-11-06T19:30:00Z",
        "content": [
            {
                "type": "p",
                "text": "Lunile ianuarie, februarie și martie sunt adesea cele mai reci și mohorâte în România, dar la doar 3 până la 5 ore de zbor există colțuri de paradis unde termometrul arată constant 22°C - 28°C. Iată topul destinațiilor calde unde poți face plajă în plină iarnă cu un buget total sub 300€ de persoană."
            },
            {
                "type": "h2",
                "text": "1. Tenerife și Gran Canaria (Insulele Canare, Spania)"
            },
            {
                "type": "p",
                "text": "Situate în Oceanul Atlantic, aproape de coasta Africii, Insulele Canare au cel mai bun climat din Europa. În sudul insulei Tenerife (Playa de las Américas, Costa Adeje) sau în Maspalomas (Gran Canaria), temperaturile de zi ating frecvent 23-25°C. Un avantaj colosal: insulele fac parte din Spania și UE, deci călătorești doar cu buletinul, plătești în Euro și folosești abonamentul de telefonie mobilă cu roaming gratuit ca acasă!"
            },
            {
                "type": "h2",
                "text": "2. Dubai și Abu Dhabi (Emiratele Arabe Unite)"
            },
            {
                "type": "p",
                "text": "Dacă în iulie Dubaiul este sufocant cu 45°C, lunile de iarnă sunt pur și simplu perfecte: 26°C ziua, briză plăcută și apă la 23°C excelentă pentru baie. Wizz Air operează zboruri directe din București și Cluj către Abu Dhabi, cu tarife dus-întors care coboară frecvent sub 80€ - 100€. De la aeroportul din Abu Dhabi până în centrul Dubaiului există autocare confortabile non-stop care costă sub 8€."
            },
            {
                "type": "h2",
                "text": "3. Aqaba și Deșertul Wadi Rum (Iordania)"
            },
            {
                "type": "p",
                "text": "Aqaba, situată în golful Mării Roșii, oferă unele dintre cele mai spectaculoase recifuri de corali din lume pentru snorkeling, la o temperatură a apei caldă pe tot parcursul anului. În plus, la doar două ore distanță se află spectaculosul deșert roșu Wadi Rum și legendara cetate antică Petra. Zborurile low-cost directe din București aterizează chiar pe aeroportul din Aqaba."
            },
            {
                "type": "h2",
                "text": "4. Hurghada (Egipt): All Inclusive la tarif imbatabil"
            },
            {
                "type": "p",
                "text": "Pentru cei care își doresc relaxare totală fără grija meselor sau a cumpărăturilor, resorturile de 4★ și 5★ din Hurghada oferă pachete All Inclusive cu plaje private la Marea Roșie la prețuri incredibil de mici în sezonul de iarnă — adesea sub 255€ de persoană pentru 7 nopți întregi cu toate mesele și zborul incluse."
            },
            {
                "type": "h2",
                "text": "5. Madeira (Portugalia): Grădina plutitoare a Atlanticului"
            },
            {
                "type": "p",
                "text": "Dacă preferi peisajele dramatice, pădurile tropicale de dafin și drumețiile deasupra norilor (levadas) în locul lenevitului pe șezlong, Madeira este alegerea perfectă. Clima blândă de 20°C permite explorarea insulei în tricou în orice zi din an."
            }
        ]
    },
    {
        "id": "post-007",
        "slug": "secretul-city-break-sub-100-euro-europa",
        "title": "Secretul City Break-urilor Sub 100€: 4 Orașe Europene de Vis cu Buget Redus",
        "excerpt": "Cum vizitezi marile orașe culturale ale Europei (Roma, Bologna, Milano, Viena) la o fracțiune din costul unui pachet turistic clasic.",
        "category": "City Break",
        "tag": "Sub 100€",
        "image": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
        "readTime": "6 min citire",
        "author": "Echipa PonturiVacanțe",
        "publishedAt": "2026-11-06T20:00:00Z",
        "content": [
            {
                "type": "p",
                "text": "Un city break de weekend nu trebuie să coste o avere. Cu zboruri low-cost de 30-40€ dus-întors și cazările inteligente rezervate pe cont propriu, poți savura un espresso pe o terasă însorită din Italia sau o felie de Sacher Torte la Viena cu un buget total mai mic decât un weekend pe Valea Prahovei."
            },
            {
                "type": "h2",
                "text": "1. Bologna (Italia): Paradisul gurmanzilor"
            },
            {
                "type": "p",
                "text": "Bologna este probabil cel mai autentic oraș italian: celebrele porticuri medievale protejate UNESCO (sub care te poți plimba kilometri întregi chiar dacă plouă), cea mai veche universitate din lume și o cultură culinară inegalabilă (tagliatelle al ragù, tortellini, mortadella proaspătă). Prețurile la mâncare și cazare sunt cu 30% mai mici decât în Florența sau Veneția, ambele fiind la doar 35 de minute distanță cu trenul de mare viteză Frecciarossa."
            },
            {
                "type": "h2",
                "text": "2. Bergamo și Milano (Lombardia)"
            },
            {
                "type": "p",
                "text": "Majoritatea zborurilor ieftine aterizează pe aeroportul Orio al Serio (BGY). Secretul călătorilor experimentați este să nu alerge direct spre Milano, ci să descopere Città Alta din Bergamo — o bijuterie medievală cocoțată pe deal, înconjurată de ziduri venețiene impresionante. De aici, poți lua trenul spre Milano (45 min, 6€) sau spre Lacul Como pentru o zi de poveste."
            },
            {
                "type": "h2",
                "text": "3. Viena (Austria): Fast imperial la preț de student"
            },
            {
                "type": "p",
                "text": "Viena este renumită pentru palatele sale grandioase (Schönbrunn, Hofburg, Belvedere), parcurile impecabile și muzeele de clasă mondială. Cu un abonament de 24h sau 48h pe rețeaua impecabilă de metrou și tramvai, poți traversa întregul oraș rapid și confortabil. Multe dintre cele mai frumoase atracții (grădinile imperiale, Catedrala Sf. Ștefan) au acces gratuit."
            },
            {
                "type": "h2",
                "text": "4. Regula de aur pentru mâncare ieftină și delicioasă"
            },
            {
                "type": "p",
                "text": "Evită restaurantele situate direct în piețele mari turistice (Piazza Navona, Domul din Milano sau Stephansplatz) unde plătești coperto uriaș și mâncare mediocră. Fă doar 2-3 străzi la stânga sau la dreapta, pe aleile pietonale înguste, și caută trattorii de familie pline de localnici. Vei mânca preparate extraordinare gătite în casă la o treime din preț!"
            }
        ]
    }
]

for na in new_articles:
    if na['id'] not in existing_ids:
        articles.append(na)
        print(f"ADĂUGAT: {na['id']} - {na['title']}")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"\nTotal articole în blog acum: {len(articles)}")
