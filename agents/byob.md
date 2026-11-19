---
name: "byob"
slug: "byob"
layout: "agent.njk"
category: "agent"
maker: "Scronkfinkle"
license: "MIT OR Apache-2.0"
url: "https://github.com/Scronkfinkle/byob"
source_code_url: "https://github.com/Scronkfinkle/byob"
source_available: "True"
homepage: null
docs_url: "https://github.com/Scronkfinkle/byob#readme"
download_url: "https://github.com/Scronkfinkle/byob/releases"
install_method: "cargo install byob (browser UI built in); cargo install byob --no-default-features (slim); nix build github:Scronkfinkle/byob; or release archives (.tar.gz/.dmg) from GitHub Releases for Linux, macOS, and Windows"
platforms:
  - "Desktop"
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-11-09"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: "https://github.com/Scronkfinkle/byob/blob/main/docs/plugins-tools-artifacts.md"
config_docs_url: null
model_providers: "Any OpenAI-compatible endpoint (llama-server, Ollama, LM Studio, vLLM, or a hosted API) plus Claude over Anthropic's Messages API; tool calling falls back to prompt-based calls when the server has none"
pricing: "BYOK"
stars: "7"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A native GPU-drawn desktop AI coworker with no Electron and no bundled inference — point it at any model endpoint you run and it reads and writes files, runs commands and sandboxed Python, and builds spreadsheets, charts, documents, and HTML apps beside the chat, where every feature (prompt, core tools, artifacts, subagents, plan, even compaction) is a bundled plugin on the same public API, and the identical interface compiled to WebAssembly serves a tab or a phone from a live session."
---

byob — Bring Your Own Brain — is a local-first desktop coworker for people who already run a model: no bundled inference and no account, just any OpenAI-compatible URL or Claude over Anthropic's Messages API, with first-run auto-discovery of local servers on their usual ports and per-model settings for context window, temperature, and extra request JSON. It is one native Rust program that draws its own interface on the GPU with no Electron (~60 MB download, 13 MB slim), and the same interface compiled to WebAssembly serves a browser tab or a phone on the live session through byob --serve or tailscale. Around the chat it builds artifacts — spreadsheets that recalculate and report errors back to the model, charts linked to sheets that redraw when data moves, Markdown documents, images, and HTML apps rendered inline by a bundled Servo process — while file tools, run_command, and sandboxed run_python carry an approval-card, diff-per-turn, undo-per-turn workflow, with a YOLO mode that drops the approvals. The defining design choice is that everything is a plugin on one API: the prompt, core tools, artifacts, appearance, and even the appearance-changing ui_look tool ship as bundled plugins anyone can fork, and byob writes and debugs its own plugins from a chat. It began as a rewrite of hob, an earlier desktop coworker that bundled llama.cpp, dropping the bundled inference; its author notes the README is heavily AI-influenced prose, a fair warning to readers.
