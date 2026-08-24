# Standardized differentiation extraction: CodeWhale

Run 2026-08-24 against official materials only (see Sources).

1. **One-sentence self-description:** An open-source Rust coding agent for the terminal that reads the repository, edits files, runs commands, and keeps working toward a goal, improved in public with its users.

2. **Claimed differentiators** (by prominence):
   - Use the model you want: hosted providers or local models via Ollama/vLLM/SGLang, provider-neutral and unaffiliated with any model provider — model/openness — https://github.com/Hmbown/CodeWhale (README "Why Codewhale", "Project history")
   - Stay in control: read-only Plan mode; Ask/Auto-Review/Full Access approval tiers made visible; `/undo` and `/restore` snapshots — workflow/trust-safety — README
   - Keep long work organized: saved sessions, durable `/goal`, reviewable workflows, coordinated agent teams whose internal instructions stay out of the transcript — workflow — README
   - Extend the agent you already have: MCP servers, skills, hooks, agent roles as readable files — capability/integration — README
   - Community-improved in public: issues/PRs solicited, "contributors keep credit", Discord + WeChat community — openness — README

3. **Stated audience:** developers in the terminal; explicit outreach to local/self-hosted model users, Chinese-speaking community (WeChat group, CNB mirror, 18 README translations), and classrooms (docs/CLASSROOM_INSTALL.md) — README/docs.

4. **Positioning against others:** "not affiliated with any model provider" (distancing from its DeepSeek origins); Runtime API pitched for integrations "instead of screen-scraping terminal output" (alludes to TUI-wrapping integrations); Claude Code named only in a compatibility doc defining what it will NOT run — README, docs/RUNTIME_API.md, docs/CLAUDE_PLUGIN_COMPAT.md.

5. **Evidence offered for claims:** GitHub star count displayed on the site; a terminal screenshot; no benchmarks, user counts, or customer names — https://codewhale.net/, README.

6. **Notable silences:** no benchmark results; no enterprise controls or pricing of any kind; no hosted/cloud offering; no telemetry claims in README (a TELEMETRY.md exists in docs); no funding or company; sandboxing mentioned only as "optional OS sandboxing... where supported".

7. **Confidence:** high — README, an extensive docs tree, and the website agree and are current; positioning is unusually explicit (ethos, authorization order, compatibility boundaries documented).

Sources: https://github.com/Hmbown/CodeWhale (README); https://codewhale.net/; https://github.com/Hmbown/CodeWhale/blob/main/docs/RUNTIME_API.md; docs/CLAUDE_PLUGIN_COMPAT.md; docs/GUIDE.md; docs/MODES.md (listed), docs/FLEET.md (listed).
