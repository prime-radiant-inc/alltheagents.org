# Dossier: Dirac (census_slug: dirac)

Compiled 2026-08-24. Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Small open-source project (Cline soft-fork) — research kept proportionate. NOT currently in the census; proposed new-entry frontmatter at end.

## 1. Identity

- name: **Dirac** (npm `dirac-cli`, binary `dirac`; VS Code extension `dirac-run.dirac`)
- maker: individual — GitHub user **dirac-run**, public profile name "Max Trivedi", bio "Founder @ SignalBloom AI. Ex-Meta infra engineer. Created Dirac to be the agent I wanted to use, then decided to open source it" [S2] (as-of 2026-08-24). npm author string: "Dirac Delta Labs"; contact hi@dirac.run [S3]. No registered-company evidence found beyond the name (researched, absent).
- product URL: https://dirac.run
- repo URL: https://github.com/dirac-run/dirac
- license: **Apache-2.0** (GitHub license detection + npm metadata agree) [S1][S3]
- open source? **True.** source_available: True — full source (TypeScript) incl. CLI, VS Code extension, and eval diffs in-repo [S1][S6].
- lineage: a **soft fork of Cline** — homepage acknowledges the Cline fork; README calls Cline "the parent repo" and links a Cline bug/PR the Dirac team filed upstream. Not a GitHub-flagged fork (fresh repo) [S4][S5].
- first public release: repo created 2026-04-05; first npm publish 0.2.1 on 2026-04-10 [S1][S3].
- latest release: 0.4.37, 2026-08-17 (npm + VS Code Marketplace same version/date); 164 npm versions in ~4.5 months [S3][S8].
- what it is:
  - Form factors: terminal CLI (interactive, plan mode `-p`, yolo mode `-y`, pipeable, `dirac history`), **VS Code extension** (sidebar), and **ACP server** (`dirac --acp`) listed in the JetBrains and Zed ACP registries [S5][S8].
  - Models: BYO multi-provider — env-key support for Anthropic, OpenAI, OpenRouter, Gemini, Groq, Mistral, xAI, HuggingFace, AWS Bedrock, GCP Vertex, plus any OpenAI-compatible endpoint (base URL + model id); optional ChatGPT sign-in in ACP mode. Requires models with native tool calling [S5].
  - Pricing: free, open source, BYOK; no paid tier found (researched, absent) [S4][S5].
  - Install: `npm install -g dirac-cli` or VS Code Marketplace; Node 20/22/24 (v25 unsupported due to a V8 bug) [S5].
  - Default autonomy: approval-based workflow ("keeping you in control"); `-y` auto-approves; tools: read/write files, terminal commands, headless browser [S5] (maker-described, not independently tested).
  - Implementation: TypeScript; CLI TUI built on Ink/React; ships `@agentclientprotocol/sdk` 1.3.0 as a direct dependency [S1][S3].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 1,465; forks 82; watchers 5; open issues 14 | 2026-08-24 | [S1] | independently observable |
| Contributors | top: dirac-run 57 commits, marton78 22, alexdim 19, devin-ai-integration[bot] 12; ~10 humans with 2+ commits | 2026-08-24 | [S7] | independently observable |
| npm downloads `dirac-cli` | 2,222/week; 8,408/month | 2026-08-24 | [S9] | independently observable |
| VS Code Marketplace | 1,226 installs; 5.0 avg rating (3 ratings); v0.4.37 2026-08-17 | 2026-08-24 | [S8] | independently observable |
| Release cadence | 164 npm versions 2026-04-10 → 2026-08-17; last push 2026-08-17 | 2026-08-24 | [S3][S1] | independently observable |
| Terminal-Bench-2 | 65.2% with `gemini-3-flash-preview`; claimed top score for that model, beating Google's baseline (47.6%) and Junie CLI (64.3%); submitted to the community leaderboard (HF discussion #145, title confirms "Dirac Gemini Flash-3-Preview 65.2%") | 2026-08-24 | [S5][S10] | maker-claimed; leaderboard submission observable but discussion page now inaccessible (see §6) |
| Cost claim | "reduces API costs by 64.8% on average" (repo desc says 50-80%); 7-task refactor eval vs Cline/Kilo/Opencode/Roo etc. with per-task diffs and costs published in-repo | 2026-08-24 | [S5][S1] | maker-claimed (reproducible-in-principle: eval diffs public) |
| Discord | server exists (invite on homepage); member count not collected | 2026-08-24 | [S4] | independently observable (existence only) |
| Third-party | hashnode essay "Harness Leaderboards Are the New Model Leaderboards" discusses Dirac's leaderboard result; community fork sekmet/dirac-agent exists | 2026-08-24 | [S10] | independently observable |
| Users / customers / funding | none found | 2026-08-24 | [S4][S10] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **none — deliberate.** README: "Native Tool Calling Only … (Note: MCP is not supported)"; homepage repeats "No MCP" as a feature [S5][S4]. Evidence: https://github.com/dirac-run/dirac (README, Features).
- plugin_support: **partial** — no plugin/extension system of its own (researched, absent); customization is via **Skills** and `AGENTS.md` project instructions; CLI has a Skills panel [S5][S6].
- claude_code_plugin: **partial** — README: "seamlessly picks up Claude's skills by automatically reading from `.ai`, `.claude`, and `.agents` directories"; supports `AGENTS.md`. Does not implement the Claude Code plugin/marketplace format [S5].
- subagents: **none found** — no subagent/task-spawning capability in README or repo tree (researched, absent) [S5][S6].
- hooks: **none found** — no lifecycle-hook system; repo-tree "hooks" matches are React UI hooks only (researched, absent) [S6].
- plan_mode: **True** — `dirac -p "prompt"` runs Plan Mode ("see the strategy before executing"); inherited Cline plan/act lineage [S5]. Evidence: https://github.com/dirac-run/dirac (Common Commands).
- plugin_docs_url: none (no plugin system) — researched, absent.
- config_docs_url: https://github.com/dirac-run/dirac/blob/master/docs/providers/README.md (provider settings); CLI guide at https://github.com/dirac-run/dirac/blob/master/cli/README.md
- ACP support: **yes, first-party** — `dirac --acp`; dedicated `cli/src/acp/` module (AcpAgent, session worktrees, protocol-conformance tests) built on `@agentclientprotocol/sdk` 1.3.0; installable from the JetBrains (2025.3+) and Zed ACP registries; owns provider config independently of the editor [S5][S6][S3]. Evidence: README "ACP Editor Integration".
- SDK: **False** — no agent SDK published (researched, absent) [S3][S6].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline: "The Agent for Precision and Speed." (homepage); page title "Dirac - The Token-Efficient Coding Agent" [S4][S10]. README H1: "Accurate & Highly Token Efficient Open Source AI Agent" [S5].
- maker claims (paraphrased):
  1. Context curation as the core thesis: model reasoning degrades with context length, so tight curation improves accuracy AND cost simultaneously [S5].
  2. 64.8% average API-cost reduction vs other agents at equal-or-better quality [S5][S4].
  3. Hash/line-anchored parallel edits that stay stable as the file changes [S4][S5].
  4. AST-native manipulation for "100% syntactic accuracy" in refactors [S4][S5].
  5. Multi-file batching — several files read/edited per LLM round-trip, "2.8x faster execution" [S4][S5].
  6. Benchmark proof: topped Terminal-Bench-2 for gemini-3-flash-preview (65.2%) with no benchmark-specific tuning; published head-to-head refactor evals with diffs vs Cline, Kilo, Opencode, Roo, others [S5].
  7. Anti-MCP stance as reliability positioning: native tool calling only, "bang-for-the-buck tooling with bare minimum prompting" [S5].
  8. Openness: Apache-2.0, evals reproducible on public repos [S5].
- audience: developers wanting cheap, accurate large refactors; explicitly benchmarked against open-source agent peers (positions within that category) [S5]. No team-size/stack claims (researched, absent).

## 5. Company & contact targets (PRI-2929)

- No company found. "Dirac Delta Labs" is the npm author label; the only public person is founder **Max Trivedi** (GitHub dirac-run; self-described Founder @ SignalBloom AI, ex-Meta) [S3][S2]. Per instruction, public identity only.
- Contact paths: hi@dirac.run (npm maintainer email, public), GitHub issues, Discord invite on homepage [S3][S4].
- Funding: none found (researched, absent).

## 6. Open questions / conflicts

- The Terminal-Bench-2 evidence link (HF discussion #145) returns 403 "Discussions are disabled for this repo" — the submission's title is confirmed via search snippets, but score acceptance/merge status could not be read. The official tbench.ai leaderboard was not checked for a Dirac row; flag for follow-up [S10][S11].
- Cost numbers vary by surface: README "64.8% on average", GitHub repo description "50-80%", homepage "64.8% vs competitors". Same claim family, inconsistent precision [S5][S1][S4].
- README itself notes a Cline cost-accounting bug that caused its own evals to "slightly underreport" costs, with an update promised — the published cost table is acknowledged-imperfect [S5].
- "Dirac Delta Labs" vs "SignalBloom AI": npm says the former, the founder's bio the latter; the legal entity (if any) behind Dirac is unresolved [S3][S2].
- Maker-claimed "100% accuracy" on its refactor evals is self-graded (🟢/🟡/🔴 scoring by the maker), though diffs are published [S5].
- VS Code extension `updateCount` (11,272) dwarfs installs (1,226) — auto-updates across 164 rapid versions; installs is the meaningful figure [S8].
- Not in the existing census; new-entry frontmatter proposed below. Note the census wrapper question: `dirac-cli` ships the full agent (138 MB unpacked, 1,471 files of compiled app), not a launcher stub [S3].

## 7. Sources

1. [S1] https://api.github.com/repos/dirac-run/dirac — stars 1,465, Apache-2.0, TypeScript, dates, description
2. [S2] https://api.github.com/users/dirac-run — Max Trivedi public profile/bio
3. [S3] https://registry.npmjs.org/dirac-cli (+ downloads API) — versions, dates, deps (@agentclientprotocol/sdk), author, license
4. [S4] https://dirac.run (via WebFetch summary) — tagline, "No MCP", Cline-fork acknowledgment, Discord, claims
5. [S5] https://raw.githubusercontent.com/dirac-run/dirac/master/README.md — features, evals table, install, ACP, skills dirs, plan/yolo modes
6. [S6] GitHub git tree (master, recursive) — cli/src/acp module, SkillsPanel, absence of subagents/lifecycle hooks/plugin system
7. [S7] https://api.github.com/repos/dirac-run/dirac/contributors — contributor distribution
8. [S8] VS Code Marketplace extensionquery API (dirac-run.dirac) — 1,226 installs, rating, version dates
9. [S9] https://api.npmjs.org/downloads/point/last-week|last-month/dirac-cli — download counts
10. [S10] Web search results 2026-08-24 — HF discussion #145 title, hashnode commentary, sekmet/dirac-agent fork, tbench.ai leaderboard link
11. [S11] https://huggingface.co/datasets/harborframework/terminal-bench-2-leaderboard/discussions/145 — UNREACHABLE (403, discussions disabled)

## Inclusion check (Jesse's test)

**Yes** — Dirac creates and modifies software with its own agentic loop: it is a maintained soft fork of Cline whose loop it owns in-repo and has substantially rebuilt (hash-anchored parallel edits, AST tools, multi-file batching, own CLI/ACP layer); the npm package ships the entire agent, not a wrapper around someone else's [S1][S3][S5][S6].

## Proposed census entry (per hc/agents/_TEMPLATE.md — new file agents/dirac.md)

```yaml
---
name: "Dirac"
slug: "dirac"
layout: "agent.njk"
category: "agent"
maker: "max-trivedi"          # new maker record: maker_type individual (npm label "Dirac Delta Labs"), country null, makes_models false, revenue_model []
license: "Apache-2.0"
url: "https://dirac.run"
source_code_url: "https://github.com/dirac-run/dirac"
source_available: True
homepage: "https://dirac.run"
docs_url: "https://github.com/dirac-run/dirac/blob/master/cli/README.md"
download_url: "https://www.npmjs.com/package/dirac-cli"
install_method: "npm install -g dirac-cli; VS Code Marketplace; JetBrains/Zed ACP registries"
platforms: ["CLI", "IDE"]
autonomy_level: ["agentic"]
specialization: "general"
language: "TypeScript"
first_released: "2026-04-10"   # first npm publish; repo created 2026-04-05
current_release: "2026-08-17"
maintained: "active"
mcp_support: "no — deliberate ('No MCP'; native tool calling only)"
plugin_support: "partial (Skills + AGENTS.md; no plugin system)"
claude_code_plugin: "partial (auto-reads Claude skills from .ai/.claude/.agents dirs; not the plugin format)"
subagents: "no (none found)"
hooks: "no (none found)"
plan_mode: "yes (dirac -p)"
plugin_docs_url: null
config_docs_url: "https://github.com/dirac-run/dirac/blob/master/docs/providers/README.md"
model_providers: "Anthropic, OpenAI, Google, OpenRouter, Groq, Mistral, xAI, Bedrock, Vertex, any OpenAI-compatible"
pricing: "BYOK"
github_stars: 1465
sources: ["paseo-acp-catalog"]
last_verified: "2026-08-24"
what_makes_it_special: "A Cline fork rebuilt around one thesis — tightly curated context makes agents both cheaper and more accurate — with hash-anchored parallel edits, AST-native refactoring, a published cost-vs-quality eval suite, and a defiant no-MCP stance."
---
Dirac began in April 2026 as ex-Meta engineer Max Trivedi's fork of Cline,
reworked to attack token waste: batched multi-file edits, AST-level rewrites,
and hash-anchored diffs that survive file drift. It courts developers doing
large refactors on a budget, backs its pitch with in-repo head-to-head evals
against Cline, Roo, and Opencode, and drew notice by topping Terminal-Bench-2's
gemini-3-flash-preview bracket. Its refusal to support MCP is a stated design
position, not an omission.
```
