path = "engine/update_exact_deeplinks.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = '"city-break-paris-din-bucuresti-119-euro": "https://www.booking.com/hotel/fr/ibis-paris-ornano-montmartre-nord-18eme.ro.html"'
addition = ''',
    "vacanta-schi-bansko-bulgaria-din-bucuresti-149-euro": "https://www.booking.com/hotel/bg/green-life-ski-spa-resort.ro.html",
    "vacanta-schi-dolomiti-val-di-fassa-din-bucuresti-289-euro": "https://www.booking.com/hotel/it/il-caminetto-sport-canazei.ro.html",
    "vacanta-schi-tirol-innsbruck-austria-din-bucuresti-319-euro": "https://www.booking.com/hotel/at/hotel-maximilian.ro.html",
    "vacanta-schi-jasna-chopok-slovacia-din-bucuresti-239-euro": "https://www.booking.com/hotel/sk/hotel-jasna.ro.html"'''

if target in content and "vacanta-schi-bansko" not in content:
    content = content.replace(target, target + addition)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated update_exact_deeplinks.py successfully")
else:
    print("Already present or target not found")
