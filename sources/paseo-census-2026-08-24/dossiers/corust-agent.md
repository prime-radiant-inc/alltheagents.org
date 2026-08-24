# Dossier: Corust Agent (census_slug: corust-agent)

Compiled 2026-08-24 (task-dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". NOT currently in the census — proposed new-entry frontmatter at the end. Caveat: the maker's homepage corust.ai was UNREACHABLE during research (DNS returns no A record from this environment and from 8.8.8.8) — homepage claims below come from search-engine index snippets only [S6][S7].

## 1. Identity

- name: Corust Agent (Zed extension id `corust-agent`; ACP binary `corust-agent-acp`; separate TUI client `corust`)
- maker: company — Corust AI / "Corust.ai" (extension author string: "Corust AI <support@corust.ai>"; LICENSE copyright "Copyright (C) 2025 Corust.ai") [S3][S4]. GitHub org `Corust-ai` created 2025-06-15, 24 followers, no location/blog set [S5]. HQ country: not published; one org repo is a Chinese-language Rust-annotation template fork, hinting at a Chinese-speaking team — unconfirmed [S5]. Org form: company (self-presented).
- product URL: https://corust.ai (indexed title: "Corust AI — Fearless Rust Coding with Reliable AI Delivery") [S6] — unreachable as-of 2026-08-24 [S7]
- repo URL: https://github.com/Corust-ai/corust-agent-release — a RELEASE/DISTRIBUTION repo only: contents are LICENSE, extension.toml (Zed agent-server extension manifest), and an icon; no source code [S2]
- license: GPL-3.0 per the LICENSE file in the release repo ("Corust Agent, Copyright (C) 2025 Corust.ai" + full GPLv3 text); GitHub API reads NOASSERTION [S4][S1]. The companion `corust-cli` installer repo is MIT [S8].
- open source? **Effectively no.** source_available: False — despite the GPL-3.0 license file, no source code for the agent was found in the org's 8 public repos (release repo has binaries only; other repos are installers, forks, registry forks, a review-test repo) [S2][S5] (researched, absent). GPL license text without published source is a conflict — see section 6.
- first public release: v0.0.1-release, 2025-12-19 (release repo created 2025-12-09) [S3][S1]
- latest release: v0.6.0, 2026-05-13 (22 releases total; repo last pushed same day) [S3][S1] (as-of 2026-08-24 — no release for ~3.5 months)
- what it is:
  - Form factor: editor agent via ACP (Zed agent-server extension downloading platform binaries and running `corust-agent-acp`; Windows/macOS/Linux targets) plus an interactive terminal client (`corust` TUI with exec/sessions/resume) [S3][S8].
  - Models: the maker's own fine-tuned Rust model — indexed homepage copy claims a model "trained deeply on Rust patterns, crates, and best practices", shared across Zed plugin, GitHub PR reviewer, and CLI; "zero-cost access" [S6] (maker-claimed, homepage unreachable to verify; BYO-key support not mentioned anywhere found — null).
  - Pricing: free ("zero-cost access … without limits" per indexed copy) [S6] (maker-claimed).
  - Install: Zed extension marketplace; curl install script or Homebrew tap for the CLI (`Corust-ai/homebrew-cli`); manual binaries [S3][S8][S5].
  - Default autonomy: not documented anywhere reachable — null.
  - Specialization: **Rust** — "Co-building with a seasoned Rust partner." (extension description, verbatim); claims tuned understanding of Cargo.toml, async Rust, lifetimes [S3][S6].
  - Sibling product: "Corust Reviewer" GitHub App for PR review (per indexed homepage copy; org has a `review-test` repo "Test repo for Corust Verify code review") [S6][S5].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars (release repo) | 31 | 2026-08-24 | [S1] | independently observable |
| GitHub forks | 2; watchers 0; open issues 1 | 2026-08-24 | [S1] | independently observable |
| Release-asset downloads | 47,647 total across 22 releases; v0.6.0 alone ~32,558 (darwin-arm64 7,610; darwin-x64 6,967; linux-x64 8,556; windows-x64 9,425). NOTE: the Zed extension auto-downloads these archives on install/update, so this doubles as an install proxy — but re-updates and CI inflate it | 2026-08-24 | [S3] | independently observable (interpret with caution) |
| corust-cli repo stars | 7 | 2026-08-24 | [S5] | independently observable |
| Zed extension listing | exists (zed.dev/extensions/corust-agent per search index; page 404'd on direct fetch; install count not obtainable via api.zed.dev) | 2026-08-24 | [S6][S9] | partially verified |
| Paseo listing | in Paseo's ACP catalog; paseo.sh/corust landing page exists | 2026-08-24 | [S10] | independently observable |
| X/Twitter | account @CorustAI exists (follower count not captured — null) | 2026-08-24 | [S6] | null |
| Maker usage claims | none found (no user counts located in any indexed copy) | 2026-08-24 | [S6] | researched, absent |
| Funding / customers / press / benchmarks / Discord | none found | 2026-08-24 | [S6] | researched, absent |

## 3. Plugin interface (PRI-2925)

Docs are unreachable (corust.ai down; no docs repo), so most fields are **null (unresearchable)**, not False:

- mcp_support: null — no reachable documentation; nothing in the release repo mentions MCP [S2].
- plugin_support: null — no evidence of a skills/plugin system; nothing reachable documents one.
- claude_code_plugin: null — no mention of CLAUDE.md/.claude anywhere found.
- subagents: null. hooks: null. plan_mode: null.
- plugin_docs_url: none found. config_docs_url: none found (corust.ai unreachable).
- ACP support: **yes, first-party and primary** — the product ships as `corust-agent-acp`, distributed as a Zed agent-server extension (extension.toml `[agent_servers.corust-agent]` with per-platform archives + cmd), and the org forked Zed's ACP `zed-registry` to list itself [S3][S5]. Evidence: https://github.com/Corust-ai/corust-agent-release/blob/main/extension.toml
- SDK: False — none found (researched, absent) [S5].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (extension.toml, verbatim): "Co-building with a seasoned Rust partner." [S3]; indexed homepage title: "Fearless Rust Coding with Reliable AI Delivery" [S6]
- maker claims (from extension metadata + indexed homepage copy; homepage itself unreachable):
  1. Rust specialization end-to-end: a model fine-tuned on Rust patterns, crates, best practices; understands Cargo.toml, async Rust, lifetimes [S6].
  2. Reliability claim: "zero hallucinations on Rust idioms" (indexed copy — strong claim, no evidence offered) [S6].
  3. One fine-tuned model across three surfaces: Zed plugin, GitHub PR reviewer ("Corust Reviewer"), terminal CLI [S6].
  4. Free: "zero-cost access … without limits" [S6].
  5. Purpose-built agent for prototyping, refactoring, crate exploration in the terminal [S6].
- audience: Rust developers (individuals; no team/enterprise language found) [S6].

## 5. Company & contact targets (PRI-2929)

- Company: "Corust.ai" / "Corust AI"; legal name, HQ, and size not published (researched, absent). Public contact: support@corust.ai (extension.toml authors field) [S3].
- Publicly named leadership: none found — no team page reachable, no bylined launch post located [S6] (researched, absent).
- Funding stage: none found (null).

## 6. Open questions / conflicts

- **Homepage unreachable**: corust.ai resolves to no A record (checked locally and via 8.8.8.8) as-of 2026-08-24, yet search engines index live-looking copy and the X account exists. Either a DNS outage, geo-restricted DNS, or the site died very recently. All homepage-derived claims are single-sourced from index snippets [S6][S7].
- **License vs source conflict**: the binary-only release repo carries a GPL-3.0 LICENSE naming "Corust Agent", but no corresponding source is published anywhere in the org. If the binary is genuinely GPLv3, source should be available on request; as observed, this is a proprietary-in-practice distribution under an open-source license text. Recorded license "GPL-3.0 (claimed)", source_available False.
- **Maintenance**: no release since 2026-05-13 (~3.5 months) and homepage down — maintained is recorded "active" only tentatively; "dormant" is defensible. Re-check before publishing.
- Zed extension install count not obtainable (extension page 404 on direct fetch; api.zed.dev queries returned nothing) — the 47.6k release-asset downloads are the best available install proxy.
- Whether the agent supports BYO models/keys, MCP, or any config at all is unknown — the only artifacts are binaries.
- Company nationality unknown; Chinese-language repo fork is a weak hint only.
- Relationship between "Corust Verify" (review-test repo description) and "Corust Reviewer" (indexed copy) — presumably the same PR-review product, unconfirmed.

## 7. Sources

1. [S1] https://api.github.com/repos/Corust-ai/corust-agent-release — stars, dates, NOASSERTION license, no language (binary repo)
2. [S2] GitHub contents API for the repo root — LICENSE + extension.toml + icon only; no source
3. [S3] https://raw.githubusercontent.com/Corust-ai/corust-agent-release/main/extension.toml + releases API — extension manifest, `corust-agent-acp` cmd, 22 releases, v0.6.0, asset download counts
4. [S4] https://raw.githubusercontent.com/Corust-ai/corust-agent-release/main/LICENSE — "Corust Agent, Copyright (C) 2025 Corust.ai", GPLv3
5. [S5] https://api.github.com/users/Corust-ai + org repos list — org identity, corust-cli, homebrew-cli, zed-registry/zed-extensions forks, review-test, Chinese annotation-template fork
6. [S6] Web search results 2026-08-24 — corust.ai indexed title/copy ("Fearless Rust Coding…", fine-tuned model, zero-cost, three surfaces, Reviewer app), @CorustAI on X, zed.dev/extensions/corust-agent listing
7. [S7] DNS checks (local + nslookup @8.8.8.8): corust.ai — no A record; WebFetch ENOTFOUND for corust.ai and www.corust.ai
8. [S8] https://raw.githubusercontent.com/Corust-ai/corust-cli/main/README.md — CLI installer repo, MIT, `corust`/`exec`/`sessions`/`resume`, curl + brew install
9. [S9] https://api.zed.dev/extensions queries — could not surface corust-agent (negative result)
10. [S10] https://paseo.sh/corust — Paseo landing page referencing the Corust agent

## Inclusion check (Jesse's test)

**Yes (with a closed-source caveat)** — Corust Agent is presented and distributed as its own coding agent: a purpose-built binary (`corust-agent-acp`) speaking ACP with its own fine-tuned Rust model and its own TUI client, not a wrapper around another vendor's agent [S3][S6][S8]. The loop cannot be inspected (no source), so "own agentic loop" rests on the maker's presentation and the standalone-binary form factor.

## Proposed census entry (new; per hc/agents/_TEMPLATE.md)

```yaml
---
name: "Corust Agent"
slug: "corust-agent"
layout: "agent.njk"
category: "agent"
maker: "corust-ai"          # new makers.json record: maker_type company, country null, makes_models true (fine-tuned Rust model, maker-claimed), revenue_model []  # currently free
license: "GPL-3.0 (claimed; no source published)"
url: "https://corust.ai"
source_code_url: "https://github.com/Corust-ai/corust-agent-release"   # binaries + extension manifest only
source_available: false
homepage: "https://corust.ai"        # UNREACHABLE 2026-08-24 (no DNS A record)
docs_url: null
download_url: "https://github.com/Corust-ai/corust-agent-release/releases"
install_method: "Zed extension; curl script / brew tap (corust CLI); binaries"
platforms: ["IDE", "CLI"]            # IDE via Zed ACP extension; corust TUI
autonomy_level: ["agentic"]
specialization: "general"            # NOTE: truly Rust-language-specialized; closed enum has no 'rust-lang' value — propose extending the enum, else 'general' + this note
language: null                       # closed source; binary presumed Rust (unverified)
first_released: "2025-12-19"         # v0.0.1-release
current_release: "2026-05-13"        # v0.6.0
maintained: "active"                 # tentative — no release in 3.5 months and homepage down; re-verify
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "locked — maker's own fine-tuned Rust model (maker-claimed)"
pricing: "free"                      # "zero-cost access", maker-claimed
github_stars: "31"
sources: ["paseo-acp-catalog", "zed-extensions"]
last_verified: "2026-08-24"
what_makes_it_special: "A Rust-only coding agent built around the maker's own Rust-fine-tuned model, delivered free through a Zed ACP extension, a terminal client, and a GitHub PR reviewer."
---
```
