---
name: "bumpgen"
slug: "bumpgen"
layout: "agent.njk"
category: "agent"
maker: "xeol-io"
license: "MIT"
url: "https://github.com/xeol-io/bumpgen"
source_code_url: "https://github.com/xeol-io/bumpgen"
source_available: "True"
platforms: []
first_released: "2024-04-09"
current_release: "2024-08-05"
stars: "146"
language: "TypeScript"
homepage: "https://www.xeol.io/beta"
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI"
pricing: "Free / open-source (MIT)"
install_method: "npm install -g bumpgen; also available as a GitHub Action (xeol-io/bumpgen@v0.0.1)"
docs_url: "https://github.com/xeol-io/bumpgen#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/xeol-io/bumpgen"
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "AI agent that bumps npm dependencies and automatically fixes breaking code changes using AST analysis (ts-morph) and a plan graph DAG (based on Microsoft's codeplan paper) to propagate fixes across the codebase. Roadmap includes Java, Go, C#, Python support."
---

bumpgen exists because dependency upgrades break code in ways that simple 'bump and pray' tools ignore: the version change succeeds but the build fails, and someone must trace every downstream use of the changed API. The agent builds the project to detect what breaks, uses ts-morph to analyze the AST and pull type definitions for the new package version, and consults an LLM for fixes; its distinctive piece is a plan-graph DAG adapted from Microsoft's CodePlan research, which lets it chain fixes so that a repair's own second-order breakage also gets addressed. Scope is deliberately narrow — npm/TypeScript only, build-error breakage only — and the tool ships both as a CLI and a GitHub Action intended to run on Dependabot or Renovate pull requests, committing fixes to the PR branch. xeol-io, the supply-chain security company behind it, used it to demonstrate AI-assisted upgrades; the repository has not seen commits since 2024 and the roadmap items (more languages, test oracles, GitHub App) were never completed.
