---
name: "demo2apk"
slug: "demo2apk"
layout: "agent.njk"
category: "other"
maker: "DeadWaveWave"
license: "MIT"
url: "https://github.com/DeadWaveWave/demo2apk"
source_code_url: "https://github.com/DeadWaveWave/demo2apk"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-11-27"
current_release: "2026-03-20"
stars: "628"
language: "TypeScript"
homepage: "https://demo2apk.lasuo.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "docker"
docs_url: "https://github.com/DeadWaveWave/demo2apk/blob/main/docs/API.md"
plugin_docs_url: null
config_docs_url: "https://github.com/DeadWaveWave/demo2apk/blob/main/DEPLOYMENT.md"
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "One-click tool that converts AI-generated code (Vibe Coding) into installable Android APKs with no Android dev environment setup required; supports HTML, React, ZIP projects with smart detection and offline support"
---

Vibe-coding tools produce HTML and React demos that die in the browser; demo2apk exists to turn them into things users can actually install on a phone. Uploads are classified into single-file, pasted-code, or ZIP project types, then routed through an appropriate build strategy — raw HTML wraps directly, React/Vite projects run an npm build — with automatic handling of CDN resources and JSX compilation so apps keep working offline in Android WebView. The service queues concurrent builds, generates shareable download links, and purges artifacts after two hours. It serves hobbyists and hackathon participants who want an APK from an LLM chat without installing Android Studio.
