---
name: "co-sh"
slug: "cosh"
layout: "agent.njk"
category: "agent"
maker: "aidreamy"
license: "Apache-2.0"
url: "https://github.com/aidreamy/co-sh"
source_code_url: "https://github.com/aidreamy/co-sh"
source_available: "True"
homepage: "https://www.co-sh.com"
docs_url: "https://www.co-sh.com/docs"
download_url: "https://github.com/aidreamy/co-sh/releases"
install_method: "curl -fsSL https://raw.githubusercontent.com/aidreamy/co-sh/main/download.sh | bash (Linux/macOS; Windows via download.ps1 in PowerShell or Git Bash/WSL), then run cosh"
platforms:
  - "CLI"
autonomy_level:
  - "pair-programmer"
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-06-01"
current_release: "2026-11-16"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: null
model_providers: "Claude, OpenAI, Gemini, plus OpenAI-compatible providers (Bedrock, Kimi, Groq, OpenRouter, Nvidia, more) and local servers (Ollama, LM Studio, vLLM, llama.cpp)"
pricing: "BYOK"
stars: "14"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A Rust TUI coding agent whose computer-use tools read and drive graphical applications through the OS accessibility tree instead of screenshot loops, and whose /agents and Manager modes run external harnesses like Claude, Codex and Gemini in split panes under the built-in agent's dispatch."
---

co-sh is a general-purpose terminal coding agent written in Rust by Diego Zaluski, positioned as a companion to established agents rather than a replacement. The built-in harness owns the default experience: build, ask and yolo modes drive its own file, search, shell, LSP and web tools, plus computer tools that observe and operate native desktop applications through a structured accessibility-tree representation, falling back to screenshots only when needed. On top of that, a /agents mode runs external harnesses such as Claude, Codex, Gemini and Cline in split panes — each with its own session, model and optional git worktree — with the main agent dispatching tasks and collecting reports, and a Manager mode keeps orchestration over your existing CLIs across multiple small tasks. Providers, models and modes are configured inside the Ratatui TUI rather than in config files, the building blocks ship as reusable crates (cosh-tools, cosh-tui, cosh-sdk, cosh-recall), and the project moved to the aidreamy organization in November 2026 with v0.3.0 out. It suits developers who like trying different agents and combining their strengths in one terminal.
