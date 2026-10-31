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
| Combos | visible | bundles de varios decants |
| Extractos de Perfume | oculta, destacada en el home | productos de 60ML extracto (creada 2026-10-31) |

Patrón de nombre de producto: `{Nombre de la fragancia} - {Marca}`
(ej. `Le Male Elixir - JPG`, `Arabians Tonka - Montale`).

## Formatos de producto y precios de referencia

- **Decants:** 5ML y 10ML, variantes dentro del mismo producto. Precios
  observados ~$29.000–$66.000 ARS según tamaño y marca.
- **Extractos:** 60ML, una sola variante, el tamaño va implícito (no se agrega
  como variante). Precio fijo definido: **$35.000 ARS**.
- **Combos:** bundles de varios decants, categoría aparte.
- **Perfumes Enteros:** frascos completos de marca, categoría oculta aparte.

## Sistema de badges visuales (CSS, en `styles/original-badge.css`)

Pill oscura (`#0d161f`, texto blanco, mayúsculas, esquina superior derecha de
la imagen) sobre cada producto:

- **"Original"** → default para todo el catálogo salvo excepción explícita.
- **"60ML Extracto"** → productos de la categoría Extractos de Perfume (por ID,
  ver el CSS — el tema no expone la categoría en el HTML de las tarjetas).
- Exclusiones (ej. futuras esencias no originales) se agregan por ID de
  producto en el mismo archivo.

Mecanismo de despliegue: el editor de temas de Tienda Nube solo tiene campo de
**CSS personalizado** (no JS), así que todo esto se resuelve con CSS puro y hay
que pegarlo manualmente ahí cada vez que cambia (no hay forma de automatizarlo
vía API con el scope actual del token — falta `write_scripts`).

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
