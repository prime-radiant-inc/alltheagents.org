---
name: "pixtuoid"
slug: "pixtuoid"
layout: "agent.njk"
category: "multiplexer"
maker: "IvanWng97"
license: "MIT"
url: "https://github.com/IvanWng97/pixtuoid"
source_code_url: "https://github.com/IvanWng97/pixtuoid"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-21"
current_release: "2026-08-19"
stars: "449"
language: "Rust"
homepage: "https://pixtuoid.dev"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "Claude Code, Codex CLI, Antigravity, DeepSeek-Reasonix, CodeWhale, Copilot CLI, opencode, Cursor CLI, Hermes Agent, Oh My Pi, OpenClaw, Grok Build, Kimi Code CLI"
pricing: "Free / open-source (MIT)"
install_method: "Homebrew (brew install pixtuoid), npm (npm install -g pixtuoid), Cargo, prebuilt binaries, or Debian .deb"
docs_url: "https://pixtuoid.dev/"
plugin_docs_url: null
config_docs_url: "https://pixtuoid.dev/config"
download_url: "https://github.com/IvanWng97/pixtuoid/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Terminal pixel-art office TUI that visualizes AI coding agents as pixel-art coworkers at desks; agents type while working, raise ? when waiting for permission, and sleep when done; A*-routed pathfinding, office pets, lofi soundtrack, floating desktop window mode, local-only privacy"
---

pixtuoid addresses the visibility gap that opens up when several coding-agent sessions run at once: nothing shows at a glance which agent is working, blocked on a permission prompt, or finished. The tool watches sessions read-only — through a hook shim and JSONL transcript tails for Claude Code, Codex, and roughly a dozen other CLIs — and renders each as a pixel-art character at a desk: typing while working, raising a ? when waiting for approval, sleeping when done. Characters walk between desks via A* pathfinding, office pets wander the floor, and a lofi soundtrack plays, with a floating desktop-window mode keeping the office visible during real work. Everything stays local with no telemetry; state arrives through the hook shim and transcript files rather than any agent integration, so pixtuoid never touches the agents themselves. Built in Rust and distributed via Homebrew, npm, and Cargo, it targets developers running multiple agent sessions who want ambient, glanceable status.
