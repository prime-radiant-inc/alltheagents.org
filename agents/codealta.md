---
name: "CodeAlta"
slug: "codealta"
layout: "agent.njk"
category: "multiplexer"
maker: "CodeAlta"
license: "BSD-2-Clause"
url: "https://github.com/CodeAlta/CodeAlta"
source_code_url: "https://github.com/CodeAlta/CodeAlta"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-25"
current_release: "2026-08-07"
stars: "221"
language: "C# / .NET"
homepage: "https://codealta.github.io"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Codex,Copilot,xAI Grok,OpenAI,Azure OpenAI,Alibaba APIs,Anthropic,Gemini/Vertex,custom endpoints"
pricing: "free"
install_method: "dotnet tool install -g CodeAlta"
docs_url: "https://codealta.github.io/"
plugin_docs_url: "https://codealta.github.io/"
config_docs_url: null
download_url: "https://www.nuget.org/packages/CodeAlta/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Terminal workspace (TUI) for agentic coding — model-provider setup, project navigation, prompt attachments, durable sessions, delegated work, and trusted local plugins via the alta command. Supports source plugins, Agent Skills skill folders, and in-session alta live tool."
---

CodeAlta organizes the workspace around agentic coding rather than adding another agent runtime: a keyboard-driven TUI holds provider configuration, a project sidebar, a prompt editor with @ file attachments and # GitHub issue search, and durable project-scoped session journals that support queuing, steering, and compaction. Sessions survive across restarts, and the interface tracks modified files, usage, and logs while remaining provider-neutral across Codex, Copilot, Grok, OpenAI/Azure, Anthropic, Gemini/Vertex, Alibaba, and custom endpoints. Extension points are local and trust-based: source plugins, Agent Skills-compatible skill folders, and an in-session alta live tool for automating the workspace itself. It is written in C# for .NET 10, installed as a dotnet global tool, requires a Nerd Fonts-patched terminal, and is explicitly marked pre-release by author Alexandre Mutel.
