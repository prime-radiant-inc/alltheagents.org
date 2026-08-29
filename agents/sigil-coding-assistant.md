---
name: "Sigil - Coding Assistant"
slug: "sigil-coding-assistant"
layout: "agent.njk"
category: "agent"
maker: "José M. Nieves"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/32492-sigil--coding-assistant"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-08-16"
current_release: null
stars: null
language: null
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://github.com/nievesj/sigil-coding-assistant"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/32492-sigil--coding-assistant"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI-assisted development plugin powered by OpenCode"
---

JetBrains users who adopted OpenCode in the terminal lacked IDE integration; Sigil supplies it by launching and managing a local opencode serve process and rendering its agent sessions inside the IDE, requiring the OpenCode CLI on PATH and any 2026.1+ JetBrains IDE. The plugin surfaces AI chat, sessions with per-session token and cost tracking, a context panel, slash commands, and tool permissions, with MCP support inherited from OpenCode. Because nothing leaves the local machine except the model API calls OpenCode itself makes, it fits developers with privacy constraints or self-hosted models. It is MIT-licensed, open source on GitHub, free on the Marketplace, and new — published mid-2026 with a few hundred downloads — so expect early-stage polish. Its audience is OpenCode users working primarily in JetBrains IDEs.
