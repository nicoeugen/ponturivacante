import rss from '@astrojs/rss';
import deals from '../../data/deals.json';

export async function GET(context) {
  return rss({
    title: 'PonturiVacanțe — Zboruri Ieftine & Vacanțe pe Cont Propriu',
    description: 'Cele mai noi oferte de vacanțe DIY din România: zboruri low-cost combinate cu opțiuni de cazare verificate.',
    site: context.site || 'https://ponturivacante.ro',
    items: deals.map((deal) => ({
      title: `${deal.title} — ${deal.priceTotalPerPerson}€ (${deal.originCity})`,
      pubDate: new Date(deal.publishedAt),
      description: `Zbor din ${deal.originCity} + ${deal.nights} nopți cazare la ${deal.destination} pentru doar ${deal.priceTotalPerPerson}€ de persoană.`,
      link: `/oferta/${deal.slug}/`,
    })),
    customData: `<language>ro-ro</language>`,
  });
}
