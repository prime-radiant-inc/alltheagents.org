---
name: "agentic-coding-tool-eval"
slug: "agentic-coding-tool-eval"
layout: "agent.njk"
category: "other"
maker: "disler"
license: "No license file is declared in the repository"
url: "https://github.com/disler/agentic-coding-tool-eval"
source_code_url: "https://github.com/disler/agentic-coding-tool-eval"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-06-29"
current_release: "2025-06-29"
stars: "41"
language: "Vue"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "git clone; use custom slash command /trees in Claude Code (or manual git worktrees)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/disler/agentic-coding-tool-eval"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Hands-on micro apps to compare and evaluate agentic coding tools (Claude Code, Gemini CLI, Codex CLI) in a standardized way. Uses a custom /trees slash command to spin up parallel git worktrees."
---

Choosing between Claude Code, Gemini CLI, and Codex CLI is usually based on demos and marketing, so this repository provides a controlled hands-on alternative: one small UI-component challenge that every candidate tool attempts under the same prompts. Each tool runs in an isolated git worktree so the attempts never interfere, and the /trees slash command creates those worktrees in one step. The tools are deliberately run in permissionless mode (claude --dangerously-skip-permissions, gemini --yolo, codex --dangerously-auto-approve-everything) so permission friction does not skew the comparison. It is aimed at developers who want to judge tool quality on a realistic task they can inspect themselves rather than on published benchmark numbers.
