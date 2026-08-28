# Modem for Claude Code

Connects Claude Code to [Modem](https://modem.dev), the developer CRM — search customer signals from chat, issue trackers, and support inboxes, run the Modem Agent, and update topics, people, and companies.

## Install

```bash
/plugin marketplace add modem-dev/mcp
/plugin install modem
```

The first tool use opens a browser window to authorize with your Modem account (OAuth — no API key). Select your organization and approve the permissions on the consent screen.

## Tools

14 tools against the hosted Modem MCP server (`https://mcp.modem.dev/mcp`): natural-language search (`search_modem`), asynchronous Modem Agent runs (`modem_agent_invoke` and friends), and workspace writes for topics, companies, and people. Writes act under your own role and are annotated destructive, so Claude Code confirms them.

Full documentation: https://modem.dev/docs/api/modem-mcp-server · Support: support@modem.dev
