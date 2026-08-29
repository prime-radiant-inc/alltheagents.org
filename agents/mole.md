---
name: "Mole"
slug: "mole"
layout: "agent.njk"
category: "other"
maker: "lajosdeme"
license: "Apache-2.0"
url: "https://github.com/lajosdeme/mole"
source_code_url: "https://github.com/lajosdeme/mole"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-08-01"
current_release: "2026-08-13"
stars: 293
language: "Go"
homepage: null
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "configurable"
pricing: "free"
install_method: "Static binaries (mole + mole-mcp) from the repo releases"
docs_url: "https://github.com/lajosdeme/mole/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/lajosdeme/mole/releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A deep-research agent with an enforced budget: every model call is reserved and settled against a ledger so --usd 0.50 hard-stops the run at fifty cents, and every claim must carry a verbatim quote from its source or be discarded. Ships with a toolkit mode where a coding agent's model does the reasoning and mole supplies deterministic quote verification, SQL rendering, and search over MCP."
---

Mole is a Go deep-research agent, not a coding agent: it takes a research question, decomposes it into sub-questions, searches the web and academic sources (Crossref, OpenAlex, arXiv, PubMed), reads sources, extracts claims, and writes a cited answer. Its two signature constraints are an enforced budget — every model call is reserved and settled against a ledger so a --usd 0.50 flag hard-stops the run at fifty cents with measured zero overshoot — and verified quotes, where every claim must carry a verbatim quote from its source and unverified claims are discarded or flagged. A privacy boundary lets it analyze local CSV/JSON data with only aggregates leaving the machine, and mole crossings shows exactly what crossed. It ships as two static binaries, mole and mole-mcp, the latter exposing it over MCP so a coding agent like Claude Code can drive it — either with mole owning the model, or in toolkit mode where the agent's model reasons while mole supplies the deterministic parts. It is included here as tooling that complements coding agents rather than a harness.
