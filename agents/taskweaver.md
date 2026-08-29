---
name: "TaskWeaver"
slug: "taskweaver"
layout: "agent.njk"
category: "other"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/TaskWeaver"
source_code_url: "https://github.com/microsoft/TaskWeaver"
source_available: "True"
platforms: []
first_released: "2023-09-11"
current_release: "2026-03-23"
stars: "6174"
language: "Python"
homepage: "https://microsoft.github.io/TaskWeaver/"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI, Azure OpenAI, local LLMs"
pricing: "open-source"
install_method: "pip, docker"
docs_url: "https://microsoft.github.io/TaskWeaver"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/taskweaver/"
maintained: "dead"
sources:
  - "caramaschi"
what_makes_it_special: "Code-first agent framework for data analytics: it interprets user requests through code snippets and orchestrates plugins (functions) to execute analytics tasks in a stateful manner. Preserves both chat history AND code execution history including in-memory data (e.g., DataFrames), verifies generated code before execution, supports reflective execution, and runs code in isolated containers by default. Repository was archived by the owner on March 23, 2026."
---

Microsoft's TaskWeaver addressed data-analytics automation by making generated code the medium of planning and execution: user requests became Python snippets orchestrated with YAML-defined plugins, executed in stateful sessions that retained DataFrames and other in-memory results across turns. Execution defaulted to an isolated Docker container, generated code was verified before running, and a reflective loop corrected failures; multi-agent extension, experience memory, and AgentOps observability rounded out the framework. It served data scientists and analysts running analytics pipelines — SQL pulls, anomaly detection, forecasting with libraries like yfinance — through CLI, web UI, or library embedding. The repository was archived on March 23, 2026 and is read-only, so the project is no longer developed; it remains a reference implementation of the code-first agent pattern.
