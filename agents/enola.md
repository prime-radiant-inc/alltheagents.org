---
name: "enola"
slug: "enola"
layout: "agent.njk"
category: "other"
maker: "enola-labs"
license: "Apache-2.0"
url: "https://github.com/enola-labs/enola"
source_code_url: "https://github.com/enola-labs/enola"
source_available: "True"
platforms: []
first_released: "2026-02-10"
current_release: "2026-08-18"
stars: "168"
language: "Go"
homepage: "https://enola.tech"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: "Free/open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/enola-labs/enola/main/install.sh | sh; also available as a GitHub Action"
docs_url: "https://enola.tech"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/enola-labs/enola/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Architectural regression testing tool that indexes a repo into a dependency graph, pins a baseline before a change, and reports deltas with an exit code that can gate builds; deterministic, no AI model/embeddings, fully local; 19 MCP tools and session-grading hooks for coding agents (Claude Code, Cursor, Copilot, Codex, Pi)."
---

Enola addresses the gap between tests passing and architecture holding: builds and tests stay green while dependency cycles, layer violations, and scope creep accumulate. It parses source with tree-sitter into a typed fact graph across 23+ languages and formats (Go, TypeScript, Java, Python, Rust, Rails, .NET, Terraform, OpenAPI, gRPC), runs explainers that detect structural problems, and grades the change against the pinned baseline — one change, one verdict. The graph is exposed through 19 MCP tools so agents like Claude Code, Cursor, Copilot, and Codex read it before editing, and `enola install --hooks` grades each agent session afterward. Teams adopt it as a pre-commit hook, a CI gate via enola-action, or a plain CLI; everything runs locally with no LLM and no telemetry.
