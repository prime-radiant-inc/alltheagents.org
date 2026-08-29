---
name: "SWE-AF"
slug: "swe-af"
layout: "agent.njk"
category: "agent"
maker: "Agent-Field"
license: "Apache-2.0"
url: "https://github.com/Agent-Field/SWE-AF"
source_code_url: "https://github.com/Agent-Field/SWE-AF"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-02-04"
current_release: "2026-08-19"
stars: "978"
language: "Python, Go"
homepage: "https://agentfield.ai/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "Anthropic (Claude), OpenRouter, OpenAI, Google, MiniMax, Codex CLI"
pricing: "open-source"
install_method: "pip, docker"
docs_url: "https://agentfield.ai/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Agent-Field/SWE-AF"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Autonomous engineering team runtime where one API call spins up a full team (PM, architect, coders, reviewers, testers) that plans, builds, adapts, and ships production-grade software end-to-end. Factory architecture with three nested adaptive control loops, hardness-aware execution, multi-model per-role assignment, continual learning across issues, agent-scale parallelism via isolated git worktrees, explicit technical-debt tracking, checkpointed resume after crashes, and sub-harness mode for issue-level delegation."
---

SWE-AF exists to turn a single API call into a coordinated engineering organization rather than a single model session. Built on the AgentField control plane, it registers a swe-planner node that decomposes a product requirement into an architecture and an issue DAG, then runs hundreds of role-specialized agent instances — coders, QA, reviewers, merger, verifier — on isolated git worktrees with hardness-aware execution and explicit technical-debt tracking. Execution is organized as three nested adaptive control loops with per-role model assignment (a flat models map assigns Claude, MiniMax, or OpenRouter models per role), a post-PR CI gate loops on failing checks, and builds checkpoint so a crash resumes rather than restarts. A sub-harness endpoint (swe-planner.implement_issue) plus a bundled Claude Code skill let outer harnesses delegate single issues to it. The runtime is free Apache-2.0 software; users pay only the underlying model tokens, and typical full builds cost a few dollars to tens of dollars.
