---
name: "Athena by LuckeySystems"
slug: "athena-by-luckeysystems"
layout: "agent.njk"
category: "multiplexer"
maker: "luckeyfaraday"
license: "NOASSERTION"
url: "https://github.com/luckeyfaraday/Athena"
source_code_url: "https://github.com/luckeyfaraday/Athena"
source_available: "True"
platforms: []
first_released: "2026-05-12"
current_release: "2026-08-10"
stars: "30"
language: "TypeScript"
homepage: "https://github.com/luckeyfaraday/Athena"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "no"
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

Athena addresses the problem that AI coding agents normally run as isolated terminal sessions with separate context windows, making it hard to see what each did or hand work between them. It embeds PTY terminals (node-pty + xterm.js with bounded streaming and snapshot replay) for Codex, OpenCode, Claude Code, Athena Code, and Hermes in one grid, discovers and resumes existing sessions on disk, and generates bounded markdown handoffs from selected sessions that get attached to fresh agent launches. Context modes start clean by default, with task/curated/immersive modes creating immutable workspace-scoped context bundles. An MCP server exposes context_workspace tools so Hermes can spawn terminals and read sessions inside Athena, secured with per-launch bearer tokens. Developers running several agent CLIs on one project use it as a command room for session-first work.
