---
name: "codex-multi-agents"
slug: "codex-multi-agents"
layout: "agent.njk"
category: "multiplexer"
maker: "violetDelia"
license: null
url: "https://github.com/violetDelia/codex-multi-agents"
source_code_url: "https://github.com/violetDelia/codex-multi-agents"
source_available: "True"
platforms: []
first_released: "2026-03-18"
current_release: "2026-03-27"
stars: "36"
language: "Shell, Bash"
homepage: null
mcp_support: null
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Clone repo; use bash scripts under skills/codex-multi-agents/scripts/. No formal install steps provided."
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/violetDelia/codex-multi-agents"
maintained: "dormant"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent task management and coordination using pure shell scripts and tmux sessions; manages agent rosters, task lifecycle (new -> dispatch -> pause -> continue -> done), inter-agent communication via tmux, and a kanban-style task board; worktree-based isolation per task. Only 2 commits, 36 stars - early/abandoned stage."
---

Codex-multi-agents coordinates several Codex sessions working on the same repository through shell scripts rather than a dedicated application. A roster script registers named agents with roles and synchronized prompts, a task script manages each task's lifecycle — create, dispatch, pause, resume, complete — with worktree paths, acceptance criteria, and logs recorded in a shared TODO file, and a tmux script relays messages between agent sessions. Each task runs in its own git worktree so parallel agents do not conflict on the working tree. The tool is structured as an agent skill package with scripts under skills/, documentation in Chinese, and a recommended workflow of spec, implementation, review, merge, and sync confirmation; the repository holds only two commits and no license file, indicating an early personal project.
