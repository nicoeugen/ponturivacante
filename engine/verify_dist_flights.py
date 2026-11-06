import re, urllib.parse

sample_page = "C:/Users/Eugen/Desktop/Proiecte/website turism/dist/oferta/vacanta-exotica-tenerife-canare-din-bucuresti-250-euro/index.html"
content = open(sample_page, encoding="utf-8").read()

matches = re.findall(r'href="(/go/flight/\?url=[^"]+)"', content)
print("Flight links gasite pe Tenerife:")
for m in matches:
    u = urllib.parse.unquote(m)
    print(" ->", u[:100] + ("..." if len(u) > 100 else ""))
