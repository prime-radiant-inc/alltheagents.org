---
name: "Zap"
slug: "zap"
layout: "agent.njk"
category: "agent"
maker: "zap-coding-agent"
license: "MIT"
url: "https://github.com/zap-coding-agent/zap-coding-agent"
source_code_url: "https://github.com/zap-coding-agent/zap-coding-agent"
source_available: True
platforms:
  - "CLI"
first_released: "2026-05-16"
current_release: "2026-08-19"
stars: "32"
language: "Rust"
homepage: "https://zap.justpush.cloud"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: True
plan_mode: False
model_providers: "Anthropic, OpenAI, Google Gemini (incl. keyless gcloud ADC), LM Studio, Ollama, Groq, OpenRouter, DeepSeek, xAI, Together AI, Mistral, Perplexity, Cohere, any OpenAI-compatible endpoint"
pricing: "Free/open source (MIT)"
install_method: "macOS/Linux: curl -fsSL https://raw.githubusercontent.com/zap-coding-agent/zap-coding-agent/main/install.sh | bash; Windows: download zip from releases; Build: cargo build --release; also on crates.io"
docs_url: "https://zap.justpush.cloud/docs.html"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/zap-coding-agent/zap-coding-agent/releases/latest"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Terminal-first, local AI coding agent built in Rust (single statically-linked binary, ~20 MB idle memory, millisecond cold start). AST-powered code indexing (tree-sitter + SQLite) — deliberately opposite to Claude Code's no-index approach; knows what exists before writing. Skill-first prompt architecture (~1.8k token baseline vs ~8-10k in competitors). Lazy-loaded MCP with zero token cost until a server is needed. SLM support with structured plan execution. Automated session continuity and 25+ pattern secret scanner."
---

Terminal-first, local AI coding agent built in Rust (single statically-linked binary, ~20 MB idle memory, millisecond cold start). AST-powered code indexing (tree-sitter + SQLite) — deliberately opposite to Claude Code's no-index approach; knows what exists before writing. Skill-first prompt architecture (~1.8k token baseline vs ~8-10k in competitors). Lazy-loaded MCP with zero token cost until a server is needed. SLM support with structured plan execution. Automated session continuity and 25+ pattern secret scanner.
