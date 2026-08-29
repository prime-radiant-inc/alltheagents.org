---
name: "Deep Agents Code"
slug: "deep-agents-code"
layout: "agent.njk"
category: "agent"
maker: "langchain-ai"
license: "MIT"
url: "https://github.com/langchain-ai/deepagents"
source_code_url: "https://github.com/langchain-ai/deepagents"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-27"
current_release: "2026-08-20"
stars: null
language: "Python"
homepage: "https://docs.langchain.com/deepagents"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google, open-weight models (Baseten, Fireworks), self-hosted (Ollama, vLLM, llama.cpp), any LangChain chat model"
pricing: "Free / open source"
install_method: "uv add deepagents (Python), curl -LsSf https://langch.in/dcode | bash (CLI)"
docs_url: "https://docs.langchain.com/oss/python/deepagents/overview"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/deepagents/"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "Batteries-included agent harness built on LangGraph. Provides planning, file system access, context management, sub-agents with isolated context windows, shell access, persistent memory, human-in-the-loop approval, skills, and tool calling. Designed for long-horizon, multi-step work. Also available as deepagents.js (TypeScript)."
---

deepagents exists because teams kept rebuilding the same scaffolding around LLM agents: a planning step, file access, context compaction, and task delegation. The library ships those as defaults inspired by Claude Code — a built-in planning tool, pluggable filesystem (local, sandboxed, or remote backends), sub-agents with isolated context windows, shell access, persistent memory, and human-in-the-loop approval gates — while every component remains replaceable for teams with different needs. It runs on any tool-calling LLM through LangGraph's production features (streaming, checkpointing, persistence) and accepts any MCP server as a tool source. Python and JavaScript teams use it as the foundation for custom agents rather than as an end-user product, with LangSmith available for tracing and evaluation.
