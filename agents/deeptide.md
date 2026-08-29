---
name: "deeptide"
slug: "deeptide"
layout: "agent.njk"
category: "agent"
maker: "paean-ai"
license: "MIT"
url: "https://github.com/paean-ai/deeptide"
source_code_url: "https://github.com/paean-ai/deeptide"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-05-05"
current_release: "2026-07-08"
stars: "1087"
language: "Rust, TypeScript, Swift"
homepage: "https://deeptide.sh"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "yes"
model_providers: "DeepSeek (default), BYOK to any Anthropic-protocol-compatible endpoint (OpenAI, Anthropic, Ollama, Gemini, Zhipu GLM, Volcengine, Moonshot, Qwen, self-hosted)"
pricing: "open-source"
install_method: "binary, npm"
docs_url: "https://deeptide.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/deeptide"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Built specifically for DeepSeek models with three flavors (native macOS app, TypeScript/Bun CLI, Rust CLI+GUI) that share configuration, sessions, and tools via a shared interface contract (tide-spec). Includes a local DeepSeek inference runtime (Metal engine + OpenAI/Anthropic-compatible gateway). Hooks engine for pre/post tool, user-prompt, session, and compaction shell hooks."
---

Deeptide exists because DeepSeek users otherwise have to run general-purpose harnesses tuned for other providers. The three form factors deliberately share one interface contract (tide-spec), so configuration, sessions, and tools carry across the native macOS app, the Bun-based CLI, and the Rust binary. The macOS build embeds a local DeepSeek V4 Flash Metal inference engine with an OpenAI/Anthropic-compatible gateway, which lets the agent run fully on-device. It is aimed at DeepSeek-centric developers who want an agent, REPL, and inference runtime from one project rather than assembling them separately.
