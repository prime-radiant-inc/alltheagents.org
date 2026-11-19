---
name: "CoderBaba"
slug: "coderbaba"
layout: "agent.njk"
category: "agent"
maker: "CoderBaba-si"
license: "MIT"
url: "https://github.com/CoderBaba-si/CoderBaba"
source_code_url: "https://github.com/CoderBaba-si/CoderBaba"
source_available: "True"
homepage: "https://coderbaba.si"
docs_url: "https://github.com/CoderBaba-si/CoderBaba#readme"
download_url: null
install_method: "npx coderbaba (or npm install -g coderbaba); requires Node.js 20+"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "TypeScript"
first_released: "2026-11-08"
current_release: "2026-11-11"
maintained: "active"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: null
subagents: "False"
hooks: "False"
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://github.com/CoderBaba-si/CoderBaba#configuration"
model_providers: "Hosted open models via CoderBaba's free cloud (Fast = Cohere North Mini Code, Smart = Qwen3-Coder-Next, both through OpenRouter with data collection denied); optional OpenRouter key for direct calls"
pricing: "freemium"
stars: "7"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A free terminal coding agent that closes its own loop after every edit — running the project's type checks, lint, and audits, starting the dev server, and testing pages in headless Chrome — and folds in /security and /seo project scanners plus /undo checkpoints that work without git."
---

CoderBaba is aimed at beginners, students, and developers who want a terminal agent that runs and verifies the app rather than only writing code: you describe a task in plain English and it reads the project, writes a todo list, edits files with targeted changes, installs dependencies, and starts the dev server. After every edit it runs the project's own checks — TypeScript and ESLint, Django's manage.py check, dependency audits — and fixes what they report, up to two rounds; when a page is running it opens it in headless Chrome to catch console errors, crashes, and failed requests that curl cannot see. Its agent loop lives in a UI-free core package with file, shell, browser, and URL tools behind an injected permission callback, so the CLI asks before every edit or command and /undo reverts any turn from per-file checkpoints. Beyond coding, /security maps the app and writes a reproducible SECURITY_REPORT.md of real breach classes (IDOR, injection, XSS, plaintext secrets), and /seo audits search engines, AI-answer visibility, speed, and WCAG 2.2 AA accessibility. Model access is through CoderBaba's free cloud on open models (1,000 free tasks per device, more with a free email login), with an optional OpenRouter key for direct calls.
