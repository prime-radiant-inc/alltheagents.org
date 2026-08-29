---
name: "clio"
slug: "clio"
layout: "agent.njk"
category: "agent"
maker: "icebear0828"
license: "MIT"
url: "https://github.com/icebear0828/clio"
source_code_url: "https://github.com/icebear0828/clio"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-27"
current_release: "2026-04-03"
stars: "184"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic, OpenAI-compatible (via --api-format openai), custom gateways/proxies"
pricing: "Free / open source (MIT); users pay their own API costs"
install_method: "git clone, npm install, npm run build, npm link (global); or npm run dev for development"
docs_url: "https://github.com/icebear0828/clio#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/icebear0828/clio"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Feature-rich Claude Code clone in TypeScript (~9200 lines, 46 source files) with prompt caching (~90% input token savings), 21 built-in tools, zero external runtime dependencies, MCP support (JSON-RPC 2.0 over stdio), manifest-driven plugins, custom subagents with git worktree isolation, agent teams with inter-agent messaging, checkpoint rollback, LSP integration, extended thinking mode, and 4-level settings hierarchy."
---

Clio's value is architectural: it demonstrates that a complete agentic coding assistant - 21 tools, three permission modes, subagents, hooks, sessions, and MCP discovery - fits in roughly 9,200 lines of TypeScript with essentially no runtime dependencies beyond fast-glob. Prompt caching is applied at section level across system prompt, tools, and message history, cutting input token cost around 90 percent, with model-aware context limits and auto-compaction at 85 percent. Tools are tiered safe/write/dangerous and gated by default, auto, and plan modes with glob rules. It targets the Anthropic API and OpenAI-compatible endpoints, and remains a young project with a small commit history and no packaged releases.
