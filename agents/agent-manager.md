---
name: "Agent-Manager"
slug: "agent-manager"
layout: "agent.njk"
category: "multiplexer"
maker: "YoanWai"
license: "Apache-2.0"
url: "https://github.com/YoanWai/agent-manager"
source_code_url: "https://github.com/YoanWai/agent-manager"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-15"
current_release: "2026-08-27"
stars: 372
language: "Go"
homepage: "https://agent-manager.dev"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to the connected agents (Claude Code, Codex, OpenCode, Grok Build, Gemini CLI, Pi, Command Code, Hermes Agent)"
pricing: "free"
install_method: "Homebrew, install script, Arch AUR, mise, go install, or prebuilt binaries; requires tmux 3.1+ and git"
docs_url: "https://github.com/YoanWai/agent-manager/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/YoanWai/agent-manager/releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A tmux-based Bubbletea TUI that runs every AI coding agent side by side, each in its own persistent tmux session with your own logins, configs, and MCP servers intact — with live status detection grouped in a project tree, spacebar quick-prompts into any session, ctrl+r diff review that sends line comments back as one review prompt, and git worktree spawning."
---

Agent-Manager is a thin layer over the agent CLIs you already have installed: each agent — Claude Code, Codex, OpenCode, Grok Build, Gemini CLI, Pi, Command Code, or Hermes Agent — runs in its own persistent tmux session, so your subscriptions, config files, and MCP servers stay exactly as they were. The Go/Bubbletea TUI shows live status detection of which agents are done, waiting, or stuck, grouped in a project tree, and the workflow keys are built for fleet supervision: space sends a prompt into any session without attaching, v revives a dead session on its own conversation, f forks a conversation into a separate named session, and ctrl+r opens syntax-highlighted full-file diffs of an agent's changes whose line comments get sent back to the agent as a single review prompt. Arbitrary CLI tools can be registered through a [tools.<name>] config block with custom status rules, and agents spawn into isolated git worktrees. It targets macOS and Linux (Windows via WSL2) developers juggling several agent subscriptions at once.
