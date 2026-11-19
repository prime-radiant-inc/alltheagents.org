---
name: "bise"
slug: "bise"
layout: "agent.njk"
category: "agent"
maker: "gvergnaud"
license: "Apache-2.0"
url: "https://bise.dev"
source_code_url: "https://github.com/gvergnaud/bise"
source_available: "True"
homepage: "https://bise.dev"
docs_url: "https://bise.dev/docs/"
download_url: "https://bise.dev/download/mac"
install_method: "bise terminal: curl -fsSL bise.dev/install | sh, then run bise inside a repo (macOS, Linux x86_64/arm64, glibc 2.34+); bise desktop: download the .dmg from bise.dev (macOS 14+, Apple silicon); from source: git clone + ./run.sh"
platforms:
  - "CLI"
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-09-25"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Anthropic, OpenAI, Google AI Studio, Mistral, OpenRouter, Groq, xAI, DeepSeek, Together AI, Fireworks AI, Cerebras, any OpenAI-compatible endpoint, local models via Ollama or LM Studio; plans via ChatGPT Plus/Pro login, OpenRouter sign-in, GLM Coding Plan, Kimi Code, MiniMax M plan"
pricing: "free"
stars: "51"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "One lead agent splits your requests into jobs and starts one of its own agents per task, each on a git worktree it creates and removes itself, while every decision that needs you waits in a single inbox — and the hub that carries the agents' messages is written in Bend with checked proofs that no message is lost or delivered twice."
---

bise is a multi-agent harness for people who would rather brief one agent than supervise five: you talk to the lead (main), it splits what you ask into tasks, does the small ones itself, and starts an agent per task when one is needed. The agents work in parallel in your checkout, message each other before touching the same files, and take an automatic git worktree when one needs its own copy — no branches to name, no folders to clean up. What needs you (approvals, choices between options, merges) waits in one inbox, and agents ask the lead rather than you, so only the decisions that are actually yours arrive. The hub that keeps the state of every agent and message runs locally, its sb-core message layer written in the Bend language with checked laws and proofs (no message lost or delivered twice, a restart rebuilds the same state), and each agent's loop runs in bise's own runtime, where agents write small TypeScript scripts to call several tools in one step. Plugins use the Agent Plugins format — skills, MCP servers (local or remote with OAuth) and hooks load from ~/.agents/plugins or your repo — and bise can import the keys, models, CLAUDE.md, skills and MCP servers you already have from Claude Code or Codex. The desktop app (macOS 14+, Apple silicon) and the terminal (macOS and Linux) are two clients of the same hub; the desktop build also adds voice and computer use, while the terminal works over SSH. It is built by Gabriel Vergnaud, largely developed using bise itself, and aimed at developers running several agents on real projects who want one thread and one inbox instead of a grid of terminals.
