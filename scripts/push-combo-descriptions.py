# -*- coding: utf-8 -*-
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data"))
from combo_notes import COMBOS, DISPLAY, BY_ID, pyramid_for  # noqa: E402

BASE_FILE = os.path.join(os.path.dirname(__file__), "..", "product-descriptions", "combos.html")
TMPDIR = "/tmp"

with open(BASE_FILE, "r", encoding="utf-8") as f:
    base = f.read()

UA = "CenziaDecants (contactoandiva@gmail.com)"
URL_TMPL = "https://api.tiendanube.com/v1/6474513/products/{}"

NUM_WORDS = {2: "los 2", 3: "los 3", 4: "los 4", 5: "los 5"}


def fmt_price(n):
    return "${:,}".format(n).replace(",", ".")


for combo in COMBOS:
    qty = len(combo["frags"])
    cards = []
    for i, fid in enumerate(combo["frags"], start=1):
        name, brand = DISPLAY[fid]
        p = BY_ID[fid]
        py = pyramid_for(fid)
        card = f'''    <div class="olf-mini">
      <div class="n">{i} / {qty} — {brand}</div>
      <h4>{name}</h4>
      <p class="blurb">"{p['tag']}"</p>
      <div class="pyramid">
        <div><b>Salida</b><p>{py['salida']}</p></div>
        <div><b>Corazón</b><p>{py['corazon']}</p></div>
        <div><b>Fondo</b><p>{py['fondo']}</p></div>
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
