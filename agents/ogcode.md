---
name: "ogcode"
slug: "ogcode"
layout: "agent.njk"
category: "agent"
maker: "prasenjeet-symon"
license: "MIT"
url: "https://github.com/prasenjeet-symon/ogcode"
source_code_url: "https://github.com/prasenjeet-symon/ogcode"
source_available: "True"
platforms: []
first_released: "2026-05-01"
current_release: "2026-08-19"
stars: "136"
language: "Go"
homepage: "https://ogcode.xyz"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, OpenRouter, Ollama"
pricing: "BYOK (Bring Your Own Key) - you only pay for your own token usage. No subscriptions."
install_method: "curl -fsSL http://ogcode.xyz/install.sh | sh (macOS/Linux), Homebrew, go install, Docker, or winget/PowerShell script (Windows)"
docs_url: "https://github.com/prasenjeet-symon/ogcode/blob/main/docs/OUTLINE.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/prasenjeet-symon/ogcode/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Token-efficient context engineering that saves 70%+ tokens on long sessions by using a persistent knowledge graph (Agentic Session Memory) to recall relevant context rather than replaying the full transcript. This enables effectively infinite context windows and allows lower-end models to match frontier models. Also features git-native parallel task execution via worktrees that automatically raise conflict-free PRs. Plan Mode features a visual Kanban board, effort estimates, dependency graphs."
---

ogcode is a single-Go-binary agentic workbench with an embedded web UI, built around the observation that replaying the full transcript every turn wastes tokens and degrades accuracy. Instead, it curates per-turn context from a knowledge graph with vector embeddings, tree-sitter file maps, and compact tool outputs. Plan mode decomposes a described goal into a task DAG rendered on a kanban board, with each task running in its own git worktree and independent tasks executing in parallel before auto-opening conflict-free PRs through the gh CLI. Permission-gated write and shell operations keep the loop safe, and a deep-research agent drives headless Chrome. Model access is BYOK across Anthropic, OpenAI, OpenRouter, and Ollama, switchable from the browser UI.
