---
name: "indxr"
slug: "indxr"
layout: "agent.njk"
category: "other"
maker: "bahdotsh"
license: "MIT"
url: "https://github.com/bahdotsh/indxr"
source_code_url: "https://github.com/bahdotsh/indxr"
source_available: "True"
platforms: []
first_released: "2026-03-23"
current_release: "2026-04-07"
stars: "71"
language: "Rust"
homepage: "https://github.com/bahdotsh/indxr"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "False"
model_providers: "Anthropic, OpenAI"
pricing: "Free/open-source (MIT)"
install_method: "cargo install indxr --features wiki (via crates.io), or build from source via git clone + cargo build"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Fast codebase indexer and self-updating knowledge wiki for AI agents, backed by a structural index (tree-sitter AST parsing for 8 languages + regex for 19 more). Provides 26 MCP tools plus 9 wiki MCP tools, token-aware progressive truncation, git structural diffing, dependency graphs, complexity hotspot analysis, monorepo support, and one-command setup for multiple AI agents. Agents can record failure patterns so future agents don't repeat mistakes."
---

indxr gives coding agents durable knowledge instead of forcing them to re-derive a codebase every session. The structural index combines tree-sitter ASTs with regex extraction for 27 languages, exposing symbol lookup, caller tracing, and complexity hotspots through MCP. On top sits a Markdown wiki in .indxr/wiki/ that agents both read and write: `wiki_record_failure` logs mistakes so later agents avoid them, and `wiki_compound` merges new findings into existing pages. Watch mode regenerates pages automatically using Anthropic or OpenAI keys. One-command setup wires it into Claude Code, Cursor, Windsurf, and Codex CLI.
