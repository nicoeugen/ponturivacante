import json

deals_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/deals.json"
with open(deals_path, "r", encoding="utf-8") as f:
    deals = json.load(f)

for d in deals:
    if d.get("slug") == "city-break-paris-din-bucuresti-119-euro":
        d["country"] = "Franța"
        for opt in d.get("accommodationOptions", []):
            if opt.get("providerId") == "agoda":
                opt["link"] = opt["link"].replace("-it.html", "-fr.html")

with open(deals_path, "w", encoding="utf-8") as f:
    json.dump(deals, f, indent=2, ensure_ascii=False)

print("[SUCCES] Paris actualizat cu Franța și link Agoda corectat!")
