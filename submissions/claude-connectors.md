# Claude Connectors Directory — portal answers

Draft answers for the submission portal inside Claude.ai org settings ([DEV-3873](https://linear.app/modem-dev/issue/DEV-3873)). Requires a **Team or Enterprise Claude.ai org** with Owner/Directory permission ([DEV-3919](https://linear.app/modem-dev/issue/DEV-3919)).

⚠️ The primary doc (claude.com/docs/connectors/building/submission) was corroborated second-hand during research — **re-read it and reconcile field-by-field before submitting** ([DEV-3921](https://linear.app/modem-dev/issue/DEV-3921)).

| Portal field | Answer |
| --- | --- |
| Server URL | `https://mcp.modem.dev/mcp` |
| Auth method | OAuth 2.1 with Dynamic Client Registration (RFC 7591, open registration — no pre-shared client needed). Authorization server: `https://app.modem.dev/api/auth`; RFC 9728 protected-resource metadata at `/.well-known/oauth-protected-resource/mcp`. Callback allow-listing not required. |
| Name / tagline / description / categories / use cases | [`LISTING-COPY.md`](LISTING-COPY.md) |
| Logo | Square 1:1 SVG (`../assets/` — pending export, DEV-3877; brand #079D7D) |
| Privacy policy / ToS | modem.dev/privacy-policy · modem.dev/terms-of-service — **confirm retention language first** (DEV-3879) |
| Test account | Seeded demo org, credentials valid ≥30 days — see [`reviewer-instructions.md`](reviewer-instructions.md) (DEV-3916/3917) |
| Tool inventory note | See LISTING-COPY.md |
| Support channel | support@modem.dev |

## Prerequisites checklist

- [ ] Team/Enterprise Claude.ai org with Owner (Directory) permission for whoever clicks submit (DEV-3919)
- [ ] Tool `title`s shipped on all 11 tools + server (DEV-3876 — their checklist requires human-readable titles)
- [ ] Square SVG logo exported (DEV-3877)
- [ ] Privacy policy retention language confirmed (DEV-3879)
- [ ] Privacy/ToS linked from docs site (DEV-3878)
- [ ] Demo org seeded + reviewer login in vault, valid ≥30 days (DEV-3916/3917)
- [ ] 3–5 screenshots captured (DEV-3920)
- [ ] Beta/GA positioning decided (DEV-3880)

## After submitting

Track in the submissions dashboard; expect the automated policy scan first, listing as a "community connector"; review ~2–3 weeks. Escalation: mcp-review@anthropic.com ([DEV-3922](https://linear.app/modem-dev/issue/DEV-3922)).
