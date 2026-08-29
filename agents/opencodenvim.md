---
name: "opencode.nvim"
slug: "opencodenvim"
layout: "agent.njk"
category: "other"
maker: "sudo-tee"
license: "Apache-2.0"
url: "https://github.com/sudo-tee/opencode.nvim"
source_code_url: "https://github.com/sudo-tee/opencode.nvim"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-06-27"
current_release: "2026-08-18"
stars: "926"
language: "Lua"
homepage: "https://github.com/sudo-tee/opencode.nvim"
mcp_support: "yes — mcp_picker keymap and /mcp command to manage MCP server connections"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes — built-in agents (Build, Plan) and custom agents; child session navigation"
hooks: "yes — on_file_edited, on_session_loaded, on_done_thinking, on_permission_requested"
plan_mode: "yes — built-in Plan agent for planning/analysis without file changes"
model_providers: "delegated to the opencode CLI (opencode auth login / config.json); the plugin adds a provider/model picker and per-prompt overrides like model=github-copilot/gpt-4.1"
pricing: "open-source"
install_method: "neovim"
docs_url: "https://opencode.ai/docs/"
plugin_docs_url: null
config_docs_url: "https://github.com/sudo-tee/opencode.nvim#configuration"
download_url: "https://github.com/sudo-tee/opencode.nvim"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Tight Neovim integration with the opencode AI agent, capturing rich editor context automatically; snapshot/diff/restore system for safe code changes; support for external/containerized/WSL servers with path mapping."
---

Running opencode in a terminal while editing in Neovim splits attention and loses editor context the agent needs. This Lua plugin, a fork of goose.nvim, embeds the agent in Neovim: a chat panel holds persistent sessions per workspace, and every prompt automatically carries the current file, visual selection, LSP diagnostics, and cursor position, with @-file mentions for explicit references. A snapshot system underpins safety — diffs are reviewable, reverts are one keystroke, and restore points let users back out of unwanted agent edits. It also surfaces opencode's build/plan agents and custom agents, MCP server support, and permission handling, and supports connecting to external, containerized, or WSL opencode servers rather than only a local CLI. Installation is a standard lazy.nvim spec with the opencode CLI (v0.6.3+) required; Apache-2.0 licensed and under active development with 931 stars, though the README warns of breaking changes. Neovim users who want Cursor-grade context sharing with a terminal agent are the audience.
