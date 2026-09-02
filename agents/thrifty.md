---
name: "Thrifty"
slug: "thrifty"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: "MIT"
url: "https://github.com/2389-research/thrifty"
source_code_url: "https://github.com/2389-research/thrifty"
source_available: "True"
platforms:
  - "IDE"
first_released: null
current_release: null
stars: "16"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes (Claude Code plugin)"
claude_code_plugin: "yes"
subagents: "yes (cheap model executes sprints, mid model verifies)"
hooks: "yes (gate tests/checklist)"
plan_mode: "yes (strong model writes CONTRACT.md and sprint briefs)"
model_providers: "Claude (Sonnet plans, Haiku executes, Sonnet verifies)"
pricing: "free"
install_method: "/plugin marketplace add 2389-research/thrifty, then /plugin install thrifty@thrifty"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Tiered-delegation task execution for Claude Code: a strong model (Sonnet) plans by writing a contract and sprint briefs with acceptance criteria, a cheap model (Haiku) executes each sprint and runs the gate (tests/checklist) self-fixing until green, and a mid model (Sonnet) does scoped verification only when the gate fails. Claims ~64% cost reduction vs Opus at equal gate quality."
---

Thrifty is a Claude Code plugin that applies tiered delegation to task execution, and the agent loop belongs to Claude Code throughout. A strong model (Sonnet) plans by writing a CONTRACT.md and per-sprint briefs with explicit acceptance criteria, then hands off. A cheap model (Haiku) executes each sprint and runs the gate — tests and a checklist — self-fixing until the gate goes green. Only when a gate fails does a mid model (Sonnet) step in for scoped verification, so the expensive tiers are used sparingly. The reported payoff is roughly 64% cost reduction versus running Opus end-to-end at equal gate quality. The audience is Claude Code users who want to cut spend without giving up the gate discipline that makes agentic work trustworthy.
