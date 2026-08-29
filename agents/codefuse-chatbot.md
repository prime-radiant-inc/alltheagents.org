---
name: "CodeFuse-ChatBot"
slug: "codefuse-chatbot"
layout: "agent.njk"
category: "agent"
maker: "codefuse-ai"
license: "NOASSERTION"
url: "https://github.com/codefuse-ai/codefuse-chatbot"
source_code_url: "https://github.com/codefuse-ai/codefuse-chatbot"
source_available: "True"
platforms: []
first_released: "2023-09-28"
current_release: "2024-07-01"
stars: "1291"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, open-source LLMs (FastChat, CodeLlama)"
pricing: "open-source"
install_method: "pip, docker"
docs_url: "https://codefuse-ai.github.io/zh-CN/docs/"
plugin_docs_url: null
config_docs_url: "https://codefuse-ai.github.io/zh-CN/docs/developer-docs/CodeFuse-ChatBot/master/quickstart"
download_url: null
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "Multi-Agent collaborative scheduling (codefuse-muAgent framework); repository-level code analysis & generation; document RAG enhanced with knowledge graphs; DevOps-domain-specific knowledge base; sandbox environment for safe code execution; supports offline private deployment."
---

CodeFuse-ChatBot, from Ant Group's CodeFuse team, targets DevOps work that spans design, coding, testing, deployment, and operations, replacing scattered platform-jumping with LLM-driven workflows. Its multi-agent scheduling core, later extracted as the standalone codefuse-muagent framework, orchestrates specialized agents over a shared memory; retrieval-augmented generation combines document knowledge bases with knowledge-graph enhancement, and a sandbox environment executes generated code safely. The system is designed for offline private deployment in enterprise settings, supporting OpenAI-compatible APIs and locally hosted models through FastChat, and it analyzes code at repository level rather than per-file. Documentation is bilingual (Chinese and English) on codefuse-ai.github.io, and development focus shifted to the separate muagent package after January 2024.
