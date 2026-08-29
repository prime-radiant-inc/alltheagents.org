---
name: "AgentCoder"
slug: "agentcoder"
layout: "agent.njk"
category: "agent"
maker: "huangd1999"
license: "MIT"
url: "https://github.com/huangd1999/AgentCoder"
source_code_url: "https://github.com/huangd1999/AgentCoder"
source_available: "True"
platforms: []
first_released: "2024-03-20"
current_release: "2025-11-18"
stars: "388"
language: "Python"
homepage: "https://github.com/huangd1999/AgentCoder"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, CodeGeeX"
pricing: "open-source"
install_method: "git clone (with CodeGeeX submodule), pip install -r requirements.txt, add API key to .env"
docs_url: "https://github.com/huangd1999/AgentCoder#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/huangd1999/AgentCoder"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent code generation framework with three specialized agents (programmer, test designer, test executor); independent test case generation and iterative code refinement through multiagent collaboration."
---

AgentCoder is a research codebase from huangd1999 that studies whether splitting code generation across specialized agents improves output quality, evaluated on the HumanEval and MBPP benchmarks. A programmer agent writes code, a test-designer agent independently generates test cases the programmer never sees, and a test executor runs them, feeding failures back for iterative refinement. The framework is deliberately modular so different LLMs can be swapped in (OpenAI models and CodeGeeX are wired up), but it is a benchmark-oriented research codebase — clone, install requirements, add an API key — not a developer product. Its users are NLP and code-generation researchers reproducing multi-agent generation experiments.
