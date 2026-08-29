---
name: "oracle-ai-developer-hub"
slug: "oracle-ai-developer-hub"
layout: "agent.njk"
category: "other"
maker: "oracle-devrel"
license: "UPL-1.0"
url: "https://github.com/oracle-devrel/oracle-ai-developer-hub"
source_code_url: "https://github.com/oracle-devrel/oracle-ai-developer-hub"
source_available: "True"
platforms: []
first_released: "2024-01-16"
current_release: "2026-08-18"
stars: "4339"
language: "Python"
homepage: "https://oracle-devrel.github.io/oracle-ai-developer-hub/"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OCI Generative AI (xAI Grok), OpenAI, Anthropic, HuggingFace, Ollama, LiteLLM"
pricing: "open-source"
install_method: "docker"
docs_url: "https://oracle-devrel.github.io/oracle-ai-developer-hub/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/oracle-devrel/oracle-ai-developer-hub"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Collection of technical resources (reference implementations, notebooks, workshops) for building AI applications using Oracle AI Database as a single converged engine for vectors, agent memory, checkpoints, semantic LLM cache, and chat history. Includes first-party LangChain integrations (langchain-oracledb, langgraph-oracledb, langchain-oci) and the oracleagentmemory package. Production-grade RAG, multi-agent, and hybrid retrieval reference implementations."
---

Oracle positions its AI Database as a single converged engine for the agent era — vector search, agent memory via the OAMP package, checkpoints, and Duality Views in one system — and this Developer Relations repository is the working evidence. The /apps directory holds complete reference implementations (agentic RAG, a finance AI agent, a LangGraph supply-chain demand planner, intelligent document processing), /notebooks teach RAG, agent memory, and CoT/ToT/ReAct reasoning against that stack, and /workshops walk through building a memory-aware enterprise data agent, including one harness for migrating RAG corpora from MongoDB to Oracle 26ai. Framework coverage spans OpenAI Agents SDK, Claude Agent SDK, LangGraph supervisors, and Deep Agents, all pointing back to the database as the state store. Everything is UPL-licensed Python and TypeScript with devcontainer-based workshops. It serves Oracle-centric developers evaluating the platform for agentic workloads, not teams selecting a coding harness.
