---
name: "Hivelore"
slug: "hivelore"
layout: "agent.njk"
category: "agent"
maker: "Doucs91"
license: "Apache-2.0"
url: "https://github.com/Doucs91/hivelore"
source_code_url: "https://github.com/Doucs91/hivelore"
source_available: True
platforms:
  - "CLI"
first_released: "2026-04-25"
current_release: "2026-08-17"
stars: "1"
language: "TypeScript"
homepage: null
mcp_support: True
plugin_support: True
claude_code_plugin: null
subagents: null
hooks: True
plan_mode: null
model_providers: "Claude Code, Cursor, VS Code, Cline, Windsurf, Codex, Continue, GitHub Copilot, Cody, Gemini CLI, Zed, Aider, Roo"
pricing: "Free / open-source"
install_method: "npm install -g @hivelore/cli (optional: npm install -g @hivelore/embeddings for local semantic search)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Doucs91/hivelore"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Deterministic policy gate for AI coding agents: briefs agents with team-specific repo knowledge before they act, then blocks commits that repeat past mistakes via MCP, Git hooks, and CI. Converts captured team mistakes into deterministic blocking gates (regex, ast-grep structural patterns, or shell/test command sensors) that refuse the commit repeating them - same diff, same verdict, every machine. The command sensor bridge routes your existing tests as behavioural oracles; prove-RED requires a reproducible incident state before a sensor can block. Cold-start seeds from stack packs, git history scars, and scanner findings (SonarQube/SARIF/ESLint). Fully reversible (rm -rf .ai)."
---

Deterministic policy gate for AI coding agents: briefs agents with team-specific repo knowledge before they act, then blocks commits that repeat past mistakes via MCP, Git hooks, and CI. Converts captured team mistakes into deterministic blocking gates (regex, ast-grep structural patterns, or shell/test command sensors) that refuse the commit repeating them - same diff, same verdict, every machine. The command sensor bridge routes your existing tests as behavioural oracles; prove-RED requires a reproducible incident state before a sensor can block. Cold-start seeds from stack packs, git history scars, and scanner findings (SonarQube/SARIF/ESLint). Fully reversible (rm -rf .ai).
