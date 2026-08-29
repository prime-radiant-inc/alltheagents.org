---
name: "GitLab Duo"
slug: "gitlab-duo"
layout: "agent.njk"
category: "agent"
maker: null
license: "Open core (proprietary with open-core contributions)"
url: "https://about.gitlab.com/gitlab-duo/"
source_code_url: null
source_available: "Partial (open core model)"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: "yes (integrates external agents like Claude Code and Codex; connects internal systems, third-party tools, external AI services)"
claude_code_plugin: null
subagents: "yes (chaining multiple agents in agentic flows)"
hooks: null
plan_mode: null
model_providers: "Anthropic (Claude Sonnet 4, Claude 3 Haiku), OpenAI (GPT-5 mini), Google Vertex AI Codey, self-hosted models"
pricing: "Usage-based via GitLab Credits (pooled across org); rates vary by model; included in Premium & Ultimate plans (GitLab 18.8+)"
install_method: "Available on GitLab Premium & Ultimate (v18.8+); free trial available"
docs_url: "https://docs.gitlab.com/user/duo_agent_platform/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "GitLab Orbit lifecycle context graph connecting code, merge requests, pipelines, and deployments for agent grounding; AI Catalog for agent/flow management; policy-driven AI control; event-driven agentic flows with full CI/CD traceability."
---

GitLab Duo Agent Platform embeds agentic automation directly in the DevSecOps platform: expert-built agents for planning, code generation, code review, and security analysis are dispatched by events, chained into multi-step flows (fix a pipeline, convert a pipeline to GitLab CI, turn an issue into an MR), and grounded by the Orbit context graph that links code, MRs, pipelines, and deployments. The AI Catalog manages agent and flow definitions, policies control what agents may do, and GitLab Credits bill usage across models including Claude, GPT, and self-hosted models. It ships with GitLab 18.8+ on Premium and Ultimate and integrates external agents such as Claude Code and Codex. The audience is enterprises that want agent automation under one governance and audit perimeter.
