---
name: "octo-web"
slug: "octo-web"
layout: "agent.njk"
category: "multiplexer"
maker: "Mininglamp-OSS"
license: "Apache-2.0"
url: "https://github.com/Mininglamp-OSS/octo-web"
source_code_url: "https://github.com/Mininglamp-OSS/octo-web"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
first_released: "2026-05-11"
current_release: "2026-08-19"
stars: "808"
language: "TypeScript"
homepage: "https://github.com/Mininglamp-OSS"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "git clone, pnpm (source)"
docs_url: "https://github.com/Mininglamp-OSS/octo-web"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Mininglamp-OSS/octo-web"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Web and desktop (Electron) client for the OCTO open workplace platform — a messaging/collaboration tool built for humans x AI agents. One codebase ships browser + desktop products. First-class AI agent UX (streaming replies, typing indicators, inline tool-call previews, agent-vs-human identity chips). Local-first philosophy, bilingual English/Chinese."
---

octo-web is the client for the OCTO open workplace platform, a self-hostable messaging system where humans work alongside AI agents called Lobsters. The interface renders agent activity with first-class UX: tool-call previews, read receipts, and identity chips distinguishing agent from human participants. One React codebase produces both the web build and an Electron desktop shell, with bilingual English/Chinese localization enforced in CI. It pairs with a Go-based octo-server and ecosystem modules for tasks, summaries, and integrations, positioning itself as a complete self-hostable workplace rather than a standalone app. The project is an active Mininglamp OSS effort forked from TangSengDaoDaoWeb.
