---
name: "vibe-local"
slug: "vibe-local"
layout: "agent.njk"
category: "agent"
maker: "ochyai"
license: "MIT"
url: "https://github.com/ochyai/vibe-local"
source_code_url: "https://github.com/ochyai/vibe-local"
source_available: "True"
platforms: []
first_released: "2026-02-22"
current_release: "2026-07-19"
stars: "802"
language: "Python, Shell"
homepage: "https://github.com/ochyai/vibe-local"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "Ollama, OpenCode multi-provider"
pricing: "open-source"
install_method: "curl install script (binary)"
docs_url: "https://github.com/ochyai/vibe-local#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ochyai/vibe-local/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Fully offline, free AI coding environment for Mac (also Intel Mac/Linux) using Ollama + local LLM. Built for workshops, students, and beginners. Auto model routing (vibe-router) sends chitchat to small models and coding to large models. RAM-aware model management prevents memory exhaustion. Classroom mode, three UI options (OpenCode TUI, Claude Code CLI, built-in Python engine)."
---

vibe-local exists for settings where paid AI subscriptions and reliable internet are not assumptions: workshops, students, and beginners learning to operate a terminal through natural language. After a one-line install it runs entirely on local Ollama models, choosing among them by available RAM (qwen3.5:4b on 8GB machines up to qwen3-coder-next on 80GB+) so sessions never exhaust memory, and a small router model triages each input — small talk gets fast small-model answers, coding and tool tasks go to the large coder model. Users choose their surface: the OpenCode TUI, Claude Code pointed at Ollama, or a built-in stdlib-only Python agent with local RAG over project files; a classroom mode lets one Mac serve the models while students attach over the network. Safety defaults to asking before every shell action since local models can emit destructive commands. Coding workshops and self-learners, primarily in Japan, use it; it is MIT-licensed and under active development.
