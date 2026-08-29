---
name: "deepseek-cli"
slug: "deepseek-cli"
layout: "agent.njk"
category: "agent"
maker: "holasoymalva"
license: "MIT"
url: "https://github.com/holasoymalva/deepseek-cli"
source_code_url: "https://github.com/holasoymalva/deepseek-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-06-25"
current_release: "2026-07-23"
stars: "299"
language: "TypeScript"
homepage: "https://deepseek-cli.vercel.app/"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "no"
model_providers: "DeepSeek (Coder 1.3B, 6.7B, 33B) via local Ollama or DeepSeek cloud API"
pricing: null
install_method: "npm install -g run-deepseek-cli"
docs_url: "https://github.com/holasoymalva/deepseek-cli/blob/main/docs/index.md"
plugin_docs_url: null
config_docs_url: "https://github.com/holasoymalva/deepseek-cli/blob/main/docs/configuration.md"
download_url: "https://www.npmjs.com/package/run-deepseek-cli"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Command-line AI coding assistant powered by DeepSeek Coder models; supports both local mode (via Ollama, free & private) and cloud mode (API key). Features code completion/generation across 100+ languages, repository-level code understanding, refactoring/migration, debugging/code review, project scaffolding, and an interactive REPL with syntax highlighting and session history."
---

deepseek-cli adapts the Gemini CLI codebase to DeepSeek Coder models, giving terminal users code generation, repository-level analysis, refactoring, debugging, and project scaffolding across roughly 100 languages. Its local mode runs DeepSeek Coder 1.3B/6.7B/33B through Ollama at no cost and entirely on-device, which the README recommends over the cloud mode that uses a DeepSeek platform API key. The interactive REPL supports session history, file-context inclusion, and model switching, and the project is MIT-licensed TypeScript installable via npm. With 14 commits and no releases since its initial push, it is best understood as a community fork demonstrating the Gemini CLI architecture on DeepSeek models rather than a product under active development.
