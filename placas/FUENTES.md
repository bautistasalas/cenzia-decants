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

## Fotos de los Decants Originales (2026-11-21 a 24)

Los 66 decants en stock llevan la misma placa (`decants.json`, variante
`linea: "decant"` de `card.html`). 13 reusan la foto de su Esencia Privé (es el
mismo perfume de marca); para los otros 53 se generó una foto nueva en el Canva
de Bautista con el mismo texto de más abajo, tomando como referencia el frasco
recortado de la foto del decant en la tienda (`prep_assets.py --decant`; el de
Chocolate Dubai se recortó a mano).

Las notas de estas 53 placas no salen de la descripción del producto sino de
la pirámide publicada por la marca o por Fragrantica/Parfumo, porque varias
descripciones de decants tienen notas que no son de ese perfume.

| Perfume | Identificador en Canva |
|---|---|
| Costa Azzurra Parfum | `MAHbp5HyXRo` |
| 9AM Dive | `MAHbgGuvbNE` |
| 9PM | `MAHbp0TFlFU` |
| 9PM Rebel | `MAHbp9JUGMg` |
| Acqua di Giò Profondo Parfum | `MAHbp1Yur4Y` |
| Acqua di Giò Parfum | `MAHbp1Vnx6Y` |
| Amber Oud Dubai Night | `MAHbp60XwsY` |
| Amber Oud Aqua Dubai | `MAHbpybw2sc` |
| Armani Code | `MAHbp_Re5pA` |
| Man In Black | `MAHbpx7oG-o` |
| Odyssey Dubai Chocolat | `MAHbp2W6tdg` |
| Divine Le Parfum | `MAHbp3jqSIA` |
| Dylan Blue | `MAHbp5FFZYY` |
| Eros Eau de Parfum | `MAHbgDY9cQE` |
| Eros Eau de Toilette | `MAHbp3fFs8k` |
| Fakhar Black | `MAHbp4ptzMo` |
| Fakhar Rose | `MAHbp7qMF34` |
| Fame | `MAHbp-2GEXg` |
| Good Girl Blush | `MAHbpz0y8Zc` |
| Hawas Ice | `MAHbh7PL-HI` |
| Hawas Malibu | `MAHbp619XsI` |
| Hawas | `MAHbhwVYYPE` |
| Hawas Tropical | `MAHbp3pMgSQ` |
| His Confession | `MAHbp07S_Ao` |
| Honor & Glory | `MAHbh7S95Ww` |
| Intense Café | `MAHbqEB4FAI` |
| Jean Lowe Immortel | `MAHbqIkYyfY` |
| Khamrah | `MAHbqNXTLjE` |
| Khamrah Qahwa | `MAHbqOk2FwI` |
| Layton | `MAHbgL_PnlY` |
| Le Beau Le Parfum | `MAHbh0tvtMk` |
| Le Male Elixir Absolu | `MAHbqLREgzs` |
| Libre | `MAHbqMAcPxk` |
| Liquid Brun | `MAHbqCwhXjA` |
| Odyssey Mandarin Sky | `MAHbqNUSfgE` |
| MYSLF | `MAHbqChb8DU` |
| Naxos | `MAHbgLrG08g` |
| Odyssey Aqua | `MAHbqKqSLME` |
| Oud For Glory | `MAHbqHDWiHw` |
| Qaed Al Fursan | `MAHbqEZXCmc` |
| Roses Musk | `MAHbqMywu-w` |
| Scandal Pour Homme Le Parfum | `MAHbqNWyY0M` |
| Stallion 53 | `MAHbqAv2BwU` |
| The Most Wanted Intense | `MAHbqBQkSBI` |
| The Most Wanted Parfum | `MAHbqCHOI3k` |
| Torino21 | `MAHbqFEAiWo` |
| Uomo Born In Roma Coral Fantasy | `MAHbqJvKPTE` |
| Uomo Born In Roma | `MAHbqKbQnOI` |
| Uomo Born In Roma Extradose | `MAHbqNFQwdE` |
| Vulcan Feu | `MAHbqAT43Ak` |
| Yara Candy | `MAHbqHWc9G4` |
| Yara | `MAHbqKdgs0E` |

Falta **Spicebomb Extreme**: el generador de Canva rechazó la imagen (el
frasco tiene forma de granada y lo frena su filtro de contenido). No se volvió
a intentar cambiando el texto para esquivar el filtro; ese producto conserva
su placa de acordes hasta que Bautista decida cómo resolverlo.

Las 52 están en `scenes/` (bajadas entre el 2026-11-21 y el 2026-11-24).

En la foto de **Fame** los trozos de sándalo parecen ramas de canela: es
candidata a rehacer si Bautista lo pide.

## Cómo se bajan y con qué texto se generaron

Para bajarlas en tamaño completo no alcanza con el identificador (Canva solo
devuelve una miniatura de 149 x 200): hay que colocar cada foto en una página
de 1500 x 2000 de un diseño, guardar y exportar esas páginas como PNG. Se usa
el diseño de trabajo "Publicación cuadrada con foto a sangre" (`DAHbGZCniAo`).
Después, `add_scene.py --blanco` las deja en `scenes/` a 1200 x 1600, con el
fondo llevado a blanco puro y los bordes fundidos.

Colocar fotos en el diseño (`edit-design`) le pide permiso a Bautista en el
celular cada vez; generar, leer y exportar no. Lo que se aprendió:

- Un pedido de permiso sin contestar deja la sesión esperando. Cuando la
  sesión se reinicia, el pedido se pierde y también la edición abierta (Canva
  responde "transaction not found"): hay que abrir otra y volver a pedirlo.
- Por eso conviene que sean **dos permisos seguidos y nada en el medio**:
  colocar todas las fotos en una sola llamada y guardar en la siguiente. Sumar
  páginas nuevas agrega un tercer permiso y medio minuto de espera entre uno y
  otro; así se perdieron tres intentos entre el 22 y el 23 de noviembre.
- Para evitar ese tercer permiso, la última tanda (28 fotos) se colocó encima
  de páginas de trabajo que ya estaban exportadas, de la 35 a la 62. En esas
  páginas el título no coincide con la foto que se ve y la foto vieja queda
  tapada debajo de la nueva: no se borró nada.
- Las fotos generadas que no se consultan enseguida se pierden (el trabajo
  vence a las pocas horas y después no hay forma de recuperarlo): pedir el
  resultado apenas se lanza.
- La última tanda se destrabó el 2026-11-24: se le mandó un aviso al celular
  (`PushNotification`) justo antes de pedir el permiso y aprobó los dos al
  rato. No se sabe si entró por el aviso o por su cuenta, pero es lo único
  que se hizo distinto.

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
