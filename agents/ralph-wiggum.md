---
name: "ralph-wiggum"
slug: "ralph-wiggum"
layout: "agent.njk"
category: "multiplexer"
maker: "fstandhartinger"
license: "MIT"
url: "https://github.com/fstandhartinger/ralph-wiggum"
source_code_url: "https://github.com/fstandhartinger/ralph-wiggum"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-01-14"
current_release: "2026-05-11"
stars: "286"
language: "Bash, PowerShell"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Claude Code, OpenAI Codex, Google Gemini, GitHub Copilot"
pricing: null
install_method: "npx add-skill fstandhartinger/ralph-wiggum; or openskills install fstandhartinger/ralph-wiggum"
docs_url: "https://ralph-wiggum-web.onrender.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/fstandhartinger/ralph-wiggum"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Enables autonomous AI coding using spec-driven development by combining an iterative bash/PowerShell loop with SpecKit-style specifications. The AI agent picks a task, implements it, verifies it, and commits it, only outputting <promise>DONE</promise> when acceptance criteria are met. It operates with fresh context each loop and shares state via disk files."
---

Ralph Wiggum packages the Ralph autonomous-loop pattern — repeatedly restarting a coding agent with clean context — on top of structured specifications rather than ad-hoc prompts. Markdown specs in a specs/ directory carry testable acceptance criteria; each loop iteration has the agent orient, pick one task, implement and test it, commit, and emit a completion phrase the outer script checks for before deciding to continue. Attempt counters flag specs that fail ten times, full logs and optional Telegram notifications keep long runs observable, and an AI-driven installer interviews you to generate a project constitution governing agent behavior. Per-agent loop scripts cover Claude Code, Codex, Gemini, Copilot, and Cursor in both bash and PowerShell, and the whole thing installs as an Agent Skill into any skills-compatible tool. Developers running long unattended builds use it to keep agents working through a spec list without context rot.
