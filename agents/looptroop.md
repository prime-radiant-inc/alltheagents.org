---
name: "LoopTroop"
slug: "looptroop"
layout: "agent.njk"
category: "multiplexer"
maker: "looptroop-ai"
license: "MIT"
url: "https://github.com/looptroop-ai/LoopTroop"
source_code_url: "https://github.com/looptroop-ai/LoopTroop"
source_available: "True"
platforms: []
first_released: "2026-03-03"
current_release: "2026-08-18"
stars: "122"
language: "TypeScript"
homepage: "https://www.looptroop.ovh/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, NVIDIA NIM (via OpenCode)"
pricing: "Free (MIT)"
install_method: "curl -fsSL https://www.looptroop.ovh/install | sh; or npm install -g looptroop; or brew install looptroop-ai/tap/looptroop; or docker pull looptroopai/looptroop:latest; requires Node 24.15.0+, git, gh, OpenCode"
docs_url: "https://www.looptroop.ovh/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.looptroop.ovh/install"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local GUI orchestrator for long-running, high-correctness AI software delivery; turns a coding ticket into a planned, reviewable, agent-executed PR through three stages (Planning with LLM Council interview/PRD/bead generation, Execution with isolated OpenCode worktrees and multi-loop automated testing, Shipping with final verification); cross-model councils with independent voting"
---

LoopTroop is built for tickets too large for chat-style coding: an interactive interview (allowed to run over an hour) produces a PRD, which decomposes into beads - the smallest independently implementable units, each with acceptance criteria, target files, and validation steps. OpenCode implements each bead in an isolated git worktree, and because worktrees isolate code but not command execution, the project recommends running inside a disposable VM. State lives outside the model in SQLite, JSONL logs, and YAML artifacts, with the agent receiving only the context its current step needs to prevent context rot; runs are expected to take ten or more hours, unattended. Teams with long-horizon, correctness-sensitive feature work who already run OpenCode are the intended users.
