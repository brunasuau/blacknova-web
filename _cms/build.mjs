// Motor de publicación del blog de Blacknova.
//
// Uso:
//   node build.mjs --source=sanity --out=..        (producción: trae de Sanity y escribe en la web)
//   node build.mjs --source=sample --out=_preview  (prueba local con datos de ejemplo)
//
// Genera:
//   <out>/blog_articles/<slug>.html   una página por artículo
//   <out>/blog.html                   índice del blog con una tarjeta por artículo
//   <out>/sitemap.xml                 sitemap completo
//
// Y actualiza en <out>/index.html el bloque "últimos artículos" (entre los
// marcadores ULTIMOS-ARTICULOS:INICIO / :FIN) con los 3 artículos más nuevos.
//
// Los artículos se ordenan por fecha de publicación (más nuevo primero).

import { writeFile, mkdir, readFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { toHTML } from "@portabletext/to-html";
import { articlePage, blogIndex, sitemap, navesIndex, navePage, homeCards } from "./lib/templates.mjs";

const __dirname = dirname(fileURLToPath(import.meta.url));

// --- args ------------------------------------------------------------------
const args = Object.fromEntries(
  process.argv.slice(2).map((a) => {
    const [k, v] = a.replace(/^--/, "").split("=");
    return [k, v ?? true];
  }),
);
const SOURCE = args.source || "sample";
const OUT = resolve(__dirname, args.out || "_preview");

// --- Portable Text -> HTML del cuerpo --------------------------------------
// Produce h2/p/ul/li/strong/a, que es justo lo que estilan las clases .body de la plantilla.
function renderBody(blocks) {
  return toHTML(blocks, {
    components: {
      block: {
        normal: ({ children }) => `  <p>${children}</p>`,
        h2: ({ children }) => `  <h2>${children}</h2>`,
        h3: ({ children }) => `  <h3>${children}</h3>`,
      },
      marks: {
        strong: ({ children }) => `<strong>${children}</strong>`,
        em: ({ children }) => `<em>${children}</em>`,
        link: ({ children, value }) =>
          `<a href="${value?.href || "#"}">${children}</a>`,
      },
      list: {
        bullet: ({ children }) => `  <ul>${children}</ul>`,
        number: ({ children }) => `  <ol>${children}</ol>`,
      },
      listItem: {
        bullet: ({ children }) => `<li>${children}</li>`,
        number: ({ children }) => `<li>${children}</li>`,
      },
    },
  });
}

// Descripción de nave -> HTML (versión más simple que renderBody: solo párrafos y listas).
function renderDescripcion(blocks) {
  return toHTML(blocks, {
    components: {
      block: {
        normal: ({ children }) => `  <p>${children}</p>`,
      },
      marks: {
        strong: ({ children }) => `<strong>${children}</strong>`,
        em: ({ children }) => `<em>${children}</em>`,
      },
      list: {
        bullet: ({ children }) => `  <ul>${children}</ul>`,
      },
      listItem: {
        bullet: ({ children }) => `<li>${children}</li>`,
      },
    },
  });
}

// --- Origen de datos -------------------------------------------------------
async function getPostsFromSample() {
  const raw = await readFile(resolve(__dirname, "sample/posts.json"), "utf8");
  return JSON.parse(raw);
}

async function getNavesFromSample() {
  const raw = await readFile(resolve(__dirname, "sample/naves.json"), "utf8");
  return JSON.parse(raw);
}

async function getNavesFromSanity() {
  const { createClient } = await import("@sanity/client");
  const client = createClient({
    projectId: process.env.SANITY_PROJECT_ID,
    dataset: process.env.SANITY_DATASET || "production",
    apiVersion: "2024-01-01",
    useCdn: false,
    token: process.env.SANITY_TOKEN, // token de solo lectura
  });
  // Solo naves publicadas (con fecha) y no marcadas como borrador.
  // "gallery[]{...}" resuelve cada foto a su URL pública del CDN de Sanity.
  const query = `*[_type == "nave" && defined(slug.current) && defined(publishedAt) && !(_id in path("drafts.**"))] | order(destacada desc, publishedAt desc){
    "slug": slug.current,
    title,
    zona,
    operacion,
    estado,
    superficieM2,
    precio,
    alturaLibre,
    muelleCarga,
    numMuelles,
    oficinas,
    oficinasM2,
    caracteristicas,
    descripcion,
    "gallery": galeria[]{"url": asset->url, alt},
    destacada,
    publishedAt
  }`;
  return client.fetch(query);
}

// Prueba con los artículos migrados (migration/posts.ndjson) antes de importarlos a Sanity.
async function getPostsFromMigration() {
  const raw = await readFile(resolve(__dirname, "migration/posts.ndjson"), "utf8");
  return raw
    .split("\n")
    .filter(Boolean)
    .map((l) => JSON.parse(l))
    .map((d) => ({ ...d, slug: d.slug?.current || d.slug }))
    .sort((a, b) => (a.publishedAt < b.publishedAt ? 1 : -1));
}

async function getPostsFromSanity() {
  const { createClient } = await import("@sanity/client");
  const client = createClient({
    projectId: process.env.SANITY_PROJECT_ID,
    dataset: process.env.SANITY_DATASET || "production",
    apiVersion: "2024-01-01",
    useCdn: false,
    token: process.env.SANITY_TOKEN, // token de solo lectura
  });
  // Solo artículos publicados (con fecha) y no marcados como borrador.
  const query = `*[_type == "post" && defined(slug.current) && defined(publishedAt) && !(_id in path("drafts.**"))] | order(publishedAt desc){
    "slug": slug.current,
    title,
    category,
    "metaDescription": coalesce(metaDescription, excerpt),
    excerpt,
    focusKeyword,
    publishedAt,
    body
  }`;
  return client.fetch(query);
}

// --- Home ------------------------------------------------------------------
// Sustituye las tarjetas entre los marcadores de index.html por los artículos
// más recientes. Si los marcadores no están, no toca nada y avisa: es preferible
// a reescribir la home a ciegas.
const HOME_INICIO = "<!-- ULTIMOS-ARTICULOS:INICIO";
const HOME_FIN = "<!-- ULTIMOS-ARTICULOS:FIN -->";

async function actualizarHome(posts) {
  const ruta = resolve(OUT, "index.html");
  let html;
  try {
    html = await readFile(ruta, "utf8");
  } catch {
    return "index.html no encontrado, no se toca";
  }

  const i = html.indexOf(HOME_INICIO);
  const j = html.indexOf(HOME_FIN, i);
  if (i === -1 || j === -1) {
    console.warn("⚠️  index.html no tiene los marcadores ULTIMOS-ARTICULOS: la home no se actualiza.");
    return "sin marcadores, no se toca";
  }

  const finComentarioInicio = html.indexOf("-->", i) + 3;
  const nuevo =
    html.slice(0, finComentarioInicio) +
    "\n" +
    homeCards(posts, 3) +
    "\n      " +
    html.slice(j);

  if (nuevo === html) return "ya estaba al día";
  await writeFile(ruta, nuevo, "utf8");
  return `actualizada con ${posts.slice(0, 3).map((p) => p.slug).join(", ")}`;
}

// --- Build -----------------------------------------------------------------
async function main() {
  const rawPosts =
    SOURCE === "sanity"
      ? await getPostsFromSanity()
      : SOURCE === "migration"
        ? await getPostsFromMigration()
        : await getPostsFromSample();

  // Las naves no existían antes de este build: en "migration" no hay datos migrados,
  // así que caen de vuelta a los de ejemplo (o vacío si tampoco los hay).
  const rawNaves =
    SOURCE === "sanity" ? await getNavesFromSanity() : await getNavesFromSample().catch(() => []);

  if (!rawPosts.length) {
    // Con Sanity como origen, cero artículos casi siempre significa token caducado,
    // red caída o consulta rota. Si siguiéramos, publicaríamos un blog vacío y
    // borraríamos el que ya está en la web: mejor fallar y dejarlo como está.
    if (SOURCE === "sanity") {
      throw new Error(
        "Sanity no ha devuelto ningún artículo publicado. Se aborta el build para no vaciar el blog.",
      );
    }
    console.warn("⚠️  No se han encontrado artículos publicados. Nada que generar.");
  }
  if (!rawNaves.length) {
    console.warn("⚠️  No hay naves publicadas todavía: naves.html se generará con el aviso de \"próximamente\".");
  }

  // Normaliza + renderiza el cuerpo (Portable Text -> HTML).
  const posts = rawPosts.map((p) => ({
    ...p,
    bodyHtml: Array.isArray(p.body) ? renderBody(p.body) : p.bodyHtml || "",
  }));

  const naves = rawNaves.map((n) => ({
    ...n,
    bodyHtml: Array.isArray(n.descripcion) ? renderDescripcion(n.descripcion) : n.bodyHtml || "",
  }));

  await mkdir(resolve(OUT, "blog_articles"), { recursive: true });
  await mkdir(resolve(OUT, "naves"), { recursive: true });

  // 1) páginas de artículo
  for (const post of posts) {
    const html = articlePage(post);
    await writeFile(resolve(OUT, "blog_articles", `${post.slug}.html`), html, "utf8");
  }

  // 2) blog.html
  await writeFile(resolve(OUT, "blog.html"), blogIndex(posts), "utf8");

  // 3) fichas de nave + naves.html
  for (const nave of naves) {
    const html = navePage(nave);
    await writeFile(resolve(OUT, "naves", `${nave.slug}.html`), html, "utf8");
  }
  await writeFile(resolve(OUT, "naves.html"), navesIndex(naves), "utf8");

  // 4) sitemap.xml
  await writeFile(resolve(OUT, "sitemap.xml"), sitemap(posts, naves), "utf8");

  // 5) "últimos artículos" de la home
  const homeActualizada = await actualizarHome(posts);

  console.log(`✅ Generados ${posts.length} artículos + ${naves.length} naves + blog.html + naves.html + sitemap.xml`);
  console.log(`   Home: ${homeActualizada}`);
  console.log(`   Origen: ${SOURCE}  →  Salida: ${OUT}`);
  for (const p of posts) console.log(`   · blog_articles/${p.slug}.html`);
  for (const n of naves) console.log(`   · naves/${n.slug}.html`);
}

main().catch((err) => {
  console.error("❌ Error en el build:", err);
  process.exit(1);
});
