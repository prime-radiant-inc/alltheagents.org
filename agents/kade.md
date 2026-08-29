---
name: "Kade"
slug: "kade"
layout: "agent.njk"
category: "agent"
maker: "kade"
license: "Apache-2.0"
url: "https://open-vsx.org/extension/kade/kade"
source_code_url: "https://github.com/KADEAI/Kade.git"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-04-07"
current_release: null
stars: null
language: null
homepage: "https://kadei.org"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic"
pricing: "open-source"
install_method: "Install from Open VSX"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-vsx.org/extension/kade/kade"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Cline/RooCode/Kilo fork for AI-assisted coding, planning, and development"
---

Kade takes the Cline lineage and rebuilds it around two bets: hierarchical multi-agent execution and aggressive context engineering. The main agent spawns sub-agents into their own tabs with isolated memory and independently chosen models, results flowing back up the tree. Tool calling moves past Cline's JSON/XML into proprietary Unified and Markdown protocols with multi-tool batching, and editing leans on fuzzy matching, whitespace normalization, and VS Code snapshots for exact undo/redo. The MCP Store advertises 25,000+ tools with security scanning. Distribution is concentrated on Open VSX (920k installs claimed), with a marketing-heavy README, only 7 commits of history, and a roadmap toward a full VS Code fork.
