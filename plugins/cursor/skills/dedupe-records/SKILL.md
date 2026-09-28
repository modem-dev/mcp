---
name: dedupe-records
description: Find and merge duplicate companies, people, or topics in Modem. Groups likely duplicates by domain, email, or title and shows the evidence. Merges only the sets you approve. Use when asked to clean up, dedupe, or merge records in Modem, or when a search returns the same company or person twice.
---

# Dedupe records

Clean up duplicate records in Modem with the merge tools, one approved set at a time.

## Steps

1. Pick the record type from the request. It can be companies, people, or topics.
2. Find candidates with `search_modem`:
   - Companies that share a domain, or names that differ only by suffix or case ("Acme", "Acme Inc", "acme.com")
   - People that share an email, or the same name at the same company
   - Topics with near-identical titles or the same linked issue
3. Present each candidate set with the fields that prove it, such as IDs, names, domains or emails, and record counts. Recommend a target, usually the record with the canonical domain or the most activity.
4. Wait for the user to approve each set. Never merge on a guess.
5. Merge with the matching tool, passing the approved target and sources.
   - `merge_companies`
   - `merge_people`
   - `merge_topics`
6. Report what merged and anything skipped.

## Notes

- Merges can't be undone from Cursor. Confirm the target before each call.
- To attach people to a company instead of merging, use `add_people_to_company`.
