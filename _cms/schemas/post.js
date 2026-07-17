// Schema del artículo de blog de Blacknova.
// Define los campos que se ven en el Studio (el panel) y que rellenan los agentes vía MCP.
// Es el mismo "molde" que consume el build para generar el HTML.

export const post = {
  name: "post",
  title: "Artículo de blog",
  type: "document",
  fields: [
    {
      name: "title",
      title: "Título (H1)",
      type: "string",
      description: "Título del artículo. También es el H1 y parte del <title> SEO.",
      validation: (Rule) => Rule.required().max(120),
    },
    {
      name: "slug",
      title: "URL (slug)",
      type: "slug",
      description:
        "Se genera desde el título. Es la dirección: blacknova.es/blog_articles/<slug>.html",
      options: { source: "title", maxLength: 80 },
      validation: (Rule) => Rule.required(),
    },
    {
      name: "category",
      title: "Categoría",
      type: "string",
      options: {
        list: [
          "Trasteros",
          "Naves industriales",
          "Patrimonio inmobiliario",
          "Gestión de proyectos",
          "Inversión",
        ],
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: "excerpt",
      title: "Resumen (para la tarjeta del blog)",
      type: "text",
      rows: 2,
      description: "1-2 frases. Es lo que se ve en la tarjeta de blog.html.",
      validation: (Rule) => Rule.required().max(200),
    },
    {
      name: "metaDescription",
      title: "Meta descripción (SEO)",
      type: "text",
      rows: 2,
      description:
        "Lo que ve Google en los resultados. Ideal 140-160 caracteres, con la keyword.",
      validation: (Rule) => Rule.max(165),
    },
    {
      name: "focusKeyword",
      title: "Keyword principal (SEO)",
      type: "string",
      description: "La palabra clave que quieres posicionar con este artículo.",
    },
    {
      name: "publishedAt",
      title: "Fecha de publicación",
      type: "datetime",
      description:
        "El artículo aparece en la web SOLO si tiene fecha. Déjala vacía para guardarlo como borrador.",
      initialValue: () => new Date().toISOString(),
    },
    {
      name: "body",
      title: "Contenido",
      type: "array",
      description: "El cuerpo del artículo. Escribe como en un Word.",
      of: [
        {
          type: "block",
          // Solo los estilos que la plantilla de Blacknova sabe pintar.
          styles: [
            { title: "Párrafo", value: "normal" },
            { title: "Subtítulo (H2)", value: "h2" },
            { title: "Subtítulo menor (H3)", value: "h3" },
          ],
          lists: [{ title: "Lista", value: "bullet" }],
          marks: {
            decorators: [
              { title: "Negrita", value: "strong" },
              { title: "Cursiva", value: "em" },
            ],
            annotations: [
              {
                name: "link",
                type: "object",
                title: "Enlace",
                fields: [{ name: "href", type: "url", title: "URL" }],
              },
            ],
          },
        },
      ],
      validation: (Rule) => Rule.required(),
    },
  ],
  orderings: [
    {
      title: "Fecha de publicación (nuevo primero)",
      name: "publishedAtDesc",
      by: [{ field: "publishedAt", direction: "desc" }],
    },
  ],
  preview: {
    select: { title: "title", subtitle: "category", date: "publishedAt" },
    prepare({ title, subtitle, date }) {
      const estado = date ? "🟢 Publicado" : "🟡 Borrador";
      return { title, subtitle: `${estado} · ${subtitle || ""}` };
    },
  },
};
