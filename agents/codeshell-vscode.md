---
name: "codeshell-vscode"
slug: "codeshell-vscode"
layout: "agent.njk"
category: "other"
maker: "WisdomShell"
license: "Apache-2.0"
url: "https://github.com/WisdomShell/codeshell-vscode"
source_code_url: "https://github.com/WisdomShell/codeshell-vscode"
source_available: "True"
platforms: []
first_released: "2023-10-19"
current_release: "2024-05-09"
stars: "575"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "CodeShell"
pricing: "open-source"
install_method: "vscode"
docs_url: "https://github.com/WisdomShell/codeshell-vscode"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Intelligent coding assistant for VSCode built on the CodeShell LLM; supports code completion, code explanation/optimization/cleanup, comment/unit test generation, performance/security checks, and multi-turn chat with session history"
---

codeshell-vscode is the VS Code client for WisdomShell's CodeShell model family, built for developers who want a coding assistant fully inside their own infrastructure. The extension provides auto-triggered inline completion (configurable delay, Tab to accept), right-click code actions that explain, optimize, or clean up code, generate comments and unit tests, and check performance and security issues, plus multi-turn chat with session history and code-block insertion. It requires a self-hosted CodeShell backend: either llama.cpp serving the 4-bit quantized chat GGUF on CPU, or Text Generation Inference running CodeShell-7B or CodeShell-7B-Chat on GPU. Development stopped in mid-2024; the repository has 55 commits, no releases, and 23 open issues without responses, and documentation is primarily in Chinese.
