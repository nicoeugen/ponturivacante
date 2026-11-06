# PonturiVacanțe — Platformă de Turism & Oferte în Timp Real (Model Aventurescu)

Platformă completă de călătorii **DIY (Do It Yourself)** dedicată pieței din România, bazată pe detectarea biletelor de avion low-cost și împerecherea automată cu opțiuni verificate de cazare (notă 8.0+ pe Booking.com).

---

## 📁 Structura Proiectului

```
C:\Users\Eugen\Desktop\Proiecte\website turism\
├── data/
│   ├── deals.json              # Baza de date locală cu ofertele active
│   └── airports.json           # Aeroporturile monitorizate (OTP, CLJ, TSR, IAS etc.)
├── engine/                     # Backend & Algoritm Python (Deal Hunter)
│   ├── config.py               # Chei API, praguri de preț și aeroporturi
│   ├── deal_hunter.py          # Scanează Kiwi Tequila API pentru zboruri chilipir
│   └── telegram_bot.py         # Transmite automat oferte pe canalul tău Telegram
├── src/                        # Platforma Web (Astro 5 + Tailwind CSS v4)
│   ├── components/             # Header, Footer, Hero (cu filtre), DealCard, TelegramBanner
│   ├── layouts/                # Template principal cu SEO OpenGraph complet
│   ├── pages/
│   │   ├── index.astro         # Homepage cu căutare & filtrare dinamică instantanee
│   │   ├── oferta/[slug].astro # Pagina completă a ofertei (Zbor + Cazare + Date alternative)
│   │   ├── despre.astro        # Pagina de transparență a modelului DIY
│   │   └── go/[type].astro     # Sistem de link cloaking & tracking afiliat
│   └── styles/                 # Tailwind CSS v4 setup
├── astro.config.mjs            # Configurație Astro SSG
└── package.json
```

---

## 🚀 1. Rularea Platformei Web (Frontend)

Platforma folosește **Astro 5** (cel mai rapid framework pentru motoare de conținut și bloguri) + **Tailwind CSS v4**.

```powershell
# Deschide directorul proiectului
cd "C:\Users\Eugen\Desktop\Proiecte\website turism"

# Pornire mod de dezvoltare (Live Reload)
npm run dev
```

Site-ul va porni la `http://localhost:4321`.

### Build pentru Producție:
```powershell
npm run build
```
Toate fișierele optimizate sunt generate în folderul `dist/` (se pot urca 100% gratuit pe **Cloudflare Pages**, **Vercel** sau **Netlify**).

---

## ⚙️ 2. Motorul de Căutare (Backend Python `engine/`)

### A. Obținerea Cheilor API Gratuite:
1. **Kiwi Tequila API:** Înregistrează-te gratuit pe [tequila.kiwi.com](https://tequila.kiwi.com/) și creează o cheie API pentru căutare de zboruri.
2. **Travelpayouts:** Înregistrează-te pe [travelpayouts.com](https://www.travelpayouts.com/) pentru a primi `Marker-ul` tău de afiliat (acoperă Booking.com, Kiwi, Aviasales, GetYourGuide).
3. **Telegram Bot:** Deschide `@BotFather` pe Telegram, creează un bot nou (`/newbot`) și copiază token-ul primit.

### B. Configurarea Cheilor:
Editează fișierul `engine/config.py`:
```python
TEQUILA_API_KEY = "CHEIA_TA_DE_LA_KIWI"
TRAVELPAYOUTS_MARKER = "ID_UL_TAU_TRAVELPAYOUTS"
TELEGRAM_BOT_TOKEN = "TOKEN_BOT_TELEGRAM"
TELEGRAM_CHANNEL_ID = "@numele_canalului_tau"
```

### C. Rularea scanării de zboruri:
```powershell
python engine/deal_hunter.py
```

---

## 💰 3. Cum funcționează Monetizarea & Sistemul de Linkuri

Pentru a nu pierde comisioane și pentru a afișa URL-uri curate, linkurile externe folosesc sistemul de **Link Cloaking**:
- Zbor: `/go/flight?url=https://wizzair.com&deal=deal-001`
- Cazare: `/go/hotel?url=https://booking.com&deal=deal-001`

Fișierul `src/pages/go/[type].astro` atașează automat parametrii tăi de partener (`marker` pentru zboruri și `aid` pentru Booking.com) înainte de a redirecționa vizitatorul.

---

## 📊 Caracteristici Implementate în UI/UX
- **Filtrare instantanee fără reîncărcare:** după oraș de plecare (București, Cluj, Timișoara, Iași etc.), buget maxim (sub 80€, sub 100€, sub 150€) și categorie (City Break, Mare & Soare, Weekend).
- **Formula Aventurescu transparentă:** Breakdown clar `Zbor + (Cazare Totală / 2) = Preț / persoană`.
- **Carduri de conversie ridicată:** Poze HD, steaguri, badge-uri de reducere (`-55%`), distanță față de centru, note Booking.
- **Canal Telegram:** Banner integrat pentru captarea traficului recurent înainte ca biletele de 20-30€ să se epuizeze.
