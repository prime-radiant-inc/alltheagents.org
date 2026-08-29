---
name: "Langroid"
slug: "langroid"
layout: "agent.njk"
category: "agent-sdk"
maker: "langroid"
license: "MIT"
url: "https://github.com/langroid/langroid"
source_code_url: "https://github.com/langroid/langroid"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-04-16"
current_release: "2026-08-18"
stars: "4101"
language: "Python"
homepage: "https://langroid.github.io/langroid/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI, Anthropic, Google Gemini, Ollama, LiteLLM, OpenRouter, Cerebras, DeepSeek, Portkey, LangDB"
pricing: "open-source"
install_method: "pip"
docs_url: "https://langroid.github.io/langroid/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "Intuitive, lightweight, extensible Python framework (from CMU/UW-Madison researchers) for building LLM-powered multi-agent applications. Agent-as-actor paradigm with hierarchical task delegation via TaskTool. Does NOT depend on LangChain. Pydantic-based tool/function definitions, built-in RAG with source citation (DocChatAgent), SQL chat, knowledge graph chat (Neo4j/ArangoDB), lineage tracking. Works with practically any LLM. Has a Claude Code plugin (claude plugin install langroid@langroid)."
---

Langroid came out of CMU and UW-Madison research as an alternative to monolithic agent chains: each agent is an actor that transforms messages, and Task objects compose them into parent-child hierarchies with explicit delegation and addressing. The library ships RAG agents, structured extraction, SQL/table agents, and vector-store integrations (Qdrant, Chroma, Milvus, pgvector, and others), and since v0.53.0 any agent can consume MCP server tools through an adapter. It targets Python developers building multi-agent LLM applications, including production users such as Nullify, and is released under MIT with monthly releases.
