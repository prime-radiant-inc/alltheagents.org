---
name: "agent-orchestrator"
slug: "agent-orchestrator"
layout: "agent.njk"
category: "multiplexer"
maker: "willynikes2"
license: "MIT"
url: "https://github.com/willynikes2/agent-orchestrator"
source_code_url: "https://github.com/willynikes2/agent-orchestrator"
source_available: True
platforms:
  - "CLI"
first_released: "2026-03-17"
current_release: "2026-04-03"
stars: "65"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic (Claude), OpenAI (Codex/GPT), Google (Gemini)"
pricing: "~$60/month total for CLI subscriptions (~$20 each for Claude Pro, OpenAI, Google); no per-token API billing"
install_method: "git clone + pip install -r requirements.txt + python3 daniel.py --setup"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/willynikes2/agent-orchestrator.git"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Terminal-based multi-agent orchestrator wrapping Claude, Codex, and Gemini CLIs with automatic failover (next-man-up); agents share context via a knowledge base server; routes messages through configurable role chains"
---

Terminal-based multi-agent orchestrator wrapping Claude, Codex, and Gemini CLIs with automatic failover (next-man-up); agents share context via a knowledge base server; routes messages through configurable role chains
