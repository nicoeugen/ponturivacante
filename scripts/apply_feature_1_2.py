import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\oferta\[slug].astro'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add savings calculation to frontmatter
frontmatter_target = 'const soloPrice = deal.flight.price + deal.hotel.priceTotal;'
frontmatter_replacement = '''const soloPrice = deal.flight.price + deal.hotel.priceTotal;
const agencyEstimatedPrice = Math.round((deal.priceTotalPerPerson * 1.85) + 35);
const savingsAmount = agencyEstimatedPrice - deal.priceTotalPerPerson;
const savingsPercent = Math.round((savingsAmount / agencyEstimatedPrice) * 100);'''

if frontmatter_target in content:
    content = content.replace(frontmatter_target, frontmatter_replacement, 1)
    print('Frontmatter updated successfully')
else:
    print('Frontmatter target not found!')

# 2. Add visual comparison and WhatsApp box before optiuni-rezervare
summary_target = '<div id="optiuni-rezervare" class="scroll-mt-20"></div>'

comparison_html = '''      <!-- Comparație Vizuală Preț DIY vs Agenție & Distribuire Prieteni -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-10">
        <!-- Card 1: Comparație Preț DIY vs Agenție -->
        <div class="md:col-span-2 bg-gradient-to-br from-slate-900 to-slate-950 text-white rounded-3xl p-5 sm:p-6 shadow-xl border border-slate-800 flex flex-col justify-between relative overflow-hidden">
          <div class="absolute -right-8 -bottom-8 w-40 h-40 bg-emerald-500/10 rounded-full blur-2xl pointer-events-none"></div>
          
          <div>
            <div class="flex items-center justify-between gap-2 mb-3">
              <span class="text-[11px] font-black uppercase tracking-wider px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-400/30">
                💰 Economie Reală (Fără Agenții)
              </span>
              <span class="text-xs text-slate-400 font-medium">Preț direct la sursă</span>
            </div>

            <div class="grid grid-cols-2 gap-3 mb-4">
              <!-- Agenție Tradițională -->
              <div class="bg-slate-800/60 rounded-2xl p-3 border border-slate-700/60">
                <div class="text-[11px] text-slate-400 font-medium mb-1">Pachet agenție turism:</div>
                <div class="text-lg sm:text-xl font-bold text-slate-400 line-through">~{agencyEstimatedPrice}&nbsp;€</div>
                <div class="text-[10px] text-slate-500">adaosuri comerciale & taxe</div>
              </div>

              <!-- PonturiVacante DIY -->
              <div class="bg-emerald-950/40 rounded-2xl p-3 border border-emerald-500/30">
                <div class="text-[11px] text-emerald-300 font-medium mb-1">PonturiVacanțe (DIY):</div>
                <div class="text-xl sm:text-2xl font-black text-emerald-400">{deal.priceTotalPerPerson}&nbsp;€</div>
                <div class="text-[10px] text-emerald-300/80">zbor direct + hotel oficial</div>
              </div>
            </div>
          </div>

          <div class="pt-3 border-t border-slate-800 flex flex-wrap items-center justify-between gap-2 text-xs">
            <span class="text-slate-300">Bani economisiți în buzunar:</span>
            <span class="font-extrabold text-emerald-400 bg-emerald-500/15 px-2.5 py-1 rounded-lg border border-emerald-500/30">
              +{savingsAmount}&nbsp;€ / persoană (-{savingsPercent}%)
            </span>
          </div>
        </div>

        <!-- Card 2: Distribuie Oferta pe WhatsApp / Prieteni -->
        <div class="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-3xl p-5 sm:p-6 border border-emerald-200/80 flex flex-col justify-between shadow-sm">
          <div>
            <div class="text-xs font-bold uppercase tracking-wider text-emerald-800 mb-1 flex items-center gap-1.5">
              <span>👥 Planifici în doi?</span>
            </div>
            <h3 class="text-base font-black text-slate-900 leading-tight mb-2">
              Trimite oferta partenerului sau prietenilor
            </h3>
            <p class="text-xs text-slate-600 mb-4 leading-relaxed">
              O vacanță frumoasă se decide în doi. Trimite linkul direct pe WhatsApp cu un singur tap.
            </p>
          </div>

          <div class="space-y-2">
            <a 
              href={`https://api.whatsapp.com/send?text=${encodeURIComponent(`Uite ce pont de vacanță am găsit pe PonturiVacanțe: ${deal.title} la doar ${deal.priceTotalPerPerson} €/pers (zbor dus-întors + cazare ${deal.nights} nopți)! Vezi aici: https://ponturivacante.ro/oferta/${deal.slug}/`)}`}
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center justify-center gap-2 w-full py-3 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs shadow-md transition-all hover:scale-[1.02] active:scale-95"
            >
              <span>📲 Trimite pe WhatsApp</span>
            </a>

            <button 
              type="button"
              id="btn-copy-offer-link"
              data-url={`https://ponturivacante.ro/oferta/${deal.slug}/`}
              class="inline-flex items-center justify-center gap-1.5 w-full py-2.5 px-3 rounded-xl bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs border border-slate-200 transition-colors cursor-pointer"
            >
              <span id="copy-icon">🔗</span>
              <span id="copy-text">Copiază Linkul Ofertei</span>
            </button>
          </div>
        </div>
      </div>

''' + summary_target

if summary_target in content:
    content = content.replace(summary_target, comparison_html, 1)
    print('Comparison and WhatsApp card added successfully')
else:
    print('Summary target not found!')

# 3. Add script for copy button
script_target = "const btnSolo = document.getElementById('toggle-solo');"
script_addition = '''const btnCopy = document.getElementById('btn-copy-offer-link');
    if (btnCopy) {
      btnCopy.addEventListener('click', async () => {
        const url = btnCopy.dataset.url || window.location.href;
        try {
          await navigator.clipboard.writeText(url);
          const icon = document.getElementById('copy-icon');
          const text = document.getElementById('copy-text');
          if (icon) icon.textContent = '✓';
          if (text) text.textContent = 'Link copiat!';
          setTimeout(() => {
            if (icon) icon.textContent = '🔗';
            if (text) text.textContent = 'Copiază Linkul Ofertei';
          }, 2500);
        } catch(e) {
          prompt('Copiază linkul:', url);
        }
      });
    }

    const btnSolo = document.getElementById('toggle-solo');'''

if script_target in content:
    content = content.replace(script_target, script_addition, 1)
    print('Copy script added successfully')
else:
    print('Script target not found!')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('File written cleanly!')
