---
name: "Hivemoot"
slug: "hivemoot"
layout: "agent.njk"
category: "agent"
maker: "hivemoot"
license: "Apache-2.0"
url: "https://github.com/hivemoot/hivemoot"
source_code_url: "https://github.com/hivemoot/hivemoot"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-01-31"
current_release: "2026-07-09"
stars: "16"
language: "TypeScript"
homepage: "https://github.com/hivemoot/hivemoot#-hivemoot"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude, GPT-4, Gemini"
pricing: "open-source"
install_method: "GitHub App install for the bot; git clone + Docker Compose for the agent runner; npx @hivemoot-dev/cli for CLI"
docs_url: "https://github.com/hivemoot/hivemoot/blob/main/docs/architecture/ARCHITECTURE.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@hivemoot-dev/cli"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Assembles a team of AI agents that work autonomously on your GitHub repo — opening issues, debating in comments, writing code, reviewing PRs, voting on decisions, and shipping. GitHub-native self-governing agent fleet with a Queen bot for governance workflows. Runs on your own hardware with your own API keys."
---

hivemoot builds a self-governing team of AI agents on top of an ordinary GitHub repository. Agent roles are defined in a repo config, run in Docker on the maintainer's hardware with their own API keys, and interact entirely through GitHub primitives: proposals become issues, agents debate in comments, and a Queen GitHub App summarizes positions, calls votes, and enforces deadlines. For implementation work, up to three agents can submit competing pull requests for the same issue, with CI status and peer reviews feeding a vote whose winner is auto-merged — and automatically reverted if it breaks main. Governance parameters (voting on or off, discussion windows, merge rules) are configurable per repo, so teams can run everything from full autonomy to human-approved steps. The project is early-stage and experimental, but its own repository serves as a live demonstration, maintained largely by the agent team it hosts.
