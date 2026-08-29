---
name: "rayu-cli"
slug: "rayu-cli"
layout: "agent.njk"
category: "agent"
maker: "Choeng-Rayu"
license: "MIT"
url: "https://github.com/Choeng-Rayu/rayu-cli"
source_code_url: "https://github.com/Choeng-Rayu/rayu-cli"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-05-31"
current_release: "2026-08-08"
stars: "36"
language: "TypeScript (CLI), Go (gateway), NestJS (backend), Next.js (web)"
homepage: "https://rayucode.com"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, DeepSeek, Google Gemini, Kimi, Ollama, LM Studio (local models)"
pricing: null
install_method: "npm install -g @rayu-dev/rayu-cli; run rayu. Or npx @rayu-dev/rayu-cli without installing."
docs_url: "https://rayucode.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@rayu-dev/rayu-cli"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal AI coding agent with native real-time P2P collaboration (no cloud intermediaries), sub-500ms time-to-first-token via a custom React/Ink renderer and Go gateway, zero-data-retention privacy, built-in Agent Swarms for parallel multi-agent execution, offline capabilities via Ollama/LM Studio, and multi-provider BYOK across 6+ providers with mid-session model switching."
---

Rayu CLI is a terminal coding agent built around a claim most competitors lack: native peer-to-peer collaboration, where two developers share a live agent session directly rather than relaying through cloud intermediaries. The client is a TypeScript/Ink application with a custom renderer, fronted by a Go gateway and a NestJS backend, with model access via BYOK across Anthropic, OpenAI, DeepSeek, Gemini, Kimi, and local Ollama or LM Studio deployments. Beyond collaboration, it runs parallel 'agent swarms' of specialized subagents and offers an optional hosted gateway with a zero-data-retention policy for users who prefer not to manage keys. The project markets aggressively against Claude Code, OpenCode, and Codex, though its performance and superiority claims remain its own rather than independently verified. It is aimed at teams and enterprises that want terminal agents without routing code through a vendor's cloud.
