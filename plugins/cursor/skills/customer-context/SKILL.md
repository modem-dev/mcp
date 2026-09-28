---
name: customer-context
description: Check Modem for the customers behind a bug, feature, or area of code before you change it. Finds the matching topics, who reported them, which companies are affected, how often they come up, and any Linear issue or pull request already linked. Use when starting work on a bug fix or feature, when a task mentions a customer or company, or when asked "who asked for this" or "who is affected".
---

# Customer context

Use Modem's `search_modem` tool to find what customers have said about the work in front of you. It is read-only and uses no agent credits, so run it early.

## When to use

- Starting a bug fix, feature, or refactor that users will notice
- A task, issue, or PR mentions a customer, company, or support ticket
- The user asks who asked for something, who is affected, or how often they come up

## Steps

1. Work out the subject in plain words. Read the issue title, branch name, error message, or the files being changed. Prefer the words a customer would use ("SSO login fails") over internal names ("SamlCallbackHandler").
2. Call `search_modem` with a direct question, for example:
   - "Which topics mention SSO login failures, and which companies reported them?"
   - "Which customers asked for CSV export in the last 90 days?"
   Ask for the columns you need when the shape matters (topic title, priority, lifecycle state, company, message count, linked issues and PRs).
3. If the first search misses, try once more with a synonym or the error text. Stop after two misses and say nothing was found.
4. Report back in a short list:
   - Matching topics with priority and lifecycle state
   - Companies and people affected, with message counts
   - One or two short customer quotes if the search returned messages
   - Linked Linear issues or pull requests, so work isn't duplicated
5. Use the findings in the work itself. Name affected customers in the PR description and flag a repro detail a customer mentioned.

## Notes

- Priority comes back as an integer: very_low (-100), low (-50), default (0), high (50), very_high (100). Show the name.
- Don't write to Modem from this skill. Use `mark-topic-shipped` or `update_topic` when the user asks for a change.
