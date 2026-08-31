---
name: "CodeFuse-muAgent"
slug: "codefuse-muagent"
layout: "agent.njk"
category: "agent-sdk"
maker: "codefuse-ai"
license: "Apache-2.0"
url: "https://github.com/codefuse-ai/CodeFuse-muAgent"
source_code_url: "https://github.com/codefuse-ai/CodeFuse-muAgent"
source_available: "True"
platforms: []
first_released: "2024-04-21"
current_release: "2025-01-15"
stars: "774"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "yes (tool registration, categorization, permission management via Swagger protocol)"
claude_code_plugin: "no"
subagents: "yes (multi-agent orchestration, virtual team design)"
hooks: "no"
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "docker, pip"
docs_url: "https://codefuse.ai/docs/api-docs/MuAgent/overview/multi-agent"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent framework driven by a Knowledge Graph (Eventic Knowledge Graph / EKG) engine rather than purely model-based or fixed-flow approaches. Successful exploration paths are documented into the KG to reduce future token costs. Supports MultiAgent, FunctionCall, CodeInterpreter, and RAG. Visual drag-and-drop canvas for building agent workflows. Validated in complex DevOps scenarios at Ant Group."
---

CodeFuse-muAgent is Ant Group's multi-agent framework built around an Eventic Knowledge Graph engine: workflows are expressed as intent, workflow, tool, and character nodes on a drag-and-drop canvas, and the graph — not free-form model prompting — drives orchestration. Successful exploration paths are written back into the knowledge graph so subsequent runs reuse proven paths and spend fewer tokens rediscovering them. The framework bundles multi-agent orchestration, function calling, a code interpreter for sandboxed execution, and RAG, with tool registration handled through a Swagger-based protocol with permission management, plus visual debugging and monitoring. It was validated in complex DevOps scenarios at Ant Group and ships as the pip package codefuse-muagent, with an SDK (v2.2, January 2025) adding ekg-sdk and parallel execution; public development activity has been quiet since early 2025.
