---
name: "kkirikkiri"
slug: "kkirikkiri"
layout: "agent.njk"
category: "multiplexer"
maker: "fivetaku"
license: "MIT"
url: "https://github.com/fivetaku/kkirikkiri"
source_code_url: "https://github.com/fivetaku/kkirikkiri"
source_available: "True"
platforms: []
first_released: "2026-02-28"
current_release: "2026-07-06"
stars: "51"
language: "JavaScript"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Anthropic Claude, OpenAI Codex CLI, Antigravity CLI"
pricing: "Free / open-source (cost is your Claude API usage; varies by team size)"
install_method: "/plugin marketplace add https://github.com/fivetaku/gptaku_plugins.git && /plugin install kkirikkiri; enable Agent Teams flag in ~/.claude/settings.json"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "github_final"
what_makes_it_special: "Natural language team builder plugin for Claude Code Agent Teams - describe what you want in one sentence and it assembles a purpose-driven AI team with validation loops (up to 3 rounds) and shared memory for cross-session persistence."
---

Assembling a useful set of Claude Code subagents by hand is slow and error-prone, so kkirikkiri automates team construction: the user describes the goal in one sentence, the plugin interviews briefly, proposes members with strictly scoped roles, and delegates execution to a team leader that plans and validates but never writes code directly. Well-performing members can be saved back to .claude/agents/ for reuse, and shared state (plans, progress) persists in .kkirikkiri/teams/ across sessions. Validation loops of up to three rounds swap underperforming members or rebuild the team. It targets Claude Code users with the experimental Agent Teams flag enabled who want repeatable multi-agent setups without hand-editing agent definitions.
