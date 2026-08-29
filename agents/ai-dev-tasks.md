---
name: "ai-dev-tasks"
slug: "ai-dev-tasks"
layout: "agent.njk"
category: "other"
maker: "snarktank"
license: "Apache-2.0"
url: "https://github.com/snarktank/ai-dev-tasks"
source_code_url: "https://github.com/snarktank/ai-dev-tasks"
source_available: "True"
platforms: []
first_released: "2025-04-19"
current_release: "2025-11-05"
stars: "7790"
language: "Markdown"
homepage: "https://youtu.be/fD4ktSkNCw4"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Any (tool-agnostic Markdown prompts)"
pricing: "free"
install_method: "git-clone"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Tool-agnostic structured prompt workflow (PRD -> granular task list -> iterative implementation with review checkpoints) that brings discipline to AI-assisted development. Just markdown files usable with any AI coding assistant (Amp, Claude Code, Windsurf, etc.) — no install, framework, or specific tool required."
---

AI coding sessions derail when a whole feature is requested at once: scope drifts, and nothing is verifiable incrementally. ai-dev-tasks replaces that with a fixed sequence — generate a PRD from a feature description, derive a granular task/subtask list from it, then implement one task at a time with the assistant pausing for review after each. The mechanism is deliberately nothing but Markdown: you clone the prompt files into the repo and tag them with @ in whichever assistant you use, so the workflow survives tool changes and can be edited like any other project file. Human checkpoints at each task boundary are the enforcement mechanism, not software. It is widely used across Claude Code, Cursor, Windsurf, and Amp users, with 7.8k stars.
