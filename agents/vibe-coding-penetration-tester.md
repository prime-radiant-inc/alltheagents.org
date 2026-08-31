---
name: "vibe-coding-penetration-tester"
slug: "vibe-coding-penetration-tester"
layout: "agent.njk"
category: "other"
maker: "firetix"
license: "Apache-2.0"
url: "https://github.com/firetix/vibe-coding-penetration-tester"
source_code_url: "https://github.com/firetix/vibe-coding-penetration-tester"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-03-19"
current_release: "2026-06-08"
stars: "175"
language: "Python"
homepage: "https://www.vibehack.io/"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "False"
model_providers: "OpenAI, Anthropic, Ollama"
pricing: "Free / open source for local use; optional hosted/billing mode with Stripe for SaaS deployments"
install_method: "git clone, python -m venv .venv, source .venv/bin/activate, pip install -r requirements.txt, playwright install, cp .env.example .env"
docs_url: "https://github.com/firetix/vibe-coding-penetration-tester#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/firetix/vibe-coding-penetration-tester"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "AI-assisted web application security testing tool (VibePenTester) with CLI and Flask web interfaces. Coordinates specialized security agents to discover and validate common web vulnerabilities. Features Playwright-powered browser automation, scope-aware scanning (url/domain/subdomain levels), dual output formats (Markdown + JSON reports), multi-agent scan workflow, and both CLI and web UI/API with session-based orchestration. Note: license discrepancy between README (GPL-3.0) and repo metadata (Apache-2.0)."
---

The tool exists because 'vibe-coded' applications reach production without security validation, and existing scanners miss logic-level vulnerabilities that require realistic interaction. Its workflow assigns specialized agents to a scan: discovery enumerates the target within a scope (url, domain, or subdomain), a planning agent prioritizes what to test, and vulnerability-testing agents probe common web vulnerability classes through a Playwright-driven browser that interacts with the application as a user would. Findings are validated and written into reproducible Markdown and JSON reports per target, with a Flask web UI and REST API available for session-based operation and sample reports plus a Juice Shop walkthrough included. Security-minded developers testing their own or authorized applications are the users; the project is Python-based, carries CI and a substantial test suite, and warns explicitly that it must only be used against owned or authorized targets.
