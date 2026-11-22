// Imagen de boceto con varias hojas lado a lado.
// Uso:  cd etiquetas && node preview-hojas.js <salida> "<título>" "<png en out/>|<leyenda>|<bajada>" ...
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [outName, title, ...items] = process.argv.slice(2);
  const n = items.length, W = 60 + n * 400 + (n - 1) * 40 + 60;
  const figs = items.map((it, i) => { const [f, cap, sub] = it.split('|');
    return `<figure style="left:${60 + i * 440}px"><img src="${f}"><figcaption>${cap}<small>${sub || ''}</small></figcaption></figure>`; }).join('');
  const html = `<!doctype html><html><head><meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
    <style>*{box-sizing:border-box;margin:0;padding:0}
    body{width:${W}px;height:850px;background:#e7ebef;font-family:Poppins,sans-serif;color:#0d161f}
    h1{position:absolute;left:60px;top:36px;font-size:28px;font-weight:700;line-height:1}
    figure{position:absolute;top:96px;width:400px}
    figure img{display:block;width:400px;height:600px;border-radius:11px;box-shadow:0 10px 30px rgba(13,22,31,.18),0 0 0 1px rgba(13,22,31,.10)}
    figcaption{margin-top:20px;font-size:21px;font-weight:600;line-height:1.25}
    figcaption small{display:block;font-size:17px;font-weight:500;color:#5b6672;margin-top:4px}</style></head>
    <body><h1>${title}</h1>${figs}</body></html>`;
  const tmp = path.join(__dirname, 'out', `_${outName}.html`);
  fs.writeFileSync(tmp, html);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: 850 }, deviceScaleFactor: 2 });
  await page.goto('file://' + tmp, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  const out = path.join(__dirname, 'out', outName + '.png');
  await page.screenshot({ path: out });
  fs.unlinkSync(tmp);
  await browser.close();
  console.log(out);
})();
