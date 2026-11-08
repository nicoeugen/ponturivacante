import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = 'https://api.github.com/repos/nicoeugen/ponturivacante/actions/runs?per_page=6'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
        runs = data.get('workflow_runs', [])
        for r in runs:
            r_id = r.get('id')
            name = r.get('name')
            event = r.get('event')
            status = r.get('status')
            conclusion = r.get('conclusion')
            created = r.get('created_at')
            print(f"ID: {r_id} | Name: {name} | Event: {event} | Status: {status} | Conclusion: {conclusion} | Created: {created}")
except Exception as e:
    print('Error:', e)
