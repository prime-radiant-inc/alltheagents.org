---
name: "herdrm"
slug: "herdrm"
layout: "agent.njk"
category: "multiplexer"
maker: "missuo"
license: "MIT"
url: "https://github.com/missuo/herdrm"
source_code_url: "https://github.com/missuo/herdrm"
source_available: "True"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-08-19"
current_release: "2026-08-19"
stars: "416"
language: "Swift"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (attaches to herdr-hosted agents: Claude Code, Codex, Gemini, Grok, OpenCode)"
pricing: "Free / open-source"
install_method: "Homebrew (brew install owo-network/brew/herdrm) or manual download of .zip from Releases"
docs_url: "https://herdr.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/missuo/herdrm/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Native macOS console for herdr that aggregates all herdr-managed coding agents across local and remote (SSH) machines in one window with live PTY attachment, notifications, and Cmd-K search; auto-reconnects remote machines via SSH tunneling"
---

herdrm is a native macOS client for herdr, the background daemon that keeps coding-agent sessions alive. It presents one window listing every herdr-managed agent across the local machine and SSH-connected servers, with live status for spaces, agents, and terminals, and Cmd-K search across all devices. Attachment happens over the genuine PTY through a SwiftTerm-based terminal view, preserving the full TUI rendering of Claude Code, Codex, Gemini, Grok, and OpenCode sessions rather than reducing them to a chat-style transcript. Beyond observation it supports interaction: pasting files and images into agents, a two-pane file manager for local and SSH transfers, and system notifications when an agent finishes or blocks. The app is signed and notarized with Sparkle auto-updates, ships as a universal binary, and is explicitly early-stage software under active development.
