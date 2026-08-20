---
name: "contextvc"
slug: "contextvc"
layout: "agent.njk"
category: "agent"
maker: "HaochengLu"
license: "Apache-2.0"
url: "https://github.com/HaochengLu/contextvc"
source_code_url: "https://github.com/HaochengLu/contextvc"
source_available: True
platforms: []
first_released: "2026-07-05"
current_release: "2026-07-05"
stars: "143"
language: "Rust"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: null
hooks: True
plan_mode: null
model_providers: null
pricing: "Free / open-source (Apache-2.0)"
install_method: "cargo install --locked --git https://github.com/HaochengLu/contextvc.git --tag v0.1.0 (requires Rust stable toolchain)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Git-native context control plane: treats agent memory as repo-level infrastructure (versioned, reviewed, merged, CI-checked, enforced). Single source of truth in .context/ compiles to multiple agent-native files (Claude Code, Cursor, Codex, Copilot, Gemini, Cline). Enforces constraints before risky actions via precheck gates. Human review queue for runtime-learned proposals. RepeatBench for failure-prevention benchmarking."
---

Git-native context control plane: treats agent memory as repo-level infrastructure (versioned, reviewed, merged, CI-checked, enforced). Single source of truth in .context/ compiles to multiple agent-native files (Claude Code, Cursor, Codex, Copilot, Gemini, Cline). Enforces constraints before risky actions via precheck gates. Human review queue for runtime-learned proposals. RepeatBench for failure-prevention benchmarking.
