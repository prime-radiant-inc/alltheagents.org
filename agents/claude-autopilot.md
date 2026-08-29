---
name: "Claude Autopilot"
slug: "claude-autopilot"
layout: "agent.njk"
category: "multiplexer"
maker: "benbasha"
license: "MIT"
url: "https://open-vsx.org/extension/benbasha/claude-autopilot"
source_code_url: "https://github.com/benbasha/Claude-Autopilot.git"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-08-21"
current_release: "2025-08-21"
stars: null
language: "TypeScript"
homepage: "https://github.com/benbasha/Claude-Autopilot#readme"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (via Claude Code CLI)"
pricing: "free"
install_method: "Install from Open VSX"
docs_url: "https://github.com/benbasha/Claude-Autopilot#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-vsx.org/extension/benbasha/claude-autopilot"
maintained: "dormant"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Automated Claude Code task management with queue processing and auto-resume"
---

Claude Autopilot addresses the operational problem of running long batches of Claude Code tasks unattended: queued work stalls when usage limits reset, the machine sleeps, or the CLI process dies. The extension launches each queued prompt as a sequential Claude Code run, monitors process health, retries failures, detects rate-limit messages, and resumes automatically when the limit window resets, while keeping the machine awake. A local web server with password and QR-code login provides mobile monitoring. Developers use it for overnight batches such as refactoring, migrations, and documentation generation; it requires an existing Claude Code installation and subscription.
