import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\Eugen\Desktop\Proiecte\website turism\src\pages\oferta\[slug].astro'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<!-- Extra Travel Services Cards'

calculator_html = '''      <!-- 🧮 CALCULATOR INTERACTIV DE BUGET TOTAL SEJUR -->
      <div class="bg-gradient-to-br from-slate-900 via-slate-950 to-slate-900 text-white rounded-3xl p-6 sm:p-8 border border-slate-800 shadow-2xl mb-10 relative overflow-hidden">
        <div class="absolute -right-12 -top-12 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -left-12 -bottom-12 w-64 h-64 bg-rose-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="relative z-10">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-6">
            <div>
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-400/20 text-amber-300 text-xs font-black uppercase tracking-wider mb-2 border border-amber-300/30">
                <span>🧮 Calculator Live</span>
                <span>•</span>
                <span>Buget Real Fără Surprize</span>
              </div>
              <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                Cât te costă toată vacanța în realitate?
              </h3>
            </div>
            <p class="text-xs text-slate-400 max-w-xs sm:text-right">
              Alege numărul de călători și opțiunile dorite pentru un calcul complet la virgulă.
            </p>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
            <!-- Coloana Stânga: Controale & Opțiuni -->
            <div class="lg:col-span-7 space-y-4">
              <!-- Selector Călători -->
              <div class="bg-slate-800/80 rounded-2xl p-4 border border-slate-700/80">
                <label class="block text-xs font-bold text-slate-300 mb-2 uppercase tracking-wider">
                  👥 Număr de persoane (adulți):
                </label>
                <div class="grid grid-cols-4 gap-2">
                  <button type="button" class="calc-pax-btn py-2 rounded-xl text-xs font-black transition-all bg-slate-700/60 text-slate-300 hover:bg-slate-700" data-pax="1">1 pers</button>
                  <button type="button" class="calc-pax-btn active py-2 rounded-xl text-xs font-black transition-all bg-rose-600 text-white shadow-md" data-pax="2">2 pers (Duo)</button>
                  <button type="button" class="calc-pax-btn py-2 rounded-xl text-xs font-black transition-all bg-slate-700/60 text-slate-300 hover:bg-slate-700" data-pax="3">3 pers</button>
                  <button type="button" class="calc-pax-btn py-2 rounded-xl text-xs font-black transition-all bg-slate-700/60 text-slate-300 hover:bg-slate-700" data-pax="4">4 pers</button>
                </div>
              </div>

              <!-- Opțiuni Extra Cheltuieli -->
              <div class="bg-slate-800/80 rounded-2xl p-4 border border-slate-700/80 space-y-3">
                <span class="block text-xs font-bold text-slate-300 uppercase tracking-wider">
                  🎯 Personalizează cheltuielile estimative:
                </span>

                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 cursor-pointer border border-slate-700/50 transition-colors">
                  <div class="flex items-center gap-3">
                    <input type="checkbox" id="calc-baggage" class="w-4 h-4 text-rose-600 rounded border-slate-600 focus:ring-rose-500 cursor-pointer" />
                    <div>
                      <div class="text-xs font-bold text-white">🧳 Bagaj mare de cală (dus-întors)</div>
                      <div class="text-[11px] text-slate-400">Rucsacul mic e deja inclus gratuit</div>
                    </div>
                  </div>
                  <span class="text-xs font-bold text-amber-300">+35 € / pers</span>
                </label>

                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 cursor-pointer border border-slate-700/50 transition-colors">
                  <div class="flex items-center gap-3">
                    <input type="checkbox" id="calc-meals" checked class="w-4 h-4 text-rose-600 rounded border-slate-600 focus:ring-rose-500 cursor-pointer" />
                    <div>
                      <div class="text-xs font-bold text-white">🍽️ Mese & Cafele ({deal.nights} zile)</div>
                      <div class="text-[11px] text-slate-400">Estimare realistă ~30 € / zi / pers</div>
                    </div>
                  </div>
                  <span class="text-xs font-bold text-amber-300">+{deal.nights * 30} € / pers</span>
                </label>

                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 cursor-pointer border border-slate-700/50 transition-colors">
                  <div class="flex items-center gap-3">
                    <input type="checkbox" id="calc-transfer" checked class="w-4 h-4 text-rose-600 rounded border-slate-600 focus:ring-rose-500 cursor-pointer" />
                    <div>
                      <div class="text-xs font-bold text-white">🚌 Transfer Aeroport ⇄ Hotel (autobuz / tren)</div>
                      <div class="text-[11px] text-slate-400">Transport local dus-întors</div>
                    </div>
                  </div>
                  <span class="text-xs font-bold text-amber-300">+15 € / pers</span>
                </label>

                <label class="flex items-center justify-between p-2.5 rounded-xl bg-slate-900/60 hover:bg-slate-900 cursor-pointer border border-slate-700/50 transition-colors">
                  <div class="flex items-center gap-3">
                    <input type="checkbox" id="calc-insurance" class="w-4 h-4 text-rose-600 rounded border-slate-600 focus:ring-rose-500 cursor-pointer" />
                    <div>
                      <div class="text-xs font-bold text-white">🛡️ Asigurare medicală călătorie</div>
                      <div class="text-[11px] text-slate-400">Asigurari.ro acoperire completă</div>
                    </div>
                  </div>
                  <span class="text-xs font-bold text-amber-300">+8 € / pers</span>
                </label>
              </div>
            </div>

            <!-- Coloana Dreapta: Rezumat Total Live -->
            <div class="lg:col-span-5 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-6 border border-slate-700 flex flex-col justify-between shadow-xl">
              <div>
                <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1">
                  Total Estimativ Vacanță:
                </span>
                <div class="flex items-baseline gap-2 mb-1">
                  <span id="calc-total-per-pers" class="text-3xl sm:text-4xl font-black text-amber-400">
                    -- €
                  </span>
                  <span class="text-xs text-slate-300 font-medium">/ persoană</span>
                </div>
                <div id="calc-total-group" class="text-xs text-emerald-400 font-semibold mb-4">
                  Total grup: -- € (~-- Lei)
                </div>

                <!-- Detaliu costuri -->
                <div class="space-y-1.5 text-xs text-slate-300 pt-3 border-t border-slate-700 mb-6">
                  <div class="flex justify-between">
                    <span>✈️ Zbor dus-întors:</span>
                    <strong id="calc-row-flight">-- €</strong>
                  </div>
                  <div class="flex justify-between">
                    <span>🏨 Cazare ({deal.nights} nopți):</span>
                    <strong id="calc-row-hotel">-- €</strong>
                  </div>
                  <div class="flex justify-between text-slate-400">
                    <span>➕ Cheltuieli opționale selectate:</span>
                    <strong id="calc-row-extras" class="text-amber-300">-- €</strong>
                  </div>
                </div>
              </div>

              <a 
                href="#optiuni-rezervare"
                class="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-black text-xs sm:text-sm text-center shadow-lg transition-all hover:scale-[1.02] active:scale-95 flex items-center justify-center gap-2"
              >
                <span>Vezi Opțiunile & Rezervă Direct</span>
                <span>&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>

      ''' + target

if target in content:
    content = content.replace(target, calculator_html, 1)
    print('Calculator HTML inserted successfully')
else:
    print('Target for calculator not found!')

# Add client-side calculator script
calc_script_target = "const btnCopy = document.getElementById('btn-copy-offer-link');"
calc_script_addition = '''// --- 🧮 CALCULATOR INTERACTIV DE BUGET ---
    let calcPax = 2;
    const flightBasePrice = ''' + str(0 if False else -1) + '''; // will substitute below

'''

script_code = """
    // --- 🧮 CALCULATOR INTERACTIV DE BUGET ---
    let calcPax = 2;
    const baseFlight = """ + str(content.count('flightBasePrice')) + """;
    const dealFlightPrice = """ + ("0" if "deal.transportType === 'car'" else "{deal.flight.price}") + """;
    const dealHotelTotal = {deal.hotel.priceTotal};
    const dealNights = {deal.nights};

    const paxBtns = document.querySelectorAll('.calc-pax-btn');
    const chkBag = document.getElementById('calc-baggage');
    const chkMeals = document.getElementById('calc-meals');
    const chkTransfer = document.getElementById('calc-transfer');
    const chkInsurance = document.getElementById('calc-insurance');

    const outPerPers = document.getElementById('calc-total-per-pers');
    const outGroup = document.getElementById('calc-total-group');
    const rowFlight = document.getElementById('calc-row-flight');
    const rowHotel = document.getElementById('calc-row-hotel');
    const rowExtras = document.getElementById('calc-row-extras');

    function updateCalculator() {
      if (!outPerPers) return;
      const flightPerPers = dealFlightPrice;
      const hotelPerPers = Math.round(dealHotelTotal / calcPax);

      let extrasPerPers = 0;
      if (chkBag && chkBag.checked) extrasPerPers += 35;
      if (chkMeals && chkMeals.checked) extrasPerPers += (dealNights * 30);
      if (chkTransfer && chkTransfer.checked) extrasPerPers += 15;
      if (chkInsurance && chkInsurance.checked) extrasPerPers += 8;

      const totalPerPers = flightPerPers + hotelPerPers + extrasPerPers;
      const totalGroup = totalPerPers * calcPax;
      const totalLei = Math.round(totalGroup * 5);

      outPerPers.textContent = `${totalPerPers} €`;
      if (outGroup) {
        outGroup.textContent = `Total grup (${calcPax} pers): ${totalGroup} € (~${totalLei} Lei)`;
      }
      if (rowFlight) rowFlight.textContent = flightPerPers === 0 ? 'Transport Propriu' : `${flightPerPers} € / pers`;
      if (rowHotel) rowHotel.textContent = `${hotelPerPers} € / pers (${dealHotelTotal} € cameră)`;
      if (rowExtras) rowExtras.textContent = `+${extrasPerPers} € / pers`;
    }

    paxBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        calcPax = parseInt(btn.dataset.pax || '2', 10);
        paxBtns.forEach(b => {
          if (b === btn) {
            b.className = 'calc-pax-btn active py-2 rounded-xl text-xs font-black transition-all bg-rose-600 text-white shadow-md';
          } else {
            b.className = 'calc-pax-btn py-2 rounded-xl text-xs font-black transition-all bg-slate-700/60 text-slate-300 hover:bg-slate-700';
          }
        });
        updateCalculator();
      });
    });

    [chkBag, chkMeals, chkTransfer, chkInsurance].forEach(el => {
      if (el) el.addEventListener('change', updateCalculator);
    });

    updateCalculator();

    const btnCopy = document.getElementById('btn-copy-offer-link');
"""

if calc_script_target in content:
    content = content.replace(calc_script_target, script_code, 1)
    print('Calculator script inserted successfully')
else:
    print('Calc script target not found!')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated successfully!')
