---
name: "PurrCode"
slug: "purrcode"
layout: "agent.njk"
category: "agent"
maker: "Weilin0723"
license: "Apache-2.0"
url: "https://github.com/Weilin0723/PurrCode"
source_code_url: "https://github.com/Weilin0723/PurrCode"
source_available: "True"
platforms: []
first_released: "2026-07-25"
current_release: "2026-08-13"
stars: "168"
language: "Rust"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Ollama, LM Studio, NVIDIA NIM, remote providers via /connect"
pricing: "Free/open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/Weilin0723/PurrCode/v1.0.0/scripts/install.sh | sh; or npm install --global @minaovo/purrcode; or cargo build --release (Rust 1.88+)"
docs_url: "https://weilin0723.github.io/PurrCode/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Weilin0723/PurrCode/releases/latest"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Judgment-first local-first coding agent runtime where model output is treated as a proposal, never authority; durable authorization + recorded validation for every native action; native pure-Rust desktop IDE (no browser/Electron/VS Code); works in isolated git worktrees; evidence-based model selection with budget enforcement; /mode switches between Ask, Plan, Build, Review."
---

PurrCode starts from the position that model output is a proposal and never authority: repository content, downloaded skills, and generated code are all untrusted until a separate authorization layer approves each action, re-checks that approval immediately before execution, and records the validation afterward. Permission modes are daemon-enforced constraints rather than prompt-level politeness, so a read-only mode genuinely prevents writes, and sandboxing via sandbox-exec or Bubblewrap is reported honestly rather than oversold. Agent work runs in detached Git worktrees so uncommitted user work is never silently stashed or overwritten. A pure-Rust desktop IDE built on egui shares one daemon-owned session with the terminal TUI, letting a task move between interfaces without losing state. Local-first operation connects to Ollama or LM Studio by default with NVIDIA NIM as a first-class cloud option, and credentials stay in the OS keychain, never in model context. Developers who want a security-enforced local agent rather than a prompt-level one use PurrCode.
