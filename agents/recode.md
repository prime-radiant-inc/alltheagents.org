---
name: "ReCode"
slug: "recode"
layout: "agent.njk"
category: "other"
maker: "FoundationAgents"
license: "MIT"
url: "https://github.com/FoundationAgents/ReCode"
source_code_url: "https://github.com/FoundationAgents/ReCode"
source_available: "True"
platforms: []
first_released: "2025-10-27"
current_release: "2026-04-21"
stars: "562"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI-compatible"
pricing: "open-source"
install_method: "pip"
docs_url: "https://arxiv.org/abs/2510.23564"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/FoundationAgents/ReCode"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Unifies planning and action into a single representation using recursive code generation, allowing dynamic adaptation from strategic thinking to concrete actions with universal granularity control"
---

ReCode is a research framework from the FoundationAgents org (the MetaGPT team) testing a specific thesis: that planning and acting should not be separate phases in an LLM agent. It represents a plan as a tree of placeholder functions in a Python program, then lets the model recursively expand each placeholder into finer-grained executable calls, with a shared constrained executor maintaining state and validating code as nodes run. Because the representation is uniform, the agent moves fluidly between strategic decomposition and concrete action without switching modes, which the paper calls universal granularity control. Evaluations on ALFWorld, WebShop, and ScienceWorld report a 60.8 average score, roughly 10.5 points above ReAct, CodeAct, and AdaPlanner baselines, with a fine-tuned Qwen2.5-7B variant reaching 70.4%. The code is a research artifact — fourteen commits, acknowledged incomplete requirements, and benchmark-specific environment conflicts — intended for researchers reproducing the paper rather than for production use.
