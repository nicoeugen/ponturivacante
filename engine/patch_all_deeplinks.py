import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = "engine/update_exact_deeplinks.py"
content = open(path, "r", encoding="utf-8").read()

slug_map = {
    "vacanta-schi-bansko-bulgaria-transport-propriu-110-euro": "https://www.booking.com/hotel/bg/green-life-ski-spa-resort.ro.html",
    "vacanta-schi-borovets-bulgaria-hotel-rila-135-euro": "https://www.booking.com/hotel/bg/rila.ro.html",
    "vacanta-schi-pamporovo-bulgaria-apartamente-98-euro": "https://www.booking.com/hotel/bg/grand-monastery-private-apartments.ro.html",
    "vacanta-schi-tirol-innsbruck-austria-hotel-maximilian-260-euro": "https://www.booking.com/hotel/at/hotel-maximilian.ro.html",
    "vacanta-schi-zell-am-see-kaprun-austria-285-euro": "https://www.booking.com/hotel/at/grand-hotel-zell-am-see.ro.html",
    "vacanta-schi-kitzbuhel-alpi-austria-295-euro": "https://www.booking.com/hotel/at/q-hotel-maria-theresia.ro.html",
    "vacanta-schi-schladming-dachstein-austria-240-euro": "https://www.booking.com/hotel/at/tui-blue-schladming.ro.html",
    "vacanta-schi-dolomiti-val-di-fassa-din-bucuresti-289-euro": "https://www.booking.com/hotel/it/il-caminetto-sport-canazei.ro.html",
    "vacanta-schi-livigno-duty-free-italia-din-bucuresti-309-euro": "https://www.booking.com/hotel/it/hotel-piccolo-tibet.ro.html",
    "vacanta-schi-cortina-dampezzo-dolomiti-din-bucuresti-320-euro": "https://www.booking.com/hotel/it/meuble-oasi.ro.html",
    "vacanta-schi-jasna-chopok-slovacia-hotel-jasna-195-euro": "https://www.booking.com/hotel/sk/hotel-jasna.ro.html",
    "vacanta-schi-tatranska-lomnica-slovacia-180-euro": "https://www.booking.com/hotel/sk/horizont-resort.ro.html",
    "vacanta-schi-val-thorens-trei-vai-franta-din-bucuresti-350-euro": "https://www.booking.com/hotel/fr/residence-le-chamois-d-or.ro.html"
}

# Verificăm dacă sunt deja prezente în VERIFIED_BOOKING_SLUGS
for k, v in slug_map.items():
    if f'"{k}"' not in content:
        # inserăm înainte de ultimul '}' din VERIFIED_BOOKING_SLUGS
        idx = content.find("VERIFIED_ROMANIA_SLUGS = {")
        before_part = content[:idx]
        after_part = content[idx:]
        
        last_brace = before_part.rfind("}")
        entry = f'    "{k}": "{v}",\n'
        content = before_part[:last_brace] + entry + before_part[last_brace:] + after_part

open(path, "w", encoding="utf-8").write(content)
print("Updated engine/update_exact_deeplinks.py with all 13 ski deals!")
