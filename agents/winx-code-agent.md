---
name: "winx-code-agent"
slug: "winx-code-agent"
layout: "agent.njk"
category: "other"
maker: "gabrielmaialva33"
license: "MIT"
url: "https://github.com/gabrielmaialva33/winx-code-agent"
source_code_url: "https://github.com/gabrielmaialva33/winx-code-agent"
source_available: "True"
platforms: []
first_released: "2025-04-17"
current_release: "2026-08-20"
stars: "33"
language: "Rust"
homepage: "https://crates.io/crates/winx-code-agent"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "True"
subagents: "False"
hooks: "False"
plan_mode: "no"
model_providers: "None — MCP tool server for any MCP client (Claude Code, Codex, Cursor, ChatGPT)"
pricing: "Free/open source (MIT)"
install_method: "cargo install winx-code-agent (Rust 1.88+); also GitHub Release .tar.gz bundles and build from source"
docs_url: "https://github.com/gabrielmaialva33/winx-code-agent/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/gabrielmaialva33/winx-code-agent/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Native Rust (not a Python wrapper) remote MCP runtime for coding agents with durable daemon architecture (winxd + winx-guardian per session). Sessions survive HTTP disconnects, client restarts, and adapter upgrades. Agent-native terminal semantics (real PTY, Ctrl+C, interactive TUIs), tree-sitter code navigation across 11 languages, robust SEARCH/REPLACE editing tolerant of LLM mistakes, token-budgeted output compression, and secret redaction by default."
---

winx-code-agent provides durable, remote-first tool access for coding agents that connect over MCP: real PTY shell sessions survive HTTP disconnects, client restarts, and adapter upgrades because a separate winxd daemon and per-session winx-guardian process own the shell. It exposes a configurable tool catalog (BashCommand, ReadFiles, EditFiles with search_replace/line_patch/undo, tree-sitter CodeMap across 13 languages, ContextSave, ReadImage) over Streamable HTTP for hosted agents or stdio for local clients like Claude Code and Cursor, with workspace modes ranging from full access to read-only architect mode. Beginning as a Rust port of WCGW, it is hardened with fuzz tests, loom model checking, SBOM attestations, secret redaction, and an opt-in Landlock sandbox. It is a tool server for agents rather than an agent itself, MIT-licensed, and installable via cargo.
