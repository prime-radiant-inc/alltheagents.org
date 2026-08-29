---
name: "tartarusai-cli"
slug: "tartarusai-cli"
layout: "agent.njk"
category: "agent"
maker: "Tartarus-AI"
license: "MIT"
url: "https://github.com/Tartarus-AI/tartarusai-cli"
source_code_url: "https://github.com/Tartarus-AI/tartarusai-cli"
source_available: "False"
platforms:
  - "CLI"
first_released: "2026-05-20"
current_release: "2026-06-22"
stars: "100"
language: null
homepage: "https://tartarusai.dev"
mcp_support: null
plugin_support: null
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "TartarusAI (proprietary uncensored model)"
pricing: "Crypto-only billing, no card on file, no recurring charge; 14-day refund. Specific prices not listed"
install_method: "curl -sSf https://dash.tartarusai.dev/tartarus-setup.sh | bash (macOS/Linux); PowerShell zip download (Windows); or binaries from GitHub Releases"
docs_url: "https://dash.tartarusai.dev/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Tartarus-AI/tartarusai-cli/releases/latest"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Uncensored-no policy filter between you and your code. Does work mainstream agents refuse (pentest PoCs for patched CVEs, deobfuscation, credential rotation tools). 256K context, crypto-only billing, no card on file, ~30s activation. Explicitly not a malware factory, piracy tool, or politics bot. Binary distribution only (no source in repo)."
---

tartarusai-cli is the terminal client for a hosted coding-agent service that competes on policy: it advertises itself as an uncensored agent that will handle work mainstream tools decline, such as writing proof-of-concept exploits for already-patched CVEs, deobfuscating samples, and building credential-rotation tooling in lab environments. The client is a MIT-licensed OpenCode fork shipped as a static binary with a setup script for macOS/Linux and a Windows zip; it connects only to TartarusAI's own hosted backend using an account API token, with no BYOK support, and billing is cryptocurrency-only with a 14-day refund window. The project states explicit boundaries — no malware development, no DRM circumvention, no attacking systems you do not own — and runs 256K-context sessions over whole repositories. Security researchers and CTF players who keep hitting refusal walls elsewhere are the intended users.
