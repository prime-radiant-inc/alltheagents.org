---
name: "Multistack"
slug: "multistack"
layout: "agent.njk"
category: "multiplexer"
maker: "gi-dellav"
license: "GPL-3.0-only"
url: "https://gi-dellav.github.io/multistack/"
source_code_url: "https://github.com/gi-dellav/multistack"
source_available: "True"
homepage: null
docs_url: "https://github.com/gi-dellav/multistack/blob/main/README.md"
download_url: null
install_method: "curl -fsSL https://raw.githubusercontent.com/gi-dellav/multistack/main/install.sh | bash"
platforms:
  - "CLI"
autonomy_level: []
specialization: "general"
language: "Rust"
first_released: "2026-06-05"
current_release: "2026-09-07"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "zerostack (OpenRouter, OpenAI, Anthropic, Gemini, Ollama, custom providers via zerostack)"
pricing: "free"
stars: "19"
sources:
  - "github-issue"
last_verified: "2026-09-16"
what_makes_it_special: "A lightweight Rust TUI for running multiple zerostack agents side by side in the terminal, with live status glyphs, per-agent timers, and desktop notifications when an agent waits for input."
---

Multistack is a lightweight Rust TUI that runs multiple zerostack agents side by side in the terminal, giving each agent its own PTY and Unix-socket status channel. It spawns parallel agents with zerostack --parallel, tracks live status (working, waiting, done, dead, conflict) with per-agent timers, and lets you drop into any agent's terminal output or signal an agent parked on a permission prompt. Keybindings spawn, rename, kill, and remove agents and projects, with support for git-worktree isolation, lazygit and shell popouts, and protocol v1.1 blocked/working signals. The tool requires Linux, BSD, or macOS, zerostack v1.5+ with the status-signals feature, and Rust 1.85+, and installs via Homebrew tap, curl script, or cargo. As a native open-source alternative to Conductor, it targets developers who orchestrate several zerostack sessions from one keyboard-driven dashboard rather than coding directly.
