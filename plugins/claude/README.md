# Modem — Claude Code plugin

Thin plugin wrapping the hosted Modem MCP server (`https://mcp.modem.dev/mcp`) for the Claude Code plugin marketplace ([DEV-3924](https://linear.app/modem-dev/issue/DEV-3924)).

- Submit at: clau.de/plugin-directory-submission (automated security scan → Anthropic approval)
- ⚠️ **Plugin names are immutable once published** — confirm `modem` is the name we want before submitting.
- Optional follow-up: bundle a skill with Modem usage guidance (tool-selection tips, example prompts).

The manifest shape (incl. the inline `mcpServers` entry with `type: "http"` + `url`) was validated against the published Claude Code plugin manifest schema (schemastore.org). Still worth a `claude plugin validate`-style dry run before submitting.
