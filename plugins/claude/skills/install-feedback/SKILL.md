---
name: install-feedback
description: Add or connect in-app feedback collection to Modem, including a feedback button, form, or contextual control. Use for implementing collection in a product, not searching feedback already in Modem.
---

# Install feedback with Modem

Help the developer add feedback collection to their app. Preserve any UI, target,
framework, and implementation scope they have already specified. A review or plan
request authorizes a review or plan, not channel creation or app edits.

## Load the current setup guide

1. Find the connected main Modem MCP at `https://mcp.modem.dev/mcp`. Discover its
   tools using the client's available tool search or tool list; tool names may
   have a client-specific prefix.
2. Call that server's `modem_skills` tool with `{ "name": "install-feedback" }`.
   This read-only call loads the current workflow and supported API contract.
3. Follow the returned `install-feedback` guide for request discovery, UI
   proposals, channel setup, implementation, verification, and handoff. Keep the
   guide as the API reference rather than guessing fields or relying on a cached
   request example.

The main MCP uses the developer's Modem OAuth connection. The separate
`https://mcp.modem.dev/feedback` server submits feedback from a deployed app or
agent using a channel key; it cannot supply this setup guide or create channels.

## If setup guidance is unavailable

- **No main Modem connection:** use the installed plugin's Modem connector or the
  [client install instructions](https://github.com/modem-dev/mcp#install) to add
  `https://mcp.modem.dev/mcp`. Reuse an existing matching connection. Complete the
  client's OAuth flow, refresh its tool list or start a new session if needed,
  then retry loading the guide. Do not ask the developer to paste an OAuth token.
- **Authentication required:** direct the developer to connect or reauthorize
  Modem in their client and select the intended organization. In Claude chat or
  Cowork, open the plugin's Connectors tab and add/connect Modem there.
- **`modem_skills` or `install-feedback` is unavailable after connection:** report
  the actual tool error and link the
  [Modem MCP documentation](https://modem.dev/docs/api/modem-mcp-server).
  The hosted server must expose the guide before setup can continue. Local app
  inspection and UI proposals can continue; do not invent a channel tool, API
  contract, install command, or successful connection.

## Keep the handoff safe and accurate

- Use the guide's automatic channel setup when the available tools, access, and
  ability to save the returned key allow it. Choose the destination before
  creation. If the developer wants the key kept out of the agent session, take
  the guide's manual setup branch before calling a tool that returns it.
- Do not paste key values into chat, logs, commits, or the final report. Report
  configuration locations and any remaining deployment step instead.
- Do not blindly repeat a channel creation whose outcome is unknown.
- Only submit test feedback under the guide's test conditions and the user's
  authorization. Report the highest verification stage actually proven; an
  accepted request does not prove a persisted record or a working record link.
