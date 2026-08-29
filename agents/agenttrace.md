---
name: "agenttrace"
slug: "agenttrace"
layout: "agent.njk"
category: "other"
maker: "luoyuctl"
license: "MIT"
url: "https://github.com/luoyuctl/agenttrace"
source_code_url: "https://github.com/luoyuctl/agenttrace"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-05-01"
current_release: "2026-08-17"
stars: "121"
language: "Rust"
homepage: "https://github.com/luoyuctl/agenttrace"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free (MIT); supports custom pricing overrides via pricing-overrides.json"
install_method: "brew install luoyuctl/tap/agenttrace; or npm install -g @zack78/agenttrace; or winget install --id Luoyuctl.AgentTrace; or cargo install --git https://github.com/luoyuctl/agenttrace agenttrace"
docs_url: "https://github.com/luoyuctl/agenttrace/blob/master/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/luoyuctl/agenttrace/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Local-first terminal TUI and report generator for AI coding-agent session history; reads logs from Claude Code, Codex CLI, Gemini CLI, Qwen Code, Cline, Aider, Cursor, and more; provides cost, token, and time analysis with baseline comparison; MCP governance inspection; all processing local"
---

After a week of agent work, developers have no easy answer to basic questions: what did the runs cost, which sessions hung, why was that task slow. AgentTrace parses local logs from Claude Code, Codex CLI, Gemini CLI, Qwen Code, Cline, Aider, Cursor exports, OpenCode, OpenClaw, Kimi CLI, and generic JSONL traces, then produces spend breakdowns by agent and model, slow-task diagnosis (retry loops, hanging sessions, context pressure), and governance reports with Git delivery correlation. Reports export as JSON, Markdown, or self-contained HTML and can be compared against a local baseline to catch regressions. Reports label their own data completeness as Detailed, Aggregate, or Limited rather than overstating coverage. It is distributed as a Rust binary via brew, npm, winget, and cargo.
