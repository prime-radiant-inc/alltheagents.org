---
name: "Bandit Stealth"
slug: "bandit-stealth"
layout: "agent.njk"
category: "agent"
maker: "BurtsonLabs"
license: "Apache-2.0"
url: "https://open-vsx.org/extension/BurtsonLabs/bandit-stealth"
source_code_url: "https://github.com/Burtson-Labs/bandit-agent-framework.git"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-08-27"
current_release: null
stars: null
language: null
homepage: "https://burtson.ai/stealth"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Ollama, Qwen"
pricing: "freemium"
install_method: "Install from Open VSX"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-vsx.org/extension/BurtsonLabs/bandit-stealth"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Local-first coding agent running Ollama models with tool use, diff approvals, and voice"
---

Bandit Stealth is a coding agent extension for VS Code and OpenVSX-compatible editors that runs locally on any Ollama model - Gemma, Qwen, Devstral, or a custom fine-tune - keeping code entirely on the user's machine by default. The agent autonomously explores the codebase, reads and writes files, and runs shell commands, with every write gated behind a unified-diff approval and inline diffs streaming into the editor as it works. Distinctive mechanics include agent-authored skills, plan preview with go/no-go confirmation, session checkpoints with /rewind, hooks for CI guardrails, and pre-write language validation for TypeScript, Python, JSON, and C#. Voice is fully pluggable and provider-independent (Bandit cloud, Whisper-compatible servers, ElevenLabs, or a local Piper server), and the composer accepts queued input while the agent streams. A companion CLI ships on npm, and an optional hosted gateway offers managed inference. It targets developers who want a real agentic loop without cloud subscriptions or code leaving the device.
