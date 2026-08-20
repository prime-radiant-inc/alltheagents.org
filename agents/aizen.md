---
name: "aizen"
slug: "aizen"
layout: "agent.njk"
category: "agent"
maker: "aizen-stack"
license: "Apache-2.0"
url: "https://github.com/aizen-stack/aizen"
source_code_url: "https://github.com/aizen-stack/aizen"
source_available: True
platforms:
  - "Autonomous"
first_released: "2026-07-05"
current_release: "2026-08-18"
stars: "92"
language: "Rust"
homepage: "https://aizen-stack.vercel.app"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: null
plan_mode: null
model_providers: "Any OpenAI-compatible (OpenAI, OpenRouter, local llama.cpp/vLLM, Anthropic gateway)"
pricing: "Free / open-source (Apache-2.0)"
install_method: "curl -fsSL https://raw.githubusercontent.com/aizen-stack/aizen/main/install.sh | sh (Linux/macOS) | irm ...install.ps1 | iex (Windows) | cargo install --git"
docs_url: "aizen-stack.vercel.app (in-repo: docs/REFERENCE.md, docs/SANDBOX.md)"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Single 34 MB static binary with zero runtime deps (no Node/Python/Docker/cloud), ~10 ms cold start, runs on 512 MB VPS or Raspberry Pi; verify-gate runs tests/typecheck and fixes failures before reporting done; offline BM25-ranked memory brain + durable SOUL identity persona; OS-level sandbox (Landlock+seccomp on Linux, Seatbelt on macOS, Job-Object on Windows) with deny-by-default networking; phone-controlled remote operation via Telegram/Discord with approval prompts for risky edits; git-backed time-machine checkpoints; bring-your-own-model never locked to one provider."
---

Single 34 MB static binary with zero runtime deps (no Node/Python/Docker/cloud), ~10 ms cold start, runs on 512 MB VPS or Raspberry Pi; verify-gate runs tests/typecheck and fixes failures before reporting done; offline BM25-ranked memory brain + durable SOUL identity persona; OS-level sandbox (Landlock+seccomp on Linux, Seatbelt on macOS, Job-Object on Windows) with deny-by-default networking; phone-controlled remote operation via Telegram/Discord with approval prompts for risky edits; git-backed time-machine checkpoints; bring-your-own-model never locked to one provider.
