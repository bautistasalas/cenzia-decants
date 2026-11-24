// Renderiza un banner del carrusel de la portada en sus dos formatos.
// Uso:  cd banners && node render.js unico-4x3/banner.html
// Deja en out/:
//   {carpeta}-computadora.png  1920 x 736
//   {carpeta}-celular.png      1920 x 1440  (celular, 4:3)
// Por cada formato imprime dónde quedó cada bloque y avisa ("fuera") si algún texto se sale del banner.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const FORMATOS = [
  { nombre: 'computadora', query: '', width: 1920, height: 736 },
  { nombre: 'celular', query: '?f=celular', width: 1920, height: 1440 },
];

(async () => {
  const files = process.argv.slice(2);
  const outDir = path.join(__dirname, 'out');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  for (const f of files) {
    const base = path.basename(path.dirname(path.resolve(f)));
    for (const fmt of FORMATOS) {
      const ctx = await browser.newContext({ viewport: { width: fmt.width, height: fmt.height }, deviceScaleFactor: 1 });
      const page = await ctx.newPage();
      await page.goto('file://' + path.resolve(f) + fmt.query);
      await page.evaluate(() => document.fonts.ready);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(300);
      const out = path.join(outDir, `${base}-${fmt.nombre}.png`);
      await page.screenshot({ path: out, clip: { x: 0, y: 0, width: fmt.width, height: fmt.height } });
      const info = await page.evaluate(() => {
        const B = document.querySelector('.banner').getBoundingClientRect();
        const fuera = [...document.querySelectorAll('.txt *')].filter(e => {
          const r = e.getBoundingClientRect();
          return r.width && (r.left < B.left || r.right > B.right || r.top < B.top || r.bottom > B.bottom);
        }).map(e => e.className || e.tagName);
        const r = s => { const b = document.querySelector(s).getBoundingClientRect(); return [b.left, b.top, b.right, b.bottom].map(Math.round); };
        const fuentes = [...document.fonts].filter(x => x.status === 'loaded').map(x => `${x.family} ${x.weight}`);
        return { fuera, pill: r('.pill'), h1: r('.h1'), feats: r('.feats'), bot: r('.bot'), txt: r('.txt'), fuentes: [...new Set(fuentes)] };
      });
      console.log(out, `${fmt.width}x${fmt.height}`, JSON.stringify(info));
      await ctx.close();
    }
  }
  await browser.close();
})();
