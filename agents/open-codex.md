---
name: "Open Codex"
slug: "open-codex"
layout: "agent.njk"
category: "agent"
maker: "codingmoh"
license: "MIT"
url: "https://github.com/codingmoh/open-codex"
source_code_url: "https://github.com/codingmoh/open-codex"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-03-29"
current_release: "2025-07-07"
stars: "696"
language: "Python"
homepage: "https://github.com/codingmoh/open-codex"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "local models (e.g. phi-4-mini) and Ollama (llama3, mistral) via localhost:11434; no cloud APIs"
pricing: "open-source"
install_method: "brew tap codingmoh/open-codex && brew install open-codex; or pipx install open-codex; or clone + pip install ."
docs_url: "https://github.com/codingmoh/open-codex#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/codingmoh/open-codex"
maintained: "dormant"
sources:
  - "hackernews"
what_makes_it_special: "Runs 100% locally with no OpenAI API key, translating natural language into shell commands via small local models or Ollama, and executes nothing without explicit per-command user confirmation."
---

Most terminal coding assistants require cloud API keys, which blocks offline use and raises cost concerns for simple tasks. Open Codex takes the opposite position: a lightweight Python CLI inspired by OpenAI Codex that converts natural-language requests into shell commands using local models or an Ollama backend such as llama3 or mistral on localhost:11434. The interaction is deliberately one-shot — prompt, suggested command, then confirm, copy, or abort — with execution gated behind explicit user approval, so nothing runs without consent. It installs via Homebrew, pipx, or Debian packaging and runs on macOS, Linux, and Windows. The project is early-stage (36 commits, 696 stars), with interactive chat, TUI, function calling, and a plugin system listed as unimplemented future plans. It fits users who want an offline, zero-API-cost natural-language shell helper rather than a full agentic harness.
