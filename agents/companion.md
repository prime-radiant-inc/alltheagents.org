---
name: "companion"
slug: "companion"
layout: "agent.njk"
category: "other"
maker: "quack-ai"
license: "Apache-2.0"
url: "https://github.com/quack-ai/companion"
source_code_url: "https://github.com/quack-ai/companion"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-07-20"
current_release: "2024-10-09"
stars: "53"
language: "Python"
homepage: "https://docs.quackai.com"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Ollama (Phi 3, Llama 3, CodeQwen, Mistral)"
pricing: "Free / open-source, self-hosted"
install_method: "git clone + cp .env.example .env + docker compose pull && docker compose up"
docs_url: "https://docs.quackai.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "github_topic4"
what_makes_it_special: "Backend API service that acts as an instantly-onboarded team member with knowledge of internal libraries and coding standards; provides code chat endpoint and REST API for guideline management, used via a VSCode extension."
---

Quack AI's companion backend served the server side of a self-hosted, team-context alternative to GitHub Copilot. The FastAPI service sat in front of an Ollama inference container running OSS models such as Phi 3, Llama 3, CodeQwen, and Mistral, exposing a code-chat endpoint plus a REST API for storing and curating the team's coding guidelines and internal library knowledge, which were injected as context into chat responses. Docker Compose brought up the API, an APM dashboard, and a Gradio chat UI together, and the Quack Companion VS Code extension was its primary client. The premise was that a team's coding standards, not model scale, determine assistant quality. Development stopped and the repository was archived on October 11, 2024, remaining as a read-only archive.
