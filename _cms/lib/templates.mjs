// Plantillas HTML de Blacknova — TODO con el sistema de diseño base.css (crema/ámbar),
// para que las páginas de artículo cuadren con blog.html y el resto de la web.
//
// - articlePage(): página de artículo (base.css) => blog_articles/<slug>.html
// - blogIndex():   página blog.html (base.css con tarjetas)
// - sitemap():     sitemap.xml completo (páginas fijas + artículos)
//
// La cabecera, el pie, la cookie banner y el botón de WhatsApp se comparten entre
// ambas páginas (chrome() con `base`), de modo que siempre son idénticos.
//   base = ""    -> enlaces relativos desde la raíz (blog.html)
//   base = "../" -> enlaces desde blog_articles/ (páginas de artículo)

const SITE = "https://blacknova.es";

const MESES = [
  "enero", "febrero", "marzo", "abril", "mayo", "junio",
  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
];

export function fechaLarga(iso) {
  const d = new Date(iso);
  const dia = String(d.getUTCDate()).padStart(2, "0");
  return `${dia} de ${MESES[d.getUTCMonth()]} de ${d.getUTCFullYear()}`;
}

function esc(s = "") {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// --- Chrome compartido (header / mobile-nav / footer / cookie / whatsapp) ----
function header(base, active = "") {
  const on = (k) => (k === active ? " class=\"is-active\"" : "");
  return `<header class="site-header" id="siteHeader">
  <div class="container">
    <a class="logo" href="${base}index.html" aria-label="Blacknova — Inicio">
      <svg viewBox="0 0 100 100" aria-hidden="true"><defs><linearGradient id="navGrad" x1="2" y1="2" x2="98" y2="98" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F0B15C"/><stop offset="0.55" stop-color="#C9822E"/><stop offset="1" stop-color="#8A4A22"/></linearGradient></defs><path d="M50,2 L59.9,40.1 L98,50 L59.9,59.9 L50,98 L40.1,59.9 L2,50 L40.1,40.1 Z" fill="url(#navGrad)"/></svg>
      <span class="logo-word">Black<b>nova</b></span>
    </a>
    <nav class="main-nav" aria-label="Navegación principal">
      <a href="${base}index.html">Inicio</a>
      <a href="${base}que-hacemos.html">Qué hacemos</a>
      <a href="${base}trasteros.html">Trasteros</a>
      <a href="${base}naves.html"${on("naves")}>Naves</a>
      <a href="${base}propietarios.html">Propietarios</a>
      <a href="${base}sobre-nosotros.html">Sobre nosotros</a>
      <a href="${base}blog.html"${on("blog")}>Blog</a>
      <a href="${base}faq.html">FAQ</a>
    </nav>
    <div class="nav-actions">
      <a class="nav-phone" href="tel:+34630879206">📞 630 87 92 06</a>
      <a class="btn btn-gold" href="${base}contacto.html">Consulta gratuita</a>
      <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<nav class="mobile-nav" id="mobileNav" aria-label="Menú móvil">
  <a href="${base}index.html">Inicio</a>
  <a href="${base}que-hacemos.html">Qué hacemos</a>
  <a href="${base}trasteros.html">Trasteros</a>
  <a href="${base}naves.html">Naves</a>
  <a href="${base}propietarios.html">Propietarios</a>
  <a href="${base}sobre-nosotros.html">Sobre nosotros</a>
  <a href="${base}blog.html">Blog</a>
  <a href="${base}faq.html">FAQ</a>
  <a href="${base}contacto.html">Contacto</a>
</nav>`;
}

function cookieBanner(base) {
  return `<div class="cookie-banner" id="cookieBanner" role="dialog" aria-live="polite" aria-label="Aviso de cookies">
  <p>Usamos cookies propias y de terceros para analizar el uso del sitio y mejorar tu experiencia. Puedes aceptarlas, rechazar las no esenciales o consultar nuestra <a href="${base}politica-cookies.html" style="text-decoration:underline">política de cookies</a>.</p>
  <div class="cookie-actions">
    <button class="btn btn-primary" id="cookieAccept">Aceptar todas</button>
    <button class="btn btn-outline" id="cookieReject">Solo esenciales</button>
  </div>
</div>`;
}

function footer(base) {
  return `<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo" href="${base}index.html" style="margin-bottom:18px;">
          <svg viewBox="0 0 100 100" aria-hidden="true" width="30" height="30"><path d="M50,2 L59.9,40.1 L98,50 L59.9,59.9 L50,98 L40.1,59.9 L2,50 L40.1,40.1 Z" fill="#C9822E"/></svg>
          <span class="logo-word">Black<b>nova</b></span>
        </a>
        <p style="font-size:14px; max-width:34ch; margin-top:14px; color:rgba(247,244,238,0.6)">Project management, trasteros e intermediación inmobiliaria en Barcelona y Catalunya.</p>
        <div class="social-row">
          <a href="https://www.instagram.com/blacknova" aria-label="Instagram" target="_blank" rel="noopener">IG</a>
          <a href="https://www.linkedin.com/company/blacknova" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
        </div>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul>
          <li><a href="${base}que-hacemos.html">Project Management</a></li>
          <li><a href="${base}trasteros.html">Trasteros en Calafell</a></li>
          <li><a href="${base}naves.html">Naves industriales</a></li>
          <li><a href="${base}propietarios.html">Intermediación inmobiliaria</a></li>
        </ul>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul>
          <li><a href="${base}sobre-nosotros.html">Sobre nosotros</a></li>
          <li><a href="${base}blog.html">Blog</a></li>
          <li><a href="${base}faq.html">Preguntas frecuentes</a></li>
          <li><a href="${base}contacto.html">Contacto</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="tel:+34630879206">+34 630 87 92 06</a></li>
          <li><a href="mailto:direccion@blacknova.es">direccion@blacknova.es</a></li>
          <li>Sant Sadurní d'Anoia, Barcelona</li>
          <li>Lun–Vie 9:00–19:00</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Blacknova S.L. Todos los derechos reservados.</span>
      <span style="display:flex; gap:18px; flex-wrap:wrap;">
        <a href="${base}aviso-legal.html">Aviso legal</a>
        <a href="${base}politica-privacidad.html">Privacidad</a>
        <a href="${base}politica-cookies.html">Cookies</a>
      </span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/34630879206?text=Hola%20Blacknova%2C%20me%20gustar%C3%ADa%20m%C3%A1s%20informaci%C3%B3n" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">
  <svg viewBox="0 0 24 24"><path d="M17.6 6.32A8.86 8.86 0 0 0 12.05 4C7.5 4 3.83 7.66 3.83 12.2c0 1.44.38 2.85 1.1 4.08L3.75 20.5l4.35-1.14a8.83 8.83 0 0 0 4.2 1.07h0c4.55 0 8.22-3.66 8.22-8.2a8.17 8.17 0 0 0-2.92-5.9Z"/></svg>
</a>

<script src="${base}assets/js/main.js" defer></script>`;
}

const FONTS = `<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Jost:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>`;

// ---------------------------------------------------------------------------
// PÁGINA DE ARTÍCULO  ->  blog_articles/<slug>.html   (diseño base.css)
// ---------------------------------------------------------------------------
export function articlePage(post) {
  const base = "../";
  const url = `${SITE}/blog_articles/${post.slug}.html`;
  const jsonld = {
    "@context": "https://schema.org",
    "@type": "Article",
    headline: post.title,
    description: post.metaDescription,
    author: { "@type": "Organization", name: "Blacknova" },
    publisher: { "@type": "Organization", name: "Blacknova", url: SITE },
    datePublished: post.publishedAt,
  };

  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>${esc(post.title)} | Blacknova</title>
<meta name="description" content="${esc(post.metaDescription)}"/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="${url}"/>
<link rel="icon" href="${base}favicon.svg" type="image/svg+xml"/>

<meta property="og:title" content="${esc(post.title)}"/>
<meta property="og:description" content="${esc(post.metaDescription)}"/>
<meta property="og:url" content="${url}"/>
<meta property="og:type" content="article"/>
<meta property="og:locale" content="es_ES"/>

<script type="application/ld+json">
${JSON.stringify(jsonld, null, 2)}
</script>

${FONTS}
<link rel="stylesheet" href="${base}assets/css/base.css"/>

<style>
.article-hero { position: relative; background: var(--bn-black); color: var(--bn-cream); padding: 168px 0 74px; overflow: hidden; }
.article-hero .nova-glow { width: 560px; height: 560px; top: -220px; right: -160px; }
.article-hero .container { position: relative; z-index: 1; }
.article-hero .cat { color: var(--bn-amber-light); }
.article-hero h1 { font-size: clamp(32px,5vw,52px); color: var(--bn-white); max-width: 20ch; margin: 6px 0 18px; }
.article-hero .meta { font-size: 13.5px; color: rgba(247,244,238,0.55); }
.article-wrap { max-width: 760px; margin: 0 auto; padding: 72px 28px 20px; }
.article-wrap p { font-size: 17px; line-height: 1.85; color: #34343b; margin-bottom: 22px; }
.article-wrap h2 { font-size: clamp(25px,3.4vw,33px); color: var(--bn-ink); margin: 48px 0 16px; padding-bottom: 10px; border-bottom: 1px solid var(--bn-border); }
.article-wrap h3 { font-size: 21px; color: var(--bn-ink); margin: 34px 0 12px; }
.article-wrap ul { margin: 8px 0 26px; }
.article-wrap li { position: relative; padding-left: 26px; margin-bottom: 12px; font-size: 17px; line-height: 1.7; color: #34343b; }
.article-wrap li::before { content: ''; position: absolute; left: 2px; top: 11px; width: 8px; height: 8px; border-radius: 50%; background: var(--bn-amber-grad); }
.article-wrap strong { color: var(--bn-ink); font-weight: 600; }
.article-wrap a { color: var(--bn-amber-dark); text-decoration: underline; text-underline-offset: 3px; }
.article-cta { max-width: 760px; margin: 30px auto 0; padding: 0 28px; }
.article-cta-inner { background: var(--bn-black); color: var(--bn-cream); border-radius: var(--radius-lg); padding: 52px 46px; text-align: center; position: relative; overflow: hidden; }
.article-cta-inner h3 { color: var(--bn-white); font-size: 28px; margin-bottom: 12px; }
.article-cta-inner p { color: rgba(247,244,238,0.72); margin-bottom: 26px; max-width: 46ch; margin-left: auto; margin-right: auto; }
@media (max-width: 620px) { .article-cta-inner { padding: 40px 26px; } }
</style>
</head>
<body>

<a class="skip-link" href="#main">Ir al contenido principal</a>

${cookieBanner(base)}

${header(base, "blog")}

<main id="main">

<section class="article-hero">
  <div class="nova-glow"></div>
  <div class="container">
    <div class="breadcrumbs" style="color:rgba(247,244,238,0.5)"><a href="${base}index.html" style="color:rgba(247,244,238,0.5)">Inicio</a> / <a href="${base}blog.html" style="color:rgba(247,244,238,0.5)">Blog</a> / ${esc(post.category)}</div>
    <div class="eyebrow cat">${esc(post.category)}</div>
    <h1>${esc(post.title)}</h1>
    <div class="meta">Blacknova · ${fechaLarga(post.publishedAt)}</div>
  </div>
</section>

<article class="article-wrap">
${post.bodyHtml}
</article>

<div class="article-cta">
  <div class="article-cta-inner">
    <h3>¿Hablamos de tu caso?</h3>
    <p>En Blacknova gestionamos trasteros, naves industriales y patrimonio inmobiliario en Barcelona y Catalunya. Primera consulta gratuita y sin compromiso.</p>
    <a class="btn btn-gold btn-lg" href="${base}contacto.html">Consulta gratuita</a>
  </div>
</div>

</main>

${footer(base)}

</body>
</html>`;
}

// ---------------------------------------------------------------------------
// PÁGINA BLOG  ->  blog.html   (una tarjeta por artículo)
// ---------------------------------------------------------------------------
function blogCard(post) {
  return `      <a class="blog-card" href="blog_articles/${post.slug}.html">
        <div class="blog-card-body">
          <span class="tag">${esc(post.category)}</span>
          <h2>${esc(post.title)}</h2>
          <p>${esc(post.excerpt)}</p>
          <span class="read">Leer artículo →</span>
        </div>
      </a>`;
}

export function blogIndex(posts) {
  const base = "";
  const cards = posts.map(blogCard).join("\n\n");
  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Blog | Naves industriales, trasteros y project management · Blacknova</title>
<meta name="description" content="Artículos sobre naves industriales, trasteros en Calafell y el Penedès, y project management en Catalunya. Guías prácticas y actualizadas."/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="https://blacknova.es/blog.html"/>
<link rel="icon" href="favicon.svg" type="image/svg+xml"/>

<meta property="og:title" content="Blog · Blacknova"/>
<meta property="og:description" content="Guías sobre naves industriales, trasteros y project management en Catalunya."/>
<meta property="og:url" content="https://blacknova.es/blog.html"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="es_ES"/>

${FONTS}
<link rel="stylesheet" href="assets/css/base.css"/>

<style>
.page-hero { position: relative; background: var(--bn-black); color: var(--bn-cream); padding: 170px 0 80px; overflow: hidden; }
.page-hero .nova-glow { width: 560px; height: 560px; top: -200px; right: -180px; }
.page-hero h1 { font-size: clamp(34px,5vw,54px); color: var(--bn-white); max-width: 16ch; }
.blog-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
@media (max-width: 980px) { .blog-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 620px) { .blog-grid { grid-template-columns: 1fr; } }
.blog-card { border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--bn-border); transition: all .3s var(--ease); }
.blog-card:hover { border-color: transparent; box-shadow: var(--shadow-soft); transform: translateY(-4px); }
.blog-card .tag { display: inline-block; font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--bn-amber-dark); margin-bottom: 12px; }
.blog-card-body { padding: 30px; }
.blog-card h2 { font-size: 19px; margin-bottom: 12px; line-height:1.3; }
.blog-card p { color: var(--bn-muted); font-size: 13.5px; margin-bottom: 18px; }
.blog-card a.read { font-size: 13px; color: var(--bn-ink); font-weight: 500; }
</style>
</head>
<body>

<a class="skip-link" href="#main">Ir al contenido principal</a>

${cookieBanner(base)}

${header(base, "blog")}

<main id="main">

<section class="page-hero">
  <div class="nova-glow"></div>
  <div class="container">
    <div class="breadcrumbs" style="color:rgba(247,244,238,0.5)"><a href="index.html" style="color:rgba(247,244,238,0.5)">Inicio</a> / Blog</div>
    <div class="eyebrow" data-animate>Blog</div>
    <h1 data-animate>Naves, trasteros y gestión de proyectos</h1>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="blog-grid" data-animate>

${cards}

    </div>
  </div>
</section>

</main>

${footer(base)}

</body>
</html>`;
}

// ---------------------------------------------------------------------------
// NAVES  ->  naves.html (listado) + naves/<slug>.html (ficha)
// ---------------------------------------------------------------------------

// Quita acentos y pasa a minúsculas: sirve para nombres de clase CSS ("Próximamente" -> "proximamente").
function slugify(s = "") {
  return String(s)
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

// Intenta sacar un precio numérico limpio de un texto libre ("1.800 €/mes" -> 1800).
// Si el texto no empieza por un número (p.ej. "A consultar"), no se inventa nada: devuelve null.
function parsePrecioNumero(precio) {
  if (!precio) return null;
  const m = String(precio).trim().match(/^([\d.,]+)/);
  if (!m) return null;
  const limpio = m[1].replace(/\./g, "").replace(",", ".");
  const n = parseFloat(limpio);
  return Number.isFinite(n) ? n : null;
}

// Mapea el estado de la nave a schema.org ItemAvailability.
function schemaAvailability(estado) {
  const map = {
    Disponible: "https://schema.org/InStock",
    Reservada: "https://schema.org/Reserved",
    Alquilada: "https://schema.org/SoldOut",
    "Próximamente": "https://schema.org/PreOrder",
  };
  return map[estado] || "https://schema.org/PreOrder";
}

function estadoBadge(estado) {
  return `<span class="nave-badge is-${slugify(estado)}">${esc(estado)}</span>`;
}

// Ficha corta (texto plano) para meta description / schema.org cuando no hay descripción propia.
function naveResumen(nave) {
  const partes = [
    nave.operacion ? `Nave industrial en ${nave.operacion.toLowerCase()}` : "Nave industrial",
    nave.zona ? `en ${nave.zona}` : null,
    nave.superficieM2 ? `de ${nave.superficieM2} m²` : null,
  ].filter(Boolean);
  return `${partes.join(" ")}. Gestionada por Blacknova.`;
}

function naveGaleria(nave, base) {
  const fotos = Array.isArray(nave.gallery) ? nave.gallery.filter((g) => g?.url) : [];
  if (!fotos.length) {
    return `<div class="nave-no-photo">
      <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Zm1 12h14l-4.3-5.6-3 3.6L8.5 12 5 17Zm2.5-8a1.75 1.75 0 1 0 0-3.5 1.75 1.75 0 0 0 0 3.5Z" fill="currentColor"/></svg>
      <span>Fotos próximamente</span>
    </div>`;
  }
  return `<div class="nave-gallery">
${fotos
  .map(
    (f, i) =>
      `      <figure${i === 0 ? ' class="is-cover"' : ""}><img src="${esc(f.url)}" alt="${esc(f.alt || nave.title)}" loading="${i === 0 ? "eager" : "lazy"}"/></figure>`,
  )
  .join("\n")}
  </div>`;
}

function naveCaracteristicas(nave) {
  const items = [];
  if (nave.superficieM2) items.push(`${nave.superficieM2} m² construidos`);
  if (nave.alturaLibre) items.push(`Altura libre: ${nave.alturaLibre}`);
  if (nave.muelleCarga) items.push(nave.numMuelles ? `${nave.numMuelles} muelle(s) de carga` : "Muelle de carga");
  if (nave.oficinas) items.push(nave.oficinasM2 ? `Oficinas: ${nave.oficinasM2} m²` : "Con oficinas");
  if (Array.isArray(nave.caracteristicas)) items.push(...nave.caracteristicas.filter(Boolean));
  return items;
}

function caracteristicasList(items) {
  if (!items.length) return "";
  return `<div class="badge-list">${items.map((i) => `<span>${esc(i)}</span>`).join("")}</div>`;
}

// --- tarjeta del listado -----------------------------------------------------
function naveCard(nave) {
  const cover = Array.isArray(nave.gallery) && nave.gallery.length ? nave.gallery[0] : null;
  const caracts = naveCaracteristicas(nave).slice(0, 3);
  return `      <a class="nave-card" href="naves/${nave.slug}.html" data-estado="${esc(nave.estado)}" data-operacion="${esc(nave.operacion)}">
        <div class="nave-cover">
          ${estadoBadge(nave.estado)}
          ${cover ? `<img src="${esc(cover.url)}" alt="${esc(cover.alt || nave.title)}" loading="lazy"/>` : `<div class="no-photo">Fotos próximamente</div>`}
        </div>
        <div class="nave-card-body">
          <span class="tag">${esc(nave.operacion)}${nave.zona ? " · " + esc(nave.zona) : ""}</span>
          <h2>${esc(nave.title)}</h2>
          ${caracts.length ? `<p class="nave-meta">${caracts.map(esc).join(" · ")}</p>` : ""}
          <span class="nave-price">${nave.precio ? esc(nave.precio) : "Precio a consultar"}</span>
        </div>
      </a>`;
}

const NAVES_STYLE = `<style>
.page-hero { position: relative; background: var(--bn-black); color: var(--bn-cream); padding: 170px 0 80px; overflow: hidden; }
.page-hero .nova-glow { width: 560px; height: 560px; top: -200px; right: -180px; }
.page-hero h1 { font-size: clamp(34px,5vw,54px); color: var(--bn-white); max-width: 22ch; }
.page-hero p { max-width: 56ch; color: rgba(247,244,238,0.72); margin-top: 18px; font-size: 16px; }
.naves-filter { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 34px; }
.naves-filter button { font-size: 13px; padding: 9px 18px; border-radius: 999px; border: 1.5px solid var(--bn-border); background: transparent; color: var(--bn-muted); cursor: pointer; transition: all .25s var(--ease); }
.naves-filter button:hover { border-color: var(--bn-ink); color: var(--bn-ink); }
.naves-filter button.is-active { background: var(--bn-ink); border-color: var(--bn-ink); color: var(--bn-white); }
.naves-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
@media (max-width: 980px) { .naves-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 620px) { .naves-grid { grid-template-columns: 1fr; } }
.nave-card { display: flex; flex-direction: column; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--bn-border); transition: all .3s var(--ease); }
.nave-card:hover { border-color: transparent; box-shadow: var(--shadow-soft); transform: translateY(-4px); }
.nave-card.is-hidden { display: none; }
.nave-cover { position: relative; aspect-ratio: 4/3; background: var(--bn-cream-2); overflow: hidden; }
.nave-cover img { width: 100%; height: 100%; object-fit: cover; display: block; }
.nave-cover .no-photo { display: flex; align-items: center; justify-content: center; height: 100%; color: var(--bn-muted-2); font-size: 13px; }
.nave-badge { position: absolute; z-index: 1; top: 14px; left: 14px; font-size: 10.5px; letter-spacing: 0.06em; text-transform: uppercase; padding: 6px 13px; border-radius: 999px; background: var(--bn-black); color: var(--bn-cream); }
.nave-badge.is-disponible { background: var(--bn-success); }
.nave-badge.is-reservada { background: var(--bn-amber-dark); }
.nave-badge.is-alquilada { background: var(--bn-muted); }
.nave-badge.is-proximamente { background: var(--bn-black); }
.nave-card-body { padding: 26px 28px; display: flex; flex-direction: column; gap: 8px; flex: 1; }
.nave-card .tag { display: inline-block; font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--bn-amber-dark); }
.nave-card h2 { font-size: 19px; line-height: 1.3; }
.nave-card .nave-meta { color: var(--bn-muted); font-size: 13px; }
.nave-card .nave-price { margin-top: auto; padding-top: 8px; font-family: var(--font-display); font-size: 21px; color: var(--bn-ink); }
.naves-empty { text-align: center; max-width: 54ch; margin: 0 auto; padding: 70px 30px; border: 1.5px dashed var(--bn-border); border-radius: var(--radius-lg); }
.naves-empty h2 { font-size: clamp(22px,3vw,28px); margin-bottom: 14px; }
.naves-empty p { color: var(--bn-muted); margin-bottom: 26px; }
</style>`;

export function navesIndex(naves) {
  const base = "";
  const activas = naves.filter((n) => n.publishedAt);
  const cards = activas.map(naveCard).join("\n\n");

  const cuerpo = activas.length
    ? `<div class="naves-filter" role="group" aria-label="Filtrar naves" data-naves-filter>
      <button type="button" class="is-active" data-filtro="todas">Todas</button>
      <button type="button" data-filtro="operacion:Alquiler">Alquiler</button>
      <button type="button" data-filtro="operacion:Venta">Venta</button>
      <button type="button" data-filtro="estado:Disponible">Disponibles</button>
      <button type="button" data-filtro="estado:Próximamente">Próximamente</button>
    </div>
    <div class="naves-grid" data-animate data-naves-grid>

${cards}

    </div>`
    : `<div class="naves-empty" data-animate>
      <div class="eyebrow" style="justify-content:center;">Próximamente</div>
      <h2>Estamos preparando nuestra primera cartera de naves</h2>
      <p>Todavía no hay ninguna nave publicada: estamos arrancando este servicio en el corredor entre Barcelona y Tarragona. Si eres propietario o buscas nave, déjanos tus datos y te avisamos en cuanto tengamos disponibilidad.</p>
      <a class="btn btn-gold btn-lg" href="propietarios.html#contacto-propietario">Avisadme cuando haya naves</a>
    </div>`;

  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Naves industriales en alquiler y venta | Corredor Barcelona-Tarragona · Blacknova</title>
<meta name="description" content="Naves industriales gestionadas por Blacknova en el corredor Barcelona-Tarragona: alquiler y venta, con ficha, características y contacto directo."/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="https://blacknova.es/naves.html"/>
<link rel="icon" href="favicon.svg" type="image/svg+xml"/>

<meta property="og:title" content="Naves industriales · Blacknova"/>
<meta property="og:description" content="Naves industriales en alquiler y venta en el corredor Barcelona-Tarragona, gestionadas por Blacknova."/>
<meta property="og:url" content="https://blacknova.es/naves.html"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="es_ES"/>

${FONTS}
<link rel="stylesheet" href="assets/css/base.css"/>

${NAVES_STYLE}
</head>
<body>

<a class="skip-link" href="#main">Ir al contenido principal</a>

${cookieBanner(base)}

${header(base, "naves")}

<main id="main">

<section class="page-hero">
  <div class="nova-glow"></div>
  <div class="container">
    <div class="breadcrumbs" style="color:rgba(247,244,238,0.5)"><a href="index.html" style="color:rgba(247,244,238,0.5)">Inicio</a> / Naves</div>
    <div class="eyebrow" data-animate>Naves industriales</div>
    <h1 data-animate>Naves en alquiler y venta en el corredor Barcelona-Tarragona</h1>
    <p data-animate>Cada nave que gestionamos, con su ficha, características y disponibilidad real. Vamos ampliando la cartera poco a poco.</p>
  </div>
</section>

<section class="section">
  <div class="container">

${cuerpo}

  </div>
</section>

</main>

${footer(base)}

<script>
(function () {
  var grupo = document.querySelector("[data-naves-filter]");
  var grid = document.querySelector("[data-naves-grid]");
  if (!grupo || !grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".nave-card"));
  grupo.querySelectorAll("button").forEach(function (btn) {
    btn.addEventListener("click", function () {
      grupo.querySelectorAll("button").forEach(function (b) { b.classList.remove("is-active"); });
      btn.classList.add("is-active");
      var filtro = btn.getAttribute("data-filtro");
      cards.forEach(function (card) {
        if (filtro === "todas") { card.classList.remove("is-hidden"); return; }
        var partes = filtro.split(":");
        var valor = card.getAttribute("data-" + partes[0]);
        card.classList.toggle("is-hidden", valor !== partes[1]);
      });
    });
  });
})();
</script>

</body>
</html>`;
}

// --- ficha de nave  ->  naves/<slug>.html ------------------------------------
export function navePage(nave) {
  const base = "../";
  const url = `${SITE}/naves/${nave.slug}.html`;
  const caracts = naveCaracteristicas(nave);
  const precioNum = parsePrecioNumero(nave.precio);
  const waTexto = encodeURIComponent(`Hola Blacknova, me interesa la nave "${nave.title}"${nave.zona ? " en " + nave.zona : ""}`);
  const fotos = Array.isArray(nave.gallery) ? nave.gallery.filter((g) => g?.url) : [];

  const jsonld = {
    "@context": "https://schema.org",
    "@type": "RealEstateListing",
    name: nave.title,
    description: naveResumen(nave),
    url,
    datePosted: nave.publishedAt,
    address: nave.zona ? { "@type": "PostalAddress", addressLocality: nave.zona, addressCountry: "ES" } : undefined,
    image: fotos.length ? fotos.map((f) => f.url) : undefined,
    floorSize: nave.superficieM2 ? { "@type": "QuantitativeValue", value: nave.superficieM2, unitCode: "MTK" } : undefined,
    additionalProperty: caracts.length
      ? caracts.map((c) => ({ "@type": "PropertyValue", name: c }))
      : undefined,
    offers: {
      "@type": "Offer",
      businessFunction: nave.operacion === "Venta" ? "http://purl.org/goodrelations/v1#Sell" : "http://purl.org/goodrelations/v1#LeaseOut",
      availability: schemaAvailability(nave.estado),
      priceCurrency: precioNum ? "EUR" : undefined,
      price: precioNum || undefined,
    },
  };

  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>${esc(nave.title)} | Naves industriales · Blacknova</title>
<meta name="description" content="${esc(naveResumen(nave))}"/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="${url}"/>
<link rel="icon" href="${base}favicon.svg" type="image/svg+xml"/>

<meta property="og:title" content="${esc(nave.title)}"/>
<meta property="og:description" content="${esc(naveResumen(nave))}"/>
<meta property="og:url" content="${url}"/>
<meta property="og:type" content="website"/>
<meta property="og:locale" content="es_ES"/>
${fotos.length ? `<meta property="og:image" content="${esc(fotos[0].url)}"/>` : ""}

<script type="application/ld+json">
${JSON.stringify(jsonld, null, 2)}
</script>

${FONTS}
<link rel="stylesheet" href="${base}assets/css/base.css"/>

<style>
.nave-hero { position: relative; background: var(--bn-black); color: var(--bn-cream); padding: 168px 0 60px; overflow: hidden; }
.nave-hero .nova-glow { width: 560px; height: 560px; top: -220px; right: -160px; }
.nave-hero .container { position: relative; z-index: 1; }
.nave-hero h1 { font-size: clamp(30px,4.6vw,46px); color: var(--bn-white); max-width: 24ch; margin: 10px 0 16px; }
.nave-hero .nave-tags { display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
.nave-hero .nave-tags span:not(.nave-badge) { font-size: 12.5px; padding: 7px 14px; border: 1px solid rgba(247,244,238,0.3); border-radius: 999px; color: rgba(247,244,238,0.8); }
.nave-hero .nave-badge { position: static; }
.nave-wrap { max-width: 980px; margin: 0 auto; padding: 60px 28px 20px; display: grid; grid-template-columns: 1.5fr 1fr; gap: 50px; align-items: start; }
@media (max-width: 860px) { .nave-wrap { grid-template-columns: 1fr; } }
.nave-gallery { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 40px; }
.nave-gallery figure { margin: 0; border-radius: var(--radius-md); overflow: hidden; aspect-ratio: 4/3; background: var(--bn-cream-2); }
.nave-gallery figure.is-cover { grid-column: 1 / -1; aspect-ratio: 16/9; }
.nave-gallery img { width: 100%; height: 100%; object-fit: cover; display: block; }
.nave-no-photo { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; aspect-ratio: 16/9; background: var(--bn-cream-2); border-radius: var(--radius-md); color: var(--bn-muted-2); margin-bottom: 40px; }
.nave-wrap h2 { font-size: 24px; margin: 0 0 16px; }
.nave-wrap .body p { font-size: 16.5px; line-height: 1.8; color: #34343b; margin-bottom: 18px; }
.nave-wrap .body ul { margin: 4px 0 20px; }
.nave-wrap .body li { position: relative; padding-left: 24px; margin-bottom: 10px; font-size: 16px; line-height: 1.7; color: #34343b; }
.nave-wrap .body li::before { content: ''; position: absolute; left: 2px; top: 10px; width: 7px; height: 7px; border-radius: 50%; background: var(--bn-amber-grad); }
.nave-side { background: var(--bn-cream); border-radius: var(--radius-lg); padding: 34px; position: sticky; top: 110px; }
.nave-side .nave-price { display: block; font-family: var(--font-display); font-size: 30px; color: var(--bn-ink); margin-bottom: 6px; }
.nave-side .nave-op { font-size: 13px; color: var(--bn-muted); margin-bottom: 22px; display:block; }
.nave-side .btn { margin-bottom: 12px; width: 100%; text-align: center; }
</style>
</head>
<body>

<a class="skip-link" href="#main">Ir al contenido principal</a>

${cookieBanner(base)}

${header(base, "naves")}

<main id="main">

<section class="nave-hero">
  <div class="nova-glow"></div>
  <div class="container">
    <div class="breadcrumbs" style="color:rgba(247,244,238,0.5)"><a href="${base}index.html" style="color:rgba(247,244,238,0.5)">Inicio</a> / <a href="${base}naves.html" style="color:rgba(247,244,238,0.5)">Naves</a></div>
    <div class="eyebrow">${esc(nave.zona || "Nave industrial")}</div>
    <h1>${esc(nave.title)}</h1>
    <div class="nave-tags">
      ${estadoBadge(nave.estado)}
      <span>${esc(nave.operacion)}</span>
      ${nave.superficieM2 ? `<span>${nave.superficieM2} m²</span>` : ""}
    </div>
  </div>
</section>

<div class="nave-wrap">
  <article>
    ${naveGaleria(nave, base)}
    <h2>Descripción</h2>
    <div class="body">
${nave.bodyHtml || "  <p>Ficha en preparación: en breve ampliaremos la descripción de esta nave.</p>"}
    </div>
    ${caracts.length ? `<h2>Características</h2>${caracteristicasList(caracts)}` : ""}
  </article>

  <aside class="nave-side">
    <span class="nave-price">${nave.precio ? esc(nave.precio) : "Precio a consultar"}</span>
    <span class="nave-op">${esc(nave.operacion)} · ${esc(nave.estado)}</span>
    <a class="btn btn-gold" href="https://wa.me/34630879206?text=${waTexto}" target="_blank" rel="noopener">Preguntar por WhatsApp</a>
    <a class="btn btn-outline" href="${base}contacto.html">Ir al formulario de contacto</a>
  </aside>
</div>

</main>

${footer(base)}

</body>
</html>`;
}

// ---------------------------------------------------------------------------
// SITEMAP.XML   (páginas fijas + un <url> por artículo + un <url> por nave)
// ---------------------------------------------------------------------------
const PAGINAS_FIJAS = [
  { loc: "/", freq: "weekly", pri: "1.0" },
  { loc: "/trasteros.html", freq: "weekly", pri: "0.95" },
  { loc: "/naves.html", freq: "weekly", pri: "0.9" },
  { loc: "/que-hacemos.html", freq: "monthly", pri: "0.9" },
  { loc: "/propietarios.html", freq: "monthly", pri: "0.85" },
  { loc: "/contacto.html", freq: "monthly", pri: "0.85" },
  { loc: "/sobre-nosotros.html", freq: "monthly", pri: "0.75" },
  { loc: "/faq.html", freq: "monthly", pri: "0.7" },
  { loc: "/blog.html", freq: "weekly", pri: "0.8" },
];

const PAGINAS_LEGALES = [
  { loc: "/politica-privacidad.html", freq: "yearly", pri: "0.3" },
  { loc: "/politica-cookies.html", freq: "yearly", pri: "0.3" },
  { loc: "/aviso-legal.html", freq: "yearly", pri: "0.3" },
];

export function sitemap(posts, naves = [], hoy = new Date().toISOString().slice(0, 10)) {
  const fija = (u) =>
    `  <url><loc>${SITE}${u.loc}</loc><lastmod>${hoy}</lastmod><changefreq>${u.freq}</changefreq><priority>${u.pri}</priority></url>`;
  const art = (p) =>
    `  <url><loc>${SITE}/blog_articles/${p.slug}.html</loc><lastmod>${p.publishedAt.slice(0, 10)}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>`;
  const nv = (n) =>
    `  <url><loc>${SITE}/naves/${n.slug}.html</loc><lastmod>${n.publishedAt.slice(0, 10)}</lastmod><changefreq>weekly</changefreq><priority>0.75</priority></url>`;

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

${PAGINAS_FIJAS.map(fija).join("\n")}

${posts.map(art).join("\n")}

${naves.map(nv).join("\n")}

${PAGINAS_LEGALES.map(fija).join("\n")}

</urlset>`;
}
