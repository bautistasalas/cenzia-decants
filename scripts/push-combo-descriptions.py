# -*- coding: utf-8 -*-
"""Genera la descripción de cada combo Cenzia Privé desde combos.html y la sube.

Uso:
    python3 scripts/push-combo-descriptions.py --diff   # compara con la tienda, no sube nada
    python3 scripts/push-combo-descriptions.py          # sube

Correr SIEMPRE --diff antes de subir: las descripciones también se editan a
mano en la tienda (ej. el cartel de preventa) y este script pisa todo el HTML.
Si el diff muestra un cambio que no viene de este repo, primero hay que traer
ese cambio a combos.html.
"""
import difflib
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data"))
from combo_notes import COMBOS, DISPLAY, BY_ID, BLURB, pyramid_for  # noqa: E402

BASE_FILE = os.path.join(os.path.dirname(__file__), "..", "product-descriptions", "combos.html")
TMPDIR = "/tmp"

with open(BASE_FILE, "r", encoding="utf-8") as f:
    base = f.read()

UA = "CenziaDecants (contactoandiva@gmail.com)"
URL_TMPL = "https://api.tiendanube.com/v1/6474513/products/{}"

NUM_WORDS = {2: "los 2", 3: "los 3", 4: "los 4", 5: "los 5", 6: "los 6"}


def fmt_price(n):
    return "${:,}".format(n).replace(",", ".")


def cards_data(combo):
    """Tarjetas del carrusel: escritas a mano ("cards") o armadas desde los IDs ("frags")."""
    if "cards" in combo:
        return combo["cards"]
    out = []
    for fid in combo["frags"]:
        name, brand = DISPLAY[fid]
        out.append({"brand": brand, "name": name, "blurb": BLURB[fid], **pyramid_for(fid)})
    return out


def build(combo):
    data = cards_data(combo)
    qty = len(data)
    cards = []
    for i, c in enumerate(data, start=1):
        card = f'''    <div class="olf-mini">
      <div class="n">{i} / {qty} — {c['brand']}</div>
      <h4>{c['name']}</h4>
      <p class="blurb">{c['blurb']}</p>
      <div class="pyramid">
        <div><b>Salida</b><p>{c['salida']}</p></div>
        <div><b>Corazón</b><p>{c['corazon']}</p></div>
        <div><b>Fondo</b><p>{c['fondo']}</p></div>
      </div>
    </div>'''
        cards.append(card)
    track_html = "\n".join(cards)
    dots_html = "".join("<span></span>" for _ in range(qty))

    unit_price = round(combo["price"] / qty / 100) * 100
    unit_price_txt = f"Desde {fmt_price(unit_price)} c/u"

    html = base
    html = html.replace("{{OLF_TRACK}}", track_html)
    html = html.replace("{{OLF_DOTS}}", dots_html)
    html = html.replace("{{COMBO_QTY_TXT}}", NUM_WORDS.get(qty, str(qty)))
    html = html.replace("{{COMBO_QTY}}", str(qty))
    html = html.replace("{{COMBO_UNIT_PRICE}}", unit_price_txt)
    assert "{{" not in html, "quedó un placeholder sin completar"
    return html


def fetch_live(pid):
    out = subprocess.run(
        ["curl", "-sS", URL_TMPL.format(pid) + "?fields=id,description", "-H", f"User-Agent: {UA}"],
        capture_output=True, text=True,
    ).stdout
    return json.loads(out)["description"]["es"]


def norm(html):
    # Tienda Nube devuelve el HTML con otros saltos de línea / espacios.
    return [ln.strip() for ln in html.replace("\r\n", "\n").split("\n") if ln.strip()]


DIFF_ONLY = "--diff" in sys.argv

for combo in COMBOS:
    html = build(combo)

    if DIFF_ONLY:
        live = fetch_live(combo["id"])
        diff = list(difflib.unified_diff(norm(live), norm(html), "tienda", "repo", lineterm="", n=0))
        print(f"=== combo {combo['id']} ({combo['name']}): {'sin cambios' if not diff else 'cambios'}")
        for ln in diff[2:]:
            print("   " + ln[:260])
        continue

    payload = {"description": {"es": html}}
    payload_path = f"{TMPDIR}/desc_payload_combo_{combo['id']}.json"
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload, f)

    result = subprocess.run(
        [
            "curl", "-sS", "-X", "PUT", URL_TMPL.format(combo["id"]),
            "-H", f"User-Agent: {UA}",
            "-H", "Content-Type: application/json",
            "-d", f"@{payload_path}",
            "-w", "\\nHTTP_STATUS:%{http_code}\\n",
            "-o", "/dev/null",
        ],
        capture_output=True, text=True,
    )
    print(f"combo {combo['id']} ({combo['name']}): {result.stdout.strip()} {result.stderr.strip()}")
    time.sleep(1)  # la API corta con 429 si se le pega muy seguido
