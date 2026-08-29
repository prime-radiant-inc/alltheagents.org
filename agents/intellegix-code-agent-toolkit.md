---
name: "intellegix-code-agent-toolkit"
slug: "intellegix-code-agent-toolkit"
layout: "agent.njk"
category: "agent"
maker: "intellegix"
license: "MIT"
url: "https://github.com/intellegix/intellegix-code-agent-toolkit"
source_code_url: "https://github.com/intellegix/intellegix-code-agent-toolkit"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-02-16"
current_release: "2026-08-17"
stars: "56"
language: "Python, Node.js"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic (Claude Sonnet/Opus/Haiku), Perplexity (multi-model council: GPT, Claude, Gemini via Perplexity)"
pricing: "Free/open source (requires own Perplexity Pro/Max subscription for research features)"
install_method: "git clone to ~/.claude, then pip install (Python deps) and npm install (Node deps)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Automated loop driver with session continuity, budget enforcement, and stagnation detection; multi-agent parallel orchestration via git worktrees; multi-model council automation through Perplexity; portfolio governance with tier-based project management; 31 custom slash commands."
---

The toolkit treats Claude Code as a runtime and layers operational discipline on top. The loop driver keeps sessions continuous, enforces token budgets, detects stagnation, and scales models to task weight, while the multi-agent orchestrator farms work into isolated git worktrees under a guard hook that keeps the orchestrator from editing code directly. The Perplexity council is the distinctive piece: it drives a logged-in Perplexity session through Playwright to consult GPT, Claude, and Gemini at zero marginal cost, then synthesizes with Opus. Thirty-one commands cover planning, implementation, review, and a seven-tier frontend E2E pipeline. It installs by cloning straight into ~/.claude and assumes the operator accepts --dangerously-skip-permissions for autonomous runs.
