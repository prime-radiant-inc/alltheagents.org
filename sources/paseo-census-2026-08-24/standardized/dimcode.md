# Standardized differentiation extraction: DimCode / DimAgent (census_slug: dimcode)

Run 2026-08-24 per STANDARD_PROMPT.md v1. Official materials only (see Sources).

1. **One-sentence self-description:** A single agent runtime usable everywhere — desktop app, terminal TUI, headless scripts, and ACP-connected editors — with any model provider, running local-first on your machine.

2. **Claimed differentiators:**
   - One agent runtime behind three entry points (desktop / CLI+headless / ACP editor server); state lives in the runtime, frontends only handle interaction — kind: workflow / integration — https://dimcode.dev/
   - Bring your own model: 30+ providers, cloud and local (Ollama/LM Studio) treated identically with uniform behavior — kind: model / openness — https://dimcode.dev/
   - Cache-friendly context management: stable system prompt, fixed tool definitions, fixed history prefix; claimed 98% KV-cache reuse on DeepSeek V4 and 90%+ elsewhere, so iteration is cheap — kind: performance / price — https://dimcode.dev/
   - Reliable unattended runtime: layered error recovery, auto context compaction, blob offload, async multi-agent orchestration with per-subagent model choice and sandboxing; "20+ hours" without babysitting — kind: capability — https://dimcode.dev/
   - Local-first trust posture: SQLite storage in ~/.dimcode, credentials in OS keychain, no forced cloud backend, structured local traces with step replay — kind: trust-safety — https://dimcode.dev/

3. **Stated audience:** "Terminal-first teams" (GitHub repo description); roadmap "Coding Plan" targets teams (collaboration, central permission management, usage dashboards) — https://github.com/arcships/dimcode ; https://dimcode.dev/

4. **Positioning against others:** "Not just another chat box" ("不只是又一个对话框") — positions against chat-UI assistants as a category; no competitor named — https://dimcode.dev/

5. **Evidence offered:** A measured-sounding number: "DeepSeek V4 measured 98% KV-cache reuse", "all major models 90%+" (no methodology published). Partner/credit logos: CC Switch, Vercel AI SDK, Bun, Electron. No benchmarks, customers, or user counts — https://dimcode.dev/

6. **Notable silences:** open source / license (never addressed; no LICENSE published), sandboxing of shell commands beyond approvals, enterprise controls (SSO, audit for orgs — only roadmap "Coding Plan"), benchmark results, pricing of "cloud features" behind `dim auth login`, model-vendor partnerships, security disclosures policy.

7. **Confidence:** medium — the homepage is a rich, claim-dense launch-style page and the npm README is thorough, but there is no launch post or blog, docs are thin (5 guide pages), and the zh-CN homepage was machine-read in translation, so emphasis ordering may be imperfect.

Sources: https://dimcode.dev/ ; https://dimcode.dev/docs/acp.html ; npm README (dimcode@0.3.19) ; https://github.com/arcships/dimcode (README)
