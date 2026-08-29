---
name: "agent-sandbox"
slug: "agent-sandbox"
layout: "agent.njk"
category: "agent"
maker: "mattolson"
license: "MIT"
url: "https://github.com/mattolson/agent-sandbox"
source_code_url: "https://github.com/mattolson/agent-sandbox"
source_available: "True"
platforms: []
first_released: "2026-01-17"
current_release: "2026-08-02"
stars: "198"
language: "Go"
homepage: "https://github.com/mattolson/agent-sandbox"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, Gemini, OpenCode, Pi, Factory, Copilot, Hermes (runs agents in sandbox)"
pricing: "Free / open-source"
install_method: "curl -fsSL https://github.com/mattolson/agent-sandbox/releases/latest/download/install.sh | sh (or download binary from Releases)"
docs_url: "https://github.com/mattolson/agent-sandbox/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/mattolson/agent-sandbox/releases/latest"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Runs AI coding agents in a locked-down local sandbox with minimal filesystem access, configurable network egress via sidecar proxy (mitmproxy), proxy-side secret injection where the agent container never sees API keys/tokens, iptables firewall preventing direct outbound bypass, hot-reloadable policies, and seamless agent switching with preserved state/credentials."
---

Giving a coding agent your real machine hands it your credentials and your whole filesystem, which is why many teams refuse to run them locally; agent-sandbox wraps agents (Claude Code, Codex, Gemini, OpenCode, Copilot, and others) in a Debian-based container that mounts only the repo directory. A mitmproxy sidecar enforces fine-grained network policy — allowed hosts with scheme, method, path, and query rules, plus repo-scoped git access with proxy-side credential injection — while iptables blocks any outbound traffic that tries to skip the proxy. Agent state persists across runs in volumes, policies hot-reload, and VS Code or JetBrains devcontainers can attach to the sandbox. Security-conscious developers on Apple Silicon (Colima + Docker) running semi-trusted agents are the users.
