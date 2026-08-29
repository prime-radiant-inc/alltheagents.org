---
name: "Rpm-Ai-Agent"
slug: "rpm-ai-agent"
layout: "agent.njk"
category: "other"
maker: "teldridge11"
license: null
url: "https://github.com/teldridge11/RPM-AI-Agent"
source_code_url: "https://github.com/teldridge11/RPM-AI-Agent"
source_available: "True"
platforms: []
first_released: "2017-09-23"
current_release: "2018-07-07"
stars: null
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (three-layer rule-based pattern matcher; no LLM involved)"
pricing: null
install_method: "git clone https://github.com/teldridge11/RPM-AI-Agent.git; run python Test.py from Agent directory"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Three-layered knowledge-based agent mimicking human reasoning for Raven's Progressive Matrices; 91.7% accuracy on basic 2x2 problems, 85% on unseen problem sets. Not LLM-based - custom pattern-matching architecture."
---

The repository documents a coursework- or research-scale exploration of whether structured, human-like reasoning stages can match learned models on Raven's Progressive Matrices, a standard test of abstract visual reasoning. Each problem image is decomposed, candidate answers are filtered against the patterns induced from the prompt matrix, and remaining options are ranked by attribute similarity, all with Pillow-based image processing in Python rather than any neural component. Reported accuracy — strong on basic 2x2 items, weak on challenge sets — is included with paper PDFs in the repo. It has no license file, no issues or forks, and twenty-two commits, marking it as an inactive personal artifact. Its relevance to this census is as a namesake only: nothing here touches coding agents.
