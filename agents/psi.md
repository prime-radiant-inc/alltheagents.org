---
name: "psi"
slug: "psi"
layout: "agent.njk"
category: "agent"
maker: "siraben"
license: "MIT"
url: "https://github.com/siraben/psi"
source_code_url: "https://github.com/siraben/psi"
source_available: "True"
homepage: "https://psicode.ai"
docs_url: "https://github.com/siraben/psi/tree/master/docs"
download_url: null
install_method: "nix run github:siraben/psi-code (a 6 MB fat binary via Cosmopolitan; same binary on Linux/macOS/Windows), or clone and make from source (C89 + Lua; needs libedit, ncurses, curl, zlib, cJSON)"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
  - "one-shot-generative"
specialization: "general"
language: "Lua"
first_released: "2026-04-26"
current_release: "2026-11-07"
maintained: "active"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "False"
hooks: "True"
plan_mode: "False"
plugin_docs_url: "https://github.com/siraben/psi/blob/master/docs/extensions.md"
config_docs_url: null
model_providers: "Anthropic, OpenAI Codex (OAuth), OpenRouter, Ollama, Moonshot (Kimi For Coding)"
pricing: "BYOK"
stars: "7"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A 6 MB coding agent written in C89 with a Lua runtime, built on the Cosmopolitan library so one binary runs on Linux, macOS, Windows, Haiku, FreeBSD, OpenBSD, and an iPhone via iSH; features beyond the base live in user-written Lua extensions — even the agent loop and TUI rendering are extension-overridable — and it deliberately ships no sandbox, marketplace, telemetry, or auto-update."
---

psi started from a frustration the README states plainly — coding agents are slow, bloated, and inscrutable, and their builds take an hour — and answers it with the most portable stack it could find: C89 for the base, Lua for the runtime, and the Cosmopolitan C library for a single ~6 MB binary that runs everywhere it could test (Linux, macOS, Windows, Haiku, OpenBSD, FreeBSD, on i686 through riscv64, under glibc, musl, cosmopolitan, and four compilers from gcc 4.6 to clang and TCC). It is heavily inspired by pi — the name itself came from a planned pi fork with Scheme as the extension language — and keeps the same shape: only the base functionality is in-tree, while the TUI, queue management, and even the agent loop defer to Lua extensions a user drops into a config directory, registered through a documented psi.* API with tool hooks, events, keybindings, and themes. Sessions are append-only JSONL in pi's v3 schema with forking and branch summaries, so a session started under one provider resumes under another. The audience is the developer who wants a fully auditable agent — it publishes a Software Bill of Materials for its dependencies — small enough to read, daily-drive, and carry anywhere; it reports no eval suite yet, only smoke tests and build-matrix checks.
