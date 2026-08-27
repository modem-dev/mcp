# Shared listing copy

Canonical copy for every directory submission. Length limits come from the strictest reviewer (Claude: tagline ≤55 chars, description 50–100 words). Source: readiness report §5.1.

| Field | Value |
| --- | --- |
| **Name** | Modem |
| **Tagline** (≤55 chars) | "The developer CRM, connected to your AI agent" (46) — alt: "Search and act on customer signals from your agent" (51) |
| **Categories** | Productivity · Sales & CRM · Developer tools |
| **Server URL** | `https://mcp.modem.dev/mcp` (Streamable HTTP, OAuth 2.1 + dynamic client registration) |
| **Website** | https://modem.dev |
| **Docs** | https://docs.modem.dev/api/modem-mcp-server |
| **Privacy** | https://modem.dev/privacy-policy |
| **Terms** | https://modem.dev/terms-of-service |
| **Trust** | https://trust.modem.dev |
| **Support** | support@modem.dev |

## Description (50–100 words)

> Modem is a CRM built for software teams. It aggregates customer signals from group chat (Slack, Discord), issue trackers (Linear, Jira, GitHub), support inboxes, and product tools into topics, people, and companies. This connector lets your agent search that knowledge base, ask the Modem agent questions in natural language, and keep records current — updating, merging, and organizing topics, companies, and people. Access is scoped to your organization through OAuth; read and write permissions are granted separately.

## Use cases (≥3)

1. "What are customers saying about [feature]?" — search topics and messages across every connected source.
2. Weekly triage: summarize the highest-priority topics and update their status without leaving your agent.
3. Account prep: pull everything Modem knows about a company before a call.
4. Data hygiene: merge duplicate people and companies, attach people to accounts.

## Tool inventory note (for reviewer forms)

> 14 tools: 1 gated by `data:read` (`search_modem`, read-only, annotated `readOnlyHint: true`), 13 gated by `agent:invoke` (4 agent-run tools + 9 workspace writes, annotated `destructiveHint` where applicable). All writes require org membership verified server-side from token claims; the model can never target another organization.

## Auth description (for reviewer forms)

> OAuth 2.1 with Dynamic Client Registration (RFC 7591, open registration — no pre-shared client needed). Authorization server: `https://app.modem.dev/api/auth`; RFC 9728 protected-resource metadata served at `/.well-known/oauth-protected-resource/mcp`. Callback allow-listing not required.

## Screenshot shot list (capture with the seeded demo org — DEV-3920)

1. Agent answering a "what are customers saying about X" query with cited topics
2. A topic being updated from chat, then shown in the Modem dashboard
3. The OAuth consent screen with org selection
4. `search_modem` results in Claude/ChatGPT
5. Company 360° view assembled by the agent

## Longer copy

The Slack manifest (`apps/slack/manifest.prod.json` in the monorepo) contains an approved long description, AI disclaimer, and pricing blurb — mine it for any directory wanting longer copy.

## awesome-mcp-servers PR line (alphabetical, category: Customer Data / Sales)

```markdown
- [Modem](https://docs.modem.dev/api/modem-mcp-server) — Developer-focused CRM: search customer
  signals from chat, issues, and support; update topics, people, and companies.
  Remote (Streamable HTTP + OAuth): https://mcp.modem.dev/mcp
```
