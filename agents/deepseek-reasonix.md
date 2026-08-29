---
name: "DeepSeek Reasonix"
slug: "deepseek-reasonix"
layout: "agent.njk"
category: "agent"
maker: "esengine"
license: "MIT"
url: "https://github.com/esengine/DeepSeek-Reasonix"
source_code_url: "https://github.com/esengine/DeepSeek-Reasonix"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-21"
current_release: "2026-08-20"
stars: null
language: "Go, TypeScript"
homepage: "http://reasonix.io/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "DeepSeek (preset), any OpenAI-compatible endpoint via config, optional dual-model (executor + planner)"
pricing: "Free / open source (donations accepted)"
install_method: "npm i -g reasonix, brew install esengine/reasonix/reasonix, desktop installer, VS Code extension, or make build from source"
docs_url: "https://esengine.github.io/DeepSeek-Reasonix/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/esengine/DeepSeek-Reasonix/releases"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "DeepSeek-native AI coding agent engineered around prefix-cache stability for long-running sessions. Distributed as a self-contained static Go binary. Features plan mode, permissions, workspace sandbox, per-turn checkpoints, config-driven providers/tools/plugins, multi-model support (executor + planner), and Extension Protocol v1 sidecars."
---

Reasonix is a DeepSeek-native coding agent built for long autonomous runs, with mechanics tuned to that goal: cache-aware context maintenance aligned with DeepSeek's prefix-cache pricing, a workspace sandbox, per-turn checkpoints with rewind, and a permission system for unattended operation. It runs as a single static Go binary in terminal/TUI, desktop, browser, or editor via ACP, with a config-driven setup (reasonix.toml), a planner/executor model split, and support for any OpenAI-compatible endpoint. Extensibility goes beyond MCP servers to an Extension Protocol with a Go SDK for sidecars that intercept events and add providers, and subagent profiles are first-class. The project is one of the most popular DeepSeek-focused harnesses (35k+ stars, very active development, bilingual docs, npm/Homebrew/desktop distribution).
