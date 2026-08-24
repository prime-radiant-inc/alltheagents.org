# Standardized differentiation extraction: Dirac (census_slug: dirac)

Run 2026-08-24 per STANDARD_PROMPT.md v1. Official materials only (see Sources).

1. **One-sentence self-description:** An open-source coding agent that curates context tightly so it completes complex, multi-file coding tasks more accurately while cutting API costs by roughly two-thirds versus other agents.

2. **Claimed differentiators:**
   - Token efficiency: ~64.8% average API-cost reduction versus competing agents at equal or better output quality — kind: price / performance — https://github.com/dirac-run/dirac ; https://dirac.run/
   - Benchmark leadership: 65.2% on Terminal-Bench-2 with gemini-3-flash-preview, beating Google's own baseline (47.6%) and the top closed-source agent (Junie CLI, 64.3%), without benchmark-specific tuning — kind: performance — https://github.com/dirac-run/dirac
   - Editing mechanics: hash/line-anchored parallel edits that stay stable across changes, AST-native manipulation for "100% syntactic accuracy", multi-file batching for "2.8x faster execution" — kind: capability — https://dirac.run/ ; https://github.com/dirac-run/dirac
   - Native tool calling only, no MCP — framed as a reliability and performance choice — kind: trust-safety / capability — https://github.com/dirac-run/dirac
   - Reproducible openness: Apache-2.0, head-to-head eval diffs against named open-source agents published in-repo, "reproducible by anyone" — kind: openness — https://github.com/dirac-run/dirac

3. **Stated audience:** "Terminal-first" is not claimed; the repo description implies developers doing complex real-world refactors who care about API cost; benchmarked explicitly against "other leading open-source agents" — https://github.com/dirac-run/dirac. Otherwise not claimed.

4. **Positioning against others:** Names competitors directly and repeatedly: eval table vs Cline, Kilo, Ohmypi, Opencode, Pimono, Roo; calls Cline "the parent repo"; contrasts with "Google's official baseline" and "top closed-source agent Junie CLI"; defines itself against MCP-based agents ("Oh, and no MCP.") — https://github.com/dirac-run/dirac

5. **Evidence offered:** Terminal-Bench-2 leaderboard submission (HF discussion link); a 7-task eval table with per-task cost figures and clickable diffs stored in the repo; a disclosed upstream Cline cost-accounting bug affecting its own numbers (with links to the issue and fix PR) — https://github.com/dirac-run/dirac

6. **Notable silences:** MCP (explicitly rejected rather than silent), subagents/orchestration, lifecycle hooks, sandboxing/isolation of shell commands, enterprise controls, pricing/paid plans, team features, desktop app, multi-model routing within a task, memory across sessions.

7. **Confidence:** high — the README is detailed, quantitative, and consistent with the homepage; positioning (cost + accuracy via context curation, anti-MCP) is stated explicitly and repeatedly, with named competitors.

Sources: https://dirac.run/ ; https://github.com/dirac-run/dirac (README, master) ; https://www.npmjs.com/package/dirac-cli (metadata)
