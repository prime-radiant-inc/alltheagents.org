---
name: "LocoTrainer"
slug: "locotrainer"
layout: "agent.njk"
category: "agent"
maker: "LocoreMind"
license: "MIT"
url: "https://github.com/LocoreMind/LocoTrainer"
source_code_url: "https://github.com/LocoreMind/LocoTrainer"
source_available: "True"
platforms: []
first_released: "2026-03-13"
current_release: "2026-03-13"
stars: "117"
language: "Python"
homepage: "https://locoremind.com/blog/locotrainer"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "False"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI-compatible (DashScope, OpenRouter, llama.cpp, vLLM)"
pricing: "Free/open-source; local GGUF deployment at zero API cost"
install_method: "pip install locotrainer (or setup scripts / git clone)"
docs_url: "https://github.com/LocoreMind/LocoTrainer"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/locotrainer/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "4B-parameter MS-SWIFT domain expert agent distilled from Qwen3-Coder-Next; simulates a Claude Code-style agent environment; trained on 361K samples with 32K context; runs locally via GGUF quantization at zero API cost; auto-clones ms-swift on first run; key insight that absolute paths + tolerant tool argument parsing yields reliable agent behavior."
---

LocoTrainer addresses a narrow, recurring need: engineers working with the MS-SWIFT training framework need codebase analysis and structured reports, and a frontier-model agent is expensive for that repetitive task. The accompanying model was trained on 361,830 samples (agent trajectories, MS-SWIFT knowledge, and project structure paths) over roughly 25 hours on 8x H100s, and the surrounding framework replicates the Claude Code-style environment the model saw in training, down to absolute paths and system reminders, because that fidelity is what makes small-model tool calling reliable. The agent loop reads, searches, and analyzes the MS-SWIFT repository and emits markdown reports, running locally through GGUF quantization at zero API cost or through OpenAI-compatible providers. ML engineers fine-tuning with MS-SWIFT are the intended users.
