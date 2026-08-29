---
name: "antigravity-nix"
slug: "antigravity-nix"
layout: "agent.njk"
category: "other"
maker: "jacopone"
license: "MIT"
url: "https://github.com/jacopone/antigravity-nix"
source_code_url: "https://github.com/jacopone/antigravity-nix"
source_available: "True"
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
pricing: "free"
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

Google ships Antigravity as proprietary binaries that assume standard FHS filesystems, which NixOS lacks; this flake wraps them in an FHS environment with bubblewrap (plus a no-fhs variant using autoPatchelfHook) and exposes three packages: the Antigravity 2.0 base app, the legacy IDE, and the agy CLI. An automated workflow checks upstream daily at 0700 UTC, verifies hashes, tests the build, and publishes tagged pins like v2.0.3-6242596486512640, so users get reproducible versions or automatic tracking. Linux x86_64/aarch64 builds are CI-verified; macOS packages exist but are untested. MIT-licensed packaging of unfree software (allowUnfree required), unofficial and unaffiliated with Google, with 160 stars and active CI.
