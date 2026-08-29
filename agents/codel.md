---
name: "Codel"
slug: "codel"
layout: "agent.njk"
category: "agent"
maker: "semanser"
license: "AGPL-3.0"
url: "https://github.com/semanser/codel"
source_code_url: "https://github.com/semanser/codel"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
first_released: "2024-03-18"
current_release: "2024-04-29"
stars: null
language: "Go"
homepage: "https://discord.gg/uMaGSHNjzc"
mcp_support: null
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI,Ollama"
pricing: "open-source"
install_method: "Docker (pre-built image from GitHub Container Registry)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "jim"
  - "ishandutta"
what_makes_it_special: "Fully autonomous AI agent running in a sandboxed Docker environment with a built-in browser, text editor, automatic Docker-image picker, and PostgreSQL-backed command history."
---

Codel is a self-hosted autonomous agent that carries a task from description to completion using a terminal, a browser, and a text editor, all inside sandboxed Docker containers. The agent decides its next step autonomously, consulting the web through a built-in browser when it needs information and editing files through an editor viewable in the web UI; command and output history persists in PostgreSQL for later review. It selects an appropriate Docker image for each task automatically and works with OpenAI models or self-hosted Ollama endpoints configured through environment variables. The project drew attention as an early open-source answer to Cognition's Devin, accumulating roughly 2.5k stars, but development stalled in 2024 and the repository has been dormant since.
