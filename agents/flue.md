---
name: "Flue"
slug: "flue"
layout: "agent.njk"
category: "agent-sdk"
maker: "withastro"
license: "Apache-2.0"
url: "https://github.com/withastro/flue"
source_code_url: "https://github.com/withastro/flue"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-07"
current_release: "2026-08-08"
stars: "7961"
language: "TypeScript"
homepage: null
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Model-agnostic via provider/model string slugs (e.g. anthropic/claude-sonnet-4-6)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://flueframework.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "author_search"
what_makes_it_special: "Programmable TypeScript harness framework for building autonomous agents where the agent IS a function composed of hooks (useModel, useSandbox, useSkill, useTool). Not an SDK -- a programmable harness that gives any model the context and environment needed for autonomous work: durable sessions, secure sandboxes, skills, tools, MCP integration, observability, and multi-channel event ingestion. Deploys to Node.js, Cloudflare Workers, GitHub Actions, GitLab CI/CD, Render, or Daytona. Extensibility via Skills, Tools, and Channels."
---

Flue's premise is that an agent should be defined in typed source code the way UIs are defined in React: a function annotated with 'agent' that declares its harness through hooks (useModel for the provider/model slug, useSandbox for execution isolation, useSkill and useTool for capabilities) and returns its instructions. The runtime supplies sessions, tools, filesystem access, durability with recovery, subagents, MCP support, and observability through OpenTelemetry, Braintrust, or Sentry, while deployment targets span Node.js, Cloudflare Workers, GitHub Actions, GitLab CI, and Render. Channels connect agents to Slack, Teams, Discord, and GitHub. Built within the Astro organization, it targets TypeScript teams who want agent behavior reviewable in code review rather than configured in YAML.
