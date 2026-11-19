---
name: "tmux-restore"
slug: "tmux-restore"
layout: "agent.njk"
category: "multiplexer"
maker: "andrewboldi"
license: "MIT"
url: "https://github.com/andrewboldi/tmux-restore"
source_code_url: "https://github.com/andrewboldi/tmux-restore"
source_available: "True"
homepage: null
docs_url: "https://github.com/andrewboldi/tmux-restore/tree/main/docs"
download_url: null
install_method: "curl -fsSL https://raw.githubusercontent.com/andrewboldi/tmux-restore/main/install.sh | bash (installs tmux, TPM, and the plugins and turns everything on); manual install documented in docs/install-manually.md"
platforms:
  - "CLI"
autonomy_level: []
specialization: "general"
language: "Shell"
first_released: "2026-10-31"
current_release: "2026-11-16"
maintained: "active"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://github.com/andrewboldi/tmux-restore/blob/main/CONTRIBUTING.md"
model_providers: "Restores panes running Claude Code, Codex CLI, Gemini CLI, opencode, pi, or ai-memory-wrapped harnesses; each agent keeps its own accounts and providers"
pricing: "free"
stars: "83"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Reboot-proof tmux built on tmux-resurrect and tmux-continuum: it saves every minute and once more at shutdown via a systemd/launchd service, and per-agent adapters find the exact conversation id in each agent's own session files (Claude Code's running-session registry, Codex's open rollout file) so panes reopen mid-conversation — while a custom-adapter directory, ai-memory wrapper support, and saved scrollback round it out."
---

tmux-restore addresses a reboot the way a developer experiences it: a dozen tmux windows gone, and with them the agent conversations running inside. On top of tmux-resurrect and tmux-continuum — which already bring back sessions, windows, splits, and working directories — it adds an agent layer: a small adapter per CLI finds the conversation's id in the agent's own on-disk state (Claude Code's registry of running sessions, Codex's open rollout file, the newest session file for Gemini CLI, opencode, and pi, or the harness child of an ai-memory wrapper) and saves the resume command instead of a bare shell. Saves run every minute and once more at shutdown through a systemd (Linux) or launchd (macOS) service, so a power cut costs at most a minute; panes that were running editors, log followers, or anything in @resurrect-processes come back typed, and zsh keeps anything unrecognized waiting on the prompt rather than lost. New agents are one short adapter file, contributed or kept private in ~/.config/tmux-restore/agents/. Terminal-centric developers whose Claude Code or Codex sessions live in tmux are exactly the audience; the project ships a per-adapter unit test suite against fake /proc plus a CI that checks the real lookups on macOS.
