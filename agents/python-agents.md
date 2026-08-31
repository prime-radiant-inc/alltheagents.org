---
name: "Python-Agents"
slug: "python-agents"
layout: "agent.njk"
category: "agent-sdk"
maker: "clarisseIO"
license: "Apache-2.0"
url: "https://github.com/clarisseIO/python-agents"
source_code_url: "https://github.com/clarisseIO/python-agents"
source_available: "Yes"
platforms:
  - "Autonomous"
first_released: "2024-12-29"
current_release: "2024-12-29"
stars: null
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Ollama, IBM Granite 3.0, Llama 3.1/3.x"
pricing: "open-source"
install_method: "npm install Clarisse-agent-framework"
docs_url: "https://github.com/clarisseIO/python-agents/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/clarisseIO/python-agents"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Despite the repo name 'python-agents', this is a TypeScript agent framework (Clarisse Agent Framework) optimized for IBM Granite and Llama 3.x models; includes sandboxed code interpreter, serialization for pause/resume workflows, OpenAI-compatible Assistants API, and multiple memory strategies. IBM has stated it will not maintain this code going forward."
---

Despite its name, python-agents is a TypeScript agent framework — the 'Clarisse Agent Framework' — built for agents that plan, call tools, and run code in a sandboxed interpreter. It offers prebuilt and custom agents, built-in tools like DuckDuckGo search, token-optimizing memory strategies, workflow serialization for pausing and resuming long tasks, and an emitter-based instrumentation system for observing agent internals. The code is a rebrand of IBM's Bee agent framework: the structure, feature list, and legal notice match i-am-bee/bee-agent-framework, with 'Bee' swapped for 'Clarisse' throughout. IBM's own notice states the code will not be maintained going forward, and the repository shows a single commit with no community adoption. It remains a reference for the Bee framework's capabilities around Granite and Llama 3.x, not a live project.
