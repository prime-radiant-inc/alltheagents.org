# Dossier: Stakpak (census_slug: stakpak)

Compiled 2026-08-24 (task-dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". NOT currently in the census — proposed new-entry frontmatter at the end. Key event: acquired by Vercel, announced ~2026-07-23 [S6].

## 1. Identity

- name: Stakpak (repo `stakpak/agent`, binary `stakpak`)
- maker: company — Stakpak, Egyptian-founded startup, founded 2023 by George Fahmy; acquired by Vercel (US) for undisclosed terms, announced week of 2026-07-23 [S6] (as-of 2026-08-24). Org form: company (now Vercel subsidiary/team).
- product URL: https://stakpak.dev | repo URL: https://github.com/stakpak/agent | docs: https://stakpak.gitbook.io
- license: Apache-2.0 (GitHub API) [S1]
- open source? True. source_available: True — full agent source in the repo [S1]
- first public release: repo created 2024-12-10 [S1]; earliest release visible in the last 100 is v0.3.1, 2025-11-30 (older releases exist beyond the API page) [S4]
- latest release: v0.3.88, 2026-06-10; repo last pushed 2026-07-06 — release cadence stopped around the Vercel acquisition [S4][S1] (as-of 2026-08-24)
- what it is:
  - Form factor: CLI/TUI agent plus a background-autonomous "autopilot" mode — "lives on your machines 24/7, keeps your apps running, and only pings when it needs a human" (repo description); also integrates into editors via ACP [S1][S3].
  - Specialization: DevOps/infrastructure — auto-healing, incident response, cost optimization, cert/secret maintenance; tutorials are containerization, TLS, migrations, VPN [S2][S5].
  - Models: BYO Anthropic/OpenAI/Gemini keys, or a Stakpak API key (no card required), or local OpenAI-compatible endpoints (Ollama, LM Studio); README config example defaults to `anthropic/claude-sonnet-4-5` [S3][S7].
  - Pricing: open source, free to self-run; hosted Stakpak API key offered; no public price list found (researched, absent on the pages consulted) [S3][S2].
  - Install: Homebrew (tap; no homebrew/core formula exists), curl script, binary releases, Docker; Linux/macOS/Windows [S3][S8].
  - Default autonomy: approval-gated with bulk message approval for multiple tool calls; "warden" guardrails block destructive operations; secret substitution keeps 210+ secret types out of LLM sight; privacy mode; reversible file operations; audit logs + session replay [S3][S2] (maker-described).
  - Language: Rust [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| Acquired by Vercel | announced ~2026-07-23; undisclosed terms; Vercel's 3rd acquisition in under a year; framed as "agentic infrastructure / self-driving DevOps" | 2026-08-24 | [S6] | independently observable (press) |
| GitHub stars | 1,748 | 2026-08-24 | [S1] | independently observable |
| GitHub forks | 185 | 2026-08-24 | [S1] | independently observable |
| GitHub watchers | 14; open issues 39 | 2026-08-24 | [S1] | independently observable |
| "5,000+ developers" | stated on stakpak.dev | 2026-08-24 | [S2] | maker-claimed |
| Customer logos on site | Paymob, Mistral AI, Writer, Breadfast, Overmind, Replicated, Daytona, Alpine SG, Haktiv AI, eVision, Luciq AI, Garment.io, Nawy, Robusta Group, Vectara | 2026-08-24 | [S2] | maker-claimed (logo wall) |
| Release-asset downloads | 33,681 on v0.3.88 alone; 66,371 across the last 100 releases (2025-11-30..2026-06-10) | 2026-08-24 | [S4] | independently observable (may include CI) |
| Release cadence | ~88 releases in the 0.3.x line; near-daily until 2026-06-10, then stopped | 2026-08-24 | [S4] | independently observable |
| Community | Discord linked from site (member count not captured — null) | 2026-08-24 | [S2] | null |
| Funding pre-acquisition | not researched beyond acquisition press — null | — | — | null |
| Benchmarks | none found | 2026-08-24 | [S6] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **server (plus MCP proxy)** — README: functions as an MCP server, and ships an MCP proxy server multiplexing connections to multiple upstream MCP servers (the proxy makes it a client of upstreams in proxy mode). Recorded as "server + proxy"; plain client-mode config for the agent loop itself not confirmed [S3] (as-of 2026-08-24). Evidence: https://github.com/stakpak/agent README.
- plugin_support: **partial — "Rulebooks"** — markdown SOPs ("smart, markdown based SOPs") that teach the agent org-specific workflows; official + custom rulebooks, managed/created at stakpak.dev, toggled per session; not an installable plugin/marketplace ecosystem [S5]. Evidence: https://stakpak.gitbook.io/docs/how-it-works/rulebooks.md
- claude_code_plugin: **no** — no mention of CLAUDE.md, `.claude/` dirs, AGENTS.md, or Claude Code plugin format (researched, absent) [S3].
- subagents: **True** — "Specialized research agents for code exploration and sandboxed analysis with different tool access levels" via `--enable-subagents` [S3].
- hooks: **False** — no lifecycle-hook system found in README or docs index (researched, absent) [S3][S9].
- plan_mode: **partial** — no dedicated read-only plan mode found; ACP integration advertises "Agent Plans — visual task breakdown and progress tracking", and bulk approval gates execution [S3].
- plugin_docs_url: https://stakpak.gitbook.io/docs/how-it-works/rulebooks.md (nearest equivalent). config_docs_url: https://stakpak.gitbook.io (docs root; install page /docs/get-started/install-stakpak.md).
- ACP support: **yes, first-party** — `stakpak acp` starts an ACP agent; README documents Zed integration; this is how Paseo drives it [S3].
- SDK: **False** — none found; it is its own Rust agent (an earlier summarizer suggestion that it builds on Anthropic's Claude Agent SDK is NOT in the README — verified absent by text search) [S3][S8].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (verbatim): "Ship your code, on autopilot" [S2][S1]
- maker claims (paraphrased):
  1. Autonomous 24/7 operations agent: auto-healing, incident response, proactive maintenance (certs, secrets, runtime updates), cost optimization — DevOps, not general coding [S2].
  2. Security architecture as the headline: "Warden" network sandbox with Cedar policy enforcement, secret substitution (210+ secret types never reach the LLM), mTLS, audit logs + session replay, rollback [S2][S3].
  3. Runs on your machines / on-prem, single binary, no cloud lock-in [S2].
  4. Human-in-the-loop economy: "only pings when it needs a human"; bulk approvals [S1][S3].
  5. Rulebooks: org-specific SOPs the agent follows "just like a teammate would" [S5].
  6. Multi-provider models: BYO Anthropic/OpenAI/Gemini, Stakpak API, or local endpoints [S3].
- audience: development teams and DevOps/platform engineers running production apps who want autonomy without losing control or compliance [S2].

## 5. Company & contact targets (PRI-2929)

- Legal/company: Stakpak (Egyptian-founded, 2023); now part of Vercel Inc. (US, valued ~$9.3B per acquisition press) [S6]. Approx size pre-acquisition: small startup (press describes a startup team; exact headcount not published — null).
- Publicly named leadership: founder George Fahmy (named in acquisition press) [S6]. Post-acquisition, partnership contact would route through Vercel. No other named executives found on the site (no team page located — researched, absent) [S2].
- Funding stage: acquired (by Vercel, 2026-07); prior rounds not researched (null).

## 6. Open questions / conflicts

- Post-acquisition fate of the OSS agent is unclear: releases stopped 2026-06-10 and pushes 2026-07-06; whether Stakpak continues as a standalone product or is folded into Vercel is unknown. `maintained` is best recorded as "acquired".
- "5,000+ developers" and the logo wall (incl. Mistral AI, Writer, Vectara) are maker-claimed and unverified; logo walls often mean users of a free tier, not paying customers.
- MCP: site/README emphasize server + proxy; whether the agent's own loop consumes arbitrary MCP servers directly (plain client mode) was not conclusively established — recorded as partial/unclear.
- Hosted pricing: a Stakpak API key exists ("no card required") but no price page was found — pricing model beyond "open source + hosted API" is null.
- Release-asset download totals (66k) may include CI/automation; no per-user install metric exists (no core brew formula, not on npm/crates).
- Pre-acquisition funding history (accelerators, seed) not researched — null.
- Older releases (< v0.3.1) exist beyond the API's 100-item page; first-ever release date not pinned (repo created 2024-12-10).

## 7. Sources

1. [S1] https://api.github.com/repos/stakpak/agent — stars, license, dates, description, topics
2. [S2] https://stakpak.dev/ — tagline, features, security claims, "5,000+ developers", logos, acquisition banner
3. [S3] https://raw.githubusercontent.com/stakpak/agent/main/README.md — install, models, MCP/ACP, subagents, warden, approval model
4. [S4] https://api.github.com/repos/stakpak/agent/releases?per_page=100 — v0.3.88 latest, asset download totals, cadence
5. [S5] https://stakpak.gitbook.io/docs/how-it-works/rulebooks.md — rulebooks = markdown SOPs
6. [S6] Web search, acquisition press 2026-07: pulse2.com; disruptafrica.com (2026-07-23); iafrica.com; techinafrica.com; businesstechafrica.co.za — Vercel acquisition, founder George Fahmy, founded 2023
7. [S7] README config excerpts (model = "anthropic/claude-sonnet-4-5") — default model reference
8. [S8] formulae.brew.sh (no `stakpak` core formula) + README text search (no "Claude Agent SDK" mention) — negative checks
9. [S9] https://stakpak.gitbook.io/ — docs index (rulebooks, warden, autopilot; no hooks/plugin pages)

## Inclusion check (Jesse's test)

**Yes** — Stakpak is a full agent with its own agentic loop implemented in Rust (own tool execution, approval gating, subagents, multi-provider model layer); it can create and modify software (and infrastructure config) via an LLM, and `stakpak acp` exposes its native loop rather than wrapping another vendor's agent [S1][S3]. Its specialization is DevOps rather than general coding.

## Proposed census entry (new; per hc/agents/_TEMPLATE.md)

```yaml
---
name: "Stakpak"
slug: "stakpak"
layout: "agent.njk"
category: "agent"
maker: "stakpak"            # new makers.json record: maker_type company, country EG (founded; acquired by Vercel, US, 2026-07), makes_models false, revenue_model ["tokens"]  # hosted API key; details unpublished
license: "Apache-2.0"
url: "https://stakpak.dev"
source_code_url: "https://github.com/stakpak/agent"
source_available: true
homepage: "https://stakpak.dev"
docs_url: "https://stakpak.gitbook.io"
download_url: "https://github.com/stakpak/agent/releases"
install_method: "brew tap, curl script, binaries, Docker"
platforms: ["CLI", "Autonomous"]
autonomy_level: ["agentic", "autonomous-background"]
specialization: "devops"
language: "Rust"
first_released: null                 # repo created 2024-12-10; first tagged release not pinned
current_release: "2026-06-10"        # v0.3.88
maintained: "acquired"               # Vercel, announced 2026-07-23; releases stopped 2026-06
mcp_support: "server + MCP proxy (multiplexes upstream servers); plain client mode unconfirmed"
plugin_support: "partial — Rulebooks (markdown SOPs, official + custom)"
claude_code_plugin: false
subagents: true                      # --enable-subagents research agents
hooks: false
plan_mode: "partial — ACP Agent Plans + bulk approval; no dedicated read-only mode"
plugin_docs_url: "https://stakpak.gitbook.io/docs/how-it-works/rulebooks.md"
config_docs_url: "https://stakpak.gitbook.io"
model_providers: "Anthropic, OpenAI, Gemini, Stakpak API, local OpenAI-compatible (Ollama, LM Studio)"
pricing: "free (OSS) + hosted API (BYOK optional)"
github_stars: "1748"
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "A security-first autonomous DevOps agent (Rust) that runs 24/7 on your own machines — Cedar-policy sandboxing, secret substitution, audit replay — acquired by Vercel in July 2026."
---
```
