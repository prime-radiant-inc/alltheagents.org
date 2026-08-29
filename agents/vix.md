---
name: "vix"
slug: "vix"
layout: "agent.njk"
category: "agent"
maker: "get-vix"
license: "AGPL-3.0"
url: "https://github.com/get-vix/vix"
source_code_url: "https://github.com/get-vix/vix"
source_available: "True"
platforms: []
first_released: "2026-04-07"
current_release: "2026-07-28"
stars: "264"
language: "Go"
homepage: "https://getvix.dev"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, OpenRouter, AWS Bedrock, Ollama, llama.cpp, custom providers via providers.json"
pricing: "Free / open-source (bring your own API key)"
install_method: "curl -fsSL https://getvix.dev/install.sh | bash; or Homebrew: brew tap get-vix/vix && brew install vix (macOS and Linux only)"
docs_url: "https://getvix.dev"
plugin_docs_url: null
config_docs_url: "https://github.com/get-vix/vix/blob/main/PROVIDERS.md"
download_url: "https://github.com/get-vix/vix/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Stem agents that maximize cache reuse across explore/plan/execute phases. Tree-sitter virtual filesystem that minifies code for 20–50% fewer tokens. Self-evolving agent that writes its own scheduled jobs/watchers/alerts. Programmable multi-phase workflows in JSON. Whiteboard mode with visual canvas and voice AI walkthrough. Benchmarked as faster and cheaper than Claude Code in plan mode."
---

vix targets the cost and latency tax that coding agents pay when every phase re-reads the same codebase. Instead of specialized subagents, one stem agent carries a generic system prompt and receives phase-specific instructions as user messages, so exploration history stays cached and reusable when the same session moves into planning and execution. A tree-sitter virtual filesystem minifies code as it is read, cutting context tokens by a reported 20-50%, and workflows defined in JSON chain agent, bash, and tool steps with branching and parallelism. Benchmarked against Claude Code on seven real tasks, vix was about 47% cheaper and 40% faster overall. It targets terminal-first developers on macOS and Linux who bring their own API keys.
