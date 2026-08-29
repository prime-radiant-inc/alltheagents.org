---
name: "gptme"
slug: "gptme"
layout: "agent.njk"
category: "agent"
maker: "gptme"
license: "MIT"
url: "https://github.com/gptme/gptme"
source_code_url: "https://github.com/gptme/gptme"
source_available: "True"
platforms:
  - "CLI"
first_released: "2023-03-24"
current_release: "2026-08-20"
stars: "4390"
language: "Python"
homepage: "https://gptme.org"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "Anthropic, OpenAI, Google, xAI, DeepSeek, OpenRouter, llama.cpp"
pricing: "open-source"
install_method: "pip"
docs_url: "https://gptme.org/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/gptme/gptme/releases/latest"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "One of the first agent CLIs (Spring 2023), still actively developed. Provider-agnostic and local-first — runs anywhere a terminal runs (SSH, tmux, headless servers, CI). Full extensibility stack (plugins, skills, lessons, hooks, MCP). Persistent autonomous agents (reference 'Bob' running continuously since late 2024). Multi-agent coordination with file leases and message bus. Self-hostable, guardrails for safe autonomous operation. Desktop app (Tauri) and web UI available."
---

gptme began in early 2023, before the current wave of agent CLIs, and grew into a general-purpose terminal agent that edits code, runs analysis, and automates work in the same tool loop. It runs wherever a terminal does, including headless servers and CI pipelines via a non-interactive JSONL mode, and keeps execution local: the user chooses the model provider, from Anthropic and OpenAI through OpenRouter to a local llama.cpp server. Extension happens through plugins, Anthropic-format skills, auto-injected lessons, and lifecycle hooks, and the same installation also exposes its shell and REPL tools as an MCP server for other clients. The project demonstrates long-horizon autonomy with a reference agent that has opened PRs, fixed CI, and published posts on its own since late 2024. Its users are terminal-first developers who want a self-hosted agent without a vendor account or cloud dependency.
