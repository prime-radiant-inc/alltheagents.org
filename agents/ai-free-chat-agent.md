---
name: "AI Free Chat & Agent"
slug: "ai-free-chat-agent"
layout: "agent.njk"
category: "agent"
maker: "Staks-sor"
license: "Custom (personal-use-only, non-standard)"
url: "https://plugins.jetbrains.com/plugin/33364-ai-free-chat--agent"
source_code_url: null
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2026-08-21"
current_release: "0.4.25"
stars: null
language: "JavaScript"
homepage: "https://github.com/Staks-sor/ai-free"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/33364-ai-free-chat--agent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "DeepSeek, Qwen, ChatGPT chats and coding agents in PyCharm"
---

The project exists because commercial API access is the main cost barrier for AI-assisted coding; it converts free web chat sessions into a programmatic backend by automating a Chromium session per provider. On top of that transport it runs a /code agent bound to a project folder: it reloads hierarchical AGENTS.md instructions before each task, executes commands through risk-tiered whitelists (rm -rf blocked, curl and bash denied by default), and keeps memory in SQLite FTS5 plus a Markdown vault linking tasks to files and fixes. The JetBrains plugin is the IDE-facing entry point, while the local API also lets tools like Kilo Code or Continue consume the same sessions. It is solo-maintained, releases frequently (v0.4.25), and is free under a personal-use-only custom license.
