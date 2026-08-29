---
name: "ralph"
slug: "ralph"
layout: "agent.njk"
category: "multiplexer"
maker: "snarktank"
license: "MIT"
url: "https://github.com/snarktank/ralph"
source_code_url: "https://github.com/snarktank/ralph"
source_available: "Yes"
platforms:
  - "Autonomous"
first_released: "2026-01-07"
current_release: "2026-02-02"
stars: "21543"
language: "Bash"
homepage: "https://x.com/ryancarson/status/2008548371712135632"
mcp_support: "no"
plugin_support: "yes (.claude-plugin manifest; Claude Code marketplace plugin)"
claude_code_plugin: "yes (/plugin marketplace add snarktank/ralph; /plugin install ralph-skills@ralph-marketplace)"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Amp (ampcode.com), Claude Code (Anthropic)"
pricing: "open-source"
install_method: "git clone (copy files), npm (Claude Code marketplace plugin)"
docs_url: "https://github.com/snarktank/ralph"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/snarktank/ralph"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "An autonomous AI agent loop that repeatedly spawns a fresh, clean-context instance of Amp or Claude Code until every item in a prd.json is passing, carrying memory only through git history, an append-only progress.txt, and prd.json status file -- the 'fresh context + persistent memory' Ralph pattern."
---

Ralph operationalizes a simple claim about AI coding: an agent with fresh context every iteration outperforms one long session that degrades under context rot. The loop reads prd.json, spawns a clean instance of Amp or Claude Code for each iteration, and that instance picks the highest-priority story marked failing, implements it, runs typecheck and tests, and commits only when they pass — then marks the story done and appends what it learned to progress.txt and an evolving AGENTS.md. No state lives in the model's window between iterations; git history and flat files carry all memory, which is why the README insists stories be small enough to fit one context window. A completion phrase or iteration cap ends the run, and typecheck/test gates prevent broken code from compounding across iterations. Teams use it for long unattended pushes through a feature backlog, accepting the project's own warning to run it in isolated environments.
