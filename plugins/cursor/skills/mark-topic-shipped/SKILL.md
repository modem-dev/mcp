---
name: mark-topic-shipped
description: After a fix or feature merges, find the Modem topic it resolves and mark it completed. Then list the customers who asked so your team can tell them. Use when a PR merges, when the user says a fix shipped, or when asked to update Modem after finishing work.
---

# Mark topic shipped

Keep Modem in step with the code. When work ships, the topic it resolves should say so, and the people who reported it should hear about it.

## Steps

1. Identify what shipped. Read the PR title and description, the linked Linear issue, and the diff summary.
2. Find the topic with `search_modem`. Ask which topics match the change, or which topics link to this PR or issue. Modem links topics to the Linear issues and pull requests that resolve them, so a linked match is the strongest signal.
3. Confirm the match with the user before writing. Show the topic title, current lifecycle state, priority, and why it matches. If several topics match, list them and let the user choose.
4. Update the topic with `update_topic`:
   - `topicId` for the confirmed topic
   - `lifecycleState: "completed"`
   Leave priority, issue type, and keywords alone unless the user asks. For several topics, use `bulk_update_topics`.
5. List who to tell. Use `search_modem` to get the people and companies on the topic, with the source each message came from (Slack, support inbox, issue tracker), so the reply goes back where they asked.
6. Offer a short customer update the user can send. Say what changed and where to find it. Don't send it from here.

## Notes

- Write tools act as the signed-in user under their Modem role, and Cursor asks for confirmation on each call.
- Settable lifecycle states are open, in_progress, completed, and dismissed. Use dismissed only when the user says the topic won't be fixed.
