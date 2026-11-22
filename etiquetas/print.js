// Archivos para imprimir una etiqueta en la térmica (hoja de 100 x 150 mm).
// Uso:  cd etiquetas && node print.js gracias-preventa/a-completa.html [más archivos...]
// Deja en out/ un PDF del tamaño exacto de la hoja (con la tipografía incluida) por cada archivo.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const files = process.argv.slice(2);
  const outDir = path.join(__dirname, 'out');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const f of files) {
    const name = path.basename(path.dirname(path.resolve(f))) + '-' + path.basename(f, '.html');
    await page.goto('file://' + path.resolve(f), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const out = path.join(outDir, name + '.pdf');
    await page.pdf({ path: out, width: '100mm', height: '150mm', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
    console.log(out, fs.statSync(out).size);
  }
  await browser.close();
})();
