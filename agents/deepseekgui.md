---
name: "DeepSeekGUI"
slug: "deepseekgui"
layout: "agent.njk"
category: "multiplexer"
maker: "See-Sol-Lab"
license: "PolyForm-Perimeter-1.0.1"
url: "https://github.com/See-Sol-Lab/DeepSeekGUI"
source_code_url: "https://github.com/See-Sol-Lab/DeepSeekGUI"
source_available: "True"
homepage: "https://www.ailover-atlas.com/deepseekgui/"
docs_url: "https://github.com/See-Sol-Lab/DeepSeekGUI/blob/main/README.en.md"
download_url: "https://github.com/See-Sol-Lab/DeepSeekGUI/releases"
install_method: "Download DeepSeekGUI-Setup-1.2.1.exe from the GitHub releases (Windows 10/11 x64, bundles its runtime, unsigned — verify SHA256 and bypass SmartScreen), or the experimental Linux AppImage (v1.2.1-linux.1); from source with pnpm install && pnpm run build && pnpm run dev:deepseekgui"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: "TypeScript"
first_released: "2026-08-17"
current_release: "2026-10-18"
maintained: "renamed"
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "DeepSeek account sign-in or DeepSeek-compatible API key; custom model providers configurable (upstream DeepSeek Harness owns the model connection)"
pricing: "free"
stars: "281"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A Windows desktop workbench that wraps DeepSeek's official open-source coding agent (DeepSeek Harness) with project workspaces, a built-in browser and terminal, Changes/Git/worktree views with commit-push-PR tools, and two-layer global/project memory — with the twist that, once DeepSeek shipped its own desktop app, v1.3.x releases became a migration assistant that moves users onto the official desktop plus the maker's DSH QoL plugin."
---

DeepSeekGUI is a third-party local workbench for DeepSeek's coding agent: the upstream DeepSeek Harness (MIT, from deepseek-ai) runs the agent loop — reading code, editing files, running commands, browsing — while this Electron/TypeScript shell adds the desktop experience around it. You sign in with a DeepSeek account or paste a compatible API key, pick a project folder, and work in sessions where a Changes view groups staged, modified, new, and conflicting files, a Git view shows branches, remotes, and this session's commits and PRs, and dedicated Git/PR tools let you request diffs, stage, discard, commit, preview pushes, push, and open PRs from the conversation with result cards. Two memory layers persist collaboration: user-edited global memory in settings and project memory the assistant maintains as a .memory.md file, both recorded into the session context. The app bundles its runtime, manages Harness Homes and profiles, supports compatible plugins, ships Chinese and English interfaces, and keeps credentials, sessions, and memory in a local data directory. In October 2026 the solo maintainer (See-Sol-Lab, Goumang) changed course: DeepSeek's official desktop client had diverged too far to keep re-merging, so v1.3.0 and v1.3.1 are the last whole-app updates and now act as a migration assistant that installs the official desktop, merges DeepSeekGUI sessions, keys, workspaces, and memory into it, and adds DSH-QoL, a plugin reimplementing DeepSeekGUI's views and memory in the official client. Existing installs keep working; the project suits Chinese-speaking Windows developers who wanted a stable DeepSeek Harness desktop before the official one existed.
