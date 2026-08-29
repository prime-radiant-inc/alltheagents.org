---
name: "pi-gui"
slug: "pi-gui"
layout: "agent.njk"
category: "multiplexer"
maker: "minghinmatthewlam"
license: "MIT"
url: "https://github.com/minghinmatthewlam/pi-gui"
source_code_url: "https://github.com/minghinmatthewlam/pi-gui"
source_available: "True"
platforms: []
first_released: "2026-03-20"
current_release: "2026-07-28"
stars: "854"
language: "TypeScript"
homepage: "https://www.pi-gui.com/"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "multiple (via pi runtime; OAuth or API key)"
pricing: "open-source"
install_method: "binary (dmg/AppImage), brew"
docs_url: "https://www.pi-gui.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/minghinmatthewlam/pi-gui/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Native desktop (Electron) shell around the pi coding agent runtime with a Codex-style threaded timeline UI, git worktrees per thread, multi-agent orchestration (supervisor/worker), integrated PTY terminal, and inline diff viewer. Uses pi's JSONL session files as the source of truth via a thin pi-sdk-driver adapter."
---

pi-gui exists because pi's terminal-first interface limits visibility once developers run several threads, supervise workers, or review diffs across parallel work. The Electron app wraps the pi runtime without forking it: a Codex-style timeline shows threaded sessions, each thread can run in an isolated git worktree, and an orchestrator thread spawns and supervises worker threads for multi-agent runs. An integrated PTY terminal, inline diff viewer, session archive, and notification system cover the day-to-day loop, while pi's JSONL session files stay the source of truth so CLI and GUI sessions interoperate. Public beta builds ship signed and notarized for Apple Silicon Macs and Linux, with a Homebrew cask and source build for contributors. Its users are pi users who want desktop ergonomics and structured orchestration instead of a raw terminal.
