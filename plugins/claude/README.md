# Modem — Claude Code plugin

Thin plugin wrapping the hosted Modem MCP server (`https://mcp.modem.dev/mcp`) for the Claude Code plugin marketplace ([DEV-3924](https://linear.app/modem-dev/issue/DEV-3924)).

- Submit at: clau.de/plugin-directory-submission (automated security scan → Anthropic approval)
- ⚠️ **Plugin names are immutable once published** — confirm `modem` is the name we want before submitting.
- Optional follow-up: bundle a skill with Modem usage guidance (tool-selection tips, example prompts).

Before submitting, validate the manifest shape against the current Claude Code plugin docs (`.claude-plugin/plugin.json` + bundled MCP config) — this draft was authored from the readiness report and needs a check against the live schema.
