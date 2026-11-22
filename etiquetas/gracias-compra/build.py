# -*- coding: utf-8 -*-
"""Arma el HTML del sticker de agradecimiento general (para cualquier compra, no solo la preventa).

Es el mismo diseño que Bautista aprobó para la preventa (gracias-preventa/a-mitad.html): dos stickers
de 100 x 75 mm por etiqueta térmica de 100 x 150 mm (Xprinter XP-470B, 203 dpi, blanco y negro), con
la línea de corte al medio. Cambia el mensaje, que acá lleva un renglón más, y por eso los bloques
están corridos un par de milímetros.

Reglas para que imprima bien en térmica: solo negro pleno y blanco (sin grises ni degradés), líneas de
0,35 mm o más, texto de 8 pt o más y nada de letra chica en blanco sobre negro (se empasta).

Uso:  python3 build.py     (después:  cd .. && node render.js gracias-compra/dos-por-hoja.html
                                              && node print.js gracias-compra/dos-por-hoja.html)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = "5OFFVIRTUAL"          # el mismo cupón del sticker de preventa
MARCA = "Cenzia Fragancias"   # así firma el sticker (pedido de Bautista); el sitio y el Instagram no cambian
BAJADA = "FRAGANCIAS"         # renglón chico debajo de CENZIA en el logo

# El mensaje: lo que cambia respecto del sticker de preventa.
GRACIAS = "¡GRACIAS!"
SUB = "por tu compra y por confiar en nosotros."
MSG = "Espero que lo disfrutes muchísimo."
FIRMA = f"— Bautista, {MARCA}"

STICKER = f"""  <div class="brand"><img src="../assets/isotipo-negro.png" alt=""><div class="w">CENZIA<small>{BAJADA}</small></div></div>
  <div class="rule"></div>
  <div class="h1">{GRACIAS}</div>
  <div class="sub">{SUB}</div>
  <div class="msg">{MSG}</div>
  <div class="sign">{FIRMA}</div>
  <div class="cup">
    <div class="l"><b>5%</b><i>OFF</i></div>
    <div class="r"><div class="when">en tu próxima compra</div><div class="lbl">CÓDIGO</div><div class="code">{CODE}</div></div>
  </div>
"""

CUT = ('<div class="cut"><svg viewBox="0 0 24 24"><circle cx="6.5" cy="6.5" r="3.2" fill="none" stroke="#000" stroke-width="2.2"/>'
       '<circle cx="6.5" cy="17.5" r="3.2" fill="none" stroke="#000" stroke-width="2.2"/>'
       '<path d="M9.2 8.4 21.5 18M9.2 15.6 21.5 6" fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="round"/></svg></div>\n')

HTML = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Sticker gracias por tu compra · dos por hoja</title>
<!-- Etiqueta térmica de 100 x 150 mm (Xprinter XP-470B, 203 dpi, blanco y negro).
     Dos stickers de 100 x 75 mm; se corta por la línea punteada del medio.
     Archivo generado por build.py: los cambios se hacen ahí. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,500;0,600;0,700;0,800;1,500;1,600&display=swap" rel="stylesheet">
<style>
@page{{size:100mm 150mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100mm;height:150mm;background:#fff}}
body{{font-family:"Poppins",system-ui,sans-serif;color:#000}}
.label{{position:relative;width:100mm;height:150mm;overflow:hidden;background:#fff}}
.st{{position:absolute;left:0;width:100mm;height:75mm;overflow:hidden}}
.s1{{top:0}}
.s2{{top:75mm}}
.cut{{position:absolute;left:0;right:0;top:75mm;height:0;border-top:.38mm dashed #000}}
.cut svg{{position:absolute;left:3.2mm;top:-2.5mm;width:5mm;height:5mm;background:#fff}}
.brand{{position:absolute;left:0;right:0;top:4mm;display:flex;justify-content:center;align-items:center;gap:2.2mm}}
.brand img{{height:9.6mm;width:auto;display:block}}
.brand .w{{font-weight:700;font-size:16pt;letter-spacing:.2em;line-height:1;text-align:left}}
.brand .w small{{display:block;font-size:8.4pt;letter-spacing:.27em;font-weight:600;margin-top:1.2mm;white-space:nowrap}}
.rule{{position:absolute;left:6mm;right:6mm;top:15.6mm;height:.7mm;background:#000}}
.h1{{position:absolute;left:0;right:0;top:17.6mm;font-weight:800;font-size:28.5pt;line-height:1;text-align:center;white-space:nowrap}}
.sub{{position:absolute;left:0;right:0;top:28.8mm;font-weight:600;font-size:11.6pt;line-height:1;text-align:center;white-space:nowrap}}
.msg{{position:absolute;left:0;right:0;top:34.2mm;font-weight:500;font-size:10pt;line-height:1;text-align:center;white-space:nowrap}}
.sign{{position:absolute;left:0;right:0;top:39.3mm;font-style:italic;font-weight:600;font-size:9.4pt;line-height:1;text-align:center}}
.cup{{position:absolute;left:5.5mm;right:5.5mm;bottom:4.6mm;height:25.4mm;border:.9mm solid #000;border-radius:4.2mm;overflow:hidden}}
.cup .l{{position:absolute;left:0;top:0;bottom:0;width:30mm;background:#000;color:#fff;text-align:center}}
.cup .l b{{display:block;font-weight:800;font-size:35pt;line-height:1;margin-top:2.1mm}}
.cup .l i{{display:block;font-style:normal;font-weight:800;font-size:18.6pt;line-height:1;letter-spacing:.12em;text-indent:.12em;margin-top:.2mm}}
.cup .r{{position:absolute;left:30mm;right:0;top:0;bottom:0;text-align:center}}
.cup .r .when{{font-weight:600;font-size:11pt;line-height:1;margin-top:3.1mm;white-space:nowrap}}
.cup .r .lbl{{font-weight:700;font-size:7.6pt;letter-spacing:.3em;text-indent:.3em;line-height:1;margin-top:2.5mm}}
.cup .r .code{{font-weight:700;font-size:20pt;letter-spacing:.03em;line-height:1;margin-top:1.3mm;white-space:nowrap}}
</style>
</head>
<body>
<div class="label">
<div class="st s1">
{STICKER}</div>
{CUT}<div class="st s2">
{STICKER}</div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    with open(os.path.join(HERE, "dos-por-hoja.html"), "w", encoding="utf-8") as f:
        f.write(HTML)
    print("ok dos-por-hoja.html")
