# Modem for Cursor

Turn customer feedback into action from Cursor. Modem connects customer conversations to your team’s work. Use the Modem Agent to triage bugs, create Linear issues, coordinate updates in Slack, and delegate fixes to coding agents with customer context. Build reusable skills and set up automations for weekly digests, priority alerts, and release updates.

## Example workflows

Ask Cursor to use the Modem Agent to:

- Triage a customer bug, find related reports, and create a Linear issue with the affected customers and source conversations.
- Create a reusable skill for your weekly customer feedback digest, then automate it every Monday in Slack.
- Set up an alert that DMs you in Slack when a topic becomes high priority, including affected customers and linked work.
- Investigate a customer bug and hand Devin the relevant context to work on a fix.
- Summarize what shipped when a pull request merges and share the update with your team in Slack.

These workflows use Modem’s connected integrations and your permissions. Coding-agent delegation requires the corresponding integration to be configured. Automations run in Modem on a schedule or after an event.

Learn more about [automations](https://modem.dev/docs/features/automations), [skills](https://modem.dev/blog/introducing-agent-skills), and [coding agents](https://modem.dev/docs/integrations/coding-agents).

## Install

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=modem&config=eyJ1cmwiOiJodHRwczovL21jcC5tb2RlbS5kZXYvbWNwIn0%3D)

One click with the button above (Cursor 3.15.12 or newer), install from the Cursor Marketplace, or add the remote server directly (**Settings** → **Tools & MCP**) with URL `https://mcp.modem.dev/mcp`.

The first tool use opens a browser window to authorize with your Modem account (OAuth — no API key). Select your organization and approve the permissions on the consent screen.

## Tools

14 tools against the hosted Modem MCP server: natural-language search (`search_modem`), asynchronous Modem Agent runs (`modem_agent_invoke` and friends), and workspace writes for topics, companies, and people. Writes act under your own role and are annotated destructive, so Cursor confirms them.

Full documentation: https://modem.dev/docs/api/modem-mcp-server · Support: support@modem.dev
