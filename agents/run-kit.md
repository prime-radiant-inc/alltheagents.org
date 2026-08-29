---
name: "run-kit"
slug: "run-kit"
layout: "agent.njk"
category: "multiplexer"
maker: "sahil87"
license: "MIT"
url: "https://github.com/sahil87/run-kit"
source_code_url: "https://github.com/sahil87/run-kit"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-03-02"
current_release: "2026-08-19"
stars: "56"
language: "TypeScript"
homepage: "https://shll.ai/run-kit"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "False"
model_providers: "Agent-agnostic (Claude Code, Codex, Gemini)"
pricing: "Free/open source"
install_method: "curl -fsSL https://shll.ai/install | sh (Homebrew); desktop app via run-kit desktop install"
docs_url: "https://shll.ai/run-kit"
plugin_docs_url: null
config_docs_url: null
download_url: "https://shll.ai/install"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Agent-agnostic remote tmux console with no database, state derived from tmux + filesystem; phone-first, keyboard-first; spawns parallel agent worktrees via git worktrees; outlives agent tooling churn."
---

The tool exists for the failure mode where an agent is running on a desk machine and the developer is elsewhere — it exposes every tmux session and pane as a live terminal in a phone-first PWA or a macOS desktop app, over Tailscale HTTPS if desired. It deliberately understands nothing about agents: a pane is a pane, and Claude Code, Codex, builds, and htop are equal citizens, which insulates it from changes in agent tooling. Optional Claude Code hooks feed lifecycle states into status dots (busy, waiting, idle), and riff provisions worktree-plus-tmux workspaces in bulk for parallel runs. It is part of the shll toolkit alongside wt for worktrees, installs in one curl line requiring tmux 3.4+, and targets developers supervising long-running agent sessions from a phone or a second screen.
