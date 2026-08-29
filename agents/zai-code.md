---
name: "Z.ai Code"
slug: "zai-code"
layout: "agent.njk"
category: "other"
maker: "Z.ai"
license: "Mixed (open weights for some GLM models under permissive license)"
url: "https://z.ai/code"
source_code_url: null
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: "Python"
homepage: "https://z.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Z.ai (Zhipu AI) GLM models"
pricing: "GLM-4-Flash free; GLM-4.6 ~$0.60/M input, $2.20/M output tokens"
install_method: "Configure GLM coding plan endpoint (Anthropic-compatible API) in your coding tool"
docs_url: "https://z.ai"
plugin_docs_url: "https://docs.z.ai"
config_docs_url: "https://docs.z.ai"
download_url: "https://docs.z.ai"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "International brand of Zhipu AI (Tsinghua University spinoff). Provides GLM series models (GLM-4.6, GLM-4.5, GLM-4-Flash) tuned for coding and agentic workflows. Open-weight releases available on Hugging Face. Not a standalone coding agent — it is a model provider that powers coding agents like Cursor, Continue, and Cline."
---

Z.ai Code is Zhipu AI's international offering of GLM-series models tuned for coding and agentic workflows, plus a GLM Coding Plan subscription served through an Anthropic-compatible API endpoint. Because the endpoint is Anthropic-compatible, coding tools such as Claude Code, Cline, Roo Code, and OpenCode can switch to GLM models with minimal configuration, making it a drop-in alternative to Claude for agentic coding. GLM-4.6, GLM-4.5, and GLM-4-Flash are the headline coding-tuned models, with open-weight releases published on Hugging Face alongside the API platform. MCP servers work through whichever coding tool the developer configures, using GLM as the model. Its audience is coding-agent users seeking cheaper inference, particularly in tools like Claude Code, Cline, Roo Code, and OpenCode.
