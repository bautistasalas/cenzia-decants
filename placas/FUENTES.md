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

- Dos recortes de `src/` se hicieron a mano porque en la foto de la tienda el
  frasco de marca toca al de 60 ml y `prep_assets.py` no encuentra el hueco:
  Stronger With You Intensely y La Bomba.

| Archivo | Origen |
|---|---|
| `scenes/born-in-roma-intense.jpg` | Recorte de la placa que Bautista generó en Runway (2026-11-20). Se usa solo la foto, sin el texto. |
| Las otras 21 de `scenes/` | Generadas en el Canva de Bautista (ver abajo). |

## Fotos generadas en el Canva de Bautista (2026-11-20)

Una por perfume, con el frasco de `src/` como única referencia, formato 3:4.
Quedan guardadas en su Canva (1088 x 1456 px); el identificador sirve para
volver a encontrarlas. Las 21 ya están en `scenes/`.

Hay dos tandas con fondo distinto:

- Las 13 primeras (combos de hombre y de mujer) tienen fondo gris claro, como
  la de Born In Roma Intense.
- Las 8 del 2026-11-20 a la tarde (individuales) tienen fondo blanco puro, por
  el pedido de Bautista de ese día: "las fotos tienen que estar en 1:1 y fondo
  full white". Se sumaron con `add_scene.py --blanco`.
- Falta Bharara King: tiene el texto y el frasco recortado, pero el permiso
  para subir su frasco al Canva quedó rechazado y no se generó la foto.

Para bajarlas en tamaño completo no alcanza con el identificador (Canva solo
devuelve una miniatura de 149 x 200): hay que colocar cada foto en una página
de 1500 x 2000 de un diseño, guardar y exportar esas páginas como PNG. Se usa
el diseño de trabajo "Publicación cuadrada con foto a sangre" (`DAHbGZCniAo`).
Después, `add_scene.py` las deja en `scenes/` a 1200 x 1600.

| Perfume | Identificador en Canva |
|---|---|
| Arabians Tonka | `MAHbdtaagtY` |
| Stronger With You Intensely | `MAHbdvIOjvI` |
| Erba Pura | `MAHbdsDZmzw` |
| Le Male Elixir | `MAHbdk-rq3I` |
| Sauvage Eau de Parfum | `MAHbdlkQe8E` |
| Ombré Leather | `MAHbdhsKiYU` |
| My Way | `MAHbdowvm-g` |
| Flower | `MAHbdt540Rs` |
| Good Girl | `MAHbdiF9Idw` |
| La Vida Es Bella | `MAHbdsqBv2U` |
| La Bomba | `MAHbdrL_gFE` |
| Eclaire | `MAHbdjsl3LU` |
| Power Of You | `MAHbdhlwaR8` |
| Y | `MAHbd0xpMTU` |
| Donna Born In Roma Intense | `MAHbd6m6OHw` |
| Club de Nuit Intense Man | `MAHbd_sd96M` |
| Scandal Pour Homme | `MAHbd9te6hg` |
| Althaïr | `MAHbd-4Kyjs` |
| Tobacco Vanille | `MAHbd4BWinE` |
| Sauvage Elixir | `MAHbd9Ht6bo` |
| Bleu de Chanel | `MAHbdwJClls` |

Texto que se usó para generar las de fondo gris (las materias salen del campo
`en` de cada materia en `placas.json`):

```
Photorealistic studio product photograph, vertical 3:4. The perfume bottle
from the reference image, centered and upright, keeping its exact shape,
label, lettering, colors and proportions. Only this bottle, no other bottle.
Around its base, arranged naturally, some slightly behind and some in front:
{materias}. Light gray seamless studio background, soft diffused light from
the upper left, soft contact shadows and a faint reflection on the surface.
Only these ingredients, no other props. No added text, no watermark.
```

Para las de fondo blanco cambia solo la frase del fondo y la luz:

```
Pure white seamless background (#FFFFFF), evenly lit high-key e-commerce
packshot, soft diffused light from the upper left, only soft contact shadows
directly under the objects, no gradient, no vignette, no gray backdrop, no
visible horizon line.
```
