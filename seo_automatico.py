import requests
from bs4 import BeautifulSoup
import json
import os
import time
from datetime import datetime

# ─── CONFIGURACIÓN ───────────────────────────────────────────
WEB = "https://blacknova.es"
KEYWORDS = [
    "gestión activos inmobiliarios Catalunya",
    "naves industriales Catalunya",
    "project manager Catalunya",
    "gestión proyectos PMI Barcelona",
    "selección talento ingeniería Catalunya",
    "construcción industrial Barcelona",
    "gestión naves industriales Barcelona",
    "project management industrial España",
]
PAGINAS = [
    "https://blacknova.es/",
    "https://blacknova.es/sobre-nosotros.html",
    "https://blacknova.es/que-hacemos.html",
    "https://blacknova.es/talentos.html",
    "https://blacknova.es/me-siento-talento.html",
    "https://blacknova.es/busco-talento.html",
    "https://blacknova.es/contacto.html",
]
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
OUTPUT_DIR = "seo_reports"
BLOG_DIR = "blog_articles"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(BLOG_DIR, exist_ok=True)
# ─────────────────────────────────────────────────────────────

ARTICULOS_BLOG = [
    {
        "slug": "gestion-activos-inmobiliarios-catalunya",
        "titulo": "Gestión de Activos Inmobiliarios en Catalunya: Guía Completa 2026",
        "descripcion": "Todo lo que necesitas saber sobre la gestión profesional de activos inmobiliarios industriales en Catalunya. Metodología, normativa y mejores prácticas.",
        "keywords_principales": ["gestión activos inmobiliarios Catalunya", "activos industriales Catalunya"],
        "contenido": """
        <h2>¿Qué es la gestión de activos inmobiliarios industriales?</h2>
        <p>La gestión de activos inmobiliarios industriales en Catalunya es el conjunto de procesos y metodologías orientados a maximizar el rendimiento de naves industriales, polígonos y propiedades de uso industrial. En un mercado tan dinámico como el catalán, contar con una gestión profesional marca la diferencia entre un activo rentable y uno que pierde valor.</p>
        <p>En Blacknova aplicamos una metodología basada en el estándar PMI para la gestión integral de activos inmobiliarios en Catalunya, garantizando transparencia, rigor y resultados medibles para propietarios e inversores.</p>

        <h2>¿Por qué Catalunya es clave en el mercado industrial español?</h2>
        <p>Catalunya concentra el 25% del PIB industrial de España. El corredor mediterráneo, el Puerto de Barcelona y la red de autopistas hacen de Catalunya el hub logístico e industrial más importante de la Península Ibérica. La demanda de naves industriales en polígonos como el Baix Llobregat, Martorell, Tarragona y Girona no para de crecer.</p>
        <p>La rentabilidad bruta de las naves industriales en Catalunya oscila entre el 6% y el 8% anual, muy por encima del 3-4% del sector residencial. Sin embargo, esta rentabilidad solo se consigue con una gestión profesional del activo.</p>

        <h2>Servicios de gestión de activos inmobiliarios de Blacknova</h2>
        <p>En Blacknova ofrecemos una gestión integral de activos inmobiliarios industriales en Catalunya que incluye:</p>
        <ul>
            <li><strong>Auditoría técnica inicial:</strong> Evaluación del estado del activo, identificación de problemas y oportunidades de mejora.</li>
            <li><strong>Gestión de contratos de arrendamiento:</strong> Negociación, redacción y seguimiento de contratos con inquilinos.</li>
            <li><strong>Mantenimiento preventivo y correctivo:</strong> Coordinación de todos los servicios de mantenimiento.</li>
            <li><strong>Control normativo:</strong> Verificación continua del cumplimiento de licencias, normativa de seguridad y urbanismo.</li>
            <li><strong>Reporting periódico:</strong> Informes mensuales al propietario sobre el estado y rendimiento del activo.</li>
            <li><strong>Optimización de rentabilidad:</strong> Análisis de mercado y propuestas para maximizar el rendimiento del activo.</li>
        </ul>

        <h2>¿Cuánto cuesta la gestión profesional de una nave industrial?</h2>
        <p>Los honorarios de gestión de activos inmobiliarios industriales en Catalunya suelen oscilar entre el 5% y el 10% de la renta mensual del activo. Una inversión que se amortiza rápidamente gracias a la optimización de la rentabilidad, la reducción de períodos de vacío y la prevención de problemas técnicos y legales.</p>

        <h2>Contacta con Blacknova para la gestión de tu activo</h2>
        <p>Si tienes una nave industrial en Catalunya y quieres gestionarla de forma profesional, contacta con nosotros. Primera consulta gratuita y sin compromiso en <a href="https://blacknova.es/contacto.html">blacknova.es</a>.</p>
        """,
    },
    {
        "slug": "naves-industriales-catalunya-guia",
        "titulo": "Naves Industriales en Catalunya: Todo lo que Necesitas Saber en 2026",
        "descripcion": "Guía completa sobre naves industriales en Catalunya: tipos, zonas, precios, normativa y cómo elegir la nave perfecta para tu empresa.",
        "keywords_principales": ["naves industriales Catalunya", "alquiler naves industriales Barcelona"],
        "contenido": """
        <h2>El mercado de naves industriales en Catalunya en 2026</h2>
        <p>Catalunya es el mercado de naves industriales más activo de España. La demanda logística impulsada por el e-commerce, la proximidad al Puerto de Barcelona y el corredor mediterráneo hacen de Catalunya la primera opción para empresas que necesitan instalaciones industriales en el sur de Europa.</p>
        <p>En 2026, la tasa de disponibilidad de naves industriales en el área metropolitana de Barcelona se sitúa por debajo del 4%, lo que refleja una demanda muy superior a la oferta disponible.</p>

        <h2>Tipos de naves industriales en Catalunya</h2>
        <p>Antes de buscar una nave industrial en Catalunya, es importante conocer los diferentes tipos disponibles según el uso:</p>
        <ul>
            <li><strong>Naves logísticas:</strong> Diseñadas para almacenamiento y distribución. Altura libre mínima de 8 metros, múltiples muelles de carga y buena accesibilidad para camiones.</li>
            <li><strong>Naves productivas:</strong> Para fabricación e industria. Requieren alta potencia eléctrica, suelos reforzados y ventilación específica.</li>
            <li><strong>Naves mixtas:</strong> Combinan producción y almacenamiento. Las más habituales en los polígonos industriales de Catalunya.</li>
            <li><strong>Naves frigoríficas:</strong> Con control de temperatura para productos alimentarios o farmacéuticos.</li>
        </ul>

        <h2>Las mejores zonas para naves industriales en Catalunya</h2>
        <p>La ubicación es el factor más importante al elegir una nave industrial en Catalunya. Estas son las principales zonas:</p>
        <ul>
            <li><strong>Corredor del Baix Llobregat:</strong> El Prat, Gavà, Viladecans. Acceso directo al aeropuerto y Puerto de Barcelona. Precios más altos pero máxima conectividad.</li>
            <li><strong>Martorell y Sant Andreu de la Barca:</strong> Gran concentración industrial. Acceso directo a la A-2 y autopistas hacia Madrid.</li>
            <li><strong>Tarragona:</strong> Hub petroquímico e industrial. Puerto propio y precios competitivos.</li>
            <li><strong>Girona:</strong> Crecimiento logístico fuerte. Acceso a Francia y norte de Europa.</li>
            <li><strong>Vic y Manresa:</strong> Precios más competitivos para empresas que no necesitan acceso al puerto.</li>
        </ul>

        <h2>¿Cómo elegir la nave industrial correcta en Catalunya?</h2>
        <p>En Blacknova ayudamos a empresas a encontrar y gestionar la nave industrial perfecta en Catalunya. Nuestro proceso incluye análisis de necesidades, búsqueda de opciones, auditoría técnica previa a la firma y gestión integral del activo.</p>
        <p>Contacta con nosotros para una consulta gratuita en <a href="https://blacknova.es/contacto.html">blacknova.es</a>.</p>
        """,
    },
    {
        "slug": "project-manager-catalunya",
        "titulo": "Project Manager en Catalunya: Cuándo y Por Qué Contratar Uno",
        "descripcion": "Descubre cuándo necesitas un Project Manager en Catalunya, qué hace exactamente y cómo Blacknova gestiona proyectos industriales con metodología PMI.",
        "keywords_principales": ["project manager Catalunya", "gestión proyectos PMI Barcelona"],
        "contenido": """
        <h2>¿Qué es un Project Manager industrial?</h2>
        <p>Un Project Manager industrial es el profesional responsable de planificar, ejecutar y controlar proyectos de construcción, ingeniería o gestión de activos industriales. En Catalunya, la figura del Project Manager es cada vez más demandada por empresas que quieren garantizar el éxito de sus proyectos sin dedicar recursos internos a su gestión.</p>
        <p>En Blacknova, nuestros Project Managers cuentan con certificación PMP y años de experiencia en proyectos industriales en Catalunya y toda Europa.</p>

        <h2>¿Cuándo necesitas un Project Manager externo en Catalunya?</h2>
        <p>Contratar un Project Manager externo en Catalunya tiene sentido cuando:</p>
        <ul>
            <li>Tu proyecto supera los 500.000€ de inversión</li>
            <li>Implica más de 3 proveedores o subcontratas diferentes</li>
            <li>Tienes un plazo de entrega crítico que no puedes incumplir</li>
            <li>Tu equipo interno no tiene experiencia en gestión de proyectos industriales</li>
            <li>El proyecto tiene componentes técnicos complejos</li>
            <li>Necesitas reporting regular para inversores o dirección</li>
        </ul>

        <h2>Metodología PMI aplicada a proyectos industriales en Catalunya</h2>
        <p>En Blacknova aplicamos la metodología PMI (Project Management Institute) en todos nuestros proyectos en Catalunya. Esta metodología internacional garantiza una gestión estructurada en 5 fases: inicio, planificación, ejecución, control y cierre.</p>
        <p>El resultado es proyectos que se entregan en plazo, dentro del presupuesto y con la calidad que el cliente merece.</p>

        <h2>El ROI de contratar un Project Manager en Catalunya</h2>
        <p>Los honorarios de un Project Manager representan entre el 3% y el 8% del presupuesto total del proyecto. En un proyecto de 1 millón de euros, eso son entre 30.000 y 80.000 euros. Sin embargo, los proyectos sin gestión profesional sufren sobrecostes medios del 30-40%, es decir, 300.000-400.000 euros adicionales.</p>
        <p>El ROI de contratar un Project Manager en Catalunya es evidente.</p>

        <h2>Contrata tu Project Manager en Catalunya con Blacknova</h2>
        <p>Primera consulta gratuita y sin compromiso. Contacta con nosotros en <a href="https://blacknova.es/contacto.html">blacknova.es</a>.</p>
        """,
    },
]


def crear_articulo_html(articulo):
    """Genera un archivo HTML completo para el artículo de blog"""
    fecha = datetime.now().strftime("%d de %B de %Y")
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{articulo['titulo']} | Blacknova Blog</title>
<meta name="description" content="{articulo['descripcion']}">
<meta name="keywords" content="{', '.join(articulo['keywords_principales'])}">
<link rel="canonical" href="https://blacknova.es/blog/{articulo['slug']}.html">
<meta property="og:title" content="{articulo['titulo']}">
<meta property="og:description" content="{articulo['descripcion']}">
<meta property="og:url" content="https://blacknova.es/blog/{articulo['slug']}.html">
<meta property="og:type" content="article">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{articulo['titulo']}",
  "description": "{articulo['descripcion']}",
  "author": {{"@type": "Organization", "name": "Blacknova"}},
  "publisher": {{"@type": "Organization", "name": "Blacknova", "url": "https://blacknova.es"}},
  "datePublished": "{datetime.now().strftime('%Y-%m-%d')}",
  "mainEntityOfPage": "https://blacknova.es/blog/{articulo['slug']}.html"
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{--gold:#b8965a;--black:#0d0d0d;--white:#ffffff;--text:#1a1a1a;--muted:#666}}
body{{font-family:'Jost',sans-serif;background:var(--white);color:var(--text);line-height:1.8}}
header{{background:var(--black);padding:20px 48px;display:flex;align-items:center;justify-content:space-between}}
.logo{{color:var(--white);font-size:18px;font-weight:700;letter-spacing:0.2em;text-decoration:none}}
.logo span{{color:var(--gold)}}
nav a{{color:rgba(255,255,255,0.7);text-decoration:none;margin-left:32px;font-size:12px;letter-spacing:0.1em;text-transform:uppercase}}
nav a:hover{{color:var(--white)}}
.article-hero{{background:var(--black);padding:80px 48px 60px;text-align:center}}
.article-category{{color:var(--gold);font-size:12px;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:16px}}
.article-title{{font-family:'Cormorant Garamond',serif;font-size:48px;color:var(--white);line-height:1.2;max-width:800px;margin:0 auto 20px}}
.article-meta{{color:rgba(255,255,255,0.5);font-size:13px}}
.article-body{{max-width:800px;margin:0 auto;padding:60px 24px}}
.article-body h2{{font-family:'Cormorant Garamond',serif;font-size:32px;color:var(--black);margin:48px 0 16px;padding-bottom:8px;border-bottom:1px solid #e2ddd4}}
.article-body p{{font-size:16px;margin-bottom:20px;color:#333;line-height:1.9}}
.article-body ul{{margin:16px 0 24px 24px}}
.article-body li{{margin-bottom:10px;font-size:16px;color:#333}}
.article-body strong{{color:var(--black);font-weight:600}}
.article-body a{{color:var(--gold);text-decoration:none}}
.article-body a:hover{{text-decoration:underline}}
.cta-box{{background:var(--black);color:var(--white);padding:48px;margin:60px 0;text-align:center;border-left:4px solid var(--gold)}}
.cta-box h3{{font-family:'Cormorant Garamond',serif;font-size:28px;margin-bottom:12px}}
.cta-box p{{color:rgba(255,255,255,0.7);margin-bottom:24px}}
.cta-btn{{background:var(--gold);color:var(--black);padding:14px 32px;text-decoration:none;font-weight:600;font-size:13px;letter-spacing:0.1em;text-transform:uppercase}}
footer{{background:var(--black);padding:40px 48px;text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-top:80px}}
footer span{{color:var(--gold)}}
@media(max-width:768px){{header{{padding:16px 24px}}.article-hero{{padding:60px 24px 40px}}.article-title{{font-size:32px}}.article-body{{padding:40px 24px}}}}
</style>
</head>
<body>
<header>
  <a href="https://blacknova.es" class="logo">BLACKNO<span>VA</span></a>
  <nav>
    <a href="https://blacknova.es">Inicio</a>
    <a href="https://blacknova.es/que-hacemos.html">Servicios</a>
    <a href="https://blacknova.es/talentos.html">Talentos</a>
    <a href="https://blacknova.es/contacto.html">Contacto</a>
  </nav>
</header>

<div class="article-hero">
  <div class="article-category">Blog · Gestión de Proyectos · Catalunya</div>
  <h1 class="article-title">{articulo['titulo']}</h1>
  <div class="article-meta">Blacknova · {fecha}</div>
</div>

<div class="article-body">
  {articulo['contenido']}

  <div class="cta-box">
    <h3>¿Necesitas gestión profesional en Catalunya?</h3>
    <p>Primera consulta gratuita y sin compromiso. Analizamos tu proyecto o activo en 45 minutos.</p>
    <a href="https://blacknova.es/contacto.html" class="cta-btn">Contactar con Blacknova →</a>
  </div>
</div>

<footer>
  <p><span>BLACKNOVA</span> · Gestión de proyectos y activos inmobiliarios en Catalunya · <a href="https://blacknova.es" style="color:var(--gold)">blacknova.es</a></p>
  <p style="margin-top:8px">© {datetime.now().year} Blacknova · Todos los derechos reservados</p>
</footer>
</body>
</html>"""
    return html


def auditar_pagina(url):
    resultado = {"url": url, "errores": [], "avisos": [], "ok": [], "keywords_ok": [], "keywords_faltantes": []}
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        resultado["tiempo"] = round(r.elapsed.total_seconds(), 2)
        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("title")
        if not title or not title.text.strip():
            resultado["errores"].append("Sin title")
        else:
            t = title.text.strip()
            resultado["title"] = t
            if len(t) < 30:
                resultado["avisos"].append(f"Title corto ({len(t)} chars)")
            elif len(t) > 60:
                resultado["avisos"].append(f"Title largo ({len(t)} chars)")
            else:
                resultado["ok"].append(f"Title OK ({len(t)} chars)")

        meta = soup.find("meta", attrs={"name": "description"})
        if not meta or not meta.get("content", "").strip():
            resultado["errores"].append("Sin meta description")
        else:
            m = meta["content"].strip()
            if len(m) < 120:
                resultado["avisos"].append(f"Meta description corta ({len(m)} chars)")
            elif len(m) > 160:
                resultado["avisos"].append(f"Meta description larga ({len(m)} chars)")
            else:
                resultado["ok"].append(f"Meta description OK ({len(m)} chars)")

        h1s = soup.find_all("h1")
        if not h1s:
            resultado["errores"].append("Sin H1")
        elif len(h1s) > 1:
            resultado["avisos"].append(f"Múltiples H1 ({len(h1s)})")
        else:
            resultado["ok"].append("H1 correcto")

        texto = soup.get_text().lower()
        for kw in KEYWORDS:
            if kw.lower() in texto:
                resultado["keywords_ok"].append(kw)
            else:
                resultado["keywords_faltantes"].append(kw)

        imgs_sin_alt = [i for i in soup.find_all("img") if not i.get("alt", "").strip()]
        if imgs_sin_alt:
            resultado["avisos"].append(f"{len(imgs_sin_alt)} imágenes sin alt")

        if resultado["tiempo"] > 3:
            resultado["avisos"].append(f"Carga lenta: {resultado['tiempo']}s")
        else:
            resultado["ok"].append(f"Velocidad OK: {resultado['tiempo']}s")

    except Exception as e:
        resultado["errores"].append(f"Error: {str(e)}")
    return resultado


def calcular_puntuacion(r):
    puntos = 100
    puntos -= len(r.get("errores", [])) * 20
    puntos -= len(r.get("avisos", [])) * 5
    puntos += len(r.get("keywords_ok", [])) * 2
    return max(0, min(100, puntos))


def generar_informe_seo(resultados):
    fecha = datetime.now().strftime("%Y%m%d_%H%M")
    nombre = f"{OUTPUT_DIR}/seo_informe_{fecha}.txt"

    puntuacion_media = round(sum(calcular_puntuacion(r) for r in resultados) / len(resultados))
    total_errores = sum(len(r["errores"]) for r in resultados)
    total_avisos = sum(len(r["avisos"]) for r in resultados)

    with open(nombre, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"BLACKNOVA — INFORME SEO AUTOMÁTICO\n")
        f.write(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"RESUMEN EJECUTIVO:\n")
        f.write(f"  Puntuación media: {puntuacion_media}/100\n")
        f.write(f"  Errores críticos: {total_errores}\n")
        f.write(f"  Avisos: {total_avisos}\n\n")

        for r in resultados:
            nombre_pag = r["url"].split("/")[-1] or "index"
            punt = calcular_puntuacion(r)
            f.write(f"{'─'*50}\n")
            f.write(f"{nombre_pag} — {punt}/100\n")
            for e in r["errores"]:
                f.write(f"  ✗ {e}\n")
            for a in r["avisos"]:
                f.write(f"  ⚠ {a}\n")
            for o in r["ok"]:
                f.write(f"  ✓ {o}\n")
            if r["keywords_faltantes"]:
                f.write(f"  → Keywords a añadir: {', '.join(r['keywords_faltantes'][:3])}\n")
            f.write("\n")

        f.write("=" * 60 + "\n")
        f.write("ACCIONES PRIORITARIAS:\n")
        f.write("─" * 40 + "\n")

        todas_faltantes = {}
        for r in resultados:
            for kw in r["keywords_faltantes"]:
                todas_faltantes[kw] = todas_faltantes.get(kw, 0) + 1
        top_kw = sorted(todas_faltantes.items(), key=lambda x: x[1], reverse=True)[:5]

        f.write("1. Keywords más ausentes en la web:\n")
        for kw, count in top_kw:
            f.write(f"   → '{kw}' falta en {count} páginas\n")
        f.write("\n2. Artículos de blog generados para mejorar keywords:\n")
        for art in ARTICULOS_BLOG:
            f.write(f"   → blog/{art['slug']}.html\n")
        f.write("\n3. Sube los artículos del blog a Netlify para indexación inmediata\n")
        f.write("4. Registra cada artículo en Google Search Console\n")
        f.write("5. Comparte cada artículo en LinkedIn e Instagram\n")

    return nombre, puntuacion_media


def ejecutar_auditoria_completa():
    print("=" * 60)
    print("BLACKNOVA — Sistema SEO Automático")
    print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 60)

    # 1. Auditoría SEO
    print("\n🔍 Auditando páginas de blacknova.es...")
    resultados = []
    for url in PAGINAS:
        nombre = url.split("/")[-1] or "index"
        print(f"   {nombre}...", end=" ", flush=True)
        r = auditar_pagina(url)
        punt = calcular_puntuacion(r)
        print(f"{'✅' if punt >= 80 else '⚠️' if punt >= 60 else '❌'} {punt}/100")
        resultados.append(r)
        time.sleep(0.5)

    # 2. Informe SEO
    print("\n📊 Generando informe SEO...")
    informe, puntuacion_media = generar_informe_seo(resultados)
    print(f"   ✅ {informe}")
    print(f"   Puntuación media: {puntuacion_media}/100")

    # 3. Artículos de blog
    print("\n✍️  Generando artículos de blog SEO...")
    blog_dir = os.path.join(BLOG_DIR)
    os.makedirs(blog_dir, exist_ok=True)
    for art in ARTICULOS_BLOG:
        html = crear_articulo_html(art)
        ruta = os.path.join(blog_dir, f"{art['slug']}.html")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"   ✅ {art['slug']}.html")

    # 4. Resumen final
    print("\n" + "=" * 60)
    print("RESUMEN:")
    print(f"  Puntuación SEO actual: {puntuacion_media}/100")
    print(f"  Artículos de blog generados: {len(ARTICULOS_BLOG)}")
    print(f"  Informe guardado en: {informe}")
    print()
    print("PRÓXIMOS PASOS:")
    print("  1. Copia la carpeta 'blog_articles' a tu carpeta blacknova-marketing")
    print("  2. Haz git add + commit + push para publicar en Netlify")
    print("  3. Registra las URLs del blog en Google Search Console")
    print("  4. Comparte los artículos en LinkedIn e Instagram")
    print("  5. Ejecuta este script cada semana para monitorizar la evolución")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_auditoria_completa()
