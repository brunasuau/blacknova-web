#!/bin/bash
# Importa tus 16 artículos actuales a Sanity (como PUBLICADOS).
# Requiere tu login de Sanity (se abre el navegador una vez).
set -e
cd "$(dirname "$0")/studio"

echo "1) Login en Sanity (se abrirá el navegador)…"
npx sanity login

echo "2) Asegurando el dataset 'production'…"
npx sanity dataset create production --visibility public 2>/dev/null || echo "   (ya existía, seguimos)"

echo "3) Importando los 16 artículos…"
npx sanity dataset import ../migration/posts.ndjson production --replace

echo "✅ Listo. Ábrelo en el panel: http://localhost:3333  → 'Artículo de blog'."
