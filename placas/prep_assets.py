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


def components(mask):
    """Manchas conectadas (8 vecinos) de una máscara chica. Devuelve la matriz de etiquetas y cuántas hay."""
    h, w = mask.shape
    lab = np.zeros((h, w), np.int32)
    n = 0
    for sy, sx in zip(*np.nonzero(mask)):
        if lab[sy, sx]:
            continue
        n += 1
        lab[sy, sx] = n
        stack = [(sy, sx)]
        while stack:
            y, x = stack.pop()
            for yy in range(max(0, y - 1), min(h, y + 2)):
                for xx in range(max(0, x - 1), min(w, x + 2)):
                    if mask[yy, xx] and not lab[yy, xx]:
                        lab[yy, xx] = n
                        stack.append((yy, xx))
    return lab, n


def brand_bottle_decant(path, out):
    """Foto principal de un Decant Original: el decant (con su cartel "Decant 5ML") va a la izquierda y el frasco
    de marca a la derecha. Se queda con la mancha más grande de la mitad derecha y borra todo lo demás."""
    im, bg = white_level(Image.open(path))
    a = np.asarray(im).astype(np.int32)
    H, W = a.shape[:2]
    content = (a.min(axis=2) < 238) | ((a.max(axis=2) - a.min(axis=2)) > 22)
    k = max(1, W // 270)                      # celda de ~4 px
    h, w = H // k, W // k
    small = content[: h * k, : w * k].reshape(h, k, w, k).any(axis=(1, 3))
    grown = small.copy()                      # se engorda dos celdas para unir tapa, vidrio claro y reflejos del mismo frasco
    for _ in range(2):
        g = grown.copy()
        g[1:] |= grown[:-1]; g[:-1] |= grown[1:]; g[:, 1:] |= grown[:, :-1]; g[:, :-1] |= grown[:, 1:]
        grown = g
    lab, n = components(grown)
    best, area = 0, 0
    for i in range(1, n + 1):
        ys, xs = np.nonzero((lab == i) & small)
        if len(xs) > area and xs.mean() > w * 0.42:
            best, area = i, len(xs)
    assert best, "no encontré el frasco de marca a la derecha"
    keep = lab == best
    ys, xs = np.nonzero(keep & small)
    pad = int(W * 0.02)
    box = (max(0, xs.min() * k - pad), max(0, ys.min() * k - pad), min(W, (xs.max() + 1) * k + pad), min(H, (ys.max() + 1) * k + pad))
    # lo que no es el frasco (el decant, su cartel) queda en blanco aunque caiga dentro del recorte
    full = np.kron(keep, np.ones((k, k), bool))
    full = np.pad(full, ((0, H - full.shape[0]), (0, W - full.shape[1])))
    c = np.where(full[..., None], a, 255)[box[1]:box[3], box[0]:box[2]].astype(np.float32)
    # la sombra del piso se desvanece hacia abajo para que no quede un corte recto
    hh = c.shape[0]
    nfade = int(hh * 0.06)
    ramp = np.linspace(1.0, 0.0, nfade)[:, None, None]
    c[hh - nfade:] = 255.0 - (255.0 - c[hh - nfade:]) * ramp
    Image.fromarray(np.clip(c, 0, 255).astype(np.uint8)).save(out)
    return box, bg


if __name__ == "__main__":
    # Uso: python3 prep_assets.py <foto principal del producto> <salida.webp> [--decant]
    #   recorta el frasco de marca de la foto de la tienda y deja el fondo en blanco puro.
    #   --decant: foto de un Decant Original (el frasco de marca está a la derecha del decant).
    args = [x for x in sys.argv[1:] if x != "--decant"]
    src, out = args[0], args[1]
    tmp = out + ".png"
    fn = brand_bottle_decant if "--decant" in sys.argv else brand_bottle
    print("recorte:", fn(src, tmp))
    Image.open(tmp).convert("RGB").save(out, quality=95, method=6)
    import os
    os.remove(tmp)
