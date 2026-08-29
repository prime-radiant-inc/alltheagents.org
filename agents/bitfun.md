---
name: "BitFun"
slug: "bitfun"
layout: "agent.njk"
category: "agent"
maker: "GCWing"
license: "MIT"
url: "https://github.com/GCWing/BitFun"
source_code_url: "https://github.com/GCWing/BitFun"
source_available: "Yes"
platforms:
  - "Desktop"
first_released: "2026-02-02"
current_release: "2026-08-20"
stars: "1798"
language: "Rust"
homepage: "https://openbitfun.com/"
mcp_support: "yes (L2 customization tier includes MCP for connecting external tools)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes (Codex-hook compatible, existing hook scripts work as-is)"
plan_mode: "yes"
model_providers: "BYOK (model-agnostic, choose provider and enter API key)"
pricing: "open-source"
install_method: "binary"
docs_url: "https://openbitfun.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/GCWing/BitFun/releases/latest"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Combines a high-performance Rust agent runtime with a polished desktop app featuring Agentic Mini Apps (each task gets its own dedicated UI bound to live conversation state), self-hosted zero-knowledge multi-device relay, 98.67% KV cache hit rate via byte-stable prompt assembly, and flashgrep for 36x faster repo search."
---

BitFun pairs a Rust agent runtime with a Tauri desktop app, positioning itself around the idea that a chat transcript is the wrong interface for many agent tasks. When the agent builds a chart, board, form, or panel, that interface persists as a mini app bound to the conversation's live state, and a public gallery hosts shareable examples. The runtime is tuned for long-horizon work: byte-stable prompt assembly keeps KV-cache hit rates at 98.67% on SWE-Bench-Pro runs, and a resident flashgrep index speeds repository search roughly 36x on Chromium-scale codebases. Customization runs through four tiers — custom agents, MCP/skills/hooks, mini apps, and source-level changes — with Codex-compatible hooks so existing scripts work unmodified. Multi-device use runs through a self-hosted, zero-knowledge relay (Argon2id and AES-GCM client-side key derivation), keeping sessions off vendor infrastructure. The project is MIT-licensed, spare-time research rather than a commercial product, and actively developed with 3,400+ commits.
