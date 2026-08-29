---
name: "Forge-Agentic-Coding-CLI"
slug: "forge-agentic-coding-cli"
layout: "agent.njk"
category: "agent"
maker: "hoangsonww"
license: "MIT"
url: "https://github.com/hoangsonww/Forge-Agentic-Coding-CLI"
source_code_url: "https://github.com/hoangsonww/Forge-Agentic-Coding-CLI"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-04-20"
current_release: "2026-08-16"
stars: "22"
language: "TypeScript"
homepage: "https://hoangsonww.github.io/Forge-Agentic-Coding-CLI/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Ollama, LM Studio, vLLM, llama.cpp, OpenAI-compatible (OpenAI/Azure/LocalAI/Together/Groq/Fireworks), Anthropic"
pricing: "Free / open-source (MIT)"
install_method: "npm install -g @hoangsonw/forge, Docker, docker compose, or VS Code extension"
docs_url: "https://hoangsonww.github.io/Forge-Agentic-Coding-CLI/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@hoangsonw/forge"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Local-first, plan-first, multi-agent, programmable software-engineering runtime with its own scheduler, sandbox, default-deny permission system, state machine, agentic loop, and 4-tier memory (hot/warm/cold/learning). Fully inspectable and replayable sessions (JSONL/SQLite), 6 built-in role-typed agents (planner, architect, executor, reviewer, debugger, memory), no telemetry."
---

Forge was built as an alternative to trusting a hosted agent with your repository: everything runs locally with no telemetry, actions pass through a default-deny permission system with a realpath-confined filesystem and destructive-command blocking, and secrets live in the OS keychain. Requests flow through a plan-first loop — classify, plan into a DAG, user approval, bounded execution, validation gate, reviewer — with retry capped at three before a debugger diagnosis phase. Local model runtimes (Ollama, LM Studio, vLLM, llama.cpp) are auto-detected and prompts are adapted across 41 classified model families per agent role, with hosted Anthropic/OpenAI-compatible access optional. Nine enforceable modes with per-mode budgets, a local web dashboard, a GitHub Action, and 24 subcommands round out a runtime aimed at developers who want Claude Code-style capability without cloud dependency.
