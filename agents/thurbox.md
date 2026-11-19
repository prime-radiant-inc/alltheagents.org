---
name: "Thurbox"
slug: "thurbox"
layout: "agent.njk"
category: "multiplexer"
maker: "Thurbeen"
license: "MIT"
url: "https://github.com/Thurbeen/thurbox"
source_code_url: "https://github.com/Thurbeen/thurbox"
source_available: "True"
homepage: "https://thurbox.thurbeen.eu/"
docs_url: "https://thurbox.thurbeen.eu/docs/"
download_url: "https://github.com/Thurbeen/thurbox/releases"
install_method: "curl -fsSL https://raw.githubusercontent.com/Thurbeen/thurbox/main/scripts/install.sh | sh (macOS/Linux; also Homebrew/AUR/Nix on the Installation page); irm .../scripts/install.ps1 | iex (Windows); cargo build --release from source; requires tmux >= 3.2 (psmux on native Windows), git, and at least one coding-agent CLI"
platforms:
  - "CLI"
  - "Desktop"
autonomy_level: []
specialization: "general"
language: "Rust"
first_released: "2026-02-12"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "False"
hooks: "True"
plan_mode: "False"
plugin_docs_url: "https://thurbox.thurbeen.eu/plugins.html"
config_docs_url: "https://thurbox.thurbeen.eu/docs/configuration.html"
model_providers: "Delegates to installed agent CLIs — Fleet bundles harness profiles for Claude Code, Codex, pi, opencode, kilo, omp, Qwen Code, Copilot CLI, and Kimi Code, each bringing its own provider and model; no model is ever passed through Thurbox"
pricing: "free"
stars: "120"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A tmux-based TUI that runs several coding-agent CLIs side by side, where each session survives crashes, restarts, and quitting the interface because a separate Fleet engine manages every session as a Task on a remote-capable runtime — and every pane of the interface, the session list included, is an editable Lua file reloaded with F10."
---

Thurbox exists to run many coding agents at once without losing one when an interface closes: sessions are Fleet Tasks kept alive in tmux (psmux on native Windows), so a crash, a restart, or Ctrl+Q stops nothing, and a worktree is created per session so agents never fight over one checkout. The TUI lists every session from every Fleet you configure — a laptop alongside a box over SSH or in WSL, with unreachable Fleets kept in the list — and the new-session flow picks a Fleet, a place, a repository, then an agent from that Fleet's harness profiles (Claude Code, Codex, pi, opencode, kilo, omp, Qwen Code, Copilot CLI, Kimi Code, launched unmodified). Developers who juggle several agent subscriptions are the audience, and the interface itself is theirs to reshape: panes are Lua plugins in a directory they own, with a shipped AGENTS.md so an agent can be asked to rearrange its own TUI. The MIT Rust project releases weekly and documents its whole three-component architecture (thurbox, Fleet, runtimes) on its site.
