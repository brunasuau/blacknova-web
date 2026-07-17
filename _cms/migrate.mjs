// Migración: convierte los artículos HTML existentes (../blog_articles/*.html)
// en documentos de Sanity (Portable Text) y los deja en migration/posts.ndjson.
//
// Uso:
//   node migrate.mjs                 -> genera migration/posts.ndjson (revísalo)
//   npx sanity dataset import migration/posts.ndjson production   (desde _cms/studio, con login)
//
// Fuentes de cada campo:
//   title, metaDescription, publishedAt, body  ->  del propio artículo
//   category, excerpt                          ->  de las tarjetas de ../blog.html (si están),
//                                                  con respaldo deducido del tema.

import { readFile, writeFile, mkdir, readdir } from "node:fs/promises";
import { resolve, dirname, basename } from "node:path";
import { fileURLToPath } from "node:url";
import { randomUUID } from "node:crypto";
import { parse } from "node-html-parser";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ARTICLES_DIR = resolve(__dirname, "../blog_articles");
const BLOG_HTML = resolve(__dirname, "../blog.html");

const key = () => randomUUID().slice(0, 8);

// Categorías válidas del schema.
function guessCategory(slug, title) {
  const s = (slug + " " + title).toLowerCase();
  if (s.includes("traster")) return "Trasteros";
  if (s.includes("project") || s.includes("manager")) return "Gestión de proyectos";
  if (s.includes("invertir") || s.includes("inversion")) return "Inversión";
  if (s.includes("patrimonio") || s.includes("activos")) return "Patrimonio inmobiliario";
  if (s.includes("nave")) return "Naves industriales";
  return "Naves industriales";
}

// --- Mapa slug -> {category, excerpt} desde las tarjetas de blog.html ---------
async function readBlogCards() {
  const map = {};
  try {
    const html = await readFile(BLOG_HTML, "utf8");
    const root = parse(html);
    for (const card of root.querySelectorAll("a.blog-card, .blog-card")) {
      const a = card.tagName === "A" ? card : card.querySelector("a");
      const href = (card.getAttribute("href") || a?.getAttribute("href") || "");
      const m = href.match(/blog_articles\/([^"]+)\.html/);
      if (!m) continue;
      const slug = m[1];
      const tag = card.querySelector(".tag, .blog-card-cat");
      const p = card.querySelector("p, .blog-card-desc");
      map[slug] = {
        category: tag ? tag.text.trim() : null,
        excerpt: p ? p.text.trim() : null,
      };
    }
  } catch {
    /* blog.html puede no existir; seguimos con respaldos */
  }
  return map;
}

// --- Inline HTML -> spans de Portable Text -----------------------------------
function inlineToSpans(node) {
  const spans = [];
  const markDefs = [];
  for (const child of node.childNodes) {
    if (child.nodeType === 3) {
      // texto
      const text = child.rawText.replace(/\s+/g, " ");
      if (text) spans.push({ _type: "span", _key: key(), text, marks: [] });
    } else if (child.tagName === "STRONG" || child.tagName === "B") {
      const text = child.text.replace(/\s+/g, " ");
      if (text) spans.push({ _type: "span", _key: key(), text, marks: ["strong"] });
    } else if (child.tagName === "EM" || child.tagName === "I") {
      const text = child.text.replace(/\s+/g, " ");
      if (text) spans.push({ _type: "span", _key: key(), text, marks: ["em"] });
    } else if (child.tagName === "A") {
      const text = child.text.replace(/\s+/g, " ");
      const href = child.getAttribute("href") || "#";
      const mk = key();
      markDefs.push({ _key: mk, _type: "link", href });
      if (text) spans.push({ _type: "span", _key: key(), text, marks: [mk] });
    } else {
      const text = child.text.replace(/\s+/g, " ");
      if (text) spans.push({ _type: "span", _key: key(), text, marks: [] });
    }
  }
  return { spans, markDefs };
}

function block(style, node) {
  const { spans, markDefs } = inlineToSpans(node);
  return { _type: "block", _key: key(), style, markDefs, children: spans };
}

function listItem(node) {
  const { spans, markDefs } = inlineToSpans(node);
  return {
    _type: "block",
    _key: key(),
    style: "normal",
    listItem: "bullet",
    level: 1,
    markDefs,
    children: spans,
  };
}

// --- .body HTML -> array de bloques ------------------------------------------
function bodyToPortableText(bodyEl) {
  const blocks = [];
  for (const el of bodyEl.childNodes) {
    if (el.nodeType !== 1) continue; // solo elementos
    const tag = el.tagName;
    const cls = el.getAttribute("class") || "";
    if (cls.includes("cta")) continue; // el CTA lo pone la plantilla
    if (tag === "P") blocks.push(block("normal", el));
    else if (tag === "H2") blocks.push(block("h2", el));
    else if (tag === "H3") blocks.push(block("h3", el));
    else if (tag === "UL" || tag === "OL") {
      for (const li of el.querySelectorAll("li")) blocks.push(listItem(li));
    }
  }
  return blocks;
}

// --- Un artículo HTML -> documento Sanity ------------------------------------
async function fileToDoc(file, cards) {
  const slug = basename(file, ".html");
  const html = await readFile(resolve(ARTICLES_DIR, file), "utf8");
  const root = parse(html);

  const title =
    root.querySelector("h1")?.text.trim() ||
    root.querySelector(".article-title")?.text.trim() ||
    slug;
  const metaDescription =
    root.querySelector('meta[name="description"]')?.getAttribute("content")?.trim() || "";

  // fecha desde JSON-LD
  let publishedAt = "2026-06-01T09:00:00Z";
  const ld = root.querySelector('script[type="application/ld+json"]');
  if (ld) {
    try {
      const j = JSON.parse(ld.text);
      if (j.datePublished) publishedAt = `${j.datePublished}T09:00:00Z`;
    } catch {}
  }

  const bodyEl = root.querySelector(".body") || root.querySelector(".article-body");
  const body = bodyEl ? bodyToPortableText(bodyEl) : [];

  const card = cards[slug] || {};
  const category = guessCategory(slug, title); // siempre un valor válido del schema
  const excerpt = card.excerpt || metaDescription.slice(0, 180);

  return {
    _id: `migrated-${slug}`,
    _type: "post",
    title,
    slug: { _type: "slug", current: slug },
    category,
    excerpt,
    metaDescription,
    publishedAt,
    body,
  };
}

async function main() {
  const cards = await readBlogCards();
  const files = (await readdir(ARTICLES_DIR)).filter((f) => f.endsWith(".html"));

  const docs = [];
  for (const file of files) docs.push(await fileToDoc(file, cards));

  await mkdir(resolve(__dirname, "migration"), { recursive: true });
  const ndjson = docs.map((d) => JSON.stringify(d)).join("\n") + "\n";
  await writeFile(resolve(__dirname, "migration/posts.ndjson"), ndjson, "utf8");

  console.log(`✅ ${docs.length} artículos convertidos → migration/posts.ndjson`);
  for (const d of docs)
    console.log(`   · ${d.slug.current}  [${d.category}]  (${d.body.length} bloques)`);
}

main().catch((e) => {
  console.error("❌ Error en la migración:", e);
  process.exit(1);
});
