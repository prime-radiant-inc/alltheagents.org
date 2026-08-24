# Dossier: VT Code (census_slug: vt-code)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (see section 7) and an as-of date. Small individual project — research kept proportionate.

## 1. Identity

- name: VT Code (repo styled "VTCode", binary/crate `vtcode`)
- maker: individual — GitHub user **vinhnx**, public profile name "Vinh Nguyen", location listed "Chau Doc, An Giang. Vietnam" [S2] (as-of 2026-08-24). No company entity found (researched, absent).
- product URL: https://github.com/vinhnx/VTCode (repo homepage field points to the wiki: https://github.com/vinhnx/VTCode/wiki) [S1]
- repo URL: https://github.com/vinhnx/VTCode
- license: first-party code "MIT OR Apache-2.0" (README License section; Homebrew formula license field agrees; GitHub API detects Apache-2.0 only) [S3][S1][S8] (as-of 2026-08-24)
- open source? True. source_available: True — full source in the repo; core is also published as reusable crates (`vtcode`, `vtcode-core`, `vtcode-config`, etc. on crates.io) [S5][S3]
- first public release: repo created 2025-08-29 [S1]; first GitHub release v0.1.2 published 2025-09-12 [S4]; first crates.io publish 2025-09-18 [S5]; first npm publish 2025-09-23 [S6]. Author called it a "research preview" in Show HN posts Oct 2025 [S12].
- latest release: v0.147.2, 2026-08-24 (GitHub release; crates.io newest 0.147.2 same day). 519 GitHub releases and 453 crates.io versions to date — near-daily, often multiple per day [S4][S5] (as-of 2026-08-24).
- what it is:
  - Form factor: terminal CLI/TUI only (interactive Ratatui TUI plus `ask`/`exec`/`review` one-shot CLI modes; headless `--full-auto`); a Zed editor extension exists in-repo as an ACP configuration package [S3][S13] (as-of 2026-08-24).
  - Models: BYO, multi-provider — "30 built-in providers" (Anthropic, OpenAI, Gemini, Meta, Z.AI, Moonshot/Kimi, Mistral, Qwen, DeepSeek, xAI, NVIDIA NIM, OpenRouter, GitHub Copilot, Poolside, etc.), custom OpenAI-compatible endpoints, and local inference via Ollama / LM Studio / llama.cpp (labeled experimental) [S3] (as-of 2026-08-24).
  - Pricing: free, open source; user supplies own API keys / OAuth logins; donations via GitHub Sponsors and Buy Me a Coffee [S3].
  - Install: `curl … scripts/install.sh | bash` (native installer, also installs ripgrep + ast-grep), `brew install vinhnx/tap/vtcode` (a `vtcode` formula also exists in homebrew/core), `cargo install vtcode`; npm package `vtcode` exists but last published 2025-12-24 (v0.52.8, far behind current) [S3][S8][S6] (as-of 2026-08-24).
  - Default autonomy: "keeps tool execution and provider access explicit"; restricted shell sandbox, tool guardrails, subprocess isolation, audit logging; per-workspace approval before workspace-defined lifecycle hooks may run shell commands; `providers_whitelist` restricts which LLM endpoints are reachable; `--full-auto` and `exec` grant full tool access for unattended runs [S3] (as-of 2026-08-24; maker-described, not independently tested).
  - Language: Rust (GitHub API) [S1].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 821 | 2026-08-24 | [S1] | independently observable |
| GitHub forks | 79 | 2026-08-24 | [S1] | independently observable |
| GitHub watchers (subscribers) | 8 | 2026-08-24 | [S1][S11] | independently observable |
| GitHub open issues | 1 (289 issues ever filed; 445 PRs ever) | 2026-08-24 | [S1][S10] | independently observable |
| Contributors (incl. anon) | 27; vinhnx has 6,486 of ~7,4xx commits (~87%); next-largest human contributor 52 commits | 2026-08-24 | [S9] | independently observable |
| Commit cadence, last 90 days (since 2026-05-26) | 1,727 commits | 2026-08-24 | [S1] | independently observable |
| Release cadence | 519 GitHub releases in ~11.5 months (first 2025-09-12); 3 releases 2026-08-22..24 alone | 2026-08-24 | [S4] | independently observable |
| crates.io downloads, `vtcode` | 28,819 all-time; 2,915 recent (~90d) | 2026-08-24 | [S5] | independently observable |
| crates.io downloads, `vtcode-core` | 35,831 all-time; 4,524 recent (~90d) | 2026-08-24 | [S5] | independently observable |
| Homebrew core formula installs (`vtcode`) | 163 (30d, rank ~2,789) / 426 (90d) / 2,067 (365d). Note: `vinhnx/tap` installs are not counted by these analytics | 2026-08-24 | [S8] | independently observable |
| npm downloads, `vtcode` | 11/week, 366/month; package stale since 2025-12-24 | 2026-08-24 | [S7] | independently observable |
| GitHub release-asset downloads | single digits per asset per release (e.g. v0.147.0 totals ~40 across all assets) — the curl installer and brew/cargo are evidently the delivery paths, or usage is very low | 2026-08-24 | [S4] | independently observable |
| GitHub Discussions | enabled; 3 discussions total | 2026-08-24 | [S11] | independently observable |
| GitHub Sponsors | 3 current sponsors (README shows 4 avatars incl. codemod, coderabbitai) | 2026-08-24 | [S11][S3] | independently observable |
| Hacker News | ~10 Show HN submissions by the author 2025-10..2026-05; best: 18 points/2 comments (2026-04-25), 16 points/6 comments (2026-05-30); rest ≤6 points | 2026-08-24 | [S12] | independently observable |
| Ecosystem listing: Paseo | listed in Paseo's supported ACP providers catalog ("VT Code, open-source multi-provider coding agent") | 2026-08-24 | [S14] | independently observable |
| Third-party coverage | vibecodinghub.org review page; DeepWiki/Context7/repo-explainer auto-generated pages; SourceForge mirror; no mainstream press found | 2026-08-24 | [S15] | independently observable (low-signal) |
| Maker usage claims | none found — the author's launch/blog posts state no user or usage numbers | 2026-08-24 | [S13] | researched, absent |
| Funding / customers / community server | none found (no Discord/Slack linked in README; no funding; donations only) | 2026-08-24 | [S3] | researched, absent |
| Benchmark placements | none found (no SWE-bench / Terminal-Bench entries located) | 2026-08-24 | [S12][S15] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** (verified in docs: `[mcp]` config, stdio/http/sse transports, allowlists, `/mcp` slash command, connection pooling, tool discovery). README claims "MCP client/server" but no server-mode documentation was found; the `vtcode-mcp` module doc describes client only. Treat "server" as maker-claimed/unverified [S3][S16][S17] (as-of 2026-08-24). Evidence: https://github.com/vinhnx/VTCode/blob/main/docs/guides/mcp-integration.md
- plugin_support: **True** — two layers: (a) Agent Skills — open `SKILL.md` format (agentskills.io), discovered from `<repo>/.agents/skills`, `~/.agents/skills`, `/etc/codex/skills`, bundled system skills; honors disable entries in `~/.codex/config.toml`; (b) Agent Plugins — the agent-plugins.org portable package format (`plugin.json` + skills + `mcp.json`), managed via `vtcode plugins add/list/info`, discovered from `.agents/plugins/` and `~/.agents/plugins/`; example first-party plugin repo vinhnx/vtcode-plugins. No marketplace of its own [S18][S19] (as-of 2026-08-24). Evidence: https://github.com/vinhnx/VTCode/blob/main/docs/guides/agent-plugins.md
- claude_code_plugin: **partial** — it consumes the same open Agent Skills `SKILL.md` format that Claude Code skills use, and its lifecycle hooks are modeled on Claude Code's ("Similar to Claude Code Hooks" with a link to Anthropic docs), but it reads `.agents/` and `~/.codex/` paths, not `.claude/` dirs, and does not implement the Claude Code plugin/marketplace format [S18][S20] (as-of 2026-08-24).
- subagents: **True** — subagents listed as core extensibility; `/plan` plan agent hands off to build/auto agents; full-automation harness uses propose/verify sub-agent separation (`SubagentController::verify_proposed_change()` spawns a fresh read-only verifier with no shared context) [S3][S21] (as-of 2026-08-24). Evidence: https://github.com/vinhnx/VTCode/blob/main/docs/guides/full-automation.md
- hooks: **True** — lifecycle hooks in `vtcode.toml` under `[hooks.lifecycle]` (session_start, pre_tool_use with matchers, etc.); can enrich context, enforce policy, or block operations; workspace-defined hooks need per-workspace approval before running shell commands [S20][S3] (as-of 2026-08-24). Evidence: https://github.com/vinhnx/VTCode/blob/main/docs/guides/lifecycle-hooks.md
- plan_mode: **True** — `/plan` command with a `plan` primary agent; iterate on a build plan, then hand off to `build`/`auto` agents through a structured review gate [S3][S22]. Evidence: https://github.com/vinhnx/VTCode/blob/main/docs/guides/planning-workflow.md
- plugin_docs_url: https://github.com/vinhnx/VTCode/blob/main/docs/guides/agent-plugins.md (skills: https://github.com/vinhnx/VTCode/blob/main/docs/skills/SKILLS_GUIDE.md)
- config_docs_url: https://github.com/vinhnx/VTCode/blob/main/docs/config/CONFIG_FIELD_REFERENCE.md
- ACP support: **yes, first-party** — built-in ACP bridge launched with `vtcode acp`, configured via `[acp]`/`[acp.zed]` in `vtcode.toml`; modeled on Zed's reference implementations; an in-repo Zed extension packages it; this is how Paseo drives it [S23][S13][S14] (as-of 2026-08-24). Evidence: https://github.com/vinhnx/VTCode/blob/main/docs/guides/zed-acp.md
- Other protocols (maker-listed): Open Responses, Agent2Agent (A2A), ATIF, Anthropic Messages API compatibility server [S3].
- SDK: **partial** — no packaged agent SDK, but the core is published as reusable Rust crates (`vtcode-core` "modular architecture … ecosystem reuse", `vtcode-config`) on crates.io with docs.rs docs [S5][S13].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo description, verbatim): "VT Code is an open-source Rust terminal coding agent." [S1]; README demo caption: "Secure, open, universal." [S3]
- README one-paragraph claim: an open-source Rust terminal coding agent for interactive and long-running autonomous workflows — responsive TUI, safe terminal tools, multi-provider LLM support, open protocols, extensible Skills, "from a question to a reviewed change without leaving your terminal" (paraphrase) [S3].
- maker claims (paraphrased):
  1. Multi-provider freedom: 30 built-in providers + OpenAI-compatible endpoints + local inference (Ollama/LM Studio/llama.cpp), no vendor lock-in [S3][S13].
  2. Open-protocol interoperability: MCP, ACP, Agent Skills, Agent Plugins, Open Responses, A2A, ATIF, Anthropic Messages API [S3].
  3. Safety as architecture: restricted shell sandbox, tool guardrails, subprocess isolation, audit logging, hook approval, provider whitelist ("defense-in-depth security … rather than warnings") [S3][S13].
  4. Semantic code understanding: Tree-sitter + ast-grep symbol maps, code intelligence, project indexing — structural refactoring, not text manipulation [S12][S13][S3].
  5. Loop engineering for unattended work: worktree isolation for parallel agents, propose/verify sub-agent separation, durable loop state, cost guardrails [S3].
  6. Planning workflow with a review gate: `/plan` agent → structured handoff to build/auto [S3].
  7. Rust engineering posture: modular crates, "infrastructure, not experiments", sustainability over prototyping [S13].
  8. Context management: automated summarization, phase-aware tool curation, real-time token budgeting for long sessions [S13].
- audience: developers who want a terminal-first agent for "both interactive development and unattended work" [S3]; HF post frames it for people building/operating serious local agent workflows [S13]. No team-size or stack claims (researched, absent).

## 5. Company & contact targets (PRI-2929)

- Not a company. Individual maintainer: GitHub **vinhnx** ("Vinh Nguyen", blog https://vinhnx.github.io, 597 followers), self-described "labor of love built in my spare time" [S2][S3] (as-of 2026-08-24). Per instruction, only the public repo identity is recorded; no employer, no personal contact details.
- Contact paths the project itself offers: GitHub issues/discussions, GitHub Sponsors page, security policy for advisories [S3].
- Funding stage: none/personal; donations via GitHub Sponsors (3 sponsors) and Buy Me a Coffee [S3][S11].

## 6. Open questions / conflicts

- Census `stars: "783"` — now 821 (2026-08-24) [S1]. Stale, not wrong.
- Census `current_release: "2026-08-19"` — v0.147.2 published 2026-08-24; 519 releases total [S4].
- Census `first_released: "2025-08-29"` — that is the repo creation date; the first tagged release is v0.1.2 on 2025-09-12 and the author still called it a research preview in Oct 2025 [S1][S4][S12]. Which counts as "first public release" is a definition call.
- Census `mcp_support: "yes (MCP client/server modes …)"` — README does say "client/server", but every doc found (mcp-integration guide, vtcode-mcp module doc) describes client mode only; no server-mode command or config located. Suggest recording client=verified, server=maker-claimed [S3][S16][S17].
- Census `claude_code_plugin: "no"` — defensible, but "partial" is arguably more accurate: it consumes the open Agent Skills SKILL.md format (shared with Claude Code) and its hooks are explicitly modeled on Claude Code's; it does not read `.claude/` dirs or the plugin/marketplace format [S18][S20].
- Census `plugin_docs_url: null` / `config_docs_url: null` — both exist; filled in section 3.
- Census `install_method: "curl install script, brew, cargo"` — correct; note brew is both `vinhnx/tap/vtcode` (README) and a `vtcode` formula in homebrew/core [S3][S8]. npm `vtcode` exists but is 8 months stale — not a current install path [S6].
- Census `model_providers: "30+ built-in"` — README says exactly "30 built-in providers" [S3].
- Census `homepage: wiki` — repo homepage field is the wiki; there is no standalone product site (vinhnx.github.io is a personal blog; the Homebrew formula's homepage field points there) [S1][S8].
- Census `sources: jqueryscript / brad / ishandutta` — none of these could be resolved to specific reachable articles; found instead: vibecodinghub.org review, HN threads, HF blog. jqueryscript's relevant property is the awesome-claude-code list [S15][S12]. Unverified census sources.
- Release-asset downloads (single digits) vs crates.io ~29k downloads: crates.io counts include CI/mirror noise and `cargo install` builds from source; true user count is unknowable from public data but all signals point to a small user base (brew 163/30d, HN ≤18 points, 3 discussions).
- Commit count 1,727/90d is inflated by a release bot (746 lifetime commits) and near-daily version-bump releases; still an unusually active solo cadence.
- Zed extension "Ready for marketplace submission" (in-repo STATUS.md) — whether it is actually published on the Zed marketplace was not verified [S23-STATUS].

## 7. Sources

1. [S1] https://api.github.com/repos/vinhnx/VTCode — stars, forks, dates, license, language, homepage
2. [S2] https://api.github.com/users/vinhnx — maker public identity
3. [S3] https://raw.githubusercontent.com/vinhnx/VTCode/main/README.md — features, install, safety, license, sponsorship, claims
4. [S4] https://api.github.com/repos/vinhnx/VTCode/releases — 519 releases, asset download counts, first release v0.1.2
5. [S5] https://crates.io/api/v1/crates/vtcode and /vtcode-core — downloads, versions, dates
6. [S6] https://registry.npmjs.org/vtcode — npm package, stale since 2025-12-24
7. [S7] https://api.npmjs.org/downloads/point/last-week|last-month/vtcode — npm downloads
8. [S8] https://formulae.brew.sh/api/formula/vtcode.json — homebrew/core formula, license, install analytics
9. [S9] https://api.github.com/repos/vinhnx/VTCode/contributors — contributor distribution
10. [S10] https://api.github.com/search/issues?q=repo:vinhnx/VTCode — issue/PR totals
11. [S11] GitHub GraphQL (discussions, watchers, sponsors counts)
12. [S12] https://hn.algolia.com/api/v1/search?query=VT%20Code — Show HN submissions and scores
13. [S13] https://huggingface.co/blog/vinhnx90/vt-code — author's design-principles post, 2025-12-07
14. [S14] https://github.com/getpaseo/paseo (public-docs/supported-providers.md) — Paseo catalog listing
15. [S15] web search results — vibecodinghub.org/tools/vt-code review; DeepWiki/Context7/SourceForge auto-pages
16. [S16] https://github.com/vinhnx/VTCode/blob/main/docs/guides/mcp-integration.md — MCP client config
17. [S17] https://github.com/vinhnx/VTCode/blob/main/docs/modules/vtcode_mcp.md — MCP module = client
18. [S18] https://github.com/vinhnx/VTCode/blob/main/docs/skills/SKILLS_GUIDE.md — Agent Skills discovery paths
19. [S19] https://github.com/vinhnx/VTCode/blob/main/docs/guides/agent-plugins.md — Agent Plugins format, vtcode plugins CLI
20. [S20] https://github.com/vinhnx/VTCode/blob/main/docs/guides/lifecycle-hooks.md — hooks config, "Similar to Claude Code Hooks"
21. [S21] https://github.com/vinhnx/VTCode/blob/main/docs/guides/full-automation.md — propose/verify subagents
22. [S22] https://github.com/vinhnx/VTCode/blob/main/docs/guides/planning-workflow.md — /plan review gate (linked from README; not fetched directly)
23. [S23] https://raw.githubusercontent.com/vinhnx/VTCode/main/src/lib.rs (rustdoc) + [S23-STATUS] extensions/zed-extension/STATUS.md — `vtcode acp` command, ACP bridge, Zed extension status

## Inclusion check (Jesse's test)

**Yes** — VT Code is a genuine agent with its own agentic loop implemented in Rust (own tool registry, provider layer, planner/build/auto agents, propose/verify subagents); its ACP mode (`vtcode acp`) exposes that native loop rather than wrapping another vendor's agent [S3][S23].
