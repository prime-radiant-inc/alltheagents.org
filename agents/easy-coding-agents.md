---
name: "easy-coding-agents"
slug: "easy-coding-agents"
layout: "agent.njk"
category: "agent"
maker: "yushui2022"
license: null
url: "https://github.com/yushui2022/easy-coding-agents"
source_code_url: "https://github.com/yushui2022/easy-coding-agents"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: "2026-02-02"
current_release: "2026-05-28"
stars: "57"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "OpenAI-compatible APIs"
pricing: "Free/open source"
install_method: "pip install -r requirements.txt then python main.py"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Evidence-gated memory system that preserves source refs across context wipe; autonomous terminal coding loop with plan/code/chat modes, custom agents, todo discipline, loop/budget guards, and final-answer quality gates; benchmarked against summary, long-context, FTS, and vector RAG memory baselines."
---

easy-coding-agents is built around a failure mode common to autonomous loops: the model loses track of what it already established, repeats itself, or declares done without evidence. The engine's guards detect repeated tool calls, over-exploration of simple tasks, and empty responses, while a final-answer quality gate blocks DONE claims that lack verification evidence. The evidence-gated memory layer persists refs, tool logs, and task state across context wipes, and the repo publishes reproducible benchmark snapshots showing memory-subsystem recall after context wipe against summary, FTS, and vector baselines. It is a single-developer research project for people studying agent memory, not a production harness.
