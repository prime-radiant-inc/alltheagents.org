---
name: "betool - AI Code Assistant"
slug: "betool-ai-code-assistant"
layout: "agent.njk"
category: "multiplexer"
maker: "beTool IA"
license: null
url: "https://plugins.jetbrains.com/plugin/31225-betool--ai-code-assistant"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-04-11"
current_release: null
stars: null
language: null
homepage: "https://www.betool.fr"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "freemium"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/31225-betool--ai-code-assistant"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Bridges AI coding assistants with the IDE via a local server"
---

betool addresses a specific gap: AI coding agents that propose edits outside the IDE have no native way to surface those changes inside JetBrains IDEs for review. The plugin runs a local server that receives code modification proposals from the betool CLI and presents them as interactive red/green diffs in a modal dialog, where each change is accepted or rejected with one click before being applied, with files backed up beforehand. It works across IntelliJ IDEA, WebStorm, PyCharm, GoLand, and other JetBrains IDEs, starts automatically with the project, requires no configuration, and falls back to terminal mode when IntelliJ is not running. The plugin is free; usage requires a betool.fr account and payment is by AI tokens consumed. It is aimed at JetBrains developers who want agent-proposed changes surfaced as in-IDE reviewable diffs.
