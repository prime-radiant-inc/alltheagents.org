---
name: "Moderne"
slug: "moderne"
layout: "agent.njk"
category: "agent"
maker: "Moderne"
license: null
url: "https://www.moderne.io"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Mass-scale automated refactoring (OpenRewrite core) + Moddy agent"
---

Moderne's substrate is the OpenRewrite Lossless Semantic Tree: each repository is sequenced into a compiler-accurate, type-attributed, format-preserving model, and deterministic recipes rewrite precisely the matched constructs without disturbing surrounding code — the mechanism behind a single Log4Shell recipe fixing 38,000 call-sites across 400 repositories with no regressions. The company's agent-era positioning splits the labor explicitly: an LLM plans, recipes execute, making Moderne 'the deterministic harness between the agent and your code.' Its first-party agent Moddy takes natural-language requests such as upgrading to Spring Boot 3.5, finds the appropriate recipes, and executes them across repository fleets; Prethink supplies pre-resolved context (endpoints, dependencies, test coverage) so external coding agents stop inferring architecture from raw source. Enterprises running from one to 100,000+ repositories deploy it as SaaS, a managed service, or air-gapped DX for vulnerability remediation and framework migrations; pricing is enterprise sales-driven rather than published.
