---
name: "vibeyard"
slug: "vibeyard"
layout: "agent.njk"
category: "multiplexer"
maker: "elirantutia"
license: "MIT"
url: "https://github.com/elirantutia/vibeyard"
source_code_url: "https://github.com/elirantutia/vibeyard"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-03-19"
current_release: "2026-07-27"
stars: "1352"
language: "TypeScript"
homepage: "https://github.com/elirantutia/vibeyard"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google"
pricing: "open-source"
install_method: "binary, npm"
docs_url: "https://github.com/elirantutia/vibeyard#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/elirantutia/vibeyard/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "IDE built specifically for AI coding agents — multi-session PTY management, kanban task board, P2P live session sharing (WebRTC), swarm mode, cost & context tracking per session, AI Readiness Score, embedded browser with DOM element inspection, multiple Claude profiles with isolated configs."
---

Running several agent CLIs means juggling terminal tabs with no overview of which session is waiting, what each costs, or whether the repository is ready for agentic work at all. Vibeyard makes sessions the primary object: each project has a kanban board whose cards spawn and resume Claude Code, Codex, or Gemini CLI sessions in dedicated PTYs, completed sessions move their own cards, and a swarm grid lays every live session out for parallel supervision. It tracks cost, token, and context-window usage per session, scores the repo's AI Readiness, embeds a browser whose DOM elements can be inspected and sent to the agent for editing, and separates work/personal Claude accounts into isolated profiles. Independent developers and small teams supervising multiple agent runs use it; it is MIT-licensed Electron/TypeScript with signed installers for all three desktop platforms.
