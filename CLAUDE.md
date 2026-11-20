# Cenzia Decants — guía de marca

Decants y extractos de perfumes originales. Argentina. Tienda Nube, tema `recife`.
Dominio: cenziadecants.com

Esta guía está armada con datos reales extraídos de la tienda en vivo (CSS del
tema, descripciones existentes, catálogo, API) — no inventados. Las secciones
marcadas **[PENDIENTE]** no se pudieron inferir y las tiene que definir Bautista.

## Identidad

- **Nombre:** Cenzia Decants
- **Rubro:** decants (fraccionados) y extractos de perfumes originales de nicho, diseñador y árabes
- **País / moneda:** Argentina / ARS
- **Dominio:** cenziadecants.com
- **Email de contacto:** cenziadecants@gmail.com
- **WhatsApp:** +54 3402 48-5423
- **Instagram:** [@cenziadecants](https://instagram.com/cenziadecants)
- **Plataforma:** Tienda Nube, tema Recife (`recife`)

**Terminología de cara al cliente (desde 2026-11-16):** la línea de extractos
ya NO se nombra "Extracto" en ningún texto visible al cliente (descripciones,
badges, CTAs, nombres de producto). Se usan dos términos, cada uno en su rol:

- **Cenzia Privé** → nombre de la línea/colección (sustantivo propio, no se
  cuenta ni se pluraliza). Se usa para presentar la línea en general: eyebrows
  de sección, el nombre de los combos ("Combo Seductor - Cenzia Privé"), la
  comparativa ("Cenzia Privé vs. perfume original"), fotos de antes/después.
  Mismo patrón que usan Dior Privé o Armani Privé en la industria real.
- **Esencia Privé** → sustantivo común, contable, para cuando se habla de una
  o varias unidades del producto: el badge ("60ML Esencia Privé"), "una
  Esencia Privé", "4 Esencias Privé de 60ml", preguntas del FAQ.

Presentada como una línea propia de Cenzia de interpretaciones/inspiraciones
de alta concentración, dejando siempre claro que no son productos oficiales
de las marcas en las que se inspiran. "Extracto" se sigue usando solo como
término técnico interno (ID de categoría de Tienda Nube, nombres de
archivo/script, handles de URL) — no como palabra que vea el cliente.

**Qué se afirma de Cenzia Privé (desde 2026-11-16):** son inspiraciones. El
copy dice "inspirada en {perfume}" y "desarrollada para replicar lo más
fielmente posible el aroma"; nunca "original", "igual al original", "mismo
aroma", "mismas esencias" ni "mismos aromatizantes". La aclaración va siempre,
pero discreta (texto chico, no como titular): a Bautista un título grande tipo
"esto no es el original" le baja la venta. Tampoco se promete "stock
permanente" mientras la línea esté en preventa.

**Una marca, dos líneas:** Decants Originales (perfume original fraccionado,
5/10 ml) y Cenzia Privé (inspiraciones, 60 ml) no se mezclan en la misma
categoría, anuncio ni pieza. Textos para Instagram y regla de anuncios en
`redes/instagram-y-anuncios.md`; memoria del chatbot en
`chatbot/memoria-ia.txt` (Bautista la pega a mano en el bot).

## Colores (extraídos del tema en vivo)

| Uso | Color |
|---|---|
| Texto principal / marca (`--main-foreground`) | `#0d161f` (navy casi negro) |
| Fondo (`--main-background`) | `#ffffff` |
| Fondo de imagen de producto | `#f6f7f8` |
| Texto secundario / cuotas | `#7a8694` |
| Precio tachado / gris claro | `#a8b0b8` |
| Bordes / separadores | `#ececec` |

El navy `#0d161f` es el color de marca de facto: se usa en botones, badges,
precios y títulos en todo el sitio. Es el color a usar por defecto para
cualquier elemento nuevo (badges, botones, acentos) salvo que se pida otra cosa.

## Tipografía (extraída del tema en vivo)

- **Títulos (`--heading-font`):** Poppins
- **Texto / cuerpo (`--body-font`):** Manrope
- Tamaño base: 16px

## Tono y estilo de copy (observado en descripciones existentes)

- Directo e informativo, no es florido ni poético.
- Formato típico de descripción de producto: nombre de la fragancia y marca en
  **negrita**, 2–4 oraciones con la familia olfativa y el público (ej. "fragancia
  oriental ambarada intensa para hombre"), pirámide olfativa cuando se conoce
  (notas de salida / corazón / fondo).
- SEO title: `Decant [Nombre] [tamaño] - Perfume Original Intenso para [Hombre/Mujer]`
- SEO description: `Disfrutá Decant [Nombre] [tamaño], fragancia [tipo] con notas de [notas]. ¡Elegí [adjetivo] y [adjetivo] hoy mismo!`
- Español rioplatense ("vos", "elegí", "disfrutá").

**[PENDIENTE]** tagline/eslogan de marca, misión, valores o adjetivos de personalidad
de marca más allá de lo observable en el copy — no hay info suficiente en el
sitio para inferir esto, hay que definirlo con Bautista.

## Catálogo — estructura de categorías

| Categoría | Visibilidad | Uso |
|---|---|---|
| Decants Originales | visible | todo el catálogo activo de decants |
| Árabes / Diseñador / Nicho | visibles | familia olfativa / segmento |
| Masculino / Femenino | visibles | género |
| Unisex | oculta | género |
| Perfumes Enteros | oculta | frascos completos (no decant) |
| Ofertas | oculta | liquidación |
| Combos | visible | bundles de varios decants (hija de Decants Originales; los combos Privé NO van acá) |
| Cenzia Privé | visible | la línea Privé completa. URL `/extracto/` (el handle no se cambió para no romper links) |
| ↳ Combos Cenzia Privé | visible | los 10 combos Privé, con subcategorías Masculino / Femenino. URL `/extracto/combos-extracto/` |
| ↳ Esencias Privé | visible | las 23 individuales, con subcategorías Masculino / Femenino. URL `/extracto/extractos-individuales/` |
| Extractos de Perfume | oculta, destacada en el home | productos de 60ML Esencia Privé — nombre de categoría interno, el cliente ve "Esencia Privé" (creada 2026-10-31) |

Patrón de nombre de producto:

- Decants: `{Nombre de la fragancia} - {Marca}` (ej. `Le Male Elixir - JPG`,
  `Arabians Tonka - Montale`).
- Esencias Privé: `{Perfume} de {Marca} - Inspiración Cenzia Privé` (ej.
  `Sauvage Elixir de Dior - Inspiración Cenzia Privé`). El nombre del perfume
  va siempre adelante. Sin repetir la marca cuando ya está en el nombre
  (`Bleu de Chanel - ...`, `Bharara King - ...`).
- Combos Privé: `Combo {Nombre} - Cenzia Privé`.

En los 33 productos Privé el campo `brand` es "Cenzia Privé" (no la marca
original) y el título SEO sigue el formato
`Inspirado en {Perfume} de {Marca} | Cenzia Privé 60 ml`.

## Formatos de producto y precios de referencia

- **Decants:** 5ML y 10ML, variantes dentro del mismo producto. Precios
  observados ~$29.000–$66.000 ARS según tamaño y marca.
- **Esencia Privé (ex "Extractos"):** 60ML, una sola variante, el tamaño va
  implícito (no se agrega como variante). Precio fijo definido: **$35.000 ARS**.
- **Combos:** bundles de varios decants, categoría aparte.
- **Combos Cenzia Privé:** escalera por cantidad de fragancias, vigente desde
  2026-11-16: 2→$59.900 · 3→$84.900 · 4→$99.900 · 5→$114.900 · 6→$124.900.
  En la API el precio de venta va en `promotional_price` y el tachado en
  `price` (= cantidad × $35.000). Composición de cada combo en
  `scripts/data/combo_notes.py`. Bautista cambia precios él mismo desde el
  panel: después de un cambio hay que actualizar el "Desde $X c/u" de la
  descripción y el cartel "Ahorrás $X" del CSS, que no se recalculan solos.
- **Perfumes Enteros:** frascos completos de marca, categoría oculta aparte.

## Sistema de badges visuales (CSS, en `styles/original-badge.css`)

Pill oscura (`#0d161f`, texto blanco, mayúsculas, esquina superior derecha de
la imagen) sobre cada producto:

- **"Original"** → default para todo el catálogo salvo excepción explícita.
- **"60ML Esencia Privé"** → productos de la categoría Extractos de Perfume
  (por ID, ver el CSS — el tema no expone la categoría en el HTML de las
  tarjetas). El texto visible dice "Esencia Privé", nunca "Extracto".
- Exclusiones (ej. futuras esencias no originales) se agregan por ID de
  producto en el mismo archivo.
- Los 10 combos Privé no llevan pill (la foto ya dice "Cenzia Privé") y en su
  ficha el chip de descuento se reemplaza por "Ahorrás $X", con el monto
  escrito a mano por ID de producto (tachado − precio promocional).

Mecanismo de despliegue: el editor de temas de Tienda Nube solo tiene campo de
**CSS personalizado** (no JS), así que todo esto se resuelve con CSS puro y hay
que pegarlo manualmente ahí cada vez que cambia (no hay forma de automatizarlo
vía API con el scope actual del token — falta `write_scripts`).

## Descripciones de producto Cenzia Privé

- Plantillas: `product-descriptions/extractos.html` (23 individuales) y
  `product-descriptions/combos.html` (10 combos). Datos por producto en
  `scripts/data/olfactory-notes.py` y `scripts/data/combo_notes.py`.
- Generadores: `scripts/push-olfactory-notes.py` y
  `scripts/push-combo-descriptions.py`. Pisan la descripción entera, así que
  **siempre correr primero con `--diff`**, que compara contra la tienda sin
  subir nada. Al 2026-11-16 las 33 descripciones publicadas salen idénticas
  del repo; si el diff muestra algo que no viene de un cambio propio, alguien
  editó en la tienda y hay que traer ese cambio a la plantilla antes de subir.
- El cartel de preventa (plazo y fecha) lo actualizan Bautista u otra sesión
  directamente en la tienda: la tienda manda. El 2026-11-16 una re-subida
  desde el repo le pisó ese cartel en 7 combos.
- Las 47 reseñas del final se dejan como están (decisión de Bautista,
  2026-11-16). Vienen en la plantilla desde el 2026-10-31 y el formulario
  "Escribir una reseña" no guarda nada, así que no describirlas como reseñas
  verificadas ni llevar el "4.8 (47 reseñas)" a productos nuevos por
  iniciativa propia.

## Placas de galería (una por perfume)

- Carpeta `placas/`: `placas.json` (textos por perfume), `card.html` (diseño,
  2000 x 2000), `render.js` (genera `out/{slug}-final.png`), `scenes/` (foto
  de cada perfume rodeado de sus materias primas), `src/` (frasco de marca
  recortado, referencia para generar la foto), `add_scene.py` (suma una foto
  nueva) y `FUENTES.md` (origen de cada imagen y cómo se bajan del Canva de
  Bautista en tamaño completo).
- Hay 23 placas con foto final, una por cada Esencia Privé del catálogo.
  Aprobó el diseño sobre la de Born In Roma Intense ("tenés que hacerlas
  así", 2026-11-20).
- **Formato que pide Bautista para toda foto de la tienda: 1:1 y fondo blanco
  puro** ("las fotos tienen que estar en 1:1 y fondo full white",
  2026-11-20). La placa es 2000 x 2000 con fondo `#fff` y la foto del perfume
  también va sobre blanco (`scene_bg: "white"`), sin recuadro gris. Las 14
  primeras se habían hecho con fondo gris claro y se rehicieron sobre blanco
  ese mismo día con su OK.
- La foto muestra solo el perfume de marca con sus materias primas: el frasco
  Cenzia Privé no aparece (pedido de Bautista, 2026-11-16). El encabezado va
  chico: lo que tiene que destacar es la información.
- El texto lo pone siempre `card.html`; nunca se le pide a un generador de
  imágenes (la prueba en Runway salió con errores de tipeo en casi todo).
- A Bautista no le sirven bocetos ni vistas previas borrosas: mostrarle la
  placa terminada.
- Las notas de cada placa son las de la descripción del producto. Excepción
  al 2026-11-20: Born In Roma Intense, donde la placa lleva las notas del
  perfume (vainilla bourbon, lavandín, vetiver ahumado) y la descripción de
  la tienda tiene otras; falta que Bautista decida si se corrige.
- Subida a las galerías de los combos: `scripts/upload-placas.py` (sin
  argumentos muestra el plan; con `--subir` sube). Al 2026-11-20 no se subió
  nada: falta el OK de Bautista.

## Fotografía de producto

Estilo de imagen principal establecido en este proyecto (ver
`scripts/original-badge.js` / conversación): fondo blanco de estudio puro,
el frasco original de marca y el decant/extracto flotando juntos, una sola
luz suave (superior izquierda), sombra de contacto realista, sin props
agregados. Flujo de trabajo: recorte en Canva → composición → Runway para
resolver luz/sombra/realismo final.

## Integraciones técnicas

- **API Tienda Nube:** REST v1, autenticación vía Network secret del entorno
  (header `Authentication: bearer <token>`, host `api.tiendanube.com`, scopes
  actuales NO incluyen `write_scripts` — para instalar scripts hay que pegar
  código manualmente en el panel).
- Ver `README.md` para cómo probar la conexión.
- **Renombrar un producto por API le cambia la URL:** un `PUT` que manda solo
  `name` regenera el `handle`, y la URL anterior pasa a dar 404 (pasó el
  2026-11-16 con los 7 combos Cenzia Privé; hubo que restaurar los handles).
  Al renombrar, mandar siempre el `handle` actual en el mismo `PUT` y verificar
  después que la URL de antes sigue cargando. Tener el mismo cuidado con las
  categorías, que también arman las URLs del menú.
- **Renombrar una categoría por API le borra la categoría padre** si el `PUT`
  no la incluye (queda en la raíz y cambia el menú). Mandar siempre `name` +
  `handle` + `parent`.
- Un `PUT` de `categories` en un producto funciona, pero la respuesta devuelve
  las categorías viejas: verificar con un `GET` aparte.
- La API corta con 429 después de unas 25 escrituras seguidas: pausar ~1 s
  entre `PUT` o reintentar.
- **El menú de la tienda no es el árbol de categorías.** Se arma aparte en el
  panel (Tienda online → Menús) y la API solo deja leerlo:
  `GET /navigations` responde (no está documentado), pero `POST`, `PUT` y
  `PATCH` dan 404, así que cualquier cambio de pestañas lo hace Bautista a
  mano. Un link de tipo categoría con `data.id` "0" es "Todas": despliega
  todas las categorías raíz adentro de esa pestaña (así estaba "Decants" el
  2026-11-16, y por eso mostraba Cenzia Privé adentro aunque en el árbol las
  dos líneas son raíz). Mientras Bautista no lo cambie en el panel, el último
  bloque de `styles/theme-custom-css-full.css` ("MENÚ: las dos líneas como
  pestañas principales") lo resuelve a la vista en celular y computadora; se
  desactiva solo cuando la pestaña deje de apuntar a /productos/. Ojo si se
  toca ese bloque: el tema le pone `pointer-events: none` al desplegable al
  salir el mouse y eso se hereda a las pestañas subidas con `display: contents`.
- **Ver la tienda en vivo desde el entorno cloud:** usar
  `https://www.cenziadecants.com` (con `www`). El dominio sin `www` falla en el
  handshake TLS desde el sandbox.
