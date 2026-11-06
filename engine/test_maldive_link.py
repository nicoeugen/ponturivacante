import urllib.request, re, sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8FTBK7LOcd54dWmzju6wQDGp3ap6wbF8IPDic67-QFIK0sNzmz5ADqN03WQ0lpbV4grDZHGYIdzPfiATJHeD7NKmOpyDl0PzBgSNESQ5gBRXNZB5a7pYkrYj0iFNxzH36UX6uzWWLOnXaUh0wseyiYjBwNZJjVRoLxdGoYedNmw=='
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        matches = re.findall(r'href="([^"]+)"', content)
        for m in matches:
            if any(k in m for k in ['momondo', 'skyscanner', 'flydubai', 'qatar', 'wizz']):
                print("Found link:", m)
except Exception as e:
    print("Error:", e)
