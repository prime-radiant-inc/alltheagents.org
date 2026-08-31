---
name: "pairup.nvim"
slug: "pairupnvim"
layout: "agent.njk"
category: "other"
maker: "Piotr1215"
license: "MIT"
url: "https://github.com/Piotr1215/pairup.nvim"
source_code_url: "https://github.com/Piotr1215/pairup.nvim"
source_available: "True"
platforms: []
first_released: "2025-09-04"
current_release: "2026-06-07"
stars: "53"
language: "Lua"
homepage: "https://github.com/Piotr1215/pairup.nvim"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "yes"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic (via Claude Code CLI)"
pricing: "Free / open-source (Claude Code CLI usage costs apply separately)"
install_method: "lazy.nvim: { 'Piotr1215/pairup.nvim', cmd = { 'Pairup' }, config = function() require('pairup').setup() end }"
docs_url: "https://github.com/Piotr1215/pairup.nvim#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/Piotr1215/pairup.nvim#readme"
download_url: "https://github.com/Piotr1215/pairup.nvim"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Inline AI pair programming Neovim plugin using cc: markers in code that Claude edits directly; supports plan markers (ccp:) with CURRENT/PROPOSED conflict review and a peripheral Claude mode running a second autonomous instance in a sibling git worktree."
---

Chat-panel AI plugins force a copy-paste loop between conversation and buffer, and the file under edit never contains the instruction that motivated the change. pairup.nvim embeds the instructions in the code itself: developers write cc: markers (or apply gC{motion} operators), save, and the Claude Code CLI edits the file in place and removes the marker. Variants extend the pattern — cc!: extracts a durable rule into CLAUDE.md as it edits, ccp: wraps proposed changes in CURRENT/PROPOSED conflict markers so acceptance is a deliberate merge rather than an overwrite, and uu: surfaces Claude's clarifying questions inline. A 'peripheral Claude' mode runs a second autonomous instance in a sibling git worktree that implements spec-file changes in parallel, with statusline todo tracking and proposal diff views keeping state visible. Version 4.0 stripped overlays, sessions, and RPC in favor of this simpler inline model, with the legacy design on a branch. Neovim 0.11+ users with a Claude Code subscription who prefer editor-embedded, marker-driven AI editing are the audience.
