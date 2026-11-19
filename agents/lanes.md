---
name: "Lanes Desktop"
slug: "lanes"
layout: "agent.njk"
category: "multiplexer"
maker: "lanes-sh"
license: "Proprietary"
url: "https://lanes.sh/desktop"
source_code_url: null
source_available: "False"
homepage: null
docs_url: "https://lanes.sh/docs/desktop"
download_url: "https://lanes.sh/docs/desktop/quick-start"
install_method: "brew install --cask lanes-sh/lanes/lanes && open -a Lanes (macOS Ventura or later, universal binary; the app updates itself on launch)"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: null
first_released: "2026-03-22"
current_release: null
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "True"
subagents: "True"
hooks: null
plan_mode: "True"
plugin_docs_url: null
config_docs_url: null
model_providers: "delegates to the connected agent CLIs (Claude Code and OpenAI Codex run natively; other CLIs run as plain shell sessions); a Gateway research preview points sessions at Ollama, LM Studio, vLLM, OpenRouter, or z.ai via process environment"
pricing: "freemium"
stars: "276"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A native macOS app that puts every agent session on an issue board — each card holds live PTY-backed terminals, its own git worktree, and the diff its agents produced — with per-issue worktree setup and teardown, a built-in MCP server so agents can read the board and drive each other's sessions, and Claude Code plugin marketplace entries for driving the board from inside the agent."
---

Lanes Desktop is the flagship product of lanes.sh, a family of agent tooling from a small company that also ships Lanes Link (an open-source MCP endpoint between agents and your accounts), Lanes Forms, and Lanes Compute. Its pitch is that agents got good at writing code while nothing got good at keeping track of them: five agents across eight terminal tabs, one waiting for input, two quietly doing the same work. The app answers with an issue board where each card is a task holding real PTY-backed terminal sessions — a plan-mode run plus the implementation runs it spawned — its own git worktree with generated branch names, setup/teardown scripts, and auto-cleanup, and the diff those agents produced, so you can review, commit, publish, or open a PR without leaving the window. Claude Code and OpenAI Codex are supported natively: Lanes detects them on PATH, reads their session state from what the CLI writes to disk, and resumes their sessions; anything else runs as a plain shell session. A Gateway research preview points a session at Ollama, LM Studio, vLLM, OpenRouter, or z.ai by setting real process environment, and GitHub and Linear OAuth import whole sprints onto the board and push results back as comments. Lanes also ships a built-in MCP server so the agents themselves can read the board and drive sessions — the docs sell this as 'stop prompting, start looping' — plus Claude Code plugins (a marketplace this repo hosts) and Lanes Link for connecting a hundred-plus apps behind one permission boundary. Local-first: issues, sessions, and settings live in SQLite on your machine, with opt-in remote workspaces for teams. It is built for macOS developers running several agents at once who want the board, not the terminal tabs, to be the source of truth.
