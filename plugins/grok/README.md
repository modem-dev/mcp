# Modem for Grok Build

Connect [Modem](https://modem.dev) to Grok Build to search customer feedback, update topics, people, and companies, and run the Modem Agent.

This package configures Modem's hosted MCP server. It needs a Modem account and organization; there is no local server or API key to provision.

## Status

- Manifest validation, isolated local installation, and plugin-origin discovery passed with Grok Build 1.0.41.
- [Source PR #8](https://github.com/modem-dev/mcp/pull/8) and [xAI marketplace PR #907](https://github.com/xai-org/plugin-marketplace/pull/907) are open for review; marketplace acceptance remains pending.
- Native Grok Build authentication and read-only search testing remain pending with a Modem-controlled xAI account.
- Grok chat OAuth and a read-only search passed in a demo test on September 24, 2026. That test does not establish native Build compatibility. Availability inside Grok on X remains unconfirmed; see [submission notes](../../docs/grok-submission.md) for the separate distribution paths.

## Test this checkout

From the repository root, with the official Grok Build CLI installed:

```bash
grok plugin validate ./plugins/grok
grok plugin install ./plugins/grok --trust
grok inspect
grok mcp doctor modem
```

- Check `grok inspect` for the Modem server's origin. An existing direct MCP configuration or Claude-compatible plugin must not mask a failed package install.
- Open Grok Build and use `/mcps` to authenticate Modem if needed. Grok documents a browser OAuth flow on first use; select the intended Modem organization and review the requested scopes.
- Ask: **Search Modem for customer feedback about file uploads. Include supporting sources. Do not change any data.** Verify it calls `search_modem`, not an agent run.
- Record the Grok version, package version, discovered server, OAuth result, and search result. Keep credentials and customer records out of this public repository.

The native manifest and root `.mcp.json` are the complete runtime package. It contains no hooks, executable installers, skills, agents, or LSP servers.

## Authentication and access

| OAuth scope | Access |
| --- | --- |
| `data:read` | Search Modem with `search_modem` |
| `agent:invoke` | Run and steer the Modem Agent; update topics, people, and companies |
| `offline_access` | Refresh authorization where requested by the client |

- MCP requests go to `https://mcp.modem.dev/mcp` using Streamable HTTP. OAuth is served by `https://app.modem.dev/api/auth`.
- Search queries are sent to Modem; returned customer information enters the Grok conversation. Connect an organization whose data you intend to use there.
- Agent runs and workspace writes act under the authorized Modem account. Agent runs may use connected integrations; a read-only test should use `search_modem` directly.
- Tool annotations do not guarantee a confirmation dialog. Grok's approval settings determine when it asks before a tool call.

## Support and source

- [MCP documentation](https://modem.dev/docs/api/modem-mcp-server)
- [Source repository](https://github.com/modem-dev/mcp)
- [Privacy](https://modem.dev/privacy-policy) · [Terms](https://modem.dev/terms-of-service)
- [support@modem.dev](mailto:support@modem.dev)
- Package license: MIT, included in `LICENSE`. The hosted Modem service is separate from this package.
