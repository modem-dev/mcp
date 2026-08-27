# Reviewer connect instructions (Claude + OpenAI test account)

Step-by-step doc handed to directory reviewers ([DEV-3918](https://linear.app/modem-dev/issue/DEV-3918)). One seeded demo org serves both reviews.

> **Status: template.** Blanks below are filled once the demo org exists (DEV-3916) and is seeded (DEV-3917). Credentials go in the vault, never in this repo.

## Account

- Organization: `modem-review-demo` *(create — DEV-3916)*
- Login: `mcp-review@modem.dev` *(password in vault; valid ≥30 days; not tied to a personal account; isolated from production customer data)*

## Connecting

1. Add the server in your MCP client: `https://mcp.modem.dev/mcp` (Streamable HTTP, OAuth).
2. A browser window opens for authorization. Sign in with the reviewer credentials above.
3. On the Modem consent screen: confirm the requesting client name, select the **modem-review-demo** organization, and approve **both** permissions:
   - `data:read` — natural-language search
   - `agent:invoke` — agent runs and workspace writes
4. Tools appear according to approved scopes. If only `search_modem` is visible, re-authorize and approve both.

## One example prompt per tool family

| Family | Prompt |
| --- | --- |
| Search (`search_modem`) | "What are customers saying about billing in the last month?" |
| Agent (`modem_agent_invoke` et al.) | "Summarize the three highest-priority open topics and who's affected." |
| Topic writes | "Mark the topic about CSV export errors as resolved." |
| Company writes | "Create a company called Acme Robotics with domain acmerobotics.com." |
| People writes | "Merge the duplicate person records for Jane Doe." |

## Notes for reviewers

- All write tools are annotated `destructiveHint`, so your client should ask you to confirm each write before it runs.
- Write tools act under the signed-in user's role in the selected organization — never more access than the account has in the Modem dashboard.
- Tool calls are rate limited at 20/min per organization per tool; rate-limit errors carry a `retryAfter` hint.
- The review org is isolated from production customer data.

## Seeded data (spec — DEV-3917)

~15 topics across priorities/statuses (incl. one about "CSV export errors" and several with recent activity), ~10 companies (one obvious duplicate pair), ~20 people (a "Jane Doe" duplicate pair), messages from ≥2 sources so `search_modem` results cite sources.
