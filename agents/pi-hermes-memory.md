---
name: "pi-hermes-memory"
slug: "pi-hermes-memory"
layout: "agent.njk"
category: "agent"
maker: "chandra447"
license: "MIT"
url: "https://github.com/chandra447/pi-hermes-memory"
source_code_url: "https://github.com/chandra447/pi-hermes-memory"
source_available: "True"
platforms: []
first_released: "2026-04-23"
current_release: "2026-08-17"
stars: "347"
language: "TypeScript"
homepage: "https://github.com/chandra447/pi-hermes-memory"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "OpenRouter, Pi (registered provider auth), configurable via llmModelOverride"
pricing: "Free/open-source (MIT)"
install_method: "pi install npm:pi-hermes-memory (or git:github.com/chandra447/pi-hermes-memory, or pi -e /path/to/src/index.ts for local testing)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/chandra447/pi-hermes-memory"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Memory and learning extension for the Pi coding agent (ported from Hermes by Nous Research): persistent two-tier (global + per-project) memory, failure learning, correction detection, procedural skills saved as SKILL.md files, secret scanning to block API keys, and auto-consolidation. Hybrid Markdown + SQLite FTS5 storage."
---

pi-hermes-memory addresses the core complaint about coding agents — that each session starts ignorant of everything learned before. Ported from Nous Research's Hermes agent, it maintains a two-tier memory of global preferences and per-project knowledge as Markdown files, mirrors them into a SQLite FTS5 index, and makes entire past sessions searchable. The system learns from failures and corrections explicitly, categorizing memories by type (failure, correction, insight, preference, convention, tool-quirk), and it saves procedural skills as SKILL.md files with structured verification steps and duplicate detection, exposed through pi's resource-discovery hook. Background review runs every ten turns, session flush happens on compaction or shutdown, and consolidation triggers automatically when stores overflow. Secret scanning blocks API keys from ever entering memory files. Pi users who run long-lived projects adopt it to keep institutional knowledge — conventions, past failures, working procedures — alive across sessions.
