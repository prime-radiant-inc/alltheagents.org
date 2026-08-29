---
name: "claude_code_sub_agents"
slug: "claude-code-sub-agents"
layout: "agent.njk"
category: "agent"
maker: "yzyydev"
license: null
url: "https://github.com/yzyydev/claude_code_sub_agents"
source_code_url: "https://github.com/yzyydev/claude_code_sub_agents"
source_available: "True"
platforms: []
first_released: "2025-06-16"
current_release: "2025-06-16"
stars: "43"
language: "Markdown"
homepage: "https://github.com/yzyydev/claude_code_sub_agents"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (via Claude Code subagents)"
pricing: "free"
install_method: "git clone; use via Claude Code custom commands (.claude/commands/)"
docs_url: "https://github.com/yzyydev/claude_code_sub_agents"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/yzyydev/claude_code_sub_agents"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Claude Multi-Agent iterative sub-agent orchestration system using Claude Code custom commands. Wave-based agent deployment, parallel task distribution with concept deduplication, and progressive context summarization to achieve infinite-scale task execution within context constraints."
---

The project demonstrates a pattern for pushing Claude Code past single-context limits: work is divided into waves, each wave spawns fresh sub-agents with clean context windows, and the orchestrator keeps only lightweight state while progressive summarization carries conclusions forward. Each sub-agent receives a unique direction to avoid duplicated output, and the system plans graceful conclusions as capacity is approached. The commands ship as markdown files dropped into .claude/commands/, with no code or runtime beyond Claude Code itself. It is a two-commit proof-of-concept used by prompt-engineering practitioners exploring large parallel generation, not a maintained product.
