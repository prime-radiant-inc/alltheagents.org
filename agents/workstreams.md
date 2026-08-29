---
name: "workstreams"
slug: "workstreams"
layout: "agent.njk"
category: "multiplexer"
maker: "workstream-labs"
license: "Elastic License 2.0"
url: "https://github.com/workstream-labs/workstreams"
source_code_url: "https://github.com/workstream-labs/workstreams"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-03-07"
current_release: "2026-04-22"
stars: "76"
language: "TypeScript"
homepage: "https://github.com/workstream-labs/workstreams"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude (Anthropic), Codex (OpenAI), Aider"
pricing: "open-source"
install_method: "macOS DMG installer (desktop app); CLI: git clone && bun install && bun link"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "IDE for orchestrating parallel AI coding agents in isolated git worktrees. Features a worktree sidebar with live diff stats, inline review comments on diffs, create workstreams with agent selection, and agent session state tracking. Agent-agnostic, works with Claude, Codex, Aider, and more. Built with Node.js 22, Electron, and Bun."
---

workstreams is a macOS desktop IDE for running multiple AI coding agents in parallel, each isolated in its own git worktree so parallel tasks cannot interfere. The worktree sidebar tracks live diff stats and agent session state, and reviewers leave inline comments on split diffs that are sent back to agents as structured prompts, creating a review-feedback loop with Claude Code, Codex, Aider, and other agent CLIs. A companion ws CLI (built on Bun) handles init, create, run, and dashboard operations, while the Electron desktop app provides the sidebar, diff stats, and review surface. It is free to download (DMG for Apple Silicon and Intel) under the Elastic License 2.0, macOS-only and early-stage. Its users are developers running several agents on separate tasks concurrently.
