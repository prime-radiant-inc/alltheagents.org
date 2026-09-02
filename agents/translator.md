---
name: "Translator"
slug: "translator"
layout: "agent.njk"
category: "other"
maker: "2389-research"
license: null
url: "https://github.com/2389-research/translator"
source_code_url: "https://github.com/2389-research/translator"
source_available: "True"
platforms:
  - "CLI"
first_released: null
current_release: null
stars: "8"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "BYOK"
install_method: "pip install"
docs_url: null
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "LLM-powered document translation CLI that uses a multi-stage pipeline (translate, edit, critique/revise) with special handling for markdown + YAML frontmatter. Uses OpenAI's API with tiktoken for token management and pycountry for language codes."
---

Translator is an LLM-powered document translation CLI, not a coding agent. It runs documents through a multi-stage pipeline — translate, edit, then critique and revise — so a draft is not the final output, and it has special handling for markdown with YAML frontmatter so structured metadata survives translation intact. It talks to OpenAI's API, uses tiktoken for token management, and pycountry for language codes. The audience is anyone who needs high-quality, pipeline-driven document translation from the command line with their own OpenAI key, and it is listed here because it is a 2389-research tool that is not an agent and should not be mistaken for one.
