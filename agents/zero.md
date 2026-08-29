---
name: "zero"
slug: "zero"
layout: "agent.njk"
category: "agent"
maker: "Gitlawb"
license: "MIT"
url: "https://github.com/Gitlawb/zero"
source_code_url: "https://github.com/Gitlawb/zero"
source_available: "True"
platforms: []
first_released: "2026-05-28"
current_release: "2026-08-19"
stars: "1590"
language: "Go"
homepage: "https://zero.gitlawb.com"
mcp_support: "yes - stdio; zero mcp manages MCP servers/tools, zero serve --mcp exposes Zero tools over MCP"
plugin_support: "yes - plugins from ~/.config/zero/plugins/ or <cwd>/.zero/plugins/, managed via zero plugins; manifest declares tools/hooks/prompts/skills"
claude_code_plugin: "no"
subagents: "yes - specialist subagents via zero specialist"
hooks: "yes - lifecycle hooks (beforeTool, afterTool, sessionStart, sessionEnd)"
plan_mode: "yes - /spec and /plan commands draft/review plans before building"
model_providers: "OpenAI, Anthropic, Gemini, Groq, OpenRouter, DeepSeek, Mistral, xAI, Qwen, Kimi, GitHub Models, Ollama, LM Studio, AIMLAPI, LongCat, Fireworks AI, MiniMax, + any OpenAI/Anthropic-compatible endpoint"
pricing: "open-source"
install_method: "npm"
docs_url: "https://zero.gitlawb.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Fully local, user-owned terminal coding agent emphasizing control and privacy. Model-agnostic (25+ providers), explicit permission-gated safety model (file writes, shell, network, elevated actions all sandboxed; secrets redacted), dual-mode operation (rich interactive TUI + scriptable headless 'zero exec' with stream-JSON I/O for CI). Sessions stored on disk, searchable, resumable, never uploaded. Extensible via MCP, plugins, hooks, skills, and specialist subagents. Reads AGENTS.md/ZERO.md hierarchically. Platform binaries ship as optional npm dependencies to avoid trust concerns."
---

Zero targets the trust gap that keeps some developers from adopting terminal coding agents: hosted tools that upload context, opaque approval models, and single-vendor lock-in. Written in Go and installed via npm (wrapping optional platform binaries, a packaging choice made deliberately to limit supply-chain surface), the agent keeps everything local — sessions persist to disk, remain searchable and resumable, and never leave the machine. Its safety model is explicit rather than gradient: workspace-only file writes by default, individually gated shell, network, and elevated actions, secret redaction in context, and an autonomous mode that must be opted into. The interactive TUI covers daily use with plan rendering, image input, and slash commands, while a headless zero exec mode emits stream-JSON and proper exit codes so the same agent drives CI jobs, with a documented GitHub Action. Extensibility is layered: MCP servers and a built-in MCP server mode, plugins declaring tools and hooks in manifest files, lifecycle hooks on tool calls and session events, skills, and specialist subagents for named roles. Configuration and context come from hierarchical AGENTS.md and ZERO.md files. Model support spans 25+ providers including local Ollama and LM Studio, matching the local-first premise; the audience is developers who want Claude Code-class capability without ceding custody of their code or credentials.
