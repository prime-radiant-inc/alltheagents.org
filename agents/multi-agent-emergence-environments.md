---
name: "multi-agent-emergence-environments"
slug: "multi-agent-emergence-environments"
layout: "agent.njk"
category: "other"
maker: "openai"
license: "MIT"
url: "https://github.com/openai/multi-agent-emergence-environments"
source_code_url: "https://github.com/openai/multi-agent-emergence-environments"
source_available: "Yes"
platforms: []
first_released: "2019-08-12"
current_release: "2024-07-30"
stars: "1814"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "github_topic4"
what_makes_it_special: "Environment generation code for the paper 'Emergent Tool Use From Multi-Agent Autocurricula', featuring specific multi-agent environments like Hide and Seek, Box locking, Blueprint Construction, and Shelter Construction."
---

This repository is the environment code behind OpenAI's 2019 multi-agent reinforcement-learning research, famous for hide-and-seek agents that emergently learned to use boxes as ramps and shelters. It provides MuJoCo-based physics environments — hide and seek in several variants, box locking, blueprint construction, shelter construction — that researchers use to study autocurricula and emergent behaviors; 'multi-agent' here means competing reinforcement learners, not LLM-based coding systems. OpenAI archived the repository (read-only as of the archive date), the code targets Python 3.6 on long-obsolete Ubuntu and macOS versions, and no updates are expected. Its presence in a coding-agent census is a pure name collision — the census category 'other' absorbs it as research tooling unrelated to software development.
