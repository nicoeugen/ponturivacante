import json
import sys
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Eugen\Desktop\Proiecte\website turism\data\deals.json', 'r', encoding='utf-8') as f:
    deals = json.load(f)

print(f"Total deals: {len(deals)}")

issues = []

for d in deals:
    slug = d.get('slug', '')
    title = d.get('title', '')
    hotel = d.get('hotel', {})
    accs = d.get('accommodationOptions', [])
    flight = d.get('flight', {})
    
    # Check flight link
    fl_link = flight.get('link', '')
    if not fl_link:
        issues.append(f"[{slug}] Missing flight.link")
    
    # Check kiwi link
    kiwi_link = flight.get('kiwiLink', '')
    if kiwi_link and 'marker=801687' not in kiwi_link:
        issues.append(f"[{slug}] kiwiLink missing marker=801687: {kiwi_link}")
        
    # Check hotel link
    h_link = hotel.get('link', '')
    if not h_link:
        issues.append(f"[{slug}] Missing hotel.link")
    
    # Check accommodation options
    for i, a in enumerate(accs):
        prov = a.get('provider', '')
        link = a.get('link', '')
        if not link:
            issues.append(f"[{slug}] acc[{i}] ({prov}) missing link")
        elif 'agoda.com' in link:
            # Check if it has cid=1980047
            if 'cid=1980047' not in link:
                issues.append(f"[{slug}] Agoda link missing cid=1980047: {link}")
            # Check if it is a generic homepage
            if link.strip().endswith('agoda.com/') or link.strip().endswith('agoda.com/ro-ro/') or link.strip().endswith('agoda.com/ro-ro'):
                issues.append(f"[{slug}] Agoda link is generic homepage: {link}")

print(f"\nAudit found {len(issues)} potential issues in deals.json:")
for iss in issues[:30]:
    print(" -", iss)
if len(issues) > 30:
    print(f" ... and {len(issues) - 30} more")
