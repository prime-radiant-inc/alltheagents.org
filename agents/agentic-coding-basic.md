---
name: "agentic-coding-basic"
slug: "agentic-coding-basic"
layout: "agent.njk"
category: "other"
maker: "thixpin"
license: "MIT"
url: "https://github.com/thixpin/agentic-coding-basic"
source_code_url: "https://github.com/thixpin/agentic-coding-basic"
source_available: "True"
platforms: []
first_released: "2026-07-06"
current_release: "2026-07-07"
stars: "59"
language: "Python (build script)"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic (via Claude Code; requires a Claude Pro/Max/Team/Enterprise plan or Console account)"
pricing: "Free book; requires Claude Code Pro/Max/Team/Enterprise Plan or Console Account"
install_method: "git clone && ./build.sh to generate EPUB/PDF in dist/"
docs_url: "https://github.com/thixpin/agentic-coding-basic#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/thixpin/agentic-coding-basic"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Burmese-language tutorial book teaching agentic coding to junior developers by building a mini ecommerce site (Myanmar-specific twist: orders via Viber screenshots, no backend)."
---

Junior developers in Myanmar face two compounding barriers to agentic coding: most material is English-only, and paid API access is out of reach, so this free MIT-licensed book by thixpin (Soe Thura) teaches the practice in Burmese using only a Claude subscription. The nine chapters build a small ecommerce site for a local shop — React, Vite, and Tailwind with no backend, orders relayed to the owner as Viber screenshots, a distinctly Myanmar workaround. Instruction covers the distinction between autocomplete and agents, CLAUDE.md and plan mode, writing reusable SKILL.md skills, regression testing, and seven context/token-economy techniques. A build script compiles the markdown into EPUB and PDF with embedded Noto Sans Myanmar fonts.
