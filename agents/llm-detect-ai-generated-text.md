---
name: "Llm-Detect-Ai-Generated-Text"
slug: "llm-detect-ai-generated-text"
layout: "agent.njk"
category: "other"
maker: "pinskyrobin"
license: null
url: "https://github.com/pinskyrobin/LLM---Detect-AI-Generated-Text"
source_code_url: "https://github.com/pinskyrobin/LLM---Detect-AI-Generated-Text"
source_available: "Source-visible (no OSS license)"
platforms: []
first_released: "2024-01-18"
current_release: "2024-01-18"
stars: null
language: "Jupyter Notebook"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "jim"
what_makes_it_special: "It bundles the Kaggle competition data with the DAIGT V2 training set and a modified test_essays.csv, so a baseline detection notebook can be debugged offline with more than the competition's three test rows."
---


The repository supports offline development of a Kaggle 'LLM - Detect AI Generated Text' competition solution: the official test file carried only three rows, too few to exercise the notebook's final evaluation block, so training essays were partially copied into a modified test_essays.csv to make local debugging meaningful. A baseline classifier notebook, adapted from a public Kaggle notebook, runs against the bundled competition and DAIGT V2 datasets. It exists as personal competition scaffolding for detecting machine-written text, not as any kind of coding tool, and it carries no license with only four commits of activity.
