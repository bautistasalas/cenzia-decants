// Genera las placas de galería (2000 x 2000) desde card.html + placas.json.
// Uso:  cd placas && node render.js            -> todas, en out/
//       cd placas && node render.js <slug>     -> una sola
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const only = process.argv[2];
  const cards = JSON.parse(fs.readFileSync(path.join(__dirname, 'placas.json'), 'utf8')).filter(c => !only || c.slug === only);
  fs.mkdirSync(path.join(__dirname, 'out'), { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 2000, height: 2000 }, deviceScaleFactor: 1 });
  for (const c of cards) {
    await page.goto('about:blank');
    await page.goto('file://' + path.join(__dirname, 'card.html') + '#' + encodeURIComponent(JSON.stringify(c)));
    await page.waitForSelector('body[data-ready="1"]', { timeout: 30000 });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(400);
    const out = path.join(__dirname, 'out', c.slug + '.png');
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: 2000, height: 2000 } });
    console.log('ok', out);
  }
  await browser.close();
})();
