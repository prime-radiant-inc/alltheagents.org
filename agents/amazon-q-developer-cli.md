---
name: "Amazon Q Developer CLI"
slug: "amazon-q-developer-cli"
layout: "agent.njk"
category: "agent"
maker: "aws"
license: "MIT,Apache-2.0"
url: "https://github.com/aws/amazon-q-developer-cli"
source_code_url: "https://github.com/aws/amazon-q-developer-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2024-09-23"
current_release: "2026-08-17"
stars: null
language: "Rust"
homepage: "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "Amazon"
pricing: null
install_method: "brew install --cask amazon-q (macOS), DMG, AppImage (Linux)"
docs_url: "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-installing.html"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "jqueryscript"
  - "brad"
what_makes_it_special: "AWS's agentic terminal chat for building applications with natural language; succeeded by the closed-source Kiro CLI. README notes it is no longer actively maintained."
---

Amazon Q Developer CLI brought agentic coding to the terminal for AWS developers: `q chat` provided an agentic experience with MCP support, built on a Rust codebase (crates/chat-cli) and authenticated through AWS login. It ran on macOS (brew cask or DMG) and Linux (deb/AppImage), with documentation in AWS's developer guide. The project accumulated roughly 2k stars and 1,100 commits before AWS announced it would receive only critical security fixes, directing users to Kiro CLI — the closed-source successor maintained at kiro.dev/cli, with issues tracked under kirodotdev/Kiro. Existing installs keep working, but feature development now happens in the proprietary successor, making this repo the last open-source artifact of that product line.
