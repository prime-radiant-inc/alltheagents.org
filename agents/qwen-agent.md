---
name: "Qwen-Agent"
slug: "qwen-agent"
layout: "agent.njk"
category: "agent-sdk"
maker: "QwenLM"
license: "Apache-2.0"
url: "https://github.com/QwenLM/Qwen-Agent"
source_code_url: "https://github.com/QwenLM/Qwen-Agent"
source_available: "Yes"
platforms: []
first_released: "2023-09-22"
current_release: "2026-03-04"
stars: "16992"
language: "Python"
homepage: "https://pypi.org/project/qwen-agent/"
mcp_support: "yes (stdio transport)"
plugin_support: "yes (custom tools via @register_tool, built-in tools, Chrome extension)"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DashScope (Alibaba Cloud), OpenAI-compatible APIs (vLLM, Ollama), Qwen models"
pricing: "open-source (Apache-2.0)"
install_method: "pip"
docs_url: "https://qwenlm.github.io/Qwen-Agent/en/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/qwen-agent/"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Framework for building LLM applications leveraging Qwen's instruction following, tool usage, planning, and memory capabilities, featuring MCP support, code interpreter with Docker sandboxing, RAG for 1M-token contexts, and example applications like Browser Assistant — serves as the backend of Qwen Chat."
---

Qwen-Agent is Alibaba's framework for building LLM applications that use tools, plan, and remember — the same code that powers Qwen Chat in production. Its building blocks are a base chat model abstraction and composable agents that combine function calling, RAG over million-token documents, a Docker-sandboxed code interpreter, and browser automation through the BrowserQwen Chrome extension. Unlike coding-specific harnesses, it treats code execution as one tool among many: the framework is equally at home building assistants, document QA pipelines, or browser agents, with prompts and tool-call templates tuned for Qwen models though it runs against any OpenAI-compatible endpoint. The Qwen team maintains it actively, and it ships its own DeepPlanning benchmark for evaluating agent planning. Developers building Qwen-powered applications use it as the foundation layer rather than as a terminal coding tool.
