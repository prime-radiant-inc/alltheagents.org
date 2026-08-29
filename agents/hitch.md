---
name: "hitch"
slug: "hitch"
layout: "agent.njk"
category: "other"
maker: "maxktz"
license: "MIT"
url: "https://github.com/maxktz/hitch"
source_code_url: "https://github.com/maxktz/hitch"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-24"
current_release: "2026-06-07"
stars: "176"
language: "Rust"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "none"
pricing: "Free / open source (MIT)"
install_method: "npm install -g hitch-cli then run hitch (first-run wizard sets up SKILL.md)"
docs_url: "https://github.com/maxktz/hitch#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Lightweight CLI tool that lets AI coding agents share, inspect, and control your real, running terminal. A shell proxy (not a tmux-like multiplexer) that lets agents observe and interact with terminals you already have running. Proxies I/O, records context, and exposes agent-friendly commands (hitch/unhitch). Integrates with skills.sh via SKILL.md. Supports macOS and Linux on arm64/x64."
---

hitch addresses the gap between a coding agent and the terminal session the developer is actually working in. Running hitch wraps the current shell as a transparent proxy: the human keeps typing normally while the proxy records useful context and exposes commands that let an agent send input, read output, and observe what is happening in the same session. This removes common frictions — an agent can check whether a dev server is already running, read the output of a long-running process, or interact with a running process without the user copy-pasting logs. The agent-facing contract ships as a SKILL.md installed on first run, so any skills-aware agent discovers how to use it without bespoke integration. The tool stays out of the way on the human side: unhitch restores an ordinary shell.
