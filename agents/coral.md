---
name: "CORAL"
slug: "coral"
layout: "agent.njk"
category: "agent"
maker: "Human-Agent-Society"
license: "Apache-2.0"
url: "https://github.com/Human-Agent-Society/CORAL"
source_code_url: "https://github.com/Human-Agent-Society/CORAL"
source_available: True
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

Infrastructure for autonomous AI agent organizations running experiments, sharing knowledge, and continuously improving solutions; multi-agent self-evolution in parallel git worktrees with shared .coral/public/ state; grader daemon scores every commit; accepted at COLM 2026.
