---
name: "opencode-android"
slug: "opencode-android"
layout: "agent.njk"
category: "other"
maker: "mulkymalikuldhrs"
license: "MIT"
url: "https://github.com/mulkymalikuldhrs/opencode-android"
source_code_url: "https://github.com/mulkymalikuldhrs/opencode-android"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-01-31"
current_release: "2026-06-11"
stars: "27"
language: "Kotlin"
homepage: "https://github.com/mulkymalikuldhrs"
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "none on-device — 75+ providers configured on the OpenCode server; the app only displays/switches server-exposed providers"
pricing: "Free / open-source"
install_method: "Download APK from GitHub Releases, or build from source via Gradle (./gradlew assembleDebug / installDebug)"
docs_url: "https://github.com/mulkymalikuldhrs/opencode-android#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/mulkymalikuldhrs/opencode-android/blob/main/ARCHITECTURE.md"
download_url: "https://github.com/mulkymalikuldhrs/opencode-android/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Native Android client for the OpenCode AI coding agent — combines SSE streaming AI chat, remote terminal (WebSocket), code editor with syntax highlighting, and file manager in a Material Design 3 dark theme. Thin-client architecture where all heavy lifting runs on the OpenCode server."
---

The OpenCode agent lives in a desktop terminal, which leaves its sessions unreachable from a phone. This Kotlin app (Jetpack Compose, Material Design 3, MVVM) connects to a running OpenCode server and mirrors it on Android: SSE-streaming AI chat, a WebSocket terminal that executes on the server machine, a code editor with syntax highlighting, and a file manager, all in a dark Material 3 interface. The README is explicit about the architecture's limits — nothing works offline, the phone manages no API keys, terminal commands execute on the server host, and security hardening (certificate pinning, encrypted preferences) is only partially implemented. APKs ship via GitHub Releases for Android 7.0+, and a Termux guide documents running the server on-device. It is a small early-stage project (27 stars, 70 commits) marked for education and research use. Developers running OpenCode who want to monitor and steer sessions from Android are the audience.
