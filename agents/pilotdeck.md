---
name: "PilotDeck"
slug: "pilotdeck"
layout: "agent.njk"
category: "agent"
maker: "OpenBMB"
license: "AGPL-3.0"
url: "https://github.com/OpenBMB/PilotDeck"
source_code_url: "https://github.com/OpenBMB/PilotDeck"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-22"
current_release: "2026-08-19"
stars: "3951"
language: "TypeScript"
homepage: "https://pilotdeck.openbmb.cn"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google Gemini, DeepSeek, Qwen, Kimi, MiniMax, Ollama"
pricing: "open-source"
install_method: "docker"
docs_url: "https://pilotdeck.openbmb.cn"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/OpenBMB/PilotDeck"
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Open-source agent operating system (by Tsinghua THUNLP/ModelBest/OpenBMB) centered on 'WorkSpace' isolation — each project gets isolated files, memory, and skills. Traceable white-box memory (visible, editable, rollbackable with Dream Mode consolidation). Smart routing auto-detects task difficulty and routes to appropriate models (~70% cost savings). Always-on background execution that breaks the ask-answer loop. Native MCP support, open plugin architecture, lifecycle hooks. Consistent across Web/CLI/IM front-ends."
---

PilotDeck, open-sourced in May 2026 by Tsinghua's THUNLP lab with ModelBest and OpenBMB, rethinks agent architecture for people juggling multiple long-running projects, where a single global context window becomes a liability. Each project gets an isolated WorkSpace — its own files, memory store, and accreting skill set — so retrieval stays scoped and parallel projects never pollute each other, and the white-box memory design makes every entry inspectable, editable, and rollbackable, with background Dream Mode consolidating memory during idle windows. Smart Routing classifies task difficulty and dispatches accordingly: complex work goes to a flagship model, routine subtasks to lighter ones, with published figures around 70% cost savings on multi-model workloads. The system runs tasks in the background after sign-off, discovering work and delivering files with summary reports. Native MCP support, lifecycle hooks, and a plugin architecture extend it, and the AGPL-licensed platform targets professional users running multiple concurrent projects.
