# -*- coding: utf-8 -*-
"""Recorta el frasco de marca de la foto principal de un producto, sobre blanco puro.
Ese recorte es la referencia que se le pasa al generador de imágenes para armar la escena de cada placa."""
import sys
import numpy as np
from PIL import Image


def white_level(im):
    """Lleva el fondo casi-blanco a blanco puro (niveles), sin tocar los tonos medios más de lo necesario."""
    a = np.asarray(im.convert("RGB")).astype(np.float32)
    # el fondo se estima con las esquinas
    k = 40
    corners = np.concatenate([a[:k, :k].reshape(-1, 3), a[:k, -k:].reshape(-1, 3), a[-k:, :k].reshape(-1, 3), a[-k:, -k:].reshape(-1, 3)])
    bg = np.percentile(corners, 20, axis=0)          # un poco por debajo de la mediana para limpiar el velo
    bg = np.minimum(bg, 252.0)
    out = np.clip(a * (255.0 / bg), 0, 255)
    return Image.fromarray(out.astype(np.uint8)), bg


def brand_bottle(path, out):
    """Recorta el frasco de marca (la mancha grande de la izquierda) de la foto principal del producto."""
    im, bg = white_level(Image.open(path))
    a = np.asarray(im.convert("L")).astype(np.int32)
    H, W = a.shape
    dark = a < 225
    # para separar los dos frascos se mira solo la parte alta (sin el reflejo del piso) y lo bien oscuro/saturado
    upper = (a[: int(H * 0.80)] < 200)
    cols = upper.sum(axis=0)
    filled = cols > 3
    xs = np.where(filled)[0]
    x0 = xs.min()
    gap_start, best = None, (0, 0, 0)
    for x in range(int(W * 0.30), int(W * 0.80)):
        if not filled[x]:
            if gap_start is None:
                gap_start = x
        else:
            if gap_start is not None:
                if x - gap_start > best[0]:
                    best = (x - gap_start, gap_start, x)
                gap_start = None
    assert best[0] > 0, "no encontré el hueco entre frascos"
    x1 = (best[1] + best[2]) // 2
    rows = np.where(dark[:, x0:x1].sum(axis=1) > 2)[0]
    y0, y1 = rows.min(), rows.max()
    pad = int(W * 0.02)
    box = (max(0, x0 - pad), max(0, y0 - pad), min(W, x1), min(a.shape[0], y1 + pad))
    crop = im.crop(box)
    # el reflejo del piso se desvanece hacia abajo para que no quede un corte recto
    c = np.asarray(crop).astype(np.float32)
    h = c.shape[0]
    n = int(h * 0.07)
    ramp = np.linspace(1.0, 0.0, n)[:, None, None]
    c[h - n:] = 255.0 - (255.0 - c[h - n:]) * ramp
    Image.fromarray(np.clip(c, 0, 255).astype(np.uint8)).save(out)
    return box, bg


if __name__ == "__main__":
    # Uso: python3 prep_assets.py <foto principal del producto> <salida.webp>
    #   recorta el frasco de marca de la foto de la tienda y deja el fondo en blanco puro.
    src, out = sys.argv[1], sys.argv[2]
    tmp = out + ".png"
    print("recorte:", brand_bottle(src, tmp))
    Image.open(tmp).convert("RGB").save(out, quality=95, method=6)
    import os
    os.remove(tmp)
