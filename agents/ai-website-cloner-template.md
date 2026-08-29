---
name: "ai-website-cloner-template"
slug: "ai-website-cloner-template"
layout: "agent.njk"
category: "other"
maker: "JCodesMore"
license: "MIT"
url: "https://github.com/JCodesMore/ai-website-cloner-template"
source_code_url: "https://github.com/JCodesMore/ai-website-cloner-template"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2026-03-13"
current_release: "2026-08-14"
stars: "32477"
language: "TypeScript"
homepage: "https://dsc.gg/jcodesmore"
mcp_support: null
plugin_support: "yes (AI agent skills system)"
claude_code_plugin: "yes (.claude/skills directory; Claude Code recommended platform)"
subagents: "yes"
hooks: null
plan_mode: null
model_providers: "Claude Code (Opus 5), Codex CLI, Gemini CLI, Cursor, Windsurf, Cline, Roo Code, GitHub Copilot, Kiro, OpenCode, Continue, Amazon Q, Augment Code"
pricing: "open-source"
install_method: "git clone (GitHub template), npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/JCodesMore/ai-website-cloner-template/generate"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Clones any website with a single command (/clone-website <url>) using AI coding agents, producing a clean Next.js codebase via a multi-phase pipeline (Reconnaissance -> Foundation -> Component Specs -> Parallel Build -> Assembly & QA) that dispatches parallel builder agents in git worktrees."
---

Users generate a repo from the template, run npm install, and invoke /clone-website <url> inside their preferred agent (Claude Code with Chrome, Codex, Cursor, Gemini CLI, and ten others via synced .claude/.codex/.cursor/ rule directories). The pipeline screenshots and probes the target, extracts fonts, colors, and computed styles into spec files, dispatches builder agents into per-section git worktrees, then merges and visually diffs the result against the original. The stack is Next.js 16, React 19, TypeScript strict mode, and Tailwind v4, with Docker support. It is MIT-licensed, sponsored, and explicitly prohibits phishing and impersonation use.
