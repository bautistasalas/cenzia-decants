// Renderiza un banner del carrusel de la portada en sus dos formatos.
// Uso:  cd banners && node render.js unico-4x3/banner.html [más banners...] [--sin-promo]
// Deja en out/:
//   {carpeta}-computadora.png  1920 x 736
//   {carpeta}-celular.png      1920 x 1440  (celular, 4:3)
// Con --sin-promo saca el aviso del 4x3 y los nombra {carpeta}-sin-promo-{formato}.png.
// Por cada formato imprime dónde quedó cada bloque y avisa ("fuera") si algún texto se sale del banner
// o ("pisa") si el texto se mete debajo de la foto.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FORMATOS = [
  { nombre: 'computadora', query: '', width: 1920, height: 736 },
  { nombre: 'celular', query: 'f=celular', width: 1920, height: 1440 },
];

(async () => {
  const args = process.argv.slice(2);
  const sinPromo = args.includes('--sin-promo');
  const files = args.filter(a => !a.startsWith('--'));
  const outDir = path.join(__dirname, 'out');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  for (const f of files) {
    const base = path.basename(path.dirname(path.resolve(f))) + (sinPromo ? '-sin-promo' : '');
    for (const fmt of FORMATOS) {
      const ctx = await browser.newContext({ viewport: { width: fmt.width, height: fmt.height }, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      const query = [fmt.query, sinPromo ? 'promo=0' : ''].filter(Boolean).join('&');
      await page.goto('file://' + path.resolve(f) + (query ? '?' + query : ''));
      await page.evaluate(() => document.fonts.ready);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(300);
      const out = path.join(outDir, `${base}-${fmt.nombre}.png`);
      await page.screenshot({ path: out, clip: { x: 0, y: 0, width: fmt.width, height: fmt.height } });
      const info = await page.evaluate(() => {
        const B = document.querySelector('.banner').getBoundingClientRect();
        const rect = e => { const b = e.getBoundingClientRect(); return [b.left, b.top, b.right, b.bottom].map(Math.round); };
        // el ancho real del texto de cada bloque (no el de su caja)
        const texto = e => { const r = document.createRange(); r.selectNodeContents(e); return rect(r); };
        const bloques = {};
        for (const e of document.querySelectorAll('.txt > *')) {
          if (getComputedStyle(e).display === 'none') continue;
          bloques[e.className] = texto(e);
        }
        const fuera = Object.entries(bloques).filter(([, r]) => r[0] < B.left || r[2] > B.right || r[1] < B.top || r[3] > B.bottom).map(([k]) => k);
        const foto = document.querySelector('.banner > img');
        const F = foto ? rect(foto) : null;
        const fuentes = [...new Set([...document.fonts].filter(x => x.status === 'loaded').map(x => `${x.family} ${x.weight}`))];
        return { fuera, bloques, foto: F, fuentes };
      });
      console.log(out, `${fmt.width}x${fmt.height}`, JSON.stringify(info));
      await ctx.close();
    }
  }
  await browser.close();
})();
