---
name: "oh-my-cli"
slug: "oh-my-cli"
layout: "agent.njk"
category: "agent"
maker: "qwen-code-dev-bot"
license: "Apache-2.0"
url: "https://github.com/qwen-code-dev-bot/oh-my-cli"
source_code_url: "https://github.com/qwen-code-dev-bot/oh-my-cli"
source_available: True
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-07-13"
current_release: "2026-08-12"
stars: "781"
language: "TypeScript"
homepage: null
mcp_support: "yes (stdio; mcp section in settings; --mcp-contract, --invoke-mcp; contract v1)"
plugin_support: "yes (provider, MCP, tool, and workflow extensions as governed contracts)"
claude_code_plugin: "no"
subagents: "partial (leased git worktrees for delegated agents; --create-worktree/--agent-identity)"
hooks: "partial (project-controlled hooks gated by folder trust)"
plan_mode: "yes (--plan emits deterministic dependency-ordered plan: understand -> implement -> verify -> review)"
model_providers: "any OpenAI-compatible (OpenAI, DashScope/Qwen, local Ollama, etc.)"
pricing: "open-source"
install_method: "npm (build + link)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Safety-first code-agent CLI: spoof-resistant approval previews (Unicode neutralization), folder-trust boundary (fail-closed), deterministic offline command policy (denies destructive git, credential access, path escape, device overwrite). Durable JSONL sessions with resume/compact/undo-redo. Headless-first JSON event stream for CI. Run summaries, scorecards, spend budgets. Self-developing via evidence-bound autonomous governance queue."
---

Safety-first code-agent CLI: spoof-resistant approval previews (Unicode neutralization), folder-trust boundary (fail-closed), deterministic offline command policy (denies destructive git, credential access, path escape, device overwrite). Durable JSONL sessions with resume/compact/undo-redo. Headless-first JSON event stream for CI. Run summaries, scorecards, spend budgets. Self-developing via evidence-bound autonomous governance queue.
