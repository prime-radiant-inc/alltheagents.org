---
name: "Auggie"
slug: "auggie"
layout: "agent.njk"
category: "agent"
maker: "augmentcode"
license: "Custom Proprietary"
url: "https://github.com/augmentcode/auggie"
source_code_url: "https://github.com/augmentcode/auggie"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2025-09-08"
current_release: "2026-08-20"
stars: "272"
language: "TypeScript"
homepage: "https://www.augmentcode.com/"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Augment Code"
pricing: "usage"
install_method: "npm install -g @augmentcode/auggie@latest"
docs_url: "https://docs.augmentcode.com/cli/overview"
plugin_docs_url: null
config_docs_url: "https://docs.augmentcode.com/cli/custom-commands-examples"
download_url: "https://www.npmjs.com/package/@augmentcode/auggie"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Augment's agentic coding CLI for the terminal. Understands your codebase and helps ship faster by analyzing code, making safe edits, and automating routine tasks via natural language."
---

Auggie is the command-line counterpart to Augment Code's IDE extensions, bringing the company's codebase-aware agent to the terminal. It builds a persistent codebase understanding (Augment's context engine) so edits and refactors respect project structure rather than isolated files, driven by natural language from any terminal. Custom slash commands live as markdown files with frontmatter in .augment/commands, shared per repository like dotfiles. Headless flags (-p, --quiet) and official GitHub Actions (augment-agent, review-pr, describe-pr) make it usable in CI for PR review and description generation. It requires Node.js 22+, installs via npm, and is actively maintained, targeting developers who already use Augment's context engine and want the same agent in terminals and CI.
