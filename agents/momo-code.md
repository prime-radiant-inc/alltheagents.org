---
name: "momo-code"
slug: "momo-code"
layout: "agent.njk"
category: "agent"
maker: "momozi1996"
license: "MIT"
url: "https://github.com/momozi1996/momo-code"
source_code_url: "https://github.com/momozi1996/momo-code"
source_available: True
platforms: []
first_released: "2026-06-16"
current_release: "2026-08-14"
stars: "309"
language: "TypeScript"
homepage: "https://momozi.cc"
mcp_support: True
plugin_support: True
claude_code_plugin: True
subagents: True
hooks: True
plan_mode: True
model_providers: "25+ providers: Deepseek, Zhipu (GLM), Moonshot (Kimi), Anthropic (Claude), OpenAI (GPT-4), Google (Gemini), Doubao, OpenRouter, Groq, Mistral, custom OpenAI-compatible"
pricing: "Free/open-source (MIT); user supplies own LLM API keys"
install_method: "curl -fsSL https://momozi.cc/install | bash; or from source: git clone, npm install, npm run build (requires Node.js >= 20.0.0; Python for simulation)"
docs_url: "https://momozi.cc"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/momozi1996/momo-code"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI coding agent built on opencode with a dual-speed self-evolution system based on the Pioneer Agent research paper: a fast loop (/evolve) that learns tactics in seconds via KEP prompt injection with Thompson sampling, and a slow loop (/fine-tune) that improves model weights over hours via Monte Carlo Graph Search + LoRA with a ratchet gate ensuring monotonic improvement. Also includes a graph engine (/graph) for resumable DAGs of parallel subagent nodes, a simulation agent, and Claude Code config interop."
---

AI coding agent built on opencode with a dual-speed self-evolution system based on the Pioneer Agent research paper: a fast loop (/evolve) that learns tactics in seconds via KEP prompt injection with Thompson sampling, and a slow loop (/fine-tune) that improves model weights over hours via Monte Carlo Graph Search + LoRA with a ratchet gate ensuring monotonic improvement. Also includes a graph engine (/graph) for resumable DAGs of parallel subagent nodes, a simulation agent, and Claude Code config interop.
