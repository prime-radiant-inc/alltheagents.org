---
name: "ZeroPath"
slug: "zeropath"
layout: "agent.njk"
category: "agent"
maker: "ZeroPath"
license: null
url: "https://zeropath.com"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: "no"
plugin_support: null
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "subscription"
install_method: "SaaS - connect GitHub, GitLab, Bitbucket, or Azure DevOps; zero-config repository scanning with no build scripts; cloud, hybrid, or on-prem deployment"
docs_url: "https://zeropath.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI-native scanning + verified security patches; RSAC 2026 Innovation Sandbox"
---

ZeroPath targets the failure mode of traditional SAST: a finding is reported, but producing an actual fix remains a human project. The platform scans repository fleets without requiring build configuration, using AI-driven analysis to catch business-logic flaws and auth bypasses that rule-based scanners miss. Its distinguishing step is agentic patching — for confirmed vulnerabilities an agent drafts a change that must compile, pass tests, and merge cleanly before it is proposed, turning scanner output into mergeable pull requests. Around that core sit complementary scanners: dependency analysis weighted by reachability, secrets detection across 40+ file types with validation, infrastructure-as-code scanning for Terraform and Kubernetes, container scanning, DAST with exploit proof, and continuous security review of pull requests. A versioned policy engine lets teams codify security requirements as testable rules, findings sync to Jira, Linear, or ServiceNow, and an AI inventory discovers models, agents, and MCP servers in customer codebases for AI-BOM compliance. A separate assistant agent, Zero, runs AppSec program tasks such as bug-bounty triage. Sold demo-first with cloud, hybrid, or on-prem deployment, it targets security engineering teams; the company was an RSAC 2026 Innovation Sandbox finalist and reports 300,000+ monthly scans.
