---
name: "Pane"
slug: "pane"
layout: "agent.njk"
category: "multiplexer"
maker: "dcouple"
license: "AGPL-3.0"
url: "https://github.com/dcouple/Pane"
source_code_url: "https://github.com/dcouple/Pane"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-02-27"
current_release: "2026-08-19"
stars: "392"
language: "TypeScript"
homepage: "https://runpane.com/"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "none (agent-agnostic — runs whatever CLI agent is installed)"
pricing: "Free / open-source (AGPL-3.0)"
install_method: "curl -fsSL https://runpane.com/install.sh | sh, or npx --yes runpane@latest, or pnpm dlx runpane@latest"
docs_url: "https://runpane.com/docs/remote-daemon"
plugin_docs_url: null
config_docs_url: "https://runpane.com/docs"
download_url: "https://github.com/dcouple/Pane/releases/latest"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Terminal-first, agent-agnostic AI agent manager that runs any CLI coding agent (Claude Code, Codex, Cursor, Aider, Goose) in parallel; cross-platform real desktop app; git-native automatic worktree management; no plugins/SDK needed; built-in diff viewer; Remote Pane for managing from desktop or phone."
---

Most agent managers reimplement the agents they host, layering configuration that drifts from the CLIs they wrap. Pane refuses that pattern: it is an Electron desktop app that organizes terminal sessions into 'panes', each with an isolated git worktree, port isolation, a diff viewer, and a file explorer, while the agents inside run completely unmodified — Claude Code, Codex, Cursor Agent, Aider, Goose, or anything terminal-based. Pane Chat adds a global orchestrator terminal for steering the fleet, workflow skills (plan, implement, review, prepare-pr) cache per agent, and @mention terminals route context between panes. A self-hosted Remote Pane exposes the desktop to a phone over pane-remote:// with approval-prompt forwarding, and an agent-operable runpane CLI lets agents create their own workspaces and terminals. Built by Dcouple Inc. under AGPL-3.0, it ships signed installers for macOS, Windows, and Linux with an active changelog. Developers who want fleet management without an abstraction layer over their agents are the audience.
