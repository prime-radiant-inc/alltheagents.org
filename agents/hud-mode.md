---
name: "HUD"
slug: "hud-mode"
layout: "agent.njk"
category: "multiplexer"
maker: "adrida"
license: "MIT"
url: "https://github.com/adrida/hud-mode"
source_code_url: "https://github.com/adrida/hud-mode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-08-05"
current_release: null
stars: 28
language: "JavaScript"
homepage: "https://tracerml.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to the connected agents (Claude Code, Codex, OpenCode)"
pricing: "free"
install_method: "npm install -g adrida/hud-mode && hud install (Node >= 18)"
docs_url: "https://github.com/adrida/hud-mode/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A compact heads-up display that collapses a coding agent session into a live instrument deck — status flag, model, messages, elapsed time, tokens, cost, context size, subagents — plus an activity line showing READ/EDIT/EXEC, driving each CLI headless through its JSON event stream with zero dependencies and no forks or patches."
---

HUD is a terminal front-end for coding agents built by adrida at tracer: rather than a scrolling wall of tool-call output, it renders the session as gauges — status, model, message count, elapsed time, tokens, cost, context size, subagents — with an activity line showing what the agent is currently doing. The prompt bar is always writable so you can queue a message mid-turn that fires when the agent finishes, escape interrupts without killing the session, and the completed answer renders as markdown with clickable OSC 8 hyperlinks. It drives Claude Code, Codex, and OpenCode headless via their JSON event streams, and a lossless /hud toggle switches back to each engine's full native TUI mid-session through its own resume mechanism. It targets developers who run agent sessions constantly and want telemetry over transcript noise.
