---
name: "Doubao-Seed-Code"
slug: "doubao-seed-code"
layout: "agent.njk"
category: "other"
maker: "ByteDance"
license: "Proprietary"
url: "https://www.doubao.com"
source_code_url: null
source_available: "No (proprietary)"
platforms:
  - "API"
first_released: "2025-11"
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "usage"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "bing_ddg_chinese"
what_makes_it_special: "ByteDance coding model built on the Doubao LLM stack, optimized for code generation, code completion, and agentic programming tasks. Achieves SOTA results on coding benchmarks like SWE-Bench. A model, not an agent harness. Details not verifiable from the doubao.com homepage (returned empty)."
---

Doubao-Seed-Code is ByteDance's entry in the agentic-coding model race, trained for multi-step tool-using loops in terminal environments rather than single-shot completion. It ships a 256K context window, targets repository-level tasks such as file editing and iterative test runs, and posts SWE-bench Verified scores in the low 60s at roughly a third of Claude Sonnet's price. ByteDance distributes it through Volcano Engine and wires it into its own coding tools, and third-party harnesses — DeerFlow among them — recommend it as a backend. In this census it is a model that other harnesses consume, not a harness itself.
