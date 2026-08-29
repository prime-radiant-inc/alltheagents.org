---
name: "PrivateCode"
slug: "privatecode"
layout: "agent.njk"
category: "agent"
maker: "Legorobotdude"
license: "MIT"
url: "https://github.com/Legorobotdude/PrivateCode"
source_code_url: "https://github.com/Legorobotdude/PrivateCode"
source_available: "True"
platforms: []
first_released: "2025-03-06"
current_release: "2025-05-12"
stars: "36"
language: "Python 3.6+"
homepage: "https://www.vibecoder.gg/"
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "no"
plan_mode: "True"
model_providers: "Ollama (local LLMs only)"
pricing: "Free / open-source"
install_method: "git clone; pip install -r requirements.txt; ensure Ollama running locally; ollama pull codellama"
docs_url: "https://www.vibecoder.gg/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Legorobotdude/PrivateCode"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Privacy-first terminal coding assistant (VibeCoder) running entirely on local Ollama models with no data sent to external services; uses DuckDuckGo for untracked web searches and URL content extraction; partial file reading with line ranges for token efficiency; intelligent file editing with diff preview; safe command execution; AI thinking blocks (toggleable reasoning display); plan:/vibecode: mode breaks complex tasks into executable JSON-formatted steps with interactive confirmation at each step; persistent conversation history."
---

PrivateCode exists for developers who want AI coding help without sending proprietary code to a cloud provider. It runs entirely against local Ollama models, with DuckDuckGo search and URL extraction as the only optional external calls, chosen because that engine does not track queries. Work happens through explicit commands — search:, edit:, run:, create:, plan: — and the vibecode mode decomposes a task into JSON steps that execute one at a time with user approval, so nothing runs without review. Edits produce .bak backups and colored diff previews, and dangerous command prefixes trigger warnings before execution. It is a single-file Python tool aimed at developers on offline machines or anyone unwilling to leak code to hosted models.
