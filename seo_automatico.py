import requests
from bs4 import BeautifulSoup
import json
import os
import time
import hashlib
from datetime import datetime

# CONFIGURACION
WEB = "https://blacknova.es"
KEYWORDS = [
    "alquiler trasteros Barcelona",
    "trasteros Barcelona precio",
    "trastero empresa Barcelona",
    "almacenamiento flexible Barcelona",
    "rentabilizar nave industrial",
    "gestion nave industrial propietario",
    "alquilar nave industrial Barcelona",
    "gestion activos inmobiliarios",
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
GA_ID = "G-DTP5WXLB81"

ARTICULOS_BLOG = [
    # ─── TRASTEROS ───────────────────────────────────────────
    {
        "slug": "alquiler-trasteros-barcelona-guia",
        "titulo": "Alquiler de Trasteros en Barcelona: Guia Completa 2026",
        "descripcion": "Todo lo que necesitas saber para alquilar un trastero en Barcelona. Precios, zonas, que mirar antes de firmar y como Blacknova te ayuda a encontrar el espacio perfecto.",
        "keywords_principales": ["alquiler trasteros Barcelona", "trasteros Barcelona precio"],
        "h1": "Alquiler de Trasteros en Barcelona: Guia Completa",
        "intro": "Alquilar un trastero en Barcelona es una de las soluciones mas practicas para ganar espacio en casa o en la empresa. Con los pisos cada vez mas pequenos y el precio del metro cuadrado al alza, los trasteros se han convertido en una necesidad real para miles de familias y empresas en el area metropolitana de Barcelona. En Blacknova gestionamos trasteros en Barcelona con contratos flexibles y trato directo.",
        "secciones": [
            {
                "titulo": "Cuanto cuesta alquilar un trastero en Barcelona",
                "texto": "El precio de un trastero en Barcelona depende principalmente de la ubicacion, el tamano y las instalaciones del edificio. En el area metropolitana de Barcelona los precios oscilan entre 40€ y 150€ al mes segun el tamano. Un trastero pequeno de 3-5 m2 cuesta entre 40€ y 70€ al mes. Un trastero mediano de 6-10 m2 oscila entre 70€ y 120€ mensuales. Los trasteros grandes de mas de 10 m2 pueden superar los 120€ al mes. En Blacknova ofrecemos trasteros con precios competitivos y contratos flexibles sin permanencia minima."
            },
            {
                "titulo": "Que mirar antes de alquilar un trastero en Barcelona",
                "lista": [
                    "Acceso y horario: verifica si puedes acceder las 24 horas o solo en horario comercial.",
                    "Seguridad: alarma, camaras de vigilancia y cerradura individual son imprescindibles.",
                    "Condiciones de humedad: un trastero humedo puede danar lo que almacenas.",
                    "Contrato: revisa el plazo minimo, las condiciones de salida y quien se hace cargo del mantenimiento.",
                    "Tamano real: mide bien lo que necesitas antes de contratar. Es mejor ir un poco mas grande.",
                ]
            },
            {
                "titulo": "Trasteros para empresas en Barcelona",
                "texto": "Las empresas tambien alquilan trasteros en Barcelona para almacenar material de oficina, stock de producto, archivo documental o equipamiento temporal durante reformas. Blacknova ofrece trasteros adaptados a las necesidades de empresas: factura, contratos anuales con opcion de renovacion y trato directo sin intermediarios."
            }
        ],
        "cta": "Si buscas trastero en Barcelona, contacta con Blacknova. Primera consulta gratuita y sin compromiso en gestion@blacknova.es"
    },
    {
        "slug": "cuanto-cuesta-trastero-barcelona",
        "titulo": "Cuanto Cuesta un Trastero en Barcelona en 2026",
        "descripcion": "Precios reales de trasteros en Barcelona por zonas y tamanos. Descubre cuanto cuesta alquilar un trastero en el area metropolitana de Barcelona y que factores influyen en el precio.",
        "keywords_principales": ["trasteros Barcelona precio", "alquiler trasteros Barcelona"],
        "h1": "Cuanto Cuesta un Trastero en Barcelona",
        "intro": "El precio de un trastero en Barcelona varia mucho segun la zona, el tamano y las instalaciones. En este articulo te damos los precios reales del mercado en 2026 para que puedas comparar y tomar la mejor decision.",
        "secciones": [
            {
                "titulo": "Precios de trasteros en Barcelona por tamano",
                "lista": [
                    "Trastero mini (1-3 m2): entre 30€ y 50€ al mes. Ideal para maletas, bicicletas o cajas de documentos.",
                    "Trastero pequeno (3-6 m2): entre 50€ y 80€ al mes. El mas demandado para uso particular.",
                    "Trastero mediano (6-12 m2): entre 80€ y 130€ al mes. Perfecto para muebles o stock de empresa.",
                    "Trastero grande (mas de 12 m2): desde 130€ al mes. Para empresas con necesidades de almacenaje importantes.",
                ]
            },
            {
                "titulo": "Factores que influyen en el precio",
                "lista": [
                    "Ubicacion: los trasteros en zonas centrales de Barcelona son mas caros que en el area metropolitana.",
                    "Acceso 24 horas: los trasteros con acceso ilimitado tienen un coste mayor.",
                    "Seguridad: alarma individual, vigilancia y CCTV incrementan el precio pero dan tranquilidad.",
                    "Condiciones del edificio: climatizacion, ascensor de carga y buena iluminacion justifican precios mas altos.",
                    "Flexibilidad del contrato: contratos sin permanencia minima suelen ser algo mas caros pero mas convenientes.",
                ]
            },
            {
                "titulo": "Como ahorrar en el alquiler de un trastero",
                "texto": "Para obtener el mejor precio en un trastero en Barcelona te recomendamos comparar varias opciones, negociar el precio si vas a firmar un contrato largo, y considerar zonas del area metropolitana como L'Hospitalet, Cornella o Sant Boi donde los precios son mas competitivos que en la ciudad. En Blacknova ofrecemos precios transparentes sin costes ocultos."
            }
        ],
        "cta": "Consulta disponibilidad y precios de trasteros en Barcelona contactando con Blacknova en gestion@blacknova.es. Primera consulta gratuita."
    },
    {
        "slug": "trasteros-para-empresas-barcelona",
        "titulo": "Trasteros para Empresas en Barcelona: Almacenamiento Flexible",
        "descripcion": "Soluciones de almacenamiento flexible para empresas en Barcelona. Trasteros con contrato, factura y trato profesional para pymes, e-commerce y autónomos en el area metropolitana.",
        "keywords_principales": ["trastero empresa Barcelona", "almacenamiento flexible Barcelona"],
        "h1": "Trasteros para Empresas en Barcelona",
        "intro": "Cada vez mas empresas en Barcelona alquilan trasteros para resolver necesidades puntuales o continuas de almacenamiento. Stock de producto, archivo documental, material de oficina, equipamiento durante reformas... Un trastero bien gestionado es una solucion practica y economica para empresas que no quieren pagar el precio de una nave industrial para pequeñas necesidades de espacio.",
        "secciones": [
            {
                "titulo": "Que tipo de empresas alquilan trasteros en Barcelona",
                "lista": [
                    "E-commerce y tiendas online: necesitan almacenar stock sin pagar el coste de una nave industrial.",
                    "Autonomos y profesionales: guardan herramientas, muestras o material de trabajo.",
                    "Empresas en reforma: almacenan mobiliario y equipamiento durante la renovacion de oficinas.",
                    "Startups y pymes: archivo documental fisico y material de marketing.",
                    "Empresas de eventos: almacenamiento de material entre eventos.",
                ]
            },
            {
                "titulo": "Ventajas de alquilar trastero en lugar de nave industrial",
                "lista": [
                    "Precio mucho mas bajo: desde 50€ al mes frente a los 800-2000€ de una nave.",
                    "Contratos mas flexibles: sin las exigencias de una nave industrial.",
                    "Sin obras ni adaptaciones: el trastero esta listo para usar desde el primer dia.",
                    "Factura mensual: deducible como gasto de empresa.",
                    "Escalabilidad: puedes ampliar o reducir espacio segun tus necesidades.",
                ]
            },
            {
                "titulo": "Que ofrece Blacknova para empresas",
                "texto": "En Blacknova gestionamos trasteros en Barcelona especialmente adaptados para empresas: factura mensual, contratos flexibles con opcion de renovacion anual, acceso comodo y seguridad garantizada. Trato directo con el equipo gestor sin intermediarios ni burocracia innecesaria."
            }
        ],
        "cta": "Si tu empresa necesita espacio de almacenamiento en Barcelona, contacta con Blacknova. Primera consulta gratuita en gestion@blacknova.es"
    },
    {
        "slug": "como-elegir-trastero-barcelona",
        "titulo": "Como Elegir el Trastero Perfecto en Barcelona: Guia Practica",
        "descripcion": "Guia practica para elegir el trastero adecuado en Barcelona. Tamano, ubicacion, seguridad, precio y contrato: todo lo que debes revisar antes de firmar.",
        "keywords_principales": ["alquiler trasteros Barcelona", "trasteros Barcelona precio"],
        "h1": "Como Elegir el Trastero Perfecto en Barcelona",
        "intro": "Elegir un trastero en Barcelona sin pensarlo bien puede costarte caro. Un trastero demasiado pequeno, mal ubicado o con condiciones de humedad puede convertirse en un problema en lugar de una solucion. En esta guia te explicamos paso a paso como elegir el trastero perfecto para tus necesidades.",
        "secciones": [
            {
                "titulo": "Paso 1: Define cuanto espacio necesitas realmente",
                "texto": "Antes de buscar trastero, haz una lista de todo lo que quieres almacenar y calcula el volumen aproximado. Recuerda que en un trastero puedes apilar en altura, lo que multiplica el espacio util. Como regla general: para cajas y objetos pequenos con 3-5 m2 es suficiente. Para muebles o stock de empresa necesitaras entre 6 y 12 m2."
            },
            {
                "titulo": "Paso 2: Elige bien la ubicacion",
                "lista": [
                    "Cerca de tu casa o empresa: reduciras el tiempo y coste de cada visita.",
                    "Con buen acceso en coche o furgoneta: fundamental si vas a llevar muebles o cajas grandes.",
                    "En zona segura: el precio mas bajo no vale si el entorno no te da confianza.",
                ]
            },
            {
                "titulo": "Paso 3: Revisa las condiciones del contrato",
                "lista": [
                    "Plazo minimo: idealmente sin permanencia o con un mes minimo.",
                    "Preaviso de salida: cuantos dias debes avisar antes de dejar el trastero.",
                    "Fianza: lo habitual es un mes de fianza.",
                    "Que incluye el precio: si hay gastos de comunidad o seguros adicionales.",
                    "Condiciones de renovacion: si el precio puede subir y con cuanta antelacion te avisan.",
                ]
            },
            {
                "titulo": "Paso 4: Comprueba la seguridad",
                "texto": "Un buen trastero debe tener cerradura individual, sistema de alarma, camaras de vigilancia en zonas comunes e iluminacion adecuada. Visita siempre el trastero antes de firmar para comprobar el estado real del espacio y las instalaciones."
            }
        ],
        "cta": "En Blacknova te ayudamos a encontrar el trastero adecuado en Barcelona. Contacta con nosotros en gestion@blacknova.es para una primera consulta gratuita."
    },
    # ─── NAVES INDUSTRIALES ──────────────────────────────────
    {
        "slug": "rentabilizar-nave-industrial",
        "titulo": "Como Rentabilizar tu Nave Industrial: Guia para Propietarios 2026",
        "descripcion": "Descubre como maximizar el rendimiento de tu nave industrial como propietario. Gestion profesional, estrategias de alquiler y optimizacion de activos industriales en Barcelona.",
        "keywords_principales": ["rentabilizar nave industrial", "gestion nave industrial propietario"],
        "h1": "Como Rentabilizar tu Nave Industrial",
        "intro": "Muchos propietarios de naves industriales en Barcelona dejan dinero sobre la mesa cada mes. Ya sea por tener la nave vacia mas tiempo del necesario, por no negociar correctamente los contratos de arrendamiento, o por no gestionar el mantenimiento de forma eficiente. En Blacknova ayudamos a propietarios a rentabilizar su nave industrial de forma profesional.",
        "secciones": [
            {
                "titulo": "5 estrategias para rentabilizar tu nave industrial",
                "lista": [
                    "Gestion profesional del arrendamiento: Un gestor profesional encuentra inquilinos solventes mas rapido y reduce los periodos de vacio.",
                    "Mantenimiento preventivo: Una nave bien mantenida atrae mejores inquilinos y se puede arrendar a precios mas altos.",
                    "Optimizacion energetica: Instalar paneles solares e iluminacion LED puede reducir costes operativos hasta un 40%.",
                    "Revision periodica de rentas: El mercado industrial en Barcelona esta al alza. Sin revisiones anuales, pierdes rentabilidad.",
                    "Auditoria tecnica y legal: Verificar que la nave cumple toda la normativa evita multas y problemas con inquilinos.",
                ]
            },
            {
                "titulo": "Cuanto puede ganar un propietario de nave industrial en Barcelona",
                "texto": "Una nave industrial bien ubicada en el area metropolitana de Barcelona puede generar entre 6.000 y 15.000 euros mensuales de renta segun la superficie. Con gestion profesional que minimice periodos de vacio y optimice condiciones de arrendamiento, la rentabilidad anual puede superar el 7%."
            }
        ],
        "cta": "En Blacknova nos encargamos de todo: busqueda de inquilinos, contratos, mantenimiento y reporting mensual. Primera consulta gratuita en gestion@blacknova.es"
    },
    {
        "slug": "alquiler-naves-industriales-barcelona",
        "titulo": "Alquiler de Naves Industriales en Barcelona: Guia 2026",
        "descripcion": "Guia completa para alquilar una nave industrial en Barcelona. Zonas, precios, que revisar antes de firmar y como Blacknova te acompana en todo el proceso.",
        "keywords_principales": ["alquilar nave industrial Barcelona", "naves industriales Barcelona"],
        "h1": "Alquiler de Naves Industriales en Barcelona",
        "intro": "Barcelona y su area metropolitana concentran una de las mayores demandas de espacio industrial de Espana. El crecimiento del e-commerce, la logistica y la industria manufacturera han disparado la busqueda de naves industriales bien ubicadas. En Blacknova acompanamos a empresas en todo el proceso de busqueda y alquiler de naves industriales en Barcelona.",
        "secciones": [
            {
                "titulo": "Mejores zonas para alquilar nave industrial en Barcelona",
                "lista": [
                    "Baix Llobregat: acceso directo al aeropuerto y Puerto de Barcelona. La zona mas demandada para logistica.",
                    "Martorell y Sant Andreu de la Barca: acceso a la A-2 y autopistas hacia Madrid. Gran concentracion industrial.",
                    "Zona Franca: ubicacion estrategica en Barcelona ciudad. Ideal para empresas que necesitan estar cerca del centro.",
                    "Sant Boi y Cornella: precios mas competitivos con buena conectividad.",
                    "Granollers y Montmelo: acceso al corredor del Valles. Zona en crecimiento.",
                ]
            },
            {
                "titulo": "Que revisar antes de firmar el contrato de una nave industrial",
                "lista": [
                    "Altura libre interior: minimo 6 metros para uso industrial, 8 metros para logistica.",
                    "Acceso de camiones: comprueba el radio de giro y los muelles de carga disponibles.",
                    "Potencia electrica: muchas naves no tienen suficiente para maquinaria industrial pesada.",
                    "Licencia de actividad: verifica que tu actividad esta permitida en esa nave.",
                    "Estado de la cubierta: una cubierta en mal estado puede generar problemas desde el primer dia.",
                ]
            }
        ],
        "cta": "Si buscas nave industrial en Barcelona, contacta con Blacknova. Primera consulta gratuita y sin compromiso en gestion@blacknova.es"
    },
]


def crear_articulo_html(articulo):
    fecha = datetime.now().strftime("%d de %B de %Y")

    secciones_html = ""
    for seccion in articulo.get("secciones", []):
        secciones_html += f"<h2>{seccion['titulo']}</h2>"
        if "lista" in seccion:
            secciones_html += "<ul>"
            for item in seccion["lista"]:
                partes = item.split(":", 1)
                if len(partes) == 2:
                    secciones_html += f"<li><strong>{partes[0]}:</strong>{partes[1]}</li>"
                else:
                    secciones_html += f"<li>{item}</li>"
            secciones_html += "</ul>"
        if "texto" in seccion:
            secciones_html += f"<p>{seccion['texto']}</p>"

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{articulo['titulo']} | Blacknova</title>
<meta name="description" content="{articulo['descripcion']}">
<link rel="canonical" href="https://blacknova.es/blog_articles/{articulo['slug']}.html">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{articulo['titulo']}",
  "description": "{articulo['descripcion']}",
  "author": {{"@type": "Organization", "name": "Blacknova"}},
  "publisher": {{"@type": "Organization", "name": "Blacknova", "url": "https://blacknova.es"}},
  "datePublished": "{datetime.now().strftime('%Y-%m-%d')}"
}}
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
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
.hero{{background:var(--black);padding:80px 48px 60px;text-align:center}}
.cat{{color:var(--gold);font-size:12px;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:16px}}
h1{{font-family:'Cormorant Garamond',serif;font-size:48px;color:var(--white);line-height:1.2;max-width:800px;margin:0 auto 20px}}
.meta{{color:rgba(255,255,255,0.5);font-size:13px}}
.body{{max-width:800px;margin:0 auto;padding:60px 24px}}
.body h2{{font-family:'Cormorant Garamond',serif;font-size:32px;color:var(--black);margin:48px 0 16px;padding-bottom:8px;border-bottom:1px solid #e2ddd4}}
.body p{{font-size:16px;margin-bottom:20px;color:#333;line-height:1.9}}
.body ul{{margin:16px 0 24px 24px}}
.body li{{margin-bottom:10px;font-size:16px;color:#333}}
.body strong{{color:var(--black);font-weight:600}}
.body a{{color:var(--gold);text-decoration:none}}
.cta{{background:var(--black);color:var(--white);padding:48px;margin:60px 0;text-align:center;border-left:4px solid var(--gold)}}
.cta h3{{font-family:'Cormorant Garamond',serif;font-size:28px;margin-bottom:12px}}
.cta p{{color:rgba(255,255,255,0.7);margin-bottom:24px}}
.cta a{{background:var(--gold);color:var(--black);padding:14px 32px;text-decoration:none;font-weight:600;font-size:13px;letter-spacing:0.1em;text-transform:uppercase;display:inline-block}}
footer{{background:var(--black);padding:40px 48px;text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-top:80px}}
footer span{{color:var(--gold)}}
@media(max-width:768px){{header{{padding:16px 24px}}h1{{font-size:32px}}.hero{{padding:60px 24px 40px}}.body{{padding:40px 24px}}}}
</style>
</head>
<body>
<header>
  <a href="https://blacknova.es" class="logo">BLACKNO<span>VA</span></a>
  <nav>
    <a href="https://blacknova.es">Inicio</a>
    <a href="https://blacknova.es/que-hacemos.html">Servicios</a>
    <a href="https://blacknova.es/blog.html">Blog</a>
    <a href="https://blacknova.es/contacto.html">Contacto</a>
  </nav>
</header>
<div class="hero">
  <div class="cat">Blog · Blacknova · Barcelona</div>
  <h1>{articulo['h1']}</h1>
  <div class="meta">Blacknova · {fecha}</div>
</div>
<div class="body">
  <p>{articulo['intro']}</p>
  {secciones_html}
  <div class="cta">
    <h3>Podemos ayudarte</h3>
    <p>{articulo['cta']}</p>
    <a href="https://blacknova.es/contacto.html">Contactar con Blacknova</a>
  </div>
</div>
<footer>
  <p><span>BLACKNOVA</span> · Trasteros y naves industriales en Barcelona · <a href="https://blacknova.es" style="color:var(--gold)">blacknova.es</a></p>
  <p style="margin-top:8px">{datetime.now().year} Blacknova · Todos los derechos reservados</p>
</footer>
</body>
</html>"""
    return html


def extraer_texto_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
    texto = soup.get_text(separator=" ")
    return " ".join(texto.split())


def verificar_originalidad(texto, titulo):
    print(f"      Verificando originalidad...", end=" ", flush=True)
    palabras = texto.split()
    coincidencias = 0
    total = 0
    for i in range(0, min(len(palabras), 300), 100):
        fragmento = " ".join(palabras[i:i+15])
        try:
            url = f"https://api.duckduckgo.com/?q=%22{requests.utils.quote(fragmento)}%22&format=json&no_html=1"
            r = requests.get(url, timeout=10, headers=HEADERS)
            if r.status_code == 200:
                data = r.json()
                if data.get("RelatedTopics") or data.get("AbstractURL"):
                    coincidencias += 1
            total += 1
            time.sleep(1)
        except:
            total += 1
    porcentaje = max(0, 100 - (coincidencias / max(total, 1)) * 100)
    hash_id = hashlib.md5(texto.encode()).hexdigest()[:8]
    if porcentaje >= 70:
        print(f"OK {porcentaje:.0f}% original")
        return True, porcentaje, hash_id
    else:
        print(f"AVISO {porcentaje:.0f}% original")
        return False, porcentaje, hash_id


def guardar_registro_copyright(articulos):
    ruta = os.path.join(OUTPUT_DIR, "copyright_registro.json")
    registro = []
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                registro = json.load(f)
        except:
            pass
    for art in articulos:
        registro.append({
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "articulo": art["slug"],
            "originalidad": art["originalidad"],
            "hash": art["hash"],
            "publicado": art["publicado"]
        })
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(registro, f, ensure_ascii=False, indent=2)


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
            resultado["avisos"].append(f"Multiples H1 ({len(h1s)})")
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
            resultado["avisos"].append(f"{len(imgs_sin_alt)} imagenes sin alt")
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
        f.write("BLACKNOVA — INFORME SEO\n")
        f.write(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
        f.write(f"Puntuacion media: {puntuacion_media}/100\n")
        f.write(f"Errores criticos: {total_errores}\n")
        f.write(f"Avisos: {total_avisos}\n\n")
        for r in resultados:
            nombre_pag = r["url"].split("/")[-1] or "index"
            punt = calcular_puntuacion(r)
            f.write(f"{nombre_pag} — {punt}/100\n")
            for e in r["errores"]:
                f.write(f"  ERROR: {e}\n")
            for a in r["avisos"]:
                f.write(f"  AVISO: {a}\n")
            if r["keywords_faltantes"]:
                f.write(f"  Keywords a anadir: {', '.join(r['keywords_faltantes'][:3])}\n")
            f.write("\n")
    return nombre, puntuacion_media


if __name__ == "__main__":
    print("=" * 60)
    print("BLACKNOVA — Sistema SEO Automatico")
    print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("=" * 60)

    print("\nAuditando paginas...")
    resultados = []
    for url in PAGINAS:
        nombre = url.split("/")[-1] or "index"
        print(f"   {nombre}...", end=" ", flush=True)
        r = auditar_pagina(url)
        punt = calcular_puntuacion(r)
        print(f"{'OK' if punt >= 80 else 'AVISO'} {punt}/100")
        resultados.append(r)
        time.sleep(0.5)

    print("\nGenerando informe...")
    informe, puntuacion_media = generar_informe_seo(resultados)
    print(f"   OK {informe} — Puntuacion: {puntuacion_media}/100")

    print("\nGenerando articulos de blog...")
    articulos_verificados = []
    for art in ARTICULOS_BLOG:
        print(f"   {art['slug']}.html")
        html = crear_articulo_html(art)
        texto = extraer_texto_html(html)
        es_original, porcentaje, hash_id = verificar_originalidad(texto, art["titulo"])
        ruta = os.path.join(BLOG_DIR, f"{art['slug']}.html")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(html)
        articulos_verificados.append({
            "slug": art["slug"],
            "originalidad": porcentaje,
            "hash": hash_id,
            "publicado": True
        })

    guardar_registro_copyright(articulos_verificados)

    print("\n" + "=" * 60)
    print(f"Puntuacion SEO: {puntuacion_media}/100")
    print(f"Articulos generados: {len(ARTICULOS_BLOG)}")
    print("\nPROXIMO PASO:")
    print("  git add blog_articles/*.html && git commit -m 'Blog actualizado' && git push")
    print("=" * 60)
