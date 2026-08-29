---
name: "auto-co"
slug: "auto-co"
layout: "agent.njk"
category: "agent"
maker: "NikitaDmitrieff"
license: "MIT"
url: "https://github.com/NikitaDmitrieff/auto-co-meta"
source_code_url: "https://github.com/NikitaDmitrieff/auto-co-meta"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2026-03-06"
current_release: "2026-06-14"
stars: "41"
language: "Bash"
homepage: "https://runautoco.com"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Anthropic"
pricing: "~$1.80/cycle (Opus) or ~$0.50/cycle (Sonnet); infra ~$5-7/mo optional"
install_method: "npx create-auto-co my-company then cd my-company then make start (or git clone + make start)"
docs_url: "https://runautoco.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/NikitaDmitrieff/auto-co-meta"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Run an autonomous AI company from a ~50 line bash loop that calls Claude Code every 2 minutes. 14 expert-modeled agents (Jeff Bezos as CEO, Werner Vogels as CTO, Charlie Munger as Critic, etc.) debate, decide, build, and deploy software 24/7. No database, server, or framework — just files, git, and a loop. State carried via a 'relay baton' markdown file. Hard safety limits (no deletion, no force push, no spending without human approval)."
---

auto-co runs an autonomous AI company from the terminal using roughly 50 lines of bash plus markdown state files, with Claude Code as the only real dependency. The auto-loop.sh script (about 3,000 lines with monitoring) reads shared state from memories/consensus.md, builds a prompt, calls claude -p, and updates consensus for the next cycle, with 3-5 of 14 expert-persona agents (Bezos, Vogels, Munger, DHH, Seth Godin) participating per cycle. Safety limits bar deletions, database resets, force pushes, credential leaks, and spending without human approval, with Telegram escalations roughly every 20-30 cycles. State lives in markdown files and JSONL logs rather than a database, and templates cover SaaS, docs-site, and API-backend projects. It is MIT-licensed, free software whose operating cost is Claude API usage, and suits tinkerers running always-on product experiments.
