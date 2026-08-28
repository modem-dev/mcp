# Plugin packaging checklists (internal)

Internal notes moved out of `plugins/*/README.md` (those are user-facing — reviewers and installing users read them).

## Claude Code plugin ([DEV-3924](https://linear.app/modem-dev/issue/DEV-3924))

- Root `.claude-plugin/marketplace.json` + `plugins/claude/.claude-plugin/plugin.json` validate against the schemastore schemas (inline `mcpServers` with `type: "http"` + `url` is explicitly permitted).
- Run `claude plugin validate ./plugins/claude` (real command; `--strict` promotes warnings) — the review pipeline runs the same check.
- ⚠️ **Plugin names are immutable once published** — confirm `modem` is the name we want before submitting.
- Submission: `claude.ai/admin-settings/directory/submissions/plugins/new` or `platform.claude.com/plugins/submit` (the `clau.de/plugin-directory-submission` shortlink resolves to docs, not a form). Approved submissions are pinned to a commit SHA in this repo.
- Optional follow-up: bundle a skill with Modem usage guidance.

## Cursor plugin ([DEV-3923](https://linear.app/modem-dev/issue/DEV-3923))

- Layout checked against `cursor/plugins` (their official marketplace repo): root `.cursor-plugin/marketplace.json` is required (their `validate-template.mjs` exits immediately without it); `plugin.json` `author` allows only `name` + `email`; `mcpServers: "./mcp.json"`; remote entries use bare `{"url": ...}` (no `type`).
- Commit the square logo as `plugins/cursor/assets/logo.png` (pending export — DEV-3877). The validator hard-errors on a missing `logo` path.
- Their official third-party entries also carry `category`, `tags`, per-plugin `LICENSE`, `CHANGELOG.md` — add before submitting.
- ⚠️ Third-party MCP plugins currently live **inside** `cursor/plugins` (authored as Cursor) — the submission may end up as a PR into their repo rather than a pointer at ours. Confirm with the form first.
- Run `scripts/validate-template.mjs` from their template against this repo.
- Submit via cursor.com/marketplace/publish (human-reviewed).

## Open questions (both)

- `license` fields currently use npm's `"SEE LICENSE AT <url>"` convention; both schemas describe SPDX identifiers. Decide a real license for this repo's contents (MIT/Apache-2.0 for manifests+docs is the norm — it licenses the JSON, not the service) and add a `LICENSE` file; GitHub shows the repo as unlicensed otherwise.
