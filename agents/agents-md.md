---
name: "agents-md"
slug: "agents-md"
layout: "agent.njk"
category: "other"
maker: "FerroxLabs"
license: "MIT"
url: "https://github.com/FerroxLabs/agents-md"
source_code_url: "https://github.com/FerroxLabs/agents-md"
source_available: "yes"
platforms:
  - "CLI"
first_released: "2026-04-19"
current_release: "2026-05-31"
stars: "657"
language: "Markdown"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Any (tool-agnostic instructions file, not a model integration)"
pricing: "open-source"
install_method: "curl"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://raw.githubusercontent.com/FerroxLabs/agents-md/main/AGENTS.md"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "A drop-in AGENTS.md file (~200 lines) that makes every coding agent (Claude Code, Codex, Cursor, Gemini CLI, Aider, Windsurf, Copilot, Devin) behave like a senior engineer — kills sycophancy, stops drive-by refactors, forces verification loops, surfaces ambiguities. Universal single-file approach: one AGENTS.md read natively by most agents; symlink covers Claude Code (CLAUDE.md) and Gemini CLI (GEMINI.md). Self-improving: Section 11 'Project Learnings' grows automatically as you correct the agent. Compact by design (~200 lines ensures rules stay loaded in context). Synthesizes Karpathy's four LLM coding principles, Boris Cherny's Claude Code workflow, and Anthropic's official best practices. Not a code project — a behavioral scaffold Markdown file."
---

Coding agents tend toward agreement instead of pushback, unrelated refactoring, and claiming completion without evidence; existing fixes are scattered across blog posts and tool-specific rules files. This project condenses Karpathy's failure-mode analysis, Boris Cherny's Claude Code workflow, and Anthropic's official guidance into roughly 200 lines that stay short enough for agents to actually follow, following the cross-tool AGENTS.md standard with symlinks for CLAUDE.md and GEMINI.md. Sections 0-9 are fixed behavioral scaffolding; only the project-context section is edited, and a learnings section grows as the user corrects the agent. The file requires no plugin or config for most tools. It targets developers who want baseline senior-engineer behavior from any agent without per-tool setup.
