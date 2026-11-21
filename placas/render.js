// Genera las placas de galería (2000 x 2000) desde card.html + placas.json.
// Uso:  cd placas && node render.js [slug] [boceto|final] [--datos decants.json]
//   --datos decants.json -> placas de la línea Decants Originales; salen como out/decant-{slug}-{modo}.png
//   boceto -> frasco real + zonas rotuladas para cada materia (guía para generar la foto en Runway)
//   final  -> con la foto ya generada (campo "scene" de placas.json)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const args = process.argv.slice(2);
  const di = args.indexOf('--datos');
  const dataFile = di >= 0 ? args.splice(di, 2)[1] : 'placas.json';
  const prefix = dataFile === 'placas.json' ? '' : path.basename(dataFile, '.json').replace(/s$/, '') + '-';
  const modeArg = args.find(a => a === 'boceto' || a === 'final');
  const only = args.find(a => a !== 'boceto' && a !== 'final');
  const cards = JSON.parse(fs.readFileSync(path.join(__dirname, dataFile), 'utf8')).filter(c => !only || c.slug === only);
  fs.mkdirSync(path.join(__dirname, 'out'), { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2000, height: 2000 }, deviceScaleFactor: 1 });
  for (const c of cards) {
    const mode = modeArg || (c.scene ? 'final' : 'boceto');
    await page.goto('about:blank');
    await page.goto('file://' + path.join(__dirname, 'card.html') + '#' + encodeURIComponent(JSON.stringify({ ...c, mode })));
    await page.waitForSelector('body[data-ready="1"]', { timeout: 30000 });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(400);
    const fit = await page.getAttribute('body', 'data-fit');
    const out = path.join(__dirname, 'out', `${prefix}${c.slug}-${mode}.png`);
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 2000, height: 2000 } });
    console.log(fit === 'ok' ? 'ok' : 'OJO: el texto no entra', out);
  }
  await browser.close();
})();
