# -*- coding: utf-8 -*-
import os

# "olfactory-notes.py" has a hyphen, so import it via exec instead of `import`.
_ns = {}
with open(os.path.join(os.path.dirname(__file__), "olfactory-notes.py"), "r", encoding="utf-8") as _f:
    exec(compile(_f.read(), "olfactory-notes.py", "exec"), _ns)
PRODUCTS = _ns["PRODUCTS"]

BY_ID = {p["id"]: p for p in PRODUCTS}

# display name/brand per fragrance id, matching store naming + combo collage text
DISPLAY = {
    378156477: ("Erba Pura", "Xerjoff"),
    378156482: ("Born In Roma Intense", "Valentino"),
    378156485: ("Le Male Elixir", "JPG"),
    378156488: ("Arabians Tonka", "Montale"),
    378156494: ("Sauvage", "Dior"),
    379371166: ("Stronger With You Intensely", "Emporio Armani"),
    379371172: ("Ombré Leather", "Tom Ford"),
}

def notes_for(pid):
    p = BY_ID[pid]
    salida = [n.strip() for n in p["salida"].split("·")]
    corazon = [n.strip() for n in p["corazon"].split("·")]
    return (salida + corazon)[:3]

COMBOS = [
    {
        "id": 379559574,
        "slug": "los-mas-buscados",
        "name": "Los Más Buscados",
        "price": 99900,
        "frags": [378156477, 379371166, 378156482, 378156488, 378156494],
    },
    {
        "id": 379559578,
        "slug": "caballero",
        "name": "Caballero",
        "price": 69900,
        "frags": [378156488, 379371166, 378156482],
    },
    {
        "id": 379559585,
        "slug": "seductor",
        "name": "Seductor",
        "price": 79900,
        "frags": [378156485, 378156477, 378156482, 379371166],
    },
    {
        "id": 379559587,
        "slug": "nocturno",
        "name": "Nocturno",
        "price": 79900,
        "frags": [378156485, 378156488, 378156482, 379371172],
    },
]
