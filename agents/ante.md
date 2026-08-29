---
name: "Ante"
slug: "ante"
layout: "agent.njk"
category: "agent"
maker: "Antigma Labs"
license: "Apache-2.0"
url: "https://github.com/AntigmaLabs/ante"
source_code_url: "https://github.com/AntigmaLabs/ante"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-23"
current_release: "2026-08-28"
stars: 1915
language: "Rust"
homepage: "https://antigma.ai"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google Gemini, xAI Grok, DeepSeek, OpenRouter, local GGUF (built-in llama.cpp), any OpenAI-compatible endpoint"
pricing: "free"
install_method: "curl -fsSL https://ante.run/install.sh | bash"
docs_url: "https://docs.antigma.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/AntigmaLabs/ante/releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A self-contained Rust coding agent shipped as a single ~15MB dependency-free binary with no model lock-in — 17 provider presets plus a custom catalog layer for any OpenAI-compatible endpoint, and fully offline operation when pointed at a local GGUF file via the built-in llama.cpp. Declarative profiles define the whole agent (system prompt, tools, skills, memory) in a settings file."
---

Ante is a terminal coding agent from Antigma Labs that works like Claude Code or Codex but ships as one compressed Rust binary with zero runtime dependencies, reflecting a design thesis of tiny, verifiable, self-contained agents built for massive scale. The whole agent — system prompt, tools, skills, memory — is declared in a settings file, and `--profile` swaps behavior per run; four modes cover interactive TUI, headless one-shot, a server daemon, and a Slack/Discord gateway. It runs any model through 17 built-in provider presets or a custom OpenAI-compatible endpoint, and goes fully offline with a local GGUF file and no API key. The core harness is developed in a private repo and distributed as a prebuilt binary under Binary Preview Terms, while the SDK, protocol crates, docs, and eval pipeline in the public repo are Apache-2.0; it scores 82.7% on Terminal-Bench 2.1 using open-weight DeepSeek V4 Flash. It targets macOS and Linux developers who want a Claude Code-style workflow without vendor or dependency constraints.
