# Memorie & Reguli Proiect — PonturiVacanțe (`ponturivacante.ro`)

## 1. Arhitectură & Infrastructură Live
* **Domeniu Oficial:** `https://ponturivacante.ro` (achiziționat de la ClausWeb, DNS conectat la Cloudflare: `ophelia.ns.cloudflare.com` & `todd.ns.cloudflare.com`).
* **Hosting & Deployment:** Cloudflare Pages conectat la repository-ul GitHub `https://github.com/nicoeugen/ponturivacante.git` (ramura `main`). Orice `git push` lansează automat un build nou în producție.
* **Stack Tehnologic:** Astro 5.x SSG (Static Site Generation), Tailwind CSS v4, scripturi modulare Python pentru automatizare.
* **Google Search Console & SEO:**
  * Domeniu verificat prin DNS în Google Search Console.
  * `robots.txt` trimite către `https://ponturivacante.ro/sitemap-index.xml`.
  * `sitemap-0.xml` este procesat cu statusul 🟢 **Succes** (77 pagini indexate curat).

---

## 2. Monetizare & Parteneriate de Afiliere
* **Travelpayouts:** Marker ID `801687` integrat în `src/pages/go/[type].astro` (campania Kiwi `p=1524`).
* **Booking.com & Agoda:** Deeplink-uri directe către paginile oficiale ale hotelurilor recomandate și căutări parametrizate cu date exacte.
* **Asigurari.ro (Asigurare Medicală de Călătorie):**
  * Link dedicat de tracking activ pe site:
    `https://www.asigurari.ro/asigurare/travel?_gl=1*sfoi5h*_up*MQ..*_ga*NTU4OTI4MDYxLjE3OTQwMDQ3Mzg.*_ga_E4EBT2LCB9*czE3OTQwMDQ3MzckbzEkZzAkdDE3OTQwMDQ3MzckajYwJGwwJGgyNDkzMzE1ODU.`
  * Integrat în toate paginile de oferte (`/oferta/...`), paginile de croaziere (`/croaziere/...`) și în subsolul global (`Footer.astro`). Se deschide în filă nouă fără intermediari, păstrând parametrii `_gl` și `_ga` intacți.

---

## 3. Motorul Autonom de Actualizare & Descoperire Oferte
* **GitHub Actions Workflow:** `.github/workflows/auto-update-deals.yml`
* **Programare Cron:** Rulează de două ori pe zi la **08:00** și **20:00** (ora României) (`0 6,18 * * *`), plus opțiune de rulare manuală (`workflow_dispatch`).
* **Script:** `scripts/deal_updater.py`
  * **Actualizare tarife live:** Interoghează API-ul oficial Ryanair FarFinder pentru rute din București (OTP) și Cluj-Napoca (CLJ).
  * **Verificare integritate:** Testează disponibilitatea cazărilor pe Booking.com și Agoda.
  * **Descoperire autonomă (`CANDIDATE_BLUEPRINTS`):**
    * Bază de date cu destinații europene de top (Napoli, Malta, Paphos, Catania, Salonic, Tirana, Gdansk, Veneția, Pisa, Madrid, Dublin etc.).
    * Dacă găsește un zbor sub 35€/segment ce nu e încă listat, generează o ofertă completă: date în română, zbor + hotel 3★–4★ (nota 8.5+), 5 comparatoare de zbor (Ryanair, Skyscanner, Google Flights, Kiwi, Momondo), cazare multiplă (Booking, Agoda), 2 date alternative (+7z, +14z) și linkuri de asigurare.
    * Limită de siguranță: adaugă 1 ofertă nouă proaspătă per rulare (2 pe zi).
    * Face automat `git commit` și `git push`, declanșând un build live pe Cloudflare Pages.

---

## 4. Starea Catalogului de Conținut (77 pagini live)
1. **Oferte Internaționale DIY:** 31 pachete (Zbor + Cazare), inclusiv noua ofertă automată *Napoli & Coasta Amalfi (124 € / pers)*.
2. **Cazări de Poveste în România:** 10 locații de top (`data/romania_deals.json`) — cabane A-frame, ciubăr, conace, spa termal și pârtii de schi în Carpați.
3. **Pachete de Croazieră:** 6 croaziere verificate (`data/cruises.json`) — Mediterana de Vest, Insulele Grecești, Golful Persic/Dubai, Fiordurile Norvegiei, Caraibe & Bahamas (MSC Seascape 749€) și Canare & Madeira (Costa Diadema 469€).
4. **Articole de Blog SEO:** 7 ghiduri detaliate (`data/blog_articles.json`) — bilete ieftine de avion, ghid prima croazieră, Maldive DIY, City Break Roma, vacanțe de schi (Bansko vs. Austria vs. Jasná), destinații calde de iarnă sub 300€ și city break-uri sub 100€.

---

## 5. Reguli de Design & UI
* **Formatare Prețuri & Simbol Euro:** Prețurile și simbolul `€` sunt legate prin spații indivizibile (`&nbsp;€` / `\u00A0€`) și clase `whitespace-nowrap flex-shrink-0 ml-2`, prevenind ruperea simbolului pe rândul următor.
* **Specificare `/pers`:** Toate prețurile de avion și cazare au mențiunea explicită `/pers` pentru transparență totală.
* **Hero Layouts Standardizate:** Paginile principale (Acasă, `/romania/`, `/croaziere/`) au aceeași structură modernă:
  * Înălțime compactă (`pt-5 sm:pt-8 pb-8 sm:pb-12`), lumini ambientale, casetă interactivă cu căutare text live și filtre specifice.
  * Spațiere sigură la grilă (`pt-10 sm:pt-14 pb-16 relative z-20`), fără suprapuneri între text și gradientul albastru închis.
* **Navigație Responsivă:** Meniu hamburger glisant pe mobil și aliniere simetrică pe desktop.
