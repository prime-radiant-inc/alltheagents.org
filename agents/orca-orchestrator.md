---
name: "Orca"
slug: "orca-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "junkyard22"
license: "PolyForm Noncommercial 1.0.0"
url: "https://github.com/junkyard22/Orca"
source_code_url: "https://github.com/junkyard22/Orca"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-02-27"
current_release: "2026-08-19"
stars: "39"
language: "TypeScript"
homepage: "https://github.com/junkyard22/Orca"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "OpenRouter, Ollama"
pricing: "free"
install_method: "git clone, pnpm install, run apps/desktop (Electron) or apps/runner (CLI)"
docs_url: "https://github.com/junkyard22/Orca"
plugin_docs_url: null
config_docs_url: "https://github.com/junkyard22/Orca"
download_url: "https://github.com/junkyard22/Orca"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Multi-Role AI Agent Runtime orchestrating multiple AI roles through a quality-gated pipeline (Brain -> Miranda -> Pappy -> Benson). Maestro manages a subagent pool (brain, strong_model, cheap_model, reviewer, narrator, planner_deep, debugger, reader, vision). MCP support, SQLite persistence, role routing between cheap and strong models, self-improving distillation loop, and training-data export for fine-tuning — all running locally."
---

Single-model coding pipelines blur responsibility: the same context plans, codes, reviews, and talks to the user, so quality control becomes an afterthought. Orca assigns each function a named role in a fixed pipeline — Brain decomposes the request, Miranda runs a PLAN-ANSWER-CRITIQUE-REWRITE compliance loop, Pappy issues PASS/WARN/FAIL quality verdicts, and Benson handles intent parsing — with a Maestro router managing a nine-role subagent pool that includes strong and cheap model tiers, debugger, reviewer, and vision roles. Runs persist in SQLite, MCP connects external tools, and a distillation loop exports interactions as training data for fine-tuning. The runtime is a TypeScript pnpm monorepo with an Electron desktop app and a CLI runner keyed to OpenRouter or local Ollama, under a PolyForm Noncommercial license and aimed primarily at Windows. It is an early personal project (39 stars, 442 commits) exploring role-decomposed agent architectures.
