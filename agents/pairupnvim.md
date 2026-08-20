---
name: "pairup.nvim"
slug: "pairupnvim"
layout: "agent.njk"
category: "agent"
maker: "Piotr1215"
license: "MIT"
url: "https://github.com/Piotr1215/pairup.nvim"
source_code_url: "https://github.com/Piotr1215/pairup.nvim"
source_available: True
platforms: []
first_released: "2025-09-04"
current_release: "2026-06-07"
stars: "53"
language: "Lua"
homepage: null
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: null
hooks: True
plan_mode: True
model_providers: "Anthropic (via Claude Code CLI)"
pricing: "Free / open-source (Claude Code CLI usage costs apply separately)"
install_method: "lazy.nvim: { 'Piotr1215/pairup.nvim', cmd = { 'Pairup' }, config = function() require('pairup').setup() end }"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Inline AI pair programming Neovim plugin using cc: markers in code that Claude edits directly; supports plan markers (ccp:) with CURRENT/PROPOSED conflict review and a peripheral Claude mode running a second autonomous instance in a sibling git worktree."
---

Inline AI pair programming Neovim plugin using cc: markers in code that Claude edits directly; supports plan markers (ccp:) with CURRENT/PROPOSED conflict review and a peripheral Claude mode running a second autonomous instance in a sibling git worktree.
