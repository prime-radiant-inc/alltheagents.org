---
name: "Jouzu"
slug: "jouzu"
layout: "agent.njk"
category: "agent"
maker: "shisa-ai"
license: "Apache-2.0"
url: "https://www.npmjs.com/package/jouzu"
source_code_url: "https://github.com/shisa-ai/jouzu"
source_available: "True"
homepage: null
docs_url: "https://github.com/shisa-ai/jouzu#readme"
download_url: null
install_method: "npm install -g jouzu"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "JavaScript"
first_released: "2026-08-03"
current_release: "2026-09-16"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Shisa AI, OpenAI, Anthropic, Google"
pricing: "free"
stars: "1"
sources:
  - "github-issue"
last_verified: "2026-09-16"
what_makes_it_special: "A terminal coding agent built on the Pi harness that bundles goals, background jobs, and child agents in one session — plus Japanese-aware terminal layout, voice dictation via Shisa, and local TextGuard scanning of skills and web results."
---

Jouzu ships the Pi coding agent as its engine and adds the session layer that long tasks need. Goals, measured improvement loops, and scheduled prompts track multi-step work, bg_task runs shell jobs without blocking the prompt and surfaces batched completion summaries, and /workflow lets you assign models, tools, and instructions to child agents and inspect, follow up, or resume their runs. The harness keeps Pi's editor, TUI library, and model catalog behavior intact, adding a Prompt Frame and Status Bar tuned for CJK and emoji widths, searchable session history after compaction, an optional Japanese profile, and TextGuard that labels untrusted web results and holds flagged skills for approval. It installs from npm as jouzu/jz, reads model catalogs from Shisa AI or any configured gateway with local Pi providers as fallback, and is aimed at developers who want Pi's inspectable runtime with built-in task, job, and subagent management in a single terminal session.
