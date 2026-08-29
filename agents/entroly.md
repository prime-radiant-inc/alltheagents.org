---
name: "Entroly"
slug: "entroly"
layout: "agent.njk"
category: "other"
maker: "juyterman1000"
license: "Apache-2.0"
url: "https://github.com/juyterman1000/entroly"
source_code_url: "https://github.com/juyterman1000/entroly"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-03-07"
current_release: "2026-08-19"
stars: "437"
language: "Python, Rust, TypeScript"
homepage: "https://juyterman1000.github.io/entroly/docs/index.html"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google, NVIDIA Nemotron via Ollama, OpenAI/Anthropic-compatible endpoints"
pricing: "Free / open-source (Apache-2.0); no paid tier; local verification requires no API key"
install_method: "pip install -U entroly, npm install -g entroly, cargo build --release (Rust), brew install juyterman1000/entroly/entroly, or docker pull ghcr.io/juyterman1000/entroly:latest"
docs_url: "https://juyterman1000.github.io/entroly/docs/index.html"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/entroly/"
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Drop-in context assurance / local-first Context OS for AI coding agents; content-addressed evidence with byte-exact recovery, auditable Context Receipts, local hallucination detection (WITNESS) without a second API call, cache-aware compression that preserves provider prompt-cache discounts, and panic-rescue for over-long sessions"
---

Entroly was built on the observation that agent failures often trace to degraded context — truncated, lossy, or unverifiable — and that token cost scales with noisy context. It intercepts requests on routes it controls, selects the highest-value evidence, compresses it, and issues receipts that make every context decision auditable and recoverable byte-for-byte, with a local WITNESS detector flagging hallucination risk without cloud calls. Attachment paths include an MCP server (with a .mcpb bundle and Smithery config), a Claude Code plugin, an API-key proxy, and an SDK, so teams can adopt it incrementally across Claude Code, Codex, Cursor, Copilot, and Aider. The project is candid that savings are workload-dependent — its own benchmark shows accuracy dropping on some workloads — and `entroly simulate` estimates savings before adoption.
