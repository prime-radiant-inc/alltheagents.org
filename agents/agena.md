---
name: "Agena"
slug: "agena"
layout: "agent.njk"
category: "agent"
maker: "aozyildirim"
license: "MIT"
url: "https://github.com/aozyildirim/Agena"
source_code_url: "https://github.com/aozyildirim/Agena"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-03-21"
current_release: "2026-08-02"
stars: "97"
language: "Python, TypeScript"
homepage: "https://agena.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Google Gemini, Claude CLI, Codex CLI, Custom"
pricing: "Free (5 tasks/month), Pro (unlimited tasks, all features, priority queue), Enterprise (unlimited, custom models, SSO, dedicated support). Stripe billing integrated."
install_method: "brew install aozyildirim/tap/agena | npm install -g @agenaai/cli | git clone + ./start.sh (Docker Compose)"
docs_url: "https://agena.dev/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aozyildirim/Agena"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Runs on existing Claude Code/Codex CLI subscriptions locally via host bridge (no API keys or per-token billing); full autonomous loop from production error to task to AI fix to PR to merge to issue resolved; Team Skill Catalog with Qdrant vector retrieval that re-applies past solutions; pixel-art 'Boss Mode' office UI for managing AI agents visually; self-hostable multi-tenant SaaS with RBAC; history-grounded sprint refinement; integrates with Sentry, New Relic, Jira, YouTrack, Azure DevOps, GitHub; drag-and-drop visual flow builder with approval gates."
---

Agena automates the path from production incident to merged fix: errors arriving from Sentry, New Relic, Jira, YouTrack, or Azure DevOps become tasks that a CrewAI/LangGraph pipeline of PM, Planner, Developer, Reviewer, and Finalizer agents turns into reviewed pull requests. Its economic hook is the host bridge — agents run on the team's existing Claude Code or Codex CLI subscriptions locally, so there are no API keys or per-token charges, with OpenAI and Gemini available as alternatives. A Team Skill Catalog in Qdrant retrieves how similar problems were solved before, and integrations cover Jira, YouTrack, and GitHub. It ships as brew/npm CLIs or a self-hosted Docker Compose stack with RBAC and Stripe billing, and a visual flow builder adds approval gates. Teams with steady production-error volume are the intended operators.
