---
name: "lsp-mcp"
slug: "lsp-mcp"
layout: "agent.njk"
category: "agent"
maker: "jonrad"
license: "MIT"
url: "https://github.com/jonrad/lsp-mcp"
source_code_url: "https://github.com/jonrad/lsp-mcp"
source_available: True
platforms:
  - "IDE"
first_released: "2025-02-23"
current_release: "2025-03-31"
stars: "191"
language: "TypeScript"
homepage: null
mcp_support: True
plugin_support: null
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open-source"
install_method: "docker run -i --rm docker.io/jonrad/lsp-mcp:0.3.1 (recommended); or npx -y --silent git+https://github.com/jonrad/lsp-mcp"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://hub.docker.com/r/jonrad/lsp-mcp"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "MCP server bridging LSP to MCP, giving AI agents real language-aware code analysis (scope, types, shadowing, etc.) instead of relying on text parsing. Dynamically generates supported LSP methods from JSON schema and supports multiple language servers simultaneously; works with Claude Desktop, Cursor, and MCP CLI Client."
---

MCP server bridging LSP to MCP, giving AI agents real language-aware code analysis (scope, types, shadowing, etc.) instead of relying on text parsing. Dynamically generates supported LSP methods from JSON schema and supports multiple language servers simultaneously; works with Claude Desktop, Cursor, and MCP CLI Client.
