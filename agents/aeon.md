---
name: "Aeon"
slug: "aeon"
layout: "agent.njk"
category: "agent"
maker: "aeonfun"
license: "MIT"
url: "https://github.com/aeonfun/aeon"
source_code_url: "https://github.com/aeonfun/aeon"
source_available: "yes"
platforms:
  - "Autonomous"
first_released: "2026-03-04"
current_release: "2026-08-19"
stars: "675"
language: "JavaScript"
homepage: "https://www.aeon.fun/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "yes"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Grok, Codex, Pi, Vibe, Kimi"
pricing: "open-source"
install_method: "source"
docs_url: "https://www.aeon.fun/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aeonfun/aeon"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Autonomous AI agent framework that runs unattended on GitHub Actions — ships features, deploys apps, finds/discloses vulnerabilities, runs research, and writes new skills for itself. Runs on a schedule (cron), remembers across runs, reacts to conditions, and self-heals its own broken skills with no approval loops. A single skill is just a Markdown file (frontmatter + prompt). Fleet model: spawn-instance forks into specialized instances with isolated billing. MCP server exposes every skill as an AeON MCP tool in Claude. Installable as a Claude Code plugin. 6 harnesses configurable per-skill in aeon.yml."
---

Aeon is built for work nobody schedules: vulnerability disclosure rounds, dependency maintenance, research digests, and feature drops that happen on cron instead of when a developer remembers. An installation is a forked repository plus GitHub Actions — Node.js 20+ and the gh CLI are the only prerequisites — with configuration in aeon.yml defining schedules, skill inputs, models, and notification channels. Skills are individual SKILL.md markdown files organized into packs, and the runtime remembers across runs, reacts to conditions, and repairs skills that break, all without approval loops. An MCP server and Claude Code/Codex plugin support let existing agents invoke Aeon skills. Solo maintainers and small teams running unattended repositories are its users.
