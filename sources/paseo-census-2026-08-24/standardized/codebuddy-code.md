# Standardized differentiation extraction: CodeBuddy Code (codebuddy-code)

Run 2026-08-24 per STANDARD_PROMPT v1. Inputs: official materials only (Tencent/CodeBuddy pages listed under Sources). Note: the CN homepage and intl pricing page are client-side rendered and yielded only titles; docs pages were the richest official source.

1. **One-sentence self-description:** Tencent's AI assistant for the terminal — it understands your codebase, edits files, runs commands, and handles entire workflows, as the CLI member of a CodeBuddy family spanning plugins, IDEs, and CLI (npm description; tencentcloud.com/products/acc).

2. **Claimed differentiators** (by prominence):
   - One family across plugins, IDEs, and CLI — a "seamless development experience" with the CLI serving DevOps engineers and senior developers (integration / audience) — https://www.tencentcloud.com/products/acc
   - Tencent-scale internal proof: used by over half of Tencent's internal R&D personnel (trust-safety / performance) — https://www.tencentcloud.com/products/acc
   - Terminal-native lifecycle automation: natural-language control of editing, Git, testing, deployment; Unix-pipeline compatible; headless and SDK use (capability / workflow) — https://www.codebuddy.ai/docs/cli/overview
   - Open extensibility: plugins/skills/hooks/subagents/MCP, with the plugin system "designed to be compatible with the Claude Code plugin specification" (openness / integration) — https://www.codebuddy.ai/docs/cli/plugins-reference
   - Open protocols: first-party ACP server (`codebuddy --acp`) so any ACP editor can host it; Agent Teams status streamed over ACP (openness / integration) — https://www.codebuddy.ai/docs/cli/acp

3. **Stated audience:** CLI: "DevOps engineers and senior developers" / professional engineers; the wider family targets product managers, designers, full-stack developers, and beginners (https://www.tencentcloud.com/products/acc).

4. **Positioning against others:** Claude Code is named as the compatibility target of the plugin system ("compatible with the Claude Code plugin specification", plugins-reference); no competitor is otherwise named or disparaged in the materials read. Launch-era marketing (per family materials) claims first-in-China full-form-factor coverage.

5. **Evidence offered:** ">50% of Tencent's internal R&D personnel" use it (tencentcloud.com/products/acc); "millisecond-level code prediction" (same page). No benchmarks, external customer names, or download figures in the official materials read.

6. **Notable silences:** default permission/approval behavior; sandboxing details (mentioned only in release notes, not overview); model lineup and multi-model choice (not stated in CLI overview); open-source status/license clarity; enterprise controls in the CLI docs; pricing on the international site; uptime/security certifications.

7. **Confidence:** medium — docs are thorough on mechanics (MCP, hooks, plugins, ACP, SDK) but the marketing surfaces (codebuddy.cn, codebuddy.ai home/pricing) could not be rendered, so positioning is reconstructed mostly from docs and one Tencent Cloud product page.

Sources: https://www.tencentcloud.com/products/acc ; https://www.codebuddy.ai/docs/cli/overview ; https://www.codebuddy.ai/docs/cli/plugins-reference ; https://www.codebuddy.ai/docs/cli/acp ; https://www.codebuddy.ai/docs/cli/mcp ; https://www.codebuddy.ai/docs/cli/hooks ; https://www.codebuddy.ai/docs/cli/sub-agents ; https://registry.npmjs.org/@tencent-ai/codebuddy-code (description) ; https://www.codebuddy.cn/cli/ (title only)
