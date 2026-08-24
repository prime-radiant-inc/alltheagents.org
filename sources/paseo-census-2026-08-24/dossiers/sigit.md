# Dossier: siGit Code (census_slug: sigit)

Compiled 2026-08-24 (task-dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Small project — research kept proportionate. NOT currently in the census — proposed new-entry frontmatter at the end.

## 1. Identity

- name: siGit Code (repo `getsigit/sigit`, binary/crate `sigit`; crate self-description: "siGit Code — ACP-compatible AI coding agent. Sí, git.") [S2] (as-of 2026-08-24)
- maker: company — copyright "© 2026 PT Sigit Mitra Bangun (siGit Code & Deploy)" (Indonesian PT entity), distribution credited to "Splitfire AB" (Swedish AB, https://5mb.app / smbCloud) [S3]. GitHub org `getsigit` ("siGit Code & Deploy", location Sweden, 6 followers, created 2026-04-11) [S4]. Dual-entity structure; org form: company.
- product URL: https://sigit.si (site tagline "Git hosting for the AI era" — the site is primarily the siGit git-hosting platform; the agent lives at code.sigit.si and the repo) [S5]; repo homepage field points to Zed's ACP directory listing https://zed.dev/acp/agent/sigit [S1]
- repo URL: https://github.com/getsigit/sigit
- license: Apache-2.0 (LICENSE file in repo is the Apache 2.0 text; crates.io newest version says Apache-2.0; GitHub API reports "NOASSERTION", likely from a modified appendix) [S6][S2][S1] (as-of 2026-08-24)
- open source? True. source_available: True — agent source in the repo, published as crate `sigit` [S1][S2]
- first public release: repo created 2026-03-19 [S1]; first crates.io publish 2026-04-12 [S2]; first npm publish (`@smbcloud/sigit` 0.1.1) 2026-04-24 [S9]. Very young project (~5 months old).
- latest release: v1.5.2, 2026-08-11 (GitHub release, crates.io, and npm all agree); 6 GitHub releases listed, oldest shown v1.3.2 2026-07-04 [S7][S2][S9] (as-of 2026-08-24)
- what it is:
  - Form factor: local CLI agent with two modes — ACP mode for editor integration (Zed, Xcode via `--acp`, VS Code via extension/ACP client) and interactive terminal chat mode [S3] (as-of 2026-08-24).
  - Models: local-LLM-first and locked to local inference — repo description "A local-Llm-first coding agent. Runs Qwen 2.5 and Qwen 3"; downloads GGUF models from Hugging Face (~1-2 GB); Zed listing mentions "on-device LLM inference via Onde"; README claims "No API keys, no cloud round-trips, no subscription"; no cloud provider support mentioned (researched in README, absent) [S1][S3][S8].
  - Pricing: free to self-host, open source; a hosted version is referenced at code.sigit.si [S3].
  - Install: `cargo install sigit`; `npx @smbcloud/sigit`; prebuilt binaries for macOS/Linux/Windows (arm64+x64); README also claims Homebrew, pip, and uv but no `sigit` package exists on PyPI (an unrelated Kivy Git GUI holds the name) and no Homebrew formula was verified — treat brew/pip/uv as maker-claimed/unverified [S3][S9][S10] (as-of 2026-08-24).
  - Default autonomy: not documented in the README — no description of edit/shell permission prompts found (researched, absent) [S3].
  - Language: Rust [S1]. Tied to the maker's own ecosystem: "more useful" on smbCloud repos ("Git hosting built for AI workflows"); model cache shared with a desktop app on macOS [S3].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 32 | 2026-08-24 | [S1] | independently observable |
| GitHub forks | 2 | 2026-08-24 | [S1] | independently observable |
| GitHub watchers (subscribers) | 0 | 2026-08-24 | [S1] | independently observable |
| Contributors | 4: paydii (168), setoelkahfi (118), claude (25), keypair34 (11) — a "claude" bot account is the #3 committer | 2026-08-24 | [S11] | independently observable |
| crates.io downloads `sigit` | 341 all-time; 297 recent (~90d); 16 versions | 2026-08-24 | [S2] | independently observable |
| npm downloads `@smbcloud/sigit` | 450/week, 1,803/month | 2026-08-24 | [S9] | independently observable |
| GitHub release-asset downloads | v1.5.2: ~4,570 total (Linux amd64 1,407; Windows amd64 1,228; arm64 ~970 each; macOS 0). Pattern (thousands on Linux/Windows, zero on macOS) looks CI/bot-driven rather than organic users | 2026-08-24 | [S7] | independently observable (interpret with caution) |
| Ecosystem listings | Zed's official ACP agent directory (zed.dev/acp/agent/sigit); Paseo ACP catalog (per task framing) | 2026-08-24 | [S8] | independently observable |
| Maker usage claims | none found — no user/customer numbers on sigit.si or README | 2026-08-24 | [S5][S3] | researched, absent |
| Funding / press / community server / benchmarks | none found (no Discord linked, no funding announcements, no benchmark placements located) | 2026-08-24 | [S5][S3] | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — `mcp.toml` with `[[server]]` sections defines external MCP servers siGit connects to; README example uses `xcrun mcpbridge` to reach Xcode build tools [S3] (as-of 2026-08-24). Evidence: https://github.com/getsigit/sigit (README, Xcode section).
- plugin_support: **False** — no plugin/extension/skills system of its own found; extensibility is via the standard protocols (ACP outward, MCP inward) [S3] (researched, absent).
- claude_code_plugin: **no** — no mention of CLAUDE.md, `.claude/` dirs, or Claude Code plugin/skills format [S3] (researched, absent).
- subagents: **False** — not mentioned [S3] (researched, absent).
- hooks: **False** — not mentioned [S3] (researched, absent).
- plan_mode: **False** — not mentioned [S3] (researched, absent).
- plugin_docs_url: none (no plugin system). config_docs_url: docs.sigit.si (site docs link; agent-specific config docs not separately located) [S5].
- ACP support: **yes, first-party and central to the product** — ACP mode is one of its two operational modes; listed in Zed's ACP registry; repo topics include `agent-client-protocol` [S3][S8][S1].
- SDK: **False** — none found (researched, absent).

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (README, verbatim): "It runs on your machine, not someone else's. No API keys, no cloud round-trips, no subscription." [S3]
- crate description (verbatim): "siGit Code — ACP-compatible AI coding agent. Sí, git." [S2]
- maker claims (paraphrased):
  1. Fully local: on-device GGUF inference (Qwen 2.5/3 via "Onde"), private by construction, no API keys or subscription [S1][S3][S8].
  2. ACP-native editor integration: Zed, Xcode, VS Code through one protocol [S3][S8].
  3. Ecosystem synergy: works anywhere but is "more useful" on the maker's smbCloud git hosting (pre-understands Rust workspace layouts, deploy flows, auth boundaries) [S3].
  4. MCP client for external tools (e.g. Xcode's mcpbridge) [S3].
  5. Model-cache sharing with the maker's desktop app on macOS [S3].
- audience: developers who want local/private AI coding, especially Rust developers and smbCloud users [S3]. The parent sigit.si platform targets "your AI coding agent" workflows ("Git hosting for the AI era", "Agent-ready") [S5].

## 5. Company & contact targets (PRI-2929)

- Legal entities (as publicly stated in the repo): PT Sigit Mitra Bangun (copyright holder, Indonesia-style PT entity) and Splitfire AB (distributor, Sweden; runs 5mb.app/smbCloud) [S3]. GitHub org located "Sweden" [S4]. Approx size: no team page found; contributor graph suggests 2-3 people (researched, size not published).
- Publicly named leadership: none found on sigit.si (no team page, no bylined launch post located) [S5]. Top human contributors' public GitHub identities: paydii, setoelkahfi, keypair34 [S11]. No further identification per instructions.
- Funding stage: none found (researched, absent).

## 6. Open questions / conflicts

- License: GitHub API says NOASSERTION, but the LICENSE file is verbatim Apache-2.0 and crates.io records Apache-2.0 — record Apache-2.0 [S6][S2][S1].
- Install claims: README lists Homebrew/pip/uv/npm, but plain `sigit` exists on neither npm nor PyPI (npm 404; PyPI `sigit` is an unrelated Kivy git GUI). Real npm package is `@smbcloud/sigit`. Brew/pip/uv unverified [S9][S10][S3].
- Release-asset download counts (~4.5k on the latest release) conflict with tiny stars (32) and crate downloads (341) — macOS at exactly 0 while Linux/Windows are in the thousands strongly suggests CI or mirror traffic, not users.
- "Onde" (the on-device inference engine named in the Zed listing) was not further researched — null.
- Exact Qwen variants/sizes and the permission model of the agentic loop are not documented in the README — null/absent.
- Relationship between PT Sigit Mitra Bangun (ID) and Splitfire AB (SE) is stated only as copyright vs. distribution — corporate structure unresearched (null).
- The word "sigit" is a common Indonesian given name; older unrelated projects share the name (PyPI collision) — disambiguation matters for search-based metrics.

## 7. Sources

1. [S1] https://api.github.com/repos/getsigit/sigit — stars, dates, description, license field, topics, homepage
2. [S2] https://crates.io/api/v1/crates/sigit — crate downloads, versions, license, dates
3. [S3] https://raw.githubusercontent.com/getsigit/sigit/main/README.md — features, install, MCP, copyright, claims
4. [S4] https://api.github.com/users/getsigit — org identity, location, followers
5. [S5] https://sigit.si — platform positioning, taglines, docs link
6. [S6] https://raw.githubusercontent.com/getsigit/sigit/main/LICENSE — Apache-2.0 text
7. [S7] https://api.github.com/repos/getsigit/sigit/releases — 6 releases, v1.5.2, asset download counts
8. [S8] https://zed.dev/acp/agent/sigit — Zed ACP directory listing, npx command, "Onde"
9. [S9] npm registry + downloads API for `@smbcloud/sigit` (and 404 for `sigit`) — npm package identity and downloads
10. [S10] https://pypi.org/pypi/sigit/json — name collision: unrelated Kivy Git GUI
11. [S11] https://api.github.com/repos/getsigit/sigit/contributors — contributor distribution

## Inclusion check (Jesse's test)

**Yes** — siGit Code is a coding agent with its own agentic loop in Rust, running its own on-device LLM inference (Qwen GGUF models) rather than wrapping another vendor's agent; its ACP mode exposes that native loop to editors [S1][S3][S8].

## Proposed census entry (new; per hc/agents/_TEMPLATE.md)

```yaml
---
name: "siGit Code"
slug: "sigit"
layout: "agent.njk"
category: "agent"
maker: "sigit"              # new makers.json record: maker_type company, country SE (distribution; copyright entity ID), makes_models false, revenue_model []
license: "Apache-2.0"
url: "https://sigit.si"
source_code_url: "https://github.com/getsigit/sigit"
source_available: true
homepage: "https://sigit.si"
docs_url: "https://docs.sigit.si"
download_url: "https://github.com/getsigit/sigit/releases"
install_method: "cargo install sigit; npx @smbcloud/sigit; prebuilt binaries"
platforms: ["CLI", "IDE"]           # IDE via ACP (Zed/Xcode/VS Code)
autonomy_level: ["agentic"]
specialization: "general"           # local-first is a posture, not a domain; Rust-ecosystem leaning
language: "Rust"
first_released: "2026-04-12"        # first crates.io publish; repo created 2026-03-19
current_release: "2026-08-11"       # v1.5.2
maintained: "active"
mcp_support: "client (mcp.toml [[server]] config)"
plugin_support: false
claude_code_plugin: false
subagents: false
hooks: false
plan_mode: false
plugin_docs_url: null
config_docs_url: "https://docs.sigit.si"
model_providers: "locked — local on-device GGUF (Qwen 2.5/3) only"
pricing: "free"
github_stars: "32"
sources: ["paseo-acp-catalog", "zed-acp-registry"]
last_verified: "2026-08-24"
what_makes_it_special: "A fully local coding agent that ships its own on-device Qwen inference — no API keys or cloud calls — and speaks ACP to Zed, Xcode, and VS Code."
---
```
