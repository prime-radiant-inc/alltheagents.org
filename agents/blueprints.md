---
name: "Blueprints"
slug: "blueprints"
layout: "agent.njk"
category: "other"
maker: "sublayerapp"
license: "MIT"
url: "https://github.com/sublayerapp/blueprints"
source_code_url: "https://github.com/sublayerapp/blueprints"
source_available: "True"
platforms:
  - "IDE"
first_released: "2024-01-29"
current_release: "2024-09-09"
stars: "61"
language: "Ruby"
homepage: "https://blueprints.sublayer.com"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (GPT-4), Google (Gemini)"
pricing: "open-source"
install_method: "Clone repo, bundle install, bin/rails db:create, bin/rails db:migrate, bin/rails tailwindcss:build, bin/rails s"
docs_url: "https://blueprints.sublayer.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sublayerapp/blueprints"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Stores chunks of code (blueprints) and uses them as a base for LLMs (GPT-4/Gemini) to generate new code based on patterns in your codebase; editor plugins for Vim, VSCode, IntelliJ, SublimeText"
---

Blueprints emerged from the Sublayer team's observation that LLM code generation drifts from a team's idioms unless it is grounded in that team's actual code. The system is a self-hosted Rails app where developers save code chunks as named, described 'blueprints'; each save triggers GPT-4 to name and describe the chunk, and its vector embedding lands in Postgres via pgvector. Later, from Vim, VS Code, IntelliJ, or Sublime Text, a developer highlights code, and the plugin finds the most similar blueprint, sends its code and description to GPT-4 or Gemini, and splices the generated variant back over the selection. This turns a codebase's own patterns into reusable generation context, predating the now-common embedding-backed codebase retrieval in coding agents. Development has been dormant since 2024, with 61 stars and no recent commits, but it remains a readable example of retrieval-grounded code generation.
