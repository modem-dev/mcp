---
name: topic-to-plan
description: Turn a Modem topic into a repro and a fix plan grounded in what customers wrote. Pulls the topic's messages, affected companies, and linked issues, then maps them to the code in this repo. Use when asked to "work on", "plan", or "pick up" a Modem topic, or to turn customer feedback into an engineering task.
---

# Topic to plan

Start from customer evidence in Modem and end with a plan for this codebase.

## Steps

1. Find the topic. If the user gave a topic name or ID, search for it directly. Otherwise ask `search_modem` for the highest-priority open topics and let the user pick one.
2. Pull the evidence with `search_modem`:
   - The messages in the topic, with author, company, source (chat, support, issue tracker), and date
   - Linked Linear issues and GitHub or GitLab pull requests
   - Issue type (bug_report, feature_request, complaint, praise) and lifecycle state
3. Extract the facts customers gave. Look for steps, versions, browsers, plan tier, error text, and what they expected to happen. Keep each fact tied to the message it came from.
4. Map to code. Search this repo for the error strings, routes, UI labels, or API names customers mentioned. Name the files and functions most likely involved.
5. Write the plan:
   - **Problem**, in one or two sentences, in the customer's terms
   - **Evidence**, the three to five most useful messages, quoted briefly with company names
   - **Repro**, steps built from those messages, marked as unverified until run
   - **Likely cause**, files and functions, with the reason for each
   - **Fix**, the proposed change and the tests to add
   - **Who to tell**, the companies and people to update when it ships
6. If a linked PR already exists, say so first. The work may be in progress.

## Notes

- Don't change the topic in Modem while planning. Offer `update_topic` with `lifecycleState: "in_progress"` once the user starts the work, and only call it when they agree.
