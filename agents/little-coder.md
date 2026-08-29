---
name: "little-coder"
slug: "little-coder"
layout: "agent.njk"
category: "agent"
maker: "itayinbarr"
license: "Apache-2.0"
url: "https://github.com/itayinbarr/little-coder"
source_code_url: "https://github.com/itayinbarr/little-coder"
source_available: "Yes"
platforms: []
first_released: "2026-04-11"
current_release: "2026-08-15"
stars: "2457"
language: "TypeScript"
homepage: "https://itayinbarr.github.io/little-coder/"
mcp_support: null
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "llama.cpp, Ollama, LM Studio, Anthropic, OpenAI, local"
pricing: "free"
install_method: "npm"
docs_url: "https://itayinbarr.github.io/little-coder/"
plugin_docs_url: "https://itayinbarr.github.io/little-coder/docs/extensions"
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Coding agent tuned for small local models, built on pi, with plan mode, dispatch sub-coders, per-phase model selection, read-before-edit enforcement, and a lifecycle-hook extension system."
---

Small local models fail at agentic coding mostly because harnesses assume frontier-model context discipline, so little-coder wraps the pi agent with extensions that enforce read-before-edit, gate permissions, inject skills per turn, watch for compaction, and monitor output quality — all as lifecycle hooks rather than core patches. Plan mode dispatches isolated read-only sub-coders for research and hands a written plan to a fresh session on the action model, with separate /plan-model and /action-model commands for big-plan/small-implement economics. Everything ships as extensions and skills around pi, keeping cold-start context near 7k tokens. Hobbyists running Qwen-class models on consumer laptops are the target audience, with published Terminal-Bench and GAIA results.
