---
name: "codebase-index-cli"
slug: "codebase-index-cli"
layout: "agent.njk"
category: "other"
maker: "dudufcb1"
license: "MIT"
url: "https://github.com/dudufcb1/codebase-index-cli"
source_code_url: "https://github.com/dudufcb1/codebase-index-cli"
source_available: "True"
platforms: []
first_released: "2025-10-17"
current_release: "2025-12-02"
stars: "59"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "False"
model_providers: "OpenAI, OpenAI-compatible (LM Studio, Nebius AI Studio, Together AI), Ollama"
pricing: "Free/open source"
install_method: "git clone + run platform install script (./scripts/install.sh on Linux)"
docs_url: "https://github.com/dudufcb1/codebase-index-cli/blob/codebase-cli/INSTALL.md"
plugin_docs_url: null
config_docs_url: "https://github.com/dudufcb1/codebase-index-cli/blob/codebase-cli/EMBEDDER_CONFIG.md"
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Lightweight semantic code indexing engine for AI coding assistants lacking native semantic search; real-time file watching, git commit tracking with LLM analysis, dual storage (SQLite-vec / Qdrant), tree-sitter parsing for 29+ languages, per-vector-store embedder configuration, and Claude Code integration via SessionStart hook."
---

Codebase-index-cli exists because most coding assistants locate code through text matching, which fails on semantic queries like 'where is rate limiting enforced.' It watches a workspace continuously, parses files with tree-sitter across 29+ languages, and maintains vector indexes in either SQLite-vec for local single-user use or Qdrant for larger deployments, with embedders configurable per store (OpenAI, OpenAI-compatible endpoints such as LM Studio or Together, or Ollama). An experimental layer analyzes git commit history with an LLM, indexing the semantic meaning of changes including retroactive indexing of historical commits. Integration targets Claude Code specifically through a SessionStart hook that launches indexing at session start, and the author ships a companion MCP server so MCP-capable IDEs can query the indexes. The project is small and self-described as experimental, derived from Roo Code's indexer.
