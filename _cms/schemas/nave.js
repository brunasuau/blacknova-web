// Schema de "Nave" (nave industrial) de Blacknova.
// Define los campos que se ven en el Studio (el panel) y que rellena la clienta a mano,
// nave por nave, a medida que las va gestionando. Es el mismo "molde" que consume el
// build para generar naves.html (listado) y naves/<slug>.html (ficha de cada nave).
//
// Nota de negocio: la gestión de naves es un servicio EN DESARROLLO (aún no hay naves
// reales gestionadas). Por eso el estado por defecto es "Próximamente" y casi todos los
// campos de datos concretos (precio, superficie, fotos...) son opcionales: se pueden
// rellenar poco a poco, nave a nave, sin que eso rompa nada en la web.

export const nave = {
  name: "nave",
  title: "Nave industrial",
  type: "document",
  fields: [
    {
      name: "title",
      title: "Nombre / referencia de la nave",
      type: "string",
      description:
        "Cómo la vas a reconocer tú y cómo se ve el título en la web. Ej: \"Nave industrial Vilafranca 800 m²\".",
      validation: (Rule) => Rule.required().max(120),
    },
    {
      name: "slug",
      title: "URL (slug)",
      type: "slug",
      description:
        "Se genera desde el nombre. Es la dirección: blacknova.es/naves/<slug>.html",
      options: { source: "title", maxLength: 80 },
      validation: (Rule) => Rule.required(),
    },
    {
      name: "zona",
      title: "Zona / población",
      type: "string",
      description:
        "Dónde está la nave (corredor Barcelona ↔ Tarragona). Ej: \"Vilafranca del Penedès\", \"El Vendrell\", \"Sant Sadurní d'Anoia\".",
      validation: (Rule) => Rule.required().max(80),
    },
    {
      name: "operacion",
      title: "Operación",
      type: "string",
      description: "¿Se alquila o se vende?",
      options: {
        list: [
          { title: "Alquiler", value: "Alquiler" },
          { title: "Venta", value: "Venta" },
        ],
        layout: "radio",
      },
      validation: (Rule) => Rule.required(),
    },
    {
      name: "estado",
      title: "Estado",
      type: "string",
      description:
        "Cómo aparece marcada la nave en la web. Usa \"Próximamente\" mientras todavía no se puede visitar/contratar.",
      options: {
        list: [
          { title: "Disponible", value: "Disponible" },
          { title: "Reservada", value: "Reservada" },
          { title: "Alquilada / Vendida", value: "Alquilada" },
          { title: "Próximamente", value: "Próximamente" },
        ],
        layout: "radio",
      },
      initialValue: "Próximamente",
      validation: (Rule) => Rule.required(),
    },
    {
      name: "superficieM2",
      title: "Superficie construida (m²)",
      type: "number",
      description: "Déjalo vacío si todavía no lo sabes con exactitud.",
      validation: (Rule) => Rule.positive(),
    },
    {
      name: "precio",
      title: "Precio",
      type: "string",
      description:
        "Texto libre: \"1.800 €/mes\", \"850.000 €\", \"A consultar\"... Déjalo vacío si aún no hay precio cerrado.",
      validation: (Rule) => Rule.max(60),
    },
    {
      name: "alturaLibre",
      title: "Altura libre",
      type: "string",
      description: "Ej: \"8 m\". Déjalo vacío si no aplica o no lo sabes todavía.",
      validation: (Rule) => Rule.max(30),
    },
    {
      name: "muelleCarga",
      title: "Muelle de carga",
      type: "boolean",
      description: "¿Tiene muelle de carga para camiones?",
      initialValue: false,
    },
    {
      name: "numMuelles",
      title: "Número de muelles",
      type: "number",
      description: "Solo si tiene muelle de carga. Déjalo vacío si no aplica.",
      validation: (Rule) => Rule.positive().integer(),
    },
    {
      name: "oficinas",
      title: "Oficinas",
      type: "boolean",
      description: "¿La nave incluye espacio de oficinas?",
      initialValue: false,
    },
    {
      name: "oficinasM2",
      title: "Superficie de oficinas (m²)",
      type: "number",
      description: "Solo si tiene oficinas. Déjalo vacío si no aplica.",
      validation: (Rule) => Rule.positive(),
    },
    {
      name: "caracteristicas",
      title: "Otras características",
      type: "array",
      description:
        "Añádelas una a una, como etiquetas. Ej: \"Suelo de hormigón pulido\", \"Trifásica 400V\", \"Parking para camiones\".",
      of: [{ type: "string" }],
      options: { layout: "tags" },
    },
    {
      name: "descripcion",
      title: "Descripción",
      type: "array",
      description: "Cuéntala como si se la explicaras a un cliente. Escribe como en un Word.",
      of: [
        {
          type: "block",
          // Solo los estilos que la ficha de nave sabe pintar (sin H2/H3: es una descripción corta).
          styles: [{ title: "Párrafo", value: "normal" }],
          lists: [{ title: "Lista", value: "bullet" }],
          marks: {
            decorators: [
              { title: "Negrita", value: "strong" },
              { title: "Cursiva", value: "em" },
            ],
          },
        },
      ],
    },
    {
      name: "galeria",
      title: "Fotos de la nave",
      type: "array",
      description:
        "Sube las fotos que tengas. Puedes dejarlo vacío por ahora y añadirlas más tarde: mientras no haya fotos, la web mostrará \"Fotos próximamente\".",
      of: [
        {
          type: "image",
          options: { hotspot: true },
          fields: [
            {
              name: "alt",
              title: "Descripción de la foto (para accesibilidad y SEO)",
              type: "string",
              description: "Ej: \"Fachada principal de la nave\", \"Interior nave diáfana\".",
            },
          ],
        },
      ],
    },
    {
      name: "destacada",
      title: "Ficha destacada",
      type: "boolean",
      description: "Actívalo para que esta nave salga primero y más destacada en el listado.",
      initialValue: false,
    },
    {
      name: "publishedAt",
      title: "Fecha de publicación",
      type: "datetime",
      description:
        "La nave aparece en la web SOLO si tiene fecha. Déjala vacía para guardarla como borrador mientras la preparas.",
      initialValue: () => new Date().toISOString(),
    },
  ],
  orderings: [
    {
      title: "Destacadas primero, luego más reciente",
      name: "destacadaDesc",
      by: [
        { field: "destacada", direction: "desc" },
        { field: "publishedAt", direction: "desc" },
      ],
    },
    {
      title: "Fecha de publicación (nueva primero)",
      name: "publishedAtDesc",
      by: [{ field: "publishedAt", direction: "desc" }],
    },
  ],
  preview: {
    select: {
      title: "title",
      zona: "zona",
      operacion: "operacion",
      estado: "estado",
      date: "publishedAt",
      media: "galeria.0",
    },
    prepare({ title, zona, operacion, estado, date, media }) {
      const estadoPub = date ? "🟢 Publicada" : "🟡 Borrador";
      return {
        title,
        subtitle: `${estadoPub} · ${estado || ""} · ${operacion || ""} · ${zona || ""}`,
        media,
      };
    },
  },
};
