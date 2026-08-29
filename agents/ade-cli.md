---
name: "ade-cli"
slug: "ade-cli"
layout: "agent.njk"
category: "other"
maker: "landing-ai"
license: "Apache-2.0"
url: "https://github.com/landing-ai/ade-cli"
source_code_url: "https://github.com/landing-ai/ade-cli"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-03-12"
current_release: "2026-08-19"
stars: "2404"
language: "Python"
homepage: "https://docs.landing.ai/ade/ade-overview"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "locked"
pricing: "usage"
install_method: "binary"
docs_url: "https://docs.landing.ai/cli/quickstart"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/landing-ai/ade-cli/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Agentic document extraction CLI (from LandingAI) that turns documents with tables/figures/charts into grounded Markdown and schema-shaped fields with page-and-box evidence; caches results locally to avoid duplicate credit usage."
---

Coding agents asked to read contracts, claims, or financial PDFs hallucinate structure unless the extraction tool returns grounded evidence, which is the gap LandingAI's Agentic Document Extraction CLI fills. Its parse command converts documents into Markdown with per-element bounding boxes, and extract fills schema-shaped fields with page-and-box evidence linking every value to its source region. Every command supports --json and ade help --json exposes the full command surface so agents can discover the interface programmatically, guided by a bundled SKILL.md contract. Results cache in ~/.ade so repeated identical commands consume no credits — important because the underlying API is metered. Data engineers and agent builders processing documents at scale are the users.
