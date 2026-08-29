---
name: "claudemacs"
slug: "claudemacs"
layout: "agent.njk"
category: "agent"
maker: "cpoile"
license: "MIT"
url: "https://github.com/cpoile/claudemacs"
source_code_url: "https://github.com/cpoile/claudemacs"
source_available: "True"
platforms: []
first_released: "2025-05-26"
current_release: "2026-08-10"
stars: "176"
language: "Emacs Lisp"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "no"
model_providers: "Any CLI-based AI tool (Claude Code, Codex, Gemini, Aider) via configurable tool registry"
pricing: "Free / open source (MIT)"
install_method: "Install via Doom Emacs package!, use-package with :vc (Emacs 30+), vc-use-package, straight.el, or manual clone. Requires Emacs 28.1+ and eat package."
docs_url: "https://github.com/cpoile/claudemacs#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/cpoile/claudemacs"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Emacs package for AI pair programming with Claude Code and other AI coding CLIs using the eat terminal emulator. Deliberately avoids agents, MCP, and IDE integration to let the LLM CLI 'shine in the terminal.' Features multi-tool support via configurable tool registry, multiple concurrent sessions per workspace, broadcast to all sessions, workspace/project-aware sessions, and rich Emacs integration (fix error at point, implement comment at point, add file/region context, transient menu UI, system notifications with sound)."
---

Claudemacs takes the position that Claude Code's terminal UI is the product, so instead of re-implementing chat, diffs, and tools in Elisp it embeds the real TUI in an Emacs terminal window and adds only the integration Emacs users miss: project-aware session management, notifications when the agent needs attention, keybindings that map terminal quirks (C-g to Esc), and commands to send the error at point or implement the comment at point. No agent, MCP, or IDE protocol layer is added, by design, to avoid consuming context. Emacs users who want Claude Code without leaving their editor are the audience, and the package is actively maintained.
