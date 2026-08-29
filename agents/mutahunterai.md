---
name: "MutahunterAI"
slug: "mutahunterai"
layout: "agent.njk"
category: "agent"
maker: "codeintegrity-ai"
license: "AGPL-3.0"
url: "https://github.com/codeintegrity-ai/mutahunter"
source_code_url: "https://github.com/codeintegrity-ai/mutahunter"
source_available: "True"
platforms: []
first_released: "2024-06-21"
current_release: "2025-04-17"
stars: "299"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI (GPT-4o, gpt-4o-mini)"
pricing: "open-source"
install_method: "pip install https://github.com/codeintegrity-ai/mutahunter"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "Open-source, language-agnostic LLM-based mutation testing tool. It generates code mutants using LLMs and runs test commands to measure mutation coverage (killed vs survived mutants)."
---

Mutahunter modernizes mutation testing, which traditionally relies on fixed operator catalogs that miss semantically meaningful mutants. Instead, an LLM reads the code under test and generates context-aware mutants — subtle behavioral variations a hand-written operator table would never produce — then the harness executes the project's test command against each mutant and classifies outcomes as killed, survived, timeout, or compile-error, yielding a mutation coverage score that reflects genuine test strength. The tool is language-agnostic by construction: it wraps whatever test command the project uses (a Maven build, pytest, anything invocable from the CLI) rather than implementing per-language integration. Per-run output includes LLM cost, making the expense of mutation testing explicit and budgetable. It installs via pip from GitHub and targets developers and QA teams assessing whether their test suites actually detect defects rather than merely execute code. Activity has slowed since early 2025, with the project sitting at a modest community size under AGPL-3.0.
