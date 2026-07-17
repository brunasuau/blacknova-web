# MCP de Sanity para los agentes de SuauMarketing

Permite que tus agentes (estratega, seo-specialist, copywriter…) **creen y publiquen
artículos directamente en Sanity**.

> ⚠️ El MCP **local** (`@sanity/mcp-server`, vía npx) está **DEPRECADO**.
> Ahora se usa el **servidor remoto** `https://mcp.sanity.io` con **OAuth** (sin tokens que gestionar),
> igual que los conectores de Google Drive / Gmail.

## Cómo se conecta (Claude Code)

Ya está añadido en la config de usuario con:

```bash
claude mcp add --transport http sanity-blacknova https://mcp.sanity.io -s user
```

Y se autoriza una sola vez desde Claude Code:

```
/mcp   →  sanity-blacknova  →  Authenticate  (se abre el navegador, das Allow)
```

Queda en estado `✔ Connected`. La autorización persiste (no hay que repetirla).

## Config equivalente (otros clientes MCP)

```json
{
  "mcpServers": {
    "sanity": {
      "url": "https://mcp.sanity.io",
      "type": "http"
    }
  }
}
```

- **Auth por OAuth** (recomendado): no hay que meter ningún token.
- **Alternativa por token**: se puede pasar `Authorization: Bearer <token>` en las cabeceras
  del MCP; entonces no usa OAuth y opera con los permisos de ese token (el `agents-write`
  con rol *Editor* que se creó en Manage → API → Tokens).

## Qué podrán hacer los agentes

- Crear artículos nuevos (tipo `post`) con título, categoría, cuerpo, meta descripción y keyword.
- Actualizar borradores existentes.
- Consultar qué hay publicado para no duplicar temas.

## Flujo recomendado con los agentes

1. Le dices al equipo (o al `seo-specialist`): *"escribe un artículo para la keyword X"*.
2. El agente lo crea en Sanity (proyecto `w7ezq063`, dataset `production`) como **borrador**.
3. Tú lo revisas en el Studio y das **Publish** → se publica solo en la web.
