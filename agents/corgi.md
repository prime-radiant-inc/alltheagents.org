---
name: "Corgi"
slug: "corgi"
layout: "agent.njk"
category: "multiplexer"
maker: "tals"
license: "MIT"
url: "https://github.com/tals/corgi"
source_code_url: "https://github.com/tals/corgi"
source_available: "True"
homepage: "https://corgi.computer"
docs_url: "https://github.com/tals/corgi/blob/main/docs/reference.md"
download_url: null
install_method: "curl -fsSL https://corgi.computer/install.sh | bash (macOS Apple Silicon; Linux amd64/arm64)"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "TypeScript"
first_released: "2026-09-20"
current_release: "2026-11-18"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Claude Code, Codex, Pi, OpenCode, and Oh My Pi run in its panes with their own accounts and providers; Corgi auto-detects them and surfaces status, tokens, and rate limits"
pricing: "free"
stars: "209"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A Ghostty-powered terminal multiplexer built agent-first: it detects Claude Code, Codex, Pi, OpenCode, and Oh My Pi in any pane, installs their hooks (or a Pi extension) to track status, activity summaries, subagents, tokens, and rate limits, and adds worktree-linked agents, session fork/resume, a Reviewer agent for diffs, headless 'Ask Corgi', and full scripting (corgi list/message/pane read --json) for driving agents from code."
---

Corgi began as its author's daily driver replacement for tmux while managing a growing stable of coding agents, and it is now a polished terminal multiplexer in the lineage of herdr (its stated inspiration, whose workspaces it can import, handoff included). Workspaces hold folders, tabs, and split panes; agents started in them are auto-detected per CLI, and Corgi installs Claude Code/Codex hooks or a Pi extension so the sidebar reports working/needs-you/done states, activity summaries, subagent activity, and token and rate-limit usage, with multiple accounts per agent and one-key jumps to the next agent that needs attention. Linked git worktrees group agents sharing a repo, a Reviewer agent can be started on any worktree's changes, 'Ask Corgi' runs an agent headlessly over the current workspace, and everything is scriptable over a JSON CLI so other agents can drive panes too. After a crash or reboot, recorded agent sessions come back dormant and resume on focus. It is built with Bun and a pinned Zig toolchain on top of Ghostty's terminal core and pi-tui, ships for macOS and Linux in five languages, and is aimed at developers running several coding agents who want terminal-native control rather than a browser dashboard.
