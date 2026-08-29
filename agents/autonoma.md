---
name: "Autonoma"
slug: "autonoma"
layout: "agent.njk"
category: "agent"
maker: "Sebasbo"
license: "MIT"
url: "https://github.com/Sebasbo/Autonoma"
source_code_url: "https://github.com/Sebasbo/Autonoma"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2024-06-25"
current_release: "2025-06-09"
stars: "11"
language: "Python"
homepage: null
mcp_support: null
plugin_support: "no"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "pluggable llm_interface (any provider)"
pricing: "open-source"
install_method: "pip install autonoma"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/autonoma/"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Agentic AI framework that autonomously modifies, analyzes, and tests codebases. Uses a multi-agent system (PlannerAgent, CoderAgent, Tester) to collaboratively generate, refactor, and test code through an iterative process. Features an extensible architecture for custom agents and tasks."
---

Autonoma is a Python framework in which a multi-agent system autonomously modifies, analyzes, and tests codebases through an event-driven loop. A PlannerAgent splits a query into tasks (up to 10 by default), CoderAgent generates or refactors code with AST manipulation and static analysis, and a Tester generates and runs unittest suites, feeding failures back for revision. Agents operate asynchronously with Pydantic-validated data structures, and the LLM interface is pluggable: any provider with a generate(prompt) method works, so backend choice is fully decoupled. Tasks can specify file paths and complexity estimates, and the architecture supports custom agents and task types. The project is an early-stage MIT-licensed Python package installed via pip, best viewed as a reference design for plan-code-test loops rather than a production harness.
