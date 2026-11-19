---
name: "Mingbird"
slug: "mingbird"
layout: "agent.njk"
category: "agent"
maker: "Mingbird"
license: "Apache-2.0"
url: "https://github.com/Mingbird/Mingbird-agent"
source_code_url: "https://github.com/Mingbird/Mingbird-agent"
source_available: "True"
homepage: null
docs_url: "https://github.com/Mingbird/Mingbird-agent#readme"
download_url: "https://github.com/Mingbird/Mingbird-agent/releases/latest"
install_method: "Windows: Mingbird-*-EN-Setup.exe from the latest GitHub release; Linux/macOS (experimental): CI-built tarball from Releases, then sh install-unix.sh; from source: pip install -r requirements.txt, then python agent_gui.py (or python ollama_agent.py for CLI)"
platforms:
  - "Desktop"
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Python"
first_released: "2026-09-17"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://github.com/Mingbird/Mingbird-agent/blob/main/AGENTS.md"
model_providers: "Ollama (default), any OpenAI-compatible local server (LM Studio, llama.app, llama-server, Jan, vLLM); optional OpenAI-compatible cloud endpoint"
pricing: "free"
stars: "32"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A local-first harness built for 2-9B models on integrated graphics: it runs the tests itself and feeds exact failures back, auto-backs-up every edit, and intercepts the repeating-command failure mode that stalls small models, so the same 2B model finishes real tasks on an ordinary laptop with zero outbound connections."
---

Mingbird starts from the claim that a 2B local model stalling in a cloud-style agent framework is a harness defect, not a model defect, and builds the harness that compensates for what small models cannot do: it runs tests and feeds back exact file:line failures, backs up every edit, detects and blocks repeated broken commands, and keeps prompt overhead frozen at 1319 estimated tokens so tool schemas fit small contexts. The Python harness drives Ollama or any OpenAI-compatible local server through prompt-model-tool-result cycles, invoking file, shell, and MCP tools itself, with a five-ring safety net around destructive operations and a one-click offline mode that keeps inference and files on the machine with no telemetry. It ships as a Windows desktop client with experimental Linux/macOS builds, a local web UI, and a CLI when run from source, with bilingual English/Chinese UI and bundled local voice input.
