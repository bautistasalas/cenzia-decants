# -*- coding: utf-8 -*-
import json
import subprocess
import sys
sys.path.insert(0, "/tmp/claude-0/-home-user-cenzia-decants/0616b845-8e51-5a26-8e41-a7b1e3748bb2/scratchpad")
from olf_data import PRODUCTS

BASE_FILE = "/home/user/cenzia-decants/product-descriptions/extractos.html"
TMPDIR = "/tmp/claude-0/-home-user-cenzia-decants/0616b845-8e51-5a26-8e41-a7b1e3748bb2/scratchpad"

with open(BASE_FILE, "r", encoding="utf-8") as f:
    base = f.read()

UA = "CenziaDecants (contactoandiva@gmail.com)"
URL_TMPL = "https://api.tiendanube.com/v1/6474513/products/{}"

for p in PRODUCTS:
    html = base
    html = html.replace("{{OLF_TAG}}", p["tag"])
    html = html.replace("{{OLF_SALIDA}}", p["salida"])
    html = html.replace("{{OLF_CORAZON}}", p["corazon"])
    html = html.replace("{{OLF_FONDO}}", p["fondo"])
    html = html.replace("{{OLF_DESC}}", p["desc"])
    html = html.replace("{{OLF_GENERO}}", p["genero"])
    html = html.replace("{{OLF_FAMILIA}}", p["familia"])
    html = html.replace("{{OLF_IDEAL}}", p["ideal"])
    html = html.replace("{{OLF_INTENSIDAD}}", p["intensidad"])

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
    print(f"producto {p['id']}: {result.stdout.strip()} {result.stderr.strip()}")
