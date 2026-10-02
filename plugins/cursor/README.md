# Modem for Cursor

Connects Cursor to [Modem](https://modem.dev), the developer CRM — search customer signals from chat, issue trackers, and support inboxes, run the Modem Agent, and update topics, people, and companies.

## Install

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=modem&config=eyJ1cmwiOiJodHRwczovL21jcC5tb2RlbS5kZXYvbWNwIn0%3D)

Install [Modem from the Cursor Marketplace](https://cursor.com/marketplace/modem)
to get the MCP connection and bundled skills.

The button above adds only the MCP connection. You can also add the remote server
directly in **Settings** → **Tools & MCP** with URL `https://mcp.modem.dev/mcp`.

The first tool use opens a browser window to authorize with your Modem account (OAuth — no API key). Select your organization and approve the permissions on the consent screen.

## Add in-app feedback

The bundled `install-feedback` skill helps add feedback collection to your app.
Ask Cursor:

> Add in-app feedback to this app with Modem.

You can name a specific page, feature, or control in the request. The skill loads
current setup guidance from `modem_skills({ "name": "install-feedback" })` on the
main OAuth MCP, then follows that guide through UI choices, channel setup,
implementation, and staged verification. If the hosted guide is unavailable, the
agent reports the missing capability before attempting setup.

With a direct MCP connection, ask Cursor to load the same `modem_skills` guide,
or import the [public skill file](../../skills/install-feedback/SKILL.md) using
Cursor's skill installation support.

## Tools

Tools from the hosted Modem MCP server include natural-language search (`search_modem`), asynchronous Modem Agent runs (`modem_agent_invoke` and friends), and workspace writes for topics, companies, and people. Writes act under your own role and are annotated destructive, so Cursor confirms them.

Full documentation: https://modem.dev/docs/api/modem-mcp-server · Support: support@modem.dev
