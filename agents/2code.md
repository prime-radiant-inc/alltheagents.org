---
name: "2code"
slug: "2code"
layout: "agent.njk"
category: "other"
maker: "AkaraChen"
license: "MIT"
url: "https://github.com/AkaraChen/2code"
source_code_url: "https://github.com/AkaraChen/2code"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-02-10"
current_release: "2026-08-17"
stars: "25"
language: "TypeScript"
homepage: "https://2code.akr.moe"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (hosts agents in terminals; agents bring their own providers)"
pricing: "Free / open-source"
install_method: "brew install --cask akarachen/tap/2code (macOS); Windows/Linux experimental"
docs_url: "https://2code.akr.moe/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/akarachen/2code/releases/latest"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Desktop 'vibe coding' workstation that treats the parallel, ephemeral state created by AI-assisted development (running commands, multiple agents, branch experiments, uncommitted diffs) as the primary interface — keeping persistent terminals, Git visibility, and isolated worktree profiles together in one calm workspace."
---

AI-assisted development produces a mess of parallel state: several terminals, experimental branches, uncommitted diffs, and agents that may or may not be waiting for input, none of which a conventional editor surfaces well. 2code is a Tauri 2 desktop app (React/TypeScript frontend, Rust backend, SQLite) that organizes that state into one workspace: persistent terminals, per-feature git worktree lanes, and status detection that infers whether an agent is running, waiting, or finished from terminal output and progress sequences. It is macOS-first with experimental Windows and Linux builds, installed via Homebrew cask. Its users are solo developers running one or two agents alongside manual terminal work.
