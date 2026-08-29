---
name: "Smol Developer"
slug: "smol-developer"
layout: "agent.njk"
category: "agent"
maker: "smol-ai"
license: "MIT"
url: "https://github.com/smol-ai/developer"
source_code_url: "https://github.com/smol-ai/developer"
source_available: "True"
platforms: []
first_released: "2023-05-13"
current_release: "2024-04-07"
stars: "12186"
language: "Python"
homepage: "https://twitter.com/SmolModels"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI (GPT-4-0613, GPT-3.5-turbo-0613)"
pricing: "open-source"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "flatlogic"
  - "e2b"
  - "brad"
  - "brandonhimpfen"
  - "ishandutta"
what_makes_it_special: "Human-centric AI scaffolding agent that generates entire codebases from a product spec. Whole-program coherence via an intermediate shared_dependencies.md step where GPT maintains cross-file consistency. First embeddable developer agent library with importable functions (plan, specify_file_paths, generate_code). Markdown-is-all-you-need philosophy. Three usage modes: Git repo (CLI), library (Python import), API (Agent Protocol server)."
---

Smol Developer addressed the failure mode of early code-generation agents, where independently generated files hallucinated incompatible interfaces. Its pipeline plans a shared dependencies document, uses OpenAI function calling to guarantee a valid file list, then generates each file with that document pinned into the prompt so the model effectively talks to itself across files. Humans stay in the loop by running the output, pasting errors back into the prompt, or using debugger.py to feed the whole codebase plus an error for fix suggestions. It shipped as a repo, an importable pip library, and an Agent Protocol API server, and at 12k stars it was one of the defining scaffolding agents of the 2023 GPT-4 era. Development stopped around 2024 and the code still targets the gpt-4-0613 era.
