# Standardized differentiation extraction: MiniMax Code (census_slug: minimax-code)

Run 2026-08-21 per STANDARD_PROMPT v1. Inputs: official MiniMax materials only (listed under Sources).

1. **One-sentence self-description**: A desktop AI-agent app (macOS/Windows) with a companion terminal CLI that does software development, everyday workflows, automation, and remote collaboration — combining chat, project context, file operations, terminal sessions, browser previews, skills, memory, and automation in one local workspace.

2. **Claimed differentiators** (in order of prominence):
   - Agent Team: describe a goal once and the product coordinates decomposition, delegation, execution, verification, and synthesis across specialized agents ("builds Agent teams" leads the tagline) — capability — https://github.com/MiniMax-AI/minimax-code ; https://agent.minimax.io/docs/code/agents/team
   - Memory of habits: "Remembers your habits" — retains preferences, project conventions, and long-term working patterns — capability — https://github.com/MiniMax-AI/minimax-code ; https://agent.minimax.io/docs/code/agents/memory
   - Automation and long-horizon autonomy: "automates the repetitive work" — scheduled/recurring tasks plus "Goal", which keeps working until a verifiable outcome is achieved or progress is blocked — workflow — https://agent.minimax.io/docs/code/automation/schedules ; https://agent.minimax.io/docs/code/desktop/goal
   - Remote collaboration: check progress, add instructions, and approve permission requests from a phone (Remote Control) or via Telegram/WeChat/Lark/Feishu messaging integrations — integration — https://agent.minimax.io/docs/code/automation/remote-control ; https://agent.minimax.io/docs/code/automation/im
   - Broader-than-coding scope: separate Coding and Work modes (development vs research/documents/everyday workflows), a domain Plugin Marketplace (financial data, company lookup, legal search, knowledge, Office), and a built-in browser — audience/capability — https://agent.minimax.io/docs/code/workflows/modes ; https://agent.minimax.io/docs/code/agents/plugins

3. **Stated audience**: Developers for Coding mode and the CLI ("the CLI stays close to code repositories, terminals, scripts, CI, and editors"); general users for Work mode ("research, documents, and everyday workflows"). No team size or stack named. — https://agent.minimax.io/docs/cli/features ; https://agent.minimax.io/docs/code/workflows/modes

4. **Positioning against others**: not claimed. No competitor is named. The materials position the CLI against the desktop app internally ("the app is well suited to visual task management... while the CLI stays close to code repositories") and integrate the desktop with editors/clients only generically via ACP. (MiniMax's platform docs separately show its models configured inside Claude Code, Cursor, Codex, etc., but the MiniMax Code materials themselves make no comparative claim.)

5. **Evidence offered for claims**: essentially none for the harness itself — no benchmarks, user counts, or customer names in the MiniMax Code materials. Named plugin partners (Hundsun, Qichacha, EverMe, PKUlaw, WPS, WeCom) at https://agent.minimax.io/docs/code/agents/plugins ; an engineering blog explains Agent Team design and cost tradeoffs (https://agent.minimax.io/docs/techblog/agent-team). Model-level claims (e.g., M3 SWE-Bench Pro 59.0% at https://www.minimax.io/models/text/m3) sit outside the MiniMax Code materials.

6. **Notable silences**: no hooks/lifecycle events (explicitly excluded from the plugin contract); no SDK; no sandboxing story beyond permission prompts; no enterprise controls (SSO, policy, audit); no multi-model marketing (BYOK exists but is documented as a settings feature, not a pitch); no open-source claim for the harness; no benchmark or adoption numbers for the harness; Linux desktop absent (CLI covers Linux); no IDE extension; MCP and Plan Mode exist but are documented as features rather than claimed as differentiators.

7. **Confidence**: **medium-high** — the docs site is thorough and current (changelogs to 2026-08-19/22), and the tagline plus docs cards give a clear prominence ordering; but the product is weeks old in CLI form, there is no launch blog post or pricing page dedicated to MiniMax Code itself, and desktop/web/CLI branding overlaps with "MiniMax Agent", so positioning may still be settling.

Sources:
- https://github.com/MiniMax-AI/minimax-code (README — tagline, downloads)
- https://agent.minimax.io/docs/code/welcome.md (product overview)
- https://code.minimax.io/docs/llms.txt (full docs index)
- https://agent.minimax.io/docs/cli/quick-start.md and /docs/cli/features.md (CLI: TUI, headless, ACP, plan mode, permissions)
- https://agent.minimax.io/docs/code/agents/team.md, /plugins.md, /mcp.md, /memory.md (agents, marketplace, MCP, memory)
- https://agent.minimax.io/docs/code/automation/schedules.md, /remote-control.md, /im.md (automation, remote)
- https://agent.minimax.io/docs/code/workflows/permissions.md (safety)
- https://agent.minimax.io/docs/changelog.md (desktop v3.0.20..v3.0.66; CLI tab)
- @minimax-ai/code npm package README/CHANGELOG (official, Chinese-language CLI reference)
- https://platform.minimax.io/docs/guides/pricing-token-plan.md (Token Plan pricing)
- https://github.com/MiniMax-AI/MiniMax-Code-Plugins (docs/plugin-compatibility.md — plugin contract)
- https://agent.minimax.io/docs/techblog/agent-team.md (Agent Team blog)
