---
name: "sage"
slug: "sage"
layout: "agent.njk"
category: "multiplexer"
maker: "youwangd"
license: "MIT"
url: "https://github.com/youwangd/SageCLI"
source_code_url: "https://github.com/youwangd/SageCLI"
source_available: True
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-03-13"
current_release: "2026-04-27"
stars: "5"
language: "Bash"
homepage: "https://youwangd.github.io/posts/sage-cli"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: True
hooks: null
plan_mode: True
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

Vendor-neutral orchestration layer (8+ runtimes, swap backends with one flag, vendor kill-switch fallback). Zero-dependency single bash script (no venv/node/npm). Unix-native (JSON out, stdin in, pipes like git/kubectl/jq). Bench-as-code for comparing agents. Works on local models with zero cloud. 53 commands, 928 tests.
