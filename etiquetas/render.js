// Renderiza una etiqueta (HTML en milímetros) a PNG.
// Uso:  cd etiquetas && node render.js gracias-preventa/opcion-a.html [más archivos...]
// Por cada archivo deja en out/:
//   {nombre}.png         -> la etiqueta en alta resolución (para verla)
//   {nombre}-203dpi.png  -> a la resolución real de la impresora térmica (8 puntos por mm), tal como la recibe
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const files = process.argv.slice(2);
  const outDir = path.join(__dirname, 'out');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  for (const f of files) {
    const name = path.basename(path.dirname(path.resolve(f))) + '-' + path.basename(f, '.html');
    for (const [suffix, dsf] of [['', 5], ['-203dpi', 203 / 96]]) {
      const ctx = await browser.newContext({ viewport: { width: 420, height: 600 }, deviceScaleFactor: dsf });
      const page = await ctx.newPage();
      await page.goto('file://' + path.resolve(f));
      await page.evaluate(() => document.fonts.ready);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(300);
      const box = await page.locator('.label').boundingBox();
      const out = path.join(outDir, name + suffix + '.png');
      await page.screenshot({ path: out, clip: box });
      // texto que se sale de su caja o de la etiqueta: se avisa
      const overflow = await page.evaluate(() => {
        const L = document.querySelector('.label').getBoundingClientRect();
        return [...document.querySelectorAll('.label *')].filter(e => {
          const r = e.getBoundingClientRect();
          return r.width && (r.left < L.left - 0.5 || r.right > L.right + 0.5 || r.top < L.top - 0.5 || r.bottom > L.bottom + 0.5 || e.scrollWidth > e.clientWidth + 1);
        }).map(e => e.className || e.tagName);
      });
      console.log(out, `${Math.round(box.width * dsf)}x${Math.round(box.height * dsf)}`, overflow.length ? 'OJO se sale: ' + overflow.join(', ') : '');
      await ctx.close();
    }
  }
  await browser.close();
})();
