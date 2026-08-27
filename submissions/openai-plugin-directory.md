# OpenAI Plugin Directory — test cases & demo outline

For the unified ChatGPT + ChatGPT Work + Codex directory ([DEV-3875](https://linear.app/modem-dev/issue/DEV-3875)). Submit at developers.openai.com/plugins/deploy/submission.

⚠️ **Blocked until** the TLS 1.0 `workers.dev` twin is retired (DEV-3881) — their automated tool scan will flag it, the same finding that failed our Slack review (DEV-3668).

## Pre-flight

- [ ] Verify the connector end-to-end as a **developer-mode custom connector** first (DEV-3925) — our transport is POST-only SSE-framed (no GET stream, no sessions); legal per spec but needs live confirmation against their client. Also sanity-check Codex via `codex mcp add`.
- [ ] Verified business identity + domain-verification challenge (DEV-3926) — identity must match listing name, website, support contact, privacy policy, ToS. Figure out who holds the OpenAI org.
- [ ] Explicit `destructiveHint` on **every** tool, including `modem_agent_invoke` and `search_modem` (DEV-3927 — `apps/agent-gateway/src/routes/mcp/server.ts`)
- [ ] 64×64 PNG icon under 5KB (DEV-3877)
- [ ] OAuth demo credentials (same seeded org as the Claude review — DEV-3916/3917)
- [ ] Demo recording (below)
- [ ] Release notes

## Test cases (their format: exactly 5 positive + 3 negative)

| # | Case | Expected |
| --- | --- | --- |
| P1 | Connect via OAuth, then: "What are customers saying about billing in the last month?" | `search_modem` returns markdown results citing seeded topics/messages; no other org's data appears |
| P2 | "Summarize the three highest-priority open topics and who's affected" | `modem_agent_invoke` returns a summary naming the seeded high-priority topics and companies |
| P3 | "Mark the topic about CSV export errors as resolved" | `update_topic` succeeds; change visible in the dashboard demo org |
| P4 | "Create a company called Acme Robotics with domain acmerobotics.com" | `create_companies` succeeds; company appears in dashboard |
| P5 | "Merge the duplicate person records for Jane Doe" | `merge_people` merges the two seeded duplicates into one |
| N1 | Ask for an update with an invalid status value | Zod validation error returned to the model; no mutation occurs |
| N2 | Reference a topic ID belonging to a different organization | Not found — token is org-scoped; no cross-tenant data leak |
| N3 | Rapid-fire more than 20 calls/min to one tool | Rate-limit error with retry guidance; service remains healthy |

## Demo recording

One take: OAuth connect → P1 (search) → P3 (topic update, dashboard shown updating live) → disconnect. ([DEV-3928](https://linear.app/modem-dev/issue/DEV-3928))
