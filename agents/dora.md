---
name: "dora"
slug: "dora"
layout: "agent.njk"
category: "agent"
maker: "butttons"
license: "MIT"
url: "https://github.com/butttons/dora"
source_code_url: "https://github.com/butttons/dora"
source_available: True
platforms:
  - "CLI"
first_released: "2026-01-17"
current_release: "2026-03-10"
stars: "108"
language: "TypeScript"
homepage: "https://dora-cli.dev"
mcp_support: True
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: True
plan_mode: null
model_providers: null
pricing: "Free/open-source (MIT)"
install_method: "Download binary from GitHub releases (macOS ARM/Intel, Linux); or bun install -g @butttons/dora"
docs_url: "https://dora-cli.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/butttons/dora/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "CLI that converts a SCIP (Sourcegraph Code Intelligence Protocol) index into a queryable SQLite database, letting AI agents query codebases in milliseconds via SQL/CLI instead of token-expensive file exploration; combines SCIP for precise symbol/reference data and Tree-sitter (WASM) for complexity/signatures/code smells; output defaults to TOON (compact JSON format optimized for LLM token efficiency) with --json fallback; built-in MCP server (dora mcp); agent integration (hooks, skills, AGENTS.md snippets) for Claude Code, OpenCode, Cursor, Windsurf; explicitly designed as an alternative to grep/find/glob for AI agents."
---

CLI that converts a SCIP (Sourcegraph Code Intelligence Protocol) index into a queryable SQLite database, letting AI agents query codebases in milliseconds via SQL/CLI instead of token-expensive file exploration; combines SCIP for precise symbol/reference data and Tree-sitter (WASM) for complexity/signatures/code smells; output defaults to TOON (compact JSON format optimized for LLM token efficiency) with --json fallback; built-in MCP server (dora mcp); agent integration (hooks, skills, AGENTS.md snippets) for Claude Code, OpenCode, Cursor, Windsurf; explicitly designed as an alternative to grep/find/glob for AI agents.
