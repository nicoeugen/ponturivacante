with open('C:/Users/Eugen/Desktop/Proiecte/website turism/dist/romania/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
articles = re.findall(r'<article[^>]+>', html)
for a in articles:
    if 'romania-card' in a:
        cat_match = re.search(r'data-category="([^"]+)"', a)
        slug_match = re.search(r'href="/romania/([^"]+)"', a)
        print(f"Card category: {cat_match.group(1) if cat_match else 'NONE'} | slug: {slug_match.group(1) if slug_match else ''}")
