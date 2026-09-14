# Modem for Cursor

Connects Cursor to [Modem](https://modem.dev), the developer CRM — search customer signals from chat, issue trackers, and support inboxes, run the Modem Agent, and update topics, people, and companies.

## Install

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=modem&config=eyJ1cmwiOiJodHRwczovL21jcC5tb2RlbS5kZXYvbWNwIn0%3D)

Use the button above to add the MCP server directly, or add this configuration to your project's `.cursor/mcp.json` (merge it into `mcpServers` if the file already exists):

```json
{
    "mcpServers": {
        "modem": {
            "url": "https://mcp.modem.dev/mcp"
        }
    }
}
```

The direct install works independently of a Cursor Marketplace listing.

The first tool use opens a browser window to authorize with your Modem account (OAuth — no API key). Select your organization and approve the permissions on the consent screen.

## Tools

The hosted Modem MCP server provides natural-language search (`search_modem`), asynchronous Modem Agent runs (`modem_agent_invoke` and related tools), and workspace writes for topics, companies, and people. Writes act under your own role. Cursor's approval settings determine when it asks before executing tools; tool annotations do not guarantee a confirmation prompt.

Try: "Search Modem for the most common customer complaints about file uploads. Include supporting sources. Do not change any data."

## Test the plugin package locally

From the repository root, copy the package into a new local plugin directory:

```bash
mkdir -p ~/.cursor/plugins/local
test ! -e ~/.cursor/plugins/local/modem && cp -R plugins/cursor ~/.cursor/plugins/local/modem
```

If that destination already exists, review it before replacing it. Copy the files rather than symlinking to a repository outside `~/.cursor/plugins/local`; current Cursor documentation says those symlinks are skipped.

1. Restart Cursor or run **Developer: Reload Window**.
2. Open **Customize** and verify the Modem plugin and MCP server appear. Team policy must allow local plugin imports. An installed marketplace plugin with the same name takes precedence.
3. Complete Modem OAuth and select the intended organization.
4. Run the read-only example above and verify that the returned sources belong to that organization.
5. Record the Cursor version, date, and result before submitting. A direct MCP connection alone does not test plugin discovery.

## Data and access

- Requires a Modem account and organization. Modem plan limits apply.
- Requests go to the hosted service at `https://mcp.modem.dev/mcp` over Streamable HTTP; there is no local server process or API key to provision.
- OAuth grants `data:read` for search and `agent:invoke` for agent runs and workspace writes. Review the permissions requested during authorization.
- Retrieved customer context becomes available to your Cursor session. Agent runs can use integrations connected to your Modem organization.
- [Privacy policy](https://modem.dev/privacy-policy) · [Terms](https://modem.dev/terms-of-service)

Package publishing instructions: [Cursor Marketplace submission](../../docs/cursor-marketplace.md).

Full documentation: https://modem.dev/docs/api/modem-mcp-server · Support: support@modem.dev
