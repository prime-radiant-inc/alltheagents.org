---
name: "HashAgent"
slug: "hashagent"
layout: "agent.njk"
category: "other"
maker: "mason131928"
license: "MIT"
url: "https://hashagent.pages.dev/"
source_code_url: "https://github.com/mason131928/hashagent"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-08-08"
current_release: null
stars: 10
language: "TypeScript"
homepage: "https://hashagent.pages.dev/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "local WebGPU models (Llama 3.2 1B, Qwen, Phi-4, SmolLM class, 360M-8B)"
pricing: "free"
install_method: "Open https://hashagent.pages.dev/ in a WebGPU-capable browser"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A complete AI agent encoded as one URL hash fragment: name, emoji, system prompt, greeting, model, and temperature live in the link, and inference runs locally in the browser via WebGPU, with no account, no tracking, and no inference server. Optional web search and page reading go through an open-source gateway that never sees the conversation."
---

HashAgent compresses an entire agent into a shareable URL. The agent's definition — a name, an emoji, a system prompt, an opening message, a model choice, and a temperature — is serialized into the URL's hash fragment, so opening the link reconstructs the agent with zero server-side state; a QR code is generated when the URL is short enough. Models run entirely in the browser through WebGPU, ranging from a 360M safe-mode default up to 8B-parameter options for capable hardware, with vision-ready variants handling images and camera input. Conversations are ephemeral by default (or kept on-device), and the only online component is an optional open-source gateway for web search and page reading, which can see the query or URL but never the conversation and can be switched off. It is a general browser agent builder rather than a repo-scale coding tool: no file editing, terminal, or workspace tools are exposed.
