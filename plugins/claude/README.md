# Modem for Claude

Connects Claude Code to [Modem](https://modem.dev), the developer CRM — search customer signals from chat, issue trackers, and support inboxes, run the Modem Agent, and update topics, people, and companies.

## Install in Claude Code

```bash
/plugin marketplace add modem-dev/mcp
/plugin install modem
```

The first tool use opens a browser window to authorize with your Modem account (OAuth — no API key). Select your organization and approve the permissions on the consent screen.

## Install in Claude chat or Cowork

In **Customize → Plugins → Add → Add marketplace**, enter
`https://github.com/modem-dev/mcp`, then add Modem. Open the plugin's **Connectors**
tab and add or connect Modem with your account. Installing the plugin alone does
not authorize the connector. Organization policy may require an owner to add it.
See [Claude's plugin instructions](https://claude.com/docs/plugins/overview).

The plugin uses a remote connector declared in `.mcp.json`, the shared layout for
[Claude chat, Cowork, and Claude Code](https://claude.com/docs/plugins/build).

## Add in-app feedback

Ask Claude in your app workspace:

> Add in-app feedback to this app with Modem.

Or invoke `/modem:install-feedback` in Claude Code. The native skill loads the
current guide with `modem_skills({ "name": "install-feedback" })` from the main
OAuth Modem MCP. It follows that guide through UI choices, channel setup,
implementation, and staged verification. If the hosted guide is unavailable, the
agent reports the missing capability before attempting setup.

Claude needs access to your app files to implement the integration. In a chat
without file-editing access, it can help plan the UI and hand the work to your
coding environment. Connecting only the MCP does not install the native skill;
you can still ask the agent to load the tool-served guide.

## Tools

Tools from the hosted Modem MCP server (`https://mcp.modem.dev/mcp`) include natural-language search (`search_modem`), asynchronous Modem Agent runs (`modem_agent_invoke` and friends), and workspace writes for topics, companies, and people. Writes act under your own role and are annotated destructive, so Claude Code confirms them.

Full documentation: https://modem.dev/docs/api/modem-mcp-server · Support: support@modem.dev
