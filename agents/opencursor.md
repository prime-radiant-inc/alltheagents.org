---
name: "OpenCursor"
slug: "opencursor"
layout: "agent.njk"
category: "agent"
maker: "PawanOsman"
license: "MIT"
url: "https://github.com/PawanOsman/OpenCursor"
source_code_url: "https://github.com/PawanOsman/OpenCursor"
source_available: "True"
platforms:
  - "IDE"
first_released: "2022-12-06"
current_release: "2026-08-15"
stars: null
language: "TypeScript"
homepage: "https://marketplace.visualstudio.com/items?itemName=pkrd.ocursor"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Gemini, OpenRouter, Ollama, llama.cpp, custom OpenAI-compatible/Anthropic-style endpoints"
pricing: "Free / open-source (MIT); BYO subscriptions or API keys; local models free"
install_method: "VS Code Marketplace"
docs_url: "https://github.com/PawanOsman/OpenCursor#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/PawanOsman/OpenCursor#readme"
download_url: "https://github.com/PawanOsman/OpenCursor/releases"
maintained: "active"
sources:
  - "jqueryscript"
what_makes_it_special: "Local-first / offline capable (built-in llama.cpp, Ollama, on-device ONNX MiniLM embeddings for semantic search), no cloud required; per-hunk inline review CodeLenses without git; OAuth subscription reuse for Claude Code, OpenAI Codex, Google Antigravity; 25 tools; 11 lifecycle hooks (Cursor/Claude-Code compatible); risk-heuristic approval policies."
---

Cursor-class assistants assume cloud APIs and per-token billing, which excludes air-gapped machines, sensitive codebases, and users avoiding subscription lock-in. OpenCursor takes the Cursor experience into a VS Code extension with a 25-tool agentic loop — workspace reading, file editing, command execution, semantic search — and makes the offline path first-class: it spawns and manages a llama.cpp server for GGUF models pulled from Hugging Face, supports Ollama, and computes semantic-search embeddings on-device with ONNX MiniLM, so it works in airplane mode. When cloud models are wanted, OAuth sign-in reuses Claude Code, OpenAI Codex, or Google Antigravity subscriptions instead of API keys, alongside standard OpenAI/Anthropic/Gemini/OpenRouter keys and MCP, hooks, and subagents across Agent/Ask/Plan/Debug/Multitask modes. It installs from the VS Code Marketplace under MIT. Developers who want a Cursor-style agent under their own hardware and terms are the audience.
