---
name: "Volar"
slug: "volar"
layout: "agent.njk"
category: "multiplexer"
maker: "VolarTools"
license: null
url: "https://marketplace.visualstudio.com/items?itemName=VolarTools.volar-ai"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2025-05-01"
current_release: "2025-07-07"
stars: null
language: null
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=VolarTools.volar-ai"
maintained: null
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Plan, Review & Build with AI"
---

Volar exists to give AI coding sessions an explicit planning and review layer before any code is written. The extension does not run AI itself; it manages a task list in a sidebar and communicates with the developer's coding tool through an MCP server (VolarTaskServer), so agents can read and update tasks from inside chat. Its Plan action prompts the connected AI to analyze the codebase and draft an implementation plan, Breakdown recursively splits complex tasks into sub-tasks, and Execute instructs the AI to implement only the approved plan. It auto-configures MCP for Cursor, Windsurf, and Claude Code, and supports any MCP-compatible tool such as Cline via a localhost URL. It targets VS Code users working with Cursor, Windsurf, or Claude Code who want approved-plan discipline.
