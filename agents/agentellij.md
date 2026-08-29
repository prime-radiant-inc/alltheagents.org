---
name: "AgentellIJ"
slug: "agentellij"
layout: "agent.njk"
category: "multiplexer"
maker: "AgentelliJ"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/31082-agentellij"
source_code_url: null
source_available: True
platforms:
  - "IDE"
first_released: "2026-08-11"
current_release: null
stars: null
language: "Kotlin"
homepage: "https://plugins.jetbrains.com/plugin/31082-agentellij"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenCode, Claude Code, Codex CLI (agent CLIs bring their own providers)"
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://plugins.jetbrains.com/plugin/31082-agentellij"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/31082-agentellij"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Hosts terminal-based AI coding agents in IntelliJ"
---

Terminal coding agents live in a separate window from IntelliJ, so every prompt re-explains context the IDE already holds. AgentelliJ embeds the agents in the IDE: OpenCode, Claude Code, and Codex CLI run in a tool window that can flip between raw terminal mode and a graphical chat without restarting, and the plugin shares the current file, selected lines, and project-tree items into the conversation. Per-agent binary paths, consent-based installation of missing CLIs, and balloon or OS-native notifications on completion round out the workflow. It is MIT-licensed (source at github.com/hei5enbug/agentellij), supports OpenCode, Claude Code, Codex CLI, and a native terminal agent, and targets IntelliJ-centered developers who use agent CLIs.
