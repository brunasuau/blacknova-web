import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm
import time

# ─── CONFIGURACIÓN ───────────────────────────────────────────
PAGINAS = [
    "https://blacknova.es/",
    "https://blacknova.es/sobre-nosotros.html",
    "https://blacknova.es/que-hacemos.html",
    "https://blacknova.es/talentos.html",
    "https://blacknova.es/me-siento-talento.html",
    "https://blacknova.es/busco-talento.html",
    "https://blacknova.es/contacto.html",
]

KEYWORDS_OBJETIVO = [
    "gestión activos inmobiliarios",
    "naves industriales Catalunya",
    "project manager Catalunya",
    "gestión proyectos PMI",
    "selección talento ingeniería",
    "construcción industrial Barcelona",
]

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
# ─────────────────────────────────────────────────────────────


def analizar_pagina(url):
    resultado = {"url": url, "errores": [], "avisos": [], "ok": []}
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        resultado["status"] = r.status_code
        resultado["tiempo_carga"] = round(r.elapsed.total_seconds(), 2)
        soup = BeautifulSoup(r.text, "html.parser")

        # Título
        title = soup.find("title")
        if not title or not title.text.strip():
            resultado["errores"].append("Sin etiqueta <title>")
            resultado["title"] = "—"
        else:
            t = title.text.strip()
            resultado["title"] = t
            if len(t) < 30:
                resultado["avisos"].append(f"Título muy corto ({len(t)} chars) — mínimo 30")
            elif len(t) > 60:
                resultado["avisos"].append(f"Título muy largo ({len(t)} chars) — máximo 60")
            else:
                resultado["ok"].append(f"Título correcto ({len(t)} chars)")

        # Meta descripción
        meta = soup.find("meta", attrs={"name": "description"})
        if not meta or not meta.get("content", "").strip():
            resultado["errores"].append("Sin meta descripción")
            resultado["meta_desc"] = "—"
        else:
            m = meta["content"].strip()
            resultado["meta_desc"] = m
            if len(m) < 120:
                resultado["avisos"].append(f"Meta descripción corta ({len(m)} chars) — mínimo 120")
            elif len(m) > 160:
                resultado["avisos"].append(f"Meta descripción larga ({len(m)} chars) — máximo 160")
            else:
                resultado["ok"].append(f"Meta descripción correcta ({len(m)} chars)")

        # H1
        h1s = soup.find_all("h1")
        if not h1s:
            resultado["errores"].append("Sin etiqueta H1")
        elif len(h1s) > 1:
            resultado["avisos"].append(f"Múltiples H1 ({len(h1s)}) — debe haber solo uno")
        else:
            resultado["ok"].append(f"H1 correcto: '{h1s[0].get_text(strip=True)[:50]}'")

        # H2
        h2s = soup.find_all("h2")
        resultado["ok"].append(f"{len(h2s)} etiquetas H2 encontradas")

        # Keywords en contenido
        texto_completo = soup.get_text().lower()
        kw_encontradas = []
        kw_faltantes = []
        for kw in KEYWORDS_OBJETIVO:
            if kw.lower() in texto_completo:
                kw_encontradas.append(kw)
            else:
                kw_faltantes.append(kw)
        resultado["keywords_ok"] = kw_encontradas
        resultado["keywords_faltantes"] = kw_faltantes
        if kw_faltantes:
            resultado["avisos"].append(f"Keywords no encontradas: {', '.join(kw_faltantes)}")

        # Imágenes sin alt
        imgs = soup.find_all("img")
        sin_alt = [i for i in imgs if not i.get("alt", "").strip()]
        if sin_alt:
            resultado["avisos"].append(f"{len(sin_alt)} imagen(es) sin atributo alt")
        elif imgs:
            resultado["ok"].append(f"Todas las imágenes ({len(imgs)}) tienen atributo alt")

        # HTTPS
        if url.startswith("https://"):
            resultado["ok"].append("HTTPS activo")
        else:
            resultado["errores"].append("Sin HTTPS — Google penaliza sitios sin SSL")

        # Tiempo de carga
        if resultado["tiempo_carga"] > 3:
            resultado["avisos"].append(f"Carga lenta: {resultado['tiempo_carga']}s — objetivo <3s")
        else:
            resultado["ok"].append(f"Velocidad correcta: {resultado['tiempo_carga']}s")

    except Exception as e:
        resultado["errores"].append(f"Error al acceder: {str(e)}")
        resultado["status"] = 0
        resultado["tiempo_carga"] = 0
        resultado["title"] = "—"
        resultado["meta_desc"] = "—"
        resultado["keywords_ok"] = []
        resultado["keywords_faltantes"] = KEYWORDS_OBJETIVO

    return resultado


def calcular_puntuacion(r):
    puntos = 100
    puntos -= len(r.get("errores", [])) * 20
    puntos -= len(r.get("avisos", [])) * 5
    return max(0, puntos)


def generar_pdf(resultados):
    doc = SimpleDocTemplate(
        "blacknova_seo_informe.pdf",
        pagesize=A4,
        topMargin=2*cm,
        bottomMargin=2*cm,
        leftMargin=2*cm,
        rightMargin=2*cm,
    )
    styles = getSampleStyleSheet()
    story = []

    # Estilos
    titulo_style = ParagraphStyle("titulo", parent=styles["Title"], fontSize=22, textColor=colors.HexColor("#1a1a2e"), spaceAfter=6)
    subtitulo_style = ParagraphStyle("subtitulo", parent=styles["Normal"], fontSize=11, textColor=colors.HexColor("#666666"), spaceAfter=20)
    h2_style = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=14, textColor=colors.HexColor("#1a1a2e"), spaceBefore=16, spaceAfter=8)
    body_style = ParagraphStyle("body", parent=styles["Normal"], fontSize=10, leading=14)
    verde = colors.HexColor("#2d6a4f")
    rojo = colors.HexColor("#c1121f")
    naranja = colors.HexColor("#e85d04")

    # Cabecera
    story.append(Paragraph("Blacknova — Informe SEO", titulo_style))
    story.append(Paragraph(f"Auditoría de {len(resultados)} páginas · Keywords objetivo: Catalunya + activos inmobiliarios", subtitulo_style))

    # Resumen ejecutivo
    total_errores = sum(len(r["errores"]) for r in resultados)
    total_avisos = sum(len(r["avisos"]) for r in resultados)
    puntuacion_media = round(sum(calcular_puntuacion(r) for r in resultados) / len(resultados))

    resumen_data = [
        ["Páginas analizadas", "Errores críticos", "Avisos", "Puntuación media SEO"],
        [str(len(resultados)), str(total_errores), str(total_avisos), f"{puntuacion_media}/100"],
    ]
    t = Table(resumen_data, colWidths=[4*cm, 4*cm, 4*cm, 4*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTSIZE", (0,0), (-1,0), 10),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BACKGROUND", (0,1), (-1,1), colors.HexColor("#f8f9fa")),
        ("FONTSIZE", (0,1), (-1,1), 16),
        ("FONTNAME", (0,1), (-1,1), "Helvetica-Bold"),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.HexColor("#f8f9fa")]),
        ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#dddddd")),
        ("ROWHEIGHT", (0,0), (-1,-1), 28),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))

    # Análisis por página
    story.append(Paragraph("Análisis por página", h2_style))

    for r in resultados:
        nombre = r["url"].split("/")[-1] or "index.html"
        puntuacion = calcular_puntuacion(r)
        color_punt = verde if puntuacion >= 70 else naranja if puntuacion >= 40 else rojo

        page_data = [
            [Paragraph(f"<b>{nombre}</b>", body_style), Paragraph(f"<b><font color='{'#2d6a4f' if puntuacion>=70 else '#e85d04' if puntuacion>=40 else '#c1121f'}'>{puntuacion}/100</font></b>", body_style)],
            [Paragraph(f"Título: {r.get('title','—')[:70]}", body_style), Paragraph(f"Carga: {r.get('tiempo_carga',0)}s", body_style)],
        ]
        pt = Table(page_data, colWidths=[12*cm, 4*cm])
        pt.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#eef2f7")),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#dddddd")),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("ROWHEIGHT", (0,0), (-1,-1), 22),
            ("LEFTPADDING", (0,0), (-1,-1), 8),
        ]))
        story.append(pt)

        # Errores
        for e in r["errores"]:
            story.append(Paragraph(f"<font color='#c1121f'>✗ {e}</font>", body_style))
        for a in r["avisos"]:
            story.append(Paragraph(f"<font color='#e85d04'>⚠ {a}</font>", body_style))
        for o in r["ok"]:
            story.append(Paragraph(f"<font color='#2d6a4f'>✓ {o}</font>", body_style))

        # Keywords
        if r.get("keywords_faltantes"):
            story.append(Paragraph(
                f"<font color='#e85d04'>Keywords a añadir: {', '.join(r['keywords_faltantes'])}</font>",
                body_style
            ))

        story.append(Spacer(1, 12))

    # Recomendaciones
    story.append(Paragraph("Próximos pasos prioritarios", h2_style))
    recomendaciones = [
        "1. Añadir meta descripción a todas las páginas (160 chars máximo, incluir keyword principal)",
        "2. Incluir keywords 'gestión activos inmobiliarios Catalunya' en títulos H1 y H2",
        "3. Optimizar todas las imágenes con atributo alt descriptivo",
        "4. Crear página específica de blog con artículos SEO mensuales",
        "5. Registrar Blacknova en Google Business Profile (local SEO Catalunya)",
        "6. Conseguir backlinks desde asociaciones inmobiliarias y de construcción catalanas",
        "7. Añadir schema markup de organización y servicios para rich results en Google",
    ]
    for rec in recomendaciones:
        story.append(Paragraph(rec, body_style))
        story.append(Spacer(1, 4))

    doc.build(story)
    print("\n✅ Informe generado: blacknova_seo_informe.pdf")
    print("   Ábrelo desde tu carpeta del proyecto.")


# ─── EJECUCIÓN ───────────────────────────────────────────────
if __name__ == "__main__":
    print("🔍 Analizando web de Blacknova...")
    print(f"   {len(PAGINAS)} páginas · {len(KEYWORDS_OBJETIVO)} keywords objetivo\n")

    resultados = []
    for url in PAGINAS:
        print(f"   Analizando: {url.split('/')[-1]}...", end=" ")
        r = analizar_pagina(url)
        puntuacion = calcular_puntuacion(r)
        print(f"{'✅' if puntuacion >= 70 else '⚠️' if puntuacion >= 40 else '❌'} {puntuacion}/100")
        resultados.append(r)
        time.sleep(0.5)

    print("\n📄 Generando informe PDF...")
    generar_pdf(resultados)
