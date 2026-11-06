import json

blog_path = "C:/Users/Eugen/Desktop/Proiecte/website turism/data/blog_articles.json"
with open(blog_path, "r", encoding="utf-8") as f:
    articles = json.load(f)

for a in articles:
    if "maldive" in a.get("slug", ""):
        a["title"] = "Vacanță în Maldive pe cont propriu: Ghid complet pentru un sejur sub 850€ de persoană"
        a["excerpt"] = "Află secretul insulelor locale locuite din Maldive (Maafushi, Dhigurah): plaje cu nisip alb, apă de 30°C și guesthouse-uri ieftine fără agenție, zbor inclus."

with open(blog_path, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)

print("[SUCCES] blog_articles.json actualizat!")
