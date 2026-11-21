# -*- coding: utf-8 -*-
"""Deja lista la foto de una placa: la recorta a 3:4, la guarda en scenes/ y la anota en placas.json.

Uso:  python3 placas/add_scene.py <slug> <foto> [--blanco] [--datos decants.json]
Después:  cd placas && node render.js <slug> final [--datos decants.json]

--datos decants.json: la placa es de la línea Decants Originales (se anota en placas/decants.json).

--blanco: la foto viene sobre fondo blanco (pedido de Bautista, 2026-11-20: "1:1 y fondo full
white"). Lleva el fondo a blanco puro, funde los bordes y anota scene_bg "white" para que en la
placa la foto no tenga recuadro.
"""
import json
import os
import sys

import numpy as np
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


def to_white(im):
    """Fondo casi blanco -> blanco puro; los bordes se funden a blanco para que la foto no deje marco."""
    a = np.asarray(im).astype(np.float32)
    h, w = a.shape[:2]
    k = max(8, w // 40)
    border = np.concatenate([a[:k].reshape(-1, 3), a[-k:].reshape(-1, 3), a[:, :k].reshape(-1, 3), a[:, -k:].reshape(-1, 3)])
    bg = np.median(border, axis=0)
    assert bg.min() >= 235, f"el fondo de esta foto no es blanco (borde {bg.astype(int)})"
    a = np.clip(a * (255.0 / (bg - 3.0)), 0, 255)  # un pelo de más para que el "casi blanco" también llegue a 255
    # una materia que toca el borde quedaría cortada en seco: se desvanece hacia el blanco
    n = max(8, w // 28)
    lin = np.linspace(0.0, 1.0, n, dtype=np.float32)
    ramp = np.ones((h, w), np.float32)
    ramp[:n] *= lin[:, None]
    ramp[-n:] *= lin[::-1][:, None]
    ramp[:, :n] *= lin[None, :]
    ramp[:, -n:] *= lin[::-1][None, :]
    a = 255.0 - (255.0 - a) * ramp[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))


def add(slug, photo, white=False, out_dir=None, json_path=None):
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
    if white:
        im = to_white(im)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"{slug}.jpg")
    im.save(out, quality=93, subsampling=0)

    card["scene"] = f"scenes/{slug}.jpg"
    if white:
        card["scene_bg"] = "white"
    else:
        card.pop("scene_bg", None)
    with open(json_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(cards, ensure_ascii=False, indent=2))
    return out, im.size


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--blanco"]
    datos = None
    if "--datos" in args:
        i = args.index("--datos")
        datos = os.path.join(HERE, os.path.basename(args[i + 1]))
        del args[i:i + 2]
    if len(args) != 2:
        sys.exit(__doc__)
    print(*add(args[0], args[1], white="--blanco" in sys.argv, json_path=datos))
