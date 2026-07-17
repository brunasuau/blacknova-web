# Naves industriales — cómo añadir una nave sin tocar código

Este documento es para ti (la clienta). El sistema es el mismo Studio donde ya escribes
los artículos del blog (http://localhost:3333 en local, o `https://blacknova.sanity.studio`
si ya lo tienes publicado): ahora tiene también una sección **"Naves industriales"**.

## Paso a paso

1. Abre el Studio y, en el menú de la izquierda, entra en **"Naves industriales"**.
2. Pulsa **"+ Create"** (o el botón `+` de arriba) → elige **"Nave industrial"**.
3. Rellena los campos. Ninguno es obligatorio salvo los que tienen un `*` rojo
   (nombre, zona, operación y estado). El resto puedes dejarlo vacío y completarlo
   más adelante:
   - **Nombre / referencia de la nave**: cómo la vas a reconocer. Ej. "Nave Vilafranca 800 m²".
   - **Zona / población**: dónde está (Vilafranca, El Vendrell, Sant Sadurní...).
   - **Operación**: Alquiler o Venta.
   - **Estado**: dale a **"Próximamente"** mientras la estés preparando y aún no se
     pueda visitar ni contratar. Cámbialo a **"Disponible"** el día que sí.
   - **Superficie, precio, altura, muelle, oficinas, características**: rellena lo que
     sepas. El precio puedes dejarlo como texto libre: "1.800 €/mes", "A consultar"...
   - **Descripción**: escribe un par de párrafos como si se lo explicaras a un cliente.
   - **Fotos de la nave**: arrastra las fotos que tengas. Si todavía no tienes, no pasa
     nada: la web mostrará "Fotos próximamente" hasta que subas alguna.
   - **Ficha destacada**: actívalo si quieres que esta nave aparezca la primera en el listado.
4. Baja hasta **"Fecha de publicación"**. Mientras esté vacía, la nave se guarda como
   **borrador** (no se ve en la web). En cuanto le pongas fecha (se rellena sola al crearla)
   y le des a **Publish**, sale publicada.
5. Pulsa **Publish** (arriba a la derecha).

En 1-2 minutos la nave aparece sola:
- En el listado **blacknova.es/naves.html**, con su tarjeta, estado y precio (o "A consultar").
- Con su propia página de ficha: **blacknova.es/naves/tu-nave.html**, con galería,
  características y botones de WhatsApp y contacto.
- Añadida automáticamente al `sitemap.xml` (para que Google la encuentre).

**No tienes que tocar ni escribir HTML en ningún momento.**

## Mientras no tengas ninguna nave publicada

Si todavía no has publicado ninguna nave (o las tienes todas en borrador), la página
`naves.html` no queda vacía ni rota: muestra automáticamente un mensaje de
"Estamos preparando nuestra primera cartera de naves" con un botón para que los
interesados dejen sus datos. En cuanto publiques la primera, ese aviso desaparece solo
y se sustituye por el listado real.

## Cómo editar o quitar una nave

- **Editar**: entra en la nave desde el Studio, cambia lo que quieras y dale a Publish otra vez.
- **Ocultarla de la web sin borrarla**: quita la fecha de "Fecha de publicación" y dale a Publish
  (o guarda sin publicar). Vuelve a quedar en borrador.
- **Borrarla del todo**: dentro de la nave, menú "..." (arriba a la derecha) → Delete.

## Filtros del listado

En `naves.html` hay unos botones (Todas / Alquiler / Venta / Disponibles / Próximamente)
que filtran las tarjetas al momento, sin recargar la página. Se generan solos a partir
de los datos de "Operación" y "Estado" de cada nave: no hay que configurar nada.

## La única cosa que queda pendiente (técnica, no tuya)

Para que esto funcione en la web real (blacknova.es) hace falta que alguien haga, **una
sola vez**, el mismo paso que ya está pendiente para el blog (ver `_cms/SETUP.md`):
crear el proyecto en Sanity, conectar el Studio y el despliegue automático. El schema de
naves y el motor que genera `naves.html` y las fichas **ya están listos y probados en
local** (ver más abajo). En cuanto ese montaje esté hecho, publicar una nave desde el
Studio es exactamente el paso a paso de arriba.

---

## Nota técnica (para Claude / quien mantenga esto)

- Molde de datos: `_cms/schemas/nave.js` (tipo de documento `nave`).
- Registrado en el Studio: `_cms/studio/sanity.config.js`.
- Motor de render: `_cms/build.mjs` (funciones `getNavesFromSanity` / `getNavesFromSample`)
  + `_cms/lib/templates.mjs` (funciones `navesIndex()` y `navePage()`).
- Genera `naves.html` (listado con filtro y empty-state) y `naves/<slug>.html` (ficha),
  y añade ambos al `sitemap.xml` generado por `sitemap(posts, naves)`.
- Nave de ejemplo para probar el build sin Sanity: `_cms/sample/naves.json`
  (bórrala del JSON de ejemplo si algún día molesta en un preview; no afecta a producción,
  solo se usa con `npm run preview`).
- Probado con:
  ```bash
  cd _cms
  node build.mjs --source=sample --out=_preview
  ```
  Genera `_preview/naves.html` y `_preview/naves/nave-ejemplo-vilafranca-del-penedes.html`.
  También se probó vaciando `sample/naves.json` a `[]` para confirmar que `naves.html`
  cae en el empty-state "próximamente" sin romper nada.
- El nav, el footer (link "Naves industriales") y la home de `propietarios.html` (botón
  "Ver naves gestionadas") ya enlazan a `naves.html` en las 11 páginas estáticas del sitio
  y en las plantillas compartidas (`header()`/`footer()` de `templates.mjs`, que usan
  también `blog.html` y los artículos).
