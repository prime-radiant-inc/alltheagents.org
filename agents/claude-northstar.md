---
name: "claude-northstar"
slug: "claude-northstar"
layout: "agent.njk"
category: "agent"
maker: "Nisarg38"
license: "MIT"
url: "https://github.com/Nisarg38/claude-northstar"
source_code_url: "https://github.com/Nisarg38/claude-northstar"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-01-06"
current_release: "2026-01-06"
stars: "1"
language: "JavaScript, Node.js"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Claude Code, OpenCode"
pricing: "Free / open-source (MIT)"
install_method: "npx claude-northstar init (recommended), or curl -fsSL https://raw.githubusercontent.com/nisarg38/claude-northstar/main/install.sh | bash"
docs_url: "https://github.com/Nisarg38/claude-northstar"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Nisarg38/claude-northstar"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Goal-oriented development framework for CLI agents that shifts them from task-based to vision-based autonomous workflows; main agent acts as 'Tech Lead' coordinating sub-agents (Product Researcher, Strategist, Developer, QA, Reviewer) with persistent state across sessions (north-star.md, project-state.json), strategic-question-only interruptions, and a continuous Analyze -> Plan -> Execute -> Evaluate work loop. Very early stage (5 commits, 1 star)."
---

The framework targets the failure mode where CLI agents complete individual tasks but lose sight of project intent: instead of issuing tasks, the developer writes a north-star vision document, and the agent plans milestones against it, executing through a develop-QA-review-merge pipeline and asking only strategic questions. State lives in project-state.json and a progress log so sessions resume coherently, and the quality pipeline gates merges behind review. It installs via npx claude-northstar init for Claude Code and OpenCode. The repository is minimal (five commits, a single star), so adoption is essentially nil, but the design documents a vision-driven alternative to task-by-task prompting.
