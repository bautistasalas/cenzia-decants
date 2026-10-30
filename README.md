# Cenzia Decants

Proyecto de la tienda **Cenzia Decants** (decants de perfumes, Argentina), en **Tienda Nube** (tema actual: `recife`).

- Dominio: cenziadecants.com
- Panel: Tienda Nube (API REST v1)

## API de Tienda Nube

Este proyecto usa la API REST de Tienda Nube. Las credenciales (Store ID y Access Token) **no se commitean** — se guardan como secretos del entorno (`TIENDANUBE_STORE_ID`, `TIENDANUBE_ACCESS_TOKEN`).

Probar la conexión:

```bash
TIENDANUBE_STORE_ID=xxx TIENDANUBE_ACCESS_TOKEN=xxx ./scripts/test-connection.sh
```

## Estado

Proyecto recién creado — todavía no hay brand guidelines ni estructura de página definida.
