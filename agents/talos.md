---
name: "Talos"
slug: "talos"
layout: "agent.njk"
category: "agent"
maker: "talos-kernel"
license: "MIT"
url: "https://github.com/talos-kernel/Talos"
source_code_url: "https://github.com/talos-kernel/Talos"
source_available: "True"
homepage: "https://talos-agent.ch"
docs_url: "https://talos-agent.ch/docs/"
download_url: "https://github.com/talos-kernel/talos/releases"
install_method: "curl -fsSL https://talos-agent.ch/install.sh | bash (signed installer, verifies checksums, runs the test suite and stops); or git clone + venv + pip install --require-hashes -r requirements.lock; Homebrew tap on Apple Silicon; Pinokio"
platforms:
  - "CLI"
  - "Desktop"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Python"
first_released: "2026-08-06"
current_release: "2026-11-17"
maintained: "active"
mcp_support: "False"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://talos-agent.ch/docs/"
model_providers: "Ollama (local models), OpenAI/Anthropic/Gemini/other API providers, Claude via the Claude Code CLI, plus operator-defined OpenAI-compatible endpoints; model switching mid-process (/model, TALOS_MODEL)"
pricing: "free"
stars: "16"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Every action the model proposes passes a deterministic permission kernel before it runs: authority is a token bound to exact arguments, valid once for thirty seconds, with allow-once / allow-this-task / standing-rule grants, a sandboxed shell that refuses rather than running unprotected, an append-only audit trail, and 277 adversarial red-team scenarios run on every change."
---

Talos takes the position that the dangerous moment in agent design is the shell request, and that neither confirm-everything prompts nor regex blocklists are real answers. Its alternative: the model proposes and a deterministic PolicyKernel decides, returning ALLOW, NEEDS_HUMAN or DENY before any runner is reachable — a tool without a target extractor is denied by construction, catastrophic commands are refused outright, persistence and secrets ask, and ordinary workspace work just runs. Authority is a token bound to exact arguments and targets, valid once for thirty seconds; forgetting to call the gate produces no effect at all, and approval grants are deliberately tiered (allow once, allow this task, exact-action standing rules, deny) so the model can never choose a wider grant than you did. The agent is practical, not just safe: it runs from the terminal or as a Telegram bot (mail and a WhatsApp broker also work, all outbound-only), searches the web keylessly over DuckDuckGo, reads documents, views images and hears recordings locally, keeps bounded channel memory, and handles scheduled and background tasks under an unattended ceiling where anything needing a human is refused rather than skipped. Coding work is a tool family like the rest: run_shell under bubblewrap or sandbox-exec, read_file/write_file with atomic publication and snapshot-backed undo, git with credentials behind per-op approval, plus opt-in bounded delegation of coding jobs to a confined Claude, Codex or agy worker. Skills are managed files the agent writes once under approval, entity knowledge comes from an operator-owned file, and every run leaves exec.intent receipts a `talos why` command can explain. It is MIT, self-hosted on macOS, Linux and Raspberry Pi, and suits an operator who wants an agent they can hand a shell to because it can prove what it will not do.
