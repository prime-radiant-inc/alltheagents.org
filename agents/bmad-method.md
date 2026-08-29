---
name: "BMAD-METHOD"
slug: "bmad-method"
layout: "agent.njk"
category: "agent"
maker: "bmad-code-org"
license: "MIT"
url: "https://github.com/bmad-code-org/BMAD-METHOD"
source_code_url: "https://github.com/bmad-code-org/BMAD-METHOD"
source_available: "Yes"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2025-04-13"
current_release: "2026-08-19"
stars: "52089"
language: "JavaScript"
homepage: "https://docs.bmad-method.org"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes (.claude-plugin directory)"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "Provider-agnostic (works with your AI coding tool; Gemini, ChatGPT bundles)"
pricing: "open-source"
install_method: "npm (npx bmad-method install)"
docs_url: "https://docs.bmad-method.org/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/bmad-code-org/BMAD-METHOD"
maintained: "active"
sources:
  - "namphuong"
what_makes_it_special: "An agile methodology framework for AI-driven development covering the entire delivery lifecycle -- from clarifying vague ideas to planning, building, verifying, and learning -- preserving durable context across sessions with specialized agent perspectives."
---

BMAD-METHOD addresses the failure mode where AI coding tools lose context between chats, forget decisions, and produce code that drifts from requirements. It installs a structured set of agent personas — product, architecture, UX, development, testing — into whatever AI tool a team already uses, with workflows that scale process to the change: trivial fixes go straight to build, larger efforts pass through explicit planning phases with durable artifacts that carry decisions forward across sessions. Installed into a project, it adds agent definitions and commands (bmad-build, bmad-help) that the host tool invokes; modules extend the base with dedicated test-architect, loop-based unattended builds, and game-dev studios. Its audience spans solo developers through teams running greenfield or legacy work, and its 50k+ stars make it one of the most widely adopted agent frameworks. Development is active, on a V6 line, with docs at docs.bmad-method.org and a no-paywall community.
