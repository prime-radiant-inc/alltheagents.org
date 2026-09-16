---
name: "maki"
slug: "maki"
layout: "agent.njk"
category: "agent"
maker: "tontinton"
license: "MIT"
url: "https://maki.sh"
source_code_url: "https://github.com/tontinton/maki"
source_available: "True"
homepage: null
docs_url: "https://maki.sh/docs/"
download_url: null
install_method: "curl -fsSL https://maki.sh/install.sh | sh"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-02-13"
current_release: "2026-09-16"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: "https://maki.sh/docs/plugins/"
config_docs_url: "https://maki.sh/docs/configuration/"
model_providers: "Anthropic, OpenAI, xAI, Google, Copilot, Ollama, llama.cpp, Mistral, Z.AI, DeepSeek, OpenRouter, Requesty, Synthetic, Regolo, TensorX, OpenCode Zen, OpenCode Go, Aperture"
pricing: "free"
stars: "1042"
sources:
  - "github-issue"
last_verified: "2026-09-16"
what_makes_it_special: "A lightweight Rust TUI coding agent built for context-token efficiency — index skeletons, code_execution sandbox, tool_search and model-tier subagents keep cost and tokens low while staying fast at 60 FPS."
---

maki exists because its author kept bumping into hourly and weekly token limits in existing coding agents and wanted a lighter way to run long sessions without blowing through context. Written mostly in Rust with a ratatui TUI, it runs as a native binary at 60 FPS with SIMD-rendered splash screens and threaded syntax highlighting, and keeps the loop honest: token count, cost, and active model stay visible in the status bar, every subagent gets its own chat window reachable from /tasks, and fuzzy search, plan mode, parallel sessions, and long-term memory are in the box. The efficiencies are the point: an index tool parses 15 languages into compact skeletons so the model reads only needed lines, code_execution exposes every tool as an async Python function so batch work never hits the context, tool_search defers MCP tool definitions behind one search tool, subagents can be weak, medium, or strong per handoff, and compaction trims long sessions while the prompt itself stays short. Plugins extend it in Lua through a Neovim-like API, so adding tools, slash commands, or UI is a single file under ~/.config/maki/plugins, and MCP over stdio or HTTP plus ACP and opt-in OpenTelemetry keep it interoperable. It covers Anthropic, OpenAI, Google, Copilot, Ollama and a dozen more providers out of the box, installs with curl -fsSL https://maki.sh/install.sh | sh, and is aimed at developers who want a hackable, local-first agent they can steer, instrument, and run headless when needed.
