---
name: "klaatcode"
slug: "klaatcode"
layout: "agent.njk"
category: "agent"
maker: "KlaatAI"
license: "Apache-2.0"
url: "https://github.com/KlaatAI/klaatcode"
source_code_url: "https://github.com/KlaatAI/klaatcode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-17"
current_release: "2026-08-16"
stars: "357"
language: "TypeScript"
homepage: "https://klaatai.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Klaatu routing, OpenAI-compatible, Claude, GPT, Gemini, DeepSeek, Kimi K3"
pricing: "usage"
install_method: "npm install -g klaatcode, or brew install KlaatAI/klaatcode/klaatcode, or curl installer"
docs_url: "https://klaatai.com/docs"
plugin_docs_url: null
config_docs_url: "https://klaatai.com/docs/configuration"
download_url: "https://klaatai.com/api/install"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Terminal-native AI coding agent with per-request smart model routing across 6 cost tiers; real code knowledge graph (call graph, semantic search, blast-radius); no Continue button (free unlimited tool rounds); visible cost caps and burn-rate monitoring; compaction with self-check; reproducible benchmarks."
---

klaatcode targets the cost problem of terminal coding agents: most tokens are spent re-reading files the agent has already seen. Indexing the project into a call graph with semantic search lets the agent query callers, callees, and blast radius directly, and routing each request through Klaatu-o1 escalates or de-escalates the model tier per task. Tool calls within a request are free; only user messages consume quota, and cost guards with burn-rate monitoring bound runaway sessions. Subagents, lifecycle hooks, plan mode, and MCP presets cover the standard harness surface, and the claimed $0.027-per-solved-task benchmark ships as a reproducible bun run bench script for verification.
