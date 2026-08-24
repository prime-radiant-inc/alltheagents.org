# Dossier: Auggie CLI (census_slug: auggie)

Compiled 2026-08-21/22. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Each non-obvious fact carries a source [Sn] (section 7) and an as-of date.

Subject note: the dossier subject is **Auggie**, Augment Code's agent/CLI (the thing Paseo drives via `auggie --acp`). Augment also ships IDE extensions, the Cosmos cloud platform, Code Review, Context Engine services, and the "Intent" desktop workspace; facts below are tagged with the surface they apply to. The same Augment agent underlies the CLI and Cosmos cloud sessions (permissions, hooks and settings are shared) [S8][S9].

## 1. Identity

- name: Auggie (product pages say "Auggie CLI"); npm `@augmentcode/auggie` [S1][S5]
- maker: Augment Code — legal name on the CLI license: "Augment Computing, Inc." [S3]; press releases use "Augment Inc." / brand "Augment Code" [S20]. Company; HQ Palo Alto, CA, USA [S20] (as-of 2024-04-24 press release; no newer HQ statement found).
- product URL: https://www.augmentcode.com/ ; docs home for the CLI: https://docs.augmentcode.com/cli/overview [S2]
- repo URL: https://github.com/augmentcode/auggie [S4] — the repo contains README, CHANGELOG, LICENSE, SECURITY, examples, `.augment-plugin`, and a `plugin_marketplace/` directory; **no agent source code**. GitHub reports repo language "Shell" [S4] (as-of 2026-08-22).
- license: proprietary — "Custom Proprietary License for Augment CLI": use requires an active Augment subscription; redistribution, modification and reverse-engineering prohibited; distribution only via Augment's npm channel [S3] (as-of 2026-08-21). npm license field: "SEE LICENSE IN LICENSE.md" [S5].
- open source? False. source_available: False for the agent (npm ships a bundled `augment.mjs`; the GitHub repo is issues/examples/marketplace scaffolding) [S3][S4][S5]. Adjacent OSS exists: MIT GitHub Actions (augment-agent, review-pr, describe-pr), MIT Zed ACP extension (auggie-zed-extension), MIT context-connectors, and the MIT/NOASSERTION augment-swebench-agent research harness [S4] (as-of 2026-08-22).
- first public release (CLI): first npm publish 0.1.0 on 2025-07-31 [S5]; GitHub repo created 2025-09-08 [S4]; Augment's own retrospective says the CLI "launch[ed] in early September" 2025 [S16]. (The census `first_released: 2025-09-08` is the repo-creation date.)
- latest release (CLI): 0.36.0, published 2026-08-21 (npm dist-tag latest); 566 npm versions total incl. prereleases; 61 stable versions; cadence roughly one minor release every 1–2 weeks [S5] (as-of 2026-08-22). GitHub "releases" are build tags named `v1.2.0-prerelease.<timestamp>` several times a day and do **not** match npm version numbers [S4].
- what it is:
  - Form factor (Auggie): terminal CLI with an interactive TUI (Ink/React) [S16]; non-interactive `--print`/`--quiet`/`--output-format json` automation mode; `--acp` ACP agent mode; `--mcp` MCP **server** mode exposing the codebase-retrieval tool to other agents; GitHub Actions wrappers [S2][S13][S14][S1]. Platform context: VS Code + JetBrains + Vim/Neovim extensions ("Augment"), Cosmos cloud agents platform, Code Review, Intent desktop workspace (macOS) [S2-LLMS][S19][S22].
  - Models: multi-vendor menu curated by Augment (no BYO key found in docs): Claude (Fable 5, Opus 5/4.8–4.5, Sonnet 5/4.6/4.5, Haiku 4.5), GPT-5.x incl. 5.6 Sol/Terra/Luna, Gemini 3.1 Pro, GLM 5.2, Kimi K3/K2.6, Grok 4.6, plus "Prism" auto-routing bundles (Claude+Gemini, GPT) [S6][S7] (as-of 2026-08-21). Selected with `/model` or `--model` [S6].
  - Pricing: token-based — LLM tokens at provider public API list price + flat 40% service fee on LLM usage + Cosmos compute $0.19/hr (5-min increments). Business plan $100/month flat, up to 50 seats, $100 usage included, pay-as-you-go top-ups; Enterprise custom (SSO/OIDC/SCIM, CMEK, ISO 42001, data residency). SOC 2 Type II; "No AI training allowed" on paid plans [S7][S10] (as-of 2026-08-21). Auggie CLI use requires an active subscription per the license [S3].
  - Install: `npm install -g @augmentcode/auggie` (docs: Node 20+; README badge: Node 22+); macOS, Windows WSL, Linux; zsh/bash/fish; auto-updates itself by default in interactive mode [S11][S1]. `auggie login` (OAuth-style browser flow); session JSON via `auggie token print` / `AUGMENT_SESSION_AUTH` for CI [S12].
  - Default autonomy: **runs tools automatically** — docs warn "Auggie runs commands and tools automatically. Only use integrations and MCP servers from trusted sources" [S13]. No default ask-before-edit/shell mode is documented; control is via opt-in `toolPermissions` rules (allow/deny/webhook-policy/script-policy, regex on shell input, most-restrictive-wins across policies) in `~/.augment/settings.json`, `.augment/settings.json`, `/etc/augment/settings.json` and `--permission` [S8]. Approval prompts exist for sensitive paths (added 0.34.0) and first-run workspace indexing (`--allow-indexing` skips) [S15][S14]. Non-interactive mode can be disabled by enterprise agreement [S2].
  - Codebase context: workspace is auto-indexed into Augment's cloud "Context Engine" (semantic index; requires consent screen at first run) [S2][S11]; the current harness (v2, shipped ~Aug 2026) is a **fork of Pi** (Mario Zechner's open-source harness) with the Context Engine integrated via Pi's extension system [S18].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars (augmentcode/auggie) | 273 | 2026-08-22 | [S4] | independently observable |
| GitHub forks / watchers | 33 / 2 | 2026-08-22 | [S4] | independently observable |
| GitHub contributors | 12 (repo is scaffolding, not source) | 2026-08-22 | [S4] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 12 | 2026-08-22 | [S4] | independently observable |
| GitHub issues (open / closed) | 84 / 16; Discussions enabled | 2026-08-22 | [S4] | independently observable |
| npm weekly downloads, @augmentcode/auggie | 31,832 (2026-08-14..20) | 2026-08-20 | [S5b] | independently observable |
| npm monthly downloads | 164,605 (2026-07-22..08-20) | 2026-08-20 | [S5b] | independently observable |
| npm downloads by month | 2025-09: 46,921 → 2026-01: 91,616 → 2026-03: 154,891 → 2026-07: 165,910 (~3.5x since launch month; roughly flat Mar–Jul 2026) | 2026-08-20 | [S5b] | independently observable |
| npm weekly, @augmentcode/auggie-sdk | 2,795 | 2026-08-20 | [S5b] | independently observable |
| PyPI monthly, auggie-sdk | 3,573 | 2026-08-21 | [S5c] | independently observable |
| VS Code Marketplace installs (augment.vscode-augment) — **IDE extension, not the CLI** | 774,212 installs; 340 ratings avg 3.59; last updated 2026-08-10 | 2026-08-21 | [S23] | independently observable |
| JetBrains Marketplace downloads (plugin 24072 "Augment") — IDE extension | 702,554 | 2026-08-21 | [S24] | independently observable |
| Homebrew | no `auggie` formula or cask exists | 2026-08-21 | [S25] | independently observable (absent) |
| Zed extension (auggie-zed-extension repo) | 22 stars; Zed extensions API returned no data for "auggie" | 2026-08-22 | [S4][S26] | independently observable |
| Reddit r/AugmentCodeAI (official community per README) | member count not obtainable (Reddit API blocked) | 2026-08-22 | [S1] | null (not obtainable) |
| CLI adoption (maker) | "one of the fastest adoption curves in company history"; "more than half of the people who use the CLI use it as their primary agent" | 2025-12-18 | [S16] | maker-claimed |
| Funding | Series B $227M at $977M post-money (2024-04-24), total $252M (after $25M prior); investors Sutter Hill, Index, Innovation Endeavors, Lightspeed, Meritech; Eric Schmidt-backed | 2024-04-24 | [S20][S27] | maker-claimed (round) / press |
| Later funding rounds | none found (Tracxn/Crunchbase still show $252M total as of 2026) | 2026-08-21 | [S27] | independently observable (absent from public record) |
| Benchmark (maker-run): SWE-bench Pro | Auggie 51.80% on 731 problems, "highest of any agent tested"; self-run comparison vs Cursor, Claude Code, Codex all on Claude Opus 4.5; Scale's leaderboard SWE-Agent+Opus 4.5 = 45.89% | 2026-02-04 | [S17] | maker-claimed (self-run, public dataset) |
| Benchmark (maker-run): Terminal-Bench 2.0, Opus 4.7 head-to-head | Auggie 67.4% vs Claude Code 66.3% pass rate; 32% fewer tokens; 33% lower cost ($463 vs $695) | 2026-05-15 | [S18b] | maker-claimed (self-run) |
| Harness v2 (Pi fork) efficiency | same pass rate on SWE-bench Pro at $1.27/task vs Claude Code $2.70 (53% cheaper); v1 was 27% cheaper | 2026-08-14 | [S18] | maker-claimed (self-run) |
| Benchmark (earlier): SWE-bench Verified | "#1 open-source SWE-bench Verified implementation" (augment-swebench-agent, Claude 3.7 + o1); repo 881 stars | 2025-03-31 | [S28][S4] | maker-claimed (open harness) |
| Outcome claims on homepage (Cosmos loops) | 66% faster time-to-merge; 2–3x engineering throughput; 60%+ CVEs remediated automatically; 70%+ incidents resolved before on-call joins | 2026-08-21 | [S19] | maker-claimed |
| Public customers / case studies | Pearl Technologies (3x productivity, 100+ PRs in first 30 days, Cosmos), WEX, GoFundMe (400 technologists), Intercom (chose Augment after trying Cursor), Rubrik (VP Eng story about Auggie), Webflow (2024-era completion), Drata (rollout story), Jellyfish + Snyk partnerships | 2026-08-21 | [S22][S29] | maker-claimed |
| Prism routing savings | designed to cost 20–30% less than frontier-model costs "with minimal quality tradeoff" | 2026-08-21 | [S7] | maker-claimed |
| Compliance signals | SOC 2 Type II; claims first AI coding assistant ISO/IEC 42001 certified | 2026-08-21 | [S10][S29] | maker-claimed |

## 3. Plugin interface (PRI-2925)

- mcp_support: **both**. Client: MCP servers via `~/.augment/settings.json` `mcpServers` (http, sse, stdio), `--mcp-config` overrides, `/mcp` status, `/restart-mcp`, OAuth for hosted servers; plus "native integrations" (GitHub, Linear, Notion — configured through the IDE extension) [S13][S14]. Server: `auggie --mcp` runs Auggie as an MCP server exposing the codebase-retrieval tool to external agents (Claude Code, Cursor, etc.) [S14]. Augment also sells a standalone "Context Engine MCP" with quickstarts for Claude Code, Codex, Cursor, Gemini CLI, Copilot, Zed, Droid, etc. [S2-LLMS][S30]. Evidence: https://docs.augmentcode.com/cli/integrations ; https://docs.augmentcode.com/cli/reference
- plugin_support: **True** — plugins bundle custom commands, subagents, rules, hooks, skills and MCP servers; distributed via **marketplaces** = Git repos with `marketplace.json`; interactive `/plugins` browser; `auggie plugin marketplace add owner/repo`, `auggie plugin install name@marketplace`; marketplaces auto-update (git pull) at startup by default; projects can ship `recommendedMarketplaces` + `enabledPlugins` in `.augment/settings.json` [S31] (as-of 2026-08-21). Evidence: https://docs.augmentcode.com/cli/plugins
- claude_code_plugin: **yes (documented backwards compatibility)** — Auggie recognizes `.claude-plugin` directories, uses a compatible `plugin.json` schema and the same commands/agents/hooks/MCP/skills layout; docs demo installing Anthropic's own marketplace (`auggie plugin marketplace add anthropics/skills`) [S31]. Also reads `CLAUDE.md` (plus hierarchical `AGENTS.md`/`CLAUDE.md` in subdirectories) [S32], `~/.claude/commands/` and `./.claude/commands/` slash commands [S14], and `.claude/skills/` + `~/.claude/skills/` skill dirs [S33][S14]. Evidence: https://docs.augmentcode.com/cli/plugins#compatibility-with-claude-plugin
- subagents: **True** — Markdown+YAML frontmatter agents in `~/.augment/agents/` (user) and `./.augment/agents/` (workspace); `/agents` creation wizard; own context window, own model, tools allowlist/denylist, parallel execution; invoked by name or auto-offered [S34]. In Cosmos, three delegation forms: workers (full Expert sessions with own VM), subagents (lightweight, repo-scoped), Expert-to-Expert via integrations [S9]. Evidence: https://docs.augmentcode.com/cli/subagents
- hooks: **True** — events: PreToolUse, PostToolUse, SessionStart, SessionEnd, Stop; handler type `command` only (.sh/.ps1/.cmd/.bat); regex tool matchers incl. `mcp:*`; PreToolUse can block, Stop can block finishing; configured in settings.json at system (`/etc/augment/settings.json`, immutable), project, local and user scopes [S35] (as-of 2026-08-21). Evidence: https://docs.augmentcode.com/cli/hooks
- plan_mode: **True** — `/plan [open]` toggles Plan Mode / opens the latest plan file in interactive mode [S36]; changelog references plan-mode editors [S15]. (No dedicated docs page; thinner than Claude Code's permission-mode plan.) Evidence: https://docs.augmentcode.com/cli/interactive
- plugin_docs_url: https://docs.augmentcode.com/cli/plugins
- config_docs_url: https://docs.augmentcode.com/cli/config (wizard); settings files documented at https://docs.augmentcode.com/cli/permissions and /cli/hooks; flags at https://docs.augmentcode.com/cli/reference
- ACP support: **yes, first-party** — `auggie --acp`; docs call Auggie "a fully compatible Agent Client Protocol (ACP) agent" while noting not all interactive features are available over ACP; launch blog 2025-11-06 (Zed via the Auggie extension, Neovim via CodeCompanion, Emacs via agent-shell.el) [S37][S38]. This is what Paseo drives. Evidence: https://docs.augmentcode.com/cli/acp/agent
- SDK: **yes** — Auggie SDK for TypeScript (`@augmentcode/auggie-sdk`, incl. a Vercel AI SDK provider) and Python (`auggie-sdk`); auth via `auggie login` session or API key; custom tools supported [S39]. Separate Context Engine SDK + open-source context-connectors library [S30]. Evidence: https://docs.augmentcode.com/cli/sdk

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo, verbatim): "An AI agent that brings Augment Code's power to the terminal." — https://github.com/augmentcode/auggie [S4]
- tagline (homepage title): "Agentic software development at organizational scale"; hero: "Run your software factory" (Cosmos-first framing) — https://www.augmentcode.com/ [S19]
- docs one-liner: "AI-native coding platform built for enterprise-grade software engineering" — https://docs.augmentcode.com/introduction [S2]
- maker claims (paraphrased):
  1. Context Engine: a real-time semantic index of the whole codebase (scales to 100M-line repos) retrieves the right code where grep-based agents miss it; positioned as the core differentiator [S17][S18b][S19].
  2. Token efficiency / cost: same or better quality than Claude Code at 23–53% lower cost on Terminal-Bench 2.0 and SWE-bench Pro (self-run head-to-heads on identical Anthropic models) [S17][S18][S18b].
  3. Benchmark leadership: top SWE-bench Pro agent score (51.80%, self-run, 2026-02); earlier #1 open-source SWE-bench Verified harness (2025-03) [S17][S28].
  4. Multi-model with Prism auto-routing: "the era of single-model engineering is over"; Prism picks the model per request, claimed 20–30% cheaper than frontier list price [S6][S7][S19b].
  5. "Software factory" / SDLC automation: Cosmos Experts triggered by PRs, alerts, tickets, schedules run review/fix/verify loops with humans at checkpoints; CLI is the same agent + automation surface (`--print`, GitHub Actions, service accounts) [S19][S9][S2].
  6. Works in your existing workflow: terminal-first, ACP into Zed/Neovim/Emacs, MCP server mode into other agents, GitHub Actions — "anywhere your code goes" [S2][S37][S14].
  7. Enterprise trust: SOC 2 Type II, claimed-first ISO/IEC 42001 certification, CMEK, no training on customer code on paid plans [S10][S29].
  8. Open standards adoption: agentskills.io skills spec, Claude Code plugin compatibility, AGENTS.md/CLAUDE.md rules, ACP, MCP [S33][S31][S32][S37].
- audience: enterprise engineering organizations and teams (docs: "enterprise-grade software engineering"; pricing: Business = whole team up to 50 seats, Enterprise; homepage speaks to engineering leaders about org-scale outcomes) [S2][S10][S19]. The CLI itself is addressed to individual developers/automators ("in your terminal, on your server, or anywhere your code runs") [S11].

## 5. Company & contact targets (PRI-2929) — company-level only

- legal name: Augment Computing, Inc. (CLI license copyright) [S3]; press releases use "Augment Inc.", brand "Augment Code" [S20]
- HQ: Palo Alto, CA (Series B press release dateline, 2024-04-24) [S20]
- size: null (not researched — no public headcount statement found in materials consulted)
- funding stage: Series B — $227M at $977M post (2024-04-24), $252M total; no later round found in public trackers as of 2026 [S20][S27]
- publicly named leadership (as the company names them):
  - Igor Ostrovsky — co-founder (former chief architect, Pure Storage; ex-Microsoft) [S20]
  - Guy Gur-Ari — co-founder (ex-Google AI researcher); company retrospective credits him with starting the CLI project [S20][S16]
  - Scott Dietzen — CEO ("led by industry veterans Scott Dietzen…", Series B release; Tracxn/Crunchbase still list him as CEO in 2026) [S20][S27]
  - Dion Almaer — named in the Series B leadership sentence (Google/Shopify/Mozilla/Palm alum; title not stated in the release) [S20]
  - Chris Kelly — Product Lead, Cosmos (blog byline; bio: previously New Relic, GitHub, Salesforce, FireHydrant; handle @amateurhuman) [S37]
- DevRel / head of partnerships: none found named on augmentcode.com (partnership announcements — Jellyfish, Snyk — carry no named partnership lead) — researched, absent [S29].
- contact: sales via https://www.augmentcode.com/ ("Book demo" / "Talk to Sales"); support portal https://support.augmentcode.com/ [S19][S1]

## 6. Open questions / conflicts

- **Census merge question (auggie / augment-code / intent):** recommend **merging `augment-code.md` into `auggie.md`** (one harness entry: Auggie, with Augment/Cosmos as the maker platform). The "Augment Code" entry describes the Cosmos orchestration platform and IDE extension, but the underlying agent, permissions, hooks and settings are the same Augment agent that Auggie exposes [S8][S9]; two census entries double-count one harness. **Intent should not be a harness entry**: it is a macOS orchestration workspace that drives *other* agents (Auggie, and BYOA: Claude Code, Codex, OpenCode) [S21] — by Jesse's test it is a wrapper/orchestrator, not an agentic loop of its own. Also, https://www.augmentcode.com/tools/intent now serves the generic homepage (title "Augment Code | AI coding platform for real software"), and Intent has no section in the docs index (llms.txt) — its current status is unclear beyond the 2026-02-10 launch post [S21][S2-LLMS] (as-of 2026-08-21).
- Existing census auggie.md `source_available: True` — wrong. The repo carries no agent source (language: Shell, scaffolding files only), npm ships a bundled `augment.mjs`, and the license forbids modification/redistribution. Should be False [S3][S4][S5].
- Existing census `license: "Custom Proprietary"` — correct [S3].
- Existing census `language: "TypeScript"` — GitHub reports the repo as Shell; the product is TypeScript per Augment's own harness-rebuild post (v1 ~250k lines TS; v2 is a fork of Pi, a TypeScript harness) [S4][S18]. Field is ambiguous (repo vs product).
- Existing census `stars: "272"` — 273 on 2026-08-22 (immaterial) [S4].
- Existing census `current_release: "2026-08-20"` — npm latest is 0.36.0 published 2026-08-21; note GitHub tags (`v1.2.0-prerelease.*`) don't match npm versions [S4][S5].
- Existing census `first_released: "2025-09-08"` — that is repo creation; first npm publish 2025-07-31; maker says public launch "early September" 2025. Defensible, but note the ambiguity [S4][S5][S16].
- Existing census `mcp_support: null`, `subagents: null`, `hooks: null`, `plan_mode: null`, `claude_code_plugin: null`, `pricing: null`, `plugin_docs_url: null` — all researched and fillable (both / True / True / True / yes / token-based+$100 Business / docs.augmentcode.com/cli/plugins) [S13][S14][S31][S34][S35][S36][S7].
- Existing census `model_providers: "Augment Code"` — misleading: models are Anthropic/OpenAI/Google/Zhipu/Moonshot/xAI served through Augment, plus Prism routing [S6].
- Existing census augment-code.md `model_providers` says "Claude (Sonnet, Opus), Gemini, multi-model auto-routing (Prism)" — incomplete (omits GPT-5.x, GLM, Kimi, Grok) [S6].
- All Auggie benchmark numbers (SWE-bench Pro 51.80%, Terminal-Bench head-to-heads, 53%-cheaper claim) are **self-run by Augment**, not leaderboard placements; Scale's official SWE-bench Pro leaderboard entry cited by Augment is for SWE-Agent scaffolds, not Auggie [S17][S18][S18b]. No independent benchmark of Auggie found.
- The homepage outcome numbers (66% faster merge, 2–3x throughput, 60%+ CVEs, 70%+ incidents) are unattributed marketing claims on solution tiles [S19].
- Default autonomy is only defined negatively ("runs commands and tools automatically"; unmatched tools follow "implicit runtime behavior" that the docs never spell out) [S13][S8].
- Reddit community size and any Discord count not obtainable; Zed extensions API returned nothing for "auggie" though the extension exists (blog + repo) [S26][S37].
- No employee-count or post-2024 funding disclosure found; leadership titles trace to the 2024 press release and may be stale [S20][S27].
- CEO/leadership beyond the 2024 release: third-party trackers (Tracxn, Crunchbase) still list Dietzen as CEO in 2026, but Augment's site has no team page to confirm [S27].

## 7. Sources

1. [S1] https://github.com/augmentcode/auggie README (raw) — tagline, install, Node 22+ badge, community links, GitHub Actions
2. [S2] https://docs.augmentcode.com/cli/overview.md — CLI positioning, modes, Node 20+, enterprise non-interactive note; [S2-LLMS] https://docs.augmentcode.com/llms.txt — full docs index (Cosmos, CLI, IDE, Context Engine; no Intent section)
3. [S3] https://raw.githubusercontent.com/augmentcode/auggie/main/LICENSE.md — custom proprietary license, Augment Computing, Inc., subscription requirement
4. [S4] GitHub API repos/augmentcode/auggie (+releases, contributors, commits, contents, search/issues; orgs/augmentcode/repos) — stars/forks/dates/language/repo contents, org repo list
5. [S5] https://registry.npmjs.org/@augmentcode/auggie — versions/dates/license/bin; [S5b] https://api.npmjs.org/downloads/... — weekly/monthly/range downloads (auggie, auggie-sdk); [S5c] https://pypistats.org/api/packages/auggie-sdk/recent
6. [S6] https://docs.augmentcode.com/models/available-models.md — model list, Prism, /model, --model
7. [S7] https://docs.augmentcode.com/models/token-based-pricing.md — 40% service fee, $0.19/hr compute, Business plan, per-model rates, Prism 20–30%
8. [S8] https://docs.augmentcode.com/cli/permissions.md — toolPermissions, policy precedence, settings files, "implicit runtime behavior", Cosmos enforcement
9. [S9] https://docs.augmentcode.com/cosmos/workers-subagents.md — workers vs subagents vs Expert-to-Expert
10. [S10] https://www.augmentcode.com/pricing — Business $100/50 seats, Enterprise features, SOC 2, no-training FAQ
11. [S11] https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli.md — npm install, Node 20+, platforms, auto-update
12. [S12] https://docs.augmentcode.com/cli/setup-auggie/authentication.md — login, token print, AUGMENT_SESSION_AUTH
13. [S13] https://docs.augmentcode.com/cli/integrations.md — MCP client config, native integrations, "runs commands and tools automatically" warning
14. [S14] https://docs.augmentcode.com/cli/reference.md — flags, --acp, --mcp server mode, .claude/commands, .claude/skills, --allow-indexing, --mcp-config
15. [S15] https://raw.githubusercontent.com/augmentcode/auggie/main/CHANGELOG.md — 0.36.0/0.35.0/0.34.0 notes (sensitive-path approval, plan-mode editors, prompt modules rename)
16. [S16] https://www.augmentcode.com/blog/building-by-using-... (2025-12-18) — CLI origin (Guy Gur-Ari), early-September launch, adoption claims, Ink TUI
17. [S17] https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro (2026-02-04) — 51.80% SWE-bench Pro, self-run comparison
18. [S18] https://www.augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper (2026-08-14) — v2 harness = Pi fork, $1.27 vs $2.70, v1 history (1,020 TS files); [S18b] https://www.augmentcode.com/blog/auggie-beats-claude-code-on-cost-and-quality (2026-05-15) — Terminal-Bench 2.0 + SWE-bench Pro head-to-heads
19. [S19] https://www.augmentcode.com/ — homepage: software factory, outcome claims, Cosmos experts; [S19b] blog the-era-of-single-model-engineering-is-over (title, sitemap)
20. [S20] https://www.augmentcode.com/blog/augment-inc-raises-227-million (2024-04-24) — Series B, valuation, founders, Dietzen, Almaer, Palo Alto
21. [S21] https://www.augmentcode.com/blog/intent-a-workspace-for-agent-orchestration (2026-02-10) — Intent launch, coordinator/implementor/verifier, BYOA (Claude Code, Codex, OpenCode), macOS; /tools/intent now serves homepage
22. [S22] https://www.augmentcode.com/customers — Pearl, WEX, GoFundMe, Intercom, Rubrik case studies
23. [S23] VS Code Marketplace extensionquery API (augment.vscode-augment) — installs/ratings
24. [S24] https://plugins.jetbrains.com/api/searchPlugins?search=augment — plugin 24072 downloads, vendor "Augment Computing"
25. [S25] https://formulae.brew.sh/api/formula|cask/auggie.json — 404 (absent)
26. [S26] https://api.zed.dev/extensions?filter=auggie — empty result
27. [S27] Tracxn / Crunchbase / TechCrunch via web search — $252M total, Dietzen CEO, no later round
28. [S28] https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1 (2025-03-31); repo augmentcode/augment-swebench-agent (881 stars)
29. [S29] sitemap blog titles: augment-code-achieves-soc2-type-ii, augment-code-is-the-first-ai-coding-assistant-to-be-iso-iec-42001-certified, Augment-Jellyfish-partnership, augment-snyk-partnership, rolling-out-ai-coding-assistants-how-drata-did-it, webflow-developers-stay-in-the-flow
30. [S30] https://docs.augmentcode.com/context-services/mcp/overview.md — Context Engine MCP for other agents; context-connectors (MIT)
31. [S31] https://docs.augmentcode.com/cli/plugins.md — plugin system, marketplaces, .claude-plugin compatibility, anthropics/skills example
32. [S32] https://docs.augmentcode.com/cli/rules.md — CLAUDE.md/AGENTS.md support, hierarchical discovery, --rules
33. [S33] https://docs.augmentcode.com/cli/skills.md — agentskills.io spec, .augment/.claude/.agents skills dirs
34. [S34] https://docs.augmentcode.com/cli/subagents.md — agents dirs, wizard, tools allow/denylists, parallel
35. [S35] https://docs.augmentcode.com/cli/hooks.md — events, command handlers, settings scopes
36. [S36] https://docs.augmentcode.com/cli/interactive.md — /plan, /plugins, /skills, /agents, slash commands
37. [S37] https://www.augmentcode.com/blog/auggie-acp-zed-neovim-emacs (2025-11-06) — ACP launch, Zed/Neovim/Emacs, Chris Kelly byline
38. [S38] https://docs.augmentcode.com/cli/acp/agent.md — --acp, "fully compatible ACP agent", feature caveat
39. [S39] https://docs.augmentcode.com/cli/sdk.md — TS/Python SDK, AI SDK provider, auth

## Inclusion check (Jesse's test)

**Yes** — Auggie is a first-party agent with its own agentic loop (its own harness — since Aug 2026 a Pi fork with Augment's Context Engine — that analyzes code, edits files, runs tools/terminal, and iterates; exposed via CLI, ACP, MCP server and SDK) [S2][S18]. (Intent, by contrast, is an orchestration workspace over other agents and would fail this test as a standalone entry [S21].)
