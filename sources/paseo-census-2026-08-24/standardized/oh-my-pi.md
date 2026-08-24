# Standardized differentiation extraction — Oh My Pi (omp) — census_slug `oh-my-pi`

Run 2026-08-21 against the harness's own materials only (README, omp.sh index metadata, repo docs, maker blog post). Where the materials are silent: "not claimed".

1. **One-sentence self-description:** A terminal coding agent, forked from Pi, with IDE-grade capabilities (LSP, debugger, subagents, plan mode, memory, hash-anchored edits, stream rules) built in and backed by a native Rust engine. (README header "A coding agent with the IDE wired in"; omp.sh meta description.)

2. **Claimed differentiators** (ordered by prominence in README):
   - Per-model-tuned tool harness: hash-anchored ("hashline") edits, summarizing reads, in-process search and tuned prompts raise pass rates and cut tokens for any model; the maker's own benchmark table is the headline (e.g. Grok Code Fast 1 6.7% -> 68.3%, Grok 4 Fast -61% output tokens, MiniMax 2.1x). Kind: performance / capability. Source: https://github.com/can1357/oh-my-pi (section "Every tool, benchmaxxed"); https://stencil.so/blog/the-harness-problem
   - IDE wired in: LSP on every write (renames, references, diagnostics; 14 ops), real debugger control via DAP (lldb/dlv/debugpy; 28 ops), persistent Python/JS execution cells that call back into agent tools, browser and desktop control. Kind: capability. Source: https://github.com/can1357/oh-my-pi (sections 01–03, 20–21)
   - Native Rust engine (~80k LoC; grep, glob, bash with in-process coreutils, AST, PTY, desktop) with no fork/exec, single binary on macOS/Linux/Windows. Kind: performance / capability. Source: https://github.com/can1357/oh-my-pi (section 09; "Roughly ~80,000 lines of Rust")
   - Orchestration built in: first-class subagents in isolated worktrees with typed results, Agent Hub, a second "advisor" model reviewing every turn, /review with P0–P3 verdicts, time-traveling stream rules that correct the model mid-stream. Kind: workflow / capability. Source: https://github.com/can1357/oh-my-pi (sections 04–06, 10)
   - Open and interoperable: 60+ providers with roles/fallbacks, MIT/all-TypeScript extensibility where extensions use the same APIs as built-ins, four entry points (TUI, one-shot, RPC, ACP) plus SDK, and native reading of other tools' configs (.claude/.cursor/.codex/.cline/... , Claude Code marketplace format). Kind: openness / integration / model. Source: https://github.com/can1357/oh-my-pi ("Sixty-plus providers", "A harness worth keeping", section 15); https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/marketplace.md

3. **Stated audience:** not claimed as a role or segment. README sign-off "made for terminals that stay open" implies terminal-centric individual developers; the blog post addresses people building coding agents. Source: https://github.com/can1357/oh-my-pi ; https://stencil.so/blog/the-harness-problem

4. **Positioning against others:** Yes. Explicitly positions as a fork that adds "batteries included" to Pi ("The Pi you love, with batteries included"); repeatedly contrasts with unnamed "other harnesses" / "most agents" / "every other agent" (shell out to rg/grep, bolt on gh_* tools, "sprinkling print statements", ship importers). Names Zed as ACP host. omp.sh sitemap lists comparison pages /vs/claude-code, /vs/cursor, /vs/cline (content not retrievable). Source: https://github.com/can1357/oh-my-pi ; https://omp.sh/sitemap.xml

5. **Evidence offered:** maker-run edit-format benchmark (180 tasks, 16 models, 3 runs; hashline wins 14/16, avg +15 pts) — https://stencil.so/blog/the-harness-problem ; README benchmark table; embedded TUI capture images/video clips for each feature (omp.sh/clips/*.mp4, omp.sh/captures/*.webp); component counts (60+ providers, 31 tools, 14 LSP ops, 28 DAP ops, ~80k Rust LoC, 23 search backends). No customer names, user counts, or third-party benchmarks offered.

6. **Notable silences:** no sandboxing/isolation story for the main agent (only subagent worktree isolation and an approval-mode doc that defaults to auto-approve); no enterprise controls (SSO, audit, telemetry policy, org admin) — only a self-hosted auth broker/gateway for credentials; no pricing/hosted tier (free only); no privacy/data-handling statement on README; no benchmark placements on public suites (SWE-bench etc.); no team/company page for Stencil Labs; no roadmap or stability/versioning policy despite multiple releases per day; no explicit security model for the browser/desktop/Slack-driving tools beyond approval tiers.

7. **Confidence:** medium-high. README is long and explicit about claims and is the primary marketing surface; omp.sh homepage/docs are a client-rendered SPA whose body could not be read, so the site's own framing (including the /vs pages) may add positioning not captured here; there is a single maker blog post (2026-02-12) and no located launch/announcement post.

Sources:
- https://github.com/can1357/oh-my-pi (README, fetched 2026-08-21 via raw.githubusercontent.com)
- https://omp.sh (index HTML title/meta description/JSON-LD only; body is SPA)
- https://omp.sh/sitemap.xml
- https://stencil.so/blog/the-harness-problem (maker blog post, 2026-02-12; redirect target of https://blog.can.ac/2026/02/12/the-harness-problem/)
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/marketplace.md
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/approval-mode.md
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/extensions.md
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/sdk.md
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/auth-broker-gateway.md
- https://raw.githubusercontent.com/can1357/oh-my-pi/main/CONTRIBUTING.md
