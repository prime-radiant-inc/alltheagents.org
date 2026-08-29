---
name: "AI expert for codebases"
slug: "ai-expert-for-codebases"
layout: "agent.njk"
category: "other"
maker: "Storia AI"
license: "Apache-2.0"
url: "https://storia.ai"
source_code_url: null
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: null
language: "Python"
homepage: "https://sage.storia.ai"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Ollama"
pricing: "Free / open-source; hosted app offers free indexing for OSS repos"
install_method: null
docs_url: "https://sage-docs.storia.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Storia-AI/sage"
maintained: "dead"
sources:
  - "toolify"
what_makes_it_special: "Chat with any codebase in under two minutes; runs fully locally (Ollama + Marqo) or via third-party APIs; modular architecture with pluggable embeddings, LLMs, and vector stores; well-documented benchmark experiments comparing retrieval strategies."
---

Sage targets the onboarding problem: understanding an unfamiliar codebase takes days, and generic chatbots lack repo-specific context. It indexes a repository into a vector store (Marqo or pluggable alternatives) and answers questions through either lightweight LLM retrieval or full RAG, with embeddings, LLMs, and vector stores all swappable via abstract classes. A fully local mode (Ollama for the LLM, Marqo for vectors) keeps proprietary code on the developer's machine, while a hosted app at sage.storia.ai serves open-source repositories. The project was archived on February 3, 2025 and is read-only.
