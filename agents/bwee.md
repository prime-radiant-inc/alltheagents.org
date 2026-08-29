---
name: "Bwee"
slug: "bwee"
layout: "agent.njk"
category: "multiplexer"
maker: null
license: null
url: "https://bwee.app"
source_code_url: null
source_available: "False"
platforms:
  - "CLI"
  - "IDE"
  - "Desktop"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://bwee.app"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic"
pricing: "Requires Claude Code access (Claude Max, Team, or Enterprise plan, or an Anthropic API key)"
install_method: "Download DMG from bwee.app, drag into Applications (Apple silicon, macOS 13+)"
docs_url: "https://bwee.app/docs/getting-started"
plugin_docs_url: null
config_docs_url: null
download_url: "https://download.bwee.app/Bwee-1.0.0-arm64.dmg"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Native Mac app that wraps Claude Code with a UI; hosts custom interfaces ('views') that Claude builds for you, running locally with persistent session state per task"
---

Bwee wraps Claude Code in a native macOS application, adding a persistent home for the agent and the interfaces it produces. Its premise is that terminal agents are awkward for work that benefits from structure, so instead of only relaying chat, Bwee asks Claude to build small custom UIs — 'views' — for specific tasks, which run locally with full access to files and the terminal, and each task's session state and views survive between visits. The user chats to request or refine a view; the agent builds and maintains it. This targets Mac users on Apple Silicon who already pay for Claude Code (a Claude subscription or API key is required) and want durable, purpose-built interfaces for recurring agent workflows rather than raw terminal sessions. The app is distributed as a DMG from bwee.app, with documentation and a changelog published on the site.
