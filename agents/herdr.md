---
name: "herdr"
slug: "herdr"
layout: "agent.njk"
category: "multiplexer"
maker: "herdrdev"
license: "Apache-2.0"
url: "https://github.com/herdrdev/herdr"
source_code_url: "https://github.com/herdrdev/herdr"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-03-27"
current_release: "2026-08-20"
stars: "30767"
language: "Rust"
homepage: "https://herdr.dev"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "none (hosts Claude Code, Codex, Cursor, OpenCode, Grok, and other agent CLIs)"
pricing: "open-source"
install_method: "curl -fsSL https://herdr.dev/install.sh | sh; also Homebrew, mise, PowerShell for Windows, or binaries from GitHub releases"
docs_url: "https://herdr.dev/docs/"
plugin_docs_url: "https://herdr.dev/plugins/"
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "A background terminal server/runtime for coding agents — the runtime 'your coding agents live on'. Always-on server keeps sessions alive across disconnects, lid close, network drops, and reboots. Pane status tracking (working, blocked, idle) lets agents spawn panes, prompt each other, and wait until blocked. Runs existing agents (Claude Code, Codex, Cursor, OpenCode, Grok) without wrapping or replacing them. Single Rust binary, no Electron. Plugin system with marketplace. ~30.8k stars."
---

herdr is a background terminal server built for the specific failure modes of long-running coding agents: a closed laptop, a dropped SSH connection, or a machine reboot used to kill a session mid-task. A daemon owns the terminal sessions that agents such as Claude Code, Codex, Cursor, and OpenCode run in, so those sessions persist across disconnects and reboots and can be reattached from any terminal or over SSH. Each pane reports working, blocked, or idle status so a developer can see at a glance which agent needs input, and a socket API lets agents themselves spawn panes, prompt each other, and wait on blocked peers. The interface keeps tmux conventions (prefix keys) while adding mouse-driven splits, and a plugin system with a marketplace extends the runtime. It ships as a single Rust binary with no Electron, with Windows support in beta.
