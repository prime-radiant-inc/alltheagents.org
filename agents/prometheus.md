---
name: "Prometheus"
slug: "prometheus"
layout: "agent.njk"
category: "agent"
maker: "EuniAI"
license: "GPL-3.0"
url: "https://github.com/EuniAI/Prometheus"
source_code_url: "https://github.com/EuniAI/Prometheus"
source_available: "True"
platforms: []
first_released: "2024-10-14"
current_release: "2026-08-16"
stars: "1123"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google Gemini (BYOK)"
pricing: "freemium"
install_method: "docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/EuniAI/Prometheus"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Multi-agent collaborative reasoning across files and commits using a Neo4j-powered Unified Codebase Knowledge Graph and long-term memory (Athena). Full detect-reproduce-repair-verify (DRRV) automation pipeline with specialized agents for issue classification, bug reproduction, patch generation, and context retrieval. Ranked top on SWE-bench with GPT-5; research-backed (arXiv paper)."
---

Prometheus was built to close the gap between chat-based coding assistants and verifiable issue resolution: given a GitHub issue, it classifies it, reproduces the bug, generates a repair, and verifies the fix in a containerized environment before responding. Its codebase understanding comes from a Unified Codebase Knowledge Graph built with Tree-sitter ASTs and stored in Neo4j, enabling graph-based semantic search over code structure rather than embedding similarity, with a long-term memory component called Athena. LangGraph state machines orchestrate specialized agents for bug reproduction, feature analysis, and question answering, with PostgreSQL checkpointing so long pipelines resume after failure. The system ships as a FastAPI service backed by Docker-isolated test execution rather than an interactive terminal tool. EuniAI reports top-five SWE-bench leaderboard placement (top-1 with GPT-5), and engineering teams use it as an autonomous service for triaging and fixing repository issues.
