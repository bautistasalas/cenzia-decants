# -*- coding: utf-8 -*-
"""Arma los HTML del sticker de agradecimiento por la preventa (cupón 5OFFVIRTUAL).

Etiqueta térmica de 100 x 150 mm (rollo "10 x 15 cm" de la Xprinter XP-470B, 203 dpi, blanco y negro).
Por cada estilo (a, b, c) salen dos archivos:
    {estilo}-completa.html   un sticker que ocupa la hoja entera (100 x 150 mm)
    {estilo}-mitad.html      dos stickers por hoja (100 x 75 mm cada uno) con la línea de corte al medio

Reglas para que imprima bien en térmica: solo negro pleno y blanco (sin grises ni degradés), líneas de
0,35 mm o más, texto de 8 pt o más y nada de letra chica en blanco sobre negro (se empasta).

Uso:  python3 build.py     (después:  cd .. && node render.js gracias-preventa/*.html)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = "5OFFVIRTUAL"
WEB = "cenziadecants.com"
IG = "@cenziadecants"

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Sticker gracias preventa · estilo {K} · {FMT_TXT}</title>
<!-- Etiqueta térmica de 100 x 150 mm (Xprinter XP-470B, 203 dpi, blanco y negro). {FMT_NOTE}
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
.st{{position:absolute;left:0;width:100mm;overflow:hidden}}
.completa .st{{top:0;height:150mm}}
.mitad .st{{height:75mm}}
.mitad .s1{{top:0}}
.mitad .s2{{top:75mm}}
.cut{{position:absolute;left:0;right:0;top:75mm;height:0;border-top:.38mm dashed #000}}
.cut svg{{position:absolute;left:3.2mm;top:-2.5mm;width:5mm;height:5mm;background:#fff}}
{CSS}</style>
</head>
<body>
<div class="label {FMT}">
{BODY}</div>
</body>
</html>
"""
CUT = ('<div class="cut"><svg viewBox="0 0 24 24"><circle cx="6.5" cy="6.5" r="3.2" fill="none" stroke="#000" stroke-width="2.2"/>'
       '<circle cx="6.5" cy="17.5" r="3.2" fill="none" stroke="#000" stroke-width="2.2"/>'
       '<path d="M9.2 8.4 21.5 18M9.2 15.6 21.5 6" fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="round"/></svg></div>\n')
FOOT = f'<div class="foot">{WEB} &nbsp;·&nbsp; {IG}</div>'

# ───────────── Estilo A: el "¡GRACIAS!" es lo que manda; el cupón va en un recuadro abajo ─────────────
A = {
 "completa": {
  "css": """
.brand{position:absolute;left:0;right:0;top:8mm;display:flex;justify-content:center;align-items:center;gap:3.2mm}
.brand img{height:15.5mm;width:auto;display:block}
.brand .w{font-weight:700;font-size:25pt;letter-spacing:.2em;line-height:1;text-align:left}
.brand .w small{display:block;font-size:13.4pt;letter-spacing:.5em;font-weight:600;margin-top:2mm}
.rule{position:absolute;left:8mm;right:8mm;top:27.6mm;height:.9mm;background:#000}
.h1{position:absolute;left:0;right:0;top:31.6mm;font-weight:800;font-size:44pt;line-height:1;white-space:nowrap;text-align:center}
.sub{position:absolute;left:0;right:0;top:48.8mm;font-weight:600;font-size:18.5pt;line-height:1.16;text-align:center;white-space:nowrap}
.msg{position:absolute;left:10mm;right:10mm;top:67mm;font-weight:500;font-size:11pt;line-height:1.34;text-align:center}
.sign{position:absolute;left:0;right:0;top:89.4mm;font-style:italic;font-weight:600;font-size:12.5pt;line-height:1;text-align:center}
.cup{position:absolute;left:7mm;right:7mm;top:98.4mm;height:40.4mm;border:1mm solid #000;border-radius:5mm;overflow:hidden;text-align:center}
.cup .off{position:absolute;left:0;right:0;top:0;height:13.4mm;background:#000;color:#fff;white-space:nowrap;line-height:13.4mm}
.cup .off b{font-weight:800;font-size:23pt;letter-spacing:.02em;vertical-align:middle}
.cup .off span{font-weight:600;font-size:12pt;margin-left:2.4mm;vertical-align:middle}
.cup .lbl{position:absolute;left:0;right:0;top:16.4mm;font-weight:700;font-size:8.6pt;letter-spacing:.3em;text-indent:.3em;line-height:1}
.cup .code{position:absolute;left:0;right:0;top:21mm;font-weight:700;font-size:30pt;letter-spacing:.04em;line-height:1;white-space:nowrap}
.cup .how{position:absolute;left:0;right:0;bottom:2.5mm;font-weight:500;font-size:8pt;line-height:1;white-space:nowrap}
.foot{position:absolute;left:0;right:0;bottom:4.3mm;font-weight:600;font-size:9.6pt;letter-spacing:.04em;line-height:1;text-align:center}
""",
  "html": f"""  <div class="brand"><img src="../assets/isotipo-negro.png" alt=""><div class="w">CENZIA<small>DECANTS</small></div></div>
  <div class="rule"></div>
  <div class="h1">¡GRACIAS!</div>
  <div class="sub">por esperar la preventa<br>y por elegirnos.</div>
  <div class="msg">Confiaste en nosotros antes de que llegara el stock, y eso vale muchísimo. Ojalá lo disfrutes tanto como nosotros disfrutamos prepararlo.</div>
  <div class="sign">— Bautista, Cenzia Decants</div>
  <div class="cup">
    <div class="off"><b>5% OFF</b><span>en tu próxima compra</span></div>
    <div class="lbl">CÓDIGO DE DESCUENTO</div>
    <div class="code">{CODE}</div>
    <div class="how">Ingresalo al finalizar tu compra en {WEB}</div>
  </div>
  {FOOT}
""",
 },
 "mitad": {
  "css": """
.brand{position:absolute;left:0;right:0;top:4.6mm;display:flex;justify-content:center;align-items:center;gap:2.2mm}
.brand img{height:10mm;width:auto;display:block}
.brand .w{font-weight:700;font-size:16.5pt;letter-spacing:.2em;line-height:1;text-align:left}
.brand .w small{display:block;font-size:9pt;letter-spacing:.48em;font-weight:600;margin-top:1.3mm}
.rule{position:absolute;left:6mm;right:6mm;top:17mm;height:.7mm;background:#000}
.h1{position:absolute;left:0;right:0;top:19.5mm;font-weight:800;font-size:30pt;line-height:1;text-align:center;white-space:nowrap}
.sub{position:absolute;left:0;right:0;top:31.3mm;font-weight:600;font-size:11.6pt;line-height:1;text-align:center;white-space:nowrap}
.sign{position:absolute;left:0;right:0;top:37.5mm;font-style:italic;font-weight:600;font-size:9.4pt;line-height:1;text-align:center}
.cup{position:absolute;left:5.5mm;right:5.5mm;bottom:5mm;height:26.6mm;border:.9mm solid #000;border-radius:4.2mm;overflow:hidden}
.cup .l{position:absolute;left:0;top:0;bottom:0;width:30mm;background:#000;color:#fff;text-align:center}
.cup .l b{display:block;font-weight:800;font-size:36pt;line-height:1;margin-top:2.5mm}
.cup .l i{display:block;font-style:normal;font-weight:800;font-size:19pt;line-height:1;letter-spacing:.12em;text-indent:.12em;margin-top:.2mm}
.cup .r{position:absolute;left:30mm;right:0;top:0;bottom:0;text-align:center}
.cup .r .when{font-weight:600;font-size:11pt;line-height:1;margin-top:3.5mm;white-space:nowrap}
.cup .r .lbl{font-weight:700;font-size:7.6pt;letter-spacing:.3em;text-indent:.3em;line-height:1;margin-top:2.7mm}
.cup .r .code{font-weight:700;font-size:20pt;letter-spacing:.03em;line-height:1;margin-top:1.4mm;white-space:nowrap}
""",
  "html": f"""  <div class="brand"><img src="../assets/isotipo-negro.png" alt=""><div class="w">CENZIA<small>DECANTS</small></div></div>
  <div class="rule"></div>
  <div class="h1">¡GRACIAS!</div>
  <div class="sub">por esperar la preventa y por elegirnos.</div>
  <div class="sign">— Bautista, Cenzia Decants</div>
  <div class="cup">
    <div class="l"><b>5%</b><i>OFF</i></div>
    <div class="r"><div class="when">en tu próxima compra</div><div class="lbl">CÓDIGO</div><div class="code">{CODE}</div></div>
  </div>
""",
 },
}

# ───────────── Estilo B: el cupón es lo que manda, con forma de vale; el gracias va arriba y la firma abajo ─────────────
B = {
 "completa": {
  "css": """
.band{position:absolute;left:6mm;right:6mm;top:6mm;height:22mm;background:#000;border-radius:5.5mm;color:#fff;display:flex;justify-content:center;align-items:center;gap:3.6mm}
.band img{height:15mm;width:auto;display:block}
.band span{font-weight:700;font-size:30pt;letter-spacing:.22em;margin-right:-.22em;line-height:1}
.thanks{position:absolute;left:0;right:0;top:32.4mm;font-weight:700;font-size:13pt;line-height:1.22;letter-spacing:.06em;text-align:center;white-space:nowrap}
.off{position:absolute;left:0;right:0;top:45mm;font-weight:800;font-size:62pt;line-height:1;text-align:center;white-space:nowrap}
.when{position:absolute;left:0;right:0;top:67.6mm;font-weight:600;font-size:19pt;line-height:1;text-align:center;white-space:nowrap}
.ticket{position:absolute;left:7mm;right:7mm;top:78.6mm;height:35.6mm;border:1.1mm dashed #000;border-radius:5mm;text-align:center}
.ticket i{display:block;font-style:normal;font-weight:700;font-size:10pt;letter-spacing:.32em;text-indent:.32em;line-height:1;margin-top:3.9mm}
.ticket b{display:block;font-weight:700;font-size:31pt;letter-spacing:.04em;line-height:1;margin-top:2.6mm;white-space:nowrap}
.ticket u{display:block;text-decoration:none;font-weight:500;font-size:8pt;line-height:1;margin-top:3.5mm;white-space:nowrap}
.msg{position:absolute;left:6mm;right:6mm;top:119.4mm;font-weight:500;font-size:11pt;line-height:1.32;text-align:center;white-space:nowrap}
.sign{position:absolute;left:0;right:0;top:132.2mm;font-style:italic;font-weight:600;font-size:11.5pt;line-height:1;text-align:center}
.foot{position:absolute;left:0;right:0;bottom:4.3mm;font-weight:600;font-size:9.6pt;letter-spacing:.04em;line-height:1;text-align:center}
""",
  "html": f"""  <div class="band"><img src="../assets/isotipo-blanco.png" alt=""><span>CENZIA</span></div>
  <div class="thanks">GRACIAS POR ESPERAR<br>LA PREVENTA Y ELEGIRNOS</div>
  <div class="off">5% OFF</div>
  <div class="when">en tu próxima compra</div>
  <div class="ticket"><i>CÓDIGO DE DESCUENTO</i><b>{CODE}</b><u>Ingresalo al finalizar tu compra en {WEB}</u></div>
  <div class="msg">Tu pedido de preventa ya está con vos.<br>Gracias por la paciencia y la confianza.</div>
  <div class="sign">— El equipo de Cenzia</div>
  {FOOT}
""",
 },
 "mitad": {
  "css": """
.band{position:absolute;left:5mm;right:5mm;top:4.5mm;height:12.4mm;background:#000;border-radius:4mm;color:#fff;display:flex;justify-content:center;align-items:center;gap:2.4mm}
.band img{height:8.8mm;width:auto;display:block}
.band span{font-weight:700;font-size:18pt;letter-spacing:.22em;margin-right:-.22em;line-height:1}
.thanks{position:absolute;left:0;right:0;top:19.5mm;font-weight:700;font-size:10pt;line-height:1.2;letter-spacing:.06em;text-align:center;white-space:nowrap}
.off{position:absolute;left:4.5mm;width:45mm;top:31mm;font-weight:800;font-size:33pt;line-height:1;text-align:center;white-space:nowrap}
.when{position:absolute;left:4.5mm;width:45mm;top:44.2mm;font-weight:600;font-size:10.6pt;line-height:1;text-align:center;white-space:nowrap}
.ticket{position:absolute;right:5.5mm;width:43.5mm;top:30.4mm;height:19mm;border:.9mm dashed #000;border-radius:3.6mm;text-align:center}
.ticket i{display:block;font-style:normal;font-weight:700;font-size:7.6pt;letter-spacing:.3em;text-indent:.3em;line-height:1;margin-top:2.7mm}
.ticket b{display:block;font-weight:700;font-size:15.4pt;letter-spacing:.03em;line-height:1;margin-top:2.1mm;white-space:nowrap}
.msg{position:absolute;left:6mm;right:6mm;top:54.6mm;font-weight:500;font-size:9.2pt;line-height:1.3;text-align:center}
.sign{position:absolute;left:0;right:0;top:61.6mm;font-style:italic;font-weight:600;font-size:9.2pt;line-height:1;text-align:center}
""",
  "html": f"""  <div class="band"><img src="../assets/isotipo-blanco.png" alt=""><span>CENZIA</span></div>
  <div class="thanks">GRACIAS POR ESPERAR<br>LA PREVENTA Y ELEGIRNOS</div>
  <div class="off">5% OFF</div>
  <div class="when">en tu próxima compra</div>
  <div class="ticket"><i>CÓDIGO</i><b>{CODE}</b></div>
  <div class="msg">Gracias por la paciencia y por confiar en nosotros.</div>
  <div class="sign">— El equipo de Cenzia</div>
""",
 },
}

# ───────────── Estilo C: una nota firmada por quien arma el pedido; el cupón cierra abajo ─────────────
C = {
 "completa": {
  "css": """
.brand{position:absolute;left:8mm;top:8mm;display:flex;align-items:center;gap:3mm}
.brand img{height:14mm;width:auto;display:block}
.brand span{font-weight:700;font-size:20pt;letter-spacing:.2em;line-height:1}
.tag{position:absolute;right:8mm;top:10mm;border:1mm solid #000;border-radius:99mm;font-weight:700;font-size:11pt;letter-spacing:.14em;line-height:1;padding:2.1mm 3.4mm 2.1mm 3.9mm}
.note{position:absolute;left:8mm;right:8mm;top:30mm;font-weight:700;font-size:23pt;line-height:1.12;white-space:nowrap}
.msg{position:absolute;left:8mm;right:8mm;top:54mm;font-weight:500;font-size:12.4pt;line-height:1.36}
.sign{position:absolute;left:8mm;top:88.4mm;font-style:italic;font-weight:600;font-size:15pt;line-height:1}
.sign small{display:block;font-style:normal;font-size:9.6pt;font-weight:700;letter-spacing:.16em;margin-top:1.8mm}
.cup{position:absolute;left:8mm;right:8mm;top:106.6mm;height:31mm;border:1.1mm solid #000;border-radius:5mm;overflow:hidden}
.cup .l{position:absolute;left:0;top:0;bottom:0;width:30mm;background:#000;color:#fff;text-align:center}
.cup .l b{display:block;font-weight:800;font-size:38pt;line-height:1;margin-top:3.6mm}
.cup .l i{display:block;font-style:normal;font-weight:800;font-size:20pt;line-height:1;letter-spacing:.12em;text-indent:.12em;margin-top:.3mm}
.cup .r{position:absolute;left:30mm;right:0;top:0;bottom:0;text-align:center}
.cup .r i{display:block;font-style:normal;font-weight:600;font-size:12pt;line-height:1;margin-top:4.3mm;white-space:nowrap}
.cup .r b{display:block;font-weight:700;font-size:19pt;letter-spacing:.025em;line-height:1;margin-top:3.1mm;white-space:nowrap}
.cup .r u{display:block;text-decoration:none;font-weight:500;font-size:8.4pt;line-height:1;margin-top:3.3mm;white-space:nowrap}
.foot{position:absolute;left:8mm;bottom:4.5mm;font-weight:600;font-size:9.6pt;letter-spacing:.04em;line-height:1}
""",
  "html": f"""  <div class="brand"><img src="../assets/isotipo-negro.png" alt=""><span>CENZIA</span></div>
  <div class="tag">PREVENTA</div>
  <div class="note">Gracias por esperar<br>y por elegirnos.</div>
  <div class="msg">Sabemos que esperar no es fácil. Confiaste en nosotros antes de que llegara el stock, y por eso armamos este pedido con muchísimo cuidado. Ojalá lo disfrutes.</div>
  <div class="sign">— Bautista<small>CENZIA DECANTS</small></div>
  <div class="cup">
    <div class="l"><b>5%</b><i>OFF</i></div>
    <div class="r"><i>en tu próxima compra</i><b>{CODE}</b><u>Usalo al finalizar tu compra</u></div>
  </div>
  {FOOT}
""",
 },
 "mitad": {
  "css": """
.brand{position:absolute;left:5.5mm;top:5mm;display:flex;align-items:center;gap:2.6mm}
.brand img{height:11.5mm;width:auto;display:block}
.brand span{font-weight:700;font-size:20pt;letter-spacing:.2em;line-height:1}
.tag{position:absolute;right:5.5mm;top:6.1mm;border:1mm solid #000;border-radius:99mm;font-weight:700;font-size:12pt;letter-spacing:.14em;line-height:1;padding:2mm 3.6mm 2mm 4.2mm}
.note{position:absolute;left:5.5mm;right:5.5mm;top:19.8mm;font-weight:700;font-size:20.5pt;line-height:1.13;white-space:nowrap}
.sign{position:absolute;left:5.5mm;top:38.2mm;font-style:italic;font-weight:600;font-size:13.5pt;line-height:1;white-space:nowrap}
.cup{position:absolute;left:5.5mm;right:5.5mm;bottom:5mm;height:25mm;border:1mm solid #000;border-radius:4.5mm;overflow:hidden}
.cup .l{position:absolute;left:0;top:0;bottom:0;width:31mm;background:#000;color:#fff;text-align:center}
.cup .l b{display:block;font-weight:800;font-size:35pt;line-height:1;margin-top:1.9mm}
.cup .l i{display:block;font-style:normal;font-weight:800;font-size:19pt;line-height:1;letter-spacing:.12em;text-indent:.12em;margin-top:.2mm}
.cup .r{position:absolute;left:31mm;right:0;top:0;bottom:0;text-align:center}
.cup .r i{display:block;font-style:normal;font-weight:600;font-size:12.6pt;line-height:1;margin-top:4.5mm;white-space:nowrap}
.cup .r b{display:block;font-weight:700;font-size:19.6pt;letter-spacing:.025em;line-height:1;margin-top:3mm;white-space:nowrap}
""",
  "html": f"""  <div class="brand"><img src="../assets/isotipo-negro.png" alt=""><span>CENZIA</span></div>
  <div class="tag">PREVENTA</div>
  <div class="note">Gracias por esperar<br>y por elegirnos.</div>
  <div class="sign">— Bautista, Cenzia Decants</div>
  <div class="cup">
    <div class="l"><b>5%</b><i>OFF</i></div>
    <div class="r"><i>en tu próxima compra</i><b>{CODE}</b></div>
  </div>
""",
 },
}

FMT = {
 "completa": ("hoja completa", "Un sticker que ocupa la hoja entera."),
 "mitad": ("dos por hoja", "Dos stickers de 100 x 75 mm; se corta por la línea punteada del medio."),
}


def scope(css, fmt):
    """Cada regla del estilo queda atada al formato, para que no se pise con las de la hoja."""
    out = []
    for line in css.strip().splitlines():
        out.append(f".{fmt} {line}" if line.startswith(".") else line)
    return "\n".join(out) + "\n"


def build():
    for key, style in (("a", A), ("b", B), ("c", C)):
        for fmt, (txt, note) in FMT.items():
            part = style[fmt]
            if fmt == "completa":
                body = f'<div class="st">\n{part["html"]}</div>\n'
            else:
                body = f'<div class="st s1">\n{part["html"]}</div>\n{CUT}<div class="st s2">\n{part["html"]}</div>\n'
            html = HEAD.format(K=key.upper(), FMT=fmt, FMT_TXT=txt, FMT_NOTE=note, CSS=scope(part["css"], fmt), BODY=body)
            with open(os.path.join(HERE, f"{key}-{fmt}.html"), "w", encoding="utf-8") as f:
                f.write(html)
            print("ok", f"{key}-{fmt}.html")


if __name__ == "__main__":
    build()
