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

# Precio = precio promocional cargado en la tienda (escalera 2026-11-16:
# 2→59.900, 3→84.900, 4→99.900, 5→114.900, 6→124.900). El tachado es
# cantidad × $35.000.
# Cada combo define sus tarjetas de una de dos formas:
#   "frags" → lista de IDs; la tarjeta se arma con DISPLAY + BLURB + pyramid_for.
#   "cards" → tarjetas escritas a mano (Ella, Icónico y Femme, que se crearon
#             con textos propios; se copiaron tal cual de la tienda).
COMBOS = [
    {
        "id": 379559574,
        "slug": "los-mas-buscados",
        "name": "Los Más Buscados",
        "price": 114900,
        "frags": [378156477, 379371166, 378156482, 378156488, 378156494],
    },
    {
        "id": 379559578,
        "slug": "caballero",
        "name": "Caballero",
        "price": 99900,
        "frags": [378156488, 379371166, 378156482, 378156485],
    },
    {
        "id": 379559585,
        "slug": "seductor",
        "name": "Seductor",
        "price": 99900,
        "frags": [378156485, 378156477, 378156482, 379371166],
    },
    {
        "id": 379559587,
        "slug": "nocturno",
        "name": "Nocturno",
        "price": 99900,
        "frags": [378156485, 378156488, 378156482, 379371172],
    },
    {
        "id": 379562938,
        "slug": "black",
        "name": "Black",
        "price": 124900,
        "frags": [378156485, 378156488, 379371172, 378156482, 379371166, 378156477],
    },
    {
        "id": 379562943,
        "slug": "intenso",
        "name": "Intenso",
        "price": 59900,
        "frags": [378156488, 378156482],
    },
    {
        "id": 379562948,
        "slug": "bestia",
        "name": "Bestia",
        "price": 84900,
        "frags": [378156485, 378156488, 378156477],
    },
    {
        "id": 380863710,
        "slug": "ella",
        "name": "Ella",
        "price": 84900,
        "cards": [
            {"brand": "Giorgio Armani", "name": "My Way", "blurb": "Nardo y azahar sobre una base cálida de cedro y vainilla — fresco al principio, envolvente con el correr de las horas.", "salida": "Bergamota, Flor de azahar", "corazon": "Nardo, Jazmín", "fondo": "Cedro, Vainilla"},
            {"brand": "Kenzo", "name": "Flower", "blurb": "Un floral clásico de rosa y violeta, dulce pero no empalagoso, con un fondo suave de vainilla e incienso.", "salida": "Rosa búlgara, Espino, Grosella negra, Mandarina", "corazon": "Violeta de Parma, Rosa, Opopónax, Jazmín", "fondo": "Almizcle blanco, Vainilla, Incienso"},
            {"brand": "Carolina Herrera", "name": "Good Girl", "blurb": "Floral dulce con un fondo gourmand de cacao y café. Femenino, reconocible, con mucha proyección.", "salida": "Almendra, Bergamota, Limón", "corazon": "Jazmín sambac, Tuberosa", "fondo": "Haba tonka, Cacao, Café, Vainilla"},
        ],
    },
    {
        "id": 380863743,
        "slug": "iconico",
        "name": "Icónico",
        "price": 99900,
        "cards": [
            {"brand": "Carolina Herrera", "name": "La Bomba", "blurb": "Fresco y jugoso de entrada, con un corazón floral tropical que se asienta en una base cálida de vainilla.", "salida": "Pitahaya (fruta del dragón)", "corazon": "Peonía cereza, Frangipani rojo", "fondo": "Vainilla, Pachulí"},
            {"brand": "Lattafa", "name": "Eclaire", "blurb": "Un gourmand goloso de caramelo y leche que se vuelve floral y envolvente en el fondo.", "salida": "Caramelo, Leche, Azúcar", "corazon": "Miel, Flores blancas", "fondo": "Almizcle, Praliné, Vainilla"},
            {"brand": "Emporio Armani", "name": "Power Of You", "blurb": "Maracuyá y frangipani sobre un fondo de vainilla y benjuí — una fragancia alegre pensada para el buen clima.", "salida": "Maracuyá, Naranja amarga, Limón", "corazon": "Frangipani, Notas solares", "fondo": "Vainilla de Madagascar, Benjuí, Labdanum"},
            {"brand": "Carolina Herrera", "name": "Good Girl", "blurb": "Floral dulce con un fondo gourmand de cacao y café. Femenino, reconocible, con mucha proyección.", "salida": "Almendra, Bergamota, Limón", "corazon": "Jazmín sambac, Tuberosa", "fondo": "Haba tonka, Cacao, Café, Vainilla"},
        ],
    },
    {
        "id": 380863745,
        "slug": "femme",
        "name": "Femme",
        "price": 114900,
        "cards": [
            {"brand": "Giorgio Armani", "name": "My Way", "blurb": "Nardo y azahar sobre una base cálida de cedro y vainilla — fresco al principio, envolvente con el correr de las horas.", "salida": "Bergamota, Flor de azahar", "corazon": "Nardo, Jazmín", "fondo": "Cedro, Vainilla"},
            {"brand": "Kenzo", "name": "Flower", "blurb": "Un floral clásico de rosa y violeta, dulce pero no empalagoso, con un fondo suave de vainilla e incienso.", "salida": "Rosa búlgara, Espino, Grosella negra, Mandarina", "corazon": "Violeta de Parma, Rosa, Opopónax, Jazmín", "fondo": "Almizcle blanco, Vainilla, Incienso"},
            {"brand": "Carolina Herrera", "name": "Good Girl", "blurb": "Floral dulce con un fondo gourmand de cacao y café. Femenino, reconocible, con mucha proyección.", "salida": "Almendra, Bergamota, Limón", "corazon": "Jazmín sambac, Tuberosa", "fondo": "Haba tonka, Cacao, Café, Vainilla"},
            {"brand": "Lancôme", "name": "La Vida Es Bella", "blurb": "Una nube dulce de praliné y vainilla, elevada por un iris floral brillante. Icónico y reconocible al instante.", "salida": "Grosella negra, Pera", "corazon": "Iris, Jazmín, Flor de azahar", "fondo": "Praliné, Vainilla, Pachulí, Haba tonka"},
            {"brand": "Carolina Herrera", "name": "La Bomba", "blurb": "Fresco y jugoso de entrada, con un corazón floral tropical que se asienta en una base cálida de vainilla.", "salida": "Pitahaya (fruta del dragón)", "corazon": "Peonía cereza, Frangipani rojo", "fondo": "Vainilla, Pachulí"},
        ],
    },
]
