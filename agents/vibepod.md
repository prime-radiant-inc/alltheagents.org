---
name: "VibePod"
slug: "vibepod"
layout: "agent.njk"
category: "multiplexer"
maker: "VibePod"
license: "MIT"
url: "https://github.com/VibePod/vibepod-cli"
source_code_url: "https://github.com/VibePod/vibepod-cli"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-02-10"
current_release: "2026-08-18"
stars: "134"
language: "Python"
homepage: "https://vibepod.dev"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude, Gemini, Codex, Devstral, Copilot, Auggie, Pi, Qwen, OpenCode"
pricing: "Free (MIT)"
install_method: "pip install vibepod"
docs_url: "https://vibepod.dev/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/vibepod/"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Unified CLI for running AI coding agents in isolated Docker/Podman containers with zero config; collects local metrics (HTTP traffic, token usage) and provides an analytics dashboard to compare agents side-by-side; privacy-first, all data stays local"
---

VibePod exists because evaluating or running several coding agents means installing a dozen CLIs, each with its own dependencies and permission flags, and no way to compare their behavior afterward. One Python CLI launches any supported agent — Claude, Gemini, Codex, Copilot, Auggie, Qwen, OpenCode, and others — inside a Docker or Podman container built from maintained images, with optional per-project overlay fragments adding dependencies without forking images. An --ikwid flag auto-appends each agent's auto-approval flag for hands-off runs, and while agents work, a local dashboard records HTTP traffic, token usage, and per-agent metrics for side-by-side comparison. Developers choosing between agents, or isolating them from their host machine, use it; it is MIT-licensed, installable via pip/Homebrew/conda, and under steady development with images published to Docker Hub.
