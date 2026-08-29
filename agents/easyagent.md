---
name: "EasyAgent"
slug: "easyagent"
layout: "agent.njk"
category: "multiplexer"
maker: "hyqf98"
license: null
url: "https://plugins.jetbrains.com/plugin/31751-easyagent"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-05-25"
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
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/31751-easyagent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Aggregates Claude Code, OpenCode, and Codex CLI into one IDE experience"
---

IntelliJ users running more than one agent CLI end up switching between terminal windows and losing session history. EasyAgent hosts Claude Code, OpenCode, and Codex simultaneously inside the IDE, streaming each tool's thinking and tool calls into a unified chat, with @-file references, image paste, and /compact or /init commands mapped to the underlying CLIs. It renders the agents' file edits as diffs and can roll them back with one click, and it auto-detects installed CLI paths. The plugin is a thin aggregation layer — no bundled models or agents — aimed at developers already paying for several agent CLIs who want one window.
