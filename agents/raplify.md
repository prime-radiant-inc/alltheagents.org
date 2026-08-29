---
name: "Raplify"
slug: "raplify"
layout: "agent.njk"
category: "multiplexer"
maker: "Raplify"
license: null
url: "https://plugins.jetbrains.com/plugin/33194-raplify"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-08-14"
current_release: null
stars: null
language: null
homepage: null
mcp_support: "no"
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
download_url: "https://plugins.jetbrains.com/plugin/33194-raplify"
maintained: "dormant"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "GUI for AI coding agents with four tool windows"
---

Raplify embeds an AI coding-agent workspace directly into JetBrains IDEs, built around the observation that agents are most useful when the developer can see the same code structures the agent is reasoning about. Its four tool windows cover an agent chat panel, every REST endpoint discovered in the source grouped and searchable by path, the Java call flow resolved from the project's real index rather than guessed from names, and a database schema browser with entity-relationship layout. The chat panel passes the current editor selection as context, offers model and permission-mode selectors, and renders tool cards and project commands inline. Because it depends on Node.js and an installed Claude CLI, the agent runtime stays external and versionable while Raplify supplies the visual surface. Backend and full-stack developers use it to keep endpoint maps, call paths, and schema visible while directing an agent without leaving the IDE.
