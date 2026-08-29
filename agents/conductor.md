---
name: "Conductor"
slug: "conductor"
layout: "agent.njk"
category: "multiplexer"
maker: "Conductor"
license: "Proprietary"
url: "https://conductor.build"
source_code_url: null
source_available: "False"
platforms:
  - "CLI"
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic (Claude Code), OpenAI (Codex), Cursor, OpenCode, xAI (Grok)"
pricing: "subscription"
install_method: "macOS desktop app (download); iOS coming soon; API available"
docs_url: "https://conductor.build/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Platform to run a team of coding agents in the cloud inside isolated microVM sandboxes with multiplayer workspaces; runs first-party Claude Code, Codex, Cursor, and OpenCode agents under the hood (BYO subscriptions/keys); macOS desktop app by Melty Labs."
---

Coding agents stop when laptops sleep, and individual developers' agent runs are invisible to the rest of a team. Conductor moves the agent runtime into cloud sandboxes - Firecracker microVMs preloaded with the repository and its dependencies - that start in seconds and keep agents running for hours unattended. The macOS desktop app manages parallel agent workspaces, and users connect their existing subscriptions and API keys for Claude Code, Codex, Cursor, and OpenCode rather than buying model access through Conductor. Its multiplayer workspaces let teammates watch and prompt the same agent session simultaneously, and an API exposes the same infrastructure to custom tooling. Product and engineering teams at companies including Linear, Vercel, and Notion use it to run more agent work than a laptop allows.
