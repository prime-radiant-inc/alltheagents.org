---
name: "ralph"
slug: "ralph"
layout: "agent.njk"
category: "agent"
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
mcp_support: null
plugin_support: "yes (.claude-plugin manifest; Claude Code marketplace plugin)"
claude_code_plugin: "yes (/plugin marketplace add snarktank/ralph; /plugin install ralph-skills@ralph-marketplace)"
subagents: null
hooks: null
plan_mode: null
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

An autonomous AI agent loop that repeatedly spawns a fresh, clean-context instance of Amp or Claude Code until every item in a prd.json is passing, carrying memory only through git history, an append-only progress.txt, and prd.json status file -- the 'fresh context + persistent memory' Ralph pattern.
