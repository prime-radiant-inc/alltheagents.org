---
name: "gpt-coder"
slug: "gpt-coder"
layout: "agent.njk"
category: "agent"
maker: "alicheg"
license: "MIT"
url: "https://github.com/alicheg/gpt-coder"
source_code_url: "https://github.com/alicheg/gpt-coder"
source_available: "True"
platforms: []
first_released: "2023-04-12"
current_release: "2025-12-25"
stars: "26"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI"
pricing: "Free / open-source"
install_method: "git clone, pip install -r requirements.txt, configure .env with OPENAI_API_KEY, run python src/main.py"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/alicheg/gpt-coder"
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "Self-supervising AI code generation tool that iteratively generates, refines, compiles, and tests solutions against extracted test cases until they meet expected criteria."
---

GPT Coder demonstrates the test-feedback loop that later defined agentic coding, compressed into a single Python script: GPT generates a coding challenge, a solution, and test cases, then the tool compiles, executes, and tests the solution against them, feeding failures back until they pass. The pipeline is fixed rather than open-ended — there is no general tool use, file editing, or interactivity — and configuration is just an OPENAI_API_KEY in a .env file. One commit, no releases, and 26 stars mark it as a ChatGPT-era experiment published in April 2023 and never developed further. Its value now is historical: an early example of test-driven self-refinement that later harnesses industrialized.
