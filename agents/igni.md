---
name: "igni"
slug: "igni"
layout: "agent.njk"
category: "agent"
maker: "Ignite Ember"
license: null
url: "https://plugins.jetbrains.com/plugin/32377-igni"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-08-03"
current_release: null
stars: null
language: null
homepage: "https://ignite-ember.sh/"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google Gemini, Groq, MiniMax"
pricing: "BYOK"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/32377-igni"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI coding assistant running parallel multi-agent workflows"
---

igni embeds an agentic chat in a JetBrains tool window and decomposes large tasks into concurrent research, implementation, and review sub-agents that stream into one conversation. Every tool call passes an approval dialogue, and plan mode gates edits behind a research-and-propose step. Sessions are stored per repository and can be forked to try alternative approaches without losing the original thread; opening the JetBrains and VS Code editions side by side keeps both live-synced to the same backend. The backend installs itself through uv on first launch, and model choice is BYOK across Claude, OpenAI, Gemini, Groq, and MiniMax with mid-session switching.
