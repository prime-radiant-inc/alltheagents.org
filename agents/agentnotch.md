---
name: "agentnotch"
slug: "agentnotch"
layout: "agent.njk"
category: "other"
maker: "AppGram"
license: "MIT"
url: "https://github.com/AppGram/agentnotch"
source_code_url: "https://github.com/AppGram/agentnotch"
source_available: "True"
platforms:
  - "IDE"
  - "Desktop"
first_released: "2026-01-05"
current_release: "2026-01-19"
stars: "211"
language: "Swift"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, OpenAI Codex (observes via OTLP telemetry)"
pricing: "Free / open-source"
install_method: "brew tap AppGram/tap && brew install --cask agentnotch (or manual download from GitHub Releases)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/AppGram/agentnotch/releases"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "macOS menu-bar app living in the Mac notch that shows real-time AI coding assistant telemetry (tool calls, token usage, cost estimates); uses source-aware color indicators (orange for Claude, blue for Codex), runs 100% locally for privacy, expands on hover to show activity."
---

Coding agents run long tool sequences in a terminal, and developers currently have no ambient way to see what the agent is doing without switching windows. AgentNotch receives OpenTelemetry OTLP logs and metrics that Claude Code and Codex CLI emit after a one-line configuration change (OTEL_EXPORTER_OTLP_ENDPOINT for Claude Code, an [otel] block in ~/.codex/config.toml), and renders tool calls, token usage, and cost estimates in the notch, expanding on hover. Completion notifications fire when a run finishes, and source-based coloring distinguishes which assistant produced each event. Everything is processed locally on port 4318; the app sends nothing anywhere. It targets macOS 14+ on notch-equipped MacBook Pros, falling back to the menu bar elsewhere.
