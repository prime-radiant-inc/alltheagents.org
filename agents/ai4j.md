---
name: "ai4j"
slug: "ai4j"
layout: "agent.njk"
category: "agent"
maker: "LnYo-Cly"
license: "Apache-2.0"
url: "https://github.com/LnYo-Cly/ai4j"
source_code_url: "https://github.com/LnYo-Cly/ai4j"
source_available: "True"
platforms:
  - "CLI"
first_released: "2024-08-17"
current_release: "2026-08-19"
stars: "423"
language: "Java"
homepage: "https://lnyo-cly.github.io/ai4j/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, OpenAI-compatible, Anthropic, DashScope, Doubao, DeepSeek, Moonshot, Zhipu, Hunyuan, Lingyi, Ollama, MiniMax, Baichuan, Suno"
pricing: "Free / open-source"
install_method: "Maven: io.github.lnyo-cly:ai4j:2.4.2 or Gradle: implementation 'io.github.lnyo-cly:ai4j:2.4.2'"
docs_url: "https://lnyo-cly.github.io/ai4j/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/LnYo-Cly/ai4j"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Java 8+ agentic SDK combining unified LLM access, Tool Calling, MCP, A2A, RAG, Agent Runtime, and a built-in Coding Agent CLI/TUI/ACP in one SDK"
---

Java teams who want agentic behavior historically had to bridge to Python ecosystems; ai4j provides the equivalent natively for JDK 8+, including Spring Boot starters and a BOM. The SDK normalizes OpenAI-compatible, Anthropic, DashScope, Doubao, DeepSeek, Moonshot, Ollama, and other wire formats behind one API, layers tool calling, RAG (Pinecone, Qdrant, pgvector, Milvus, Redis), and AgentFlow integration with Dify, Coze, and n8n on top, and ships a coding agent surface installable via Maven (io.github.lnyo-cly:ai4j). It is a single-maintainer project with 949 commits, an active changelog, and GitHub Pages documentation, at version 2.4.2.
