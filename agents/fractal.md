---
name: "fractal"
slug: "fractal"
layout: "agent.njk"
category: "multiplexer"
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
homepage: "https://github.com/plasma-ai/fractal"
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
plugin_docs_url: "https://github.com/plasma-ai/plugins"
config_docs_url: null
download_url: "https://pypi.org/project/plasma-fractal/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Hierarchical agent loops with recursive self-organization — autonomous agent loops arrange into a tree; each node iterates toward a goal in its own git worktree and spawns child nodes for separable subtasks. Fractal tree grows to fit the problem rather than a fixed plan. Each node runs in an isolated git worktree with hard caps (iterations, depth, children, cost, time). All run metadata including cost tracked in local SQLite database viewable live in a terminal UI. Agents run autonomously without permission prompts by default. Installable via Claude Code and Codex plugin marketplaces."
---

Fractal addresses the failure mode of long autonomous runs: a single agent loop loses coherence on large tasks and burns unbounded budget. It decomposes work recursively, running each node as an autonomous session of a backend agent such as Claude Code, Codex, Grok Build, OpenCode, or Oh My Pi, isolated in its own git worktree and capped by configurable iteration, depth, cost, and time limits. Run metadata, including per-node cost, lands in a local SQLite database that the fractal open dashboard renders live. It is installed from PyPI or as a Claude Code and Codex marketplace plugin, and because nodes run with permission prompts disabled by default, it is aimed at operators running it on tasks and hosts they are willing to leave unsupervised.
