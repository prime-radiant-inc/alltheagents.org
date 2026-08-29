---
name: "AppAgent"
slug: "appagent"
layout: "agent.njk"
category: "other"
maker: "TencentQQGYLab"
license: "MIT"
url: "https://github.com/mnotgod96/AppAgent"
source_code_url: "https://github.com/mnotgod96/AppAgent"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-12-20"
current_release: "2025-03-19"
stars: "6847"
language: "Python"
homepage: "https://appagent-official.github.io/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (GPT-4V), Alibaba (Qwen-VL-Max)"
pricing: "BYOK"
install_method: "pip"
docs_url: "https://appagent-official.github.io/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "LLM-based multimodal agent that operates smartphone apps through a simplified action space mimicking human interactions (tapping/swiping) via ADB — no system back-end access needed. Two-phase approach: exploration (autonomous or human-guided) generates a knowledge base of UI element documentation, then deployment completes user tasks. Published at CHI 2025; successor AppAgentX adds an evolving mechanism."
---

AppAgent addresses GUI automation without backend access: an LLM-driven agent explores an app either autonomously or by watching human demonstrations, tagging interactive elements in screenshots and writing documentation for each, then executes tasks referencing that documentation in deployment. It runs on GPT-4V (about $0.03 per request pair) or free Qwen-VL-Max, needs only ADB and USB debugging (Android Studio emulators auto-detected), and is MIT-licensed with a CHI 2025 paper. The mnotgod96 repository mirrors Tencent QQGY Lab's official project (~6.9k stars), which saw its last major update with the AppAgentX successor in March 2025 — the original is minimally maintained and focused on GUI operation research, not software development.
