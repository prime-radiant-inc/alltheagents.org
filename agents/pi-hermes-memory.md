---
name: "pi-hermes-memory"
slug: "pi-hermes-memory"
layout: "agent.njk"
category: "agent"
maker: "chandra447"
license: "MIT"
url: "https://github.com/chandra447/pi-hermes-memory"
source_code_url: "https://github.com/chandra447/pi-hermes-memory"
source_available: True
platforms: []
first_released: "2026-04-23"
current_release: "2026-08-17"
stars: "347"
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: True
plan_mode: null
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

Memory and learning extension for the Pi coding agent (ported from Hermes by Nous Research): persistent two-tier (global + per-project) memory, failure learning, correction detection, procedural skills saved as SKILL.md files, secret scanning to block API keys, and auto-consolidation. Hybrid Markdown + SQLite FTS5 storage.
