---
name: "10xProductivity"
slug: "10xproductivity"
layout: "agent.njk"
category: "other"
maker: "ZhixiangLuo"
license: "MIT"
url: "https://github.com/ZhixiangLuo/10xProductivity"
source_code_url: "https://github.com/ZhixiangLuo/10xProductivity"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-03-17"
current_release: "2026-07-13"
stars: "467"
language: "Python"
homepage: "https://github.com/ZhixiangLuo/10xProductivity"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "agent-agnostic (Cursor, Claude Code, Codex, Copilot via --engine flag)"
pricing: "open-source"
install_method: "git clone; create python venv (python3 -m venv .venv); pip install -e .[dev]; instruct coding agent to read setup.md"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ZhixiangLuo/10xProductivity"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Local-first personal AI assistant that turns existing coding agents (Cursor, Claude Code, Codex, Copilot) into a work assistant operating within corporate constraints — no new infrastructure, no IT approval, no Slack apps or webhooks. Uses your existing authenticated sessions and permissions. Features a coaching loop where human-AI interaction creates reusable skills, triggers, and workflows over time. Ships 25+ pre-built tool-connection recipes."
---

Inside most companies, employees cannot install Slack apps, webhooks, or automation platforms without IT approval, yet their coding agent already has authenticated browser sessions and broad tool access. 10xProductivity exploits that: a local-first Python framework invokes the agent you already use (Cursor, Claude Code, Codex, Copilot) through an --engine flag and drives it with recipes, triggers, and workflows for enterprise search, stand-up prep, or Slack polling. A hooks directory keeps credentials and browser state out of the repo tree, and new workflows are built in supervised coaching sessions before being trusted to run autonomously. It targets employees who want personal automation without IT involvement.
