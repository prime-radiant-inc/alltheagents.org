---
name: "coding_agent_session_search"
slug: "coding-agent-session-search"
layout: "agent.njk"
category: "other"
maker: "Dicklesworthstone"
license: "MIT"
url: "https://github.com/Dicklesworthstone/coding_agent_session_search"
source_code_url: "https://github.com/Dicklesworthstone/coding_agent_session_search"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-11-21"
current_release: "2026-08-19"
stars: "1071"
language: "Rust"
homepage: null
mcp_support: "yes (HTTP)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Local only (MiniLM all-minilm-l6-v2, FNV-1a hash fallback)"
pricing: "open-source"
install_method: "brew, binary"
docs_url: "https://github.com/Dicklesworthstone/coding_agent_session_search#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Dicklesworthstone/coding_agent_session_search/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Unified TUI that aggregates and indexes local coding agent history across 24+ agents (Claude Code, Codex, Cursor, Gemini, Aider, ChatGPT, etc.) into a single searchable timeline. Fully local/private with hybrid BM25+vector search, multi-machine SSH sync, self-documenting robot API, token-budgeted answer packs for agent handoffs, and atomic index swaps for crash safety."
---

Developers running coding agents accumulate thousands of sessions across different CLIs, and the solutions, dead ends, and context in those sessions become unreachable because each tool stores history in its own format. cass indexes them all into one SQLite-backed archive on the local machine and serves lexical, semantic, and hybrid search through a Rust terminal UI and CLI. Semantic search runs a local MiniLM model with a hash-based fallback, so the index works without network access or API keys, and multi-machine search extends the corpus over SSH and rsync. A JSON robot mode exposes the archive to agents themselves, letting a coding agent query how similar problems were solved before. Individual developers and teams auditing agent activity are the users; the project is in alpha but developed intensively.
