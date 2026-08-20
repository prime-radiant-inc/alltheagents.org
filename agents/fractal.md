---
name: "fractal"
slug: "fractal"
layout: "agent.njk"
category: "agent"
maker: "plasma-ai"
license: "Apache-2.0"
url: "https://github.com/plasma-ai/fractal"
source_code_url: "https://github.com/plasma-ai/fractal"
source_available: "yes"
platforms:
  - "CLI"
first_released: "2026-07-01"
current_release: "2026-08-18"
stars: "693"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, Grok Build, OpenCode, Oh My Pi (omp), OpenRouter"
pricing: "open-source"
install_method: "pip"
docs_url: "https://docs.plasma.ai/fractal"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/plasma-fractal/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Hierarchical agent loops with recursive self-organization — autonomous agent loops arrange into a tree; each node iterates toward a goal in its own git worktree and spawns child nodes for separable subtasks. Fractal tree grows to fit the problem rather than a fixed plan. Each node runs in an isolated git worktree with hard caps (iterations, depth, children, cost, time). All run metadata including cost tracked in local SQLite database viewable live in a terminal UI. Agents run autonomously without permission prompts by default. Installable via Claude Code and Codex plugin marketplaces."
---

Hierarchical agent loops with recursive self-organization — autonomous agent loops arrange into a tree; each node iterates toward a goal in its own git worktree and spawns child nodes for separable subtasks. Fractal tree grows to fit the problem rather than a fixed plan. Each node runs in an isolated git worktree with hard caps (iterations, depth, children, cost, time). All run metadata including cost tracked in local SQLite database viewable live in a terminal UI. Agents run autonomously without permission prompts by default. Installable via Claude Code and Codex plugin marketplaces.
