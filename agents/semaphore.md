---
name: "semaphore"
slug: "semaphore"
layout: "agent.njk"
category: "other"
maker: "lucianodiisouza"
license: "MIT"
url: "https://github.com/lucianodiisouza/semaphore"
source_code_url: "https://github.com/lucianodiisouza/semaphore"
source_available: "True"
platforms: []
first_released: "2026-06-26"
current_release: "2026-07-03"
stars: "42"
language: "Rust"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: null
pricing: "Free"
install_method: "Download pre-built binaries or build from source; semctl install --all for hooks"
docs_url: "https://github.com/lucianodiisouza/semaphore"
plugin_docs_url: "https://github.com/lucianodiisouza/semaphore"
config_docs_url: "https://github.com/lucianodiisouza/semaphore"
download_url: "https://github.com/lucianodiisouza/semaphore/releases/latest"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Floating traffic-light widget for AI coding agents. Always-on-top indicator shows green (idle), yellow (thinking/running tools), or red (writing/editing files) without switching windows. Cross-platform with Stream Deck integration, stealth mode (hidden from screen capture), multi-session state machine with priority-based color selection, themes, sounds, and i18n."
---

The problem is mundane but constant: an agent has been running for ten minutes in a background window and the developer has no idea whether it is waiting for permission or editing files. Semaphore puts a traffic light on top of every workspace, colored by hooks that Cursor, Claude Code, Codex CLI, and Gemini CLI emit into a per-session state machine. The Rust core and Tauri widget are MIT-licensed, with theming, sounds, idle timeout, and a Node.js Stream Deck plugin as conveniences around the IPC protocol. It is cross-platform with signed builds from GitHub Releases and a semctl doctor command to verify hook wiring. The audience is solo developers and pairing sessions where a glanceable indicator beats alt-tabbing, and the project is a modestly maintained hobby-scale codebase with tagged releases.
