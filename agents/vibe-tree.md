---
name: "vibe-tree"
slug: "vibe-tree"
layout: "agent.njk"
category: "multiplexer"
maker: "sahithvibudhi"
license: "MIT"
url: "https://github.com/sahithvibudhi/vibe-tree"
source_code_url: "https://github.com/sahithvibudhi/vibe-tree"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
first_released: "2025-07-29"
current_release: "2026-07-25"
stars: "266"
language: "TypeScript"
homepage: "https://sahithvibudhi.github.io/vibe-tree/"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "False"
model_providers: "Claude Code, OpenAI Codex CLI, Gemini CLI, Aider, opencode, any terminal-based agent CLI"
pricing: "Free / open-source (MIT)"
install_method: "macOS: brew install --cask --no-quarantine sahithvibudhi/tap/vibetree; Windows/Linux: download installer; From source: pnpm install then pnpm dev:desktop"
docs_url: "https://sahithvibudhi.github.io/vibe-tree/docs/"
plugin_docs_url: null
config_docs_url: "https://sahithvibudhi.github.io/vibe-tree/docs/config.html"
download_url: "https://github.com/sahithvibudhi/vibe-tree/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Every AI coding task gets its own isolated git worktree with its own branch and persistent terminal, enabling true parallel agent execution without agents stomping on each other. Supports any terminal-based agent CLI. Usable as desktop app or browser-accessible server (including phone access via QR pairing). One-click disposal of failed experiments."
---

Running several AI agents against one checkout means merge conflicts and clobbered edits, and terminal-based agents die when a window closes. VibeTree gives every task an isolated git worktree with its own branch and a persistent terminal whose scrollback survives reloads and reconnects, so parallel agents never stomp on each other and long-running sessions survive reconnects. A fleet view shows which agents are working, waiting, or done (with a chime when one needs attention), a changes view puts the diff beside the terminal so a comment can be sent back as the agent's next prompt, and dev-server URLs are detected for browser preview. Because it hosts real terminals, it works with claude, codex, gemini, aider, or any shell command, and a standalone server mode adds phone access via QR pairing. Developers running parallel agent tasks use it as a desktop app or self-hosted server; it is MIT-licensed and actively maintained.
