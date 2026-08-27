# Modem — Cursor plugin

Package for the Cursor Marketplace ([DEV-3923](https://linear.app/modem-dev/issue/DEV-3923)), wrapping the hosted Modem MCP server (`https://mcp.modem.dev/mcp`).

Checklist before submitting:

1. Start from `cursor/plugin-template` and mirror its layout — the manifest here is a draft from the readiness report §5.6, not yet validated.
2. Commit the square logo as `assets/logo.png` (pending export — DEV-3877).
3. Run their `scripts/validate-template.mjs` against the package.
4. Submit via cursor.com/marketplace/publish (human-reviewed by the Cursor team). Remote MCP + OAuth is supported — users get one-click "Add to Cursor".
