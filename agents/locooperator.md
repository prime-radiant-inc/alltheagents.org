---
name: "LocoOperator"
slug: "locooperator"
layout: "agent.njk"
category: "other"
maker: "LocoreMind"
license: "MIT"
url: "https://github.com/LocoreMind/LocoOperator"
source_code_url: "https://github.com/LocoreMind/LocoOperator"
source_available: "True"
platforms: []
first_released: "2026-02-21"
current_release: "2026-02-25"
stars: "160"
language: "Python"
homepage: "https://locoremind.com/blog/loco-operator"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "yes"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "OpenRouter (cloud fallback); local llama.cpp (GGUF)"
pricing: "Free/open-source (zero API cost when run locally)"
install_method: "git clone + uv sync; requires Claude Code (npm install -g @anthropic-ai/claude-code), llama.cpp, and an OpenRouter API key"
docs_url: "https://locoremind.com/blog/loco-operator"
plugin_docs_url: null
config_docs_url: null
download_url: "https://huggingface.co/LocoreMind/LocoOperator-4B-GGUF"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "4B-parameter code-exploration agent distilled from Qwen3-Coder-Next, designed as a local sub-agent for Claude Code-style agent loops; 100% JSON-valid tool calls (outperforming the teacher model's 87.6%); runs locally via GGUF/llama.cpp at zero API cost; hybrid routing proxy falls back to OpenRouter on context overflow."
---

The project targets the cost profile of Claude Code sessions, where every cheap exploration subagent still bills API tokens. A local proxy intercepts Claude Code's subagent dispatches (which would otherwise default to Haiku) and routes them to LocoOperator-4B served by llama.cpp, translating between the Anthropic Messages API and the model's JSON tool-call format. Training prioritized tool-call validity over general capability, which is why the distilled model beats its teacher on JSON validity. When a subagent's context overflows, the proxy falls back to OpenRouter so sessions do not die mid-exploration. Claude Code users with local GPU capacity use it to cut per-session cost while keeping the main agent on a frontier model.
