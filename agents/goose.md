---
name: "Goose"
slug: "goose"
layout: "agent.njk"
category: "agent"
maker: "aaif-goose"
license: "Apache-2.0"
url: "https://github.com/aaif-goose/goose"
source_code_url: "https://github.com/aaif-goose/goose"
source_available: "True"
homepage: "https://goose-docs.ai/"
docs_url: "https://goose-docs.ai/"
download_url: "https://goose-docs.ai/docs/getting-started/installation"
install_method: "curl -fsSL https://github.com/aaif-goose/goose/releases/download/stable/download_cli.sh | bash (CLI); desktop app download from goose-docs.ai"
platforms:
  - "CLI"
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2024-08-23"
current_release: "2026-09-03"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: "https://goose-docs.ai/docs/getting-started/using-extensions"
config_docs_url: null
model_providers: "Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more (15+ providers)"
pricing: "free"
stars: "53895"
sources:
  - "github-issue"
last_verified: "2026-09-04"
what_makes_it_special: "Open-source, extensible AI agent that runs locally as a desktop app, CLI, or API on macOS, Linux, and Windows, for code and general tasks alike, with 70+ MCP extensions."
---

Goose is a general-purpose agent that runs on your own machine, for coding as well as research, writing, automation, and data analysis, packaged as a native desktop app, a CLI, and an embeddable API on macOS, Linux, and Windows and built in Rust. Its extension model is MCP-first: more than 70 documented extensions cover databases, APIs, browsers, and GitHub, and you can build your own, while model access stays provider-neutral across Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and others. The project started at Block and is now hosted by the Agentic AI Foundation at the Linux Foundation, with 149 releases since September 2024. It suits developers who want a local, hackable agent they can extend with their own MCP servers.
