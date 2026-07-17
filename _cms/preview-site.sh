#!/bin/bash
# Ensambla una copia COMPLETA de la web (con navegación funcionando) y regenera
# el blog desde los datos migrados, en _cms/_preview_site/.
# Sirve como preview fiel de cómo quedará todo con el CMS, sin tocar la web en vivo.
set -e
cd "$(dirname "$0")"          # -> _cms
SITE=..
OUT=_preview_site

echo "→ Limpiando $OUT ..."
rm -rf "$OUT"
mkdir -p "$OUT"

echo "→ Copiando la web actual (sin herramientas) ..."
rsync -a \
  --exclude '_cms' \
  --exclude 'node_modules' \
  --exclude '.git' \
  --exclude '.github' \
  --exclude '.wrangler' \
  --exclude 'seo_reports' \
  --exclude 'blacknova-deploy' \
  --exclude 'tools' \
  "$SITE"/ "$OUT"/

echo "→ Regenerando el blog desde Sanity (en vivo) ..."
export SANITY_PROJECT_ID="${SANITY_PROJECT_ID:-w7ezq063}"
export SANITY_DATASET="${SANITY_DATASET:-production}"
node build.mjs --source=sanity --out="$OUT"

echo "✅ Preview completo del sitio en: $OUT"
echo "   Ábrelo con:  open $OUT/blog.html"
