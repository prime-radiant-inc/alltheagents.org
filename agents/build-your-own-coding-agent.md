---
name: "build-your-own-coding-agent"
slug: "build-your-own-coding-agent"
layout: "agent.njk"
category: "other"
maker: "yanhua1010"
license: "MIT"
url: "https://github.com/yanhua1010/build-your-own-coding-agent"
source_code_url: "https://github.com/yanhua1010/build-your-own-coding-agent"
source_available: "True"
platforms: []
first_released: "2026-07-26"
current_release: "2026-08-07"
stars: "33"
language: "TypeScript/Node.js"
homepage: "https://github.com/yanhua1010/build-your-own-coding-agent"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "DeepSeek, GLM (Zhipu), Kimi (Chinese domestic LLM APIs)"
pricing: "Free/open source"
install_method: "cd steps/01-minimal-loop && npm install && npm start (Node.js 20+; requires DeepSeek or GLM API key)"
docs_url: "https://github.com/yanhua1010/build-your-own-coding-agent"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/yanhua1010/build-your-own-coding-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Educational tutorial series that reverse-engineers three industrial-grade open-source coding agents (pi, codex, grok-build) layer by layer, teaching you to build a working mini-agent from ~100 lines up — using exclusively Chinese domestic LLM APIs, making it accessible to developers in China without needing OpenAI/Anthropic access."
---

build-your-own-coding-agent is an educational repository that dissects how production coding agents work, publishing condensed architecture notes alongside runnable code for each layer. The series targets Chinese-speaking developers and reverse-engineers three open-source agents — pi, Codex, and grok-build — explaining the agent loop, LLM API contracts, tool-calling mechanics, and context management step by step, with articles distributed through a WeChat public account and X. All exercises run against Chinese domestic providers (DeepSeek, GLM, Kimi), which removes the OpenAI/Anthropic access barrier for developers in China and distinguishes it from Western equivalents of the same tutorial genre. The audience is developers who want to understand agent internals rather than ship a product, and the repository is early-stage and small (33 stars, recent creation). It is classified as educational material rather than a harness because nothing here is a tool others adopt for daily coding.
