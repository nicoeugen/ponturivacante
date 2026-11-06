"""
Modul Notificări Telegram — Emite automat oferte 'Chilipir' pe canalul tău
"""
import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

def trimite_alerta_telegram(deal, site_url="https://ponturivacante.ro"):
    """
    Trimite un mesaj frumos formatat pe canalul de Telegram.
    """
    if not TELEGRAM_BOT_TOKEN:
        print("[TELEGRAM] Token-ul botului nu este configurat. Setează TELEGRAM_BOT_TOKEN.")
        return False

    link_oferta = f"{site_url}/oferta/{deal['slug']}"
    
    text = (
        f"🔥 <b>OFERTĂ NOUĂ: {deal['destination'].upper()} ({deal.get('flag', '✈️')})</b>\n\n"
        f"📍 <b>Plecare:</b> {deal['originCity']} ({deal['originCode']})\n"
        f"📅 <b>Perioadă:</b> {deal['dates']} ({deal['nights']} nopți)\n\n"
        f"✈️ <b>Zbor dus-întors:</b> {deal['flight']['price']} € / pers ({deal['flight']['airline']})\n"
        f"🏨 <b>Cazare ({deal['nights']} nopți):</b> {deal['hotel']['pricePerPerson']} € / pers ({deal['hotel']['name']})\n"
        f"----------------------------------------\n"
        f"💰 <b>TOTAL: {deal['priceTotalPerPerson']} € / persoană (zbor + cazare)</b>\n\n"
        f"👉 <a href='{link_oferta}'>Vezi oferta completă și rezervă aici</a>\n\n"
        f"⚠️ <i>Prețurile biletelor de avion fluctuează rapid! Rezervă cât timp tariful este valabil.</i>"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code == 200:
            print(f"[TELEGRAM] Ofertă trimisă cu succes pentru {deal['destination']}!")
            return True
        else:
            print(f"[TELEGRAM] Eroare trimitere: {r.text}")
            return False
    except Exception as e:
        print(f"[TELEGRAM] Eroare conexiune: {e}")
        return False

if __name__ == "__main__":
    exemplu_deal = {
        "destination": "Roma",
        "flag": "🇮🇹",
        "originCity": "București",
        "originCode": "OTP",
        "dates": "14 – 17 Mai 2026",
        "nights": 3,
        "slug": "city-break-roma-din-bucuresti-98-euro",
        "priceTotalPerPerson": 98,
        "flight": {"price": 38, "airline": "Wizz Air"},
        "hotel": {"name": "Hotel San Giovanni 3★", "pricePerPerson": 60}
    }
    print("Testare formatare mesaj Telegram:")
    print("-" * 50)
    trimite_alerta_telegram(exemplu_deal)
