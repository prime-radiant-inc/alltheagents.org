---
name: "codedna"
slug: "codedna"
layout: "agent.njk"
category: "agent"
maker: "Larens94"
license: "MIT"
url: "https://github.com/Larens94/codedna"
source_code_url: "https://github.com/Larens94/codedna"
source_available: True
platforms: []
first_released: "2026-03-15"
current_release: "2026-07-12"
stars: "144"
language: "Python"
homepage: "https://larens94.github.io/codedna"
mcp_support: null
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: null
model_providers: "Anthropic, Google, DeepSeek, Ollama"
pricing: "Free (structural-only mode); LLM mode ~$0.40/200 files (DeepSeek); free with local Ollama"
install_method: "Claude plugin (claude plugin marketplace add Larens94/codedna && claude plugin install codedna@codedna) or pipx install git+https://github.com/Larens94/codedna.git (Python 3.11+)"
docs_url: "https://github.com/Larens94/codedna/blob/main/SPEC.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "In-source communication protocol - AI agents embed architectural context (exports, used_by, related, rules, message) directly in code files. No external memory, retrieval pipeline, or infrastructure needed. Code carries its own context across sessions, models, and multi-agent teams."
---

In-source communication protocol - AI agents embed architectural context (exports, used_by, related, rules, message) directly in code files. No external memory, retrieval pipeline, or infrastructure needed. Code carries its own context across sessions, models, and multi-agent teams.
