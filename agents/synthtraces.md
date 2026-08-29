---
name: "synthtraces"
slug: "synthtraces"
layout: "agent.njk"
category: "other"
maker: "julien-c"
license: "MIT"
url: "https://github.com/julien-c/synthtraces"
source_code_url: "https://github.com/julien-c/synthtraces"
source_available: "True"
platforms: []
first_released: "2026-06-03"
current_release: "2026-06-04"
stars: "59"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Remote hosted open models (DeepSeek-V4-Pro, gpt-oss-120b, Qwen3.6-27B, GLM-5.1, etc.), Local models via llama.cpp"
pricing: "Free/open source"
install_method: "Node/TypeScript project (pnpm); runs the Pi coding agent per session"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/datasets/julien-c/synthtraces"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Generates synthetic coding agent session traces by pairing two models: a remote open model as the coding agent and a local llama.cpp model as the user, across 20 codebases x 20 starting questions = 24,000 total sessions."
---

Synthtraces exists to supply realistic multi-turn interaction data for coding-agent research without proprietary logs. Each generated session boots the Pi coding agent with read, write, edit, and bash tools inside one of twenty real codebases (transformers, diffusers, lerobot, candle, and others), pairs it with a remotely hosted open model, and has a local llama.cpp model play the user starting from one of twenty seed questions such as 'How is CI set up in this repo?'. The released dataset is the cross product of 20 agent models, 3 local user models, 20 codebases, and 20 questions — 24,000 sessions — published on Hugging Face alongside this small TypeScript generator. Because both sides are models, the traces capture authentic tool-use dynamics (edits, shell runs, follow-up questions) without any human transcription effort. Researchers studying agent behavior across model families or training interaction models are the intended consumers.
