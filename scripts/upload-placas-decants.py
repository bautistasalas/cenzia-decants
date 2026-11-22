# -*- coding: utf-8 -*-
"""Sube las placas de los Decants Originales (placas/out/decant-*-final.png).

En cada decant la placa nueva ocupa el lugar de la vieja placa de "acordes
principales", que se borra de la tienda. Qué foto es la vieja en cada producto
está anotado en placas/acordes-respaldo.json, y su copia en
placas/respaldo-acordes/: sin esa copia no se borra nada.

Uso:
    python3 scripts/upload-placas-decants.py                       # muestra el plan, no cambia nada
    python3 scripts/upload-placas-decants.py --subir               # todos los de placas/decants.json
    python3 scripts/upload-placas-decants.py --subir 283341797     # solo ese producto
    python3 scripts/upload-placas-decants.py --restaurar 283341797 # vuelve a subir la placa de acordes guardada

Antes hay que generar las placas:  cd placas && node render.js --datos decants.json
Se puede correr más de una vez: una placa que ya está en la galería (se la
reconoce por el nombre placa-decant-{slug}) no se vuelve a subir, y la única
foto que se borra es la anotada en el respaldo.
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
PLACAS = os.path.join(ROOT, "placas")
BASE = "https://api.tiendanube.com/v1/6474513"
UA = "CenziaDecants (contactoandiva@gmail.com)"

with open(os.path.join(PLACAS, "decants.json"), encoding="utf-8") as f:
    CARDS = json.load(f)
with open(os.path.join(PLACAS, "acordes-respaldo.json"), encoding="utf-8") as f:
    OLD = {o["product_id"]: o for o in json.load(f)}


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


def gallery(pid):
    code, d = api("GET", f"/products/{pid}?fields=id,images")
    assert code == 200, f"no pude leer el producto {pid}: HTTP {code}"
    return sorted(d.get("images", []), key=lambda i: i.get("position", 0))


def short(img):
    return img["src"].split("/products/")[-1].split("-1024-1024")[0][:34]


def jpeg_b64(slug):
    path = os.path.join(PLACAS, "out", f"decant-{slug}-final.png")
    if not os.path.exists(path):
        sys.exit(f"falta {path}: correr primero  cd placas && node render.js {slug} final --datos decants.json")
    buf = io.BytesIO()
    Image.open(path).convert("RGB").save(buf, "JPEG", quality=92, subsampling=0)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def restaurar(pid):
    """Vuelve a subir, al final de la galería, la placa de acordes guardada de ese producto."""
    old = OLD[pid]
    path = os.path.join(PLACAS, old["archivo"])
    imgs = gallery(pid)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    code, d = api("POST", f"/products/{pid}/images",
                  {"attachment": b64, "filename": "acordes-" + os.path.basename(path), "position": len(imgs) + 1})
    print(f"{old['name']} ({pid}): placa de acordes restaurada -> HTTP {code}")
    return code in (200, 201)


def main():
    args = sys.argv[1:]
    only = {int(a) for a in args if a.isdigit()}
    if "--restaurar" in args:
        if not only:
            sys.exit("--restaurar necesita el ID de al menos un producto")
        sys.exit(0 if all(restaurar(pid) for pid in only) else 1)
    subir = "--subir" in args
    hechas = pendientes = sin_foto = 0
    for card in CARDS:
        pid, slug = card["product_id"], card["slug"]
        if only and pid not in only:
            continue
        if not card.get("scene"):  # todavía no tiene la foto generada: no hay placa que subir
            sin_foto += 1
            continue
        imgs = gallery(pid)
        tag = f"placa-decant-{slug}-"
        new = next((i for i in imgs if tag in i["src"]), None)
        old_info = OLD.get(pid)
        old = next((i for i in imgs if old_info and i["id"] == old_info["image_id"]), None)
        print(f"\n{card['name']} ({pid}): {len(imgs)} foto(s) -> " + ", ".join(short(i) for i in imgs))
        if new and not old:
            print("   ya está la placa nueva y la de acordes ya no está")
            continue
        pendientes += 1
        # la placa nueva queda donde estaba la de acordes (o al final, si no hay ninguna anotada)
        target = imgs.index(old) + 1 if old else len(imgs) + 1
        if old:
            backup = os.path.join(PLACAS, old_info["archivo"])
            if not os.path.exists(backup):
                sys.exit(f"   falta la copia {backup}: no borro nada")
        if not subir:
            print(f"   subiría   placa-decant-{slug}.jpg -> posición {target}"
                  + (f"   y borraría la de acordes ({short(old)}, copia en placas/{old_info['archivo']})" if old else "   (no hay placa de acordes anotada)"))
            continue
        if not new:
            code, d = api("POST", f"/products/{pid}/images",
                          {"attachment": jpeg_b64(slug), "filename": f"placa-decant-{slug}.jpg", "position": len(imgs) + 1})
            if code not in (200, 201):
                sys.exit(f"   ERROR al subir placa-decant-{slug}.jpg (HTTP {code}): {str(d)[:200]}")
            new = d
            print(f"   subida    placa-decant-{slug}.jpg  (foto {new['id']})")
            time.sleep(1)
        # la vieja se borra recién cuando la nueva ya está confirmada en la galería
        now = gallery(pid)
        assert any(i["id"] == new["id"] for i in now), "la placa nueva no aparece en la galería: no borro la de acordes"
        if old:
            code, d = api("DELETE", f"/products/{pid}/images/{old['id']}")
            if code not in (200, 204):
                sys.exit(f"   ERROR al borrar la de acordes {old['id']} (HTTP {code}): {str(d)[:200]}")
            print(f"   borrada   la de acordes (foto {old['id']})")
            time.sleep(1)
        now = gallery(pid)
        if [i["id"] for i in now].index(new["id"]) + 1 != target:
            code, d = api("PUT", f"/products/{pid}/images/{new['id']}", {"position": target})
            print(f"   movida a la posición {target} (HTTP {code})")
            time.sleep(1)
            now = gallery(pid)
        ok = [i["id"] for i in now].index(new["id"]) + 1 == target and not any(old and i["id"] == old["id"] for i in now)
        print(f"   {'OK' if ok else 'REVISAR'}: {len(now)} fotos -> " + ", ".join(short(i) for i in now))
        if not ok:
            sys.exit(1)
        hechas += 1
    print(f"\n{'Reemplazadas' if subir else 'Para reemplazar'}: {hechas if subir else pendientes} placa(s)."
          + (f"  Sin foto todavía: {sin_foto}." if sin_foto else "")
          + ("" if subir else "  Nada se cambió: agregar --subir."))


if __name__ == "__main__":
    main()
