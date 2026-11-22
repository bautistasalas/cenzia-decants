# -*- coding: utf-8 -*-
"""Arma las hojas de logos para recortar (etiqueta térmica de 100 x 150 mm, Xprinter XP-470B, blanco y negro).

    4-por-hoja.html   4 stickers de 50 x 75 mm
    6-por-hoja.html   6 stickers redondos de 44 mm (en celdas de 50 x 50 mm)
    8-por-hoja.html   8 stickers rectangulares de 50 x 37,5 mm

La hoja siempre queda dividida en partes iguales (pedido de Bautista).

En las dos alterna el logo en negro sobre blanco y en blanco sobre negro, con líneas punteadas de corte.
Uso:  python3 build.py     (después:  cd .. && node render.js logos/*.html)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MARCA, BAJADA = "CENZIA", "FRAGANCIAS"

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Logos para recortar · {TXT}</title>
<!-- Etiqueta térmica de 100 x 150 mm (Xprinter XP-470B, 203 dpi, blanco y negro). {TXT}.
     Solo negro pleno y blanco. Archivo generado por build.py: los cambios se hacen ahí. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap" rel="stylesheet">
<style>
@page{{size:100mm 150mm;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100mm;height:150mm;background:#fff}}
body{{font-family:"Poppins",system-ui,sans-serif;color:#000}}
.label{{position:relative;width:100mm;height:150mm;overflow:hidden;background:#fff}}
.cell{{position:absolute;width:50mm;height:{CH}mm;display:flex;align-items:center;justify-content:center}}
.cutv{{position:absolute;left:50mm;top:0;bottom:0;width:0;border-left:.38mm dashed #000}}
.cuth{{position:absolute;left:0;right:0;height:0;border-top:.38mm dashed #000}}
.w{{font-weight:700;letter-spacing:.2em;line-height:1;text-align:left;white-space:nowrap}}
.w small{{display:block;font-weight:600;letter-spacing:.27em;white-space:nowrap}}
{CSS}</style>
</head>
<body>
<div class="label">
{BODY}</div>
</body>
</html>
"""

RECT_CSS = """
.box{width:44mm;height:31.5mm;border-radius:4.5mm;display:flex;align-items:center;justify-content:center;gap:2.4mm}
.neg .box{background:#000;color:#fff}
.box img{height:17.5mm;width:auto;display:block}
.w{font-size:16.4pt}
.w small{font-size:8.55pt;margin-top:1.3mm}
"""
BIG_CSS = """
.box{width:44mm;height:69mm;border-radius:5mm;display:flex;flex-direction:column;align-items:center;justify-content:center}
.neg .box{background:#000;color:#fff}
.box img{height:31mm;width:auto;display:block}
.w{font-size:16pt;text-align:center;text-indent:.2em;margin-top:4mm}
.w small{font-size:8.35pt;margin-top:1.4mm;text-indent:.27em}
"""
ROUND_CSS = """
.box{width:44mm;height:44mm;border-radius:50%;border:.9mm solid #000;display:flex;flex-direction:column;align-items:center;justify-content:center}
.neg .box{background:#000;color:#fff}
.box img{height:17mm;width:auto;display:block;margin-top:-1mm}
.w{font-size:13pt;text-align:center;text-indent:.2em;margin-top:2mm}
.w small{font-size:6.8pt;margin-top:1.1mm;text-indent:.27em}
"""


def cell(col, row, ch, neg):
    iso = "isotipo-blanco.png" if neg else "isotipo-negro.png"
    return (f'<div class="cell{" neg" if neg else ""}" style="left:{col * 50}mm;top:{row * ch}mm">'
            f'<div class="box"><img src="../assets/{iso}" alt=""><div class="w">{MARCA}<small>{BAJADA}</small></div></div></div>\n')


def sheet(rows, css, txt, name):
    ch = 150 / rows
    body = "".join(cell(c, r, ch, (c + r) % 2 == 1) for r in range(rows) for c in range(2))
    body += '<div class="cutv"></div>\n' + "".join(f'<div class="cuth" style="top:{r * ch}mm"></div>\n' for r in range(1, rows))
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        f.write(HEAD.format(TXT=txt, CH=ch, CSS=css.lstrip("\n"), BODY=body))
    print("ok", name)


if __name__ == "__main__":
    sheet(2, BIG_CSS, "4 stickers de 50 x 75 mm", "4-por-hoja.html")
    sheet(3, ROUND_CSS, "6 stickers redondos de 44 mm", "6-por-hoja.html")
    sheet(4, RECT_CSS, "8 stickers rectangulares de 50 x 37,5 mm", "8-por-hoja.html")
