# Awesome AI Coding Agents

A curated list of AI coding assistants, agents, and frameworks — with setup guides for connecting MCP servers to each one.

The right AI tool paired with the right data sources changes everything.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Contents

- [IDE-Based Agents](#ide-based-agents)
- [Terminal-Based Agents](#terminal-based-agents)
- [Autonomous Agents](#autonomous-agents)
- [Multi-Agent Frameworks](#multi-agent-frameworks)
- [Code Review Agents](#code-review-agents)
- [Specialized Agents](#specialized-agents)
- [MCP Integration Guides](#mcp-integration-guides)

---

## IDE-Based Agents

| Agent | Editor | MCP Support | Description |
|---|---|---|---|
| [Cursor](https://cursor.sh) | VS Code fork | Native | AI-first code editor with .cursorrules and MCP |
| [GitHub Copilot](https://github.com/features/copilot) | VS Code, JetBrains, Vim | Via extensions | Code completion and chat by GitHub |
| [Windsurf](https://codeium.com/windsurf) | VS Code fork | Native | Cascade flows with deep codebase understanding |
| [Continue](https://continue.dev) | VS Code, JetBrains | Native | Open-source AI code assistant |
| [Cody](https://sourcegraph.com/cody) | VS Code, JetBrains | Via integrations | Context-aware assistant by Sourcegraph |
| [Supermaven](https://supermaven.com) | VS Code, JetBrains | Via extensions | Ultra-fast code completion |
| [Tabnine](https://tabnine.com) | Multi-editor | Via extensions | AI code completion for teams |

## Terminal-Based Agents

| Agent | MCP Support | Description |
|---|---|---|
| [Claude Code](https://claude.ai/code) | Native | Anthropic's agentic coding tool — thinks, writes, tests |
| [Aider](https://aider.chat) | Via config | Terminal pair programming with git integration |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Via tools | Autonomous software development agent |
| [Mentat](https://mentat.ai) | Via config | Terminal-based AI coding assistant |
| [GPT Engineer](https://gptengineer.app) | Via tools | Generate full codebases from prompts |
| [Sweep](https://sweep.dev) | Via GitHub | AI-powered pull request generation |

## Autonomous Agents

| Agent | MCP Support | Description |
|---|---|---|
| [Devin](https://devin.ai) | Native | Cognition's autonomous software engineer |
| [SWE-Agent](https://swe-agent.com) | Via tools | Autonomous bug-fixing agent |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | Via plugins | Self-prompting autonomous agent |
| [AgentGPT](https://agentgpt.reworkd.ai) | Via tools | Browser-based autonomous agent |
| [MetaGPT](https://github.com/geekan/MetaGPT) | Via tools | Multi-agent for software development |
| [OpenClaw](https://openclaw.ai) | Native | Personal AI assistant agent |

## Multi-Agent Frameworks

| Framework | Language | MCP Support | Description |
|---|---|---|---|
| [CrewAI](https://crewai.com) | Python | Native | Role-based multi-agent collaboration |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | Python, JS | Native | Stateful multi-agent orchestration |
| [AutoGen](https://microsoft.github.io/autogen/) | Python | Via tools | Microsoft's multi-agent framework |
| [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/) | C#, Python, Java | Via plugins | Microsoft's AI orchestration SDK |
| [Google ADK](https://google.github.io/adk-docs/) | Python | Native | Google's Agent Development Kit |
| [Dify](https://dify.ai) | Multi | Native | Low-code agent builder |
| [n8n](https://n8n.io) | Multi | Via nodes | Workflow automation with AI agents |

## Code Review Agents

| Agent | Description |
|---|---|
| [CodeRabbit](https://coderabbit.ai) | AI-powered code reviews on pull requests |
| [Codium (Qodo)](https://qodo.ai) | Test generation and code integrity |
| [Sourcery](https://sourcery.ai) | Automated Python code quality improvements |
| [Greptile](https://greptile.com) | Codebase-aware AI for code reviews |

## Specialized Agents

| Agent | Focus | Description |
|---|---|---|
| [v0](https://v0.dev) | UI/Frontend | Generates React components from prompts |
| [bolt.new](https://bolt.new) | Full-stack | Full-stack web apps from prompts |
| [Replit Agent](https://replit.com) | Full-stack | Build and deploy apps in-browser |
| [Lovable](https://lovable.dev) | Full-stack | AI-powered web app builder |
| [Claude Artifacts](https://claude.ai) | Components | Interactive component generation |
| [ChatGPT Canvas](https://chat.openai.com) | Writing/Code | Collaborative editing with AI |

---

## MCP Integration Guides

### Connecting MCP to Claude Code

```bash
# Add a memory server
echo '{"mcpServers":{"memory":{"url":"'$VINKIUS_MEM0_MCP_URL'"}}}' > .mcp.json
claude  # MCP is auto-detected
/mcp    # verify connection
```

### Connecting MCP to Cursor

1. Open Settings → MCP
2. Add server with SSE URL from [Vinkius](https://vinkius.com)
3. Restart Cursor

### Connecting MCP to CrewAI

```python
from crewai import Agent
from crewai_tools import MCPServerAdapter

tools = MCPServerAdapter(
    server_params={"url": "https://edge.vinkius.com/vk_live_xxx/mcp"}
).tools

agent = Agent(role="Researcher", tools=tools)
```

### Where to Get MCP Servers

The [Vinkius AI Gateway](https://vinkius.com) provides **2,600+ production-ready MCP servers** — deploy any of them in under a minute and receive an SSE endpoint URL.

Browse: [vinkius.com/en/categories](https://vinkius.com/en/categories)

---

## License

MIT — [Vinkius Labs](https://vinkius.com)
