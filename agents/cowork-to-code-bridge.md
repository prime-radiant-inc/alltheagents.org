---
name: "cowork-to-code-bridge"
slug: "cowork-to-code-bridge"
layout: "agent.njk"
category: "other"
maker: "abhinaykrupa"
license: "MIT"
url: "https://github.com/abhinaykrupa/cowork-to-code-bridge"
source_code_url: "https://github.com/abhinaykrupa/cowork-to-code-bridge"
source_available: "True"
platforms:
  - "IDE"
  - "Web"
  - "Desktop"
  - "Autonomous"
first_released: "2026-05-28"
current_release: "2026-08-07"
stars: "12"
language: "Python"
homepage: "https://github.com/abhinaykrupa/cowork-to-code-bridge#install--two-pastes-total"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "True"
plan_mode: "True"
model_providers: "Claude (haiku, sonnet, opus, fable)"
pricing: "open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/abhinaykrupa/cowork-to-code-bridge/main/install.sh | bash; brew install abhinaykrupa/tap/cowork-to-code-bridge; pip install cowork-to-code-bridge"
docs_url: "https://github.com/abhinaykrupa/cowork-to-code-bridge/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/cowork-to-code-bridge/"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Bridges Claude Cowork (cloud sandbox) to Claude Code on your local machine via a shared file-based queue — no open ports, no network listener. Outbound-only, idempotent task execution (safe retries after dropped connections/crashes), token-gated, only runs user-whitelisted scripts, daemon auto-restarts and survives reboots. Designed as a universal MCP-based local code execution backend."
---

Claude Cowork runs in a cloud sandbox that cannot reach the local machine, so any task needing the real filesystem - builds, tests, commits - stops at the sandbox wall. This bridge connects the two environments without opening a network port: a Claude skill converts a Cowork request into a JSON task written to a shared bridge folder, a launchd/systemd daemon on the local machine polls that folder roughly once per second, and an approved script hands the task to Claude Code on the host. Execution is whitelisted to user-approved scripts, idempotency keys make retries safe (a repeated git push returns the cached result), and spend caps plus permission scopes bound each task. Progress and results stream back into the Cowork chat. Developers who work in Cowork but need local execution use it; it is a third-party fill for a gap Anthropic's --remote-control only partly covers.
