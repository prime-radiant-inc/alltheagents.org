---
name: "agent-sh"
slug: "agent-sh"
layout: "agent.njk"
category: "agent"
maker: "guanyilun"
license: "MIT"
url: "https://github.com/guanyilun/agent-sh"
source_code_url: "https://github.com/guanyilun/agent-sh"
source_available: True
platforms: []
first_released: "2026-04-08"
current_release: "2026-08-14"
stars: "66"
language: "TypeScript"
homepage: "https://agent-sh.dev"
mcp_support: False
plugin_support: True
claude_code_plugin: False
subagents: False
hooks: False
plan_mode: False
model_providers: "OpenRouter, OpenAI, DeepSeek, Ollama"
pricing: "Free/open-source (MIT, BYO API keys)"
install_method: "npm install -g agent-sh (requires Node.js 18+; supports bash, zsh, fish; not native Windows, use WSL)"
docs_url: "https://agent-sh.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Composable agent runtime pairing any frontend (shell, TUI, GUI) with any agent backend over one shared extension layer. A pure kernel (typed event bus + handler registry + extension loader) sits at the center, knowing nothing about terminals, LLMs, shells, or rendering. The bundled frontend is a shell where typing > invokes an agent that already sees your cwd, last command, and its output. Frontends and backends are freely mix-and-matchable (swap ash for pi, claude-code, or opencode via in-the-box bridges)."
---

Composable agent runtime pairing any frontend (shell, TUI, GUI) with any agent backend over one shared extension layer. A pure kernel (typed event bus + handler registry + extension loader) sits at the center, knowing nothing about terminals, LLMs, shells, or rendering. The bundled frontend is a shell where typing > invokes an agent that already sees your cwd, last command, and its output. Frontends and backends are freely mix-and-matchable (swap ash for pi, claude-code, or opencode via in-the-box bridges).
