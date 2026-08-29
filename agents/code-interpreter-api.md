---
name: "Code-Interpreter-Api"
slug: "code-interpreter-api"
layout: "agent.njk"
category: "other"
maker: "leezhuuuuu"
license: "GPL-3.0"
url: "https://github.com/leezhuuuuu/Code-Interpreter-Api"
source_code_url: "https://github.com/leezhuuuuu/Code-Interpreter-Api"
source_available: "True"
platforms: []
first_released: "2024-08-13"
current_release: "2025-01-04"
stars: "166"
language: "Python"
homepage: "https://code.leez.tech/doc"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free/open-source"
install_method: "git clone; pip install -r requirements.txt; configure config.yaml; docker pull leezhuuu/code_interpreter:latest; python3 center.py"
docs_url: "https://code.leez.tech/doc"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/leezhuuuuu/Code-Interpreter-Api"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Scheduling center plus sandbox using Docker for safe, isolated Python code execution; stores generated image data in PostgreSQL with API access; designed to accelerate AI agent development by providing a reliable remote code-execution API."
---

The service gives LLM applications a safe code-execution backend without exposing the host: each request runs in an isolated Docker container with configurable memory/CPU limits and timeouts, and generated images persist in PostgreSQL for retrieval through a REST endpoint. The scheduling center manages concurrency with queues and semaphores, and a hosted demo integrates with FastGPT, so agent platforms can add code execution without building sandbox infrastructure. It deliberately contains no LLM, planning, or agent logic - it is the tool, not the agent. Development activity ceased in early 2025.
