---
name: "Townie"
slug: "townie"
layout: "agent.njk"
category: "agent"
maker: "Val Town"
license: null
url: "https://www.val.town"
source_code_url: null
source_available: null
platforms:
  - "Web"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://www.val.town"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "freemium"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI assistant that writes and deploys server vals/apps"
---

Townie addresses the gap between describing a small server-side tool and having it running: on Val Town, code is deployed the moment it is saved, so an assistant that writes vals produces live software rather than files that still need hosting. The assistant generates vals within the platform's editor alongside the code and SQLite views, and the underlying platform provides the runtime pieces small server apps need — scheduled execution, email handling, databases, blob storage, and a sandbox for running untrusted code. Developers building websites, APIs, automations, and MCP servers on Val Town use Townie as the generation layer, while external agents (Claude Code, Codex, Cursor) connect through the Val Town plugin and MCP server; pricing follows Val Town's subscription tiers.
