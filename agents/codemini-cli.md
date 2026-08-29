---
name: "Codemini-CLI"
slug: "codemini-cli"
layout: "agent.njk"
category: "agent"
maker: "havingautism"
license: "MIT"
url: "https://github.com/havingautism/Codemini-CLI"
source_code_url: "https://github.com/havingautism/Codemini-CLI"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-03-27"
current_release: "2026-08-19"
stars: "191"
language: "JavaScript (Node.js)"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "OpenAI-compatible, Anthropic"
pricing: "Free / open-source"
install_method: "npm install -g codemini-cli"
docs_url: "https://github.com/havingautism/Codemini-CLI/blob/main/OPERATIONS.md"
plugin_docs_url: null
config_docs_url: "https://github.com/havingautism/Codemini-CLI/blob/main/deployment.md"
download_url: "https://www.npmjs.com/package/codemini-cli"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Restrained coding + tasks CLI with both TUI and browser Web UI sharing the same runtime; minimizes unnecessary context usage via managed compaction, lazy-loaded skills, project-aware retrieval (Tree-sitter AST, dependency/knowledge graphs, CodeWiki), proportional risk-based approvals, local persistence, and Microsandbox isolation. All sessions, memory, and state remain local."
---

Codemini-CLI is a terminal-first agent for coding and operational tasks, built around minimizing unnecessary context consumption: managed compaction, lazy-loaded skills, and project-aware retrieval through Tree-sitter AST parsing, dependency and knowledge graphs, and a generated CodeWiki keep prompts small. Its tool runtime includes plans, todos, subagents, background tasks, and parallel tool calls, with approvals proportional to the risk of each change and sandbox modes from read-only through workspace-write to full access, optionally backed by Microsandbox microVMs with Landlock/Seatbelt fallbacks. Claude-compatible hooks observe or gate lifecycle events, and MCP servers extend the tool surface without runtime changes. A TUI and a browser Web UI share the same session engine and local persistence, so a session started in the terminal continues in the browser.
