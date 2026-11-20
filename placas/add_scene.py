# -*- coding: utf-8 -*-
"""Deja lista la foto de una placa: la recorta a 3:4, la guarda en scenes/ y la anota en placas.json.

Uso:  python3 placas/add_scene.py <slug> <foto>
Después:  cd placas && node render.js <slug> final
"""
import json
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
MIN_W, MIN_H = 900, 1200  # tamaño del recuadro de la foto dentro de la placa de 2000 px
MAX_H = 1600              # más alto que esto no suma nitidez en la placa y solo pesa en el repo


def to_3x4(im):
    """Recorte centrado a 3:4 (ancho:alto), sin deformar."""
    w, h = im.size
    if w * 4 > h * 3:  # sobra ancho
        nw = round(h * 3 / 4)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = round(w * 4 / 3)  # sobra alto
    y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def add(slug, photo, out_dir=None, json_path=None):
    out_dir = out_dir or os.path.join(HERE, "scenes")
    json_path = json_path or os.path.join(HERE, "placas.json")
    with open(json_path, encoding="utf-8") as f:
        cards = json.load(f)
    card = next((c for c in cards if c["slug"] == slug), None)
    assert card, f"no hay una placa con slug {slug!r}"

    im = to_3x4(Image.open(photo).convert("RGB"))
    if im.height > MAX_H:
        im = im.resize((round(im.width * MAX_H / im.height), MAX_H), Image.LANCZOS)
    if im.width < MIN_W or im.height < MIN_H:
        print(f"OJO: la foto quedó de {im.width}x{im.height}; en la placa se va a ver blanda (mínimo {MIN_W}x{MIN_H})")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"{slug}.jpg")
    im.save(out, quality=93, subsampling=0)

    card["scene"] = f"scenes/{slug}.jpg"
    with open(json_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(cards, ensure_ascii=False, indent=2))
    return out, im.size


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    print(*add(sys.argv[1], sys.argv[2]))
