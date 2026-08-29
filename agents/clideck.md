---
name: "CliDeck"
slug: "clideck"
layout: "agent.njk"
category: "multiplexer"
maker: "rustykuntz"
license: "MIT"
url: "https://github.com/rustykuntz/clideck"
source_code_url: "https://github.com/rustykuntz/clideck"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-03-03"
current_release: "2026-08-19"
stars: "151"
language: "JavaScript"
homepage: "https://clideck.dev"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Claude Code, Codex, Gemini CLI, OpenCode, Pi (any terminal CLI)"
pricing: "free"
install_method: "npm install -g clideck or npx clideck (Node 18+)"
docs_url: "https://docs.clideck.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/clideck"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local dashboard for running and coordinating multiple AI CLI coding agents (Claude Code, Codex, Gemini CLI, OpenCode, Pi) in one browser window with chat-style sidebar, live status detection, session resume, inter-agent communication, autopilot routing between agents, projects grouping, prompt library, and an E2E encrypted mobile relay - without sitting between agents rewriting prompts."
---

CliDeck rethinks the tmux pane grid as a chat-style interface: agents keep running in their real terminals, but the dashboard groups them by project, shows live working/idle/waiting status, previews messages, and resumes sessions, all while explicitly not sitting in the middle of the conversation. The ask-another-session feature injects a message into a target agent's terminal and returns the response, giving lightweight cross-agent consultation without an orchestration layer. Everything is local with no data leaving the machine, and a plugin API covers voice input and autopilot. Developers who run several CLIs but dislike pane-based multiplexers are the audience.
