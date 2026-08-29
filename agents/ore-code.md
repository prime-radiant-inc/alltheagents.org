---
name: "ore-code"
slug: "ore-code"
layout: "agent.njk"
category: "agent"
maker: "233i"
license: "MIT"
url: "https://github.com/233i/ore-code"
source_code_url: "https://github.com/233i/ore-code"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-05-31"
current_release: "2026-08-03"
stars: "104"
language: "TypeScript, Rust"
homepage: "https://github.com/233i/ore-code"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, Mimo, Ark Coding, custom endpoints"
pricing: "Free / open source"
install_method: "Download macOS .dmg from GitHub Releases; or build from source via pnpm install && pnpm dev (Tauri 2 build)"
docs_url: "https://github.com/233i/ore-code/blob/main/docs/README.md"
plugin_docs_url: null
config_docs_url: "https://github.com/233i/ore-code/blob/main/docs"
download_url: "https://github.com/233i/ore-code/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "DeepSeek-first coding agent with a native desktop shell (Tauri/Rust) providing a secure OS boundary for file, shell, process, Git, keychain, artifact, and MCP operations; long-context features including history compression, context briefing, checkpoint summaries, and provider-aware request shaping"
---

Desktop coding agents typically hand the model broad shell access, which makes accidental filesystem or process damage hard to contain. Ore Code structures the problem differently: a Tauri 2.x shell with a Rust layer mediates every sensitive operation — file, shell, process, Git, keychain, artifact, and MCP calls — while a TypeScript agent runtime and React frontend drive the workflow above it. The agent targets DeepSeek first (with Mimo, Ark Coding, or custom endpoints supported) and includes long-context features such as history compression and checkpoint summaries for extended sessions, plus project-aware chat, diff review, task-change restore, a skills system, and MCP server support. Configuration lives in ~/.ore-code/config.toml with API keys stored in the OS keychain. It is early — v0.1.1, 39 commits, macOS Apple Silicon only with an ad-hoc-signed DMG and Windows pending — so it is best treated as a promising architecture preview for developers invested in the DeepSeek ecosystem.
