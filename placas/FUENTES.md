# Placas de galería — de dónde sale cada imagen

- `src/{perfume}.webp`: frasco de marca recortado de la foto principal de ese
  producto en la tienda (`prep_assets.py`). Se usa como referencia para generar
  la foto.
- `scenes/{perfume}.jpg`: el perfume solo, rodeado de sus materias primas,
  sobre fondo blanco puro. Imagen generada con IA a partir del frasco de
  referencia. En la foto NO va el frasco Cenzia Privé (pedido de Bautista,
  2026-11-16).
- El texto de la placa nunca lo escribe la IA: lo pone `card.html` con los
  datos de `placas.json`. La prueba hecha en Runway con el texto adentro de la
  imagen salió con errores de tipeo en casi todos los renglones.
- Tres recortes de `src/` se hicieron a mano porque en la foto de la tienda el
  frasco de marca toca al de 60 ml y `prep_assets.py` no encuentra el hueco:
  Stronger With You Intensely, La Bomba y Althaïr.

## Fotos generadas en el Canva de Bautista (2026-11-20)

Las 23 fotos de `scenes/` se generaron en su Canva, una por perfume, con el
frasco de `src/` como única referencia y formato 3:4. Quedan guardadas ahí
(1088 x 1456 px); el identificador sirve para volver a encontrarlas.

Todas tienen fondo blanco puro, por el pedido de Bautista de ese día: "las
fotos tienen que estar en 1:1 y fondo full white". Las primeras 14 se habían
hecho con fondo gris claro y se rehicieron sobre blanco con su OK; las grises
quedaron en su Canva y en el historial de git, y la de Born In Roma Intense
que él había generado en Runway también se reemplazó.

| Perfume | Identificador en Canva |
|---|---|
| Born In Roma Intense | `MAHbeBwe2Ek` |
| Arabians Tonka | `MAHbeNozIqY` |
| Stronger With You Intensely | `MAHbeJHxAdE` |
| Erba Pura | `MAHbeNKmsqo` |
| Le Male Elixir | `MAHbeERMSik` |
| Sauvage Eau de Parfum | `MAHbeBgE9a4` |
| Ombré Leather | `MAHbeEKq8YY` |
| My Way | `MAHbeJHoKws` |
| Flower | `MAHbeCzyZUY` |
| Good Girl | `MAHbeJq7EaI` |
| La Vida Es Bella | `MAHbeJ6m0uY` |
| La Bomba | `MAHbeCsetxY` |
| Eclaire | `MAHbeEmBvwQ` |
| Power Of You | `MAHbeLMX1Vc` |
| Y | `MAHbd0xpMTU` |
| Donna Born In Roma Intense | `MAHbd6m6OHw` |
| Club de Nuit Intense Man | `MAHbd_sd96M` |
| Bharara King | `MAHbeGM2d9M` |
| Scandal Pour Homme | `MAHbd9te6hg` |
| Althaïr | `MAHbd-4Kyjs` |
| Tobacco Vanille | `MAHbd4BWinE` |
| Sauvage Elixir | `MAHbd9Ht6bo` |
| Bleu de Chanel | `MAHbdwJClls` |

Para bajarlas en tamaño completo no alcanza con el identificador (Canva solo
devuelve una miniatura de 149 x 200): hay que colocar cada foto en una página
de 1500 x 2000 de un diseño, guardar y exportar esas páginas como PNG. Se usa
el diseño de trabajo "Publicación cuadrada con foto a sangre" (`DAHbGZCniAo`).
Después, `add_scene.py --blanco` las deja en `scenes/` a 1200 x 1600, con el
fondo llevado a blanco puro y los bordes fundidos.

Cada llamada a Canva le pide permiso a Bautista en el celular. Lanzar más de
cuatro o cinco juntas terminó dos veces en un permiso rechazado sin querer o
en un corte de la sesión: conviene ir de a tandas chicas.

Texto que se usó para generarlas (las materias salen del campo `en` de cada
materia en `placas.json`):

```
Photorealistic studio product photograph, vertical 3:4. The perfume bottle
from the reference image, centered and upright, keeping its exact shape,
label, lettering, colors and proportions. Only this bottle, no other bottle.
Around its base, arranged naturally, some slightly behind and some in front:
{materias}. Pure white seamless background (#FFFFFF), evenly lit high-key
e-commerce packshot, soft diffused light from the upper left, only soft
contact shadows directly under the objects, no gradient, no vignette, no gray
backdrop, no visible horizon line. Only these ingredients, no other props. No
added text, no watermark.
```
