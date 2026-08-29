---
name: "open-agent-hub"
slug: "open-agent-hub"
layout: "agent.njk"
category: "other"
maker: "guanyang"
license: "MIT"
url: "https://github.com/guanyang/open-agent-hub"
source_code_url: "https://github.com/guanyang/open-agent-hub"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-01-13"
current_release: "2026-08-19"
stars: "952"
language: "JavaScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes — agents directory with Orchestrator, Evaluator, and Optimizer roles with handoff contracts"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "npm"
docs_url: "https://github.com/guanyang/open-agent-hub#readme"
plugin_docs_url: "https://github.com/guanyang/open-agent-hub/blob/main/docs/Skill_Guidelines.md"
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Zero-dependency, single-command activation of Skills/Agents/Commands across 8+ AI coding assistants (Claude Code, Cursor, Trae, Gemini CLI, Codex, Antigravity, OpenCode, Kiro) with 83+ modular skills and upstream community sync."
---

open-agent-hub addresses the fragmentation of agent configuration formats across coding assistants by maintaining one library of skills, agent role definitions, and slash commands that activate into any supported tool. The oah CLI symlinks rather than copies, so a single source of truth updates everywhere, and an upstream sync command pulls community skill updates. Agent definitions go beyond static prompts: the hub ships Orchestrator, Evaluator, and Optimizer roles with explicit handoff contracts, encoding an evaluator-optimizer loop. Installation ranges from Vercel's skills CLI for skill-only use to the full oah CLI from a cloned repository. Bilingual documentation serves both English and Chinese-speaking users.
