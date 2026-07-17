# Replicar el CMS en otro cliente de SuauMarketing

El sistema es un patrón repetible. Para un cliente nuevo cuya web sea **estática + GitHub +
Cloudflare** (como Blacknova), el montaje es prácticamente copiar-pegar.

## Pasos

1. **Copia la carpeta `_cms/`** al repo del nuevo cliente.
2. **Adapta la plantilla** `_cms/lib/templates.mjs` al diseño de ESE cliente:
   - `articlePage()` → cabecera, colores, tipografías y footer del cliente.
   - `blogIndex()` → su página de blog.
   - `sitemap()` → su dominio y sus páginas fijas.
   > Este es el único trabajo "de diseño": una vez hecho, el resto es automático.
3. **Crea un proyecto de Sanity** para el cliente (o un dataset nuevo dentro de tu organización).
   Reutiliza el mismo `schemas/post.js` salvo que cambien las categorías.
4. **Pon su Project ID** en `studio/sanity.config.js` y `studio/sanity.cli.js`.
5. **Despliega el Studio**: `npm run deploy` → `https://<cliente>.sanity.studio`.
6. **Secrets + webhook + MCP** igual que en el SETUP de Blacknova, con los datos del cliente.

## Coste por cliente

- Sanity: **0 €** (free tier) para volúmenes de blog normales.
- Cloudflare + GitHub: **0 €**.
- Único coste: tu tiempo de adaptar la plantilla (una vez por cliente).

## Idea de producto para la agencia

Puedes venderlo como servicio recurrente ("gestión de blog + SEO") con **coste de herramientas
cero**, mientras la competencia paga WordPress/Webflow cada mes. El contenido lo generan tus
agentes; tú revisas y publicas.

## Ojo

Este patrón aplica a clientes con web **estática (HTML) en GitHub + Cloudflare/Netlify**.
Si un cliente ya tiene **WordPress**, ahí el sistema es otro (WordPress ya es su propio CMS y
tiene su propio MCP aparte).
