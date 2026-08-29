---
name: "loom"
slug: "loom"
layout: "agent.njk"
category: "other"
maker: "husu"
license: null
url: "https://github.com/husu/loom"
source_code_url: "https://github.com/husu/loom"
source_available: "True"
platforms: []
first_released: "2026-05-15"
current_release: "2026-05-28"
stars: "581"
language: "TypeScript"
homepage: "https://loom.vegamo.cn"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek, OpenAI"
pricing: "free"
install_method: "npm"
docs_url: "https://loom.vegamo.cn"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "AI-driven JSON Schema API documentation generator with a TUI chat interface, built-in React-based Web viewer, and a Mock service that auto-generates realistic mock data from schemas. Supports entity modeling with x-entity-ref reuse, LLM-powered source code API scanning, in-TUI service control, and vibe-coding style doc creation."
---

API documentation drifts out of sync with code, and Loom addresses that with a chat TUI where developers describe endpoints in natural language and an LLM writes versioned JSON Schema files into docs/, or points /scan at existing source code to derive schemas from the implementation. A four-phase scan pipeline with checkpoints and resume keeps long scans resumable, and entity references (x-entity-ref) keep shared schemas consistent across endpoints. The generated docs render in a bundled React viewer, and a Fastify mock service turns schemas into realistic test data with status-code overrides. Backend teams maintaining REST APIs are the intended users; the project is early-stage with a small commit history, silent usage telemetry, and no license file.
