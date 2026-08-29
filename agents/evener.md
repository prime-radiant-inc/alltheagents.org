---
name: "Evener"
slug: "evener"
layout: "agent.njk"
category: "agent"
maker: "prime-radiant-inc"
license: "MIT"
url: "https://github.com/prime-radiant-inc/evener"
source_code_url: "https://github.com/prime-radiant-inc/evener"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-10"
current_release: "2026-08-20"
stars: "103"
language: "Go"
homepage: "https://github.com/prime-radiant-inc/evener"
mcp_support: "yes"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "OpenAI, Anthropic, Google, MiniMax, OpenRouter, OpenRouter-Anthropic, Kimi, GLM, Ollama"
pricing: "Free / open source"
install_method: "curl -fsSL https://raw.githubusercontent.com/prime-radiant-inc/evener/main/install.sh | sh or make install from source"
docs_url: "https://github.com/prime-radiant-inc/evener/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/prime-radiant-inc/evener/releases"
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "Non-interactive design (give it a prompt, it does the work autonomously); multi-session web orchestrator (Hub) with browser UI; TUI dashboard; edit-to-fork session branching; transparent session resume; sandbox mode (--sandbox); structured output via JSON Schema; forked from Kilroy (Dan Shapiro / StrongDM Attractor project); unified LLM library across many providers"
---

Evener came out of the observation that interactive chat is the wrong default for much agent work: given a prompt, it reads, writes, runs commands, and searches in a loop until done, and every surface — the one-shot CLI, the terminal TUI, and the browser Hub — drives that same loop. The Hub serves many concurrent sessions with a live project-grouped sidebar, a two-tier transcript that separates messages from muted tool annotations, ⌘K search, and cookie-based auth via one-time token URLs. Any user message can be forked into a sibling branch or, via /aside, forked at the tip into a side thread with the same permissions and config, which makes recovering from a bad direction cheap. Subagents and hooks follow documented runtime contracts, sandbox flags confine file/process/network access, and nine model providers including local Ollama are supported.
