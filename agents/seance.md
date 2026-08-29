---
name: "seance"
slug: "seance"
layout: "agent.njk"
category: "multiplexer"
maker: "no1msd"
license: "MIT"
url: "https://github.com/no1msd/seance"
source_code_url: "https://github.com/no1msd/seance"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-08"
current_release: "2026-05-27"
stars: "128"
language: "Zig"
homepage: "https://no1msd.github.io/seance"
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: null
pricing: "Free (MIT)"
install_method: "Arch: yay -S seance; Nix: nix run git+https://github.com/no1msd/seance; AppImage from GitHub Releases; from source: zig build (requires Zig 0.15.2+, GTK4, libadwaita)"
docs_url: "https://no1msd.github.io/seance"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/no1msd/seance/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Scrolling terminal multiplexer that auto-detects and tracks AI coding agent sessions (Claude Code, Codex, Pi) live in the sidebar; surfaces permission requests and task completions as desktop notifications; fully scriptable via seance ctl over Unix domain socket with JSON output; GPU-accelerated rendering via libghostty"
---

Long agent sessions scroll vertically for thousands of lines, which tiling multiplexers handle poorly; Séance arranges panes as a horizontal scrolling strip and adds agent awareness — sidebar status for working, waiting-on-permission, and idle, with desktop notifications for permission requests and completions. The agents themselves are unmodified external processes; detection is automatic and other agents integrate via a hook config, while non-hook agents still get ordinary multiplexer features. A Unix-socket CLI (`seance ctl`) lets scripts and agents create workspaces, open panes, and read output as JSON, effectively letting an agent manage its own terminal. It is written in Zig on libghostty, supports X11 and Wayland, and installs from AUR, Nix, or AppImage. It suits Linux developers running several agent sessions who want visibility without leaving the terminal.
