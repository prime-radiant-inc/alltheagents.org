---
name: "hypernovum"
slug: "hypernovum"
layout: "agent.njk"
category: "multiplexer"
maker: "Pardesco"
license: "AGPL-3.0"
url: "https://github.com/Pardesco/hypernovum"
source_code_url: "https://github.com/Pardesco/hypernovum"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-02-05"
current_release: "2026-08-04"
stars: "89"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: null
model_providers: null
pricing: "Free (Obsidian plugin, AGPL-3.0); Hypernovum Pro (standalone desktop app) is paid"
install_method: "Obsidian > Settings > Community plugins > Browse > search 'Hypernovum' > enable > run 'Open code city' from command palette"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Obsidian plugin (desktop-only) that turns vault projects into a live 3D 'code city' visualization built on Three.js with integrated agent ops; each project note becomes a procedurally-generated building (color=status, height=priority, category=district); vault backlinks become glowing neural arcs; agent sessions appear as colored orbs orbiting buildings with conflict detection; installs agent heartbeat hooks (.hypernovum/heartbeat.js) with ready-to-paste hook JSON for Claude Code settings; publishes agent skills (SKILL.md) and AGENTS.md context to launched agents (Claude Code, GPT Codex, Antigravity CLI); zero network requests/telemetry. MCP server only in paid Hypernovum Pro."
---

Hypernovum treats a personal knowledge vault as mission control for AI coding agents. Each project note becomes a procedurally generated building in a Three.js city, with status as color, priority as height, and vault backlinks as glowing arcs, while live agent sessions appear as colored orbs that expose file conflicts between concurrently running agents. Setup commands install a heartbeat hook script and print ready-to-paste JSON for Claude Code settings, so session state streams into the visualization. When launching an agent, the plugin publishes SKILL.md skills and an AGENTS.md context file so the agent starts with vault-specific knowledge. Everything runs locally with no network calls, and a paid Pro app adds MCP, Engram agent memory, and whole-drive scanning.
