---
name: "open-aware"
slug: "open-aware"
layout: "agent.njk"
category: "other"
maker: "qodo-ai"
license: "MIT"
url: "https://github.com/qodo-ai/open-aware"
source_code_url: "https://github.com/qodo-ai/open-aware"
source_available: "True"
platforms: []
first_released: "2025-07-16"
current_release: "2025-10-29"
stars: "502"
language: "TypeScript"
homepage: "https://www.qodo.ai/products/qodo-aware/"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none (model-agnostic; the calling client's model invokes the MCP tools)"
pricing: "Free public access (~10 calls/min); paid enterprise plans (Qodo Aware) for private repos, custom indexing, high/unlimited usage"
install_method: "Add MCP server config: {'mcpServers':{'open-aware':{'url':'https://open-aware.qodo.ai/mcp'}}}  (or via npm install -g mcp-remote proxy)"
docs_url: "https://www.qodo.ai/products/qodo-aware/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-aware.qodo.ai/mcp"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Semantic code intelligence across multiple repositories simultaneously (cross-repo analysis) exposed via MCP, with daily updated indexes of popular OSS libraries and vector embeddings. Provides get_context (semantic code search), deep_research (architecture/implementation analysis), and ask (coding questions) tools."
---

Coding agents frequently misanswer questions about third-party libraries because their training data is stale and the repositories involved are too large to clone on demand. Qodo's Open Aware closes that gap by maintaining daily-updated indexes of popular open-source repositories and exposing them over a public MCP endpoint with three tools: get_context for semantic code search across multiple repositories at once, deep_research for architecture analysis and implementation planning, and ask for direct coding questions. Clients connect via Streamable HTTP or an mcp-remote proxy with no local indexing, and a Gemini CLI extension exists for that ecosystem. The free tier is rate-limited to roughly ten calls per minute and covers only the pre-indexed public repositories; private repos and custom indexing require the commercial Qodo Aware product. It suits developers whose agents need ground truth about dependencies and cross-repository architecture rather than another local search tool.
