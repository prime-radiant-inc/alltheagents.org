---
name: "auto-company"
slug: "auto-company"
layout: "agent.njk"
category: "agent"
maker: "nicepkg"
license: "MIT"
url: "https://github.com/nicepkg/auto-company"
source_code_url: "https://github.com/nicepkg/auto-company"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-02-11"
current_release: "2026-02-12"
stars: "185"
language: "Shell"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "no"
model_providers: "Anthropic (Claude Code CLI required; Opus default, Sonnet via env var)"
pricing: "Free software (MIT); requires Claude API/subscription credits (Pro/Max recommended)"
install_method: "git clone then make start (foreground) or make install (launchd daemon). Requires macOS + Claude Code CLI."
docs_url: "https://github.com/nicepkg/auto-company#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/nicepkg/auto-company"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Fully autonomous AI company that runs 24/7 using 14 AI agents modeled after real-world legendary experts (Bezos, Munger, DHH, etc.) powered by Claude Code Agent Teams. Features 24/7 launchd daemon loop with crash auto-restart, consensus memory via consensus.md, auto-convergence cycles with GO/NO-GO decisions, 6 standard workflows, and hardcoded safety red lines. macOS-only, experimental."
---

auto-company is an experimental project that runs a simulated software company around the clock using 14 AI agents modeled on real-world figures (Bezos, Munger, DHH, Werner Vogels) and powered by Claude Code Agent Teams. A launchd-managed bash loop invokes Claude Code every cycle; agents read a shared consensus file plus company charter, pick 3-5 agents per cycle, and update shared state before the next cycle, with convergence rules to prevent endless discussion. State lives in markdown files, with six standard workflows (new product eval, feature dev, release, pricing, weekly review, opportunity discovery) and safety red lines baked into CLAUDE.md. It is an early experimental project (about a dozen commits), macOS-only via launchd, MIT-licensed, and requires a Claude Code subscription to run.
