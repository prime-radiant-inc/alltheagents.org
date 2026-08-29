---
name: "MiniCode"
slug: "minicode"
layout: "agent.njk"
category: "agent"
maker: "LiuMengxuan04"
license: "MIT"
url: "https://github.com/LiuMengxuan04/MiniCode"
source_code_url: "https://github.com/LiuMengxuan04/MiniCode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-31"
current_release: "2026-08-09"
stars: "1061"
language: "TypeScript, Rust, Python, Go, Java"
homepage: "https://liumengxuan04.github.io/MiniCode/"
mcp_support: "yes (stdio, HTTP)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic-compatible (via ANTHROPIC_BASE_URL)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://github.com/LiuMengxuan04/MiniCode/blob/main/USAGE.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Intentionally compact implementation of a Claude Code-like agent loop suitable for study, modification, and as a reference architecture. Available in 5 languages. Features full-screen TUI with session persistence, review-before-write edits, layered memory, context auto-compact/collapse, oversized-result offloading to disk, and local skills via SKILL.md files."
---

MiniCode exists to be read: it reproduces the Claude Code interaction model — terminal session, tool calls, review-before-write edits, persistent sessions — in a codebase small enough to study and modify, and then makes the architecture portable by maintaining equivalent implementations in Rust, Python, Go, and Java alongside the TypeScript original. The agent loop supports multiple tool calls per turn, and up to three concurrent read-only subagents explore while the root agent retains sole ownership of writes. Tool results that would bloat context are offloaded to disk with a preview left in place, and context auto-compacts as sessions grow. MCP servers attach over stdio or HTTP, and skills are discovered from SKILL.md files for local capability extension. Configuration runs through Anthropic-compatible environment variables, so any Anthropic-API-compatible backend — including local proxies — works, with a mock mode for offline development. Developers use it as a reference implementation, a hackable base for custom tooling, and a compact daily-driver alternative.
