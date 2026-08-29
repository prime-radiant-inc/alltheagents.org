---
name: "Multiagent Debate"
slug: "multiagent-debate"
layout: "agent.njk"
category: "other"
maker: "composable-models"
license: null
url: "https://github.com/composable-models/llm_multiagent_debate"
source_code_url: "https://github.com/composable-models/llm_multiagent_debate"
source_available: "True"
platforms: []
first_released: "2023-05-23"
current_release: "2025-04-24"
stars: "545"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "git clone; install requirements.txt; run python scripts (e.g. python gen_math.py)"
docs_url: "https://composable-models.github.io/llm_debate/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "e2b"
what_makes_it_special: "Official implementation of the ICML 2024 paper 'Improving Factuality and Reasoning in Language Models through Multiagent Debate', using multiagent debate to enhance factuality and reasoning."
---

This repository holds the code behind one of the most-cited LLM-collaboration papers: multiple model instances propose, critique, and refine answers across rounds of debate, and the final answer's factuality improves over single-model baselines. The four task directories cover arithmetic and math problems, grade-school math, biography generation, and MMLU multiple choice, each runnable as standalone scripts against OpenAI models. The implementation is explicitly preliminary — the README promises future task releases that never arrived — and the repository carries no license file, so reuse beyond reading is technically unlicensed. It has served as the reference point for a wave of follow-up work, including community alternatives like LLM-Agora that extended debate to open-source models. The code is an archival research artifact from 2023: no coding tools, no agentic loop over software, and no maintenance since 2025.
