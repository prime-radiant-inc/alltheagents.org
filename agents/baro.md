---
name: "baro"
slug: "baro"
layout: "agent.njk"
category: "multiplexer"
maker: "jigjoy-ai"
license: "MIT"
url: "https://github.com/jigjoy-ai/baro"
source_code_url: "https://github.com/jigjoy-ai/baro"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-22"
current_release: "2026-08-18"
stars: "111"
language: "TypeScript,Rust"
homepage: "https://baro.rs"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "claude,codex,opencode,openai,hybrid,jigjoy"
pricing: "Free/open-source (MIT); cloud version uses prepaid credits (pay-as-you-go)"
install_method: "npm install -g baro-ai; or curl -fsSL https://api.baro.jigjoy.ai/install.sh | sh (cloud runner)"
docs_url: "https://docs.baro.rs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/baro-ai"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "CLI that turns a natural-language goal into a build-verified PR by orchestrating a fleet of parallel AI coding agents; Mozaik event-bus architecture (no central orchestrator bottleneck, every role is a participant reacting to typed events); true parallelism with each story in its own isolated git worktree (demonstrated 2.2x parallel speedup, 33 stories -> PR in 71 min); semantic memory via local ONNX embeddings (no API calls); per-story model tiering (cheap stories to cheaper models, cross-cutting to stronger models); per-phase and per-story provider overrides; auth inherited from existing CLI sessions."
---

baro is a CLI that takes a goal sentence and returns a build-verified pull request, orchestrating a fleet of AI coding agents in parallel. An Architect pins the design, a Planner decomposes the goal into a story DAG, and each story runs as an independent agent in its own git worktree; a Critic reviews, a Surgeon replans stuck stories, and a Verifier runs builds and tests before a pull request opens. Coordination happens over the Mozaik event bus with no central orchestrator, so every role is a peer reacting to typed events, and a semantic memory (local ONNX embeddings) lets sibling agents share findings to avoid duplicate exploration. Backends include Claude Code, Codex, opencode, any OpenAI-compatible endpoint, and a hosted jigjoy gateway, with per-phase and per-tier model overrides. It is MIT-licensed, runs from npm or brew, and suits developers who want hands-off, parallel PR generation.
