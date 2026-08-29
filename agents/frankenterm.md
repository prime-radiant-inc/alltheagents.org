---
name: "frankenterm"
slug: "frankenterm"
layout: "agent.njk"
category: "multiplexer"
maker: "Dicklesworthstone"
license: "NOASSERTION"
url: "https://github.com/Dicklesworthstone/frankenterm"
source_code_url: "https://github.com/Dicklesworthstone/frankenterm"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-01-18"
current_release: "2026-08-20"
stars: "107"
language: "Rust"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "Run install.sh script in repository root"
docs_url: "https://github.com/Dicklesworthstone/frankenterm/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Dicklesworthstone/frankenterm"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Terminal hypervisor for AI agent swarms; provides real-time pane capture, state-machine pattern detection for agent state, and a JSON API for coordinating fleets of coding agents across WezTerm; turns a terminal multiplexer into a coordination layer for AI agent swarms."
---

Running many CLI coding agents means manually watching terminals for the moments an agent goes idle, asks a question, or gets stuck. Frankenterm treats the terminal itself as the integration surface: it captures WezTerm pane content in real time, runs state-machine pattern detection to classify what each agent is doing, and publishes that state through a JSON API that scripts and other tools can query and act on. This lets operators build their own coordination logic on top of unmodified agents rather than adopting a vendor's orchestration format. It targets developers running agent swarms in WezTerm who want programmatic fleet control without changing how each agent is invoked.
