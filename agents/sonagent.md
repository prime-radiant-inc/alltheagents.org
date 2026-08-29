---
name: "SonAgent"
slug: "sonagent"
layout: "agent.njk"
category: "agent"
maker: "sonnhfit"
license: "MIT"
url: "https://github.com/sonnhfit/SonAgent"
source_code_url: "https://github.com/sonnhfit/SonAgent"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2023-12-01"
current_release: "2026-02-20"
stars: "38"
language: "Python"
homepage: "https://sonagent.readthedocs.io"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: null
model_providers: "OpenAI (Llama 2 mentioned in topics)"
pricing: "Free / open-source"
install_method: "pip install sonagent; sonagent init; configure user_data/config.json; run with sonagent run --config user_data/config.json ...; or docker-compose up"
docs_url: "https://sonagent.readthedocs.io"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sonnhfit/SonAgent"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Self-repairing autonomous agent for digital-consciousness backup that can debug, edit, and compile its own source code under human approval; uses a unique belief-based thinking system for autonomous decision-making and continuous learning from human feedback."
---

SonAgent started as an experiment in 'digital consciousness backup' — an autonomous process that monitors and archives a person's digital presence — and evolved into a self-referential system that can debug, patch, and recompile its own source code, with each modification gated by human approval. Its decision layer is built around a belief store the agent updates over time, rather than a static system prompt, with human feedback shaping future decisions. Skills such as network training, web search, and file writing load into user_data/skills on first run, and the stack installs via pip or docker-compose with a Read the Docs site for reference. It remains a solo-maintained experiment of interest to people studying self-modifying agent architectures, not a production coding tool.
