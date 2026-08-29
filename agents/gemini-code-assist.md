---
name: "Gemini Code Assist"
slug: "gemini-code-assist"
layout: "agent.njk"
category: "agent"
maker: "Google"
license: "Proprietary (IDE extensions); Apache-2.0 (CLI)"
url: "https://codeassist.google"
source_code_url: null
source_available: "True"
platforms:
  - "IDE"
first_released: "2024"
current_release: "2026"
stars: null
language: "TypeScript"
homepage: "https://codeassist.google"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Google (Gemini)"
pricing: "Standard: $22.80/user/month (monthly) or $19/user/month (annual). Enterprise: $54/user/month (monthly) or $45/user/month (annual). 30-day free trial available for up to 50 users. CLI is free with 60 req/min and 1000 req/day."
install_method: "IDE extensions via marketplace (VS Code, JetBrains) or CLI via npx/npm/homebrew"
docs_url: "https://developers.google.com/gemini-code-assist/docs/overview"
plugin_docs_url: null
config_docs_url: "https://developers.google.com/gemini-code-assist/docs/overview"
download_url: "https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "1M token context window, enterprise security and IP indemnification, code customization using private codebases, deep integration with Google Cloud services (Firebase, BigQuery, Apigee, Application Integration). Agent mode supports MCP integration. CLI is fully open source (Apache-2.0)."
---

Gemini Code Assist is Google's business-facing coding assistant, spanning VS Code, JetBrains, Cloud Workstations, Cloud Shell, and the terminal through the Gemini CLI. Its agent mode moves past chat into multi-file edits with full project context, built-in tools, MCP ecosystem integration, and human-in-the-loop approval, grounded in Gemini 3 with a 1M-token context window and private-codebase customization. Pricing runs $19-22.80 per user per month on Standard and $45-54 on Enterprise, with a 30-day trial and a free CLI tier of 60 requests per minute and 1,000 per day. The individual free tier was folded into Antigravity in June 2026, leaving the paid product focused on enterprises that need Google Cloud integration and indemnification.
