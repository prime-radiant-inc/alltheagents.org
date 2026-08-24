# Dossier: Hermes Agent (census_slug: hermes-agent — NEW ENTRY, not yet in census)

Compiled 2026-08-24 (task dated 2026-08-21; live API numbers fetched 2026-08-24). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (section 7) and an as-of date.

## 1. Identity

- name: Hermes Agent
- maker: Nous Research (company; self-described "leader in the American open source AI movement"; also makes the Hermes model family, Nous Portal, Nous Chat) [S10][S11]. HQ not stated on company site (researched, absent on nousresearch.com) [S11]. Founded 2023 [S12].
- product URL: https://hermes-agent.nousresearch.com (docs at /docs) [S2]
- repo URL: https://github.com/NousResearch/hermes-agent [S1][S3]
- license: MIT (GitHub API license field; README badge; PyPI license_expression MIT) [S3][S1][S5] (as-of 2026-08-24)
- open source? True. source_available: True — full agent source in the repo (Python 73.7MB + TypeScript 20.7MB per languages API); docs site source in-repo (`website/docs/`) [S3][S16].
- first public release: earliest GitHub release tag v2026.3.12 ("Hermes Agent v0.2.0"), published 2026-03-12 [S4]. Repo created 2025-07-22 [S3]. Third-party wikis claim a public launch on 2026-02-25 — no first-party source found; treat as unverified [S15]. First PyPI upload 0.13.0 on 2026-05-14 [S5]; first npm publish 0.14.0 on 2026-05-25 [S6].
- latest release: v2026.8.19 = "Hermes Agent v0.20.5", published 2026-08-21 (GitHub release; npm 0.20.5 same day; PyPI lags at 0.19.0, 2026-07-20) [S4][S6][S5]. 29 tagged GitHub releases since 2026-03-12 [S4].
- what it is:
  - Form factors: terminal CLI/TUI (primary); messaging gateway (Telegram, Discord, Slack, WhatsApp, Signal, Email — "20+ messaging platforms" maker-claimed); Hermes Desktop app for macOS/Windows/Linux (public preview 2026-06-02); ACP server for IDEs (VS Code, Zed, JetBrains — this is how Paseo drives it, via `hermes acp`); OpenAI-compatible API server; voice mode with wake word; cron-scheduled background automations; "Bot Mode" multi-profile roster (v0.20.3, 2026-08) [S1][S2][S8][S13][S14][S16].
  - Models: BYO / model-agnostic — Nous Portal, OpenRouter, OpenAI, "your own endpoint"; switch with `hermes model`, "no lock-in" (maker wording) [S1][S2].
  - Pricing: agent itself free (MIT). Optional Nous Portal subscription (Plus / Super / Ultra tiers; TechCrunch reports cloud tiers "$20–$200 monthly") bundles 300+ models plus a Tool Gateway (search, image gen, TTS, cloud browser) [S1][S10][S12].
  - Install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash` (Linux/macOS/WSL2/Termux); PowerShell `iex (irm .../install.ps1)` (native Windows); desktop DMG/EXE installers; `brew install hermes-agent` (homebrew/core formula); `pip install hermes-agent`; Docker image nousresearch/hermes-agent; npm package hermes-agent exists (see section 6 re: maintainer) [S1][S7][S5][S6][S9][S10].
  - Default autonomy: `approvals.mode: "smart"` by default — an auxiliary LLM risk-assesses shell commands (low-risk auto-approve, dangerous auto-deny, uncertain → user prompt); `manual` and `off` (`--yolo`) modes; permanent hardline blocklist (`rm -rf /`, fork bombs, `dd` to devices); file-write denylist for SSH keys/.env/credentials; hardened Docker backend; DM-pairing authorization for messaging [S17]. File edits are not individually approval-gated by default (write violations error rather than prompt) [S17].
  - Repo language: Python (TypeScript secondary — desktop/website) [S3][S16].
  - Lineage note: README ships `hermes claw migrate` — "Migrate from OpenClaw", i.e. an official migration path from OpenClaw [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 235,605 | 2026-08-24 | [S3] | independently observable |
| GitHub forks | 47,524 | 2026-08-24 | [S3] | independently observable |
| GitHub watchers (subscribers) | 915 | 2026-08-24 | [S3] | independently observable |
| GitHub open issues | 35,282 | 2026-08-24 | [S3] | independently observable |
| GitHub contributors (incl. anonymous) | 3,029 | 2026-08-24 | [S3] | independently observable |
| Commits, last 90 days (since 2026-05-26) | 15,524 | 2026-08-24 | [S3] | independently observable |
| Release cadence | 29 GitHub releases in ~5 months (2026-03-12 → 2026-08-21); 3 releases in the week of Aug 16-21 | 2026-08-24 | [S4] | independently observable |
| Star trajectory corroboration | ~214,000 stars / ~40,000 forks reported by TechCrunch on 2026-07-13 (→ +21k stars in ~6 weeks) | 2026-07-13 | [S12] | press (independent) |
| PyPI downloads, hermes-agent | 71,564 weekly / 394,231 monthly | 2026-08-24 | [S18] | independently observable |
| npm downloads, hermes-agent | 5,639 weekly (08-17..23) / 10,220 monthly | 2026-08-24 | [S6b] | independently observable (package officialness unclear, see §6) |
| Homebrew installs (formula hermes-agent) | 3,524 (30d) / 8,847 (90d) / 10,397 (365d) | 2026-08-24 | [S7] | independently observable |
| Docker Hub pulls, nousresearch/hermes-agent | 8,556,005 pulls; 152 stars | 2026-08-24 | [S9] | independently observable |
| Discord members (Nous Research server — company-wide, not agent-specific) | ~133,864 members, ~16,152 online | 2026-08-24 | [S19] | independently observable |
| GitHub Discussions | not enabled on repo | 2026-08-24 | [S3] | independently observable |
| Funding: Series A | $50M led by Paradigm, April 2025, ~$1B (token) valuation | 2025-04-28 | [S20] | press |
| Funding: prior total | ~$70M from Paradigm, Robot Ventures, North Island Ventures, Delphi Ventures, OSS Capital, Balaji Srinivasan (per TechCrunch) | 2026-07-13 | [S12] | press |
| Funding: new round in talks | ≥$75M at $1.5B valuation, led by Robot Ventures, USV participating ("in talks", not closed at publication) | 2026-07-13 | [S12] | press |
| Cloud-hosted tiers | $20–$200/month (TechCrunch); Portal tiers named Plus/Super/Ultra on homepage, prices not shown there | 2026-07-13 | [S12][S10] | press / maker |
| Usage numbers from maker (users, revenue, tokens) | none found on site or repo | 2026-08-24 | [S10][S11][S1] | researched, absent |
| Public customers / case studies / logos | none found on site | 2026-08-24 | [S10][S11] | researched, absent |
| Benchmarks | no first-party SWE-bench / Terminal-Bench placement found; open issue #23137 requests SWE benchmarks; only aggregator "benchmark hubs" (Armalo etc.) publish numbers | 2026-08-24 | [S21] | researched, absent (first-party) |
| Press coverage | TechCrunch (funding, 2026-07-13); MarkTechPost (Bot Mode, 2026-08-17); Startup Fortune (Hermes Desktop preview, announced 2026-06-02) | 2026-08-24 | [S12][S13][S14] | press |
| GitHub topics self-tagging | tags itself with 'claude-code', 'codex', 'anthropic', 'openai' (discoverability positioning against those tools) | 2026-08-24 | [S3] | independently observable |

## 3. Plugin interface (PRI-2925)

- mcp_support: **both** — MCP client (stdio + HTTP transports, per-server include/exclude tool filtering with glob patterns, OAuth 2.1 with headless paste-back/SSH-forward flows, tools namespaced `mcp_<server>_<tool>`) AND MCP server (`hermes mcp serve` exposes Hermes's messaging capabilities to other MCP clients such as Claude Code or Cursor) [S22] (as-of 2026-08-24). Evidence: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- plugin_support: **True** — Python plugin system: `plugin.yaml` + `register(ctx)` entry point; four types (general, memory providers, context engines, model providers); registration APIs for tools, hooks (26 events), slash commands, CLI subcommands, skills, gateway platforms, media providers; discovery from bundled / `~/.hermes/plugins/` / project / pip entry points / NixOS; curated community index (`hermes-plugin-index`, commit-SHA-pinned); capability-consent model with install-time static security scanning (safe/caution/dangerous verdicts, dangerous not overridable); `hermes://` deep links from Desktop; declarative plugin packs [S23]. Separate skills system (SKILL.md, below). Evidence: https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins
- claude_code_plugin: **partial** — no support for the Claude Code plugin format/marketplaces (researched, absent from plugin docs [S23]); but it auto-discovers CLAUDE.md, AGENTS.md and .cursorrules project context files (subagents inherit them too) [S25], and its skills use the SKILL.md format per the agentskills.io open standard, with `hermes skills install` sourcing from anthropics/skills, openai/skills, skills.sh, well-known endpoints, ClawHub, LobeHub [S24].
- subagents: **True** — `delegate_task` tool spawns child agents with fresh isolated context; default 3 concurrent (configurable, no hard ceiling); async top-level delegation (handle returned, result re-enters conversation); flat by default, hierarchical via `role="orchestrator"` + `max_spawn_depth`; restricted toolset for children; optional per-child git-worktree isolation (`delegation.worktree_isolation`) [S25]. Evidence: https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation
- hooks: **True** — four hook systems: gateway hooks (Python in `~/.hermes/hooks/`; session/agent/command/reaction events), plugin hooks (26 events incl. `pre_tool_call`, `post_tool_call`, `pre_llm_call`, `post_llm_call`, `subagent_start/stop`, kanban task events), shell hooks (config.yaml, any language), outbound webhooks (HTTP POST). `pre_tool_call` can block or rewrite tool args; transform hooks rewrite tool results, terminal output, and final LLM output [S26]. Evidence: https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks
- plan_mode: **partial** — a bundled "plan" skill (`/skill plan`, `hermes -s plan`) constrains the agent to read-only inspection and writes a markdown plan to `.hermes/plans/` without executing; but it is prompt-level (one-shot, evictable by context compression), not an enforced config-level mode — open feature requests #20616 and #26352 explicitly ask for a Claude-Code-style enforced plan mode [S27]. Security docs mention no read-only mode [S17]. Evidence: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-plan
- plugin_docs_url: https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins (skills: .../docs/user-guide/features/skills)
- config_docs_url: https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- ACP support: **yes, first-party** — `hermes acp` / `hermes-acp` / `python -m acp_adapter` runs an ACP server over stdio; documented clients: VS Code (ACP Client extension), Zed, JetBrains, Buzz Desktop, Buzz Relay Bridge; curated `hermes-acp` toolset (files, terminal, web/browser, memory search, skills, code execution, vision; messaging/cron excluded); sessions are not persisted across server restarts; approval UX depends on host [S8]. This is the surface Paseo uses (`hermes acp`). Evidence: https://hermes-agent.nousresearch.com/docs/user-guide/features/acp
- SDK: no separate agent SDK found (researched, absent) — extensibility is via the plugin API, the OpenAI-compatible API server, MCP server mode, and A2A v1.0 agent-to-agent communication (Herald release) [S23][S2][S15].
- Skills system (context for the census): SKILL.md + YAML frontmatter, three-level progressive disclosure; dirs `~/.hermes/skills/`, project `.hermes/skills/` and `.agents/skills/`; `hermes skills browse/search/inspect/install` with security scanning; agent autonomously creates and patches skills via `skill_manage` (gate with `skills.write_approval`); `/learn` turns source material into skills [S24].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage, verbatim): "The Agent That Grows With You" [S10]; repo description: "The agent that grows with you" [S3]
- docs one-liner (verbatim, short): "The self-improving AI agent built by Nous Research. The only agent with a built-in learning loop" [S2]
- maker claims (paraphrased):
  1. Only agent with a closed learning loop: creates skills from experience after complex tasks, improves them during use, nudges itself to persist knowledge, searches its own past conversations (FTS5 + LLM summarization), builds a deepening user model across sessions (Honcho dialectic modeling) [S2][S1][S28].
  2. Agent-curated persistent memory: MEMORY.md + USER.md, bounded and injected into the system prompt; background post-turn review updates memory/skills; `/journey` timeline to audit what it learned [S28].
  3. Runs anywhere, cheap: "$5 VPS", GPU cluster, or serverless (Daytona/Modal hibernation "costing nearly nothing between sessions"); seven terminal backends (local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox) [S1].
  4. Lives in your messaging apps: Telegram, Discord, Slack, WhatsApp, Signal, Email + CLI from one gateway; cross-platform conversation continuity; not tied to your laptop [S1][S2].
  5. Model-agnostic, no lock-in: any provider/endpoint, switch with `hermes model`; optional one-subscription Nous Portal (300+ models + Tool Gateway) [S1].
  6. Scheduled autonomy: natural-language cron automations delivered to any platform, running unattended [S1].
  7. Delegation + zero-context-cost pipelines: isolated subagents; Python scripts calling tools via RPC collapse multi-step pipelines into single turns [S1].
  8. Research-ready: batch trajectory generation and trajectory compression "for training the next generation of tool-calling models" [S1].
- audience: developers and technical users self-hosting an extensible agent [S10]; plus researchers (trajectory/training tooling) [S1]. Not positioned primarily as a coding tool — coding is one capability among many (general autonomous assistant).

## 5. Company & contact targets (PRI-2929) — company-level only

- company: Nous Research (exact legal name not verified; researched, not published on site) [S11]
- HQ: not stated on nousresearch.com (researched, absent); US-based per self-description ("American open source AI movement") [S11]
- size: not researched (null)
- funding stage: venture-backed; $50M Series A led by Paradigm (Apr 2025, ~$1B valuation) [S20]; ~$70M total prior; in talks (Jul 2026) for ≥$75M at $1.5B led by Robot Ventures with USV [S12]
- other products: Hermes open-model family (Hermes 4), Nous Portal (inference + tool subscription), Nous Chat, Psyche/decentralized training, Atropos RL framework [S11][S10]
- publicly named leadership: the company site names no individuals (researched, absent on nousresearch.com) [S11]. Founders as named in press (TechCrunch, 2026-07-13): Jeffrey Quesnelle (CEO per multiple press/aggregator profiles), Karan Malhotra, Ryan "Teknium", Shivani Mitra [S12][S29]. Per DOSSIER_SPEC these are press-named, not company-page-named — flagged in §6.
- contact: Discord (https://discord.gg/NousResearch) and GitHub are the public channels; no partnerships contact page found (researched, absent) [S1][S11]

## 6. Open questions / conflicts

- **No existing census entry** — hermes-agent is a new entry. Note: the census already has slug `nous` (hc/agents/nous.md), which is an UNRELATED project (TrafficGuard/nous = "TypedAI", maker TrafficGuard). No data conflict, but naming-confusion risk; proposed slug `hermes-agent` avoids collision.
- First public release date is fuzzy: repo created 2025-07-22 [S3]; earliest GitHub release 2026-03-12 (tagged v0.2.0) [S4]; several SEO-ish third-party wikis state a 2026-02-25 launch [S15] — no first-party announcement located. Recommend `first_released: 2026-03-12` (first verifiable public release) with a note.
- The npm package `hermes-agent` tracks official versions (0.20.5 same-day as GitHub) and points its homepage at NousResearch/hermes-agent, but its sole npm maintainer is a personal account ("wyrtensi") [S6]. Official docs/README install paths do not mention npm. Officialness unverified.
- Star velocity is extreme (0 → 235k in ~5-6 months of public life). TechCrunch independently reported 214k on 2026-07-13 [S12], so the order of magnitude is corroborated, but growth-curve claims ("95.6k by mid-April", "152k by early May") come only from aggregator sites [S15] — unverified.
- Discord member count (~134k) is the company-wide Nous Research server, not an agent-specific community [S19].
- Cloud pricing: "$20–$200 monthly" is TechCrunch's summary [S12]; homepage names tiers (Plus/Super/Ultra) without prices on the page fetched [S10]. Portal pricing page not fetched (behind portal.nousresearch.com; not researched).
- Leadership names come from press, not the company's own pages — DOSSIER_SPEC prefers company-named; treat §5 names as press-sourced.
- "Only agent with a built-in learning loop" is a maker superlative; competing agents (e.g. OpenClaw-family, pi-hermes-memory-style plugins) make adjacent claims — not adjudicated here.
- Lineage vs. OpenClaw: `hermes claw migrate` (README) and an arXiv benchmark grouping "OpenClaw-style agent harnesses" [S21] suggest Hermes Agent is positioned as an OpenClaw-family successor/competitor; exact code lineage not researched.
- Unofficial lookalike domains exist and were NOT used as sources: hermes-ai.net, hermes-agent.org, get-hermes.ai, hermes-tutorials.dev, aiwiki.ai, kie.ai, armalo.ai [S15][S21].
- pypistats first attempt rate-limited (429); succeeded on retry — numbers in §2 are from the successful call [S18].
- PyPI latest is 0.19.0 while GitHub/npm are at 0.20.5 — PyPI channel appears to lag ~1 month [S5][S4].

## Proposed new-entry frontmatter (schema v1.1, hc/agents/hermes-agent.md)

```yaml
name: "Hermes Agent"
slug: "hermes-agent"
layout: "agent.njk"
category: "agent"
maker: "nous-research"        # new maker record needed: maker_type company, country US (site
                              # says "American"; HQ unpublished), makes_models: True (Hermes
                              # model family), revenue_model: [tokens, subscriptions] (Nous Portal)
license: "MIT"
url: "https://hermes-agent.nousresearch.com"
source_code_url: "https://github.com/NousResearch/hermes-agent"
source_available: True
homepage: "https://hermes-agent.nousresearch.com"
docs_url: "https://hermes-agent.nousresearch.com/docs/"
download_url: "https://hermes-agent.nousresearch.com/"
install_method: "curl install script, PowerShell script, desktop installer (macOS/Win/Linux), brew, pip, docker"
platforms: ["CLI", "Desktop", "Autonomous"]   # + IDE via first-party ACP (`hermes acp`)
autonomy_level: ["agentic", "autonomous-background"]
specialization: "general"
language: "Python"
first_released: "2026-03-12"   # first verifiable public GitHub release (v0.2.0); repo created 2025-07-22
current_release: "2026-08-21"  # v2026.8.19 / 0.20.5
maintained: "active"
mcp_support: "both"            # MCP client + `hermes mcp serve`
plugin_support: "yes"          # plugin.yaml Python plugins + SKILL.md skills, community index
claude_code_plugin: "partial"  # reads CLAUDE.md/AGENTS.md and agentskills.io SKILL.md skills; no CC plugin format
subagents: "yes"               # delegate_task, orchestrator role, worktree isolation
hooks: "yes"                   # 4 hook systems, blocking pre_tool_call, transforms
plan_mode: "partial"           # bundled read-only 'plan' skill; no enforced config-level mode
plugin_docs_url: "https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins"
config_docs_url: "https://hermes-agent.nousresearch.com/docs/user-guide/configuration"
model_providers: "Nous Portal, OpenRouter, OpenAI, any OpenAI-compatible endpoint"
pricing: "free"                # agent MIT/free; optional Nous Portal subscription
github_stars: "235605"         # 2026-08-24
sources: ["paseo"]
last_verified: "2026-08-24"
what_makes_it_special: "A self-improving general agent with a closed learning loop — it autonomously creates SKILL.md skills after complex tasks, improves them during use, and curates its own persistent memory — designed to live on a cheap VPS and be driven from messaging apps as much as from the terminal (Paseo drives it as a coding agent over first-party ACP)."
```

## 7. Sources

1. [S1] https://raw.githubusercontent.com/NousResearch/hermes-agent/main/README.md — tagline, claims, install, commands, Portal, OpenClaw migrate
2. [S2] https://hermes-agent.nousresearch.com/docs — self-description, install, providers, nav
3. [S3] https://api.github.com/repos/NousResearch/hermes-agent (+ search, languages, org) — stars/forks/dates/license/topics
4. [S4] https://api.github.com/repos/NousResearch/hermes-agent/releases — release list, first/latest
5. [S5] https://pypi.org/pypi/hermes-agent/json — PyPI versions, dates, license
6. [S6] https://registry.npmjs.org/hermes-agent — npm versions, maintainer; [S6b] https://api.npmjs.org/downloads/point/... — npm downloads
7. [S7] https://formulae.brew.sh/api/formula/hermes-agent.json — brew formula + install analytics
8. [S8] https://hermes-agent.nousresearch.com/docs/user-guide/features/acp — ACP server, clients, toolset
9. [S9] https://hub.docker.com/v2/repositories/nousresearch/hermes-agent/ — Docker pulls
10. [S10] https://hermes-agent.nousresearch.com/ — homepage tagline, tiers, downloads
11. [S11] https://nousresearch.com/ — company mission, products, no named team
12. [S12] https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/ — funding, founders, 214k stars, cloud tiers
13. [S13] https://www.marktechpost.com/2026/08/17/nous-research-hermes-bot-mode/ — Bot Mode, v0.20.3
14. [S14] https://startupfortune.com/nous-research-brings-hermes-agent-out-of-the-terminal/ — Hermes Desktop preview (2026-06-02)
15. [S15] web search results (kie.ai, aiwiki.ai, hermes-agent.org, baike.baidu.com, layer3labs.io) — unverified launch-date and star-growth claims; Herald release/A2A mention
16. [S16] https://api.github.com/repos/NousResearch/hermes-agent/languages — Python/TypeScript split
17. [S17] https://hermes-agent.nousresearch.com/docs/user-guide/security — approval modes, blocklist, isolation
18. [S18] https://pypistats.org/api/packages/hermes-agent/recent — PyPI downloads (retry after 429)
19. [S19] https://discord.com/api/v9/invites/NousResearch?with_counts=true — Discord member count
20. [S20] https://www.theblock.co/post/352000/paradigm-leads-50-million-usd-round-decentralized-ai-project-nous-research — Series A
21. [S21] web search results (armalo.ai, arxiv 2606.12344, GitHub issues #23137, #477) — no first-party benchmarks; OpenClaw-family framing
22. [S22] https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp — MCP client+server details
23. [S23] https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins — plugin system, index, security scanning
24. [S24] https://hermes-agent.nousresearch.com/docs/user-guide/features/skills — SKILL.md, sources, autonomous creation
25. [S25] https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation — subagents, worktrees, context-file inheritance (CLAUDE.md etc.)
26. [S26] https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks — hook systems and events
27. [S27] https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/software-development/software-development-plan + GitHub issues #20616, #26352 — plan skill and its limits
28. [S28] https://hermes-agent.nousresearch.com/docs/user-guide/features/memory — MEMORY.md/USER.md, learning loop
29. [S29] web search results (rocketreach, cbinsights aggregators) — CEO title corroboration (press-level only)
30. https://hermes-agent.nousresearch.com/docs/user-guide/features/overview — feature index (skills/plugins/hooks/MCP/subagents map)

## Inclusion check (Jesse's test)

**Yes** — Hermes Agent is a first-party agent with its own agentic loop (file ops, patch/write tools, terminal execution across seven backends, sandboxed code execution via RPC, iterating to completion), not a wrapper around someone else's agent; its ACP mode exposes that same loop to editors/Paseo [S1][S8][S17]. Caveat for the directory narrative: it is a general-purpose autonomous agent for which coding is one capability, rather than a coding-first harness.
