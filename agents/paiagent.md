---
name: "PaiAgent"
slug: "paiagent"
layout: "agent.njk"
category: "other"
maker: "itwanger"
license: "MIT"
url: "https://github.com/itwanger/PaiAgent"
source_code_url: "https://github.com/itwanger/PaiAgent"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-11-25"
current_release: "2026-06-17"
stars: "633"
language: "Java, TypeScript"
homepage: "https://github.com/itwanger/PaiAgent"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, DeepSeek, Tongyi Qwen (DashScope), Zhipu AI (GLM), AIPing"
pricing: "open-source"
install_method: "source"
docs_url: "https://github.com/itwanger/PaiAgent/blob/main/USER_GUIDE.md"
plugin_docs_url: null
config_docs_url: "https://github.com/itwanger/PaiAgent/blob/main/USER_GUIDE.md"
download_url: "https://github.com/itwanger/PaiAgent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Dual-engine architecture (self-developed DAG + LangGraph4j state graph), zero-code visual drag-and-drop orchestration, Skills system with 3-level progressive loading to save tokens, Spring AI unified multi-model access"
---

PaiAgent is a self-hosted, visual platform for composing AI workflows in the style of Dify or n8n, built as a public demonstration that a complete enterprise-grade system can be produced through AI-assisted 'vibe coding'. A ReactFlow drag-and-drop editor assembles flows from LLM nodes (OpenAI, DeepSeek, Qwen, ZhiPu, AIPing), TTS nodes, and input/output nodes, with LLM calls unified through Spring AI and Spring AI Alibaba (DashScope) and SSE streaming throughout. Its differentiator is the dual engine: a hand-built DAG engine using Kahn topological sorting with DFS cycle detection runs alongside a LangGraph4j StateGraph engine, switchable per workflow via an EngineSelector, while a Skills system loads YAML-defined prompts with three-level progressive loading to economize tokens. The stack is Java 21/Spring Boot 3.4 with MySQL 8 on the backend and React 18/TypeScript on the frontend, requiring local Java and Node setup rather than a packaged binary. Java developers studying or extending AI workflow platforms — and instructors demonstrating AI-built software — are the audience.
