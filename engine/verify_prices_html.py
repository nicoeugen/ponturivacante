import json, re

sample_maldive = "C:/Users/Eugen/Desktop/Proiecte/website turism/dist/oferta/vacanta-exotica-maldive-diy-din-bucuresti-435-euro/index.html"
txt = open(sample_maldive, encoding="utf-8").read()
print("Maldive pret total gasit in HTML:", re.findall(r'id="badge-total-price"[^>]*>([^<]+)<', txt))
print("Maldive pret zbor gasit in HTML:", re.findall(r'1\. Bilet Avion Dus-Întors</div><div class="[^"]+">([^<]+)<', txt))

sample_znz = "C:/Users/Eugen/Desktop/Proiecte/website turism/dist/oferta/vacanta-exotica-zanzibar-tanzania-din-bucuresti-570-euro/index.html"
txt_z = open(sample_znz, encoding="utf-8").read()
print("Zanzibar pret total gasit in HTML:", re.findall(r'id="badge-total-price"[^>]*>([^<]+)<', txt_z))
print("Zanzibar pret zbor gasit in HTML:", re.findall(r'1\. Bilet Avion Dus-Întors</div><div class="[^"]+">([^<]+)<', txt_z))
