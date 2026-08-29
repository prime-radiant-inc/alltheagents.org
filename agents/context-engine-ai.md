---
name: "context-engine-ai"
slug: "context-engine-ai"
layout: "agent.njk"
category: "other"
maker: "Quinnod345"
license: "MIT"
url: "https://github.com/Quinnod345/context-engine"
source_code_url: "https://github.com/Quinnod345/context-engine"
source_available: "True"
platforms: []
first_released: "2026-03-01"
current_release: "2026-03-16"
stars: null
language: "TypeScript"
homepage: "https://quinnod345.github.io/context-engine/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (embeddings), Local TF-IDF, Anthropic (via MCP clients)"
pricing: "Open-source (MIT); managed cloud API with Free, Pro ($29/mo), Team ($99/mo), and Enterprise (custom) tiers"
install_method: "npm install context-engine-ai"
docs_url: "https://github.com/Quinnod345/context-engine/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Quinnod345/context-engine"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Lightweight context engine for AI agents that ingests events from any source and builds semantic context with ranked, time-decayed results; requires no vector database or API keys by default; runs as an MCP tool server for Claude Desktop, Cursor, and Windsurf; pluggable storage/embedding adapters"
---

Agents that operate over hours lose track of what happened earlier, and the conventional fix - a vector database plus an embedding API - adds infrastructure many projects cannot justify. context-engine-ai packages agent memory as a TypeScript library: callers ingest typed events, query in natural language, and receive ranked, time-decayed results together with a summary string formatted for direct injection into a system prompt. The default stack is SQLite with local TF-IDF embeddings, requiring no vector database, no API keys, and no network access; optional adapters swap in PostgreSQL with pgvector and OpenAI embeddings. The same engine is exposed through a CLI, an HTTP server, and an example MCP server wired for Claude Desktop, Cursor, and Windsurf. Developers building agent memory without infrastructure overhead are the target users, though the project is new with minimal adoption.
