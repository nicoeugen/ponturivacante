import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = "src/pages/oferta/[slug].astro"
content = open(path, "r", encoding="utf-8").read()

# 1. Înlocuire Summary Grid
old_summary_target = """        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center">
          <div class="bg-white rounded-xl p-3 border border-slate-200/80 shadow-sm">
            <div class="text-xs text-slate-500 mb-0.5">1. Bilet Avion Dus-Întors</div>
            <div class="text-lg font-black text-slate-900">{deal.flight.price} €</div>
            <div class="text-[11px] text-slate-500 font-semibold">{deal.flight.airline}</div>
          </div>
          <div class="bg-white rounded-xl p-3 border border-slate-200/80 shadow-sm">
            <div class="text-xs text-slate-500 mb-0.5">2. Cazare ({deal.nights} nopți)</div>
            <div id="summary-hotel-price" class="text-lg font-black text-slate-900">{deal.hotel.pricePerPerson} € <span class="text-xs font-normal">/pers</span></div>
            <div class="text-[11px] text-slate-500">Notă {deal.hotel.rating} ⭐</div>
          </div>
          <div class="bg-rose-600 text-white rounded-xl p-3 shadow-md">
            <div class="text-xs text-rose-100 mb-0.5">Total Vacanță</div>
            <div id="summary-total-price" class="text-xl font-black">{deal.priceTotalPerPerson} €</div>
            <div id="summary-total-sub" class="text-[11px] text-rose-100">zbor + cazare / pers</div>
          </div>
        </div>"""

new_summary = """        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center">
          <div class="bg-white rounded-xl p-3 border border-slate-200/80 shadow-sm">
            <div class="text-xs text-slate-500 mb-0.5">{deal.transportType === 'car' ? '1. Transport' : '1. Bilet Avion Dus-Întors'}</div>
            <div class="text-lg font-black text-slate-900">{deal.flight.price === 0 ? 'Transport Propriu' : `${deal.flight.price} €`}</div>
            <div class="text-[11px] text-slate-500 font-semibold">{deal.transportType === 'car' ? 'Mașină personală / Fără avion' : deal.flight.airline}</div>
          </div>
          <div class="bg-white rounded-xl p-3 border border-slate-200/80 shadow-sm">
            <div class="text-xs text-slate-500 mb-0.5">2. Cazare ({deal.nights} nopți)</div>
            <div id="summary-hotel-price" class="text-lg font-black text-slate-900">{deal.hotel.pricePerPerson} € <span class="text-xs font-normal">/pers</span></div>
            <div class="text-[11px] text-slate-500">Notă {deal.hotel.rating} ⭐</div>
          </div>
          <div class="bg-rose-600 text-white rounded-xl p-3 shadow-md">
            <div class="text-xs text-rose-100 mb-0.5">Total Vacanță</div>
            <div id="summary-total-price" class="text-xl font-black">{deal.priceTotalPerPerson} €</div>
            <div id="summary-total-sub" class="text-[11px] text-rose-100">{deal.transportType === 'car' ? 'cazare de top / pers' : 'zbor + cazare / pers'}</div>
          </div>
        </div>"""

# 2. Înlocuire PASUL 1 cu verificare de transportType === 'car'
# Căutăm de la <!-- PASUL 1: până la <!-- PASUL 2:
pasul1_pattern = re.compile(r"(<!-- PASUL 1: Detalii Zbor & Opțiuni Alternative -->\s*<div class=\"bg-white rounded-3xl p-6 sm:p-8 border-2 border-slate-200 shadow-md mb-10\">.*?</div>\s*</div>)(\s*<!-- PASUL 2: Cazare)", re.DOTALL)

def pasul1_replacement(match):
    original_flight_block = match.group(1)
    following = match.group(2)
    
    car_block = """<!-- PASUL 1: Detalii Transport (Zbor sau Terestru) -->
      {deal.transportType === 'car' ? (
        <div class="bg-white rounded-3xl p-6 sm:p-8 border-2 border-emerald-300 shadow-md mb-10">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center gap-3">
              <span class="w-9 h-9 rounded-full bg-emerald-600 text-white font-black flex items-center justify-center text-sm shadow">
                1
              </span>
              <div>
                <h3 class="text-lg sm:text-xl font-bold text-slate-900">
                  Transport Terestru / Cu Mașina Proprie
                </h3>
                <p class="text-xs text-slate-500">{deal.flight.airline}</p>
              </div>
            </div>
            <span class="px-3 py-1 rounded-xl text-xs font-black bg-emerald-100 text-emerald-800 border border-emerald-200">
              🚗 Fără bilet avion
            </span>
          </div>

          <div class="bg-emerald-50/60 rounded-2xl p-4 text-sm text-slate-700 mb-4 space-y-2 border border-emerald-100">
            <div><strong>Rută & Durată:</strong> {deal.flight.route}</div>
            <div><strong>Perioadă recomandată:</strong> {deal.dates}</div>
            <div><strong>Bagaj & Echipamente Schi:</strong> {deal.flight.baggageInfo}</div>
          </div>

          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
            <a 
              href={deal.flight.link}
              target="_blank"
              rel="noopener noreferrer"
              class="flex-1 inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm transition-all shadow-md hover:shadow-emerald-600/30"
            >
              <span>🗺️ Deschide Traseul & Navigația pe Google Maps</span>
              <span>&rarr;</span>
            </a>
          </div>

          <div class="mt-4 pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3 text-xs text-slate-500">
            <span class="flex items-center gap-1.5 font-medium text-emerald-700">
              <span class="font-bold">✓</span> Fără taxe suplimentare pentru echipamentul de schi (schiuri, bețe, clăpari în portbagaj)
            </span>
            <span class="text-slate-500">Vinietă online obligatorie la trecerea graniței</span>
          </div>
        </div>
      ) : (
""" + original_flight_block + """
      )}""" + following
    return car_block

# Normalizăm line endings pentru înlocuire
content_norm = content.replace("\r\n", "\n")
old_summary_norm = old_summary_target.replace("\r\n", "\n")
new_summary_norm = new_summary.replace("\r\n", "\n")

if old_summary_norm in content_norm:
    content_norm = content_norm.replace(old_summary_norm, new_summary_norm)
    print("Replaced summary grid successfully")
else:
    print("Summary grid already updated or not matched")

content_norm, count = pasul1_pattern.subn(pasul1_replacement, content_norm, count=1)
print(f"Replaced PASUL 1 block (count={count})")

# 3. BaggageGuide: afișăm doar dacă NU este car
content_norm = content_norm.replace(
    "<!-- Ghidul Dimensiunilor de Bagaje pe Companii -->\n      <BaggageGuide />",
    "<!-- Ghidul Dimensiunilor de Bagaje pe Companii (doar pentru zbor) -->\n      {deal.transportType !== 'car' && <BaggageGuide />}"
)

# Salvăm înapoi cu CRLF
content_final = content_norm.replace("\n", "\r\n")
open(path, "w", encoding="utf-8").write(content_final)
print("Updated src/pages/oferta/[slug].astro successfully!")
