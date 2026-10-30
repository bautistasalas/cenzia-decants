#!/usr/bin/env bash
# Prueba rápida de la API de Tienda Nube usando variables de entorno.
# Uso: TIENDANUBE_STORE_ID=... TIENDANUBE_ACCESS_TOKEN=... ./scripts/test-connection.sh
set -euo pipefail

: "${TIENDANUBE_STORE_ID:?Falta la variable TIENDANUBE_STORE_ID}"
: "${TIENDANUBE_ACCESS_TOKEN:?Falta la variable TIENDANUBE_ACCESS_TOKEN}"

curl -sS -X GET "https://api.tiendanube.com/v1/${TIENDANUBE_STORE_ID}/store" \
  -H "Authentication: bearer ${TIENDANUBE_ACCESS_TOKEN}" \
  -H "User-Agent: CenziaDecants (contactoandiva@gmail.com)" \
  -H "Content-Type: application/json" \
  -w "\nHTTP_STATUS:%{http_code}\n"
