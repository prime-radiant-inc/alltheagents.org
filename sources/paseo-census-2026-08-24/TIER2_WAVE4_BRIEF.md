# Tier-2 wave-4 harness brief (for Eden) — 2026-08-24

Thirteen small(er) harnesses, one compact block each. Everything traces to dossiers/<slug>.md and standardized/<slug>.md; rows in rows_wave4.tsv. "Observable" = measured ourselves; "maker-claimed" = the maker said it. Only autohand-code-cli is already in the census; the other twelve are proposed NEW entries (nova as nova-compass), and one fails the inclusion test outright.

## Autohand Code CLI (Autohand AI, New Zealand)
- What it is: TypeScript/Bun terminal agent (VS Code extension, native --acp, iOS pairing, /squad multi-agent) from a one-person company (Igor Costa, ~96% of commits); "Apache-2.0" with an ARR-gated commercial carve-out — dual licensing in practice; BYO multi-provider.
- Adoption reality: 178 stars, ~4.8k npm/week, 189 VS Code installs, 1-point HN. No maker numbers exist.
- How it plugs in: MCP client; skills + Code Extensions + community registry; partial Claude skill-format compat; subagents; plan mode; ACP twice — a native --acp AND the stale Jan-2026 npm adapter Paseo actually catalogs.
- Maker says special: "self evolving" (auto-generates project skills from codebase analysis), ultra-fast Bun, iOS remote steering.
- Worth an opinion: (a) the installer silently clobbers any existing `agent` binary on PATH from any vendor — maker-documented; (b) ARR-gated "Apache"; (c) Paseo may be driving the dormant adapter, not the live --acp.
- Your take: ____

## CodeWhale (Hmbown, individual)
- What it is: MIT Rust terminal agent (TUI, exec, local web + mobile control) born as deepseek-tui in Jan 2026, rebranded provider-neutral in May; BYO across ~45 claimed providers or local Ollama/vLLM/SGLang; Plan/Ask/Auto-Review/Full-Access tiers, /undo snapshots.
- Adoption reality: 40,842 stars — top-tier by stars — but only ~20-30k downloads/month across channels and 4 HN points; strong Chinese-community base (WeChat, CNB mirror, 18 translations). Stars outrun everything else by two orders.
- How it plugs in: MCP client; skills + plugin.toml bundles + hooks + Fleet agent teams; a dedicated CLAUDE_PLUGIN_COMPAT.md that reads .claude/skills but refuses Claude plugin runtimes; first-party ACP inside its Runtime API.
- Maker says special: model freedom, visible control, community-improved in public, an "honesty posture" (unknown model prices stay unknown).
- Worth an opinion: (a) briefed as small — it is not; (b) whether 40.8k stars are organic; (c) the agent and its bot commit to their own repo.
- Your take: ____

## Crow / crow-cli (odellus, individual)
- What it is: MIT Python "Minimal ACP Agent", solo-built; every session in a shared local sqlite db with full-text search — persistence and multi-agent memory-sharing are the whole thesis; BYO OpenAI-compatible; needs Python 3.14 + uv + Docker (bundled SearXNG).
- Adoption reality: 56 stars, ~1k PyPI/month, 1 HN point, no community channel — minimal and early is the finding.
- How it plugs in: its own toolbox ships as an MCP server and external MCP servers mount alongside; SKILL.md skills (distribution unfinished); subagents via shared memory; no hooks, no plan mode; ACP first-party via the official Python SDK.
- Maker says special: "most agent toolkits treat persistence as an afterthought"; the sqlite file is the integration point.
- Worth an opinion: (a) default approval behavior undocumented; (b) the site's editor/skill-catalog framing runs ahead of the code; (c) a heavy prerequisite stack for "minimal".
- Your take: ____

## DimCode / DimAgent (arcships, Singapore-listed org)
- What it is: closed-source local-first "one agent runtime" — TUI, headless exec, Electron desktop with in-page annotation, dim acp — with NO published license anywhere (npm points to a LICENSE that does not exist); BYO 30+ providers, China-market heavy; Chinese-first site.
- Adoption reality: ~11.3k npm/month with 365 versions in 7 months; the 22-star GitHub repo is an issues-only dead-drop. Headline claims (98% KV-cache reuse, 20-hour runs) have no methodology.
- How it plugs in: MCP client; manifest-driven plugins; SKILL.md skills; subagents with per-subagent models and worktree/container sandboxes; claimed 15 hook points; enforced read-only plan mode (claimed); first-party ACP.
- Maker says special: cache-friendly context management as a cost story; reliable unattended runtime; local-first trust (SQLite + OS keychain).
- Worth an opinion: (a) shipping a proprietary binary with a dangling license pointer; (b) four names/domains for one product (DimCode/DimAgent/arcships/dimagent.com); (c) no company, team, or funding trace at all.
- Your take: ____

## Dirac (Max Trivedi, individual)
- What it is: Apache-2.0 TypeScript Cline soft-fork rebuilt around token efficiency — context curation, hash-anchored parallel edits, AST refactors, multi-file batching; CLI + VS Code + first-party ACP (JetBrains and Zed registries); BYO multi-provider; deliberately NO MCP ("Oh, and no MCP.").
- Adoption reality: 1,465 stars, ~2.2k npm/week, 1,226 VS Code installs; claims TB-2 65.2% with gemini-3-flash-preview (beating Google's own baseline) — submission title confirmed but the evidence link 403s and tbench.ai was not checked.
- How it plugs in: skills + AGENTS.md, auto-reads Claude skills from .ai/.claude/.agents; no subagents, no hooks; plan mode via -p; no SDK.
- Maker says special: 64.8% average API-cost cut at equal-or-better quality, with named-competitor eval diffs published in-repo (self-graded).
- Worth an opinion: (a) the only harness here that markets AGAINST MCP; (b) cost claim varies by surface (64.8% vs 50-80%); (c) evals disclose their own upstream cost-accounting bug — unusual candor.
- Your take: ____

## Nova (Compass Agentic Platform)
- What it is: closed-development enterprise CLI agent (npm @compass-ai/nova, codename Kore-CLI, private Azure DevOps) in a suite with Office-app agents; MIT-labeled minified bundle, no source; Compass plan-gated model proxy + Anthropic/OpenAI/Ollama; EUR40-500/seat/mo; "guarded execution" risk-tiered approvals; ACP + A2A first-party.
- Adoption reality: ~4.4k npm/month vs "500+ enterprise teams", SOC 2/ISO 27001 and a 99.9% SLA claimed on a site whose only contact is a gmail address. Nothing public corroborates; no named person anywhere.
- How it plugs in: MCP client with OAuth; SKILL.md skills and slash commands that mirror Claude Code's formats (its docs literally route skill installs through claude-code, then move the folder); subagents, hooks, /plan; no SDK (JSON-RPC tools server instead).
- Maker says special: production-repo focus, verification-first ("tests, not vibes"), one platform across terminal and Office.
- Worth an opinion: (a) the bundle ships OpenAI Codex CLI's OAuth client id and signs in to OpenAI as Codex — sanction unknown; (b) MIT label with zero source; (c) enterprise certifications with no auditor, customer, or entity behind them.
- Your take: ____

## fast-agent (evalstate / Shaun Smith, individual)
- What it is: Apache-2.0 Python MCP-native agent FRAMEWORK that also ships a usable coding-agent shell plus ACP/MCP/A2A server modes; BYO across all majors + local; derivative of mcp-agent, acknowledged.
- Adoption reality: 178k PyPI/month (CI-noisy) and 3.9k stars — the biggest footprint of the wave-4 open projects.
- How it plugs in: claims the most complete MCP support (sampling, elicitations); Agent Skills with three default registries (fast-agent, HuggingFace, Anthropic); subagents as ACP Modes; hooks via skills; qualified plan mode; it IS its own SDK.
- Maker says special: "The harness your model deserves. Same model, better results."; first/only-tool superlatives (unverified).
- Worth an opinion: (a) Paseo's catalog command launches the fast-agent-acp wrapper frozen in Feb 2026, pinning a ~6-month-old build — the live path is fast-agent-mcp; (b) framework-vs-agent categorization; (c) README MIT badge vs Apache-2.0 metadata.
- Your take: ____

## Minion Code (femto, individual)
- What it is: Python "minion's implementation of Claude Code" on the maker's own Minion framework; 12+ bundled tools, mcode acp for Zed; license conflicted (MIT per README/PyPI, AGPL-3.0 per GitHub); DORMANT since 2026-03-15.
- Adoption reality: 39 stars, ~500 PyPI/month — near zero, and shrinking relevance while Paseo still lists it live.
- How it plugs in: MCP client via JSON config; no skills/plugins, no subagents, no hooks, no plan mode, no Claude compat despite the name; ACP first-party.
- Maker says special: batteries included, one-line creation, built on a framework "that can do everything".
- Worth an opinion: (a) a five-word repo description carries the whole Claude Code positioning; (b) should the census carry a dormant near-zero-adoption provider at all; (c) the license conflict.
- Your take: ____

## GLM Agent / glm-acp-agent (stefandevo, individual, Belgium)
- What it is: Apache-2.0 TypeScript agent whose ONLY surface is an ACP stdio server — no CLI/TUI — locked to Zhipu/Z.AI GLM Coding Plan models; own 20-turn loop, 7 tools, graduated permission modes; third-party with no Zhipu endorsement.
- Adoption reality: ~9.7k npm/month on a 4-month-old solo package (notable), 43 stars; no maker claims.
- How it plugs in: hardwired Z.AI web/vision MCP only; no skills/plugins/subagents/hooks/plan mode; thinking-mode chain-of-thought visibility is the party trick.
- Maker says special: the community bridge putting GLM Coding Plan subscriptions into ACP editors — a native loop, not a wrapper.
- Worth an opinion: (a) the purest single-model, single-protocol agent in the census; (b) whether arbitrary MCP servers work is unverified; (c) an ecosystem signal about ACP enabling one-person model-bridges.
- Your take: ____

## siGit Code (PT Sigit Mitra Bangun, ID + Splitfire AB, SE)
- What it is: Apache-2.0 Rust local-only agent with its own on-device GGUF inference (Qwen 2.5/3 via "Onde") — no API keys, no cloud, period; ACP to Zed/Xcode/VS Code; tied to the maker's smbCloud git-hosting ecosystem; ~5 months old.
- Adoption reality: 32 stars, 341 crate downloads, 450 npm/week; ~4.6k release-asset downloads that look CI-driven (macOS exactly 0). Effectively pre-adoption.
- How it plugs in: MCP client via mcp.toml; nothing else — no skills, subagents, hooks, or plan mode; ACP is central.
- Maker says special: fully local and private by construction; "more useful" on the maker's own git hosting.
- Worth an opinion: (a) the only harness in the census shipping its own local inference as the ONLY model path; (b) README install claims (brew/pip/uv) don't check out; (c) a "claude" bot is its #3 committer.
- Your take: ____

## Stakpak (Egyptian-founded; acquired by Vercel 2026-07)
- What it is: Apache-2.0 Rust DevOps agent — 24/7 autopilot on your own machines (incident healing, cert/secret maintenance) with a Warden/Cedar sandbox and 210+-type secret substitution; BYO or hosted key; first-party ACP; releases stopped 2026-06-10 around the Vercel acquisition.
- Adoption reality: 1,748 stars, 66k release-asset downloads (CI-inclusive), "5,000+ developers" + a logo wall (Mistral AI, Writer, Vectara) maker-claimed; the acquisition itself is the strongest signal.
- How it plugs in: MCP server + multiplexing proxy (plain client mode unconfirmed); Rulebooks (markdown SOPs) instead of plugins; subagents; no hooks; partial plan mode.
- Maker says special: security-first autonomous operations, on-prem, no cloud lock-in.
- Worth an opinion: (a) whether the OSS agent survives inside Vercel — maintained is best recorded "acquired"; (b) the only DevOps-specialized entry in this wave; (c) security marketing vs an agent designed to run unattended with prod credentials.
- Your take: ____

## Corust Agent (Corust AI)
- What it is: Rust-language-specialized agent on the maker's own Rust-fine-tuned model — Zed ACP extension + TUI + GitHub PR reviewer, free "without limits"; GPL-3.0 LICENSE on a binaries-only repo with NO source anywhere (proprietary in practice); homepage corust.ai has no DNS A record as of 2026-08-24; no release since 2026-05-13.
- Adoption reality: 47.6k release-asset downloads (Zed auto-download inflated), 31 stars, zero maker claims/funding/press. All marketing claims survive only in search-index snippets.
- How it plugs in: unknowable — docs unreachable, artifacts are binaries; ACP first-party is the one certainty.
- Maker says special: "zero hallucinations on Rust idioms" (no evidence), one model across three surfaces.
- Worth an opinion: (a) likely dying or dead — re-verify before publishing; (b) GPL text without source is a license violation in waiting; (c) the census specialization enum has no Rust-language value.
- Your take: ____

## Agoragentic (pseudonymous "Rhein1") — FAILS INCLUSION
- What it is: not a coding agent. An MIT stdio MCP relay (zero deps, calls no LLM) into a closed hosted marketplace of paid agent services settled in USDC via x402 micropayments, with governance framing ("control and proof"); --acp re-exposes the same six marketplace tools over ACP with no agent behind them.
- Adoption reality: 1k npm/week (automation-dominated); the site's own counters — 84 listings, 1,164 lifetime calls — are the honest scale; purchasing is currently frozen.
- Verdict: fails Jesse's test (no loop, no LLM, edits no files). Recommend exclusion, or a non-agent marketplace annex; also fix the "174+ AI capabilities" figure floating in the Paseo framing — the site says 84.
- Worth an opinion: whether Paseo should list ACP-protocol-compliant non-agents at all.
- Your take: ____

## Cross-dossier notes
- Inclusion: 12 of 13 pass Jesse's test; Agoragentic fails outright (relay, no loop, no LLM). Corust passes only on presentation — its loop is uninspectable. Autohand's Paseo-cataloged npm adapter would fail alone but wraps Autohand's own agent.
- License mess is the wave's theme: Autohand (Apache + ARR gate), DimCode (no license at all), Nova (MIT label, no source), Minion Code (MIT vs AGPL conflict), Corust (GPL text, binaries only). Only CodeWhale, Crow, Dirac, fast-agent, GLM Agent, siGit, and Stakpak are cleanly open.
- Dormancy/death watch: Minion Code (silent since 2026-03), Corust (since 2026-05, homepage DNS dead), Stakpak (releases stopped 2026-06, acquired), Autohand's ACP adapter (Jan 2026). Paseo lists all four paths as live.
- Stale-launcher pattern: Paseo drives fast-agent through a wrapper frozen in February and Autohand possibly through a dormant adapter — worth a Paseo-side audit of catalog commands vs current vendor docs.
- Solo-maintainer share: 8 of 13 are individuals (CodeWhale, Crow, Dirac, fast-agent, Minion Code, GLM Agent, Agoragentic, and Autohand-in-practice); none of the 13 has any disclosed funding; the only named executives in the whole wave are Igor Costa and (via acquisition press) George Fahmy.
- ACP is first-party in all 13 — this wave exists because of ACP — but three are ACP-only surfaces (GLM Agent, Corust, and Agoragentic's hollow relay), a new form factor the census platforms field should represent.
- Scale check: nothing here has a single public benchmark row except Dirac's contested TB-2 submission; the largest real open-source footprint is fast-agent (178k PyPI/month), the largest star count CodeWhale (40.8k, uncorroborated), and everything else is under ~12k downloads/month.
