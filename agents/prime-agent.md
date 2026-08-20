---
name: "Prime Agent"
slug: "prime-agent"
layout: "agent.njk"
category: "agent"
maker: "PrimeIntellect-ai"
license: "MIT"
url: "https://github.com/PrimeIntellect-ai/prime-agent"
source_code_url: "https://github.com/PrimeIntellect-ai/prime-agent"
source_available: "Yes"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: "2026-05-08"
current_release: "2026-08-20"
stars: "17385"
language: "TypeScript (TUI), Python (agent runtime)"
homepage: null
mcp_support: null
plugin_support: "yes (skills as importable Python packages)"
claude_code_plugin: "no"
subagents: "yes (rlm(...) spawns child agents for parallel/background work)"
hooks: null
plan_mode: null
model_providers: "subscription and API-key (BYOK) providers via /login"
pricing: "open-source (MIT); subscription and BYOK options"
install_method: "binary"
docs_url: "https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/index.md"
plugin_docs_url: "https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/skills.md"
config_docs_url: "https://github.com/PrimeIntellect-ai/prime-agent/blob/main/packages/coding-agent/docs/providers.md"
download_url: "https://app.primeintellect.ai/prime-agent/install.sh"
maintained: "active"
sources:
  - "brad"
  - "zhouhao"
what_makes_it_special: "Uses a Recursive Language Model (RLM) that treats context as variables and tools as function calls in a persistent IPython REPL, combined with a Continual Harness that self-improves via /refine — persisting lessons, memories, and reusable subagent specifications as durable state across sessions."
---

Uses a Recursive Language Model (RLM) that treats context as variables and tools as function calls in a persistent IPython REPL, combined with a Continual Harness that self-improves via /refine — persisting lessons, memories, and reusable subagent specifications as durable state across sessions.
