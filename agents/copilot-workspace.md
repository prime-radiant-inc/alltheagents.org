---
name: "Copilot Workspace"
slug: "copilot-workspace"
layout: "agent.njk"
category: "agent"
maker: null
license: null
url: "https://githubnext.com/projects/copilot-workspace"
source_code_url: null
source_available: "False"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "True"
model_providers: "GitHub Copilot (OpenAI-based)"
pricing: "Free during technical preview"
install_method: "Web-based; accessed through browser at githubnext.com (sign-up required for preview access)"
docs_url: "https://githubnext.com/projects/copilot-workspace"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Task-centric AI flow from GitHub issue to plan to code to PR; understands repo context and lets developers iterate on AI-proposed plans before implementation. Technical preview / research project from GitHub Next."
---

Moving from a GitHub issue to a pull request involved spec-writing, planning, and implementation steps that plain Copilot completions did not cover, and GitHub Next built Copilot Workspace to fill that gap. A task - an issue, a discussion, or a blank idea - produced a natural-language spec of current behavior and proposed design, then a file-by-file implementation plan, then code changes in an ephemeral environment, with every stage editable before a branch and pull request emerged. The experience was deliberately human-in-the-loop: the developer revised each artifact rather than watching an autonomous run. GitHub sunset the technical preview in 2025, folding its spec-and-plan mechanics into the Copilot coding agent and agent mode in VS Code. It is remembered as the design bridge between chat-based Copilot and GitHub's current agentic offerings.
