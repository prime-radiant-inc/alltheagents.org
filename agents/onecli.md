---
name: "OneCLI"
slug: "onecli"
layout: "agent.njk"
category: "agent"
maker: "onecli"
license: "Apache-2.0 (with enterprise features under the OneCLI Enterprise License)"
url: "https://github.com/onecli/onecli"
source_code_url: "https://github.com/onecli/onecli"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
first_released: "2026-03-08"
current_release: "2026-08-29"
stars: 3423
language: "TypeScript"
homepage: "https://onecli.sh"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: "no"
model_providers: "configurable (gateway-mediated)"
pricing: "freemium"
install_method: "Self-host via Node/pnpm monorepo with Docker and PostgreSQL, or use the cloud at onecli.sh (free tier: $5 AI credits, 500 calls/month)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Sandboxed per-employee agent platform where credentials never reach the model: a Rust gateway performs MITM HTTPS to inject scoped secrets per request, backed by an AES-256-GCM secret store or on-demand Bitwarden/1Password, with policy enforced at the network level and deterministic human-in-the-loop approvals for sensitive actions. The runner is outbound-only, working on laptops, homelabs, or NAT'd VPCs."
---

OneCLI is an open-source, YC-backed agent platform that gives every employee a personal AI agent in a sealed sandbox, originally built as a Rust credential vault for AI agents and repivoted to team-based agent management after demand from users running autonomous agents like Hermes and OpenClaw. Agents chat via a dashboard or per-agent Slack apps and work on real tasks — triaging tickets, reconciling Stripe charges, opening PRs, revoking access — while all outbound traffic is routed through the gateway, which injects credentials on the fly so the model never sees real secrets, blocks forbidden actions, rate-limits runaway agents, and pauses sensitive actions for approval cards. The stack is a Next.js dashboard, API control plane, Rust gateway, sandbox supervisor with a vendor-neutral harness interface, and an outbound-only runner that needs no inbound ports; it is self-hostable or available as a cloud product. Free tier includes $5 in AI credits and 500 calls per month, with paid tiers beyond.
