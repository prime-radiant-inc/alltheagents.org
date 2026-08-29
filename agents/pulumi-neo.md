---
name: "Pulumi Neo"
slug: "pulumi-neo"
layout: "agent.njk"
category: "agent"
maker: "Pulumi"
license: null
url: "https://www.pulumi.com"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "Pulumi-hosted agent (models not disclosed); integrates with external coding agents via Pulumi's open-source MCP skills for Claude Code, Cursor, etc."
pricing: "freemium"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.pulumi.com/product/neo/"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI agent that writes/updates infrastructure-as-code"
---

Pulumi Neo applies the agentic coding pattern to infrastructure engineering, where a bad change can take a production system down rather than just failing a test. Neo takes a natural-language infrastructure request, generates code in Pulumi's general-purpose IaC languages (TypeScript, Python, Go, C#, YAML, HCL) across 170+ providers, runs tests and policy-as-code checks, and deploys with pulumi up — either autonomously or with human approval gates. Because it sits on Pulumi's platform, it inherits organizational context: existing stacks, policy enforcement, secrets management, and cloud discovery, which keeps agent-generated infrastructure from drifting from organizational rules. Pulumi also publishes open-source skills so coding agents developers already use can drive Pulumi workflows directly. Platform and DevOps teams use Neo for provisioning, drift remediation, and — through Neo Security — continuous threat modeling and attack-path tracing across their cloud estate.
