---
name: "Bullet"
slug: "bullet"
layout: "agent.njk"
category: "agent"
maker: "trybullet"
license: "Proprietary"
url: "https://www.codewithbullet.com"
source_code_url: null
source_available: "False"
platforms:
  - "CLI"
  - "Desktop"
first_released: "2026-08-07"
current_release: "2026-08-28"
stars: null
language: null
homepage: "https://www.codewithbullet.com"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: "no"
model_providers: "multi-model routing (fast models for simple work, deeper reasoning on escalation)"
pricing: "free"
install_method: "npm install -g @trybullet/cli (Node 18+), or download the desktop app"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/trybullet/bullet-releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Speed-first routing architecture that sends straightforward work to fast models and escalates to deeper reasoning only for complex tasks, finds relevant code without embedding the whole repo, and runs independent tool calls in parallel while intercepting duplicate calls and stuck loops. Claims 95.8% on SWE-Bench Verified."
---

Bullet is a YC-backed coding agent built by a team that got frustrated waiting on agent runs while building with Claude Code, and its whole pitch is keeping up with the developer rather than the other way around. Three protocols drive the speed: routing tasks to the right model tier, targeted search that finds relevant code without ingesting the entire repository, and parallel execution of independent tool calls with interception of duplicate calls and stuck loops. The same agent loop and tools are available both as a desktop GUI app and as a CLI installed via npm, and the team reports 95.8% on SWE-Bench Verified. Access is currently free with no subscription or API key required to start, and it runs on macOS, Linux, and Windows.
