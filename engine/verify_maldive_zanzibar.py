import re, urllib.parse

def check(name, file_path):
    c = open(file_path, encoding='utf-8').read()
    print(f"=== {name} ===")
    matches = re.findall(r'href="(/go/flight/\?url=[^"]+)"', c)
    for m in matches:
        u = urllib.parse.unquote(m)
        print("  ->", u[:100] + ("..." if len(u) > 100 else ""))

check("MALDIVE", "C:/Users/Eugen/Desktop/Proiecte/website turism/dist/oferta/vacanta-exotica-maldive-diy-din-bucuresti-435-euro/index.html")
check("ZANZIBAR", "C:/Users/Eugen/Desktop/Proiecte/website turism/dist/oferta/vacanta-exotica-zanzibar-tanzania-din-bucuresti-570-euro/index.html")
