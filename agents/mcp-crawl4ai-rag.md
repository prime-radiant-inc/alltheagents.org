---
name: "mcp-crawl4ai-rag"
slug: "mcp-crawl4ai-rag"
layout: "agent.njk"
category: "other"
maker: "coleam00"
license: "MIT"
url: "https://github.com/coleam00/mcp-crawl4ai-rag"
source_code_url: "https://github.com/coleam00/mcp-crawl4ai-rag"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2025-05-03"
current_release: "2025-07-25"
stars: "2240"
language: "Python"
homepage: null
mcp_support: "yes (SSE and stdio)"
plugin_support: "no"
claude_code_plugin: "yes"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "open-source"
install_method: "docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/coleam00/mcp-crawl4ai-rag"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Combines Crawl4AI + Supabase + optional Neo4j knowledge graph with 5 toggleable advanced RAG strategies including contextual embeddings, hybrid search, agentic RAG, cross-encoder reranking, and AI hallucination detection via knowledge graph validation of AI-generated code against real GitHub repos."
---

Coding assistants hallucinate APIs and library usage because they answer from parametric memory, so this server gives them a retrieval layer: Crawl4AI ingests documentation sites or GitHub repositories into a Supabase vector store, and the agent queries it mid-task through MCP tools. Strategy toggles adjust behavior per deployment - hybrid search, contextual embeddings, cross-encoder reranking - and an optional Neo4j knowledge graph powers a hallucination checker that validates AI-written Python against real repository code. Claude Desktop, Claude Code, Windsurf, and n8n are documented clients over SSE or stdio. The author considers the repository a testbed feeding his Archon project, so issues are not actively worked.
