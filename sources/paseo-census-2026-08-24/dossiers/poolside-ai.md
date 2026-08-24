# Dossier: Poolside (pool CLI) (census_slug: poolside-ai)

Compiled 2026-08-21. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Subject = the `pool` coding agent / Poolside Agent CLI; company context included because Poolside is primarily a model + enterprise/government platform company.

## 1. Identity

- name: `pool` — "Poolside Agent CLI" (docs title); repo and README call it "pool, Poolside's coding agent" [S1][S2] (as-of 2026-08-21)
- maker: Poolside, Inc., Delaware corporation, 548 Market St., PMB 53385, San Francisco, CA 94104 (Terms of Use) [S20]; public-sector entity "Poolside Federal LLC" (CAGE 11R53) [S21]; org form: company; offices US + Paris [S27][S37] (as-of 2026-08-21)
- product URL: https://docs.poolside.ai/cli/pool (GitHub repo homepage field) [S1][S2]; company site https://poolside.ai
- repo URL: https://github.com/poolsideai/pool — holds README.md, CHANGELOG.md, LICENSE.md, `third_party/`, and release binaries only; no agent source [S1][S4] (as-of 2026-08-21)
- license: proprietary. LICENSE.md: "(c) Poolside. All rights reserved. Use is subject to the Poolside End User License Agreement" (links to poolside.ai/eula, which serves the Terms of Use) [S4][S20]. GitHub API reports license: null [S3].
- open source? False for the CLI. source_available: False (binaries + changelog only) [S1][S3]. The *models* (Laguna family) are open-weight: Laguna S 2.1 and XS 2.1 under OpenMDW-1.1, Laguna M.1 and XS.2 under Apache-2.0, weights on Hugging Face [S8][S24]. Terms of Use state models are "licensed under their respective open source licenses" and are not "Products" [S20].
- first public release: 2026-04-28 — CHANGELOG `[1.0.0] - 2026-04-28`; same-day launch post "Introducing Laguna XS.2 and Laguna M.1" describes pool as a terminal coding agent and dual ACP client/server released as a research preview [S5][S23]. GitHub repo created 2026-04-14 [S3].
- latest release: v1.0.16, 2026-08-14 (GitHub release; docs page states "v1.0.16") [S3][S2][S5]. 14 GitHub releases (v1.0.3..v1.0.16, 2026-05-27..2026-08-14; each with 7 binary assets); CHANGELOG also lists 1.0.0-1.0.2 (Apr 28, May 4, May 14) without GitHub releases [S3][S5].
- what it is:
  - Form factors: terminal TUI (`pool`), non-interactive (`pool exec`), ACP server (`pool acp` stdio; `pool acp serve` HTTP, experimental) for Zed/JetBrains/Xcode/other ACP clients, and ACP *client* (`pool --agent-server`) that can drive other agents (e.g. claude-agent-acp, codex-acp) [S1][S7]. Related surfaces: Poolside Desktop Assistant (macOS, Apple Silicon; an ACP client that bundles its own copy of the pool agent) [S16][S28]; "Poolside Assistant" VS Code / Visual Studio extensions [S12][S34]; Poolside Chat web (chat.poolside.ai) [S12].
  - Models: default = Poolside-hosted Laguna (Laguna S 2.1 118B-A8B 1M ctx; Laguna XS 2.1 33B-A3B 256K; Laguna M.1 225B-A23B 256K) via Poolside Platform (`pool login`), self-managed Poolside deployment (`--api-url`), OpenRouter (native), Ollama (`ollama launch pool`), or any OpenAI-compatible endpoint via `POOLSIDE_STANDALONE_BASE_URL` — i.e. BYO model/endpoint supported [S1][S6][S8] (as-of 2026-08-21).
  - Pricing: CLI is free to download; Poolside Platform gives "free developer access to models hosted by Poolside" [S6]; models page: "free to use for a limited time" [S11]; Terms of Use allow training on content unless opted out [S20]. Paid usage via OpenRouter (Laguna S 2.1 $0.10/$0.20 per 1M in/out at launch) [S24][S22]. Enterprise/government: self-managed subscription, no public price [S21][S31].
  - Install: `curl -fsSL https://downloads.poolside.ai/pool/install.sh | sh` (macOS/Linux); `irm https://downloads.poolside.ai/pool/install.ps1 | iex` (Windows, beta/preview); `pool update`; no npm/brew/cargo path documented; a `poolsideai/homebrew-tap` repo exists but its formula is a placeholder (version 0.0.0) [S6][S1][S36] (as-of 2026-08-21).
  - Default autonomy: approval mode `default` ("Always ask") prompts for tool actions not already allowed; other modes `accept-edits`, `auto` (classifier-rated risk; requires a configured classifier model; added v1.0.16), `always-allow`; Shift+Tab / `/mode`. Separate agent modes Build / Plan; Plan→Build switch always requires user review. Optional Docker-based sandbox (`--sandbox required|disabled`) [S1][S9][S5] (as-of 2026-08-21).
  - Repo language per GitHub API: null (no source) [S3].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars, poolsideai/pool | 408 | 2026-08-21 | [S3] | independently observable |
| GitHub forks / watchers / open issues | 22 / 9 / 22 | 2026-08-21 | [S3] | independently observable |
| GitHub issues ever filed | 39 | 2026-08-21 | [S3] | independently observable |
| GitHub contributors (incl. anonymous) | 4 (release-publishing repo, no source) | 2026-08-21 | [S3] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 26 | 2026-08-21 | [S3] | independently observable |
| Releases | 14 on GitHub, roughly weekly-to-biweekly (v1.0.3 2026-05-27 -> v1.0.16 2026-08-14) | 2026-08-21 | [S3][S5] | independently observable |
| GitHub Discussions | not enabled | 2026-08-21 | [S3] | independently observable |
| npm / PyPI / crates downloads | none — not distributed via package registries (installer script only) | 2026-08-21 | [S6][S1] | researched, absent |
| Homebrew | `poolsideai/homebrew-tap` exists with a placeholder formula; no analytics | 2026-08-21 | [S36] | independently observable |
| Hugging Face downloads (last 30d / all-time): poolside/Laguna-S-2.1 | 113,981 / 126,610; 981 likes (created 2026-07-13) | 2026-08-21 | [S25] | independently observable (model, not CLI) |
| HF: Laguna-S-2.1-NVFP4 / Laguna-S-2.1-GGUF (30d) | 596,798 / 420,275 | 2026-08-21 | [S25] | independently observable |
| HF: Laguna-XS-2.1 / XS-2.1-GGUF (30d) | 61,548 / 148,329 | 2026-08-21 | [S25] | independently observable |
| HF: Laguna-XS.2 all-time | 410,407 (created 2026-04-23) | 2026-08-21 | [S25] | independently observable |
| HF: Laguna-M.1 all-time | 12,571 | 2026-08-21 | [S25] | independently observable |
| VS Code Marketplace: poolside-ai.poolside-assistant ("Poolside Enterprise Assistant", v5.0.0, released 2025-03-25) | 10,762 installs; 2 ratings avg 5.0 | 2026-08-21 | [S34] | independently observable |
| VS Code Marketplace: poolside-ai.acp-assistant ("Poolside Assistant", v1.5.3, released 2026-07-22) | 757 installs | 2026-08-21 | [S34] | independently observable |
| Visual Studio Marketplace: vs-poolside-assistant / vs-acp-assistant | 1,392 / 134 installs | 2026-08-21 | [S34] | independently observable |
| ACP registry listing | "Poolside" listed in the ACP agents directory (link to github.com/poolsideai/pool) | 2026-08-21 | [S17] | independently observable |
| Paseo support | Paseo's ACP provider catalog: id "poolside", command `["pool","acp"]`, install link docs.poolside.ai/cli/pool; listed in public-docs/supported-providers.md | 2026-08-21 | [S35] | independently observable |
| Third-party harness integrations (docs pages) | Zed, JetBrains, Neovim/CodeCompanion, Cline, GitHub Copilot, Kilo Code, Goose, OpenClaw, Hermes, OpenCode, Pi, GitHub Actions, n8n, Ollama (these consume Laguna models, not pool) | 2026-08-21 | [S10] | maker-documented |
| Benchmarks (model, pool harness not named on leaderboard): Laguna S 2.1 Terminal-Bench 2.1 70.2%; SWE-Bench Multilingual 78.5%; SWE-Bench Pro 59.4%; DeepSWE v1.1 40.4%; SWE Atlas 46.2%; Toolathlon Verified 49.7% | as stated | 2026-07-21 | [S24] | maker-claimed |
| Benchmarks: Laguna M.1 SWE-Bench Verified 72.5% / Pro 46.9%; XS.2 68.2% / 44.5% | as stated | 2026-04-28 | [S23][S29] | maker-claimed |
| tbench.ai Terminal-Bench 2.1 public leaderboard | no Poolside/Laguna/pool rows among the 17 shown | 2026-08-21 | [S18] | independently observable (absence) |
| Applied Research team size | "approximately 60-person" | 2026-04-28 | [S23] | maker-claimed |
| Company headcount | ~150 (Dec 2025, Wikipedia); Nvidia to make offers to >100 / 109 Laguna staff (Aug 2026) | 2026-08-21 | [S27][S30][S32] | press / third-party |
| Funding: Seed $26M; Series A $100M; Series B $500M at $3B (2024-10-02, Bain Capital Ventures lead; eBay, Nvidia, DST, etc.; total $626M) | as stated | 2024-10-02 | [S26][S27][S33] | maker-claimed (round) / press |
| Funding: Nvidia up to $1B in a ~$2B round at $12B pre-money (reported Oct 2025); the $2B Series C "had fallen apart by April 2026" (press) | as stated | 2025-10-30 / 2026-04 | [S27][S38][S39] | press |
| Nvidia deal: $6B non-exclusive license (Model Factory / models) + $1B investment at $12B pre-money; >100 staff to receive Nvidia offers; Poolside to operate independently | as stated | 2026-08-20/21 | [S30][S32] | press (Newcomer, Bloomberg) |
| Project Horizon: 2 GW AI campus, Fort Stockton / Pecos County, West Texas; CoreWeave anchor tenant for first 250 MW (15-yr lease); >40,000 GB300 NVL72 GPUs via CoreWeave; announced Oct 2025; press later reported CoreWeave exit/project turmoil (2026) | as stated | 2025-10 / 2026 | [S38][S40] | press (official blog URL 404, see s.6) |
| Public customers / partners: Vibrint, Northrop Grumman, Cubic, Sterling Computers, Dell, Hunted Labs, Atos, IQT (government page); AWS first-party partnership (2024-12-04); Dell (2026-05-28); Redpanda (2025-10-28); RTX and U.S. DoD (press/Wikipedia) | as stated | 2026-08-21 | [S21][S14][S27][S31] | maker-claimed (logos) / press |
| Acquisition: Fern Labs (2025-11-18) | as stated | 2025-11-18 | [S14] | maker-claimed |
| Community: Discord / subreddit | none found on README/docs (README directs bugs to GitHub issues) | 2026-08-21 | [S1][S2] | researched, absent |
| Third-party reviews | codexpedite review (tool-call looping "in Malibu 2.2"); VentureBeat, MarkTechPost coverage of Laguna releases | 2026 | [S41][S29][S37] | press |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — connects to MCP servers over stdio (runs inside sandbox), streamable HTTP, and SSE; OAuth/headers/env for auth; `pool mcp add|list|get|remove`; stored under `mcp_servers` in `~/.config/poolside/settings.yaml` or `.poolside/settings(.local).yaml`; no MCP-server mode documented [S13][S1] (as-of 2026-08-21). Evidence: https://docs.poolside.ai/mcp-servers
- plugin_support: **partial / skills only** — Agent Skills format (agentskills.io): `SKILL.md` with `name`/`description` frontmatter in `~/.config/poolside/skills/`, `.poolside/skills/`, `.agents/skills/`, `~/.agents/skills/`; skills surface as slash commands (also advertised to ACP clients); `/skills`. No plugin bundle format, no marketplace, no extensions API [S15][S1] (as-of 2026-08-21). Evidence: https://docs.poolside.ai/skills
- claude_code_plugin: **no** — does not read Claude Code plugins, `.claude/skills`, or CLAUDE.md (docs list only AGENTS.md and the four skills dirs above); compatible with the cross-vendor Agent Skills spec and AGENTS.md, which Claude Code skills can be dropped into if relocated [S15][S19][S1]. Researched, absent.
- subagents: **True** — built-in `general` subagent (in-process, inherits model/config/MCP); custom named subagents in `settings.yaml` (`subagents:` key) of type `in_process`, `command` (any stdio ACP server), or `agent_server`; parallel runs share the workspace; cannot nest or ask questions; `/usage` shows per-subagent tokens [S14b][S1][S5] (as-of 2026-08-21). Evidence: https://docs.poolside.ai/subagents
- hooks: **True** — six shell-command events: `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `PreCompact`, `SessionStart`; can block/rewrite tool calls and prompts, inject context, continue a turn; configured under `hooks:` in settings.yaml (three scopes); fail-open, "not a security boundary"; command type only (no http/prompt hooks) [S16b][S1][S5] (added v1.0.16, 2026-08-14). Evidence: https://docs.poolside.ai/hooks
- plan_mode: **True** — Plan agent mode (`/plan`, `/agent-mode plan`): inspects codebase, prepares a plan without modifying source; no startup flag; return to Build always reviewed by user even under Allow all [S1][S9][S2]. Evidence: https://docs.poolside.ai/cli/pool ; https://docs.poolside.ai/permissions
- plugin_docs_url: https://docs.poolside.ai/skills (skills); https://docs.poolside.ai/mcp-servers (MCP)
- config_docs_url: https://docs.poolside.ai/configure ; settings reference https://docs.poolside.ai/settings-file-reference ; permissions https://docs.poolside.ai/permissions
- ACP support: **yes, first-party, both directions** — `pool acp` is an ACP server (session/list, session/load, mid-turn steering via `poolside/session_steer`, config options, slash commands advertised); `pool --agent-server` makes pool an ACP client for other agents; `pool acp serve` HTTP (experimental); listed in the ACP registry; Poolside also publishes `acp-go-sdk` [S1][S7][S17][S3-org] (as-of 2026-08-21).
- SDK: **no agent SDK** for pool found (researched, absent). Programmatic use = `pool exec -o json` or ACP. Poolside publishes `bridge-sdk` (Python, workflow steps) and an OpenAI-compatible API for models [S3-org][S10].
- Other: AGENTS.md (personal `~/.config/poolside/AGENTS.md`, repo root, nested dirs) [S19]; system prompt override in settings.yaml; web search via Exa/Parallel; secrets keychain; sessions/rewind; git worktree flag `-w`; trajectory export (`--atif`) [S1][S7].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (homepage, verbatim-short): "Build with our open-weight agentic coding models" — https://poolside.ai [S12]
- repo one-liner: "pool is Poolside's coding agent that runs in your terminal or integrates with any ACP-compatible editor" — https://github.com/poolsideai/pool [S1][S3]
- docs one-liner: pool can read code, answer questions, propose changes, edit files, run commands, use MCP servers and skills — https://docs.poolside.ai/cli/pool [S2]
- maker claims (paraphrased):
  1. pool is the same harness Poolside uses internally for agent RL training/evaluation, released as a research preview; "best agent experience" for Laguna models [S23] (2026-04-28).
  2. Open agent specs by design: AGENTS.md, Agent Skills, MCP, ACP (server and client) [S1].
  3. Dual ACP role: runs inside any ACP editor *and* can drive other agents (Claude Agent, Codex) as a client, including remote ACP over streamable HTTP [S1].
  4. Model freedom: Poolside-hosted Laguna, OpenRouter, Ollama, any OpenAI-compatible endpoint; Laguna is open-weight, runs locally (XS on a 36 GB Mac / single GPU; S on one DGX Spark) [S1][S23][S24].
  5. Control: approval modes incl. classifier-based Auto, plan mode with forced review, Docker sandbox, allow/deny tool and path rules [S1][S9].
  6. Company-level: "frontier-class reasoning at mid-size cost"; "The West needs open-weight models" (Warner); models free for a limited time [S12][S37][S11].
  7. Enterprise/government: run inside your own security boundary — on-prem, air-gapped, IL5-deployable, ATO achieved, no per-token fees, full weights [S21][S31].
- audience: developers ("Build with our open-weight agentic coding models"; free developer platform) [S12][S6]; enterprises/regulated industries and public sector needing self-managed inference [S10][S21][S31].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Poolside, Inc. (Delaware; 548 Market St, PMB 53385, San Francisco) [S20]; Poolside Federal LLC for public sector [S21]
- HQ: San Francisco, USA; engineering presence in Paris/France and UK [S27][S32]
- size: ~150 employees (Dec 2025, Wikipedia) [S27]; ~60-person Applied Research team (maker, Apr 2026) [S23]; Nvidia offers to >100/109 staff (Aug 2026 press) [S30][S32]
- funding stage: late private; $626M raised through Series B (Oct 2024, $3B); $12B valuation with Nvidia (Oct 2025 report; Aug 2026 $1B at $12B pre-money plus $6B license) [S26][S27][S30][S38]
- publicly named leadership (as the company names them):
  - Jason Warner — CEO & Co-founder (poolside.ai/vision); "co-CEO" in the 2026-04-28 launch byline and VentureBeat [S42][S23][S37]
  - Eiso Kant — CTO & Co-founder (poolside.ai/vision); "co-CEO" in the 2026-04-28 launch byline [S42][S23]
  - Philip Drury — Chief Investment Officer (newsroom item 2025-07-28) [S14]
  - Pengming Wang — co-head of applied research (VentureBeat quote, 2026-07-21) [S37]
  - Andy Appleton — Product Engineering Lead (byline, Desktop Assistant post 2026-07-28) [S28]
  - Head of product / DevRel / partnerships lead: none named on poolside.ai pages reviewed — researched, absent.
- contact: government page lists Poolside Federal LLC identifiers and AWS contract route [S21]; docs support pages (standard/premium) at https://docs.poolside.ai/support/overview [S10]

## 6. Open questions / conflicts

- Existing census `license: "Proprietary"` / `source_available: False` — confirmed for the CLI; note models are open-weight (OpenMDW-1.1 / Apache-2.0) [S4][S8].
- Existing census `source_code_url: null` — a public repo exists (https://github.com/poolsideai/pool) but holds binaries/changelog only; suggest recording the URL with "binaries only" [S1][S3].
- Existing census `first_released: "2024"` — pool CLI 1.0.0 shipped 2026-04-28; "2024" is the company's earlier "Poolside Enterprise Assistant" era (VS Code extension released 2025-03-25) [S5][S34]. Field is ambiguous; the CLI date is 2026-04-28.
- Existing census `current_release: "2026"` — v1.0.16, 2026-08-14 [S3].
- Existing census `mcp_support/plugin_support/claude_code_plugin/subagents/hooks/plan_mode: null` — filled in section 3 (client / skills-only / no / True / True / True).
- Existing census `model_providers` lists "Laguna S 2.1 118B/1M context, Laguna XS 2.1 33B on-device), OpenRouter, Vercel AI Gateway" — CLI docs also list Laguna M.1, Ollama, and any OpenAI-compatible endpoint; Vercel AI Gateway is a model distribution channel, not a CLI login option [S6][S8][S1].
- Existing census `install_method: "Desktop app and CLI; get started at .../get-started"` — CLI install is a curl script; Desktop is macOS Apple Silicon only [S6][S16].
- Existing census `pricing: null` — free developer tier "for a limited time" with training-on-content default; OpenRouter per-token; enterprise subscription [S11][S20][S24].
- Existing census `stars: null` — 408 [S3]. `language: null` — GitHub reports null (no source).
- Existing census `what_makes_it_special` says "agent runtime (research preview)" — homepage shows "Poolside Runtime" version 1.0.6 [S12]; the April post called pool itself the research preview [S23]. Whether "research preview" still applies in Aug 2026 is unclear (docs carry no such label).
- Title conflict: Wikipedia infobox lists Jason Warner as "President"; poolside.ai/vision says CEO; April 2026 launch byline says "co-CEOs" for Warner and Kant [S27][S42][S23]. Newcomer refers to "three co-founders" (third not named in accessible text) [S30].
- Project Horizon: the official blog URL https://poolside.ai/blog/announcing-project-horizon returned 404 on 2026-08-21; facts taken from press; one 2026 article claims the CoreWeave partnership collapsed — unverified [S40].
- Nvidia deal (Aug 20-21 2026): reported by Newcomer/Bloomberg from an investor letter; no Poolside press release found as of 2026-08-21 [S30][S32].
- Newsroom page content appears stale (latest item 2025-07-28) [S14].
- Leaderboard: Poolside reports Terminal-Bench 2.1 numbers but the public tbench.ai 2.1 leaderboard showed no Poolside/pool row [S18][S24].
- Paywalled/unreachable: newcomer.co full text (paywall); datacenterdynamics.com (403); poolside.ai/blog/announcing-project-horizon (404); docs legal index gives no entity details (Terms of Use used instead).

## 7. Sources

1. [S1] https://github.com/poolsideai/pool (README via GitHub API) — modes, install, approval modes, hooks, subagents, ACP server/client, MCP, config
2. [S2] https://docs.poolside.ai/cli/pool — CLI overview, v1.0.16, features list
3. [S3] https://api.github.com/repos/poolsideai/pool (+releases, contributors, commits, search/issues); [S3-org] https://api.github.com/orgs/poolsideai/repos — stars/forks/dates, org repos (acp-go-sdk, bridge-sdk, homebrew-tap)
4. [S4] https://github.com/poolsideai/pool/blob/main/LICENSE.md — all rights reserved, EULA link
5. [S5] https://github.com/poolsideai/pool/blob/main/CHANGELOG.md — 1.0.0 2026-04-28; 1.0.16 notes (hooks, auto mode, subagents)
6. [S6] https://docs.poolside.ai/cli/install — install commands, auth options, free developer access
7. [S7] https://docs.poolside.ai/cli/cli-reference — commands, flags, `pool acp serve`, slash commands, config paths
8. [S8] https://docs.poolside.ai/get-started/supported-models — Laguna specs, licenses, HF availability
9. [S9] https://docs.poolside.ai/permissions — approval modes, default mode, plan/build, rules, sandbox
10. [S10] https://docs.poolside.ai/llms.txt ; https://docs.poolside.ai/get-started/overview — docs index, platform description, integrations list
11. [S11] https://poolside.ai/models — model specs, benchmarks, "free to use for a limited time", pool v1.0.6 mention
12. [S12] https://poolside.ai ; https://poolside.ai/get-started — tagline, products, get-started options, chat.poolside.ai
13. [S13] https://docs.poolside.ai/mcp-servers — MCP client transports, config, auth
14. [S14] https://poolside.ai/blog ; https://poolside.ai/newsroom — post list/dates (Desktop 2026-07-28, Platform 2026-05-05, Dell, AWS, Fern Labs, $500M), CIO appointment; [S14b] https://docs.poolside.ai/subagents — subagent types/limits
15. [S15] https://docs.poolside.ai/skills — Agent Skills format, directories
16. [S16] https://docs.poolside.ai/tools/poolside-assistant-desktop — desktop ACP client, bundles pool, macOS Apple Silicon; [S16b] https://docs.poolside.ai/hooks — six events, command hooks
17. [S17] https://agentclientprotocol.com/get-started/agents — Poolside listed in ACP agents directory
18. [S18] https://www.tbench.ai/leaderboard/terminal-bench/2.1 — no Poolside rows
19. [S19] https://docs.poolside.ai/agent-instructions — AGENTS.md locations, no CLAUDE.md
20. [S20] https://poolside.ai/eula (serves Terms of Use) — Poolside, Inc., Delaware, address, products covered, training on content
21. [S21] https://poolside.ai/government — IL5, ATO, partner logos, Poolside Federal LLC, named quotes
22. [S22] https://www.usagepricing.com/blueprint/poolside — third-party pricing roundup (OpenRouter rates, free-tier terms)
23. [S23] https://poolside.ai/blog/introducing-laguna-xs2-m1 — 2026-04-28 launch, co-CEO byline, pool research preview, ~60-person research team
24. [S24] https://poolside.ai/blog/introducing-laguna-s-2-1 — 2026-07-21, benchmarks, OpenMDW-1.1, OpenRouter pricing, pool CLI, integrations
25. [S25] https://huggingface.co/api/models?author=poolside — HF download/like counts
26. [S26] https://techcrunch.com/2024/10/02/ai-coding-startup-poolside-raises-500m-from-ebay-nvidia-and-others — Series B $500M at $3B, investors
27. [S27] https://en.wikipedia.org/wiki/Poolside_AI — founding, HQ, ~150 staff, funding timeline, customers (DoD, RTX), Project Horizon
28. [S28] https://poolside.ai/blog/introducing-poolside-desktop-assistant — 2026-07-28, byline, bundles pool, third-party agents
29. [S29] https://www.marktechpost.com/2026/04/28/poolside-ai-introduces-laguna-xs-2-and-m-1-... (via search) — M.1/XS.2 benchmark numbers
30. [S30] https://www.newcomer.co/p/sources-poolside-strikes-6-billion — $6B license + $1B at $12B (2026-08-20); paywalled
31. [S31] https://poolside.ai/blog/introducing-the-poolside-platform — 2026-05-05, enterprise platform positioning, Hunted Labs quote
32. [S32] https://finance.yahoo.com/technology/ai/articles/nvidia-pay-poolside-6-billion-181448803.html (Bloomberg syndication) — >100 staff offers, independence, US + Paris
33. [S33] https://poolside.ai/blog/announcing-our-500-million-fundraise-to-make-progress-towards-agi (listed on blog index) — $500M raise 2024-10-02
34. [S34] https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery (publisher poolside-ai) — extension installs and dates
35. [S35] https://github.com/getpaseo/paseo (public-docs/supported-providers.md; packages/app/src/data/acp-provider-catalog.ts) — Paseo runs `pool acp`
36. [S36] https://github.com/poolsideai/homebrew-tap (Formula/pool.rb) — placeholder formula
37. [S37] https://venturebeat.com/infrastructure/poolside-drops-laguna-s-2-1-... — company context, co-CEO quotes, Pengming Wang title, 4,096 H200s
38. [S38] web search (techstartups, DCD, fxleaders, CoreWeave press release) — Nvidia up to $1B at $12B (Oct 2025); Project Horizon 2 GW, 40k GB300
39. [S39] web search (getlatka/tracxn/sacra summary) — "$2B Series C fell apart by April 2026" (third-party, unverified)
40. [S40] https://tech-insider.org/poolside-ai-project-horizon-coreweave-2gw-texas-collapse-2026/ (via search) — claims CoreWeave exit; unverified
41. [S41] https://codexpedite.com/pool-by-poolside-... (via search) — third-party review
42. [S42] https://poolside.ai/vision — CEO/CTO titles, mission, RL-from-code-execution claim

## Inclusion check (Jesse's test)

**Yes** — `pool` is Poolside's own coding agent with its own agentic loop (reads/edits files, runs shell, subagents, hooks, plan/build modes) that defaults to Poolside's hosted Laguna models but runs on any OpenAI-compatible endpoint; it can additionally act as an ACP client for other agents, but that is an optional mode, not its core [S1][S2][S23].
