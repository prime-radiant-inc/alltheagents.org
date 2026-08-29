---
name: "VT Code"
slug: "vt-code"
layout: "agent.njk"
category: "agent"
maker: "vinhnx"
license: "MIT OR Apache-2.0"
url: "https://github.com/vinhnx/VTCode"
source_code_url: "https://github.com/vinhnx/VTCode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-08-29"
current_release: "2026-08-19"
stars: "783"
language: "Rust"
homepage: "https://github.com/vinhnx/VTCode/wiki"
mcp_support: "yes (MCP client/server modes; docs/guides/mcp-integration.md; /mcp slash command)"
plugin_support: "yes (Agent Plugins: portable skill + MCP packages via vtcode plugins)"
claude_code_plugin: "no"
subagents: "yes (subagents and propose/verify sub-agent separation for loop engineering)"
hooks: "yes (lifecycle hooks with per-workspace approval before running shell commands)"
plan_mode: "yes (/plan command with plan agent and structured review gate handoff to build/auto agents)"
model_providers: "30+ built-in (Anthropic, OpenAI, Gemini, Mistral, DeepSeek, xAI, Qwen, etc.), OpenAI-compatible endpoints, local via Ollama, LM Studio, llama.cpp"
pricing: "open-source"
install_method: "curl install script, brew, cargo"
docs_url: "https://github.com/vinhnx/VTCode/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Rust terminal coding agent combining LLM-native code understanding, OS-native sandboxing, multi-provider support (including local inference), open protocols (MCP, ACP, A2A, Open Responses), Agent Skills/Plugins extensibility, loop engineering with worktree isolation, and a full TUI — all in a single Rust terminal tool."
---

VT Code is a Rust, Ratatui-based terminal coding agent aimed at long-running autonomous workflows where safety and cost control matter. Its loop engineering includes worktree isolation for parallel agents, a propose/verify split between sub-agents, durable loop state, and cost guardrails, with both an interactive TUI and headless modes (vtcode exec, --full-auto, scheduled tasks). Protocol coverage is unusually broad: MCP in both client and server modes, ACP for Zed integration, A2A, Open Responses, and the Anthropic Messages API, plus Agent Skills and portable Agent Plugins packages. Around 30 providers are built in, from Anthropic and OpenAI to DeepSeek and Moonshot, with experimental local inference via Ollama, LM Studio, and llama.cpp. Lifecycle hooks and provider whitelists are configured in vtcode.toml with per-workspace approval gating.
