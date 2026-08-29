---
name: "CORAL"
slug: "coral"
layout: "agent.njk"
category: "other"
maker: "Human-Agent-Society"
license: "Apache-2.0"
url: "https://github.com/Human-Agent-Society/CORAL"
source_code_url: "https://github.com/Human-Agent-Society/CORAL"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-03-16"
current_release: "2026-08-15"
stars: "900"
language: "Python"
homepage: "https://coral.compounding-intelligence.ai"
mcp_support: "no — explicitly described as a skills-first bundle (no MCP)"
plugin_support: "yes — plugin system installable in Claude Code and Codex; marketplace Human-Agent-Society/CORAL"
claude_code_plugin: "yes"
subagents: "yes — coral-task-author (autonomously scaffolds tasks) and coral-run-doctor (triages stuck runs)"
hooks: "no"
plan_mode: "no"
model_providers: "LiteLLM gateway (custom models); supported agents: Claude Code, Codex, Cursor, Kiro, OpenCode"
pricing: "open-source"
install_method: "pip"
docs_url: "https://coral.compounding-intelligence.ai/docs/"
plugin_docs_url: "https://coral.compounding-intelligence.ai/docs/guides/plugin"
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Infrastructure for autonomous AI agent organizations running experiments, sharing knowledge, and continuously improving solutions; multi-agent self-evolution in parallel git worktrees with shared .coral/public/ state; grader daemon scores every commit; accepted at COLM 2026."
---

Running one coding agent against a benchmark is straightforward; running populations of agents that build on each other's results without contaminating evaluation is not, and CORAL supplies that substrate. Each agent works in an isolated git worktree, shared state (attempts, notes, skills) lives in a .coral/public/ directory symlinked into every worktree so agents see each other's progress in real time, and a grader daemon scores each commit so progress is measured rather than claimed. A manager agent injects heartbeat prompts - reflect, consolidate, pivot - to steer long runs, and multi-island runs with migration support evolution-style experiments across isolated agent populations. Docker isolation keeps agents from reading grader answer keys, and rubric-based LLM judges score open-ended tasks. Research groups studying self-improving agent systems use it; the project ships as a pip/uv install with a Claude Code plugin for authoring tasks.
