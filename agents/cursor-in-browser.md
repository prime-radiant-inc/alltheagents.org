---
name: "cursor-in-browser"
slug: "cursor-in-browser"
layout: "agent.njk"
category: "other"
maker: "Arfo-du-blo"
license: "MIT"
url: "https://github.com/Arfo-du-blo/cursor-in-browser"
source_code_url: "https://github.com/Arfo-du-blo/cursor-in-browser"
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: "2025-07-03"
current_release: "2026-05-16"
stars: "65"
language: "Dockerfile"
homepage: "https://github.com/Arfo-du-blo/cursor-in-browser"
mcp_support: null
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Docker (via Docker Hub or ghcr.io)"
docs_url: "https://hub.docker.com/r/arfodublo/cursor-in-browser"
plugin_docs_url: null
config_docs_url: null
download_url: "https://hub.docker.com/r/arfodublo/cursor-in-browser"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Deploys and runs Cursor AI Code Editor directly in a web browser using Docker/KasmVNC; tracks Cursor releases for x64 and arm64"
---

cursor-in-browser is a containerization project that runs the Cursor AI code editor inside a Docker image and streams its UI to a browser via KasmVNC, modeled on LinuxServer-style remote-desktop images. The image exposes the editor with basic-auth protection and persistent volumes for configuration and Cursor data, and its build scripts pull current Cursor releases for both x64 and arm64, with tags tracking versions from 0.47.7 onward and a 'latest' tag following new releases. All AI functionality remains Cursor's own; the repo contributes only the packaging. It serves developers who want Cursor on Chromebooks, tablets, or locked-down machines where local installation is impractical, and it remains actively maintained with images on Docker Hub and ghcr.io.
