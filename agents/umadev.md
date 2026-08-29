---
name: "umadev"
slug: "umadev"
layout: "agent.njk"
category: "agent"
maker: "umacloud"
license: "MIT"
url: "https://github.com/umacloud/umadev"
source_code_url: "https://github.com/umacloud/umadev"
source_available: "True"
platforms: []
first_released: "2026-06-19"
current_release: "2026-08-07"
stars: "250"
language: "Rust"
homepage: "https://umadev.goder.ai"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code, Codex, OpenCode, Grok Build, Kimi Code (drives 5 base CLIs which bring their own models)"
pricing: "Free / open-source (MIT)"
install_method: "npm install -g umadev; or native installer (curl -fsSL https://umadev.goder.ai/install.sh | bash / irm https://umadev.goder.ai/install.ps1 | iex); or build from source with Cargo"
docs_url: "https://umadev.goder.ai"
plugin_docs_url: null
config_docs_url: "https://github.com/umacloud/umadev/blob/main/CONFIG.md"
download_url: "https://umadev.goder.ai/install.sh"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Orchestrates a 9-seat dev team (8 specialist roles + coordinator) over borrowed AI brains — driving one of 5 existing AI coding CLIs rather than owning any model endpoint. Deterministic acceptance floor (build/test/contract verification runs regardless of model self-assessment). 113 governance checks with fail-open design. Delivery evidence with proof packs, scorecards, compliance mappings (SOC 2 / ISO 27001 / EU AI Act). Spec-driven with 34 normative clauses. Local-first retrieval with BM25 + optional local vector embeddings. Frontend↔backend contract verification."
---

UmaDev exists because a raw coding CLI has no delivery discipline: it declares completion without evidence, and teams adopting it for real work need governance, plans, and proof. The tool drives one of five installed coding CLIs as its brain — the CLI keeps its own login and model config — while umadev supplies the process: clarify, research, PRD/architecture/UI-UX documents, staged gates, and delivery artifacts including a proof pack and compliance mapping. Roles coordinate through shared blackboard artifact files rather than chat; reviewer roles run as fresh read-only child sessions whose verdicts feed a coordinator; and quality gates run builds, tests, and OpenAPI contract checks regardless of what the model claims. Trust tiers (plan/guarded/auto) set autonomy per task, irreversible actions always confirm, and hooks wire governance into Claude Code and git pre-commit; an MCP server exposes the governor to other clients. Teams needing auditable, compliance-mapped AI development use it; it is a single MIT-licensed Rust binary distributed via npm or native installer.
