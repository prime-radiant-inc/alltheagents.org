---
name: "orchestration-framework"
slug: "orchestration-framework"
layout: "agent.njk"
category: "other"
maker: "Snowflake-Labs"
license: "Apache-2.0"
url: "https://github.com/Snowflake-Labs/orchestration-framework"
source_code_url: "https://github.com/Snowflake-Labs/orchestration-framework"
source_available: "True"
platforms: []
first_released: "2024-09-18"
current_release: "2025-07-02"
stars: "74"
language: "Python"
homepage: "https://github.com/Snowflake-Labs/orchestration-framework"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "Snowflake Cortex"
pricing: "open-source"
install_method: "pip install orchestration-framework"
docs_url: "https://github.com/Snowflake-Labs/orchestration-framework#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/Snowflake-Labs/orchestration-framework#faq"
download_url: "https://pypi.org/project/orchestration-framework/"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Multi-agent orchestration framework (also called 'Agent Gateway') with native Snowflake services support. Routes requests to appropriate tools (Cortex Search for RAG, Cortex Analyst for Text2SQL, Python for custom operations, SQL for custom pipelines) instead of requiring users to choose between them. Uses LLM Compiler architecture from Berkeley AI Research, supports parallel function calling, Trulens tracing, and runs in SPCS/Snowflake Notebooks with a Streamlit UI demo. Not a coding agent harness."
---

Snowflake shops face a forced choice when serving AI features: Cortex Search for unstructured RAG or Cortex Analyst for Text2SQL, with no client-side layer that combines them in one request. Snowflake Labs' Agent Gateway fills that gap as a pip-installable Python framework built on Snowpark: a planner LLM decomposes a request into an execution graph of tasks with parallel function calling, following Berkeley's LLM Compiler architecture, and routes each step to Cortex Search, Cortex Analyst, Python tools, or custom SQL tools. Multi-step, multi-tool, multi-hop workflows run client-side with an optional TruLens observability extra, and a Quickstart notebook plus Streamlit demo cover onboarding. The FAQ points teams wanting in-Snowflake orchestration to the managed Cortex Agent API instead, positioning this as the client-side alternative. It is Apache-2.0 Python for Snowpark users, with moderate activity (132 commits).
