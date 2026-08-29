---
name: "fx"
slug: "fx"
layout: "agent.njk"
category: "agent"
maker: "vercel-labs"
license: "Apache-2.0"
url: "https://fx.sh"
source_code_url: "https://github.com/vercel-labs/fx"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-08-11"
current_release: "2026-08-20"
stars: "1271"
language: "Zig"
homepage: "https://fx.sh"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Model-agnostic (local models, gateways, direct provider APIs, or subscriptions)"
pricing: "open-source"
install_method: "curl -fsSL https://fx.sh/setup.sh | bash"
docs_url: "https://fx.sh/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://fx.sh/setup.sh"
maintained: "active"
sources:
  - "user_reported"
what_makes_it_special: "A coding agent harness written in Zig that behaves like a Unix shell rather than a terminal IDE: a ~6 MB binary with microsecond cold start, a shell-like UI that preserves scroll history, WebAssembly builds with a pluggable network stack, and a deliberately minimal system prompt for token efficiency."
---

Most agent CLIs are Node or Python applications with heavy startup costs, which limits where they can run. Vercel Labs built fx in Zig as a ~6 MB static binary with near-instant cold start and a small memory footprint, intended to be embedded in sandboxes, CI, and larger systems rather than to replace an editor. The UI follows shell conventions and preserves scrollback, and the core stays small by pushing capability into skills, plugins, and MCP servers while remaining model- and provider-agnostic. Version 0.0.6 is explicitly experimental with frequent breaking changes expected, so adopters are largely tool builders evaluating embeddable agent runtimes.
