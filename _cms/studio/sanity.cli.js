// CLI de Sanity: define a qué proyecto apunta `sanity deploy`, `sanity dev`, etc.
// Usa el mismo Project ID que sanity.config.js.

import { defineCliConfig } from "sanity/cli";

export default defineCliConfig({
  api: {
    projectId: "w7ezq063",
    dataset: "production",
  },
  // El Studio quedará online en https://blacknova.sanity.studio
  studioHost: "blacknova",
});
