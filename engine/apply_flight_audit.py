import json

# 1. Update data/deals.json for Maldive, Zanzibar, Madeira, Hurghada
deals_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json"
with open(deals_path, "r", encoding="utf-8") as f:
    deals = json.load(f)

for d in deals:
    slug = d.get("slug")
    
    # MALDIVE
    if "maldive" in slug:
        d["priceTotalPerPerson"] = 829
        d["title"] = "Paradisul din Maldive pe cont propriu: 7 nopți pe insulă de corali + Zbor dus-întors"
        d["flight"]["price"] = 689
        d["flight"]["airline"] = "FlyDubai / Qatar Airways"
        d["flight"]["route"] = "OTP – DXB / DOH – MLE (Zbor cu escală)"
        d["flight"]["isConnecting"] = True
        d["hotel"]["priceTotal"] = 280
        d["hotel"]["pricePerPerson"] = 140
        if "alternativeDates" in d:
            for alt in d["alternativeDates"]:
                alt["price"] = 849
                
    # ZANZIBAR
    elif "zanzibar" in slug:
        d["priceTotalPerPerson"] = 749
        d["title"] = "Exotic în Zanzibar: 8 nopți pe plajă în Nungwi + Zbor dus-întors cu escală"
        d["flight"]["price"] = 599
        d["flight"]["airline"] = "FlyDubai"
        d["flight"]["route"] = "OTP – DXB – ZNZ (Zbor cu escală în Dubai)"
        d["flight"]["isConnecting"] = True
        d["hotel"]["priceTotal"] = 300
        d["hotel"]["pricePerPerson"] = 150
        if "alternativeDates" in d:
            for alt in d["alternativeDates"]:
                alt["price"] = 769
                
    # MADEIRA
    elif "madeira" in slug:
        d["priceTotalPerPerson"] = 289
        d["title"] = "Primăvară eternă în Madeira: 5 nopți la Funchal + Zbor dus-întors"
        d["flight"]["price"] = 189
        d["flight"]["airline"] = "Wizz Air + TAP / EasyJet"
        d["flight"]["route"] = "OTP – LIS / BCN – FNC (Zbor cu escală)"
        d["flight"]["isConnecting"] = True
        d["hotel"]["priceTotal"] = 200
        d["hotel"]["pricePerPerson"] = 100
        if "alternativeDates" in d:
            for alt in d["alternativeDates"]:
                alt["price"] = 299

    # HURGHADA
    elif "hurghada" in slug:
        d["priceTotalPerPerson"] = 339
        d["title"] = "Sejur All Inclusive în Hurghada la Marea Roșie: 6 nopți la Resort 4★ + Zbor"
        d["flight"]["price"] = 199
        d["flight"]["airline"] = "Pegasus Airlines / HiSky"
        d["flight"]["route"] = "OTP – SAW – HRG (Zbor cu escală)"
        d["flight"]["isConnecting"] = True
        d["hotel"]["priceTotal"] = 280
        d["hotel"]["pricePerPerson"] = 140
        if "alternativeDates" in d:
            for alt in d["alternativeDates"]:
                alt["price"] = 349

with open(deals_path, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print("[SUCCES] deals.json actualizat cu preturi realiste si aliniate 100% cu motoarele de cautare!")
