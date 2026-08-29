---
name: "agent-orchestrator"
slug: "agent-orchestrator"
layout: "agent.njk"
category: "multiplexer"
maker: "willynikes2"
license: "MIT"
url: "https://github.com/willynikes2/agent-orchestrator"
source_code_url: "https://github.com/willynikes2/agent-orchestrator"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-17"
current_release: "2026-04-03"
stars: "65"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude), OpenAI (Codex/GPT), Google (Gemini)"
pricing: "~$60/month total for CLI subscriptions (~$20 each for Claude Pro, OpenAI, Google); no per-token API billing"
install_method: "git clone + pip install -r requirements.txt + python3 daniel.py --setup"
docs_url: "https://github.com/willynikes2/agent-orchestrator#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/willynikes2/agent-orchestrator.git"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Terminal-based multi-agent orchestrator wrapping Claude, Codex, and Gemini CLIs with automatic failover (next-man-up); agents share context via a knowledge base server; routes messages through configurable role chains"
---

Three CLI subscriptions cover most frontier models, but each has separate quotas, and hitting one mid-task means losing momentum, so this orchestrator wraps the Claude, Codex, and Gemini CLIs and fails over automatically — when one agent hits a cap or errors, the next in the role chain continues the work. It is deliberately minimal: a single Python file (daniel.py, about 1,100 lines) with role-based routing chains (orchestrator, implementation, ui-docs, review), direct addressing like @claude or @codex, cooldown timers on exhausted agents, and an optional knowledge-base server for shared context. New agents are added by writing roughly 30-line wrapper functions. Solo developers running all three ~$20/month CLI subscriptions are the intended users.
