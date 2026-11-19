---
name: "OpenFlow"
slug: "openflow"
layout: "agent.njk"
category: "multiplexer"
maker: "SeeRay11"
license: "MIT"
url: "https://github.com/SeeRay11/OpenFlow"
source_code_url: "https://github.com/SeeRay11/OpenFlow"
source_available: "True"
homepage: null
docs_url: "https://github.com/SeeRay11/OpenFlow/blob/dev/packages/flow/README.md"
download_url: null
install_method: "git clone https://github.com/SeeRay11/OpenFlow.git && cd OpenFlow && bun install (needs Bun 1.3+ and Git), then run with bun openflow.ts or the openflow.sh/openflow.ps1 shims; engine on port 4096, canvas on 5174"
platforms:
  - "Desktop"
  - "Web"
autonomy_level:
  - "agentic"
specialization: "general"
language: "TypeScript"
first_released: "2026-08-18"
current_release: "2026-10-18"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "any provider opencode supports via models.dev (keys connected per provider in the app); opencode zen free-tier models run with no key"
pricing: "free"
stars: "182"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A visual canvas where you drag role cards (planner, architect, coder), wire them into a DAG, and run them as real parallel opencode sessions — with three schedulers (pipeline, swarm, orchestration), a gauntlet mode that loops builders against fresh-context critics until a written bar is cleared, and a deterministic coach that audits how far to trust each run's report."
---

OpenFlow is an independent fork of opencode by a solo developer: it keeps upstream's headless engine (`opencode serve`) unmodified and adds its own package, a browser canvas served on localhost. You drag role cards onto that canvas and wire a pipeline — planner → architect → coder — and the scheduler turns each card into a real opencode session, dispatching each topological layer through a concurrency pool with a briefing that tells every card what the graph around it looks like and who reads its output. Three schedulers cover different shapes of work: a pipeline runs the DAG in dependency order, a swarm prompts peers over rounds until a synthesizer decides, and an orchestration lets a card hand work to its children (subagents deploying subagents, bounded by graph depth and dispatch counts). A gauntlet toggle on orchestration loops builders against critics that get a fresh session per verdict until the work clears a bar you wrote, with money, wall-clock, and stall bounds. The engine is opencode itself, so models come from whatever provider key you connect — opencode zen's free-tier models run with no credential — and per-node tool allowlists, including project MCP servers, take effect through generated opencode agent definitions merged into the project config. It suits developers who want multi-agent workflows they can see, price, and re-run card by card rather than prompt-engineer in a terminal.
