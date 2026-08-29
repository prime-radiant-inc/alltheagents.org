---
name: "claude-swarm"
slug: "claude-swarm"
layout: "agent.njk"
category: "agent"
maker: "affaan-m"
license: "MIT"
url: "https://github.com/affaan-m/claude-swarm"
source_code_url: "https://github.com/affaan-m/claude-swarm"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-11"
current_release: "2026-02-11"
stars: "322"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic (Opus 4.6 for planning/quality review, Haiku for worker execution)"
pricing: "Free/open-source (MIT); usage costs via Anthropic API key with budget enforcement (default $5.00)"
install_method: "pip install claude-swarm; set ANTHROPIC_API_KEY"
docs_url: "https://github.com/affaan-m/claude-swarm#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/claude-swarm/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Multi-agent orchestration for Claude Code: Opus 4.6 decomposes tasks into a dependency graph of subtasks, Haiku worker agents execute in parallel with pessimistic file locking, then Opus runs a quality gate review. htop-style TUI dashboard, hard budget enforcement, JSONL session replay, and declarative YAML agent topologies."
---

Claude Swarm demonstrates a cost-tiered orchestration pattern: expensive reasoning is confined to planning and integration review while cheap, well-specified execution runs on Haiku in parallel. Dependency-ordered waves via topological sorting, file locking to avoid write collisions, and a hard dollar budget with per-agent accounting make parallel agent runs economically controllable. A quality gate scores the combined output and can reject it, and sessions record to JSONL for replay. Built for the February 2026 Cerebral Valley x Anthropic hackathon, it has seen little development since, but the pattern it demonstrates influenced later planner-worker-review harness designs.
