---
name: "Hindsight"
slug: "hindsight"
layout: "agent.njk"
category: tool
maker: "vectorize-io"
license: "MIT"
url: "https://github.com/vectorize-io/hindsight"
source_code_url: "https://github.com/vectorize-io/hindsight"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-10-30"
current_release: "2026-08-20"
stars: "20288"
language: "Python"
homepage: null
mcp_support: "yes (HTTP transport — http://localhost:8888/mcp/{bank_id}/)"
plugin_support: "yes (60+ integrations; extensibility via tenant, auth, storage extension points)"
claude_code_plugin: "yes (native integration via npx @vectorize-io/hindsight-coding-agents install claude-code)"
subagents: null
hooks: "yes (webhooks for retain, consolidation, and refresh lifecycle events)"
plan_mode: null
model_providers: "OpenAI, Anthropic, Google, Groq, Bedrock, VertexAI, DeepSeek, Ollama, LMStudio, LiteLLM, 100+ via LiteLLM, subscription passthrough (openai-codex, claude-code, github-copilot)"
pricing: "freemium (open-source self-hosted + paid managed Cloud + Enterprise)"
install_method: "pip"
docs_url: "https://hindsight.vectorize.io"
plugin_docs_url: "https://hindsight.vectorize.io/integrations"
config_docs_url: "https://hindsight.vectorize.io/developer/configuration"
download_url: null
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Agent memory system using biomimetic data structures (world facts, experiences, observations, mental models) to make agents genuinely learn over time rather than just recall conversation history. Achieves state-of-the-art on LongMemEval with a 2-line LLM wrapper for persistent memory."
---

Agent memory system using biomimetic data structures (world facts, experiences, observations, mental models) to make agents genuinely learn over time rather than just recall conversation history. Achieves state-of-the-art on LongMemEval with a 2-line LLM wrapper for persistent memory.
