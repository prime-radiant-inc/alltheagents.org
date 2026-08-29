---
name: "coding-agents-workshop"
slug: "coding-agents-workshop"
layout: "agent.njk"
category: "other"
maker: "sshh12"
license: "MIT"
url: "https://github.com/sshh12/coding-agents-workshop"
source_code_url: "https://github.com/sshh12/coding-agents-workshop"
source_available: "True"
platforms: []
first_released: "2026-02-21"
current_release: "2026-03-03"
stars: "29"
language: "Python"
homepage: "https://html-preview.github.io/?url=https://github.com/sshh12/coding-agents-workshop/blob/main/slides.html"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "None (attendees bring their own: Claude Code, Gemini CLI, Codex CLI, or Cursor)"
pricing: "Free/open source"
install_method: "git clone https://github.com/sshh12/coding-agents-workshop.git then pip install -r requirements.txt"
docs_url: "https://html-preview.github.io/?url=https%3A%2F%2Fgithub.com%2Fsshh12%2Fcoding-agents-workshop%2Fblob%2Fmain%2Fslides.html"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sshh12/coding-agents-workshop"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Workshop materials for 'Optimizing Codebases for Agents' — a tangible before/after comparison of the same application (Version A = realistic mess with deliberate anti-patterns vs. Version B = agent-optimized), paired with an AI-readiness scorecard runnable against any repo via Claude Code, and a live agent race demo where two terminals run the same prompt against different codebases to visually demonstrate the impact of codebase optimization on AI agent performance."
---

When coding agents produce poor results, teams usually blame the model or the prompt; this workshop argues the codebase is often the real constraint. Built for the 'Optimizing Codebases for Agents' session at the Coding Agents conference (March 2026, Computer History Museum) by Shrivu Shankar of Abnormal Security, the repository contains two complete implementations of the same ML experiment tracker - one deliberately full of anti-patterns, one restructured for agent navigation - plus a scoring rubric that audits any repository from 0 to 9 across three readiness dimensions. A ready-made Claude Code prompt runs the audit against any repo, and a scripted race demo shows the same prompt on both codebases side by side. Conference attendees and team leads use the materials to assess and restructure their own repositories for agent work.
