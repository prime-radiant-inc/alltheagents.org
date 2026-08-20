---
name: "clawdstrike"
slug: "clawdstrike"
layout: "agent.njk"
category: "agent"
maker: "backbay-labs"
license: "Apache-2.0"
url: "https://github.com/backbay-labs/clawdstrike"
source_code_url: "https://github.com/backbay-labs/clawdstrike"
source_available: True
platforms:
  - "Autonomous"
first_released: "2026-01-31"
current_release: "2026-08-17"
stars: "286"
language: "Rust, TypeScript, Python, Go"
homepage: "https://backbay.io"
mcp_support: True
plugin_support: True
claude_code_plugin: True
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic (Claude), Vercel AI, LangChain, OpenClaw"
pricing: null
install_method: "brew install backbay-labs/tap/clawdstrike; npm install @clawdstrike/sdk; pip install clawdstrike; cargo add clawdstrike"
docs_url: "https://github.com/backbay-labs/clawdstrike/tree/main/docs"
plugin_docs_url: "https://github.com/backbay-labs/clawdstrike/blob/main/docs/src/guides/openclaw-integration.md"
config_docs_url: "https://github.com/backbay-labs/clawdstrike/blob/main/docs/src/reference/policy-schema.md"
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Policy engine / EDR / signed audit chain for AI agents and OS-level events. Treats AI tool calls in the same taxonomy as kernel events (file access, process exec, network flow, etc.). Fail-closed defaults, Ed25519-signed causal graph, formally verified (Lean 4)."
---

Policy engine / EDR / signed audit chain for AI agents and OS-level events. Treats AI tool calls in the same taxonomy as kernel events (file access, process exec, network flow, etc.). Fail-closed defaults, Ed25519-signed causal graph, formally verified (Lean 4).
