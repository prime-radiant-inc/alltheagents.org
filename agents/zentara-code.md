---
name: "Zentara-Code"
slug: "zentara-code"
layout: "agent.njk"
category: "agent"
maker: "Zentar-Ai"
license: "Apache-2.0"
url: "https://github.com/Zentar-Ai/Zentara-Code"
source_code_url: "https://github.com/Zentar-Ai/Zentara-Code"
source_available: "True"
platforms: []
first_released: "2025-06-04"
current_release: "2026-03-17"
stars: "84"
language: "TypeScript"
homepage: "https://zentar.ai"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Claude (Anthropic)"
pricing: "open-source"
install_method: "VS Code Marketplace (search 'Zentara Code'); from source: pnpm install && pnpm vsix"
docs_url: "https://zentar.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "VS Code extension AI coding assistant and debugger, a mod/fork of Roo-Code (which derives from Cline). Features parallel subagents with isolated contexts, 25+ LSP semantic tools, runtime debugging with 35+ operations (launch, step, breakpoints, state inspection), plan/approve/execute/verify workflow, tool integration for custom extensions, and /init project analysis command. Optimized for speed, safety, and correctness via parallel execution and LSP semantics."
---

Zentara-Code addresses a gap in chat-driven coding assistants: they can write code but cannot observe it executing, so verification rests on assumptions. Built as a fork of Roo-Code (which descends from Cline), the extension exposes the debugger to the agent — launch and restart sessions, conditional and temporary breakpoints, stepping, stack and variable inspection, and expression evaluation, roughly 35 operations in total. Code intelligence rides the Language Server Protocol rather than text matching, giving the agent semantic usages, call hierarchies, safe renames, and workspace symbol search across 25+ tools. Work follows an explicit pipeline: the agent decomposes a request into steps and proposes an execution order, the user approves impactful actions, parallel subagents with isolated contexts and opt-in write permissions handle independent pieces, and a verification pass exercises the result in the debugger. Custom agent definitions and modes are configurable through project files, and an /init command analyzes a codebase to generate AI-friendly documentation. The extension is free under Apache-2.0, installed from the VS Code Marketplace, with a Claude Max subscription recommended for model access; teams adopting it tend to be those debugging behavior where static chat suggestions repeatedly miss.
