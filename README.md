# Modem MCP Server

Connect [Modem](https://modem.dev) to any MCP-compatible client. Modem builds a custom context graph of your customers and product, grouping disparate data from chat, issue trackers, and support inboxes into topics, people, and companies. From your assistant you can search that graph, run the Modem Agent, and update your workspace directly.

```text
https://mcp.modem.dev/mcp
```

- **Transport**: Streamable HTTP
- **Auth**: OAuth 2.1 with Dynamic Client Registration — no API key to create or paste
- **Docs**: https://modem.dev/docs/api/modem-mcp-server

> This repo holds the public manifests, install docs, and listing assets for the Modem MCP server. The server itself is a hosted service; there is nothing to run from this repo.

## What you can do

| Kind | Tools | Scope |
| --- | --- | --- |
| Run the Modem Agent | `modem_agent_invoke`, `modem_agent_get_run`, `modem_agent_send_message`, `modem_agent_cancel_run` | `agent:invoke` |
| Search your data | `search_modem` — natural-language search over topics, messages, people, companies | `data:read` |
| Update your workspace | `update_topic`, `bulk_update_topics`, `merge_topics`, `create_companies`, `update_companies`, `merge_companies`, `add_people_to_company`, `update_people`, `merge_people` | `agent:invoke` |

Write tools act as **you**, under your existing role in the organization you authorize — never more access than your Modem account already has. All writes are annotated destructive, so most clients confirm each call.

## Install

In every client, the server URL is `https://mcp.modem.dev/mcp`. The first connection opens a browser window for OAuth authorization.

### Claude Code

```bash
claude mcp add --transport http modem https://mcp.modem.dev/mcp
```

Then run `/mcp` inside Claude Code and complete the browser authorization flow.

### Cursor

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=modem&config=eyJ1cmwiOiJodHRwczovL21jcC5tb2RlbS5kZXYvbWNwIn0%3D)

Or **Settings** → **Cursor Settings** → **Tools & MCP** → add a new MCP server, or add to `mcp.json`:

```json
{
    "mcpServers": {
        "modem": {
            "url": "https://mcp.modem.dev/mcp"
        }
    }
}
```

If Cursor asks for a transport type, choose **Streamable HTTP**.

### Grok Build and Grok chat

The Grok Build package is under [`plugins/grok`](plugins/grok/README.md), with local install and verification steps. [Source PR #8](https://github.com/modem-dev/mcp/pull/8) and [xAI marketplace PR #907](https://github.com/xai-org/plugin-marketplace/pull/907) are open for review. Native Build OAuth, tool discovery, and one read-only search passed a smoke test with Grok Build 1.0.41 on September 24, 2026.

For Grok chat, add a Custom connector at [grok.com/connectors](https://grok.com/connectors) using `https://mcp.modem.dev/mcp` and complete authentication. OAuth and a read-only search passed in a demo test on September 24, 2026. Availability inside Grok on X remains unconfirmed. See [Grok submission notes](docs/grok-submission.md) for the separate Build, chat, Bot, and X distribution paths.

### VS Code / GitHub Copilot

In your user profile `mcp.json` or workspace `.vscode/mcp.json`:

```json
{
    "servers": {
        "modem": {
            "type": "http",
            "url": "https://mcp.modem.dev/mcp"
        }
    }
}
```

Or use **MCP: Add Server** from the command palette.

### Codex

```bash
codex mcp add modem --url https://mcp.modem.dev/mcp
codex mcp login modem
```

Or in `~/.codex/config.toml`:

```toml
[mcp_servers.modem]
url = "https://mcp.modem.dev/mcp"
auth = "oauth"
```

`auth` defaults to `oauth`, so it can be omitted. If you edit `config.toml` directly, you still need `codex mcp login modem` to complete OAuth.

### Gemini CLI

This repo is a Gemini CLI extension (see [`gemini-extension.json`](gemini-extension.json)):

```bash
gemini extensions install https://github.com/modem-dev/mcp
```

Then authorize when prompted on first use (or run `/mcp auth modem` inside Gemini CLI).

### opencode

In `opencode.json`:

```json
{
    "$schema": "https://opencode.ai/config.json",
    "mcp": {
        "modem": {
            "type": "remote",
            "url": "https://mcp.modem.dev/mcp"
        }
    }
}
```

Then `opencode mcp auth modem` (or authorize when prompted on first use).

### ChatGPT

ChatGPT connects to remote MCP servers through **Developer mode**, available on paid plans. Depending on your ChatGPT version the setting lives under **Settings** → **Security and login**, or under **Apps** (previously **Connectors**) → **Advanced settings**.

1. Enable **Developer mode**.
2. In the apps/connectors list, click the add (**+**) button to create a new connection.
3. Give it a name such as `Modem` and enter the server URL `https://mcp.modem.dev/mcp`.
4. If asked for an authentication type, choose **OAuth**. Create the connection.
5. Complete the Modem authorization flow in the browser window that opens, then review the discovered tools.

In a conversation, enable the Modem connection from the composer's tools menu. ChatGPT asks for confirmation before running write tools.

### Any other MCP client

| Field | Value |
| --- | --- |
| Name | `modem` |
| URL | `https://mcp.modem.dev/mcp` |
| Transport | Streamable HTTP (or "HTTP") |
| Authentication | OAuth |

## Add in-app feedback

The Cursor and Claude plugin packages include the native `install-feedback` skill.
Ask your coding agent:

> Add in-app feedback to this app with Modem. Use the installed Modem skill if available, or ask `modem_skills` for `install-feedback`. If Modem is not connected, help me connect it and then continue. If I have not named a feedback surface, offer a few choices and recommend one after inspecting the app.

The skill loads the current setup guide from the main OAuth Modem MCP. It can use
that guide to help choose UI, configure a feedback channel, implement submission,
and verify delivery. It needs a hosted server that exposes `install-feedback`;
if the guide is unavailable, the agent reports that and can still help plan the UI.

Install the [Cursor plugin](plugins/cursor/README.md) or
[Claude plugin](plugins/claude/README.md) to get the native skill. A direct MCP
connection gives the agent tools; use the same prompt to request the guide.
For a client that supports importing skill files, use the public
[`install-feedback` skill](skills/install-feedback/SKILL.md) or its
[raw URL](https://raw.githubusercontent.com/modem-dev/mcp/main/skills/install-feedback/SKILL.md).
OAuth authorization remains a separate client step.

## Example prompts

- "What are customers saying about billing in the last month?"
- "Summarize the three highest-priority open topics and who's affected."
- "Mark the topic about SSO login failures as high priority in Modem."
- "Find the duplicate Acme companies in Modem and merge them into the one with the acme.com domain."

## Security and access

- OAuth tokens are scoped to the account and organization selected on the consent screen; the server resolves the organization from token claims, never from the URL.
- Two permissions, granted separately: `data:read` (natural-language search only) and `agent:invoke` (agent runs + workspace writes).
- Tool calls are rate limited per organization, per tool (20/min).
- Privacy policy: https://modem.dev/privacy-policy · Terms: https://modem.dev/terms-of-service · Trust center: https://trust.modem.dev

## Support

Questions or issues: [support@modem.dev](mailto:support@modem.dev)

---

Plugin packages for Cursor, Claude Code, and Grok Build live in [`plugins/`](plugins/).

## Maintaining the feedback skill

Edit `skills/install-feedback/SKILL.md`, then run:

```bash
python3 scripts/sync-feedback-skill.py
python3 scripts/sync-feedback-skill.py --check
```

The script copies the canonical skill into each plugin so downloaded packages
contain their own skill file. Keep detailed API and setup instructions in the
hosted `modem_skills` guide. Check plugin manifests and test a fresh client session
before releasing a package update; merging this repository does not itself prove
marketplace publication.
