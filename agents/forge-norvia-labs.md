---
name: "Forge (Norvia Labs)"
slug: "forge-norvia-labs"
layout: "agent.njk"
category: "agent"
maker: "NorviaLabs"
license: "MIT"
url: "https://github.com/NorviaLabs/forge"
source_code_url: "https://github.com/NorviaLabs/forge"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-07-22"
current_release: "2026-08-20"
stars: "6"
language: "Rust"
homepage: "https://forge.norvialabs.com"
mcp_support: True
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: False
plan_mode: False
model_providers: "OpenAI, Anthropic, xAI Grok, OpenAI Codex (via device login), OpenCode Go, OpenCode Zen, Ollama"
pricing: "Free / open-source (MIT)"
install_method: "Prebuilt installer: curl --proto '=https' --tlsv1.2 -LsSf https://raw.githubusercontent.com/NorviaLabs/forge/main/install/forge-installer.sh | sh; Windows PowerShell: irm https://raw.githubusercontent.com/NorviaLabs/forge/main/install/forge-installer.ps1 | iex; Build from source: cargo build --release --locked --package forge-cli"
docs_url: "https://forge.norvialabs.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/NorviaLabs/forge/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Unifies AI agent, code editor, file explorer, shell, approvals, diffs, and durable sessions in one keyboard-driven TUI workspace. Every shell command runs inside an OS-level sandbox (macOS Seatbelt, Linux bubblewrap, WSL2) with network egress filtering via an allow-list proxy. Durable SQLite session journals allow resuming after interruption. Vim-style editing built in."
---

Unifies AI agent, code editor, file explorer, shell, approvals, diffs, and durable sessions in one keyboard-driven TUI workspace. Every shell command runs inside an OS-level sandbox (macOS Seatbelt, Linux bubblewrap, WSL2) with network egress filtering via an allow-list proxy. Durable SQLite session journals allow resuming after interruption. Vim-style editing built in.
