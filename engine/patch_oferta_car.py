import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = "src/pages/oferta/[slug].astro"
content = open(path, "r", encoding="utf-8").read()

# Curățăm eventuale dubluri de \r\n
content = content.replace("\r\r\n", "\r\n").replace("\r\n", "\n")

idx1 = content.find("<!-- PASUL 1: Detalii Zbor")
idx2 = content.find("<!-- PASUL 2: Selector Multi-Cazare")

flight_original_block = content[idx1:idx2].strip()

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
""" + flight_original_block + """
      )}

"""

new_content = content[:idx1] + car_block + content[idx2:]

# Ghidul Dimensiunilor de Bagaje pe Companii: afișăm doar dacă nu este car
new_content = new_content.replace(
    "<BaggageGuide />",
    "{deal.transportType !== 'car' && <BaggageGuide />}"
)

# Salvăm cu \r\n standard
open(path, "w", encoding="utf-8").write(new_content.replace("\n", "\r\n"))
print("Done patching oferta/[slug].astro successfully!")
