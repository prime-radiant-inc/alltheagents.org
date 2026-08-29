---
name: "Aikido Autofix"
slug: "aikido-autofix"
layout: "agent.njk"
category: "agent"
maker: "Aikido Security"
license: "Proprietary"
url: "https://www.aikido.dev"
source_code_url: null
source_available: "No"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: "https://www.aikido.dev"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "freemium"
install_method: null
docs_url: "https://help.aikido.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI autofix PRs for vulnerabilities (Belgium)"
---

Aikido is a Belgian application security platform whose AutoFix feature converts scanner findings into pull requests instead of tickets. For dependency CVEs it groups fixes by repo and lockfile; for SAST findings it previews a full diff that can be applied from the IDE or inline in a PR; for containers it generates three to five Dockerfile patch options across base images, stating what each fixes and risks. Developers refine patches conversationally (different error handling, an added test) before merging, with custom branch names and merge rules. Aikido holds read-only repository access and never pushes directly — one customer reports roughly 200 AutoFixes per month against their backlog. Proprietary SaaS with a free tier and docs at help.aikido.dev.
