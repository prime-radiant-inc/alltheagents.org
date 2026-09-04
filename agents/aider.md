---
name: "Aider"
slug: "aider"
layout: "agent.njk"
category: "agent"
maker: "aider-ai"
license: "Apache-2.0"
url: "https://github.com/Aider-AI/aider"
source_code_url: "https://github.com/Aider-AI/aider"
source_available: "True"
homepage: "https://aider.chat/"
docs_url: "https://aider.chat/docs/"
download_url: null
install_method: "python -m pip install aider-install && aider-install"
platforms:
  - "CLI"
autonomy_level:
  - "pair-programmer"
specialization: "general"
language: "Python"
first_released: "2023-05-09"
current_release: "2025-08-09"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "OpenAI, Anthropic, Gemini, Groq, LM Studio, xAI, Azure, Cohere, DeepSeek, Ollama, OpenRouter, Vertex AI, Amazon Bedrock"
pricing: "free"
stars: "48721"
sources:
  - "github-issue"
last_verified: "2026-09-04"
what_makes_it_special: "AI pair programming in the terminal: it maps the codebase, auto-commits every change with git, lints and tests as it goes, and takes voice, images, and web pages as context. Works with 100+ languages and almost any LLM, including through copy/paste to a web chat."
---

Aider works against existing codebases as well as greenfield projects: launch it in a repo, request changes in natural language, and it edits files directly while committing automatically with descriptive messages. It supports voice-to-code, image and web-page context, and a watch mode that lets you drive it from comments inside any IDE, and its model leaderboard is a standard reference for coding performance. Nearly any LLM works, including local models through Ollama or OpenRouter. Installation is a pip one-liner via the aider-install bootstrapper, documentation lives at aider.chat, and with nearly 49,000 GitHub stars it is among the most starred open-source coding tools.
