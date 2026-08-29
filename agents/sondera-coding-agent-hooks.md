---
name: "sondera-coding-agent-hooks"
slug: "sondera-coding-agent-hooks"
layout: "agent.njk"
category: "other"
maker: "sondera-ai"
license: "MIT"
url: "https://github.com/sondera-ai/sondera-coding-agent-hooks"
source_code_url: "https://github.com/sondera-ai/sondera-coding-agent-hooks"
source_available: "True"
platforms: []
first_released: "2026-02-27"
current_release: "2026-08-19"
stars: "222"
language: "Rust"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: "Free"
install_method: "Download prebuilt archive from GitHub Releases"
docs_url: "https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sondera-ai/sondera-coding-agent-hooks/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Reference monitor for AI coding agents; Rust hook binaries and Cedar policies intercept every shell command, file operation, and web request to block exfiltration, destructive behaviors, and enforce information flow control. Hook adapters for Claude Code, Cursor, Copilot, Gemini CLI, Antigravity, Codex, Hermes, OpenCode, OpenHands, VS Code."
---

The project addresses a concrete gap: coding agents execute shell commands, file writes, and web requests with limited enforcement, and most guardrails are advisory. Sondera's adapters for Claude Code, Cursor, Copilot, Gemini CLI, Codex, OpenCode, OpenHands, and others normalize agent events and forward them over local gRPC; the service evaluates Cedar policies and YARA signatures deterministically, with optional LLM classifiers for data sensitivity, and can block, escalate to an approval UI, steer via context injection, redact, or terminate. Enforcement fails closed — if the harness is unreachable, hooks deny — and no API key or external service is required. A TUI replays adjudicated trajectories for audit. It was released alongside Unprompted 2026 and Black Hat Arsenal 2026 talks for teams that need policy enforcement, not suggestions, around coding agents.
