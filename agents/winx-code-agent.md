---
name: "winx-code-agent"
slug: "winx-code-agent"
layout: "agent.njk"
category: "agent"
maker: "gabrielmaialva33"
license: "MIT"
url: "https://github.com/gabrielmaialva33/winx-code-agent"
source_code_url: "https://github.com/gabrielmaialva33/winx-code-agent"
source_available: True
platforms: []
first_released: "2025-04-17"
current_release: "2026-08-20"
stars: "33"
language: "Rust"
homepage: "https://crates.io/crates/winx-code-agent"
mcp_support: True
plugin_support: False
claude_code_plugin: True
subagents: False
hooks: False
plan_mode: null
model_providers: null
pricing: "Free/open source (MIT)"
install_method: "cargo install winx-code-agent (Rust 1.88+); also GitHub Release .tar.gz bundles and build from source"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/gabrielmaialva33/winx-code-agent/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Native Rust (not a Python wrapper) remote MCP runtime for coding agents with durable daemon architecture (winxd + winx-guardian per session). Sessions survive HTTP disconnects, client restarts, and adapter upgrades. Agent-native terminal semantics (real PTY, Ctrl+C, interactive TUIs), tree-sitter code navigation across 11 languages, robust SEARCH/REPLACE editing tolerant of LLM mistakes, token-budgeted output compression, and secret redaction by default."
---

Native Rust (not a Python wrapper) remote MCP runtime for coding agents with durable daemon architecture (winxd + winx-guardian per session). Sessions survive HTTP disconnects, client restarts, and adapter upgrades. Agent-native terminal semantics (real PTY, Ctrl+C, interactive TUIs), tree-sitter code navigation across 11 languages, robust SEARCH/REPLACE editing tolerant of LLM mistakes, token-budgeted output compression, and secret redaction by default.
