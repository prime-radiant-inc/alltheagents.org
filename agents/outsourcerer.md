---
name: "outsourcerer"
slug: "outsourcerer"
layout: "agent.njk"
category: "multiplexer"
maker: "alexgreensh"
license: "PolyForm Noncommercial 1.0.0"
url: "https://github.com/alexgreensh/outsourcerer"
source_code_url: "https://github.com/alexgreensh/outsourcerer"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-10"
current_release: "2026-08-19"
stars: "135"
language: "Bash"
homepage: "https://github.com/alexgreensh/outsourcerer"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "OpenRouter, Claude, Codex, Gemini, Hermes, Ollama, LM Studio"
pricing: "Free (PolyForm Noncommercial license; commercial use requires separate license)"
install_method: "Claude Code: /plugin marketplace add alexgreensh/outsourcerer then /plugin install outsourcerer@outsourcerer; Antigravity: agy plugin import claude-code; Codex: outsourcerer parity-codex; Devin: outsourcerer parity; Hermes: outsourcerer parity-hermes"
docs_url: "https://github.com/alexgreensh/outsourcerer#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/alexgreensh/outsourcerer#readme"
download_url: "https://github.com/alexgreensh/outsourcerer/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Delegates work from your main AI coding session to cheaper models; advisor panels with consensus gating; tracks real savings with 'The Tab'; fanout parallel agents across any backend; runs on local models for $0"
---

Coding sessions burn frontier-model tokens on mechanical work — repo mapping, bulk refactors, test loops, wide searches — that cheaper engines handle fine. Outsourcerer, a single self-contained Bash script installed as a Claude Code plugin (with parity installers for Antigravity, Codex, Devin, Hermes, Cursor, and Droid), delegates those tasks to engines the user already pays for while the primary agent keeps orchestration and judgment. Advisor panels of stronger models review results under consensus gating, fanout runs parallel delegates across any backend, and the tool carries the host's skills, plugins, and MCP setup to each delegate so context survives the hop. 'The Tab' tracks real savings in dollars and subscription rate-limit headroom, and a keyless local lane covers zero-cost runs via Ollama or LM Studio. It is one Bash file with no server, proxy, or telemetry, distributed under PolyForm Noncommercial with paid commercial licensing from the author. Cost-conscious Claude Code users running repetitive workloads are the audience.
