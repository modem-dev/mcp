# Submit Modem to Cursor Marketplace

## Package

- Repository to submit: https://github.com/modem-dev/mcp
- Root marketplace manifest: `.cursor-plugin/marketplace.json`
- Plugin source: `plugins/cursor`
- Plugin manifest: `plugins/cursor/.cursor-plugin/plugin.json`
- MCP configuration: `plugins/cursor/mcp.json`
- Logo: `plugins/cursor/assets/logo.png`
- License: MIT, already included in the repository and plugin package.

This repository packages access to Modem's hosted MCP service. It does not contain the hosted service implementation. The Cursor package can contain only an MCP configuration; additional skills, rules, and commands are optional.

## Steps

1. Validate the root marketplace manifest, plugin manifest, MCP URL, and referenced logo paths. Keep the plugin name `modem` consistent between manifests.
2. Follow the [local plugin test](../plugins/cursor/README.md#test-the-plugin-package-locally). Verify discovery, OAuth, and a read-only search in Cursor. Save the version and result. Avoid duplicate direct MCP configuration during the test so it cannot mask failed plugin discovery.
3. Merge the reviewed package changes into the public repository's default branch.
4. Sign in at https://cursor.com/marketplace/publish with the intended Modem publisher account. Check for an existing official application before submitting another one.
5. Complete the publisher application and submit the public repository URL. Use the values below for matching fields; the signed-in portal determines the actual required fields.
6. Retain the submission confirmation and respond to Cursor's review requests. Verify a public Modem listing and installation before marking the work complete. Cursor manually reviews plugins and subsequent updates; no review turnaround is promised here.

## Application copy

| Field | Value |
| --- | --- |
| Publisher | Modem |
| Plugin identifier | modem |
| Display name | Modem |
| Contact | support@modem.dev |
| Website | https://modem.dev |
| Repository | https://github.com/modem-dev/mcp |
| Description | Bring customer feedback into Cursor. Search Modem topics, people, and companies, update your workspace, and run the Modem Agent. |
| Authentication | Browser OAuth; requires a Modem account and organization. No API key to provision. |
| Endpoint | https://mcp.modem.dev/mcp |
| Transport | Streamable HTTP |
| Setup documentation | https://modem.dev/docs/api/modem-mcp-server |
| Privacy | https://modem.dev/privacy-policy |
| Terms | https://modem.dev/terms-of-service |

Suggested review prompt: "Search Modem for the most common customer complaints about file uploads. Include supporting sources. Do not change any data."

Use a workspace containing suitable demo data for review. Do not commit credentials or customer records to this public repository.

## Sources

- [Cursor plugin manifest and submission reference](https://cursor.com/docs/reference/plugins)
- [Local testing and marketplace review](https://cursor.com/docs/plugins)
- [Official submission portal](https://cursor.com/marketplace/publish)

The official marketplace is separate from the community site at cursor.directory. A community submission does not submit this package to Cursor's official review.
