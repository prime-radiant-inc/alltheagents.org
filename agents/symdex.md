---
name: "SymDex"
slug: "symdex"
layout: "agent.njk"
category: "other"
maker: "husnainpk"
license: "MIT"
url: "https://github.com/husnainpk/SymDex"
source_code_url: "https://github.com/husnainpk/SymDex"
source_available: "True"
platforms: []
first_released: "2026-03-08"
current_release: "2026-04-22"
stars: "208"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "n/a"
subagents: "False"
hooks: "no"
plan_mode: "no"
model_providers: "Local sentence-transformers, Voyage, OpenAI-compatible /embeddings, Gemini Embedding (embedding backends)"
pricing: "Free / open-source"
install_method: "pip install symdex (or uv tool install symdex / uvx symdex); optional extras: symdex[local], symdex[voyage], symdex[voyage-multimodal]"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/symdex/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Repo-local symbolic indexing engine turning a checked-out repo into a local SQLite knowledge base of symbols, routes, relations, docs, tests, and context. Provides 21 MCP tools, HTTP route extraction across 10+ frameworks, call graph traversal, token-budgeted context packs, and ROI/token-savings reporting via both CLI and MCP without requiring a hosted index."
---

SymDex exists because agents burn context reading whole files when they need one definition or call site. It indexes a checked-out repository into a local SQLite database: exact symbols with byte offsets, file and repo outlines, HTTP routes extracted across a dozen web frameworks, caller/callee graphs, docs, and tests, spanning roughly 20 language surfaces via tree-sitter. Agents reach it through an MCP server (21 tools, stdio or HTTP) or a CLI, and an installable skill teaches agents to query the index instead of browsing files; retrieval is token-budgeted so a context pack fits the model's budget, and everything runs locally with optional sentence-transformers or Voyage embeddings. Reports of token savings and index ROI are built in. Developers wiring their own agents to precise, hosted-service-free codebase retrieval are the intended users.
