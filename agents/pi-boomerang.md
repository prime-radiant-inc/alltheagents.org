---
name: "pi-boomerang"
slug: "pi-boomerang"
layout: "agent.njk"
category: "other"
maker: "nicobailon"
license: null
url: "https://github.com/nicobailon/pi-boomerang"
source_code_url: "https://github.com/nicobailon/pi-boomerang"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-03-02"
current_release: "2026-08-03"
stars: "296"
language: "TypeScript"
homepage: "https://github.com/nicobailon/pi-boomerang"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "whatever the host pi session uses (pi is multi-provider)"
pricing: "open-source"
install_method: "pi install npm:pi-boomerang"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/nicobailon/pi-boomerang"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Token-efficient autonomous task execution with automatic context summarization for pi coding agent. Executes tasks autonomously, then replaces raw turn history in future context with an expanded handoff summary (changed files, relevant reads, commands, failures, outcome) — saving tokens while preserving work. Supports chain execution, rethrow/loop execution, prompt templates, anchor mode, and an agent-callable tool."
---

pi-boomerang exists because autonomous agent tasks generate enormous turn histories that crowd out useful context in every later turn. The extension runs a task from start to finish without questions, then a heuristic summarizer condenses the recorded tool calls and results into a handoff block — outcome, changed files, relevant reads, commands, validation results, failures — which replaces the raw history for all subsequent turns while the full session tree remains navigable. Templates with frontmatter configure model, skills, and thinking level per task, chaining turns multi-stage flows into pipelines, and rethrow or loop modes re-run failed tasks with accumulated context. An optional agent-callable tool lets the model boomerang its own subtasks, and file state is never touched, only context. Pi users running long autonomous tasks use it to keep later turns cheap without losing the work record.
