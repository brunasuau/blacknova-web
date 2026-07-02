# Blacknova — Guía de despliegue y migración de hosting

Guía actualizada tras el rediseño completo del sitio (julio 2026). Sustituye a la versión anterior de este documento, que describía un proceso de subida manual por FTP ya obsoleto.

---

## 1. Qué ha cambiado en el repositorio

- Nueva identidad visual (logo, color, tipografía) en `assets/css/base.css` y `assets/brand/`.
- Todas las páginas comparten `assets/css/base.css` y `assets/js/main.js` en lugar de CSS/JS duplicado en cada archivo.
- Se ha eliminado `blacknova-deploy/` (una copia manual y desactualizada del sitio) y el workflow que la mantenía. **El propio repositorio, en su raíz, es ahora la única fuente de verdad del sitio.**
- Scripts internos de SEO/Instagram movidos a `tools/` (no se publican).
- Informes internos (`*.pdf`, `*.txt`, `seo_reports/`) ya no se suben al repositorio — antes se publicaban por error junto con el sitio web.
- Email de contacto unificado a `gestion@blacknova.es` en todo el sitio (antes convivían `info@blacknova.com` y `gestion@blacknova.es`).

## 2. Por qué migrar de Nominalia a un hosting nuevo

Nominalia es un buen sitio para **registrar el dominio**, pero como hosting de una web estática no ofrece por defecto protección DDoS, WAF (firewall de aplicaciones web) ni CDN global — y el despliegue actual es manual (subir archivos por FTP), lo que facilita errores humanos como los que hemos corregido.

**Recomendación: Cloudflare Pages** para alojar el sitio. El dominio se queda registrado en Nominalia (decisión confirmada) — solo cambian los nameservers, no el registro.

Por qué:
- Despliegue automático: cada `git push` a `main` publica el sitio en segundos, sin FTP ni carpetas duplicadas.
- HTTPS gratuito y automático, con renovación de certificados sin intervención manual.
- CDN global (el sitio se sirve desde el nodo más cercano al visitante — más rápido, mejor para SEO).
- Protección DDoS y WAF (firewall) incluidos gratis, precisamente lo que se pedía ("que no se pueda caer ni hackear").
- Gratis para un sitio de este tamaño y tráfico.

Alternativas equivalentes: Netlify o Vercel. Cualquiera de las tres es válida; Cloudflare tiene la red anti-DDoS más robusta de las tres en el plan gratuito.

## 3. Migración paso a paso

Confirmado con el cliente: el dominio se queda registrado en Nominalia; solo se migran DNS y hosting a Cloudflare. Los buzones `@blacknova.es` existen en Nominalia pero **no se han usado nunca** (cero correos), así que no hay riesgo real de perder correo — aun así, conviene guardar una copia de los registros DNS actuales antes de tocar nada, por si en el futuro se activan esos buzones o hay algún TXT de verificación (ej. Google Search Console) que valga la pena conservar.

1. Entra en el panel de Nominalia → DNS de `blacknova.es` y **haz una captura o copia de todos los registros actuales** (MX, TXT, etc.) antes de cambiar los nameservers.

### Paso a paso

1. **Crear cuenta en Cloudflare** (cloudflare.com, plan gratuito).
2. **Añadir el sitio `blacknova.es`** en Cloudflare — el sistema escaneará automáticamente los registros DNS existentes en Nominalia. Verifica que ha detectado bien los MX del correo antes de continuar.
3. **Cloudflare Pages → Crear proyecto → Conectar con GitHub** → selecciona el repositorio `brunasuau/blacknova-web`.
4. Configuración de build:
   - Framework preset: `None`
   - Build command: *(vacío — no hay build)*
   - Build output directory: `/`
5. Desplegar. Cloudflare asignará una URL temporal `*.pages.dev` para probar antes de conectar el dominio real.
6. **Dominio personalizado:** en el proyecto de Pages, añade `blacknova.es` y `www.blacknova.es` como dominios personalizados.
7. **Cambiar los nameservers** en Nominalia a los dos que te indique Cloudflare (esto es lo único que se toca en Nominalia; el dominio se puede seguir renovando allí sin problema). La propagación puede tardar hasta 24-48h.
8. Tras la propagación, en Cloudflare → SSL/TLS: modo **"Full (strict)"**. En Edge Certificates, activa **"Always Use HTTPS"** y **HSTS** (con `max-age` alto, ya incluido en el archivo `_headers` del repo).
9. En Security → WAF, activa las reglas gestionadas gratuitas y (opcional) "Bot Fight Mode".
10. Verifica que el correo sigue llegando (envía un email de prueba) antes de dar la migración por cerrada.

## 4. Formularios (Formspree)

**Ya configurado.** Los formularios de `contacto.html`, `trasteros.html` y `propietarios.html` usan [Formspree](https://formspree.io) con el formulario real "Blacknova-Contacto" (`https://formspree.io/f/xjgqpwrp`), compartido entre los tres.

Pendiente de verificar por el cliente: confirmar en Formspree (cuenta → email de la cuenta o "Emails" verificados) que las notificaciones llegan a `direccion@blacknova.es` y no al email personal usado para crear la cuenta.

## 5. Search Console y analítica

1. Si cambias de verificación de dominio, en Search Console puedes verificar por registro **DNS TXT** en lugar del archivo HTML (`googleb764219703c919a8.html`), que es más robusto frente a cambios de hosting.
2. Reenvía el sitemap actualizado: `https://blacknova.es/sitemap.xml`.
3. Solicita indexación manual de `/trasteros.html` y `/propietarios.html`.

## 6. Checklist final

- [ ] El correo `@blacknova.es` sigue funcionando tras el cambio de nameservers
- [ ] `https://blacknova.es` carga por HTTPS sin avisos de seguridad
- [ ] El banner de cookies aparece en la primera visita y GA/GTM no cargan antes de aceptar
- [ ] Formularios de contacto, trasteros y propietarios funcionan (con el ID real de Formspree)
- [ ] WhatsApp flotante funciona en móvil
- [ ] Sitemap reenviado a Search Console
- [ ] Cabeceras de seguridad activas (compruébalo en [securityheaders.com](https://securityheaders.com))

---

## 7. Pendiente de decisión del cliente

- **Datos del Registro Mercantil** de Blacknova S.L. (tomo/folio/hoja) para completar el aviso legal conforme al art. 10.1.c de la LSSI-CE. Cliente avisará en cuanto los tenga.
- **Fotos reales** de los trasteros en Calafell y de las naves gestionadas — de momento el sitio no usa fotografía de estos activos (se ha priorizado un lenguaje visual propio con la marca en vez de fotos de stock genéricas).

## 8. Cambios de la segunda revisión

- **Talentos eliminado**: `talentos.html`, `busco-talento.html` y `me-siento-talento.html` se han retirado del sitio (línea de negocio descartada). Se han limpiado los enlaces residuales que quedaban en 3 artículos del blog.
- **Precio de trasteros en Calafell corregido**: el artículo `blog_articles/trasteros-calafell.html` afirmaba en el título, meta descripción y FAQ un precio fijo ("desde 80€/mes") que contradecía la política real del sitio (precio a consultar). Se ha reformulado como rango orientativo de mercado, dejando claro que Blacknova confirma el precio exacto en cada consulta.
- **Los 16 artículos del blog se mantienen** (ver análisis abajo), pero se ha corregido un fallo de cumplimiento que tenían los 16: cargaban Google Tag Manager y Google Analytics de forma incondicional, antes de cualquier consentimiento — el mismo problema de RGPD/LSSI-CE que ya se había corregido en el resto del sitio meses atrás, pero que nunca se aplicó al blog. Ahora los 16 artículos cargan GTM/GA4 solo tras aceptar cookies, y cada uno tiene su propio banner de cookies funcional.

### Análisis: ¿merece la pena mantener los 16 artículos del blog?

Sí. Son contenido de calidad: texto largo y específico (no genérico), con datos estructurados correctos (Schema.org `Article` + `FAQPage`), buen enfoque de palabras clave locales (Calafell, Penedès, Tarragona, Barcelona) y un diseño coherente con la marca original (negro/dorado, mismas tipografías). Reescribirlos desde cero sería tirar trabajo de SEO ya bien hecho.

Lo que sí seria recomendable en una futura pasada (no urgente):
- Actualizar visualmente su cabecera/pie de página para que compartan la nueva paleta ámbar y el nuevo logo (ahora mismo siguen con el dorado `#b8965a` original, muy parecido pero no idéntico al nuevo `#c9822e`).
- Enlazar de forma cruzada más artículos entre sí (mejora el SEO interno).
