# -*- coding: utf-8 -*-
"""Arma la foto de grupo del banner de Cenzia Privé: nuestro envase adelante y tres perfumes de diseñador.

    python3 grupo.py                      -> ../assets/prive-grupo.png  (lo que usa banner.html)
    python3 grupo.py envase <foto-combo>  -> ../assets/envase-prive.png (solo si hay que rehacer el recorte)

Nuestro envase es el de las fotos de los combos Cenzia Privé (vidrio con el isotipo). Se recortó de la foto
principal del Combo Intenso, que es donde menos lo tapan los otros frascos:
  https://acdn-us.mitiendanube.com/stores/006/474/513/products/combo-intenso-cenzia-prive-79611a635c2d7192ed17948061107258.webp
Los frascos de marca salen de placas/src/ (los mismos recortes de las placas).

Cada frasco viene sobre blanco con su reflejo en el piso. El cuerpo queda opaco y la sombra de apoyo y el
reflejo pasan a ser una veladura (alfa según lo oscuro), así se pueden apoyar sobre blanco o sobre otro frasco.
"""
import os
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
SRC = os.path.join(HERE, '..', '..', 'placas', 'src')


def _fondo(white):
    """Blanco conectado con el borde (se agrega un marco blanco de 1 px y se inunda desde la esquina)."""
    H, W = white.shape
    m = np.zeros((H + 2, W + 2), np.uint8)
    m[1:-1, 1:-1] = np.where(white, 255, 0)
    m[0, :] = m[-1, :] = 255
    m[:, 0] = m[:, -1] = 255
    pm = Image.fromarray(m, 'L').copy()        # sin .copy() la imagen es de solo lectura y no se inunda
    ImageDraw.floodfill(pm, (0, 0), 128, thresh=0)
    return np.asarray(pm)[1:-1, 1:-1] == 128


def _veladura(a, veil):
    """Color que, puesto con ese alfa sobre blanco, reproduce el gris original."""
    v = veil[..., None]
    return np.clip(np.where(v > 0.02, (a - 255.0 * (1 - v)) / np.maximum(v, 0.02), a), 0, 255)


def recortar(im, base_y, thr=247, thr_base=236, banda=70):
    """Frasco de marca sobre blanco -> RGBA. base_y: fila donde termina el frasco y empieza el reflejo."""
    a = np.asarray(im.convert('RGB')).astype(np.float32)
    H, W = a.shape[:2]
    mn = a.min(axis=2)
    y0 = int(base_y)
    body = ~_fondo(mn >= thr)
    yb = max(0, y0 - banda)                       # cerca de la base el umbral baja: la sombra de apoyo no es cuerpo
    body[yb:] = (~_fondo(mn >= thr_base))[yb:]
    body[y0:] = False
    alpha = np.asarray(Image.fromarray((body * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.9))).astype(np.float32) / 255.0
    alpha = np.clip((alpha - 0.35) / 0.5, 0, 1)   # un pelo hacia adentro: sin halo blanco
    alpha[y0:] = 0
    dark = np.clip((253.0 - a.mean(axis=2)) / 253.0, 0, 1)
    ramp = np.ones(H, np.float32)
    ramp[y0:] = np.clip(1.0 - np.arange(H - y0) / float(H - y0), 0, 1)
    ramp[:yb] = 0
    edge = np.minimum(np.arange(W), np.arange(W)[::-1]).astype(np.float32)
    veil = dark * ramp[:, None] * np.clip(edge / 24.0, 0, 1)[None, :]
    tot = alpha + veil * (1 - alpha)
    out = np.zeros((H, W, 4), np.float32)
    out[..., :3] = np.where(tot[..., None] > 1e-4,
                            (a * alpha[..., None] + _veladura(a, veil) * (veil * (1 - alpha))[..., None]) / np.maximum(tot[..., None], 1e-4), a)
    out[..., 3] = tot * 255.0
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), 'RGBA')


# ---- nuestro envase, desde la foto del Combo Intenso (coordenadas de esa foto, 2000 x 2000) ----
X0, Y0, X1, Y1 = 330, 1090, 990, 1960
# arriba y a la derecha de esta línea ya es el frasco de Montale, el de Valentino o el texto: afuera
CORTE = [(742, 1090), (990, 1090), (990, 1960), (935.5, 1960), (935.5, 1326), (934.5, 1319), (931, 1312.5), (925, 1308),
         (900, 1301.5), (860, 1292), (830, 1285), (800, 1278.5), (780, 1278), (760, 1279.5), (742, 1281)]
# por debajo de esta línea ya es reflejo en el piso
BASE = [(330, 1806), (385, 1828), (870, 1770), (934, 1752), (990, 1740)]


def envase(src, dst):
    im = Image.open(src).convert('RGB').crop((X0, Y0, X1, Y1))
    a = np.asarray(im).astype(np.float32)
    H, W = a.shape[:2]
    body = ~_fondo(a.min(axis=2) >= 249)
    ss = 4

    def poli(pts):
        m = Image.new('L', (W * ss, H * ss), 0)
        ImageDraw.Draw(m).polygon([((x - X0) * ss, (y - Y0) * ss) for x, y in pts], fill=255)
        return np.asarray(m.resize((W, H), Image.LANCZOS)).astype(np.float32) / 255.0

    cut = poli(CORTE)
    below = poli(BASE + [(X1, Y1), (X0, Y1)])
    alpha = np.asarray(Image.fromarray((body * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32) / 255.0
    alpha = np.clip((alpha - 0.3) / 0.5, 0, 1) * (1 - cut)
    dark = np.clip((253.0 - a.mean(axis=2)) / 253.0, 0, 1)
    yy = np.arange(H, dtype=np.float32)[:, None] + Y0
    xs = np.arange(W, dtype=np.float32) + X0
    basey = np.interp(xs, [p[0] for p in BASE], [p[1] for p in BASE])[None, :]
    refl = dark * np.clip(1.0 - (yy - basey) / 125.0, 0, 1) * (1 - cut)
    b3 = below[..., None]
    out = np.zeros((H, W, 4), np.float32)
    out[..., :3] = a * (1 - b3) + _veladura(a, refl) * b3
    out[..., 3] = (alpha * (1 - below) + refl * below) * 255.0
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), 'RGBA').save(dst, optimize=True)
    print('ok', dst)


# ---- la foto de grupo. Medidas en píxeles del recorte del envase (escala 1) ----
EX, EY = 30, 400             # dónde va el envase
YB = EY + 352                # piso de la fila de atrás (igual que el frasco de atrás en la foto del combo)
YF = EY + 640                # piso del frasco de adelante a la derecha
W, H = 1520, 1295
# (archivo en placas/src, fila de la base, borde izquierdo del frasco, escala, x destino, piso). De atrás para adelante.
FRASCOS = [
    ('stronger-with-you-intensely', 1544, 47, 0.399, EX + 828, YB),
    ('sauvage-eau-de-parfum', 1566, 41, 0.464, EX + 545, YB),
    ('born-in-roma-intense', 1599, 40, 0.4227, EX + 1090, YF),
]


def grupo(dst):
    c = Image.new('RGBA', (W, H), (255, 255, 255, 0))
    for name, base_y, left, scale, x_dst, piso in FRASCOS:
        im = recortar(Image.open(os.path.join(SRC, name + '.webp')), base_y)
        im = im.resize((round(im.size[0] * scale), round(im.size[1] * scale)), Image.LANCZOS)
        c.alpha_composite(im, (round(x_dst - left * scale), round(piso - base_y * scale)))
    c.alpha_composite(Image.open(os.path.join(ASSETS, 'envase-prive.png')), (EX, EY))
    bg = Image.new('RGBA', (W, H), (255, 255, 255, 255))
    bg.alpha_composite(c)
    bg.convert('RGB').save(dst, optimize=True)
    print('ok', dst, (W, H))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'envase':
        envase(sys.argv[2], os.path.join(ASSETS, 'envase-prive.png'))
    else:
        grupo(os.path.join(ASSETS, 'prive-grupo.png'))
