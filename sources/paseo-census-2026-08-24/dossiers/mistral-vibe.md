# Dossier: Mistral Vibe (census_slug: mistral-vibe)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date.

Naming note (load-bearing): since 2026-05-28 "Vibe" is Mistral's name for its whole rebranded Le Chat assistant (Vibe Work / Vibe Chat / Vibe Code) [S10][S11]. The harness Paseo drives — the thing this dossier is about — is the open-source **Vibe CLI / Vibe Code CLI** (repo mistralai/mistral-vibe, PyPI `mistral-vibe`, binary `vibe`, ACP binary `vibe-acp`). Numbers for the chat app are labeled as such and are NOT harness adoption.

## 1. Identity

- name: Mistral Vibe (CLI); repo self-description "Minimal CLI coding agent by Mistral" [S1]; docs call the surface "Vibe Code CLI" [S13]
- maker: Mistral AI (company; legal name Mistral AI SAS; HQ Paris, France) [S20] (as-of 2026-08-21)
- product URL: https://mistral.ai/products/vibe/ (whole Vibe product incl. Code); docs https://docs.mistral.ai/vibe/code/... and https://docs.mistral.ai/mistral-vibe/introduction [S12][S13]
- repo URL: https://github.com/mistralai/mistral-vibe [S1]
- license: Apache-2.0 (LICENSE in repo; GitHub API spdx apache-2.0; pyproject license text Apache-2.0) [S1][S2] (as-of 2026-08-21)
- open source? **True** — full CLI source is public under Apache-2.0; source_available: True (the CLI). The hosted parts (Le Chat/Vibe web Code Mode, remote-agent cloud sandboxes, Mistral-hosted models other than open-weight ones) are not open source [S1][S10][S16].
- first public release: repo created 2025-12-08; first GitHub release v1.0.0 published 2025-12-09; announced 2025-12-09 in the "Devstral 2 & Vibe CLI" launch post [S2][S3][S8]. (PyPI shows a placeholder 0.0.0 uploaded 2025-11-17 — name reservation before launch [S4].)
- latest release: v2.24.3, 2026-08-20 (GitHub release 2026-08-20T17:39Z; PyPI 2.24.3 2026-08-20) [S3][S4]. 81 releases / 81 PyPI versions to date; 29 releases in the last 90 days [S3][S4] (as-of 2026-08-21).
- what it is:
  - Form factors: terminal CLI (primary; interactive TUI + programmatic `--prompt` mode); ACP agent (`vibe-acp` ships in the same package) for Zed, JetBrains AI Assistant, Neovim/avante and other ACP editors; the same harness also backs Mistral's VS Code extension, Le Chat/Vibe web "Code Mode", Le Chat Desktop worktrees, and cloud "remote agents" (spawn from CLI or Le Chat; "teleport" a local session to cloud) — Mistral: CLI, VS Code extension and web Code Mode run "the same harness" [S1][S7][S10][S16] (as-of 2026-08-21).
  - Models: Mistral models by default (launch: Devstral 2 123B / Devstral Small 2 24B; since 2026-05-22 Mistral Medium 3.5 is the default model in Le Chat) [S8][S16]; BYO endpoints supported: Mistral-compatible custom domains/deployments [S1], and docs show custom third-party providers ("such as OpenRouter", custom `api_base`/`api_style`) and say it works with local models without Mistral services [S13][S14] (as-of 2026-08-21).
  - Pricing: free CLI (Apache-2.0); usage via (a) Mistral account login — included in Le Chat/Vibe plans: Free (limited coding sessions), Pro $14.99/mo ("all-day coding in the CLI, IDE, or on web"; student $5.99), Team $24.99/user/mo, Enterprise custom; pay-as-you-go credits beyond plan limits; or (b) API key — Devstral 2 $0.40/$2.00 per M tokens in/out, Devstral Small 2 $0.10/$0.30, Medium 3.5 $1.50/$7.50; Devstral was free via API during a launch promo period on the Experiment plan [S8][S9][S15][S16] (as-of 2026-08-21).
  - Install: `curl -LsSf https://mistral.ai/vibe/install.sh | bash` (script installs uv, then the PyPI package), `uv tool install mistral-vibe`, `pip install mistral-vibe`, or Homebrew formula `mistral-vibe` (homebrew-core); Python 3.12+; daily PyPI update check with in-app upgrade prompt [S1][S5][S6] (as-of 2026-08-21).
  - Default autonomy: default agent profile is **`accept-edits`** — auto-approves file edits (`write_file`, `edit`) but asks before shell and other tools; other built-ins: `ask` (approve everything), `plan` (read-only), `auto-approve` (`--yolo`); trust-folder system gates running in new directories; programmatic mode has `--max-turns` / `--max-price` / `--max-tokens` budgets [S1] (as-of 2026-08-21).
  - Language: Python (GitHub API; pyproject requires-python >=3.12) [S2][S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 4,860 | 2026-08-21 | [S2] | independently observable |
| GitHub forks | 637 | 2026-08-21 | [S2] | independently observable |
| GitHub watchers (subscribers) | 24 | 2026-08-21 | [S2] | independently observable |
| GitHub open issues+PRs (API open_issues_count) | 271; open issues via search: 105 | 2026-08-21 | [S2] | independently observable |
| GitHub issues / PRs ever (search API) | 436 issues / 402 PRs | 2026-08-21 | [S2] | independently observable |
| GitHub contributors (incl. anonymous) | 10 (top: mgesbert 37, maiengineering 14, Nemtecl 11 — Mistral-side team; low count suggests squash-merged internal development) | 2026-08-21 | [S2] | independently observable |
| Commits on main, last 90 days (since 2026-05-23) | 30 | 2026-08-21 | [S2] | independently observable |
| Releases, last 90 days | 29 (roughly weekly-or-faster; 3 in Aug 2026) | 2026-08-21 | [S3] | independently observable |
| PyPI downloads `mistral-vibe`, last 30 days (2026-07-23..08-21, mirrors excluded) | 12,693,255 | 2026-08-21 | [S5] | independently observable (caveat: includes installer-script and `uv tool` CI/automated installs; recent days run ~260k-640k/day) |
| PyPI downloads, prior 30 days | 4,037,931 (≈3.1x growth month-over-month) | 2026-08-21 | [S5] | independently observable |
| PyPI downloads, last 7 days (2026-08-15..21) | 2,989,206 | 2026-08-21 | [S5] | independently observable |
| PyPI downloads, pypistats 180-day window (2026-02-22..08-21) | 32,171,170 (window-limited, not lifetime) | 2026-08-21 | [S5] | independently observable |
| Homebrew formula installs, 30d / 90d / 365d | 1,519 / 5,177 / 12,072 | 2026-08-21 | [S6] | independently observable |
| VS Code Marketplace, "Mistral Vibe VS Code" (mistralai.mistral-vibe-code) | 27,447 installs; 16 ratings avg 4.44; released 2026-05-27, v1.17.24 updated 2026-08-21 | 2026-08-21 | [S17] | independently observable |
| JetBrains standalone plugin | none — Vibe reaches JetBrains via the JetBrains AI Assistant agents catalog (no public download count); Mistral's separate "Mistral Code Enterprise" plugin (a different product) has 14,656 downloads | 2026-08-21 | [S7][S17] | independently observable |
| Zed | listed in Zed's ACP agent gallery as "The terminal-native coding agent by Mistral"; Zed tracks weekly Vibe sessions but publishes no count | 2026-08-21 | [S18] | independently observable listing; no numbers |
| Paseo | shipped in Paseo's ACP provider catalog (`vibe-acp`, catalog pin v2.9.3) | 2026-08-21 | [S19] | independently observable |
| Discord | Mistral community server ≈38,894 members (whole company community, not Vibe-specific) | 2026-08-21 | [S21] | independently observable |
| GitHub Discussions | enabled on repo (has_discussions: true); volume not counted | 2026-08-21 | [S2] | independently observable |
| Maker usage numbers for the CLI (users, sessions, tokens) | none published — researched and absent | 2026-08-21 | [S8][S10][S16] | none |
| Chat-app numbers (NOT the CLI): Le Chat 1M mobile downloads in 14 days | Feb 2025 (pre-rebrand) | 2025-02 | [S22] | maker-claimed via press |
| Chat-app numbers (NOT the CLI): "~5M users" for Vibe | aggregator estimate, no Mistral source found | 2026-08-21 | [S22] | unverified third-party |
| Benchmarks (models, maker-run): Devstral 2 72.2% SWE-bench Verified; Devstral Small 2 68.0%; Medium 3.5 77.6% | launch posts | 2025-12-09 / 2026-05-22 | [S8][S16] | maker-claimed (model, not harness) |
| Cost claim | Devstral 2 "7x more cost-efficient" than Claude Sonnet on real-world tasks | 2025-12-09 | [S8] | maker-claimed |
| Ecosystem quote | Kilo Code: 17B tokens through Devstral 2 in first 24h; Cline praised tool-calling success rate (both about the model, not Vibe) | 2025-12-09 | [S8] | maker-claimed (partner quotes) |
| Public customers (Vibe product page logos; product-wide, not CLI-specific) | ASML, BNP Paribas, Luxembourg Government, CMA CGM, Abanca, Stellantis, La Banque Postale, SNCF | 2026-08-21 | [S12] | maker-claimed |
| Company funding | Series C €1.7B at €11.7B post-money, led by ASML (2025-09); March 2026 $830M debt for datacenters; June 2026 Bloomberg/TechCrunch: talks to raise ≈€3B at ≈€20B; July 2026 FT: Samsung in advanced talks for up to €1B — 2026 round not confirmed closed | 2026-08-21 | [S20][S23] | press / maker (Series C) |
| Press | Devstral 2 + Vibe CLI launch and the May 2026 Le Chat→Vibe rebrand covered by TechCrunch, TechRadar (review), MarkTechPost, winbuzzer, Futurum; no press-reported CLI usage numbers found | 2026-08-21 | [S16b][S22] | press |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — `mcp_servers` config in config.toml; transports stdio, http, streamable-http; static-auth headers/API-key-env or OAuth (`/mcp add`, `vibe mcp add` CLI); per-tool permissions on MCP tools (`{server}_{tool}`); startup/tool timeouts. No MCP-server mode found (researched, absent). Evidence: README "MCP Server Configuration" [S1]; https://docs.mistral.ai/vibe/code/cli/mcp-servers [S14] (as-of 2026-08-21)
- plugin_support: **True (skills, no marketplace)** — Skills system following the cross-vendor Agent Skills specification (agentskills.io): SKILL.md dirs discovered from `.agents/skills/`, `.vibe/skills/`, `~/.vibe/skills/`, `~/.agents/skills/`, plus `skill_paths`; skills can add tools, slash commands (`user-invocable: true`), behaviors; enable/disable by glob/regex. Also custom agents (TOML), custom system/compaction prompts, custom tools (deprecated in favor of skills). No plugin marketplace (researched, absent). Evidence: README "Skills System" [S1]; https://docs.mistral.ai/vibe/code/cli/skills [S14]
- claude_code_plugin: **partial** — speaks the same Agent Skills SKILL.md standard Claude Code skills use and reads the standard `.agents/skills/` path, so individual skills port; but it does not read `.claude/` dirs, CLAUDE.md (uses AGENTS.md), or the Claude Code plugin/marketplace format (`.claude-plugin/plugin.json`) — researched, absent [S1][S14] (as-of 2026-08-21)
- subagents: **True** — `task` tool delegates to subagents running independently; built-in read-only `explore` subagent; custom subagents via `agent_type = "subagent"` in agent TOML; subagents inherit parent hook config; custom-subagent support headlined in Vibe 2.0 [S1][S9]. Evidence: README "Subagents and Task Delegation"
- hooks: **True** — `hooks.toml` (project `.vibe/hooks.toml` + user `~/.vibe/hooks.toml`); events `pre_tool` (deny or rewrite tool args), `post_tool` (deny/replace or append to tool output), `post_agent` (deny → retry, max 3/turn); JSON-over-stdin contract, exit-code + stdout JSON responses, `strict` mode, timeouts [S1][S14]. Evidence: README "Hooks"; https://docs.mistral.ai/vibe/code/cli/hooks
- plan_mode: **True** — built-in `plan` agent: "Read-only agent for exploration and planning", auto-approves safe tools (grep, read); `vibe --agent plan`, Shift+Tab cycles agents [S1]. Evidence: README "Built-in Agents"
- plugin_docs_url: https://docs.mistral.ai/vibe/code/cli/skills (skills); hooks: https://docs.mistral.ai/vibe/code/cli/hooks
- config_docs_url: https://docs.mistral.ai/vibe/code/cli/configuration (also safety/permissions: https://docs.mistral.ai/vibe/code/safety-approvals-permissions)
- ACP support: **yes, first-party** — `vibe-acp` binary ships in the package (dependency `agent-client-protocol==0.11.0`); official setup docs for Zed (also a hosted Zed ACP agent entry), JetBrains AI Assistant (agents catalog install), Neovim/avante [S1][S7][S2]. This is what Paseo launches [S19].
- SDK: **none found** (researched, absent) — no separate SDK package; scripting is via programmatic mode: `vibe --prompt` with `--output text|json|streaming`, `--max-turns/--max-price/--max-tokens`, tool allow/deny lists [S1].
- Also: OpenTelemetry tracing (OTLP/HTTP, client-side redaction); GrowthBook server-managed feature rollout (managed shell tools); admin config fetch (enterprise-managed settings) noted in changelog; git worktree integration (`--worktree`, shared semantics with Le Chat Desktop); voice mode (experimental); image attachments to vision models [S1][S3].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README, verbatim-short): "Mistral's open-source CLI coding assistant." — https://github.com/mistralai/mistral-vibe [S1]
- repo description: "Minimal CLI coding agent by Mistral" [S2]
- Vibe 2.0 post headline: "Terminally online Mistral Vibe" [S9]; Vibe product page: "Work. Vibe." / agent for "long-horizon tasks" [S12]
- maker claims (paraphrased):
  1. Open source (Apache-2.0) CLI harness paired with open-weight coding models (Devstral 2 modified-MIT 123B, Devstral Small 2 Apache-2.0 24B, Medium 3.5 open weights) — the openness-and-ownership pitch, "intelligence you own, not rent" (product page, data-residency framing) [S1][S8][S12].
  2. Cost efficiency: Devstral 2 claimed "7x more cost-efficient" than Claude Sonnet at real-world tasks; competitive SWE-bench with 5-28x fewer parameters than DeepSeek V3.2 / Kimi K2 [S8].
  3. Local/self-hosted capability: Devstral Small 2 runs on consumer GPUs or CPU-only; docs say the CLI works with local models without Mistral services; Medium 3.5 self-hostable on 4 GPUs [S8][S13][S16].
  4. One harness, many surfaces: same harness behind CLI, VS Code extension, and web Code Mode; remote agents run sessions in cloud sandboxes and "teleport" preserves history and approval state between local and cloud [S10][S16].
  5. Agentic feature set: custom subagents, multi-choice clarifications before execution ("clarify before you execute"), slash-command skills, unified agent modes (tools+permissions), auto-updates (Vibe 2.0 headline features) [S9].
  6. Editor-neutral via ACP: works in Zed, JetBrains, Neovim and any ACP client instead of shipping its own IDE [S1][S7].
  7. Safety/controls: trust-folder system, tool-approval permissions, budgets (`--max-price`/`--max-tokens`/`--max-turns`), hooks for gating/audit, OTel tracing with redaction [S1].
  8. Included in cheap plans: Pro $14.99/mo buys "all-day coding in the CLI, IDE, or on web"; free tier has limited coding sessions; BYO API key allowed [S15][S9].
- audience: developers (pyproject classifiers "Intended Audience :: Developers"); Vibe 2.0: full-time developers and teams, students (50% Pro discount); product page: developers, teams, enterprises (esp. European/data-residency-sensitive) [S1][S9][S12].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Mistral AI SAS; HQ Paris, France [S20]
- size: 1,000+ employees (Wikipedia, 2026); company founded 2023-04-28 [S20]
- funding stage: late private; Series C €1.7B at €11.7B post (2025-09, ASML lead ~11%); 2026 raise at ≈€20B reported in talks (Bloomberg 2026-06-12; FT on Samsung 2026-07-22), not confirmed closed [S20][S23]
- publicly named leadership (as named on mistral.ai/about and Mistral posts):
  - Arthur Mensch — Co-founder & CEO [S24]
  - Guillaume Lample — Co-founder & Chief Science Officer (Wikipedia: Chief Scientist) [S24][S20]
  - Timothée Lacroix — Co-founder & CTO [S24]
  - Vibe/Devstral launch posts are bylined "Mistral AI" with no individual product-lead names [S8][S9][S10]; no head of product / DevRel / partnerships lead named on mistral.ai pages consulted — researched on those pages, absent (about page lists only the three founders) [S24].
- contact: enterprise/partnership contact via mistral.ai site contact flows (Enterprise plan "contact us") [S12][S15]

## 6. Open questions / conflicts

- Census `stars: null` — GitHub shows 4,860 stars, 637 forks (2026-08-21) [S2].
- Census `current_release: "2026-08-18"` — that matches v2.24.2; latest is v2.24.3, 2026-08-20 [S3].
- Census `first_released: "2025-12-08"` — that is repo creation; first release v1.0.0 and launch post are 2025-12-09 [S2][S3][S8]. Minor.
- Census `homepage: null` / `pricing: null` / `plugin_docs_url: null` / `config_docs_url: null` — all fillable (see sections 1, 3): product page mistral.ai/products/vibe, docs.mistral.ai/vibe/code/..., plans Free/Pro $14.99/Team $24.99/Enterprise + API per-token [S12][S15].
- Census `model_providers: "Mistral (default); Mistral-compatible domains/deployments"` — understated: docs explicitly support third-party providers (OpenRouter example, custom api_base/api_style) and local models with no Mistral services [S13][S14].
- Census `claude_code_plugin: null` — verdict from research: **partial** (shares the Agent Skills SKILL.md standard and `.agents/skills/` path; no `.claude/` dirs, no CLAUDE.md — AGENTS.md instead, no Claude Code plugin/marketplace format) [S1][S14].
- Census `docs_url` points at repo `docs/` — official docs now live at docs.mistral.ai (vibe/code section); repo docs/ still holds acp-setup.md [S13][S7].
- Census `platforms: ["CLI"]` — defensible for the harness, but the same harness officially ships as a VS Code extension, web Code Mode, and cloud remote agents, plus ACP editors [S10][S16].
- Name collision risk for the directory: "Mistral Vibe" is also the renamed Le Chat consumer assistant (Wikipedia's "Mistral Vibe" article is about the chatbot, initial release Feb 2024); adoption figures circulating for "Vibe" (e.g. "~5M users") are chat-app numbers, not CLI numbers [S22][S10].
- PyPI download quality: ~12.7M/30d is unusually high for a 4,860-star tool; the official installer and `uv tool` reinstalls/updates, CI, and possibly Le Chat Desktop bundling inflate raw counts; day-to-day swings (258k-637k) look automated. Treat as directionally strong (3.1x MoM growth) but not "12.7M developers" [S5].
- pypistats "overall" only covers a rolling ~180-day window (from 2026-02-22) — lifetime downloads since 2025-12 are higher than 32.2M but not retrievable from that endpoint [S5].
- No maker-published usage numbers exist for the CLI itself (sessions, users, tokens) as of 2026-08-21 — the strongest observable signals are PyPI velocity, the VS Code extension count, and first-party placement in Zed/JetBrains/Paseo catalogs.
- 2026 funding round (≈€20B valuation, Samsung participation) reported by Bloomberg/FT as talks; no Mistral confirmation found by 2026-08-21 [S23].
- Devstral 2 "modified MIT" license and benchmark figures are maker-claimed from the launch post; not independently re-verified here [S8].

## 7. Sources

1. [S1] https://github.com/mistralai/mistral-vibe (README via raw.githubusercontent.com) — features, agents, skills, hooks, MCP, install, license
2. [S2] https://api.github.com/repos/mistralai/mistral-vibe (+ contributors, search/issues, commits) — stars/forks/dates/counts
3. [S3] https://api.github.com/repos/mistralai/mistral-vibe/releases — 81 releases, v1.0.0 2025-12-09, v2.24.3 2026-08-20
4. [S4] https://pypi.org/pypi/mistral-vibe/json — versions, upload dates, project URLs
5. [S5] https://pypistats.org/api/packages/mistral-vibe/overall — daily downloads, 30d/7d windows
6. [S6] https://formulae.brew.sh/api/formula/mistral-vibe.json — Homebrew installs, license
7. [S7] https://github.com/mistralai/mistral-vibe/blob/main/docs/acp-setup.md — vibe-acp, Zed/JetBrains/Neovim setup
8. [S8] https://mistral.ai/news/devstral-2-vibe-cli — 2025-12-09 launch, Devstral 2 benchmarks/pricing, cost claims, partner quotes
9. [S9] https://mistral.ai/news/mistral-vibe-2-0/ — 2026-01-27 Vibe 2.0 features, plans, student discount
10. [S10] https://mistral.ai/news/vibe-agent/ — 2026-05-28 Le Chat→Vibe rebrand, Work/Code modes, VS Code extension, "same harness"
11. [S11] https://help.mistral.ai/en/articles/682992-le-chat-is-now-vibe — rebrand mechanics, Vibe Work/Code/Chat
12. [S12] https://mistral.ai/products/vibe/ — product page, taglines, surfaces, customer logos, MCP/fine-tuning claims
13. [S13] https://docs.mistral.ai/mistral-vibe/introduction — install, auth (account login vs API key), local models
14. [S14] https://docs.mistral.ai/vibe/code/cli/configuration — config keys, third-party providers (OpenRouter), sub-page URLs (skills, hooks, mcp-servers, agents)
15. [S15] https://mistral.ai/pricing — Free/Pro $14.99/Team $24.99/Enterprise, student $5.99, "all-day coding", API credits
16. [S16] https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5 — 2026-05-22 remote agents, teleport, Medium 3.5 77.6% SWE-bench, $1.5/$7.5 pricing; [S16b] https://www.marktechpost.com/2026/05/02/mistral-ai-launches-remote-agents-in-vibe-and-mistral-medium-3-5-with-77-6-swe-bench-verified-score/ — press recap
17. [S17] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery — mistralai.mistral-vibe-code installs/ratings; https://plugins.jetbrains.com/api/searchPlugins — no standalone Vibe plugin
18. [S18] https://zed.dev/acp/agent/mistral-vibe — Zed ACP agent gallery entry
19. [S19] https://raw.githubusercontent.com/getpaseo/paseo/main/packages/app/src/data/acp-provider-catalog.ts — Paseo catalog entry (vibe-acp)
20. [S20] https://en.wikipedia.org/wiki/Mistral_AI — legal name, HQ, founders, employees, funding history
21. [S21] https://discord.com/api/v9/invites/mistralai?with_counts=true — Mistral Discord ≈38.9k members
22. [S22] web search results (theairankings.com/mistral, getpanto, techradar review, en.wikipedia.org/wiki/Mistral_Vibe) — chat-app numbers (1M downloads/14 days Feb 2025; "~5M users" unverified), rebrand coverage
23. [S23] https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/ ; Bloomberg 2026-06-12; FT via search (Samsung, 2026-07-22) — 2026 funding talks
24. [S24] https://mistral.ai/about/ — founders' names/titles, mission
25. https://mistral.ai/vibe/install.sh — installer mechanics (uv + PyPI, checksum-verified)

## Inclusion check (Jesse's test)

**Yes** — Mistral Vibe is a first-party harness with its own agentic loop: it plans, reads/writes/patches files, runs shell commands, greps, manages todos, asks the user questions, and delegates to subagents, driven by Mistral (or user-configured) models; `vibe-acp` is its own ACP surface, not a wrapper around someone else's agent [S1].
