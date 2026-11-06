import re, glob, urllib.parse

html_files = glob.glob('C:/Users/Eugen/Desktop/Proiecte/website turism/dist/**/*.html', recursive=True)
checked = set()
for f in html_files:
    content = open(f, encoding='utf-8').read()
    for m in re.finditer(r'/go/hotel/\?url=([^&\"\'>\s]+)', content):
        url = urllib.parse.unquote(m.group(1))
        if url not in checked:
            checked.add(url)
            print(f"- {url}")

print(f"\nTotal linkuri unice de cazare in dist: {len(checked)}")
