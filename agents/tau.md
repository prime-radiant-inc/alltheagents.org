---
name: "Tau"
slug: "tau"
layout: "agent.njk"
category: "agent"
maker: "huggingface"
license: "MIT"
url: "https://github.com/huggingface/tau"
source_code_url: "https://github.com/huggingface/tau"
source_available: "Yes"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-11"
current_release: "2026-08-18"
stars: "2368"
language: "Python"
homepage: "http://twotimespi.dev/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, OpenRouter, Hugging Face, local"
pricing: "open-source"
install_method: "pip"
docs_url: "https://twotimespi.dev/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/tau-ai/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Small, readable terminal coding agent — a Python port of Pi's minimalist coding agent — that reads, edits, and runs commands with durable JSONL sessions; also serves as a teaching project for how coding-agent systems are built."
---

Tau is Hugging Face's Python port of the Pi minimalist coding agent, published both as a usable terminal agent and as a reference for how coding agents are constructed. The package splits into tau_ai (a provider-neutral event stream over OpenAI, Anthropic, Codex, OpenRouter, HF, and OpenAI-compatible endpoints), tau_agent (the harness loop, tools, and durable JSONL sessions with resume and branching), and tau_coding (the Textual TUI, one-shot print mode, file/shell tools, skills, and AGENTS.md project instructions). Context accounting with manual and automatic compaction keeps long sessions coherent, and providers are configured through a catalog file rather than code. Because the 'brain' is decoupled from the interface, the project doubles as teaching material — the docs site walks through the architecture — and the README states the goal of showing how coding agents work. Developers who want a small, inspectable agent they can read and modify, rather than a maximalist product, are the audience.
