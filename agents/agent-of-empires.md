---
name: "agent-of-empires"
slug: "agent-of-empires"
layout: "agent.njk"
category: "multiplexer"
maker: "agent-of-empires"
license: "MIT"
url: "https://github.com/njbrake/agent-of-empires"
source_code_url: "https://github.com/njbrake/agent-of-empires"
source_available: "Yes"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-01-09"
current_release: "2026-08-19"
stars: "3102"
language: "Rust"
homepage: "http://www.agent-of-empires.com/"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google, Mistral, BYOK"
pricing: "open-source"
install_method: "brew"
docs_url: "https://www.agent-of-empires.com/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/agent-of-empires/agent-of-empires/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Session manager for AI coding agents (TUI + web dashboard) that runs multiple agents in parallel across git branches in isolated tmux sessions with optional Docker sandboxing, accessible from any browser or phone."
---

Running several coding agents against one repository creates branch collisions and terminal sprawl, so agent-of-empires assigns each agent its own git branch inside an isolated tmux session, with Docker sandboxing optional for riskier work. It speaks the Agent Client Protocol, which is why the web dashboard can show structured views — plan panels, tool-call cards, swipe-to-approve permission requests — instead of raw terminal output, all reachable from a laptop browser or a phone. A TUI covers terminal-native workflows, and agents (Claude Code, Codex CLI, Gemini CLI, OpenCode) run in parallel across branches. It is MIT-licensed Rust, installed via brew or an install script, aimed at developers running several agents concurrently.
