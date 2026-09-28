# Modem for Cursor

Connects Cursor to [Modem](https://modem.dev), the developer CRM — search customer signals from chat, issue trackers, and support inboxes, run the Modem Agent, and update topics, people, and companies.

## Install

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=modem&config=eyJ1cmwiOiJodHRwczovL21jcC5tb2RlbS5kZXYvbWNwIn0%3D)

One click with the button above (Cursor 3.15.12 or newer), install from the Cursor Marketplace, or add the remote server directly (**Settings** → **Tools & MCP**) with URL `https://mcp.modem.dev/mcp`.

The first tool use opens a browser window to authorize with your Modem account (OAuth — no API key). Select your organization and approve the permissions on the consent screen.

## Tools

14 tools against the hosted Modem MCP server: natural-language search (`search_modem`), asynchronous Modem Agent runs (`modem_agent_invoke` and friends), and workspace writes for topics, companies, and people. Writes act under your own role and are annotated destructive, so Cursor confirms them.

## Skills

| Skill | What it does |
| --- | --- |
| `customer-context` | Finds the Modem topics, customers, and linked work behind the bug or feature you're changing |
| `topic-to-plan` | Turns a Modem topic into a repro and fix plan, citing customer messages and the likely files |
| `mark-topic-shipped` | After a merge, marks the matching topic completed and lists who to tell |
| `customer-signals-canvas` | Opens a canvas of top open topics, bugs versus feature requests, and the most active companies |
| `dedupe-records` | Finds duplicate companies, people, or topics and merges the sets you approve |

## Commands

- `/who-asked` finds the customers behind the current task.
- `/customer-digest` opens the customer signals canvas for the last 30 days.
- `/mark-shipped` marks the topic this work resolves as completed.

## Rule

`modem-customer-context` runs in Agent Decides mode. It tells the agent to check Modem before changing user-facing behavior and to call write tools only when you ask.

Full documentation: https://modem.dev/docs/api/modem-mcp-server · Support: support@modem.dev
