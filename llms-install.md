# Installing the Modem MCP server (for AI agents)

Modem is a **hosted remote MCP server**. There is nothing to clone, build, or run locally.

## Configuration

Add a remote MCP server with these values:

- **URL**: `https://mcp.modem.dev/mcp`
- **Transport**: Streamable HTTP
- **Authentication**: OAuth (the server supports Dynamic Client Registration; no API key or pre-shared client credentials are needed)

Example (Cline / generic `mcpServers` shape):

```json
{
    "mcpServers": {
        "modem": {
            "url": "https://mcp.modem.dev/mcp",
            "type": "streamableHttp"
        }
    }
}
```

## After configuration

1. The client opens a browser window for OAuth on first connection.
2. The user signs in with their Modem account, selects an organization, and approves the requested permissions (`data:read` for search, `agent:invoke` for agent runs and workspace writes).
3. Tools appear according to the approved scopes. If only `search_modem` is visible, the token carries `data:read` only — re-authorize and approve both permissions for the full tool set.

## Requirements

- A Modem account (https://modem.dev) with access to the organization to connect
- An MCP client that supports remote Streamable HTTP servers with OAuth

Full documentation: https://docs.modem.dev/api/modem-mcp-server
