---
name: "LineCodePro"
slug: "linecodepro"
layout: "agent.njk"
category: "agent"
maker: "LangLang03"
license: "GPL-3.0-or-later"
url: "https://github.com/LangLang03/LineCodePro"
source_code_url: "https://github.com/LangLang03/LineCodePro"
source_available: "True"
platforms: []
first_released: "2026-06-03"
current_release: "2026-08-18"
stars: "84"
language: "Java"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenAI-compatible, Anthropic, Codex (OpenAI), Local GGUF (llama.cpp)"
pricing: null
install_method: "Download prebuilt APK from GitHub Releases (sideload) or build with Gradle: ./gradlew :app:assembleDebug"
docs_url: "https://github.com/LangLang03/LineCodePro/blob/master/CLAUDE.md"
plugin_docs_url: null
config_docs_url: "https://github.com/LangLang03/LineCodePro/blob/master/ipc/README.md"
download_url: "https://github.com/LangLang03/LineCodePro/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Self-hosted, on-device AI coding workspace/assistant for Android 8.0+. Runs a real tool-call loop where models can read/edit files, run shell commands (via Termux/SSH/IPC), search the web, generate images, and dispatch sub-agents. Supports custom MCP-HTTP tools (mcpx_*), custom agents (agentx_*), and pluggable IPC terminal providers, plus local on-device llama.cpp GGUF inference."
---

LineCodePro brings a Claude Code-style tool loop to Android, where nearly all coding agents assume a desktop: models read/edit/delete files, run shell commands through Termux, SSH, or a sandboxed IPC terminal-provider app, search the web, and dispatch sub-agents, with every write producing a DiffRecord for inline review. Inference runs against OpenAI-compatible, Anthropic, or Codex protocols, or entirely on-device through llama.cpp GGUF models, so the tool works without any cloud dependency. Custom MCP-HTTP tools and custom agents register through an extensions screen, and a pluggable AIDL terminal-provider interface lets any third-party app supply the shell. Android-toting developers who want their coding agent self-hosted and on-device use the sideloaded APK or build from source.
