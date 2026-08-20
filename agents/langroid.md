---
name: "Langroid"
slug: "langroid"
layout: agent.njk
maker: "langroid"
license: "MIT"
url: "https://github.com/langroid/langroid"
source_code_url: "https://github.com/langroid/langroid"
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2023-04-16"
current_release: "2026-08-18"
stars: 4101
language: "Python"
homepage: "https://langroid.github.io/langroid/"
sources:
  - "e2b"
---

`Langroid` is an intuitive, lightweight, extensible and principled Python framework to easily build LLM-powered applications. You set up Agents, equip them with optional components (LLM, vector-store and methods), assign them tasks, and have them collaboratively solve a problem by exchanging messages. This Multi-Agent paradigm is inspired by the [Actor Framework](https://en.wikipedia.org/wiki/Actor_model) (but you do not need to know anything about this!). `Langroid` is a fresh take on LLM app-development, where considerable thought has gone into simplifying the developer experience; it does not use `Langchain`. - Works with most commercial/remote and open/local LLMs. - Set up Multi-agent, multi-LLM system: use stronger LLMs for agents requiring strong reasoning and instruction-following, and delegate simpler tasks to weaker/local LLMs. - Supports OpenAI function-calling as well as native equivalent called `ToolMessage`, which works with LLMs that do not have built-in function-calling. Simply specify structure as a (nested) Pydantic object. - Batteries-included: vector-databases for RAG (Retrieval-Augmented Generation), caching, logging/observability. - Specialized agents available: `DocChatAgent`, `SQLChatAgent`, `TableChatAgent` (for tabular data, e.g. csv/dataframes). - `DocChatAgent` handles text, PDF, Docx files/URLS, and has state-of-the art techniques for retrieval combining lexical and semantic search. - Documentation: https://langroid.github.io/langroid/ </details>
