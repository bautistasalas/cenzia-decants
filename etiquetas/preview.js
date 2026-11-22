// Arma la imagen de preview de un estilo: la hoja completa y la de dos por hoja, lado a lado.
// Uso:  cd etiquetas && node preview.js gracias-preventa a "título" [b "título" ...]
// Antes hay que correr render.js (toma los PNG de out/).
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const [folder, ...rest] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1020 }, deviceScaleFactor: 2 });
  for (let i = 0; i < rest.length; i += 2) {
    const [k, title] = [rest[i], rest[i + 1]];
    const img = f => `${folder}-${k}-${f}.png`;   // relativo a out/, donde se escribe la página
    const html = `<!doctype html><html><head><meta charset="utf-8">
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&display=swap" rel="stylesheet">
      <style>
        *{box-sizing:border-box;margin:0;padding:0}
        body{width:1200px;height:1020px;background:#e7ebef;font-family:Poppins,sans-serif;color:#0d161f}
        h1{position:absolute;left:60px;top:38px;font-size:30px;font-weight:700;line-height:1}
        h1 span{font-weight:500;color:#5b6672}
        figure{position:absolute;top:104px;width:520px}
        figure.f1{left:60px} figure.f2{left:620px}
        figure img{display:block;width:520px;height:780px;border-radius:14px;box-shadow:0 10px 30px rgba(13,22,31,.18),0 0 0 1px rgba(13,22,31,.10)}
        figcaption{margin-top:22px;font-size:22px;font-weight:600;line-height:1.25}
        figcaption small{display:block;font-size:18px;font-weight:500;color:#5b6672;margin-top:4px}
      </style></head><body>
      <h1>Opción ${k.toUpperCase()} <span>· ${title}</span></h1>
      <figure class="f1"><img src="${img('completa')}"><figcaption>Hoja completa<small>1 sticker de 10 × 15 cm</small></figcaption></figure>
      <figure class="f2"><img src="${img('mitad')}"><figcaption>Dos por hoja<small>2 stickers de 10 × 7,5 cm · se corta por la línea</small></figcaption></figure>
      </body></html>`;
    const tmp = path.join(__dirname, 'out', `_preview-${k}.html`);
    fs.writeFileSync(tmp, html);
    await page.goto('file://' + tmp, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(400);
    const out = path.join(__dirname, 'out', `preview-${folder}-${k}.png`);
    await page.screenshot({ path: out });
    fs.unlinkSync(tmp);
    console.log(out);
  }
  await browser.close();
})();
