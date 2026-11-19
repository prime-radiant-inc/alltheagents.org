---
name: "Agav"
slug: "agav"
layout: "agent.njk"
category: "agent"
maker: "prapaa-ai"
license: "Apache-2.0"
url: "https://github.com/prapaa-ai/agav"
source_code_url: "https://github.com/prapaa-ai/agav"
source_available: "True"
homepage: "https://agav.dev"
docs_url: "https://docs.agav.dev"
download_url: "https://github.com/prapaa-ai/agav/releases"
install_method: "curl -fsSL https://agav.dev/install.sh | bash (self-contained binary, no Node.js); Windows: irm https://www.agav.dev/install.ps1 | iex; binaries from GitHub releases"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
  - "one-shot-generative"
specialization: "general"
language: "TypeScript"
first_released: "2026-07-31"
current_release: "2026-11-12"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: "https://docs.agav.dev/features/plugins-and-subagents"
config_docs_url: "https://docs.agav.dev/reference/configuration"
model_providers: "Anthropic, OpenAI, OpenRouter, NVIDIA NIM, Google Gemini, Vertex AI, Ollama (switch mid-session with /model)"
pricing: "free"
stars: "189"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A terminal coding agent built around harness efficiency — cached context, bounded retries and budgets, interrupted repair loops, and isolated subagent exploration — publishing its cost methodology alongside its benchmarks, with per-action tool permissions, sandboxed commands on macOS and Linux, and skills, plugins and an agent marketplace on top."
---

Agav is an open-source terminal agent for work in real repositories, and its distinguishing bet is that coding cost is a harness problem: it reuses cached context, limits repeated work, interrupts unproductive repair loops, bounds retries and token budgets, and keeps subagent exploration in fresh contexts so the same repository context is not resent over and over. The authors publish the evidence with the engineering — a Terminal-Bench 2.1 cost study reporting 15.2¢ median trial cost and 49.1% lower total spend than Codex at matched rates, alongside the accuracy numbers and their limitations, and a #1-verified spot on the SWE-bench-Live Lite leaderboard at the time of the README — which sets it apart from harnesses that quote only accuracy. Day to day it behaves like a modern coding CLI: inspect code, make focused edits, run tests, verify changes, with LSP queries, notebook support, /undo, and a planning UI whose plans survive restarts; sessions resume, branch, and compact without losing the plan; /permission switches ask/auto-accept/deny-writes mid-session; and non-interactive agav run takes a one-shot prompt for scripts and CI with per-tool permissions and optional JSON Schema output. Local plugins are plain JavaScript tools in ~/.agav/plugins, subagents take scoped work on the same or a different model, skills bundle instructions, a marketplace offers installable service agents, and background jobs with cron schedules outlive a single turn. API keys are encrypted at rest, local-first operation works with Ollama, and commands can run in a sandbox on macOS and Linux. It is explicitly an experimental beta — breaking changes expected — under Apache-2.0, suited to developers who pay their own model bills and want the harness spending them carefully.
