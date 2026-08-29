---
name: "Letta-Deepseek"
slug: "letta-deepseek"
layout: "agent.njk"
category: "agent"
maker: "mahawi1992"
license: "MIT"
url: "https://github.com/mahawi1992/letta-deepseek"
source_code_url: "https://github.com/mahawi1992/letta-deepseek"
source_available: "True"
platforms: []
first_released: "2024-12-07"
current_release: "2024-12-08"
stars: "11"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Letta AI, DeepSeek, Tavily"
pricing: null
install_method: "git clone; create Python venv; pip install -r requirements.txt; configure .env from .env.example"
docs_url: "https://github.com/mahawi1992/letta-deepseek/blob/main/docs/deployment.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Advanced multi-agent system built with Letta AI and DeepSeek, featuring memory optimization and Lightning AI deployment. Comprises a Research Agent, Coding Agent, Documentation Agent, and an Orchestrator coordinating them."
---

The project demonstrates wiring Letta's stateful-memory framework to DeepSeek models for a division-of-labor coding pipeline: a research agent with Tavily web search, a DeepSeek-powered coding agent, a documentation agent, and an orchestrator coordinating them. Memory features emphasize optimization, pattern recognition, and knowledge accumulation across runs, with deployment documented for Lightning AI. At nine commits, eleven stars, and no issues or releases, it is a personal reference implementation rather than a supported product. Developers use it as a worked example of wiring Letta's memory framework to DeepSeek and Tavily rather than as a daily-driver tool.
