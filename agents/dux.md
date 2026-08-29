---
name: "dux"
slug: "dux"
layout: "agent.njk"
category: "multiplexer"
maker: "patrickdappollonio"
license: "MIT"
url: "https://github.com/patrickdappollonio/dux"
source_code_url: "https://github.com/patrickdappollonio/dux"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-03-22"
current_release: "2026-08-19"
stars: "66"
language: "Rust"
homepage: "https://getdux.app/"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: "Claude, Codex, OpenCode, custom"
pricing: "Free / open source (MIT)"
install_method: "brew install patrickdappollonio/tap/dux, npm install -g @patrickdappollonio/dux, or curl install script; binary download from Releases"
docs_url: "https://getdux.app/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/patrickdappollonio/dux/releases"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Terminal UI for running multiple AI coding agents side by side, each in its own isolated git worktree, with companion terminals, macros, AI commit generation, session forking, and a command palette"
---

dux organizes parallel agent work around git worktrees: creating an agent branches a fresh worktree, spawns the CLI through a real PTY, and shows it alongside companion terminals for builds and tests. Because nothing sits between the CLI and the terminal, permission dialogs, slash commands, hooks, and MCP servers behave exactly as they do standalone. Agents can be forked to try a variant approach without losing the original, companion terminals handle builds and tests, and commit generation plus a command palette round out the tooling. The author positions it against heavier orchestration layers: no JSON-RPC, no adapters, just terminals and worktrees with low resource overhead.
