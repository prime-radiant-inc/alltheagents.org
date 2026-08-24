# Standardized differentiation extraction: Kimi Code CLI (census_slug: kimi-code-cli)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: An open-source (MIT) AI coding agent that runs in your terminal — reading and editing code, running shell commands, searching files, and fetching web pages, choosing its next step from the feedback it receives — working out of the box with Moonshot AI's Kimi models and configurable for other compatible providers. (README; docs getting-started)

2. Claimed differentiators (by prominence):
   - Single-binary distribution with "blazing-fast startup": one install command, no Node.js setup or global-module conflicts; TUI ready in milliseconds. Kind: workflow / performance (of the tool, not the model). https://github.com/MoonshotAI/kimi-code
   - Purpose-built TUI "optimized end to end for long, focused agent sessions". Kind: workflow. https://github.com/MoonshotAI/kimi-code
   - Video input: drop a screen recording or demo clip into the chat — "turn a reference clip into a LUT... a screen recording into working code". Kind: capability. https://github.com/MoonshotAI/kimi-code
   - Editor/IDE integration via the Agent Client Protocol: `kimi acp` lets Zed, JetBrains, or any ACP client (docs also name Paseo) drive a session over stdio. Kind: integration / openness. https://github.com/MoonshotAI/kimi-code ; https://moonshotai.github.io/kimi-code/en/guides/ides
   - Extensibility bundle: AI-native MCP configuration (`/mcp-config`, conversational, no hand-edited JSON), a plugin marketplace with per-install trust levels (skills, MCP servers, data sources), built-in `coder`/`explore`/`plan` subagents in isolated contexts, and lifecycle hooks to gate risky tool calls. Kind: capability / trust-safety. https://github.com/MoonshotAI/kimi-code ; https://moonshotai.github.io/kimi-code/en/customization/plugins

3. Stated audience: developers using the terminal for "software development tasks and day-to-day terminal operations" (writing/modifying code, understanding projects, automating tasks); bilingual English/Chinese docs; the product page frames Kimi Code as a code-development subscription benefit compatible with diverse dev workflows. No role/team-size segmentation claimed. https://moonshotai.github.io/kimi-code/en/guides/getting-started ; https://www.kimi.com/code/

4. Positioning against others: no competitor named in README or docs. Closest allusions: install works with "No Node.js required" (contrast with npm-installed CLIs, unstated); the tagline "The Starting Point for Next-Gen Agents"; a built-in `/import-from-cc-codex` command to "Import Claude Code and Codex instructions, skills, and MCP settings" — acknowledging those tools as the incumbents users switch from. https://github.com/MoonshotAI/kimi-code ; https://moonshotai.github.io/kimi-code/en/reference/slash-commands

5. Evidence the maker offers for its claims: an internal case study — Moonshot AI used Kimi Code CLI (with Kimi K2.5) to ship a visual refactor of moonshot.ai, describing MCP-to-Figma alignment and a custom review skill (2026-08-12, https://www.kimi.ai/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli). The product page cites the Kimi K3 model (1M context) as the engine. No user counts, benchmark scores, or customer names appear in the CLI's README or docs.

6. Notable silences: no adoption or user numbers; no harness benchmark results (SWE-bench, Terminal-Bench) in CLI materials; no sandboxing/OS-isolation claim (permissions are approval-based; hooks are explicitly fail-open and "should not be used as the sole security barrier"); no enterprise controls (SSO, managed policy, audit); no cloud/background-agent offering (local `kimi web` server only, marked experimental); no CLAUDE.md compatibility claim (workspace instructions use AGENTS.md); multi-model support exists in docs but is not front-page positioning; no pricing on the README/docs (pricing lives on the kimi.com membership page).

7. Confidence: medium-high — the README, extensive bilingual docs, and product page are consistent and current (releases through 0.38.0, 2026-08-20), but there is no discoverable launch post or manifesto from Moonshot for the CLI itself, so prominence ordering is inferred from the README's own feature ordering.

Sources:
- https://github.com/MoonshotAI/kimi-code (README)
- https://moonshotai.github.io/kimi-code/en/guides/getting-started
- https://moonshotai.github.io/kimi-code/en/guides/interaction
- https://moonshotai.github.io/kimi-code/en/guides/ides
- https://moonshotai.github.io/kimi-code/en/guides/server
- https://moonshotai.github.io/kimi-code/en/customization/plugins
- https://moonshotai.github.io/kimi-code/en/customization/mcp
- https://moonshotai.github.io/kimi-code/en/customization/skills
- https://moonshotai.github.io/kimi-code/en/customization/agents
- https://moonshotai.github.io/kimi-code/en/customization/hooks
- https://moonshotai.github.io/kimi-code/en/configuration/providers
- https://moonshotai.github.io/kimi-code/en/reference/kimi-acp
- https://moonshotai.github.io/kimi-code/en/reference/slash-commands
- https://moonshotai.github.io/kimi-code/en/release-notes/changelog
- https://www.kimi.com/code/
- https://www.kimi.ai/resources/shipping-a-refactor-of-moonshot-ai-with-kimi-code-cli
- https://github.com/MoonshotAI/kimi-cli (README, legacy deprecation notice)
