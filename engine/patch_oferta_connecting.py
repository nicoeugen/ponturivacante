with open("C:/Users/Eugen/Desktop/Proiecte/website turism/src/pages/oferta/[slug].astro", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Rută & tip zbor (Direct vs Escală)
old_route_badge = """            <span class="text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">Zbor Direct</span>"""
new_route_badge = """            {deal.flight.isConnecting ? (
              <span class="text-xs font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded">Zbor cu Escală</span>
            ) : (
              <span class="text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">Zbor Direct</span>
            )}"""

# 2. Text Buton Principal
old_btn_text = """            <span>✈️ Rezervă direct pe site-ul {deal.flight.airline} ({deal.flight.price} €)</span>"""
new_btn_text = """            <span>✈️ {deal.flight.isConnecting ? `Rezervă zborul (${deal.flight.airline} · ${deal.flight.price} €)` : `Rezervă direct pe site-ul ${deal.flight.airline} (${deal.flight.price} €)`}</span>"""

# 3. Adaugare Momondo in comparatoare
old_comparators = """          <div class="flex items-center gap-2.5">
            <span class="text-slate-400">Sau compară pe:</span>
            {deal.flight.googleFlightsLink && ("""

new_comparators = """          <div class="flex items-center gap-2.5">
            <span class="text-slate-400">Sau compară pe:</span>
            {deal.flight.momondoLink && (
              <a 
                href={`/go/flight/?url=${encodeURIComponent(deal.flight.momondoLink)}&deal=${deal.id}&provider=momondo`}
                target="_blank"
                rel="noopener noreferrer"
                class="font-bold text-amber-600 hover:text-amber-700 transition-colors"
              >
                Momondo
              </a>
            )}
            {deal.flight.googleFlightsLink && (
              <>
                <span>&bull;</span>
                <a 
                  href={`/go/flight/?url=${encodeURIComponent(deal.flight.googleFlightsLink)}&deal=${deal.id}&provider=google`}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="font-bold text-slate-700 hover:text-rose-600 transition-colors"
                >
                  Google Flights
                </a>
              </>
            )}"""

# Replace
if old_route_badge in content:
    content = content.replace(old_route_badge, new_route_badge)
    print("Route badge inlocuit!")
else:
    print("AVERTISMENT: old_route_badge nu a fost gasit!")

if old_btn_text in content:
    content = content.replace(old_btn_text, new_btn_text)
    print("Button text inlocuit!")
else:
    print("AVERTISMENT: old_btn_text nu a fost gasit!")

if old_comparators in content:
    content = content.replace(old_comparators, new_comparators)
    print("Comparators inlocuit!")
else:
    print("AVERTISMENT: old_comparators nu a fost gasit!")

with open("C:/Users/Eugen/Desktop/Proiecte/website turism/src/pages/oferta/[slug].astro", "w", encoding="utf-8") as f:
    f.write(content)

print("[SUCCES] Step 1 din oferta/[slug].astro complet finisat!")
