---
name: "Stakpak"
slug: "stakpak"
layout: "agent.njk"
category: "agent"
maker: "Stakpak"
license: "Apache-2.0"
url: "https://stakpak.dev"
source_code_url: null
source_available: "yes"
platforms: []
first_released: null
current_release: null
stars: null
language: "Rust"
homepage: "https://stakpak.dev"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "curl -sSL https://stakpak.dev/install.sh | sh"
docs_url: "https://stakpak.gitbook.io/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "acquired"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI DevOps agent for infrastructure code"
---

Stakpak runs as a single Rust binary installed as a system service on the machines it manages, addressing the gap between hosted PaaS convenience and the lock-in that comes with it. In autopilot mode it performs health checks, renews expiring certificates and secrets, flags deprecated APIs, and hunts idle RDS and EBS resources for cost savings, surfacing only the decisions that need a human. All agent network traffic passes through a Cedar-policy proxy, secrets are substituted with placeholders before reaching the model, and full session audit logs support rollback. A single TUI handles interactive work alongside the background service. The site announced the company is joining Vercel, so teams evaluating it should account for the transition.
