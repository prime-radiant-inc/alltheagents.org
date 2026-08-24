# Standardized differentiation extraction: GLM Agent / glm-acp-agent (2026-08-21)

Inputs: official materials only — GitHub README, repo description, npm package page. No homepage, docs site, or launch post exists.

1. **One-sentence self-description:** An Agent Client Protocol agent written in TypeScript that uses the Z.AI / Zhipu AI GLM Coding Plan model family (GLM-5.3, GLM-5 Turbo, GLM-4.7) as its reasoning core.

2. **Claimed differentiators** (by prominence):
   - Uses GLM Coding Plan models as the reasoning core inside any ACP-compatible editor — the defining claim (model / integration) — https://github.com/stefandevo/glm-acp-agent
   - "Full ACP compliance" with real-time streaming over stdio (capability / integration) — https://github.com/stefandevo/glm-acp-agent
   - Thinking-mode integration: chain-of-thought / reasoning-token visibility in the client (capability) — https://github.com/stefandevo/glm-acp-agent
   - Session persistence and per-session switching among the three GLM models (workflow) — https://github.com/stefandevo/glm-acp-agent
   - Graduated permission modes: default (prompt on writes/commands), accept_edits, bypass_permissions (trust-safety) — https://github.com/stefandevo/glm-acp-agent

3. **Stated audience:** developers on the Z.AI GLM Coding Plan who want those models in an ACP editor (Zed recommended) — https://github.com/stefandevo/glm-acp-agent. No role/team-size claims: not claimed.

4. **Positioning against others:** not claimed — no competitor or category named; positioning is implicit (a native GLM agent rather than a wrapper, and an ACP citizen rather than a standalone CLI).

5. **Evidence offered:** none offered — no benchmarks, numbers, customers, or demos; the materials are descriptive (tool list, model specs, config snippets).

6. **Notable silences:** user-configurable MCP servers (only built-in Z.AI web/vision MCP mentioned); skills/plugins; subagents; hooks; plan mode; multi-provider support (locked to Z.AI by design); sandboxing; enterprise controls; any Zhipu endorsement or official status.

7. **Confidence:** medium — a single thorough README is the only material, but it is specific and technical, so the self-description is likely accurate; there is simply no broader positioning to capture.

Sources: https://github.com/stefandevo/glm-acp-agent (README + repo description) ; https://www.npmjs.com/package/glm-acp-agent
