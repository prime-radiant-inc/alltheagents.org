---
name: "ntm"
slug: "ntm"
layout: "agent.njk"
category: "multiplexer"
maker: "Dicklesworthstone"
license: "MIT (with additional rider in LICENSE file)"
url: "https://github.com/Dicklesworthstone/ntm"
source_code_url: "https://github.com/Dicklesworthstone/ntm"
source_available: "True"
platforms: []
first_released: "2025-12-10"
current_release: "2026-08-20"
stars: "429"
language: "Go"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, Antigravity CLI (AGY), Grok Build (xAI), Gemini CLI"
pricing: "Free / open-source"
install_method: "Install script (curl ... | bash -s -- --easy-mode), Homebrew (brew install dicklesworthstone/tap/ntm), Docker (docker pull ghcr.io/dicklesworthstone/ntm), or from source (go install ./cmd/ntm)"
docs_url: "https://github.com/Dicklesworthstone/ntm"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Dicklesworthstone/ntm"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Turns tmux into a local control plane for multi-agent software development; graph-aware work triage, Agent Mail coordination, file reservations, worktrees, safety policy with two-person approval workflows, durable checkpoints/timelines/audit trails, robot-mode CLI surfaces, and REST/SSE/WebSocket/OpenAPI APIs in one Go binary"
---

ntm turns a local tmux setup into a control plane for running many coding agents across a codebase, launching labeled panes for Claude Code, Codex, Antigravity, Grok Build, and Gemini CLI. Work is assigned through graph-aware triage backed by the Beads issue system, with dependency-aware auto-assignment rather than broadcast prompting. Coordination primitives include Agent Mail messaging, file reservations to prevent conflicting edits, and git worktree isolation per agent. Safety is structural: policy rules gate destructive commands, with approval workflows and audit logs, and durable state supports checkpointing and pipeline resume. Automation surfaces include robot-mode CLI flags and a local REST/WebSocket API, and the project is maintained largely by the author's own agents.
