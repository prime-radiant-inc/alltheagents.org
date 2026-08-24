# Dossier: CodeWhale (census_slug: codewhale)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7. NOT in census — proposed new-entry frontmatter at the end of section 6. NOTE: briefed as a "small" harness, but it is not — 40.8k GitHub stars.

## 1. Identity

- name: CodeWhale (README styles it "Codewhale"; npm `codewhale`, crate `codewhale-cli`)
- maker: individual — GitHub user **Hmbown**, public name "Hunter Bown", blog field https://codewhale.net/, 1,437 followers; README invites contact via WeChat (`hunterbown`) "Whale Brothers" group. No company entity found (researched, absent) [S2][S3] (as-of 2026-08-24)
- product URL: https://codewhale.net/ | repo URL: https://github.com/Hmbown/CodeWhale
- license: MIT (GitHub API + README; third-party notices file for adapted code) [S1][S3]
- open source? True. source_available: True — full source; "Portions adapted from other open-source projects are recorded in third-party notices" [S3]
- first public release: repo created 2026-01-19 **as `deepseek-tui`**; README Project history: "Codewhale began as `deepseek-tui`" and is "now provider-neutral and independently maintained; it is not affiliated with any model provider"; rebrand ~2026-05 (npm `codewhale` first published 2026-05-23 at v0.8.41; docs/REBRAND.md exists) [S1][S3][S5]
- latest release: v0.9.11, 2026-08-23; 135 GitHub releases total; repo pushed 2026-08-24 [S4][S1]
- what it is:
  - Form factor: terminal TUI + `codewhale exec` one-shot CLI; local web client (`docs/WEB.md`, localhost-bound Runtime API); mobile control page (`app-server --mobile`); voice input doc; community VS Code GUI / nvim / Electron desktop clients exist as third-party repos [S3][S6][S8]
  - Models: BYO, provider-neutral — hosted providers or local models via Ollama, vLLM, SGLang; site claims 45 providers; switch with `/model`; DeepSeek heritage but explicitly unaffiliated [S3][S9]
  - Pricing: free, MIT, no commercial tier found (researched, absent) [S3]
  - Install: `npm install -g codewhale` (Node 18+); also Cargo, Docker, Nix, Scoop, prebuilt archives, Android/Termux, CNB (China) mirror [S3]
  - Default autonomy: modes Plan (read-only) / Ask / Auto-Review / Full Access; `/undo` and `/restore` snapshots; repository rules; optional OS sandboxing (docs/SANDBOX.md) [S3]
  - Language: Rust [S1]

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 40,842 | 2026-08-24 | [S1] | independently observable |
| GitHub forks / watchers | 3,535 / 160 | 2026-08-24 | [S1] | independently observable |
| GitHub open issues | 142 | 2026-08-24 | [S1] | independently observable |
| Contributors | Hmbown 5,756 commits; "CodeWhale Bot" 675 + "CodeWhale Agent" 160 (the agent commits to its own repo); then a long human tail (cyq1017 112, Paulo Aboim Pinto 95, nightt5879 95, idling11 59, dependabot 74, ...) | 2026-08-24 | [S4] | independently observable |
| Releases | 135 releases in ~7 months (v0.9.11 latest, 2026-08-23); ~every 1-2 days recently | 2026-08-24 | [S4] | independently observable |
| Release-asset downloads | 3,872-8,216 per recent release (v0.9.8-v0.9.11) | 2026-08-24 | [S4] | independently observable |
| npm `codewhale` downloads | 6,422/week; 20,646/month | 2026-08-24 | [S5] | independently observable |
| crates.io `codewhale-cli` | 9,164 all-time; 7,882 recent (~90d); first published 2026-05-23 | 2026-08-24 | [S7] | independently observable |
| Third-party ecosystem | community VS Code GUI (HengQuWorld/CodeWhale-VSCode, 7 stars), codewhale.nvim, two Electron desktop clients, a Homebrew tap, forks incl. deepseek-nyamu (zh fork of v0.8.46) and WEIPING_WHALE (134 stars); npm satellites (codewhale.history, lark-to-codewhale Feishu bridge, codewhale-unicornt fork) | 2026-08-24 | [S8] | independently observable |
| Hacker News | "Terminal coding agent for DeepSeek V4" — 4 points, 0 comments (2026-05-26); mentioned in an Ask HN (8 pts). No front-page traction found | 2026-08-24 | [S10] | independently observable |
| Community channels | Discord (discord.gg/37gfS3ksug) + WeChat "Whale Brothers" group; sizes not researched | 2026-08-24 | [S3] | null (sizes) |
| Maker usage claims | none found beyond the star count shown on the site; no user/customer/funding numbers | 2026-08-24 | [S9][S3] | researched, absent |
| Benchmark placements | none found | 2026-08-24 | [S10] | researched, absent |

Signal shape: 40.8k stars + 3.5k forks in 7 months with modest npm/HN numbers and a strong Chinese-community footprint (WeChat group, CNB mirror, zh/ja/ko/vi/id docs, zh forks). Stars vastly outrun every other signal; downloads (~20-30k/month across channels) are real but two orders below the star count.

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — docs/MCP.md; `/mcp` command "Configure or inspect MCP server integration"; README: "Connect MCP servers and skills" [S3][S6]. Evidence: https://github.com/Hmbown/CodeWhale/blob/main/docs/MCP.md
- plugin_support: **True** — layered: Skills (docs/SKILLS.md, `/skill install` from GitHub/tarball), versioned "plugin bundles" (`plugin.toml` activating namespaced Skills + MCP config, docs/PLUGIN_BUNDLES.md, docs/PLUGINS.md), hooks (docs/HOOKS.md), agent roles as readable files, automatic workflows (docs/AUTOMATIC_WORKFLOWS.md, WORKFLOW_AUTHORING.md) [S6][S11]
- claude_code_plugin: **partial** — dedicated docs/CLAUDE_PLUGIN_COMPAT.md: treats Claude Code skill folders (`.claude/skills/<name>/SKILL.md`) as instruction bundles, discovered by the normal skill registry; explicitly does NOT run Claude Code plugin runtimes (`.claude-plugin/plugin.json`, slash-command bundles, `model: inherit`); `/skill install` rejects multi-skill plugin archives [S11]. Evidence: https://github.com/Hmbown/CodeWhale/blob/main/docs/CLAUDE_PLUGIN_COMPAT.md
- subagents: **True** — docs/SUBAGENTS.md plus "Fleet" agent-teams system (docs/FLEET.md, FLEET_WORKFLOW_TUTORIAL.md); README: "coordinate agents without turning their internal instructions into your transcript" [S6][S3]
- hooks: **True** — docs/HOOKS.md; README lists "configure hooks" as core extensibility [S6][S3]
- plan_mode: **True** — "Plan is read-only" (README); docs/MODES.md; GUIDE.md: "Plan for read-only exploration, use Act for normal changes" [S3][S6]
- plugin_docs_url: https://github.com/Hmbown/CodeWhale/blob/main/docs/PLUGINS.md (bundles: docs/PLUGIN_BUNDLES.md; skills: docs/SKILLS.md)
- config_docs_url: https://github.com/Hmbown/CodeWhale/blob/main/docs/CONFIGURATION.md
- ACP support: **yes, first-party** — docs/RUNTIME_API.md: "`codewhale serve --acp` speaks the Agent Client Protocol over stdio for editors"; sits beside the canonical `codewhale app-server` HTTP/SSE Runtime API (`serve --http`/`--mobile` are compatibility aliases) [S6] (as-of 2026-08-24). Evidence: https://github.com/Hmbown/CodeWhale/blob/main/docs/RUNTIME_API.md
- SDK: **partial** — no packaged language SDK found; the documented integration surface is the local Runtime API (HTTP/SSE, "/v1/*") and ACP, "instead of screen-scraping terminal output" [S6]

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline: site (verbatim): "dives into the deep so you don't have to" [S9]; repo description: "Open-source coding agent for your terminal, built in Rust and on a journey of continuous community improvement" [S1]
- maker claims (paraphrased, README "Why Codewhale" + site) [S3][S9]:
  1. Model freedom: any hosted provider or local model (Ollama/vLLM/SGLang), per-task model switching; provider-neutral, "not affiliated with any model provider"
  2. Visible control: Plan read-only mode; Ask/Auto-Review/Full Access approval tiers; `/undo` / `/restore` workspace snapshots
  3. Long-work organization: durable `/goal`, saved sessions, reviewable workflows, Fleet agent teams whose internal instructions stay out of your transcript
  4. Extensibility on open parts: MCP servers, skills, hooks, agent roles as plain files
  5. Built-in-public / community-improved: "improved in public with the people who use it"; agent+bot commit to its own repo; contributor credit preserved
  6. Honesty posture: "Unknown model prices stay unknown instead of being reported as free"; docs/AGENT_ETHOS.md, RECEIPTS.md
  7. Reach: Android/Termux, HarmonyOS doc, China CNB mirror, 18 README translations, local web + mobile control surfaces
- audience: terminal developers wanting local/self-hosted model control; strong outreach to Chinese-speaking community (WeChat group, CNB mirror, zh docs) and classrooms (CLASSROOM_INSTALL.md) [S3][S6]

## 5. Company & contact targets (PRI-2929)

- Not a company. Individual maintainer: GitHub **Hmbown** ("Hunter Bown"); public contact paths the project offers: GitHub issues/PRs, Discord, WeChat `hunterbown` [S2][S3]. Per instruction, public identity only.
- Funding: none found; no sponsors links found in README (researched, absent) [S3]
- Legal entity: none found (researched, absent)

## 6. Open questions / conflicts

- Brief described CodeWhale as a small project ("terminal coding agent for DeepSeek V4 and open models") — that matches the pre-rebrand `deepseek-tui` identity (HN post 2026-05-26); today it is provider-neutral and, at 40,842 stars, would rank among the most-starred harnesses in the census. The briefing framing is stale.
- Stars vs everything else: 40.8k stars against ~20k npm downloads/month, 4 HN points, 160 watchers, and 7-star third-party GUI repos is an unusual profile; star acquisition dynamics (community campaigns, CN developer channels) were not investigated. Treat raw stars with care until corroborated.
- "45 providers" is site-claimed (via rendered page summary); not counted independently [S9].
- Contributor identities "CodeWhale Bot"/"CodeWhale Agent" (anon email contributors) imply self-committing automation; exact mechanism not verified.
- deepseek-tui prehistory: repo created 2026-01-19; whether it was public/promoted under that name from day one was not traced; first npm publish under `codewhale` is 2026-05-23.
- No ACP entry in docs index by filename; ACP lives inside RUNTIME_API.md — easy to miss when auditing.
- Proposed new census entry (per _TEMPLATE.md schema v1.1):

```yaml
---
name: "CodeWhale"
slug: "codewhale"
layout: "agent.njk"
category: "agent"
maker: "hmbown"            # new makers.json record: maker_type individual, country null, makes_models false, revenue_model []
license: "MIT"
url: "https://codewhale.net/"
source_code_url: "https://github.com/Hmbown/CodeWhale"
source_available: True
homepage: "https://codewhale.net/"
docs_url: "https://github.com/Hmbown/CodeWhale/tree/main/docs"
download_url: "https://www.npmjs.com/package/codewhale"
install_method: "npm install -g codewhale; also Cargo, Docker, Nix, Scoop, prebuilt archives, Android/Termux, CNB mirror"
platforms: ["CLI", "Web"]
autonomy_level: ["pair-programmer", "agentic"]
specialization: "general"
language: "Rust"
first_released: "2026-01-19"   # repo created as deepseek-tui; rebranded to CodeWhale ~2026-05
current_release: "2026-08-23"  # v0.9.11
maintained: "active"
mcp_support: True
plugin_support: True
claude_code_plugin: "partial"  # reads .claude/skills SKILL.md as instruction bundles; no plugin runtime (docs/CLAUDE_PLUGIN_COMPAT.md)
subagents: True
hooks: True
plan_mode: True
plugin_docs_url: "https://github.com/Hmbown/CodeWhale/blob/main/docs/PLUGINS.md"
config_docs_url: "https://github.com/Hmbown/CodeWhale/blob/main/docs/CONFIGURATION.md"
model_providers: "BYO multi-provider (site claims 45); local via Ollama, vLLM, SGLang; provider-neutral"
pricing: "free"
github_stars: "40842"
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "Rust terminal agent that grew out of deepseek-tui into a provider-neutral, community-improved harness — Plan/Ask/Auto-Review/Full-Access control tiers, /undo and snapshot restore, Fleet agent teams, and a local HTTP/SSE Runtime API plus first-party ACP (codewhale serve --acp)."
---
```

## 7. Sources

1. [S1] https://api.github.com/repos/Hmbown/CodeWhale — stars, forks, dates, license, language, description
2. [S2] https://api.github.com/users/Hmbown — maker public identity
3. [S3] https://raw.githubusercontent.com/Hmbown/CodeWhale/main/README.md — install, Why, safety, history (deepseek-tui), license, community
4. [S4] https://api.github.com/repos/Hmbown/CodeWhale/releases + /contributors — 135 releases, asset downloads, contributor split
5. [S5] https://registry.npmjs.org/codewhale + api.npmjs.org download points — versions, first publish, downloads
6. [S6] https://api.github.com/repos/Hmbown/CodeWhale/contents/docs + raw docs (RUNTIME_API.md, WEB.md, GUIDE.md) — ACP/serve, runtime API, docs inventory
7. [S7] https://crates.io/api/v1/crates/codewhale-cli — crate downloads
8. [S8] https://api.github.com/search/repositories?q=codewhale — third-party ecosystem, forks
9. [S9] https://codewhale.net/ (WebFetch summary) — tagline, 45 providers, differentiators
10. [S10] https://hn.algolia.com/api/v1/search?query=CodeWhale — HN signal
11. [S11] https://raw.githubusercontent.com/Hmbown/CodeWhale/main/docs/CLAUDE_PLUGIN_COMPAT.md — Claude skills compat boundary

## Inclusion check (Jesse's test)

**Yes** — CodeWhale is a genuine agent with its own agentic loop implemented in Rust (own TUI, tool surface, modes, Fleet multi-agent runtime, Runtime API control plane); `codewhale serve --acp` exposes that native loop over ACP rather than wrapping another vendor's agent [S3][S6]. It began life as a DeepSeek-focused TUI but is its own agent, not a wrapper around DeepSeek tooling.
