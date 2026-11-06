with open("C:/Users/Eugen/Desktop/Proiecte/website turism/src/pages/oferta/[slug].astro", "r", encoding="utf-8") as f:
    content = f.read()

dup = """              <a 
                href={`/go/flight/?url=${encodeURIComponent(deal.flight.googleFlightsLink)}&deal=${deal.id}&provider=google`}
                target="_blank"
                rel="noopener noreferrer"
                class="font-bold text-slate-700 hover:text-rose-600 transition-colors"
              >
                Google Flights
              </a>
            )}"""

if dup in content:
    content = content.replace(dup, "")
    with open("C:/Users/Eugen/Desktop/Proiecte/website turism/src/pages/oferta/[slug].astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("Duplicat eliminat cu succes!")
else:
    print("Nu s-a gasit duplicatul exact!")
