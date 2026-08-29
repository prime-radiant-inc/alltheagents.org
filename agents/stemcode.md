---
name: "StemCode"
slug: "stemcode"
layout: "agent.njk"
category: "agent"
maker: "rizwan3d"
license: "Apache-2.0"
url: "https://github.com/rizwan3d/StemCode"
source_code_url: "https://github.com/rizwan3d/StemCode"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Desktop"
first_released: "2026-04-18"
current_release: "2026-08-19"
stars: "31"
language: "C# / .NET"
homepage: "https://rizwan3d.github.io/StemCode/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI, ChatGPT Plus/Pro sign-in, Anthropic Claude Pro/Max sign-in, GitHub Copilot sign-in, OpenRouter, OpenCode Zen, Kilo Code, Cerebras, Groq, DeepSeek, Google AI Studio, Ollama, LM Studio, Ollama Cloud, OpenAI-compatible"
pricing: "Free/open source"
install_method: "Desktop app from GitHub Releases; CLI via install script (curl/PowerShell), npm/pnpm/bun, or NuGet"
docs_url: "https://github.com/rizwan3d/StemCode/blob/master/docs/documentation.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/rizwan3d/StemCode/releases/latest"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Local-first AI coding agent for desktop, terminal, editor (VS Code, Visual Studio, JetBrains), and CI workflows. Works inside a real local repository (not a detached chat sandbox), keeps the human in control with approval prompts/permissions/profiles, stores reusable commands and team memory in versionable .stemcode/ files, reuses the same agent across desktop/CLI/IDE/CI. Profiles include planning, implementation, review, exploration, and delegated work modes. Includes local voice dictation and automatic AI git commits scoped to changed files."
---

StemCode is built around operating inside a real local repository rather than a detached chat sandbox: repository-aware search, LSP symbol intelligence, and graph-aware indexing feed surgical tracked edits (patches, insertions, search/replace) with undo/redo, while permission rules and approval prompts gate sensitive actions. The same engine ships as a desktop app, a CLI, editor extensions, and CI jobs, so the agent that plans locally can also run in GitHub Actions or GitLab CI. Profiles switch behavior between implementation, planning, review, and exploration postures, subagents take delegated tasks in independent contexts, and slash commands plus project memory persist in .stemcode. Model access is deliberately broad, from subscription sign-ins (ChatGPT, Claude, Copilot) to OpenRouter, Ollama, LM Studio, and any OpenAI-compatible endpoint. It is Apache-2.0 and free, positioned for developers who want agent assistance without their code leaving the machine.
