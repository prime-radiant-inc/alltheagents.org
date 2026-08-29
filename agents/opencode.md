---
name: "OpenCode"
slug: "opencode"
layout: "agent.njk"
category: "agent"
maker: "anomalyco"
license: "MIT"
url: "https://github.com/anomalyco/opencode"
source_code_url: "https://github.com/anomalyco/opencode"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-04-30"
current_release: "2026-08-20"
stars: null
language: "TypeScript, JavaScript (Node.js, Bun, Turborepo monorepo)"
homepage: "https://opencode.ai"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "yes"
plan_mode: "True"
model_providers: "Any LLM provider (via API key configuration); curated tested models via OpenCode Zen"
pricing: "Free / open-source (MIT)"
install_method: "curl -fsSL https://opencode.ai/install | bash; or npm/bun/pnpm/yarn install -g opencode-ai; or brew install opencode-ai; or scoop/choco/pacman/paru/mise/nix; or download desktop app from releases"
docs_url: "https://opencode.ai/docs"
plugin_docs_url: "https://opencode.ai/docs/plugins"
config_docs_url: "https://opencode.ai/docs/config"
download_url: "https://github.com/anomalyco/opencode"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "tiennm"
what_makes_it_special: "Fully open-source AI coding agent with both terminal UI and beta desktop app; built-in switchable agents (build/plan) via Tab key - the plan agent is read-only, denies file edits, and asks permission before bash commands; @general subagent for complex searches/multistep tasks; MCP server support; plugin system; 20+ language README translations; broad package manager support across all major OSes. Major project (199k stars, 15k+ commits)."
---

OpenCode positions itself as the fully open-source alternative to closed terminal coding agents, MIT-licensed and hosted under the anomalyco organization after starting in the sst org. Its architecture separates a client/server core from every interface: the same agent serves the terminal UI, a beta desktop app, IDE extensions, and third-party clients, which is why an ecosystem of plugins, Neovim integrations, Android clients, and orchestrators has grown around it. Built in TypeScript on Bun, it exposes built-in build and read-only plan agents switchable with Tab, a @general subagent, and hooks plus plugin and config surfaces documented at opencode.ai/docs. Distribution is unusually broad — curl script, npm, Homebrew, scoop, choco, pacman, AUR, mise, nix — and the project shows 202k stars, 26k forks, and 15,600 commits. It serves developers who want a Claude Code-class terminal agent with no vendor lock-in.
