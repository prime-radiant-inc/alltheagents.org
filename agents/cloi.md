---
name: "cloi"
slug: "cloi"
layout: "agent.njk"
category: "agent"
maker: "gabrielchasukjin"
license: "MIT"
url: "https://github.com/gabrielchasukjin/cloi"
source_code_url: "https://github.com/gabrielchasukjin/cloi"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-05-01"
current_release: "2026-08-11"
stars: "408"
language: "JavaScript"
homepage: "http://www.cloi-ai.com"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "no"
plan_mode: "True"
model_providers: "Ollama"
pricing: "Free / open-source (runs locally)"
install_method: "npm install -g @cloi-ai/cloi; requires Ollama, Node 22.5+"
docs_url: "https://github.com/gabrielchasukjin/cloi#readme"
plugin_docs_url: null
config_docs_url: "docs/configuration.md (in-repo)"
download_url: "https://www.npmjs.com/package/@cloi-ai/cloi"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Local-first terminal coding agent powered by Ollama; auto-selects models by measuring hardware (VRAM/RAM/cores); two-model system with escalation on failure; answer verification without model calls (line citations/quotes checked against workspace); named reusable results across sessions; session-long Python interpreter with stored results; history summarised instead of dropping tokens; guardrails (workspace path containment, permission prompts, secret redaction)."
---

Cloi exists for developers who want agentic coding without any cloud dependency: it runs entirely through Ollama with no API key, and its model selection is measured rather than guessed - the installer benchmarks the hardware and proposes a VRAM-resident primary plus a larger RAM-resident fallback. Escalation is triggered by observed failure signals (repeated identical calls, malformed tool calls, narrated-but-skipped steps) rather than task classification, and the inheriting model receives everything already attempted. Verification checks citations and quotes against the real workspace before spending model calls, and named tool results persist across sessions. The README publishes its own limits, including zero for twelve on hard cross-file debugging with 8 GB-class models.
