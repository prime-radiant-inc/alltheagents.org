---
name: "sudocode"
slug: "sudocode"
layout: "agent.njk"
category: "agent"
maker: "sudoprivacy"
license: "MIT"
url: "https://github.com/sudoprivacy/sudocode"
source_code_url: "https://github.com/sudoprivacy/sudocode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-22"
current_release: "2026-08-19"
stars: "294"
language: "Rust"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, xAI, Gemini, proxy/mock (model-agnostic)"
pricing: "open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/sudoprivacy/sudocode/main/install.sh | sh"
docs_url: "https://github.com/sudoprivacy/sudocode/blob/main/docs/usage.md"
plugin_docs_url: "https://github.com/sudoprivacy/sudocode/blob/main/docs/plugins.md"
config_docs_url: null
download_url: "https://github.com/sudoprivacy/sudocode/releases/latest"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal-native, pipe-composable, scrollback-safe CLI coding agent for heavy users. Inline-only (never hijacks terminal), model-agnostic, headless-first, local-first (zero telemetry by default), open source. Designed as an interchangeable agent unit for multi-agent orchestration via the nexus VFS chat-with-me mailbox."
---

sudocode was built by the Sudo Privacy community in explicit reaction to Claude Code's beginner-oriented direction, and its design choices follow from that audience: output renders inline so tmux, ssh, and terminal scrollback stay intact; JSON output pipes into jq like any Unix tool; and sessions are stored as readable, forkable jsonl files with zero telemetry by default. The same binary runs as a REPL, a one-shot command, or a headless ACP server for editors and web clients, with MCP servers mounted alongside built-in tools. It is deliberately positioned as an agent unit rather than an orchestrator — fleets of 7-10 or 100+ instances coordinate through a nexus VFS mailbox under the broader Sudowork platform. Releases are gated on dogfooding, and everything is configuration files: sessions as jsonl, config as .scode.json, docs as markdown.
