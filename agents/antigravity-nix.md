---
name: "antigravity-nix"
slug: "antigravity-nix"
layout: "agent.njk"
category: "agent"
maker: "jacopone"
license: "MIT"
url: "https://github.com/jacopone/antigravity-nix"
source_code_url: "https://github.com/jacopone/antigravity-nix"
source_available: True
platforms:
  - "IDE"
first_released: "2025-11-18"
current_release: "2026-08-19"
stars: "160"
language: "Nix"
homepage: "https://antigravity.google"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "nix run github:jacopone/antigravity-nix; or add as an input to NixOS/Home Manager configurations"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jacopone/antigravity-nix/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Auto-updating Nix Flake for Google Antigravity (an agentic IDE/CLI); auto-updates 3x/week via GitHub Actions with hash verification and build testing; provides three components (Antigravity 2.0 Base App, IDE, and CLI 'agy'); offers an FHS bubblewrap-sandboxed environment and a native autoPatchelfHook variant; supports version pinning for reproducible builds."
---

Auto-updating Nix Flake for Google Antigravity (an agentic IDE/CLI); auto-updates 3x/week via GitHub Actions with hash verification and build testing; provides three components (Antigravity 2.0 Base App, IDE, and CLI 'agy'); offers an FHS bubblewrap-sandboxed environment and a native autoPatchelfHook variant; supports version pinning for reproducible builds.
