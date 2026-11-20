# Placas de galería — de dónde sale cada imagen

- `src/{perfume}.webp`: frasco de marca recortado de la foto principal de ese
  producto en la tienda (`prep_assets.py`). Se usa como referencia para generar
  la escena.
- `scenes/{perfume}.jpg`: el perfume solo, rodeado de sus materias primas.
  Imagen generada con IA a partir del frasco de referencia. En la foto NO va
  el frasco Cenzia Privé (pedido de Bautista, 2026-11-16).
- El texto de la placa nunca lo escribe la IA: lo pone `card.html` con los
  datos de `placas.json`. La prueba hecha en Runway con el texto adentro de la
  imagen salió con errores de tipeo en casi todos los renglones.

| Archivo | Origen |
|---|---|
| `scenes/born-in-roma-intense.jpg` | Recorte de la placa que Bautista generó en Runway (2026-11-20). Se usa solo la foto, sin el texto. |

## Fotos generadas en el Canva de Bautista (2026-11-20)

Una por perfume, con el frasco de `src/` como única referencia, formato 3:4.
Quedan guardadas en su Canva (1088 x 1456 px); el identificador sirve para
volver a encontrarlas. Todavía no están en `scenes/`: falta bajarlas en tamaño
completo, y hasta entonces esas seis placas no tienen foto.

| Perfume | Identificador en Canva |
|---|---|
| Arabians Tonka | `MAHbdtaagtY` |
| Stronger With You Intensely | `MAHbdvIOjvI` |
| Erba Pura | `MAHbdsDZmzw` |
| Le Male Elixir | `MAHbdk-rq3I` |
| Sauvage Eau de Parfum | `MAHbdlkQe8E` |
| Ombré Leather | `MAHbdhsKiYU` |

Texto que se usó para generarlas (las materias salen del campo `en` de cada
materia en `placas.json`):

```
Photorealistic studio product photograph, vertical 3:4. The perfume bottle
from the reference image, centered and upright, keeping its exact shape,
label, lettering, colors and proportions. Only this bottle, no other bottle.
Around its base, arranged naturally, some slightly behind and some in front:
{materias}. Light gray seamless studio background, soft diffused light from
the upper left, soft contact shadows and a faint reflection on the surface.
Only these ingredients, no other props. No added text, no watermark.
```
