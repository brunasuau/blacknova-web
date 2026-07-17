# CMS de Blacknova con Sanity — Guía de puesta en marcha

Sistema para **publicar artículos de blog y naves industriales sin escribir código**, con
panel visual (Sanity Studio) y publicación automática por tus agentes de SuauMarketing (vía MCP).

> ¿Quieres publicar una **nave industrial** (no un artículo)? El paso a paso está en
> [`_cms/NAVES.md`](./NAVES.md). El montaje inicial (esta guía) es el mismo para ambos.

## ⚡ Arranque rápido (los 2 comandos que quedan por hacer)

Desde `~/Desktop/blacknova-marketing/_cms`:

```bash
# 1) Meter tus 16 artículos en Sanity (te pedirá login una vez)
npm run import

# 2) Publicar una URL de PRUEBA en Cloudflare (no toca blacknova.es; login una vez)
npm run deploy:preview
```

- El panel para escribir ya está en marcha: http://localhost:3333
- Preview local del sitio completo (sin subir nada): `npm run preview:site` → `open _preview_site/blog.html`

---

## Cómo funciona (el flujo)

```
  Tus agentes SEO  ─┐
   (vía MCP)        ├──►  SANITY  ──(publicar)──►  webhook  ──►  GitHub Action
  Tú en el Studio  ─┘     (contenido)                              │
                                                                   ▼
                                            build: Sanity → HTML (diseño Blacknova)
                                                                   │
                                                                   ▼
                                                    Cloudflare (web en vivo)
```

- **Escribir/revisar**: en el Studio (panel web) o los agentes vía MCP.
- **Publicar**: das a *Publish* en Sanity → en 1-2 min está online, con el diseño de Blacknova,
  listado en el blog y añadido al `sitemap.xml`. **Nunca tocas HTML.**

---

## Qué está ya hecho (por Claude)

- ✅ Motor de render (`_cms/`): convierte los artículos y las naves de Sanity al HTML EXACTO
  de Blacknova (páginas de artículo + `blog.html` + fichas de nave + `naves.html` +
  `sitemap.xml`). **Probado en local.**
- ✅ Schema del artículo (`_cms/schemas/post.js`) y de la nave (`_cms/schemas/nave.js`), y Studio (`_cms/studio/`).
- ✅ GitHub Action de despliegue (`.github/workflows/publish-blog.yml`).
- ✅ `.assetsignore` para que las herramientas no se publiquen en la web.
- ✅ Ver [`_cms/NAVES.md`](./NAVES.md) para el paso a paso de publicar una nave.

## Qué tienes que hacer tú (una sola vez, ~20 min)

### 1) Crear el proyecto en Sanity (gratis)
1. Entra en https://www.sanity.io/ y crea una cuenta (con Google/GitHub).
2. En https://www.sanity.io/manage crea un proyecto nuevo → **New project**.
   - Nombre: `Blacknova`
   - Dataset: `production` (público).
3. Copia el **Project ID** (algo como `a1b2c3d4`).

### 2) Pegar tu Project ID (2 archivos)
Sustituye `TU_PROJECT_ID` por el tuyo en:
- `_cms/studio/sanity.config.js`
- `_cms/studio/sanity.cli.js`

> Dile a Claude "pega mi Project ID `xxxx`" y lo hace por ti.

### 3) Levantar el panel (Studio)
```bash
cd _cms/studio
npm install
npm run dev        # abre http://localhost:3333  → ya puedes escribir artículos
```
Para dejarlo online (accesible desde cualquier sitio, gratis):
```bash
npx sanity login
npm run deploy     # queda en https://blacknova.sanity.studio
```

### 4) Crear los tokens (Manage → API → Tokens)
En https://www.sanity.io/manage (tu proyecto → **API → Tokens**):
- **Token de LECTURA** (para el build): permiso *Viewer*. Nómbralo `build-read`.
- **Token de ESCRITURA** (para el MCP de los agentes): permiso *Editor*. Nómbralo `agents-write`.

Guárdalos bien; solo se muestran una vez.

### 5) Conectar el MCP a tus agentes (para que publiquen solos)
Ver `_cms/mcp-sanity.md`. En resumen, añade el servidor MCP de Sanity con tu Project ID
y el token de ESCRITURA. Tus agentes de SuauMarketing podrán crear y publicar artículos.

### 6) Deploy automático (secrets en GitHub)
En el repo `brunasuau/blacknova-web` → **Settings → Secrets and variables → Actions**, crea:
- `SANITY_PROJECT_ID` → tu Project ID
- `SANITY_TOKEN` → el token de **lectura** (`build-read`)
- `CLOUDFLARE_API_TOKEN` → token de Cloudflare con permiso *Edit Workers* (dash.cloudflare.com → My Profile → API Tokens)
- `CLOUDFLARE_ACCOUNT_ID` → tu Account ID de Cloudflare

### 7) Webhook: publicar en Sanity → republica la web
En https://www.sanity.io/manage (proyecto → **API → Webhooks → Create webhook**):
- **URL**: `https://api.github.com/repos/brunasuau/blacknova-web/dispatches`
- **Trigger on**: Create, Update, Delete
- **HTTP method**: POST
- **HTTP Headers**:
  - `Authorization: Bearer <GITHUB_TOKEN>`  (un *fine-grained token* con permiso *Contents: read/write* sobre el repo)
  - `Accept: application/vnd.github+json`
- **Projection / Body**: `{ "event_type": "sanity-publish" }`

Con esto, cada publicación en Sanity dispara el GitHub Action que reconstruye y despliega.

---

## El día a día (una vez montado)

1. Pides a tus agentes SEO un artículo para una keyword → lo crean en Sanity vía MCP (como borrador).
2. Lo revisas en el Studio (https://blacknova.sanity.studio), ajustas y das **Publish**.
3. Solo: se genera la página con el diseño de Blacknova, entra en el blog y en el sitemap,
   y Cloudflare republica. Online en 1-2 min.

## Probar el motor sin Sanity (ya funciona)
```bash
cd _cms
npm install
npm run preview     # genera en _cms/_preview/ con datos de ejemplo (posts + 1 nave de ejemplo)
```
Abre `_cms/_preview/blog_articles/como-elegir-trastero-barcelona.html` en el navegador,
o `_cms/_preview/naves.html` y `_cms/_preview/naves/nave-ejemplo-vilafranca-del-penedes.html`
para ver el listado y la ficha de nave de ejemplo.

## Replicar en otro cliente de SuauMarketing
Ver `_cms/REPLICAR.md`.
