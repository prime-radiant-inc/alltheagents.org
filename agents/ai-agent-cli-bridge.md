---
name: "AI Agent CLI Bridge"
slug: "ai-agent-cli-bridge"
layout: "agent.njk"
category: "multiplexer"
maker: "Hannos"
license: null
url: "https://plugins.jetbrains.com/plugin/31364-ai-agent-cli-bridge"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-05-05"
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/31364-ai-agent-cli-bridge"
maintained: null
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Launch preconfigured AI terminal sessions with IDE context"
---

Developers working in JetBrains IDEs who use terminal-based coding agents lose IDE context when they switch to a shell. This plugin launches AI terminal sessions preconfigured with the IDE's current context, so the agent starts with the project state rather than requiring manual setup. It occupies the bridge layer between IDE and CLI agent, without itself providing chat, completion, or an agentic loop. Its users are JetBrains-centric developers who run Claude Code-style CLI agents alongside the IDE.
