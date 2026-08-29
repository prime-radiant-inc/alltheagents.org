---
name: "sage"
slug: "sage"
layout: "agent.njk"
category: "multiplexer"
maker: "youwangd"
license: "MIT"
url: "https://github.com/youwangd/SageCLI"
source_code_url: "https://github.com/youwangd/SageCLI"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-03-13"
current_release: "2026-04-27"
stars: "5"
language: "Bash"
homepage: "https://youwangd.github.io/posts/sage-cli"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Claude Code, Gemini CLI, Codex, Cline, Kiro, Ollama, llama.cpp, ACP (Agent Client Protocol), Bash"
pricing: "Free / open-source (MIT)"
install_method: "Homebrew: brew tap youwangd/sage && brew install sage; or curl -fsSL https://raw.githubusercontent.com/youwangd/SageCLI/main/install.sh | bash; or manual git clone + symlink. Requires: bash 4.0+, jq 1.6+, tmux 3.0+"
docs_url: "https://github.com/youwangd/SageCLI/blob/main/docs/USAGE.md"
plugin_docs_url: null
config_docs_url: "https://github.com/youwangd/SageCLI/blob/main/docs/COMMANDS.md"
download_url: "https://raw.githubusercontent.com/youwangd/SageCLI/main/install.sh"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Vendor-neutral orchestration layer (8+ runtimes, swap backends with one flag, vendor kill-switch fallback). Zero-dependency single bash script (no venv/node/npm). Unix-native (JSON out, stdin in, pipes like git/kubectl/jq). Bench-as-code for comparing agents. Works on local models with zero cloud. 53 commands, 928 tests."
---

Teams running several agent CLIs accumulate incompatible invocation styles, session stores, and failure modes; Sage normalizes them behind one command surface with messages as files under ~/.sage and agents running in tmux windows. Its 53 commands cover multi-agent create/send/peek, parallel multi-runtime execution, headless CI mode, guardrails, shared memory, and token/cost tracking, and `sage bench` compares agents on real tasks as code. The acp runtime speaks JSON-RPC 2.0 over stdio so any Agent Client Protocol agent joins the fleet without a custom adapter, and local models via Ollama or llama.cpp are first-class runtimes. Being bash means it installs in seconds with no venv or node_modules, which suits CI and air-gapped environments. The project is MIT-licensed, actively developed through a documented roadmap, and so far a solo effort with small adoption.
