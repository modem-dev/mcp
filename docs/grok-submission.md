# Modem on Grok: package and submission routes

Verified September 24, 2026. Marketplace acceptance and authenticated Grok testing are pending.

## Which Grok surface?

| Surface | Verified route | Next action |
| --- | --- | --- |
| Grok Build | Public plugin PR to `xai-org/plugin-marketplace` | Test this package, publish its source, then submit a pinned catalog entry |
| Grok chat on grok.com and the Grok apps | Bring-your-own remote MCP; a separate catalog of preconfigured connectors also exists | Test Modem as a Custom connector; ask xAI how vendors enter the catalog |
| Grok Bot | Cursor plugin infrastructure and marketplace controls | Check the existing Modem listing inside Grok Bot before creating any new application |
| Grok inside X | No public plugin submission or custom MCP setup route found in the official sources reviewed | Ask xAI whether catalog connectors are available inside X and whether a separate review is required |

Sources: [Build marketplace](https://x.ai/news/grok-plugin-marketplace), [Grok connectors](https://docs.x.ai/grok/connectors), [web/mobile availability](https://x.ai/news/grok-connectors), [Grok Bot connector policy](https://docs.x.ai/grok-bot/teams-and-enterprises), [Grok Bot plugin help](https://cursor.com/help/grok-bot/connect-plugins), [Grok on X](https://help.x.com/en/using-x/about-grok).

**Existing distribution:** [Modem is publicly listed in Cursor's marketplace](https://cursor.com/marketplace/modem), with Modem as publisher and the Modem GitHub repository as source. The shared plugin layer makes that the first Grok Bot route to test. Its actual availability and OAuth behavior inside Grok Bot have not been verified.

“Official Modem plugin” means maintained by Modem. An xAI catalog listing does not mean xAI endorses the plugin; its [marketplace README](https://github.com/xai-org/plugin-marketplace) explicitly distinguishes third-party plugins.

## Prepared package

- Source: `plugins/grok`.
- Metadata: `plugins/grok/.grok-plugin/plugin.json`.
- MCP configuration: `plugins/grok/.mcp.json`.
- Publisher-owned marketplace: `.grok-plugin/marketplace.json`.
- Component index: `.grok-plugin/plugin-index.json`, generated with xAI's public index generator.
- Install and test instructions: [package README](../plugins/grok/README.md).
- Existing backend: `https://mcp.modem.dev/mcp`; no new hosted service required by this design.

The native package follows xAI's [plugin format](https://docs.x.ai/build/features/skills-plugins-marketplaces) and [accepted MCP configuration](https://github.com/xai-org/plugin-marketplace/blob/main/external_plugins/neon/.mcp.json). xAI also supports Claude-compatible plugins, so the existing Claude package remains a reuse option.

## Build marketplace submission

1. Run the package README's Grok validation, discovery, OAuth, and read-only search checks. Save results without customer content.
2. Publish the reviewed package to `modem-dev/mcp`. Record a reachable full commit SHA containing `plugins/grok`.
3. Recheck xAI's catalog and open PRs for `modem` to avoid duplicates.
4. Fork [xAI's marketplace](https://github.com/xai-org/plugin-marketplace), branch from `main`, and add one entry to `.grok-plugin/marketplace.json`.
5. Generate the index and run the official checks below. Include `.grok-plugin/plugin-index.json` in the PR.
6. Complete the [PR template](https://github.com/xai-org/plugin-marketplace/blob/main/.github/PULL_REQUEST_TEMPLATE.md), submit, and handle reviewer feedback. After acceptance, verify installation from the official catalog.

These are the [published contribution steps](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md). No review turnaround is promised.

Run in the xAI marketplace checkout:

```bash
python3 scripts/generate-plugin-index.py
python3 scripts/validate-catalog.py
python3 scripts/generate-plugin-index.py --check
```

Catalog entry to prepare **after publication**. The SHA below is an explicit template value, not a valid submission:

```json
{
  "name": "modem",
  "description": "Search customer feedback in Modem, update topics, people, and companies, and run the Modem Agent from Grok Build.",
  "category": "productivity",
  "source": {
    "source": "url",
    "url": "https://github.com/modem-dev/mcp.git",
    "sha": "REPLACE_WITH_PUBLISHED_40_CHARACTER_COMMIT_SHA",
    "path": "plugins/grok"
  },
  "homepage": "https://modem.dev",
  "keywords": ["modem", "modem mcp", "modem crm"],
  "domains": ["modem.dev"]
}
```

The source object and subdirectory field match the [current catalog format](https://github.com/xai-org/plugin-marketplace/blob/main/.grok-plugin/marketplace.json). Product-specific discovery terms avoid triggering this plugin for unrelated CRM or database requests.

## Review copy

| Review detail | Answer |
| --- | --- |
| Maintainer | Modem; source under `modem-dev` |
| Contact | support@modem.dev |
| Purpose | Bring customer evidence into Grok Build; search Modem and perform authorized workspace updates |
| Components | One HTTP MCP server; no local executable, hooks, skills, agents, or LSP |
| License | MIT package; hosted service governed by Modem's terms |
| Network | MCP at `mcp.modem.dev/mcp`; OAuth under `app.modem.dev/api/auth` |
| Credentials | Browser OAuth; requires a Modem account and organization |
| Permissions | `data:read` for search; `agent:invoke` for agent runs and workspace writes; `offline_access` where requested |
| Data flow | Queries and instructions go to Modem; results are returned to Grok. Authorized agent runs may use connected integrations |
| Test status | Public authentication discovery checked; authenticated Grok test still pending |

## Grok chat setup and catalog inquiry

- For a personal account, use [Grok Connectors](https://grok.com/connectors) → New Connector → Custom → `https://mcp.modem.dev/mcp`, then complete authentication.
- Business/Enterprise admins first provision the connector in the [team console](https://docs.x.ai/grok/connector-management).
- Verify OAuth discovery, organization selection, consent scopes, tool discovery, and one `search_modem` call using suitable demo data. Capture any required client registration fields from the actual UI; do not guess callback URLs.
- A Custom connection is not a catalog application. No public vendor intake form for the Grok chat catalog was found in the official documentation reviewed.

## Verification record

- Static checks passed: JSON parsing, package and config paths, plugin identity, endpoint, and license consistency. xAI's catalog validator accepted the local catalog; its component extractor found version `0.1.0` and one HTTP MCP server named `modem`. Its index generator produced the local component index and a second generation matched exactly. These checks do not exercise Grok's runtime.
- The live xAI catalog contained no Modem entry. A GitHub PR search for `modem` across all states returned no matches; this is a duplicate check, not a guarantee against differently named submissions.
- September 24, 2026: unauthenticated MCP initialization returned HTTP 401 and `WWW-Authenticate` pointing to `https://mcp.modem.dev/.well-known/oauth-protected-resource/mcp`.
- Protected-resource metadata returned the correct MCP resource, `https://app.modem.dev/api/auth` as authorization server, and `offline_access`, `agent:invoke`, `data:read` scopes.
- Authorization-server metadata advertises dynamic registration, authorization-code and refresh-token flows, public-client authentication (`none`), and PKCE S256. This is discovery evidence, not a completed OAuth test.
- Official Grok Build 1.0.41 (`4220f3b224a6`) passed `grok plugin validate`; isolated local installation succeeded and `grok plugin list --json` reported Modem 0.1.0 from this package. `grok inspect --json` confirmed the MCP server originated from the installed Modem plugin and targeted `https://mcp.modem.dev/mcp`. Authenticated end-to-end testing remains open.
- No customer data was fetched through Grok and no OAuth grant was created during package validation.
