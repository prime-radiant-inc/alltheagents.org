---
name: "InstallCursorEditorLinux"
slug: "installcursoreditorlinux"
layout: "agent.njk"
category: "other"
maker: "IsRengel"
license: "Apache-2.0"
url: "https://github.com/IsRengel/InstallCursorEditorLinux"
source_code_url: "https://github.com/IsRengel/InstallCursorEditorLinux"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-12-11"
current_release: "2026-01-21"
stars: "160"
language: "Shell"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "git clone https://github.com/IsRengel/InstallCursorEditorLinux.git --depth=1 && cd InstallCursorEditorLinux && ./install.sh"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/IsRengel/InstallCursorEditorLinux"
maintained: "dormant"
sources:
  - "github_deep"
what_makes_it_special: "Shell script installer that sets up Cursor AI Code Editor as a desktop application on any Linux distribution (creates .desktop file, configures automatic updates via systemd). Deprecated: Cursor now ships an official .deb package; the repo is kept for historical/educational purposes."
---

InstallCursorEditorLinux existed because Cursor initially shipped only as an AppImage with no Linux packaging. The script downloaded the AppImage, installed it under /opt/cursor, generated a .desktop entry, and wired a systemd unit for automatic updates across Debian, Arch, Fedora, OpenSUSE, Gentoo, and Solus. Once Cursor shipped an official .deb, the README added a deprecation notice directing users to cursor.com. The 160-star repo survives as an educational example of packaging AppImage software for multiple distributions.
