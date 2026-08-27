# Modem MCP Server

Connect the [Modem](https://modem.dev) developer CRM to any MCP-compatible client — search customer signals from chat, issue trackers, and support inboxes, run the Modem Agent, and update topics, people, and companies directly from your assistant.

```text
https://mcp.modem.dev/mcp
```

- **Transport**: Streamable HTTP
- **Auth**: OAuth 2.1 with Dynamic Client Registration — no API key to create or paste
- **Docs**: https://docs.modem.dev/api/modem-mcp-server

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

**Settings** → **Cursor Settings** → **Tools & MCP** → add a new MCP server, or add to `mcp.json`:

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
```

If you edit `config.toml` directly, you still need `codex mcp login modem` to complete OAuth.

### Gemini CLI

This repo is a Gemini CLI extension (see [`gemini-extension.json`](gemini-extension.json)):

```bash
gemini extensions install https://github.com/modem-dev/mcp
```

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

### Any other MCP client

| Field | Value |
| --- | --- |
| Name | `modem` |
| URL | `https://mcp.modem.dev/mcp` |
| Transport | Streamable HTTP (or "HTTP") |
| Authentication | OAuth |

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

**For the Modem team**: submission copy, portal answers, test cases, and the per-directory tracker live in [`submissions/`](submissions/). Plugin packages for Cursor and Claude Code live in [`plugins/`](plugins/).
