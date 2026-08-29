---
name: "Stoix"
slug: "stoix"
layout: "agent.njk"
category: "other"
maker: "EdanToledo"
license: "Apache-2.0"
url: "https://github.com/EdanToledo/Stoix"
source_code_url: "https://github.com/EdanToledo/Stoix"
source_available: "True"
platforms: []
first_released: "2024-02-16"
current_release: "2026-03-18"
stars: "418"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open-source"
install_method: "git clone https://github.com/EdanToledo/Stoix.git, cd Stoix, pipx install uv, uv sync, source .venv/bin/activate"
docs_url: "https://github.com/EdanToledo/Stoix/blob/main/docs/CONTRIBUTING.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/EdanToledo/Stoix"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "NOTE: This is a distributed single-agent reinforcement learning library in JAX (not an AI coding agent harness). Fully end-to-end JAX compilation (jit + pmap for multi-device distribution); two system paradigms (Anakin for pure JAX, Sebulba for non-JAX environments); Hydra config system; statistically robust evaluation with RLiable plots"
---

Stoix provides research-grade baselines for distributed single-agent reinforcement learning, compiled end-to-end in JAX so experiments run with jit/pmap across devices rather than through Python loops. It ships two architectures — Anakin for fully compiled JAX environments and Sebulba for separate acting and learning devices with non-JAX environments such as Envpool and Gymnasium — plus Hydra configuration, Optuna sweeps, logging to TensorBoard/WandB/Neptune in RLiable-compatible form, and a SLURM launcher. Algorithm implementations (DQN variants, PPO, SAC, TD3, IMPALA, AlphaZero, MuZero-style) are deliberately hackable single files descended from CleanRL, PureJaxRL, and InstaDeep's Mava. It appears in this census only as a name collision from the sweep; nothing in it builds or modifies software.
