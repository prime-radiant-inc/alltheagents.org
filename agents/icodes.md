---
name: "Icodes"
slug: "icodes"
layout: "agent.njk"
category: "other"
maker: "a115"
license: "CC0-1.0"
url: "https://github.com/a115/iCODES"
source_code_url: "https://github.com/a115/iCODES"
source_available: "True"
platforms: []
first_released: "2024-03-31"
current_release: "2024-05-19"
stars: "6"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI"
pricing: "Free / open-source (CC0)"
install_method: "pip install icodes; or clone repo and use Poetry: git clone https://github.com/a115/iCODES.git then poetry install"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/a115/iCODES.git"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "LLM-powered Git archeology tool (Intelligent Commit Ontology Distiller and Enhanced Search) that analyzes and indexes Git commit histories in context, summarizing commit intents and enabling semantic search. Suggests commit messages from staged changes and extracts insights/trends from code evolution history."
---

iCODES addresses a narrow problem: Git histories record what changed but rarely why. The tool walks a repository's commit history, sends each commit to an LLM for intent summarization, and stores the results in an index that supports filtered and semantic search over authors, paths, dates, and meanings. Secondary commands suggest commit messages from staged changes and surface trends across code evolution. There is no agentic loop — the LLM performs one-shot analysis per commit — and the project is single-maintainer hobby code on OpenAI's API, last touched in May 2024.
