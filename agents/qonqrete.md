---
name: "QonQrete"
slug: "qonqrete"
layout: "agent.njk"
category: "agent"
maker: "QonQrete"
license: null
url: "https://plugins.jetbrains.com/plugin/30764-qonqrete"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-05-30"
current_release: null
stars: null
language: null
homepage: "https://qonqrete.sh"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "yes"
model_providers: null
pricing: null
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/30764-qonqrete"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Deterministic AI coding agent in secure sandboxes"
---

QonQrete starts from the premise that AI coding fails not because models are weak but because the process around them is uncontrolled, so it replaces free-form agent sessions with a deterministic pipeline: plain-English tasks in a tasq.md file are clarified, planned into concrete steps with completion criteria and cost estimates, built inside a containerized qage sandbox, then reviewed by a validator that produces a structured verdict and repair plan with capped iterations. Outputs land in staging paths rather than your repository until you explicitly sync them, and a no-sync mode keeps everything out of the repo entirely, which also keeps source code away from cloud AI services by default. Every run leaves an on-disk audit trail — timeline, event log, run manifest, validation artifacts — so any construction is reproducible and resumable. Per-agent model configuration supports Venice, DeepSeek, OpenRouter, and local MLX or llama.cpp runtimes, with API keys held in the OS keychain. Solo developers and small teams use it when they want AI-built code they can inspect, gate, and reproduce rather than auto-merged diffs.
