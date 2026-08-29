---
name: "oh-my-cli"
slug: "oh-my-cli"
layout: "agent.njk"
category: "agent"
maker: "qwen-code-dev-bot"
license: "Apache-2.0"
url: "https://github.com/qwen-code-dev-bot/oh-my-cli"
source_code_url: "https://github.com/qwen-code-dev-bot/oh-my-cli"
source_available: "True"
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
docs_url: "https://github.com/qwen-code-dev-bot/oh-my-cli#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/qwen-code-dev-bot/oh-my-cli"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Safety-first code-agent CLI: spoof-resistant approval previews (Unicode neutralization), folder-trust boundary (fail-closed), deterministic offline command policy (denies destructive git, credential access, path escape, device overwrite). Durable JSONL sessions with resume/compact/undo-redo. Headless-first JSON event stream for CI. Run summaries, scorecards, spend budgets. Self-developing via evidence-bound autonomous governance queue."
---

oh-my-cli is a coding agent CLI built around the premise that safety guarantees must be structural rather than advisory. Approval previews are hardened against Unicode spoofing, untrusted workspaces fail closed on mutations, and a deterministic command policy denies destructive operations even in yolo mode. Sessions are durable JSONL records that can be resumed, compacted, and undone turn-by-turn with file-level checkpoints. Headless runs emit a versioned JSON event stream with spend budgets, tool-call caps, and signed evidence archives for audit. MCP servers are declared as versioned contracts resolved read-only, and leased git worktrees give each mutating agent an isolated workspace with idempotent lease semantics.
