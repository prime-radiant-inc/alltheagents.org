---
name: "ForgeCode"
slug: "forgecode"
layout: "agent.njk"
category: "agent"
maker: "tailcallhq"
license: "Apache-2.0"
url: "https://github.com/tailcallhq/forgecode"
source_code_url: "https://github.com/tailcallhq/forgecode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2024-12-08"
current_release: "2026-08-19"
stars: null
language: "Rust"
homepage: "https://forgecode.dev"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google Vertex AI, Groq, OpenRouter, Requesty, x-ai, z.ai, Cerebras, Neuralwatt, OrcaRouter, Meta, IO Intelligence, Amazon Bedrock, ForgeCode Services, OpenAI-compatible"
pricing: "open-source"
install_method: "curl -fsSL https://forgecode.dev/cli | sh"
docs_url: "https://github.com/tailcallhq/forgecode/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jqueryscript"
  - "ishandutta"
what_makes_it_special: "ZSH plugin with colon prefix system (use AI without leaving shell), three-mode architecture (TUI/CLI one-shot/ZSH plugin), semantic code search, conversation management with branching/cloning, sandbox mode via git worktrees, custom agents/skills/commands system, 300+ models."
---

ForgeCode, built by Tailcall HQ, offers three surfaces over one Rust core: an interactive TUI, a one-shot CLI (`forge -p` for prompts, `forge commit` for AI commit messages, `forge suggest` for natural-language shell commands), and a ZSH plugin where colon-prefixed commands invoke agents without leaving the shell. Three built-in agents divide labor — forge implements code, sage researches read-only, muse writes plans — drawing on 300+ models across OpenAI, Anthropic, Google Vertex AI, Bedrock, OpenRouter, Groq, and OpenAI-compatible endpoints. Conversations persist with resume, clone, and compact operations, semantic workspace indexing speeds context assembly, and forge.yaml plus AGENTS.md configure rules and tool limits. A sandboxed git-worktree mode and restricted shell give teams a safety story for daily-driver adoption.
