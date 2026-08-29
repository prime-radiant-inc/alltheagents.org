---
name: "WebCode"
slug: "webcode"
layout: "agent.njk"
category: "multiplexer"
maker: "shuyu-labs"
license: "AGPL-3.0"
url: "https://github.com/shuyu-labs/WebCode"
source_code_url: "https://github.com/shuyu-labs/WebCode"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-01-14"
current_release: "2026-06-20"
stars: "284"
language: "C#"
homepage: "https://wc.tree456.com/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Claude Code, Codex, OpenCode (via cc-switch)"
pricing: "open-source"
install_method: "docker compose up -d; or dotnet run --project WebCodeCli; or Windows installer from GitHub Releases"
docs_url: "https://github.com/shuyu-labs/WebCode/blob/main/QUICKSTART.md"
plugin_docs_url: null
config_docs_url: "https://github.com/shuyu-labs/WebCode/blob/main/docs/CLI%E5%B7%A5%E5%85%B7%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E.md"
download_url: "https://github.com/lusile2024/WebCode/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Browser-based AI CLI work platform that wraps Claude Code, Codex, and OpenCode into a manageable, deployable, collaborative, remotely-accessible system with Web, mobile, and Feishu (Lark) unified session flow. Supports multi-user, permissions, external session import/recovery, Superpowers workflows, Codex /goal, and cc-switch as the sole provider authority."
---

WebCode addresses the operational problem of running AI coding CLIs for a team or across machines: sessions are tied to local terminals and hard to share, secure, or reach remotely. It wraps Claude Code, Codex, and OpenCode into a self-hostable Blazor Server (.NET 10) platform where sessions can be created, restored from raw CLI transcripts, bound to workspaces, and accessed from web, mobile, or Feishu (Lark) chats with streaming card output. Multi-user support includes per-user CLI restrictions, directory whitelists, and Feishu bot bindings, with provider switching centralized through cc-switch. An office-assistant mode extends the same session infrastructure to planning, summaries, and document drafting. It is self-hosted via Docker or Windows installers under AGPLv3, aimed at teams wanting shared, remotely accessible agent sessions.
