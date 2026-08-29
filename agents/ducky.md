---
name: "Ducky"
slug: "ducky"
layout: "agent.njk"
category: "other"
maker: "ParthSareen"
license: "MIT"
url: "https://github.com/ParthSareen/ducky"
source_code_url: "https://github.com/ParthSareen/ducky"
source_available: "True"
platforms: []
first_released: "2023-12-14"
current_release: "2026-02-04"
stars: "26"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Ollama"
pricing: "Free / open-source"
install_method: "uv tool install rubber-ducky, or uvx rubber-ducky"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ParthSareen/ducky"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Inline terminal companion that turns natural language into bash commands. Features a 'Crumbs' system for saving and reusing command shortcuts with argument substitution, piped input support, interactive REPL with rich keyboard shortcuts, and clipboard support across macOS/Windows/Linux. Works with both local and cloud Ollama models."
---

Ducky sits between the shell prompt and an LLM: describe what you want in English, get a concrete bash command back, inspect it, and run it — the human stays in the loop at every step. Rather than shipping its own models, it rides a local or cloud Ollama endpoint, so it works offline with qwen3-class models and costs nothing beyond compute. Its Crumbs system turns one-off suggestions into persistent parameterized shortcuts (with $variable substitution), which turns ad-hoc LLM answers into a personal command library. It is built for terminal-comfortable users who want command synthesis and explanation without a full agentic coding loop.
