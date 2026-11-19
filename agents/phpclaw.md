---
name: "phpClaw"
slug: "phpclaw"
layout: "agent.njk"
category: "agent-sdk"
maker: "phpclaw-php"
license: "MIT"
url: "https://github.com/phpclaw-php/phpclaw-monorepo"
source_code_url: "https://github.com/phpclaw-php/phpclaw-monorepo"
source_available: "True"
homepage: "https://phpclaw.ai"
docs_url: "https://phpclaw.ai/docs"
download_url: null
install_method: "composer require phpclaw/phpclaw (PHP 8.1+, ext-curl/json/mbstring); CMS adapters are ZIP uploads from GitHub Releases; MCP server: composer require phpclaw/phpclaw-mcp"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "PHP"
first_released: "2026-09-23"
current_release: "2026-10-16"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Anthropic, OpenAI, Groq, Gemini, Mistral, DeepSeek, Ollama (auto-detected from env vars), plus any custom OpenAI-compatible endpoint"
pricing: "free"
stars: "32"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A PHP-native agent engine that ships the whole runtime — ReAct loop, tool registry, swappable memory, 8 default security guards, 44 lifecycle hooks, and 8 framework/CMS adapters — with zero framework dependencies in core."
---

Every 'AI in PHP' tutorial ends with an HTTP client bolted onto a provider API and a hand-rolled tool-calling loop, so phpClaw ships the runtime instead: a ReAct engine with a hard iteration cap, pluggable tools, pluggable memory drivers, and skills the model loads on demand through a load_skill tool. Developers register the tools their application needs — ShellTool (allowlist-only, with a fixed blocklist), HttpTool (validates resolved IPs against DNS-rebinding), sandboxed FileRead/FileWrite, DatabaseQueryTool, CodeSearchTool — and the agent decides which to call and in what order. Eight framework and CMS adapters (Laravel, Symfony, Drupal, Magento, WordPress, Joomla, OpenCart, PrestaShop) wire the same three-table memory schema into each host's idioms, and Pipeline and Graph classes chain agents into steps that loop, branch, pause for a human, and fan out to workers. The intended users are PHP and Laravel shop developers embedding an agent inside an existing application rather than running one in a terminal, and the bundled MCP server can also expose those tools to Claude Desktop, Claude Code, or Cursor.
