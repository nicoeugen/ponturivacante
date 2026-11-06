import urllib.request, re, sys

url = 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0zusqHqueRKrLdRqG1EcyIXuI-X4ahWM9ds4uEw3bxk5Tcf2KJzFrevx9QPc9UE8n_l3YjdXljYSIdT-7lz2r19urCrU7fAjrwTqi5U8puQru9aKGgok0W2XHSv4D-pp52N2SOh0eV_02sQCGYmMaEllw7V8phwX5ulTvgfC1qdXiqrRFDhAvEJeL'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        # find outbound links
        matches = re.findall(r'href="([^"]+)"', content)
        for m in matches:
            if any(k in m for k in ['momondo', 'skyscanner', 'kiwi', 'wizz', 'ryanair', 'kayak', 'flights', 'go']):
                print("Link gasit:", m)
except Exception as e:
    print("Eroare:", e)
