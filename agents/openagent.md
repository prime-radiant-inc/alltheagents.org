---
name: "openagent"
slug: "openagent"
layout: "agent.njk"
category: "agent"
maker: "the-open-agent"
license: "Apache-2.0"
url: "https://github.com/the-open-agent/openagent"
source_code_url: "https://github.com/the-open-agent/openagent"
source_available: "True"
platforms:
  - "Web"
first_released: "2020-05-29"
current_release: "2026-08-18"
stars: "5536"
language: "Go"
homepage: "https://www.openagentai.org/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI, Anthropic, Google Gemini, DeepSeek, Mistral, Grok, Qwen, Doubao, Moonshot, ChatGLM, Baichuan, Ernie, iFlytek, HuggingFace, Cohere, Amazon Bedrock, OpenRouter, Ollama"
pricing: "open-source"
install_method: "binary, docker"
docs_url: "https://www.openagentai.org"
plugin_docs_url: null
config_docs_url: "https://www.openagentai.org"
download_url: "https://github.com/the-open-agent/openagent#install"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Open-source personal AI assistant shipped as a single binary with no runtime dependencies (runs natively on Linux/macOS/Windows, including native Windows without WSL/Docker). 30+ LLM providers switchable per conversation. Autonomous agent loops with browser-use, shell execution, office automation, and MCP integration (SSE/Stdio/StreamableHTTP). Built-in RAG knowledge base with pluggable embeddings, visual BPMN-style workflow builder with conditional/parallel execution and scheduling, and enterprise features (SSO via OIDC/OAuth2/LDAP/SAML, multi-tenancy, audit logs, admin dashboard with usage analytics)."
---

Personal AI assistants usually demand Python environments, Docker, or per-seat cloud accounts, which puts them out of reach for privacy-conscious individuals and small teams. OpenAgent compiles a Go backend with a React frontend into a single binary that installs via curl or PowerShell script, runs natively on Linux, macOS, and Windows without WSL or Docker, and starts a web UI on port 14000. Its agent loop draws on 30-plus switchable LLM providers (OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Qwen, OpenRouter, Ollama, and more), executes tools through any MCP-compatible server over SSE, stdio, or Streamable HTTP, and adds browser automation, shell execution, office automation, and a RAG knowledge base with pluggable embeddings. Multi-tenancy with OIDC/OAuth2/LDAP/SAML, audit logs, and usage-cost analytics target self-hosted team deployment. It suits users who want a private, single-binary assistant combining coding-agent abilities with office and browser automation.
