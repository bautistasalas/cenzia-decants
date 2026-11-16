# -*- coding: utf-8 -*-
"""Genera la descripción de cada Esencia Privé individual desde extractos.html y la sube.

Uso:
    python3 scripts/push-olfactory-notes.py --diff   # compara con la tienda, no sube nada
    python3 scripts/push-olfactory-notes.py          # sube

Correr SIEMPRE --diff antes de subir: las descripciones también se editan a
mano en la tienda (ej. el cartel de preventa) y este script pisa todo el HTML.
Si el diff muestra un cambio que no viene de este repo, primero hay que traer
ese cambio a extractos.html.
"""
import difflib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

# "olfactory-notes.py" tiene guion, así que se carga con exec en vez de import.
_ns = {}
with open(os.path.join(HERE, "data", "olfactory-notes.py"), "r", encoding="utf-8") as _f:
    exec(compile(_f.read(), "olfactory-notes.py", "exec"), _ns)
PRODUCTS = _ns["PRODUCTS"]

BASE_FILE = os.path.join(HERE, "..", "product-descriptions", "extractos.html")
TMPDIR = "/tmp"

with open(BASE_FILE, "r", encoding="utf-8") as f:
    base = f.read()

UA = "CenziaDecants (contactoandiva@gmail.com)"
URL_TMPL = "https://api.tiendanube.com/v1/6474513/products/{}"

PLACEHOLDERS = {
    "{{INSP_NAME}}": "insp",
    "{{OLF_TAG}}": "tag",
    "{{OLF_SALIDA}}": "salida",
    "{{OLF_CORAZON}}": "corazon",
    "{{OLF_FONDO}}": "fondo",
    "{{OLF_DESC}}": "desc",
    "{{OLF_GENERO}}": "genero",
    "{{OLF_FAMILIA}}": "familia",
    "{{OLF_IDEAL}}": "ideal",
    "{{OLF_INTENSIDAD}}": "intensidad",
}


def build(p):
    html = base
    for ph, key in PLACEHOLDERS.items():
        html = html.replace(ph, p[key])
    assert "{{" not in html, "quedó un placeholder sin completar"
    return html


def fetch_live(pid):
    out = subprocess.run(
        ["curl", "-sS", URL_TMPL.format(pid) + "?fields=id,description", "-H", f"User-Agent: {UA}"],
        capture_output=True, text=True,
    ).stdout
    return json.loads(out)["description"]["es"]


def norm(html):
    return [ln.strip() for ln in html.replace("\r\n", "\n").split("\n") if ln.strip()]


DIFF_ONLY = "--diff" in sys.argv

for p in PRODUCTS:
    html = build(p)

    if DIFF_ONLY:
        live = fetch_live(p["id"])
        diff = list(difflib.unified_diff(norm(live), norm(html), "tienda", "repo", lineterm="", n=0))
        print(f"=== producto {p['id']} ({p['insp']}): {'sin cambios' if not diff else 'cambios'}")
        for ln in diff[2:]:
            print("   " + ln[:260])
        continue

    payload = {"description": {"es": html}}
    payload_path = f"{TMPDIR}/desc_payload_{p['id']}.json"
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload, f)

    result = subprocess.run(
        [
            "curl", "-sS", "-X", "PUT", URL_TMPL.format(p["id"]),
            "-H", f"User-Agent: {UA}",
            "-H", "Content-Type: application/json",
            "-d", f"@{payload_path}",
            "-w", "\\nHTTP_STATUS:%{http_code}\\n",
            "-o", "/dev/null",
        ],
        capture_output=True, text=True,
    )
    print(f"producto {p['id']} ({p['insp']}): {result.stdout.strip()} {result.stderr.strip()}")
    time.sleep(1)  # la API corta con 429 si se le pega muy seguido
