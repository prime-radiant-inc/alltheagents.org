---
name: "SWE-Dev"
slug: "swe-dev"
layout: "agent.njk"
category: "other"
maker: "THUDM"
license: "MIT"
url: "https://github.com/THUDM/SWE-Dev"
source_code_url: "https://github.com/THUDM/SWE-Dev"
source_available: "True"
platforms: []
first_released: "2025-03-21"
current_release: "2025-07-21"
stars: "65"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Qwen, GPT-4o (configurable)"
pricing: "Free / open source (MIT)"
install_method: "Python packaging (setup.py/pyproject.toml) + Docker (docker build -t swedev-evaluator:latest .)"
docs_url: "https://arxiv.org/abs/2506.07636"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/THUDM/SWE-Dev-32B"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "SWE agent focused on training and inference scaling; pipeline to synthesize test cases and scale up agent trajectories for training data; ACL'25 Findings paper"
---

SWE-Dev, from Tsinghua's THUDM lab, tackles the data bottleneck for open software-engineering agents. Its pipeline crawls top PyPI repositories, mines issues and PRs into tasks, generates Gherkin-style behavior descriptions, and synthesizes test cases with an optional revision pass driven by traceback errors, validating each case in Docker so that fail-to-pass tests prove the task is real. The same machinery scales inference: giving a single run a larger interaction budget lifted SWE-Dev-32B from 34.0% to 36.6% on SWE-bench Verified, with SWE-Dev-7B at 23.4%. Configuration is centralized in a YAML schema, and both trained models and trajectory datasets are published on Hugging Face. Agent-training researchers use it as a recipe for building test-verified training data without human annotation.
