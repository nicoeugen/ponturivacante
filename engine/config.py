"""
Configurare Motor Deal Hunter - Platforma Ponturi Vacanțe
"""
import os

# 1. API Keys (pot fi setate și ca variabile de mediu)
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY", "DEMO_TEQUILA_KEY")
TRAVELPAYOUTS_MARKER = os.getenv("TRAVELPAYOUTS_MARKER", "123456") # ID-ul tău de afiliat
BOOKING_AID = os.getenv("BOOKING_AID", "000000")                   # ID-ul tău de afiliat Booking

# 2. Telegram Bot & Channel
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "@canalul_tau_de_vacante")

# 3. Aeroporturi de plecare monitorizate
ORIGIN_AIRPORTS = [
    {"code": "OTP", "city": "București"},
    {"code": "CLJ", "city": "Cluj-Napoca"},
    {"code": "TSR", "city": "Timișoara"},
    {"code": "IAS", "city": "Iași"},
    {"code": "SBZ", "city": "Sibiu"},
    {"code": "CRA", "city": "Craiova"}
]

# 4. Filtre & Praguri
MAX_FLIGHT_PRICE_EUR = 50       # Zboruri dus-întors sub acest prag
MIN_HOTEL_RATING = 8.0          # Nota minimă pentru cazare pe Booking
DEFAULT_DOUBLE_ROOM_NIGHT = 60  # Cost estimat / noapte cameră dublă decentă
