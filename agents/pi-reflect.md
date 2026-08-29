---
name: "pi-reflect"
slug: "pi-reflect"
layout: "agent.njk"
category: "agent"
maker: "jo-inc"
license: "MIT"
url: "https://github.com/jo-inc/pi-reflect"
source_code_url: "https://github.com/jo-inc/pi-reflect"
source_available: "True"
platforms: []
first_released: "2026-02-13"
current_release: "2026-07-21"
stars: "43"
language: "TypeScript (Node.js)"
homepage: "https://www.npmjs.com/package/@jo-inc/pi-reflect"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "Anthropic"
pricing: "~$0.05-0.15 per run with Sonnet"
install_method: "pi install git:github.com/jo-inc/pi-reflect (also on npm as @jo-inc/pi-reflect)"
docs_url: "https://github.com/jo-inc/pi-reflect/blob/main/SETUP.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@jo-inc/pi-reflect"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Iterative self-improvement for pi coding agents. Define a target behavior/personality and reflect iterates toward it by reading recent conversations and reference material, comparing actual behavior against the target, and making surgical edits to behavioral markdown files (AGENTS.md, MEMORY.md, SOUL.md). Over time corrections get absorbed as rules, memory accumulates durable facts, personality sharpens. Safety: backups, rejecting suspicious deletions, git auto-commit. Impact metrics: correction rate trend, rule recidivism. Invoked via pi slash commands (/reflect, /reflect-config, /reflect-history, /reflect-stats, /reflect-backfill)."
---

pi-reflect exists because behavioral rules for coding agents decay: instructions get ignored, the same mistakes recur, and nobody revisits the behavioral files that were supposed to prevent them. The extension runs a reflection cycle against a target file — collecting recent transcripts and reference material, sending them to a Sonnet-class model, and applying surgical edits that close the gap between observed and intended behavior — with backups, rejection of suspicious deletions, and git auto-commit making every change reversible. Metrics track whether the process works: correction-rate trends show whether the agent improves, and a rule-recidivism flag surfaces rules that keep being edited without effect. Runs can be scheduled via cron or launchd in headless mode, turning reflection into unattended maintenance. Developers running pi on long-lived projects use it to keep behavioral files honest instead of accreting stale instructions.
