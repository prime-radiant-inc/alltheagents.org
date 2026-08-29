---
name: "swival"
slug: "swival"
layout: "agent.njk"
category: "agent"
maker: "Swival"
license: "MIT"
url: "https://github.com/Swival/swival"
source_code_url: "https://github.com/Swival/swival"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-24"
current_release: "2026-08-19"
stars: "324"
language: "Python"
homepage: "https://swival.dev"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "n/a"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "LM Studio, llama.cpp, HuggingFace Inference, OpenRouter, Google Gemini, Vertex AI, ChatGPT Plus/Pro (browser auth), AWS Bedrock, Apple Foundation Models, generic OpenAI-compatible (ollama, vLLM), Command"
pricing: "Free/open-source (MIT)"
install_method: "uv tool install --python 3.14 swival; or macOS: brew install swival/tap/swival"
docs_url: "https://swival.dev/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Swival/swival"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "CLI coding agent built for any model, especially small/local models with tight context windows. Pure Python (no framework) with graduated compaction, persistent thinking notes, todo checklists that survive context resets, secret encryption, cross-session BM25 memory, goal-driven loops, timer-based scheduled runs, A2A/ACP server modes, and a built-in security audit pipeline."
---

Swival exists because most coding-agent CLIs assume frontier models with large context windows, leaving users of small or locally hosted models with tools that degrade quickly. It is a single pure-Python agent loop with a deliberately small tool set (read, write, edit, bash) and no framework dependency, and its engineering centers on context discipline: graduated compaction that summarizes in stages, persistent thinking notes that survive context resets, todo checklists that are re-injected after compaction, and cross-session BM25 memory so resumed work recalls earlier decisions. Connectivity is unusually broad for its size — LM Studio and llama.cpp auto-discovery, OpenRouter, Gemini, Bedrock, Vertex, Apple Foundation Models, browser-authenticated ChatGPT subscriptions, and any OpenAI-compatible server — plus a command provider that shells out to external agents like codex exec. Lifecycle hooks and command middleware support unattended or policy-constrained operation, A2A/ACP server modes let other harnesses call it, and scheduled runs suit automation. It targets developers running local or low-cost models who still want durable, multi-session agent behavior.
