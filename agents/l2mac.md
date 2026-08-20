---
name: "L2MAC"
slug: "l2mac"
layout: "agent.njk"
category: "agent"
maker: "samholt"
license: "MIT"
url: "https://github.com/samholt/l2mac"
source_code_url: "https://github.com/samholt/l2mac"
source_available: True
platforms: []
first_released: "2024-03-08"
current_release: "2024-12-27"
stars: "158"
language: "Python"
homepage: "https://samholt.github.io/L2MAC/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: null
model_providers: "OpenAI (gpt-4o), Azure, others via ApiType config"
pricing: null
install_method: "pip install --upgrade l2mac"
docs_url: "https://samholt.github.io/L2MAC/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/samholt/l2mac"
maintained: "abandoned"
sources:
  - "e2b"
what_makes_it_special: "First practical LLM-based von Neumann-architecture stored-program automatic computer; uses a self-bootstrapped prompt-program where each instruction step is loaded into a new LLM agent to execute, with persistent file-store memory, error correction, and unit test generation; 90.2% Pass@1 on HumanEval; accepted at ICLR 2024."
---

First practical LLM-based von Neumann-architecture stored-program automatic computer; uses a self-bootstrapped prompt-program where each instruction step is loaded into a new LLM agent to execute, with persistent file-store memory, error correction, and unit test generation; 90.2% Pass@1 on HumanEval; accepted at ICLR 2024.
