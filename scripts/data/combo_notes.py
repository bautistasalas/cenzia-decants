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
    379371171: ("Good Girl", "Carolina Herrera"),
    379371165: ("Donna Born In Roma Intense", "Valentino"),
}

# reseña breve en tono humano (mood/ocasión), no la "tag" técnica de olf_data
BLURB = {
    378156477: "Fresca y alegre, perfecta para el día a día y el buen clima.",
    378156482: "Amaderada con carácter, para quien quiere destacar sin esfuerzo.",
    378156485: "Intensa y seductora, ideal para la noche y salidas especiales.",
    378156488: "Oriental potente y magnética, para quien busca dejar huella.",
    378156494: "Fresca y versátil, el clásico infalible para cualquier ocasión.",
    379371166: "Cálida y seductora, especial para citas y noches de frío.",
    379371172: "Cuero floral elegante y distinto, para looks sofisticados.",
    379371171: "Dulce y gourmand, femenina y con muchísima proyección.",
    379371165: "Floral ambarado y sensual, ideal para la noche.",
}

def notes_for(pid):
    p = BY_ID[pid]
    salida = [n.strip() for n in p["salida"].split("·")]
    corazon = [n.strip() for n in p["corazon"].split("·")]
    return (salida + corazon)[:3]


def pyramid_for(pid):
    """Top 3 notes per pyramid tier (salida/corazón/fondo)."""
    p = BY_ID[pid]
    def top3(field):
        return ", ".join(n.strip() for n in p[field].split("·")[:3])
    return {
        "salida": top3("salida"),
        "corazon": top3("corazon"),
        "fondo": top3("fondo"),
    }

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
    {
        "id": 379562938,
        "slug": "black",
        "name": "Black",
        "price": 119900,
        "frags": [378156485, 378156488, 379371172, 378156482, 379371166, 378156477],
    },
    {
        "id": 379562941,
        "slug": "ella",
        "name": "Ella",
        "price": 69900,
        "frags": [379371171, 379371165, 378156477],
    },
    {
        "id": 379562943,
        "slug": "intenso",
        "name": "Intenso",
        "price": 69900,
        "frags": [378156485, 378156488, 378156482],
    },
    {
        "id": 379562948,
        "slug": "bestia",
        "name": "Bestia",
        "price": 69900,
        "frags": [378156485, 378156488, 378156477],
    },
]
