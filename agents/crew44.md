---
name: "Crew44"
slug: "crew44"
layout: "agent.njk"
category: "multiplexer"
maker: "Crew44"
license: "MIT"
url: "https://crew44.io"
source_code_url: null
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: null
language: "Go, TypeScript"
homepage: "https://crew44.io"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Claude Code, Codex, Cursor Agent, Gemini CLI, Hermes, Kimi, OpenCode, OpenClaw, Pi, Qoder, Qwen Code"
pricing: "Free, no account required, no subscription"
install_method: "Pre-built signed desktop builds (.dmg/.exe/.AppImage/.deb) from crew44.io/download, or build from source with npm install && npm run dev (requires Node 20+, Go 1.26+, at least one coding-agent CLI)"
docs_url: "https://crew44.io"
plugin_docs_url: null
config_docs_url: null
download_url: "https://crew44.io/download"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Local-first orchestrator that turns coding-agent CLIs into a coordinated crew of specialist agents (Partner, Engineer, Product Lead, Designer), each bound to its best model. Per-project memory so skills compound over time. Right-model-per-role cost optimization. Parallel specialists with context-light handovers. Verifiable Goals checked by an independent fresh-session verifier. Encrypted mobile pairing via Noise tunnel through a self-hostable relay. One shared skills folder across all providers. State in ~/.crew44/, no cloud/telemetry."
---

Crew44 addresses the sprawl that appears when developers run several AI coding CLIs side by side with no shared state or division of labor. A local Go daemon binds each specialist role to the model best suited to it, coordinates handoffs between the underlying CLIs (Claude Code, Codex, Gemini CLI, Cursor Agent, OpenCode, and others), and runs agents in parallel in one workspace. Per-project memory and skills are stored as plain files, and a background Partner agent proposes new memories with evidence for the user to accept or dismiss. Everything stays on the machine: the daemon binds to localhost, state lives in ~/.crew44, and there is no account, subscription, or telemetry, which appeals to developers who want multi-agent workflows without cloud services.
