---
name: "Athena by LuckeySystems"
slug: "athena-by-luckeysystems"
layout: "agent.njk"
category: "agent"
maker: "luckeyfaraday"
license: "NOASSERTION"
url: "https://github.com/luckeyfaraday/Athena"
source_code_url: "https://github.com/luckeyfaraday/Athena"
source_available: True
platforms: []
first_released: "2026-05-12"
current_release: "2026-08-10"
stars: "30"
language: "TypeScript"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: null
plan_mode: null
model_providers: "Codex, Claude Code, OpenCode, Grok"
pricing: "Free (open source)"
install_method: "git clone https://github.com/luckeyfaraday/Athena.git && cd Athena/client && npm install && npm run dev"
docs_url: "https://github.com/luckeyfaraday/Athena/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/luckeyfaraday/Athena"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Local desktop 'command room' that orchestrates multiple isolated AI coding agents (Codex, Claude Code, OpenCode, Grok) into one unified workspace with shared project context, cross-agent session recall, and bounded handoffs. Installs a bundled agent skill (athena-context-workspace) into local directories for Codex, Claude Code, and OpenCode. Hermes MCP bridge allows Hermes to control the workspace, spawn terminals, and read sessions. Embedded PTYs, native session discovery, agent grids for parallel work."
---

Local desktop 'command room' that orchestrates multiple isolated AI coding agents (Codex, Claude Code, OpenCode, Grok) into one unified workspace with shared project context, cross-agent session recall, and bounded handoffs. Installs a bundled agent skill (athena-context-workspace) into local directories for Codex, Claude Code, and OpenCode. Hermes MCP bridge allows Hermes to control the workspace, spawn terminals, and read sessions. Embedded PTYs, native session discovery, agent grids for parallel work.
