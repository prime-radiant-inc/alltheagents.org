---
name: "Mava"
slug: "mava"
layout: "agent.njk"
category: "other"
maker: "instadeepai"
license: "Apache-2.0"
url: "https://github.com/instadeepai/Mava"
source_code_url: "https://github.com/instadeepai/Mava"
source_available: "True"
platforms: []
first_released: "2021-03-30"
current_release: "2026-05-26"
stars: "927"
language: "Python (JAX)"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Research-friendly codebase for distributed multi-agent reinforcement learning (MARL) in JAX with single-file implementations built for rapid research iteration; end-to-end JIT compilation via Anakin architecture."
---

Mava exists because multi-agent RL research moves faster when algorithms fit in single readable files that researchers clone and modify rather than install. InstaDeep's library provides exactly that for JAX: single-file implementations of IPPO, MAPPO, QMIX, IQL, MAT, Sable and newer methods, distributed architectures (Anakin/Sebulba) that JIT-compile the entire training loop, and wrappers for standard MARL environments such as Robot Warehouse, Level-based Foraging, and SMAC. Reinforcement-learning researchers at InstaDeep and in the wider MARL community are the users, with the codebase tracking recent papers (GPO/MagPO, Sable) through sustained maintenance. It is an RL research library with no coding-agent functionality.
