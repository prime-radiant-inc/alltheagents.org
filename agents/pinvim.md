---
name: "pi.nvim"
slug: "pinvim"
layout: "agent.njk"
category: "agent"
maker: "pablopunk"
license: "MIT"
url: "https://github.com/pablopunk/pi.nvim"
source_code_url: "https://github.com/pablopunk/pi.nvim"
source_available: "True"
platforms: []
first_released: "2026-02-06"
current_release: "2026-07-06"
stars: "240"
language: "Lua"
homepage: "https://github.com/pablopunk/pi.nvim"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenRouter, OpenAI, Anthropic"
pricing: "Free / open-source"
install_method: "Via lazy.nvim, packer.nvim, or mini.deps (requires the pi CLI to be installed globally)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/pablopunk/pi.nvim"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "The most minimal AI coding agent for Neovim, designed to embrace the simplicity of the CLI rather than imitating complex IDE features. Context-aware (sends buffer, cwd, selection, and optional diagnostics), unsaved-buffer aware (treats Neovim buffer content as the source of truth over stale disk files), and stays out of the user's way."
---

pi.nvim exists because its author found most Neovim AI plugins recreate the IDE bloat that drove people to Neovim in the first place. The plugin instead wraps the globally installed pi CLI, passing provider, model, and thinking options while contributing just what the editor knows: the current buffer, working directory, selection, and optional diagnostics, with unsaved buffer content treated as authoritative over files on disk. Commands stay minimal — ask, ask-with-selection, cancel, log — with no default keymaps and async execution that never blocks editing. Skills and extensions can be toggled per invocation by mapping to pi's own flags rather than adding a parallel feature set. Distributed under MIT with tests and CI, it serves Neovim users who want pi's terminal-native agent loop one keypress away without an IDE-style sidebar.
