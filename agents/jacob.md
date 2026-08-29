---
name: "JACoB"
slug: "jacob"
layout: "agent.njk"
category: "agent"
maker: "Renaissance-Innovation-Labs"
license: "Apache-2.0"
url: "https://jacb.ai"
source_code_url: "https://github.com/Renaissance-Innovation-Labs/jacob-ai"
source_available: "True"
platforms: []
first_released: "2024-09-17"
current_release: "2024-09-16"
stars: "1"
language: "TypeScript/JavaScript (Next.js, tRPC, Tailwind, Orchid ORM)"
homepage: "https://jacb.ai"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: "OpenAI, Ollama, PortKey"
pricing: "Self-hosted free/open-source (requires own OpenAI API key); hosted version exists but pricing not detailed"
install_method: "Hosted: sign up at jacb.ai/signup. Self-hosted: clone repo, create GitHub App, configure .env, docker compose up -d, npm install, npm run db create & npm run db migrate, npm run dev. Also requires Figma plugin install and npx jacob-setup create in target projects."
docs_url: "https://docs.jacb.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Renaissance-Innovation-Labs/jacob-ai"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Open-source AI coding bot that automates development tasks, transforms Figma designs into deployable code, and integrates into GitHub workflows via webhooks (Issues, PRs, reviews). Learns your coding style to generate project-aligned code. Figma-to-code via dedicated plugin. Customizable via JSON config (jacob.config). Privacy-focused (no codebase storage, no data training). Outperformed 7 top design-to-code tools in their JACoB Arena benchmark. Forked from adamloving/jacob."
---

JACoB positions itself beyond autocomplete: assign it a GitHub issue or a Figma design and it produces a complete pull request, having mapped the repository to match existing patterns. A Figma plugin hands it design context, and webhooks let it respond to issues, PRs, and reviews without leaving GitHub. Behavior is tuned through a jacob.config JSON file in the repo, and the project emphasized privacy — no codebase storage, no training on user code — alongside a JACoB Arena benchmark where it compared itself against seven design-to-code tools. The site went dark around December 2025 (jacb.ai no longer resolves), so the entry now stands on the archived Apache-2.0 codebase.
