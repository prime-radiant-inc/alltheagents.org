---
name: "FLEX"
slug: "flex"
layout: "agent.njk"
category: "other"
maker: "GenSI-THUAIR"
license: "MIT"
url: "https://github.com/GenSI-THUAIR/FLEX"
source_code_url: "https://github.com/GenSI-THUAIR/FLEX"
source_available: "True"
platforms: []
first_released: "2025-11-03"
current_release: "2026-06-09"
stars: "86"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI-compatible"
pricing: null
install_method: "cd FLEX && uv pip install -e ."
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_topic2"
what_makes_it_special: "Research codebase implementing Forward Learning from Experience, where agents improve via an evolvable experience library rather than modifying model parameters. Evaluated on AIME25 (math), USPTO-50k (chemical retrosynthesis), and ProteinGym (protein fitness). Not a software-engineering coding agent harness; it's a scientific reasoning agent research framework."
---

FLEX is the official codebase for a Tsinghua AIR paper (arXiv:2511.06449, November 2025) proposing Forward Learning from Experience as an alternative to fine-tuning: an actor agent solves tasks, a critic distills each trajectory into structured experiences, an updater deduplicates and filters the library, and relevant experiences are retrieved at inference time to improve future performance. The release evaluates the paradigm on AIME25 (Olympiad math), USPTO-50k (retrosynthesis planning), and ProteinGym (protein fitness prediction) using ReAct-style agents built on Smolagents with Phoenix tracing. As a paper artifact it has few commits and no product ambitions; its audience is researchers studying non-gradient agent improvement, not software developers.
