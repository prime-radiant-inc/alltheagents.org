---
name: "Bestie"
slug: "bestie"
layout: "agent.njk"
category: "agent"
maker: "jolexxa"
license: "MPL-2.0"
url: "https://github.com/jolexxa/bestie"
source_code_url: "https://github.com/jolexxa/bestie"
source_available: "True"
homepage: null
docs_url: "https://github.com/jolexxa/bestie#readme"
download_url: "https://github.com/jolexxa/bestie/releases"
install_method: "curl -fsSL https://raw.githubusercontent.com/jolexxa/bestie/main/install.sh | bash (downloads the latest release for your platform to ~/.local/bin); Windows needs Developer Mode plus a one-time elevation prompt for sandbox provisioning"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Dart"
first_released: "2026-09-08"
current_release: "2026-10-15"
maintained: "active"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "Fireworks AI, OpenRouter, any OpenAI-compatible server"
pricing: "free"
stars: "13"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A native terminal coding agent in Dart whose selling point is total visibility — a details pane showing inputs and outputs for every action — with a cross-platform sandbox (wide reads, limited writes, configurable network levels), subagents, background jobs, compaction, and pull-based handling of long outputs."
---

Bestie is a native terminal coding-agent harness by Joanna May, written in Dart and built as a Flutter-style layered package set (domain, data, infra, use cases, view). Its stated purpose is visibility: a details pane shows the inputs and outputs of every action the agent takes, so, in the author's words, Bestie can't sneak anything past you — the product is for people who want total power over robots. The agent loop invokes its own tools through isolate-backed worker pools with parallel execution: filesystem create/edit tools for text, a sandboxable bash environment for everything else, web search and fetch (using curl-impersonate to dodge captchas), plus calculator, date-time, Wikipedia, and arXiv utilities. Sandboxing is cross-platform — wide read access with writes limited to the working directory and configurable network access levels — with a Windows 10-compatible approach that trades a one-time elevation prompt for simplicity. Subagents are focused workers spawned to finish one self-contained task and report back (they cannot spawn further subagents), and long-running work uses a pull-based paradigm where jobs notify the agent and it pulls the report. Sessions save and load, compaction happens automatically or on demand, and a built-in terminal emulator/multiplexer, command palette, themes, and mascot characters round out the TUI. Providers are Fireworks AI, OpenRouter, and any OpenAI-compatible server, configured through a JSON-schema'd config file or a visual options menu. The project is explicitly alpha ('brand new and should be considered to be in alpha still'), with MCP, ACP, skills, and agents.md on the roadmap. It suits developers who want an agent whose every action they can watch — and a Dart codebase they can read.
