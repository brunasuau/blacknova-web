import os
from bs4 import BeautifulSoup

# ─── CONFIGURACIÓN SEO POR PÁGINA ────────────────────────────
SEO = {
    "index.html": {
        "title": "Blacknova | Gestión de Activos Inmobiliarios y Proyectos en Catalunya",
        "description": "Blacknova es tu partner en gestión de activos inmobiliarios, naves industriales y proyectos de construcción en Catalunya. Metodología PMI y red de talento europea.",
    },
    "sobre-nosotros.html": {
        "title": "Sobre Nosotros | Blacknova – Gestión de Proyectos PMI en Catalunya",
        "description": "Más de 10 años de experiencia en gestión de proyectos industriales y activos inmobiliarios en Catalunya. Equipo multidisciplinar con metodología PMI y Agile.",
    },
    "que-hacemos.html": {
        "title": "Qué Hacemos | Blacknova – Proyectos Industriales y Naves en Catalunya",
        "description": "Gestión integral de proyectos, naves industriales y activos inmobiliarios en Catalunya. Análisis de viabilidad, coordinación RRHH y supervisión de obra con metodología PMI.",
    },
    "talentos.html": {
        "title": "Talentos | Blacknova – Selección de Ingenieros y Project Managers Catalunya",
        "description": "Conectamos empresas con los mejores project managers, ingenieros y técnicos de construcción en Catalunya. Red de talento especializado en proyectos industriales e inmobiliarios.",
    },
    "me-siento-talento.html": {
        "title": "Me Siento Talento | Únete a Blacknova – Project Manager e Ingenieros Catalunya",
        "description": "¿Eres project manager, ingeniero o técnico de construcción en Catalunya? Únete al equipo Blacknova y desarrolla tu carrera en gestión de proyectos industriales e inmobiliarios.",
    },
    "busco-talento.html": {
        "title": "Busco Talento | Blacknova – Reclutamiento Industrial y PMI en Catalunya",
        "description": "¿Necesitas incorporar project managers o ingenieros a tu empresa en Catalunya? Blacknova selecciona el talento técnico que necesitas con garantía de encaje y seguimiento.",
    },
    "contacto.html": {
        "title": "Contacto | Blacknova – Gestión de Proyectos e Inmobiliario en Catalunya",
        "description": "Contacta con Blacknova para gestión de activos inmobiliarios, proyectos industriales o selección de talento técnico en Catalunya. Te respondemos en menos de 24 horas.",
    },
}
# ─────────────────────────────────────────────────────────────

# Carpeta donde están los HTML (misma carpeta que este script)
CARPETA = os.path.dirname(os.path.abspath(__file__))

print("🔧 Aplicando mejoras SEO a los archivos HTML de Blacknova...\n")

modificados = 0
errores = 0

for archivo, datos in SEO.items():
    ruta = os.path.join(CARPETA, archivo)

    if not os.path.exists(ruta):
        print(f"   ⚠️  No encontrado: {archivo} — asegúrate de que está en la misma carpeta")
        errores += 1
        continue

    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

    soup = BeautifulSoup(contenido, "html.parser")
    head = soup.find("head")

    if not head:
        print(f"   ❌ Sin <head> en {archivo}")
        errores += 1
        continue

    # Actualizar o crear <title>
    title_tag = soup.find("title")
    if title_tag:
        title_tag.string = datos["title"]
    else:
        nuevo_title = soup.new_tag("title")
        nuevo_title.string = datos["title"]
        head.insert(0, nuevo_title)

    # Actualizar o crear <meta name="description">
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag:
        meta_tag["content"] = datos["description"]
    else:
        nuevo_meta = soup.new_tag("meta")
        nuevo_meta["name"] = "description"
        nuevo_meta["content"] = datos["description"]
        # Insertar después del title
        title_tag = soup.find("title")
        if title_tag:
            title_tag.insert_after(nuevo_meta)
        else:
            head.insert(1, nuevo_meta)

    # Añadir meta charset y viewport si no existen
    if not soup.find("meta", attrs={"charset": True}):
        charset_tag = soup.new_tag("meta")
        charset_tag["charset"] = "UTF-8"
        head.insert(0, charset_tag)

    if not soup.find("meta", attrs={"name": "viewport"}):
        viewport_tag = soup.new_tag("meta")
        viewport_tag["name"] = "viewport"
        viewport_tag["content"] = "width=device-width, initial-scale=1.0"
        head.insert(1, viewport_tag)

    # Guardar el archivo modificado
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"   ✅ {archivo}")
    print(f"      Título: {datos['title'][:60]}...")
    print(f"      Meta:   {datos['description'][:60]}...")
    print()
    modificados += 1

print("─" * 50)
print(f"✅ {modificados} archivos actualizados correctamente")
if errores:
    print(f"⚠️  {errores} archivos no encontrados — cópialos a la misma carpeta que este script")
print("\n📌 Próximo paso: sube los archivos modificados a tu servidor (blacknova.es)")
print("   Después vuelve a ejecutar seo_audit.py para verificar que todo está correcto.")
