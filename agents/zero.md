---
name: "zero"
slug: "zero"
layout: "agent.njk"
category: "agent"
maker: "Gitlawb"
license: "MIT"
url: "https://github.com/Gitlawb/zero"
source_code_url: "https://github.com/Gitlawb/zero"
source_available: True
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

Fully local, user-owned terminal coding agent emphasizing control and privacy. Model-agnostic (25+ providers), explicit permission-gated safety model (file writes, shell, network, elevated actions all sandboxed; secrets redacted), dual-mode operation (rich interactive TUI + scriptable headless 'zero exec' with stream-JSON I/O for CI). Sessions stored on disk, searchable, resumable, never uploaded. Extensible via MCP, plugins, hooks, skills, and specialist subagents. Reads AGENTS.md/ZERO.md hierarchically. Platform binaries ship as optional npm dependencies to avoid trust concerns.
