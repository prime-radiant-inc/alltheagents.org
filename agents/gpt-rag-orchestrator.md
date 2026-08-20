---
name: "gpt-rag-orchestrator"
slug: "gpt-rag-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "Azure"
license: "MIT"
url: "https://github.com/Azure/gpt-rag-orchestrator"
source_code_url: "https://github.com/Azure/gpt-rag-orchestrator"
source_available: True
platforms: []
first_released: "2023-06-27"
current_release: "2026-08-17"
stars: "100"
language: "Python, TypeScript"
homepage: null
mcp_support: True
plugin_support: null
claude_code_plugin: null
subagents: True
hooks: null
plan_mode: null
model_providers: "Azure OpenAI, Azure AI Foundry Agent Service v2"
pricing: "Free / open source (requires Azure resources)"
install_method: "azd init -t azure/gpt-rag-orchestrator -> azd env refresh -> azd deploy (recommended); or PowerShell script (scripts/deploy.ps1)"
docs_url: "https://azure.github.io/GPT-RAG/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Azure/gpt-rag-orchestrator"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Multi-strategy agentic RAG orchestration with dynamic routing; MCP support (SSE + streamable HTTP); NL2SQL for structured data; Work IQ (Microsoft 365) knowledge source integration; Toolbox OAuth identity passthrough for Foundry hosted agents; versioned audit events with HMAC pseudonymization; optional admin dashboard with Entra ID auth; configurable retrieval backends with Foundry IQ generic MCP knowledge sources"
---

Multi-strategy agentic RAG orchestration with dynamic routing; MCP support (SSE + streamable HTTP); NL2SQL for structured data; Work IQ (Microsoft 365) knowledge source integration; Toolbox OAuth identity passthrough for Foundry hosted agents; versioned audit events with HMAC pseudonymization; optional admin dashboard with Entra ID auth; configurable retrieval backends with Foundry IQ generic MCP knowledge sources
