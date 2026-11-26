import json
import re

def audit():
    deals = json.load(open('data/deals.json', encoding='utf-8'))
    ro_deals = json.load(open('data/romania_deals.json', encoding='utf-8'))
    cruises = json.load(open('data/cruises.json', encoding='utf-8'))

    errors = []
    warnings = []

    print(f"Total deals: {len(deals)}")
    print(f"Total ro_deals: {len(ro_deals)}")
    print(f"Total cruises: {len(cruises)}")

    # 1. Audit deals.json
    for d in deals:
        deal_id = d.get('id')
        title = d.get('title')
        transport_type = d.get('transportType', 'flight')

        # Flight check
        flight = d.get('flight')
        if not flight:
            errors.append(f"[{deal_id}] Lipseste obiectul flight!")
        else:
            if transport_type == 'flight':
                if 'price' not in flight:
                    errors.append(f"[{deal_id}] Lipseste flight.price!")
                if flight.get('price', 0) <= 0:
                    errors.append(f"[{deal_id}] flight.price <= 0 pentru transport avion!")
                
                f_link = flight.get('link', '')
                if not f_link.startswith(('http://', 'https://')):
                    errors.append(f"[{deal_id}] flight.link invalid: {f_link}")
                if 'ryanair.com' in f_link and 'tpAdults' in f_link:
                    errors.append(f"[{deal_id}] Ryanair link contine tpAdults!")

                # Check Kiwi / Google flights / Skyscanner
                kiwi = d.get('kiwiLink', '')
                if kiwi:
                    if 'affilid=travelpayouts' not in kiwi or 'marker=801687' not in kiwi:
                        warnings.append(f"[{deal_id}] kiwiLink nu are parametrii completi affilid/marker!")
            elif transport_type == 'car':
                if flight.get('price', 0) != 0:
                    warnings.append(f"[{deal_id}] transportType='car' dar flight.price != 0 ({flight.get('price')})")
                f_link = flight.get('link', '')
                if not f_link.startswith(('http://', 'https://')):
                    errors.append(f"[{deal_id}] flight.link (harta auto) invalid: {f_link}")

        # Hotel check
        hotel = d.get('hotel')
        if not hotel:
            errors.append(f"[{deal_id}] Lipseste obiectul hotel!")
        else:
            h_link = hotel.get('link', '')
            if not h_link.startswith(('http://', 'https://')):
                errors.append(f"[{deal_id}] hotel.link invalid: {h_link}")
            if 'booking.com' in h_link and 'aid=304142' not in h_link:
                errors.append(f"[{deal_id}] hotel.link Booking nu contine aid=304142!")

        # Accommodation options
        acc_opts = d.get('accommodationOptions', [])
        for opt in acc_opts:
            opt_link = opt.get('link', '')
            if 'booking.com' in opt_link and 'aid=304142' not in opt_link:
                errors.append(f"[{deal_id}] optiune booking ({opt.get('name')}) nu are aid=304142!")
            if 'agoda.com' in opt_link and 'cid=1980047' not in opt_link:
                errors.append(f"[{deal_id}] optiune agoda ({opt.get('name')}) nu are cid=1980047!")

    # 2. Audit romania_deals.json
    for d in ro_deals:
        deal_id = d.get('id')
        b_link = d.get('bookingUrl', '')
        if not b_link.startswith(('http://', 'https://')):
            errors.append(f"[{deal_id}] bookingUrl invalid: {b_link}")
        if 'booking.com' in b_link and 'aid=304142' not in b_link:
            errors.append(f"[{deal_id}] bookingUrl Booking nu contine aid=304142!")
        if not d.get('priceTotalPerPerson'):
            errors.append(f"[{deal_id}] Lipseste priceTotalPerPerson!")

    # 3. Audit cruises.json
    for c in cruises:
        cid = c.get('id')
        cd = c.get('cruiseDetails', {})
        c_link = cd.get('link', '')
        if not c_link.startswith(('http://', 'https://')):
            errors.append(f"[{cid}] cruiseDetails.link invalid: {c_link}")
        fl = c.get('flight')
        if fl:
            flink = fl.get('link', '')
            if not flink.startswith(('http://', 'https://')):
                errors.append(f"[{cid}] flight.link invalid: {flink}")
            if 'ryanair.com' in flink and 'tpAdults' in flink:
                errors.append(f"[{cid}] Ryanair link contine tpAdults in cruise!")

    print("\n" + "="*50)
    print(f"REZULTATE AUDIT:")
    print(f"Erori critice: {len(errors)}")
    for e in errors:
        print(f"  ❌ {e}")
    print(f"Avertismente: {len(warnings)}")
    for w in warnings:
        print(f"  ⚠️ {w}")
    print("="*50)

if __name__ == '__main__':
    audit()
