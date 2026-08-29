---
name: "Devika"
slug: "devika"
layout: "agent.njk"
category: "agent"
maker: "stitionai"
license: "MIT"
url: "https://github.com/stitionai/devika"
source_code_url: "https://github.com/stitionai/devika"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2024-03-21"
current_release: "2025-09-25"
stars: null
language: "Python"
homepage: "https://winfunc.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "Claude 3, GPT-4, Gemini, Mistral, Groq, Ollama"
pricing: "Free / open-source"
install_method: "git clone, uv venv, uv pip install -r requirements.txt, python devika.py"
docs_url: "https://github.com/stitionai/devika/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jqueryscript"
  - "flatlogic"
  - "e2b"
  - "jim"
  - "brandonhimpfen"
what_makes_it_special: "First open-source implementation of an agentic software engineer; open-source alternative to Devin (Cognition AI). README banner now directs users to its successor, Opcode."
---

Devika demonstrated in March 2024 that a Devin-style software engineer could be assembled from open components: high-level objectives are decomposed into steps, each step gets focused web research via extracted keywords, and code is written against the plan while agent state is visualized in a chat UI. It supported Claude 3, GPT-4, Gemini, Mistral, Groq, and local Ollama models, and organized work into browser-managed projects. The project was always labeled experimental, and its maintainers eventually moved to a successor called Opcode. It remains historically important as the template many later open-source agents copied, but the codebase itself is no longer developed.
