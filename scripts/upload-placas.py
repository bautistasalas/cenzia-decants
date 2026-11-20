# -*- coding: utf-8 -*-
"""Sube las placas de galería (placas/out/*-final.png) a la tienda.

- Cada combo Cenzia Privé recibe, después de las fotos que ya tiene, la placa
  de cada perfume que trae, en el mismo orden que su descripción
  (scripts/data/combo_notes.py).
- Cada Esencia Privé individual recibe su propia placa como foto siguiente.

Uso:
    python3 scripts/upload-placas.py                    # muestra el plan, no sube nada
    python3 scripts/upload-placas.py --subir            # sube lo que falta (combos e individuales)
    python3 scripts/upload-placas.py --subir 379562943  # solo ese producto
    python3 scripts/upload-placas.py --solo-combos      # deja afuera las individuales (o --solo-individuales)

Antes hay que generar las placas:  cd placas && node render.js
Se puede correr más de una vez: una placa que ya está en la galería (se la
reconoce por el nombre de archivo placa-{slug}) no se vuelve a subir.
"""
import base64
import io
import json
import os
import subprocess
import sys
import time

from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "scripts", "data"))
from combo_notes import COMBOS  # noqa: E402

BASE = "https://api.tiendanube.com/v1/6474513"
UA = "CenziaDecants (contactoandiva@gmail.com)"
OUT = os.path.join(ROOT, "placas", "out")

with open(os.path.join(ROOT, "placas", "placas.json"), encoding="utf-8") as f:
    CARDS = json.load(f)
BY_ID = {c["product_id"]: c for c in CARDS}
BY_NAME = {c["name"]: c for c in CARDS}


def api(method, path, body=None, _try=0):
    cmd = ["curl", "-sS", "-m", "120", "-X", method, BASE + path, "-H", f"User-Agent: {UA}",
           "-H", "Content-Type: application/json", "-w", "\n__HTTP__%{http_code}"]
    if body is not None:
        cmd += ["--data-binary", "@-"]
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None, capture_output=True, text=True)
    out, _, code = r.stdout.rpartition("\n__HTTP__")
    code = int(code.strip() or 0)
    if code == 429 and _try < 6:  # la API corta después de unas 25 escrituras seguidas
        time.sleep(4 * (_try + 1))
        return api(method, path, body, _try + 1)
    try:
        return code, json.loads(out) if out.strip() else None
    except ValueError:
        return code, out


def cards_of(combo):
    """Placas del combo, en el orden de su descripción."""
    if "frags" in combo:
        return [BY_ID[fid] for fid in combo["frags"]]
    return [BY_NAME[c["name"]] for c in combo["cards"]]


def gallery(pid):
    code, d = api("GET", f"/products/{pid}?fields=id,images")
    assert code == 200, f"no pude leer el producto {pid}: HTTP {code}"
    return sorted(d.get("images", []), key=lambda i: i.get("position", 0))


def jpeg_b64(slug):
    path = os.path.join(OUT, f"{slug}-final.png")
    if not os.path.exists(path):
        sys.exit(f"falta {path}: correr primero  cd placas && node render.js")
    buf = io.BytesIO()
    Image.open(path).convert("RGB").save(buf, "JPEG", quality=92, subsampling=0)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def main():
    args = sys.argv[1:]
    subir = "--subir" in args
    only = {int(a) for a in args if a.isdigit()}
    # (producto, nombre para mostrar, placas que le tocan)
    targets = []
    if "--solo-individuales" not in args:
        targets += [(c["id"], "Combo " + c["name"], cards_of(c)) for c in COMBOS]
    if "--solo-combos" not in args:
        targets += [(c["product_id"], c["name"], [c]) for c in CARDS]
    total = 0
    for pid, label, cards in targets:
        if only and pid not in only:
            continue
        imgs = gallery(pid)
        pos = max([i.get("position", 0) for i in imgs] or [0])
        print(f"\n{label} ({pid}): {len(imgs)} foto(s) hoy")
        for card in cards:
            slug = card["slug"]
            if any(f"placa-{slug}-" in i["src"] for i in imgs):
                print(f"   ya está   placa-{slug}")
                continue
            pos += 1
            total += 1
            if not subir:
                print(f"   subiría   placa-{slug}.jpg  -> posición {pos}")
                continue
            code, d = api("POST", f"/products/{pid}/images",
                          {"attachment": jpeg_b64(slug), "filename": f"placa-{slug}.jpg", "position": pos})
            ok = code in (200, 201)
            print(f"   {'subida   ' if ok else 'ERROR    '} placa-{slug}.jpg  -> posición {pos}  (HTTP {code})"
                  + ("" if ok else f"  {str(d)[:200]}"))
            if not ok:
                sys.exit(1)
            time.sleep(1)
        if subir:
            final = gallery(pid)
            print(f"   galería ahora: {len(final)} fotos -> " + ", ".join(
                i["src"].split("/products/")[-1].split("-1024-1024")[0][:38] for i in final))
    print(f"\n{'Subidas' if subir else 'Para subir'}: {total} placa(s)." + ("" if subir else "  Nada se subió: agregar --subir."))


if __name__ == "__main__":
    main()
