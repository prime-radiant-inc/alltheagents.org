---
name: "Vibe Kanban"
slug: "vibe-kanban"
layout: "agent.njk"
category: "multiplexer"
maker: "bloop"
license: null
url: "https://marketplace.visualstudio.com/items?itemName=bloop.vibe-kanban"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2025-08-14"
current_release: "2026-02-05"
stars: null
language: null
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None (connects to a local Vibe Kanban instance, which drives the coding agents)"
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: "https://marketplace.visualstudio.com/items?itemName=bloop.vibe-kanban"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=bloop.vibe-kanban"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Control your Vibe Kanban coding agents from within VS Code"
---

Vibe Kanban orchestrates coding agents from a browser interface, and this extension exists for developers who would rather not leave their editor to check on that work. Once a local Vibe Kanban instance is running, the extension adds an Activity Bar icon that opens the agent control panel in a sidebar webview, connected to the local server — auto-detecting its port from the port file the server writes, with a settings override available — and provides two-way messaging and live status for the agents it manages. Developers running parallel agent tasks through Vibe Kanban use it to supervise and redirect work without switching to a browser tab; the extension is free, early at version 0.1.0, and requires the separately installed Vibe Kanban server.
