---
name: "vs-code-agents"
slug: "vs-code-agents"
layout: "agent.njk"
category: "agent"
maker: "groupzer0"
license: "MIT"
url: "https://github.com/groupzer0/vs-code-agents"
source_code_url: "https://github.com/groupzer0/vs-code-agents"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-12-13"
current_release: "2026-01-18"
stars: "284"
language: "Markdown, Python"
homepage: null
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "GitHub Copilot (via VS Code)"
pricing: "open-source"
install_method: "git clone https://github.com/groupzer0/agents.git; copy .agent.md files into .github/agents/ or user-level VS Code profile; install Flowbaby extension from VS Code Marketplace"
docs_url: "https://github.com/groupzer0/vs-code-agents/blob/main/USING-AGENTS.md"
plugin_docs_url: "https://marketplace.visualstudio.com/items?itemName=flowbaby.flowbaby"
config_docs_url: "https://code.visualstudio.com/docs/copilot/copilot-agents"
download_url: "https://github.com/groupzer0/agents.git"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent workflow system for GitHub Copilot in VS Code bringing structure, quality gates, and long-term memory to AI-assisted development. Specialized agents (Planner, Implementer, Security, QA, etc.) each own a specific part of the dev workflow with clear constraints and document-driven output; designed for persistent, workspace-scoped memory via Flowbaby."
---

vs-code-agents exists because unstructured Copilot sessions forget context, skip quality gates, and lose decision history. It defines 13 custom agents (planner, analyst, architect, security, critic, implementer, code-reviewer, QA, UAT, devops, roadmap, retrospective, process-improvement) as Markdown files installed into a project's .github/agents/ directory, each with hard constraints: the Planner cannot write code and the Implementer cannot redesign. Agents hand off through structured Markdown documents stored in an agent-output/ audit trail, and the Security agent follows a five-phase framework covering STRIDE threat modeling, OWASP Top 10, CVE scanning, and ASVS compliance. Cross-session memory requires the companion Flowbaby VS Code extension backed by Python 3.10+. It targets teams standardizing Copilot-assisted development with review gates.
