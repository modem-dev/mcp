# Modem on Grok: package and submission routes

Status as of September 24, 2026:

- [Source PR #8](https://github.com/modem-dev/mcp/pull/8) and [xAI marketplace PR #907](https://github.com/xai-org/plugin-marketplace/pull/907) are open for review. Neither has been merged; marketplace acceptance remains pending.
- Grok chat OAuth and a read-only search passed in a demo test on September 24, 2026.
- Native Grok Build authentication and read-only search testing remain pending with a Modem-controlled xAI account. The chat test does not establish native Build compatibility.
- Availability inside Grok on X remains unconfirmed.

## Which Grok surface?

| Surface | Verified route | Next action |
| --- | --- | --- |
| Grok Build | Source PR #8 and xAI marketplace PR #907 are open for review | Complete native authentication/search testing with a Modem-controlled xAI account and handle review feedback |
| Grok chat on grok.com and the Grok apps | Bring-your-own remote MCP; a separate catalog of preconfigured connectors also exists | Web chat OAuth and read-only search passed; ask xAI how vendors enter the catalog |
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

Continue the existing source PR #8 and marketplace PR #907; do not open duplicate submissions.

1. Complete the package README's native OAuth and read-only search checks with a Modem-controlled xAI account. Save results without customer content. Native validation, installation, and discovery have already passed.
2. Address source review in `modem-dev/mcp` and keep the reviewed package reachable at a full commit SHA containing `plugins/grok`.
3. If the source commit changes, update the pinned SHA in marketplace PR #907, regenerate `.grok-plugin/plugin-index.json`, and run the official checks below.
4. Keep the [PR template](https://github.com/xai-org/plugin-marketplace/blob/main/.github/PULL_REQUEST_TEMPLATE.md) answers current and handle reviewer feedback. After acceptance, verify installation from the official catalog.

The [published contribution guide](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md) does not require a completed authenticated native test before requesting review. Keep the pending test disclosed. No review turnaround is promised.

Run in the xAI marketplace checkout:

```bash
python3 scripts/generate-plugin-index.py
python3 scripts/validate-catalog.py
python3 scripts/generate-plugin-index.py --check
```

Catalog entry format for future updates. PR #907 contains the actual pinned entry; the SHA below is an explicit template value, not a valid submission:

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
| Test status | Native validation/install/discovery passed; Grok chat OAuth/read-only search passed September 24, 2026; native Build authentication/search pending with a Modem-controlled xAI account |

## Grok chat setup and catalog inquiry

- For a personal account, use [Grok Connectors](https://grok.com/connectors) → New Connector → Custom → `https://mcp.modem.dev/mcp`, then complete authentication.
- Business/Enterprise admins first provision the connector in the [team console](https://docs.x.ai/grok/connector-management).
- Verify OAuth discovery, organization selection, consent scopes, tool discovery, and one `search_modem` call using suitable demo data. Capture any required client registration fields from the actual UI; do not guess callback URLs.
- A Custom connection is not a catalog application. No public vendor intake form for the Grok chat catalog was found in the official documentation reviewed.

## Verification record

- Static checks passed: JSON parsing, package and config paths, plugin identity, endpoint, and license consistency. xAI's catalog validator accepted the local catalog; its component extractor found version `0.1.0` and one HTTP MCP server named `modem`. Its index generator produced the local component index and a second generation matched exactly. These checks do not exercise Grok's runtime.
- Before submission, the live xAI catalog contained no Modem entry and a GitHub PR search for `modem` across all states returned no matches. Source PR #8 and marketplace PR #907 are now open for review; no listing acceptance has been verified.
- September 24, 2026: unauthenticated MCP initialization returned HTTP 401 and `WWW-Authenticate` pointing to `https://mcp.modem.dev/.well-known/oauth-protected-resource/mcp`.
- Protected-resource metadata returned the correct MCP resource, `https://app.modem.dev/api/auth` as authorization server, and `offline_access`, `agent:invoke`, `data:read` scopes.
- Authorization-server metadata advertises dynamic registration, authorization-code and refresh-token flows, public-client authentication (`none`), and PKCE S256. This is discovery evidence, not a completed OAuth test.
- Official Grok Build 1.0.41 (`4220f3b224a6`) passed `grok plugin validate`; isolated local installation succeeded and `grok plugin list --json` reported Modem 0.1.0 from this package. `grok inspect --json` confirmed the MCP server originated from the installed Modem plugin and targeted `https://mcp.modem.dev/mcp`. Native authentication and search testing remain pending with a Modem-controlled xAI account.
- No customer data was fetched and no OAuth grant was created during native package validation.
- September 24, 2026: Grok web chat completed a demo OAuth connection and one read-only search successfully. No agent invocation or workspace write occurred. This result covers that chat test; it does not verify native Grok Build, Grok Bot, mobile apps, or Grok on X.
