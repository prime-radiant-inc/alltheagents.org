---
name: "agent-md"
slug: "agent-md"
layout: "agent.njk"
category: "other"
maker: "iamfakeguru"
license: "MIT"
url: "https://github.com/iamfakeguru/agent-md"
source_code_url: "https://github.com/iamfakeguru/agent-md"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2026-03-31"
current_release: "2026-04-27"
stars: "967"
language: "Shell (Bash)"
homepage: "https://github.com/iamfakeguru/agent-md"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes — extensive hook system for Claude Code, Codex, and Git hooks (destructive command blocking, stop-verify, state-enforcement, visual evidence)"
plan_mode: "no"
model_providers: "agent-agnostic (Claude Code, Codex, Cursor, Windsurf, Aider)"
pricing: "open-source"
install_method: "binary"
docs_url: "https://github.com/iamfakeguru/agent-md#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/iamfakeguru/agent-md"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Portable contracts for coding agents — single source-of-truth rules file, repo-local hooks, persistent task state, and helper scripts so AI agents verify their work rather than guess. Multi-agent portable (Claude Code, Codex, Cursor, Windsurf, Aider)."
---

Rules written in prose get ignored the moment a model rationalizes around them, so agent-md moves everything that can be forgotten into things that cannot: an installer lays down a single AGENT.md source of truth, generates per-tool variants (AGENTS.md, CLAUDE.md), and wires repo-local hooks for Claude Code, Codex, and git pre-commit that block destructive commands and force stop-verify steps. Task state lives in memory files — plan, progress, verify — so commitments survive across sessions instead of being re-derived from chat. Helper scripts add a doctor check and Playwright screenshot capture for visual evidence. Teams running Claude Code, Codex, Cursor, Windsurf, or Aider over the same repo use it to make all of them obey the same contract.
