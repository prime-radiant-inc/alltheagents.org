---
name: "miii-cli"
slug: "miii-cli"
layout: "agent.njk"
category: "agent"
maker: "maruakshay"
license: "MIT"
url: "https://github.com/maruakshay/miii-cli"
source_code_url: "https://github.com/maruakshay/miii-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-06"
current_release: "2026-07-13"
stars: "29"
language: "TypeScript/Node.js"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "True"
model_providers: "Ollama (default), any OpenAI-compatible local server (llama.cpp, LM Studio)"
pricing: "Free forever — no API keys, no per-token billing, runs on your own hardware"
install_method: "macOS/Linux: curl -fsSL https://raw.githubusercontent.com/maruakshay/miii-cli/main/install.sh | sh; Windows: irm https://raw.githubusercontent.com/maruakshay/miii-cli/main/install.ps1 | iex; npm: npm install -g miii-agent"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/miii-agent"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "100% local and private open-source terminal AI coding agent — code never leaves your machine, no cloud, no accounts, works fully offline. Free forever with no API keys or per-token metering. Lossless output spill: large tool outputs are written to disk and paged through by the model, never truncated. miii doctor grades installed local models on real engineering tasks. Plan -> Act -> Observe loop. Image paste support with vision-capable models. MIII.md repo-level conventions file."
---

miii exists for engineers whose code cannot leave the machine: it talks only to local inference servers — Ollama by default, plus any OpenAI-compatible local endpoint like llama.cpp or LM Studio — so it works offline with no accounts and no per-token billing. The loop plans a task, acts through six permission-gated tools (read, write, edit, glob, grep, bash) confined to the workspace, and observes results before proceeding, with ~/.miii/permissions.json persisting approvals across sessions. Two implementation choices stand out: oversized tool output is written to disk and paged through the model rather than truncated, so long build logs survive intact, and MIII.md plays the role of CLAUDE.md as a per-repo conventions file read every turn. Model choice is hardware-bound — qwen2.5-coder 7b for 8 GB VRAM up to 32b at 48 GB+ — and miii doctor grades installed candidates on real tasks rather than trusting benchmarks. Privacy-sensitive codebases and offline environments are the audience; the project is a one-maintainer MVP at small star count but actively developed.
