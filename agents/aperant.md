---
name: "Aperant"
slug: "aperant"
layout: "agent.njk"
category: "multiplexer"
maker: "AndyMik90"
license: "AGPL-3.0"
url: "https://github.com/AndyMik90/Aperant"
source_code_url: "https://github.com/AndyMik90/Aperant"
source_available: "Yes"
platforms:
  - "Autonomous"
first_released: "2025-12-04"
current_release: "2026-06-14"
stars: "14536"
language: "TypeScript (Electron desktop app)"
homepage: "https://aperant.com"
mcp_support: null
plugin_support: null
claude_code_plugin: "yes (requires Claude Code CLI)"
subagents: "yes (up to 12 parallel agent terminals)"
hooks: null
plan_mode: "yes (agents autonomously plan, implement, and validate tasks)"
model_providers: "Anthropic/Claude (requires Claude Pro/Max subscription)"
pricing: "open-source (AGPL-3.0); requires paid Claude subscription"
install_method: "binary"
docs_url: "https://github.com/AndyMik90/Aperant/tree/develop/guides"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/AndyMik90/Aperant/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Autonomous multi-agent coding framework that plans, builds, and validates software using Claude Code. It runs up to 12 parallel agents in isolated git worktrees with self-validating QA loops, AI-powered merge conflict resolution, and a Kanban board for visual task management."
---

Aperant (formerly Auto Claude) addresses the throughput ceiling of single-agent coding: it decomposes a goal into tasks, runs them concurrently in isolated worktrees, validates each with automated QA, and merges results with AI-assisted conflict resolution, holding session memory across runs and integrating GitHub, GitLab, and Linear. It drives the Claude Code CLI rather than bundling its own model access, so users need a Claude Pro/Max subscription. The AGPL-3.0 desktop app is free with prebuilt binaries for all three platforms; version 3.0 is a ground-up rebuild in a separate repo with cloud features, placing 2.x in maintenance mode with code PRs paused. Around 14.5k stars and an active Discord community, with docs in the repo guides/ and at aperant.com.
