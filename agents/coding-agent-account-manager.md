---
name: "coding_agent_account_manager"
slug: "coding-agent-account-manager"
layout: "agent.njk"
category: "other"
maker: "Dicklesworthstone"
license: "MIT"
url: "https://github.com/Dicklesworthstone/coding_agent_account_manager"
source_code_url: "https://github.com/Dicklesworthstone/coding_agent_account_manager"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-17"
current_release: "2026-08-17"
stars: "156"
language: "Go"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Claude Code (Claude Max), Codex CLI (GPT Pro), Gemini CLI (Gemini Ultra, legacy), Antigravity CLI, Grok Build (xAI); fixed-cost subscriptions only, not API keys"
pricing: "Free / open-source (manages subscriptions like Claude Max $200, GPT Pro $200, Gemini Ultra $275)"
install_method: "Homebrew (brew install dicklesworthstone/tap/caam), Scoop, curl install script, Go install, or build from source"
docs_url: "https://github.com/Dicklesworthstone/coding_agent_account_manager#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Dicklesworthstone/coding_agent_account_manager/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Sub-100ms OAuth token file swapping to instantly switch between fixed-cost subscription accounts (Claude Max, GPT Pro, Gemini Ultra) when hitting rate limits without browser re-auth. Features smart rotation algorithms, cooldown tracking, isolated/shallow profiles for parallel sessions, and automatic failover via `caam run`."
---

Subscription coding agents stop at usage ceilings, and the official recovery path is a slow browser re-authentication that breaks flow and parallel workflows. caam treats stored OAuth credential files as swappable state: it backs up each CLI's auth files (Claude Code, Codex, Gemini CLI, Antigravity, Grok Build) into a local vault and restores a different account's files on demand in under 100 milliseconds, with no browser round trip. A rotation engine tracks cooldowns and health per account, `caam run` wraps the underlying CLI and fails over automatically on rate limits, and isolated profiles let parallel sessions run against separate accounts. The Go CLI works offline with no daemons, exposes JSON output for use by other agents, and manages fixed-cost subscriptions rather than metered API keys. Individual developers and orchestrator operators running many parallel agent sessions are its users.
