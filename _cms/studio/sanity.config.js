// Configuración del Sanity Studio de Blacknova (el panel donde escribes/revisas artículos).
//
// ⚠️ Rellena projectId con el ID de tu proyecto de Sanity (lo obtienes al crearlo,
//    o en sanity.io/manage). Es lo ÚNICO que hay que tocar aquí.

import { defineConfig } from "sanity";
import { structureTool } from "sanity/structure";
import { post } from "../schemas/post.js";
import { nave } from "../schemas/nave.js";

export default defineConfig({
  name: "blacknova",
  title: "Blacknova · Blog y Naves",

  projectId: "w7ezq063",
  dataset: "production",

  plugins: [
    structureTool({
      structure: (S) =>
        S.list()
          .title("Contenido")
          .items([
            S.listItem()
              .title("Artículos de blog")
              .child(S.documentTypeList("post").title("Artículos de blog")),
            S.listItem()
              .title("Naves industriales")
              .child(S.documentTypeList("nave").title("Naves industriales")),
          ]),
    }),
  ],

  schema: {
    types: [post, nave],
  },
});
