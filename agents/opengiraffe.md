---
name: "OpenGiraffe"
slug: "opengiraffe"
layout: "agent.njk"
category: "multiplexer"
maker: "zclllyybb"
license: null
url: "https://github.com/zclllyybb/OpenGiraffe"
source_code_url: "https://github.com/zclllyybb/OpenGiraffe"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2026-03-03"
current_release: "2026-05-08"
stars: "104"
language: "Python"
homepage: "https://github.com/zclllyybb/OpenGiraffe"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "opencode CLI (any LLM backend)"
pricing: "Free / open source, self-hosted"
install_method: "git clone + pip install -r requirements.txt + configure config.yaml + python cli.py start"
docs_url: "https://github.com/zclllyybb/OpenGiraffe/tree/main/docs"
plugin_docs_url: null
config_docs_url: "https://github.com/zclllyybb/OpenGiraffe/blob/main/config.yaml.template"
download_url: "https://github.com/zclllyybb/OpenGiraffe"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Autonomous batch task queue (not interactive copilot); continuous codebase Explorer that proactively finds work; Plan->Code->Review loop with multi-reviewer voting (all must approve) and automatic retry on rejection; persistent SQLite state for resume-after-reboot; each task isolated in its own git worktree/branch; web dashboard for runtime model editing and task management"
---

Interactive copilots wait for a prompt, so the backlog of small fixes and TODOs scattered through a codebase never gets touched. OpenGiraffe runs as a persistent daemon that flips the model: a continuous Explorer scans the repository for work (including TODO/FIXME mining and optional Jira-issue skills), feeds it through a Planner-Coder-Reviewer pipeline, and executes tasks in parallel across isolated git worktrees with retry logic. Nothing lands without review — the pipeline requires reviewer approval, and a local web dashboard on port 8778 visualizes the queue and active work. It drives the opencode CLI rather than talking to model APIs directly, so model choice and keys come from the opencode configuration. Setup is clone, pip install, configure YAML, and start, under Python 3.11+. Maintainers who want a codebase to accumulate autonomous progress between human sessions are the audience.
