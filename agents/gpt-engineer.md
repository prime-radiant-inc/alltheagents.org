---
name: "GPT Engineer"
slug: "gpt-engineer"
layout: "agent.njk"
category: "agent"
maker: "AntonOsika"
license: "MIT"
url: "https://github.com/AntonOsika/gpt-engineer"
source_code_url: "https://github.com/AntonOsika/gpt-engineer"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2023-04-29"
current_release: "2025-05-14"
stars: "55133"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no (customizable preprompts only)"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI, Anthropic"
pricing: "open-source"
install_method: "pip"
docs_url: "https://gpt-engineer.readthedocs.io/en/latest/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/gpt-engineer-org/gpt-engineer"
maintained: "dead"
sources:
  - "flatlogic"
  - "brandonhimpfen"
  - "tiennm"
what_makes_it_special: "Self-described as 'The OG code generation experimentation platform'; an early tool for specifying software in natural language and having AI write/execute code, a precursor to lovable.dev and gptengineer.app."
---

GPT Engineer was one of the first tools to demonstrate specifying software in natural language and having an LLM write, execute, and improve the resulting code, spawning the wave of prompt-to-app products and directly preceding lovable.dev and gptengineer.app. Its design was deliberately hackable: a preprompts folder let users customize the agent's identity and memory, vision models accepted UX or architecture diagrams, and a bench CLI ran custom agents against APPS and MBPP benchmarks. It supported OpenAI, Azure, Anthropic, and local open-source models, with an improve-existing-code mode and Docker support. The repository was archived by its owner on April 22, 2026, with the README redirecting CLI users to aider and the commercial line continuing as gptengineer.app and lovable.dev.
