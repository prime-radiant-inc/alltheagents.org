---
name: "Hazzel"
slug: "hazzel"
layout: "agent.njk"
category: "agent"
maker: "mukundzha"
license: "Apache-2.0"
url: "https://github.com/mukundzha/hazzel"
source_code_url: "https://github.com/mukundzha/hazzel"
source_available: "True"
homepage: "https://agenthazzel.vercel.app"
docs_url: "https://github.com/mukundzha/hazzel/blob/main/README.md"
download_url: null
install_method: "uvx hazzel (try without installing; or pip install hazzel / uv tool install hazzel / pipx install hazzel), then run hazzel in your project"
platforms:
  - "CLI"
autonomy_level:
  - "pair-programmer"
  - "agentic"
specialization: "general"
language: "Python"
first_released: "2026-09-07"
current_release: "2026-10-26"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "False"
hooks: "False"
plan_mode: "True"
plugin_docs_url: null
config_docs_url: null
model_providers: "Groq, OpenAI, Anthropic, Mistral, Gemini, DeepSeek, OpenRouter, Ollama"
pricing: "BYOK"
stars: "29"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A terminal coding agent you can read end to end (~10k lines of Python, agent/core.py is the whole loop) that shows every write as an approved diff first and keeps automatic checkpoints, so /undo reverts only the agent's hunks while keeping your own later edits."
---

Hazzel is a deliberately small terminal coding agent by Mukund Jha, built for developers who want to see exactly what is about to happen to their files before it happens. The loop lives in one readable file (src/hazzel/agent/core.py) driving sixteen tools: reads, searches and globs are answered locally with no model round trip, while every write stops at a diff you approve — one decision per turn, never re-prompted — and shell commands are sandboxed to the project root with git reset --hard and clean blocked outright. Writes are checkpointed automatically, so /undo reverts only the agent's hunks and keeps edits you made afterwards, and provider-reported token costs are parsed into real dollars with a live tokens-dollar line and /usage and /budget commands. It extends through a minimal MCP stdio client configured in .hazzel/mcp.json and SKILL.md skills that load on demand, and it runs one-shot in CI via hazzel -p with JSON output and real exit codes. Eight providers work with one environment variable each, including keyless local Ollama. The project is honest about being early-stage — no autonomous PRs, no cloud dashboard, no session sync — and stays small on purpose for users who want an inspectable agent next to their editor rather than a heavy automated one.
