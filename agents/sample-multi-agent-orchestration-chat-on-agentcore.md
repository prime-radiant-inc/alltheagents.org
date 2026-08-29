---
name: "sample-multi-agent-orchestration-chat-on-agentcore"
slug: "sample-multi-agent-orchestration-chat-on-agentcore"
layout: "agent.njk"
category: "multiplexer"
maker: "aws-samples"
license: "MIT-0"
url: "https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore"
source_code_url: "https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore"
source_available: "True"
platforms: []
first_released: "2026-05-17"
current_release: "2026-08-19"
stars: "123"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Amazon Bedrock (Anthropic Claude)"
pricing: "~$84/month for 100 chat sessions (5 turns each); ~$1/month when idle; no upfront or fixed compute costs"
install_method: "npm ci; npx -w packages/cdk cdk bootstrap; npm run deploy; requires Node.js 22.12.0+ and AWS CLI"
docs_url: "https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aws-samples/sample-multi-agent-orchestration-chat-on-agentcore"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Multi-agent orchestration chat platform built on Amazon Bedrock AgentCore; enables teams to create, customize, and share AI agents across an organization; includes preset agents (Software Developer, Data Analyst, Physicist); supports event-driven automation, extensible tools, JWT/Cognito auth, persistent memory; proof-of-concept (PoC)"
---

The sample demonstrates how an organization stands up a shared agent workspace on AWS: teams create custom agents, discover and reuse colleagues' agents, and trigger any of them from schedules or GitHub webhooks. Preset agents such as Software Developer and Data Analyst ship with tool access to command execution, web search, and GitHub, and agents persist context through AgentCore's short- and long-term memory. Everything deploys from one repository via CDK — React on CloudFront, Express on Lambda, DynamoDB and S3 storage, AppSync WebSockets for streaming — with Cognito JWTs for access control. The repository is explicit that this is a proof of value for a few hundred users, not production software, and may change without backward compatibility. AWS customers evaluating internal agent platforms are the intended audience.
