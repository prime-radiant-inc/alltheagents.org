---
name: "codevibes"
slug: "codevibes"
layout: "agent.njk"
category: "other"
maker: "danish296"
license: "MIT"
url: "https://github.com/danish296/codevibes"
source_code_url: "https://github.com/danish296/codevibes"
source_available: "True"
platforms: []
first_released: "2026-01-06"
current_release: "2026-01-12"
stars: "255"
language: "TypeScript"
homepage: "https://codevibes.akadanish.dev"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "DeepSeek"
pricing: "Free / open-source (beta)"
install_method: "git clone + npm install (requires Node.js v18+, DeepSeek API key)"
docs_url: "https://codevibes.akadanish.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/danish296/codevibes"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Free, open-source AI code review alternative to CodeRabbit. Uses DeepSeek AI for security vulnerability detection, bug/performance analysis, and code quality review. Priority-based three-tier scanning system (P1 security → P2 core logic → P3 quality). Provides a quantifiable 0-100 Vibe Score. Real-time streaming analysis via SSE. Stores analysis history locally in SQLite."
---

CodeVibes provides AI code review for developers who cannot justify a paid review service: a web dashboard where a GitHub repository URL yields security findings, bug and performance issues, and quality observations, condensed into a 0-100 score. Analysis runs on DeepSeek models (deepseek-chat or deepseek-reasoner) with a user-supplied free API key, organized as a priority pipeline — security first, then core-logic defects, then style and quality — with results streaming in real time over server-sent events. The application is a TypeScript monorepo: a React 18 and Vite frontend, an Express backend storing analysis history in SQLite via Better-SQLite3, and Octokit for GitHub access. It is a beta-stage single-author project with a dozen commits, self-described as an affordable CodeRabbit alternative.
