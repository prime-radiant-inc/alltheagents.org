---
name: "EggShell"
slug: "eggshell"
layout: "agent.njk"
category: "multiplexer"
maker: "Best Practice"
license: null
url: "https://plugins.jetbrains.com/plugin/31171-eggshell"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-08-10"
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
pricing: "free"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/31171-eggshell"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Embeds terminal sessions dedicated to AI CLI coding agents"
---

EggShell exists because JetBrains users wanted to talk to CLI coding agents without leaving the IDE or juggling a separate terminal app. It opens a native IDE terminal bound to a chosen agent CLI, tracks chat sessions and their owning agent in .idea/eggshell.xml so tabs persist across restarts, and wires IDE state into the conversation: files dragged from the project tree become agent-specific @path references, editor selections become line-range code citations, and clipboard images are saved and passed as paths. Agent launch commands are editable templates in Settings with dry-run test buttons to validate argv before spawning, and API keys live in the IDE Password Safe while the plugin itself collects no data. The split-plugin structure lets it run identically in local IDEs and JetBrains Gateway remote environments.
