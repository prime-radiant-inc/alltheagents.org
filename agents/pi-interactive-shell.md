---
name: "pi-interactive-shell"
slug: "pi-interactive-shell"
layout: "agent.njk"
category: "agent"
maker: "nicobailon"
license: null
url: "https://github.com/nicobailon/pi-interactive-shell"
source_code_url: "https://github.com/nicobailon/pi-interactive-shell"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-01-18"
current_release: "2026-08-15"
stars: "561"
language: "TypeScript"
homepage: "https://github.com/nicobailon/pi-interactive-shell"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "Pi, Codex, Claude, Cursor, Aider"
pricing: "free"
install_method: "npm"
docs_url: "https://github.com/nicobailon/pi-interactive-shell"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/nicobailon/pi-interactive-shell"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Full PTY emulation without tmux; observable TUI overlay where the user can take over control anytime; token-efficient; four modes (interactive, hands-free, dispatch, monitor) with event-driven triggers; structured spawn for multiple coding agents; headless background dispatch for parallel work"
---

pi-interactive-shell solves a specific failure mode in coding agents: their shell tools time out on anything interactive, so vim, REPLs, SSH sessions, and long-running dev servers stay out of reach. The extension runs a full PTY stack — zigpty binaries plus headless terminal emulation — so subprocesses believe they have a real terminal, while a TUI overlay shows the user exactly what the agent sees and allows typing to take over at any moment. Four modes fit different workflows: interactive for back-and-forth editors, hands-free for servers the agent polls, dispatch for fire-and-forget work that wakes the agent on completion, and monitor for event-driven triggers like regex matches or file changes. Structured spawn parameters can launch entire coding agents (pi, codex, claude, cursor) as subagents, optionally in isolated worktrees, with output transferable back to the parent session. Pi users who want the agent handling interactive workflows rather than just one-shot commands are the audience.
