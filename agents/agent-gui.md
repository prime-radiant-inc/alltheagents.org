---
name: "Agent GUI"
slug: "agent-gui"
layout: "agent.njk"
category: "multiplexer"
maker: "matsumo0922"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/30428-agent-gui"
source_code_url: null
source_available: True
platforms:
  - "IDE"
first_released: "2026-03-03"
current_release: null
stars: null
language: "Kotlin"
homepage: "https://github.com/matsumo0922/agent-gui-plugin"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Anthropic (via Claude Code CLI)"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://plugins.jetbrains.com/plugin/30428-agent-gui"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/30428-agent-gui"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Native chat GUI for AI coding agents inside JetBrains"
---

Running Claude Code next to IntelliJ means context lives in two places: the IDE knows the project, the terminal knows the agent. Agent GUI embeds the agent as a native JetBrains tool window built with Compose for IDE, streaming responses with markdown rendering, visualizing tool calls and sub-agent tasks inline, and routing file-edit permissions through approve/deny prompts inside the IDE. Sessions persist across IDE restarts, files attach to prompts, and the UI follows the editor's light/dark theme. It currently drives Claude Code (CLI on PATH with an Anthropic API key or Claude Max plan), with Codex support planned. JetBrains-centric developers who want their agent conversation co-located with their code are the audience.
