---
name: customer-signals-canvas
description: Build a canvas of what customers are saying right now. Shows top open topics by priority and volume, bugs versus feature requests, the companies raising them, and which topics already have linked work. Use when asked for a customer feedback dashboard, a weekly signals review, "what are customers asking for", or a canvas of Modem data.
---

# Customer signals canvas

Render Modem data as a canvas so the team can scan it, reopen it, and refresh it with new data.

## Data

Run these `search_modem` queries. Pass `limit` and follow the returned `cursor` if you need more rows. Default to the last 30 days unless the user gives a range.

1. Open topics ordered by priority, then by message count. Columns: topic title, priority, issue type, lifecycle state, message count, company count, last message date.
2. Companies with the most messages in the range. Columns: company, message count, topic count, top topic.
3. Open topics with a linked Linear issue or pull request, and the state of that work.
4. New topics first seen in the range.

## Layout

1. **Header** with the date range and when the data was pulled
2. **Stat row** with open topics, new topics this range, bug reports, feature requests, and companies with activity
3. **Top topics** table showing title, priority name, type, messages, companies, and linked work (yes or no), sorted by priority then messages
4. **Needs an owner**, high and very_high topics with no linked issue or PR
5. **Most active companies** table
6. **New this range** list

## Formatting

- Show priority names, not integers. very_low (-100), low (-50), default (0), high (50), very_high (100).
- Dates as YYYY-MM-DD. Counts as plain integers.
- Keep topic titles as Modem returns them. Don't rewrite them.
- If a query returns nothing, show the section with "None in this range" rather than dropping it.

## Refreshing

When the user asks to refresh, rerun the same queries with the same range and update the canvas in place.
