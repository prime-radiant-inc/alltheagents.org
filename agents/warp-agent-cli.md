---
name: "Warp Agent CLI"
slug: "warp-agent-cli"
layout: "agent.njk"
category: "agent"
maker: "warpdotdev"
license: "Proprietary"
url: "https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent"
source_code_url: null
source_available: "False"
platforms:
  - "CLI"
first_released: "2026-08-04"
current_release: null
stars: null
language: null
homepage: "https://www.warp.dev"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Warp-provided models, custom model routers via YAML config, bring-your-own API keys and OpenAI-compatible endpoints"
pricing: "freemium"
install_method: "curl -fsSL https://app.warp.dev/download/agent-cli | bash (Mac/Linux); PowerShell one-liner on Windows"
docs_url: "https://docs.warp.dev/agents/cli/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://app.warp.dev/download/agent-cli"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "The Warp Agent shipped as a standalone CLI that is also a native terminal multiplexer: agent sessions run atop managed pty connections, so you can switch directories within a persistent session, run agents over SSH without installing a remote binary, and drive full-screen apps like vim and gdb. The harness delegates across subagents using different models and different harnesses, including Claude Code and Codex."
---

The Warp Agent CLI (announced August 4, 2026) takes the multi-model agent built into Warp Terminal and makes it runnable in any terminal — Ghostty, iTerm 2, VS Code, or the built-in Windows and Mac terminals — with no Warp app install required. Because it is built on Warp's terminal infrastructure, each agent session sits on a managed pty connection like tmux, which enables persistent sessions across directory changes, remote execution over SSH, and interaction with full-screen programs; natural shell input means tab completions work and a classifier detects whether you typed a shell command or a prompt. The agent orchestrates subagents and can hand work off to Warp's cloud agents for monitoring and steering from the web, delegating across different models and even different harnesses including Claude Code and Codex. Inference is configurable three ways: a Warp subscription starting at $18/month including inference credits, ad-hoc credits starting at $10, or bring-your-own API keys and endpoints.
