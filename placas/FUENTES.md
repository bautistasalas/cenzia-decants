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

## Fotos de los Decants Originales (2026-11-21 a 23)

Los 66 decants en stock llevan la misma placa (`decants.json`, variante
`linea: "decant"` de `card.html`). 13 reusan la foto de su Esencia Privé (es el
mismo perfume de marca); para los otros 53 se generó una foto nueva en el Canva
de Bautista con el mismo texto de más abajo, tomando como referencia el frasco
recortado de la foto del decant en la tienda (`prep_assets.py --decant`; el de
Chocolate Dubai se recortó a mano).

Las notas de estas 53 placas no salen de la descripción del producto sino de
la pirámide publicada por la marca o por Fragrantica/Parfumo, porque varias
descripciones de decants tienen notas que no son de ese perfume.

| Perfume | Identificador en Canva | Estado |
|---|---|---|
| Costa Azzurra Parfum | `MAHbp5HyXRo` | en `scenes/` |
| 9AM Dive | `MAHbgGuvbNE` | en `scenes/` |
| 9PM | `MAHbp0TFlFU` | en `scenes/` |
| 9PM Rebel | `MAHbp9JUGMg` | en `scenes/` |
| Acqua di Giò Profondo Parfum | `MAHbp1Yur4Y` | en `scenes/` |
| Acqua di Giò Parfum | `MAHbp1Vnx6Y` | en `scenes/` |
| Amber Oud Dubai Night | `MAHbp60XwsY` | en `scenes/` |
| Amber Oud Aqua Dubai | `MAHbpybw2sc` | en `scenes/` |
| Armani Code | `MAHbp_Re5pA` | en `scenes/` |
| Man In Black | `MAHbpx7oG-o` | en `scenes/` |
| Odyssey Dubai Chocolat | `MAHbp2W6tdg` | en `scenes/` |
| Divine Le Parfum | `MAHbp3jqSIA` | en `scenes/` |
| Dylan Blue | `MAHbp5FFZYY` | en `scenes/` |
| Eros Eau de Parfum | `MAHbgDY9cQE` | en `scenes/` |
| Eros Eau de Toilette | `MAHbp3fFs8k` | en `scenes/` |
| Fakhar Black | `MAHbp4ptzMo` | en `scenes/` |
| Fakhar Rose | `MAHbp7qMF34` | en `scenes/` |
| Fame | `MAHbp-2GEXg` | en `scenes/` |
| Good Girl Blush | `MAHbpz0y8Zc` | falta bajarla |
| Hawas Ice | `MAHbh7PL-HI` | en `scenes/` |
| Hawas Malibu | `MAHbp619XsI` | falta bajarla |
| Hawas | `MAHbhwVYYPE` | en `scenes/` |
| Hawas Tropical | `MAHbp3pMgSQ` | falta bajarla |
| His Confession | `MAHbp07S_Ao` | falta bajarla |
| Honor & Glory | `MAHbh7S95Ww` | en `scenes/` |
| Intense Café | `MAHbqEB4FAI` | falta bajarla |
| Jean Lowe Immortel | `MAHbqIkYyfY` | falta bajarla |
| Khamrah | `MAHbqNXTLjE` | falta bajarla |
| Khamrah Qahwa | `MAHbqOk2FwI` | falta bajarla |
| Layton | `MAHbgL_PnlY` | en `scenes/` |
| Le Beau Le Parfum | `MAHbh0tvtMk` | en `scenes/` |
| Le Male Elixir Absolu | `MAHbqLREgzs` | falta bajarla |
| Libre | `MAHbqMAcPxk` | falta bajarla |
| Liquid Brun | `MAHbqCwhXjA` | falta bajarla |
| Odyssey Mandarin Sky | `MAHbqNUSfgE` | falta bajarla |
| MYSLF | `MAHbqChb8DU` | falta bajarla |
| Naxos | `MAHbgLrG08g` | en `scenes/` |
| Odyssey Aqua | `MAHbqKqSLME` | falta bajarla |
| Oud For Glory | `MAHbqHDWiHw` | falta bajarla |
| Qaed Al Fursan | `MAHbqEZXCmc` | falta bajarla |
| Roses Musk | `MAHbqMywu-w` | falta bajarla |
| Scandal Pour Homme Le Parfum | `MAHbqNWyY0M` | falta bajarla |
| Stallion 53 | `MAHbqAv2BwU` | falta bajarla |
| The Most Wanted Intense | `MAHbqBQkSBI` | falta bajarla |
| The Most Wanted Parfum | `MAHbqCHOI3k` | falta bajarla |
| Torino21 | `MAHbqFEAiWo` | falta bajarla |
| Uomo Born In Roma Coral Fantasy | `MAHbqJvKPTE` | falta bajarla |
| Uomo Born In Roma | `MAHbqKbQnOI` | falta bajarla |
| Uomo Born In Roma Extradose | `MAHbqNFQwdE` | falta bajarla |
| Vulcan Feu | `MAHbqAT43Ak` | falta bajarla |
| Yara Candy | `MAHbqHWc9G4` | falta bajarla |
| Yara | `MAHbqKdgs0E` | falta bajarla |

Falta **Spicebomb Extreme**: el generador de Canva rechazó la imagen (el
frasco tiene forma de granada y lo frena su filtro de contenido). No se volvió
a intentar cambiando el texto para esquivar el filtro; ese producto conserva
su placa de acordes hasta que Bautista decida cómo resolverlo.

Las que dicen "falta bajarla" están generadas y guardadas en su Canva, pero
todavía no pasaron por el diseño de trabajo: para eso hacen falta tres
aprobaciones suyas seguidas (sumar páginas, colocar fotos, guardar) y si no
contesta alguna en unos minutos la sesión se reinicia y hay que empezar de
nuevo ese paso.

## Cómo se bajan y con qué texto se generaron

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
