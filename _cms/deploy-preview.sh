#!/bin/bash
# Publica una URL de PRUEBA en Cloudflare Pages (proyecto aparte, no toca blacknova.es).
# Reconstruye el sitio de preview y lo sube a https://blacknova-preview.pages.dev
# Requiere tu login de Cloudflare (se abre el navegador la primera vez).
set -e
cd "$(dirname "$0")"

echo "→ Reconstruyendo el sitio de preview…"
./preview-site.sh

echo "→ Subiendo a Cloudflare Pages (proyecto 'blacknova-preview')…"
npx wrangler pages deploy _preview_site \
  --project-name blacknova-preview \
  --commit-dirty=true

echo "✅ URL de prueba lista (mira la línea de arriba con *.pages.dev)."
