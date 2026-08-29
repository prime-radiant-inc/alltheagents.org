---
name: "Crush"
slug: "crush"
layout: "agent.njk"
category: "agent"
maker: "charmbracelet"
license: "FSL-1.1-MIT"
url: "https://github.com/charmbracelet/crush"
source_code_url: "https://github.com/charmbracelet/crush"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-05-21"
current_release: "2026-08-20"
stars: null
language: "Go"
homepage: "https://charm.land"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: "Charm Hyper, Anthropic, OpenAI, Google Gemini, OpenRouter, Amazon Bedrock, Azure OpenAI, Vertex AI, Ollama, llama.cpp, LM Studio, LiteLLM, Groq, Cerebras, Hugging Face, Moonshot, MiniMax, Z.ai, Vercel AI Gateway, any OpenAI/Anthropic-compatible API"
pricing: "Free / open source. Hyper (official provider) has free tier + paid subscription. BYOK for other providers."
install_method: "Homebrew, NPM, Winget, Scoop, apt (Debian/Ubuntu), yum (Fedora/RHEL), Nix, FreeBSD pkg, Arch (yay), go install, or direct binary download"
docs_url: "https://github.com/charmbracelet/crush/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/charmbracelet/crush/releases"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Glamourous terminal-based coding agent by Charmbracelet. Supports multi-model LLMs, session-based contexts, LSP integration, MCP servers (stdio/http/sse with OAuth), agent skills (agentskills.io standard), and preliminary hooks support."
---

Crush is Charmbracelet's entry into terminal coding agents, built to run anywhere a terminal exists: macOS, Linux, Windows, BSDs, and even Android. It maintains multiple named sessions per project, enriches model context through language servers, and connects to tools via MCP servers (with OAuth) and the agentskills.io Agent Skills standard, with hooks and configurable permissions including a --yolo bypass. Any OpenAI- or Anthropic-compatible provider works, alongside auto-discovered local models through Ollama or LM Studio, and models can be switched mid-session without losing context. Charm offers its own Hyper subscription as the hosted option, while the agent itself installs through Homebrew, npm, winget, and most system package managers; with about 28,000 GitHub stars it is one of the most widely used open terminal agents.
