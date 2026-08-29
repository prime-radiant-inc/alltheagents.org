---
name: "Ivy Tendril"
slug: "ivy-tendril"
layout: "agent.njk"
category: "multiplexer"
maker: "Ivy-Interactive"
license: "FSL-1.1-ALv2"
url: "https://github.com/Ivy-Interactive/Ivy-Tendril"
source_code_url: "https://github.com/Ivy-Interactive/Ivy-Tendril"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-04-15"
current_release: "2026-08-19"
stars: "171"
language: "C#"
homepage: "https://tendril.ivy.app"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: "True"
model_providers: null
pricing: "free"
install_method: "Download installer from GitHub Releases, or: curl -sSf https://cdn.ivy.app/install-tendril.sh | sh (macOS/Linux), irm https://cdn.ivy.app/install-tendril.ps1 | iex (Windows)"
docs_url: "https://tendril.ivy.app/docs/gettingstarted/introduction"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Ivy-Interactive/Ivy-Tendril/releases/latest"
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "Desktop orchestrator for parallel AI coding agents using isolated git worktrees; works with any CLI agent (Claude Code, Codex, GitHub Copilot, Gemini, OpenCode); Cloudflare Quick Tunnel remote/mobile coding, Whisper voice input, plan versioning, automated code review gates (build/test/lint/format)."
---

Tendril is built by the Ivy-Interactive team (behind the Ivy framework) as an IDE replacement for the agentic era. The core mechanic is worktree isolation: each agent gets its own git worktree so parallel work never touches main, and humans review diffs, annotate plans (edits automatically revise agent goals), and approve merges through verification gates. GitHub webhooks convert issues and jam.dev bug reports into jobs automatically. Cloudflare Quick Tunnels expose running sessions to a phone for remote steering, and Whisper dictation feeds prompts by voice. It ships as installers or one-line scripts for macOS, Windows, and Linux under the Functional Source License, free today and Apache/MIT after the grace period.
