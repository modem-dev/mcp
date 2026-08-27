# Submission tracker

One row per directory. Linear project: [MCP Marketplace Listings](https://linear.app/modem-dev/project/mcp-marketplace-listings-9bf115cf52c4). Full research + eligibility matrix: the readiness report (Notion, linked from the project).

Recommended order: pre-flight fixes → official registry → GitHub onboarding → this repo public → Claude directory (+ cheap PRs/forms in parallel) → Cursor/Claude Code plugins → OpenAI (after TLS fix).

| Directory | How | Status | Linear | Notes |
| --- | --- | --- | --- | --- |
| Official MCP Registry | `mcp-publisher` + DNS TXT on modem.dev | ☐ Not started | DEV-3868/3884/3885 | Do first — upstream feed for GitHub, VS Code, Docker, Smithery, PulseMCP, Anthropic. `server.json` at repo root. |
| GitHub MCP Registry + VS Code/Copilot gallery | Onboarding request in github-mcp-server discussion #1257 | ☐ Not started | DEV-3871/3886/3887 | Needs registry publish + validator/curl proof first. Manual curation, no SLA. |
| Claude Connectors Directory | Portal in Claude.ai org settings | ☐ Not started | DEV-3873 (+3916–3922) | See [claude-connectors.md](claude-connectors.md). Needs Team/Enterprise org. |
| OpenAI Plugin Directory | developers.openai.com/plugins | ☐ **Blocked** (TLS 1.0 twin — DEV-3881) | DEV-3875 (+3925–3928) | See [openai-plugin-directory.md](openai-plugin-directory.md). |
| Cursor Marketplace | cursor.com/marketplace/publish | ☐ Not started | DEV-3923 | Package in [`../plugins/cursor/`](../plugins/cursor/). |
| Claude Code plugin | clau.de/plugin-directory-submission | ☐ Not started | DEV-3924 | Package in [`../plugins/claude/`](../plugins/claude/). Name immutable once published. |
| Docker MCP Catalog | Fork docker/mcp-registry, `task remote-wizard`, PR | ☐ Not started | DEV-3904 | Don't hand-write server.yaml — the wizard generates it. Resolve license question first. |
| Gemini CLI extensions | Public repo + `gemini-extension.json` + topic `gemini-cli-extension` | ☐ Waiting on repo going public | DEV-3901 | Crawled daily, no form. Add the GitHub topic when flipping public. |
| Glama | `glama.json` auto-index + claim listing | ☐ Waiting on repo going public | DEV-3902 | Curated "remote MCP services" list: reach out on their Discord. |
| Cline | GitHub issue on cline/mcp-marketplace | ☐ Waiting on repo going public + 400×400 PNG | (DEV-3869 scope) | `llms-install.md` at repo root helps their auto-install. |
| Hermes (Nous Research) | PR to `optional-mcps/` in NousResearch/hermes-agent | ☐ Not started | DEV-3906 | Mirror an existing entry. Our DCR OAuth works zero-config. |
| awesome-mcp-servers (punkpeye) | One-line fork/PR | ☐ Not started | DEV-3903 | Draft line in [LISTING-COPY.md](LISTING-COPY.md). Feeds Glama visibility. |
| PulseMCP + Smithery | Verify auto-ingested listings, claim & enrich | ☐ After registry publish | DEV-3914 | Smithery external lane wants `/.well-known/mcp-config` — decide or rely on ingestion. |
| mcpservers.org + mcp.so | Web forms | ☐ Not started | DEV-3913 | Batch with §5.1 copy. |
| LobeHub, MCPMarket, MCP.Directory | CLI/forms | ☐ Not started | DEV-3915 | Batch in one sitting; SEO breadth. |
| Perplexity / Devin / Grok / Mistral / Gemini app / Composio | BD/partnership only | — Out of scope | — | Hand to partnerships. |
| Microsoft M365 Copilot Agent Store | Partner Center + certification | — Deferred | — | Revisit on enterprise pull. |

## Pre-flight blockers (monorepo work)

| Blocker | Linear | Status |
| --- | --- | --- |
| Retire TLS 1.0 workers.dev twin serving `/mcp` | DEV-3881 | ☐ |
| Tool/server `title`s (server title + router-tool titles exist in code; verify all 14 tools render titled) | DEV-3876 | ☐ verify |
| Explicit `destructiveHint` on every tool | DEV-3927 | ☐ |
| Square logo exports (1:1 SVG, 64×64 PNG <5KB, 400×400 PNG) | DEV-3877 | ☐ |
| Privacy/ToS/trust links on docs site | DEV-3878 | ☐ |
| Retention language legal check | DEV-3879 | ☐ |
| Beta→GA decision + version 1.0.0 (⚠️ the manifests in this repo already assert `1.0.0` — revisit them if the decision is "stay beta") | DEV-3880 | ☐ |
| DCR default scope → `data:read`; enforce PKCE | DEV-3882 | ☐ |
| Bare well-known endpoints + PRM name/docs fields | DEV-3883 | ☐ |
| **Flip this repo to public** (required by Gemini/Glama/Cline/LobeHub/raw asset URLs) | DEV-3869 | ☐ |
