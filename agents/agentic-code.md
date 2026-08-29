---
name: "agentic-code"
slug: "agentic-code"
layout: "agent.njk"
category: "other"
maker: "shinpr"
license: "MIT"
url: "https://github.com/shinpr/agentic-code"
source_code_url: "https://github.com/shinpr/agentic-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-09-16"
current_release: "2026-03-30"
stars: "48"
language: "TypeScript / JavaScript (Node.js)"
homepage: "https://github.com/shinpr/agentic-code"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "model-agnostic (works with any LLM via AGENTS.md-compatible tools: Cursor, Codex CLI, Gemini CLI)"
pricing: "Free / Open Source (MIT)"
install_method: "npx agentic-code my-project"
docs_url: "https://github.com/shinpr/agentic-code"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/shinpr/agentic-code"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Standardizes AI coding workflows via the open AGENTS.md standard with zero configuration, enforcing a test-first approach and progressive skill loading across multiple AI coding tools (Cursor, Codex, Gemini CLI). Provides pre-built workflows and quality gates (requirements analysis, architecture planning, test-first generation, implementation). Supports sub-agents-mcp for running isolated context reviews in Cursor."
---

Teams using several AI coding tools end up maintaining separate instruction files and workflows per tool, so agentic-code standardizes on the open AGENTS.md format and generates the scaffolding in one npx command with zero configuration. Its workflows impose a test-first discipline with quality gates between phases — requirements analysis, architecture planning, test-first generation, implementation — and skills install into Cursor or Codex CLI from the shared .agents/skills directory. For deeper review isolation it supports sub-agents-mcp, running reviews in a separate context window. It is MIT-licensed, model-agnostic, and built for teams that run Cursor, Codex, and Gemini CLI against the same repository without wanting per-tool workflow drift.
