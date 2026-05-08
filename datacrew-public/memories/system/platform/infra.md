---
description: Where I run, what tools I have, and how to use them.
---

# Platform Infrastructure

## Running Location

- **Host:** VPS (Hostinger) — `letta-code-channels-datacrew-public` Docker container
- **Working directory:** `/workspace`
- **Skills directory:** `/workspace/.agents/skills/`
- **Memory directory:** `/workspace/dc_public_memories/`

## DataCrew MCP Server

- **URL:** `https://mdrag.datacrew.space/mcp/`
- **Auth:** Requires `CF-Access-Client-Id` and `CF-Access-Client-Secret` headers (Cloudflare Access). Credentials stored in Infisical project `homeserver`, env `prod`, path `/infrastructure`
- **Tool tiers:** primary (10), secondary, internal — see `/workspace/libraries/mdrag/src/interfaces/mcp/tools/registry.py`
- **Primary tools (10):**
  - `search_web` — SearXNG-powered web search
  - `crawl_url` / `crawl_site` — single page or deep site crawl
  - `query_rag` — knowledge base Q&A with citations (requires org_id)
  - `save_url_to_knowledge` / `save_text_to_knowledge` — ingest into RAG
  - `query_wiki` / `compile_wiki` — wiki vault search & compile
  - `research_with_ai` — delegates to Letta Deep Thought agent
  - `search_graph` — Neo4j knowledge graph search
- **Secondary tools:** graph CRUD, browser sessions, research workflows, CivitAI, etc.
- **Use mdrag first** for Domo questions — it has verified Domo content indexed
- **Connection status:** Not yet connected — need CF Access credentials from Infisical

## Skills Available

- `mdrag-mcp` — connect to DataCrew MCP for search, crawl, and RAG
- `verified-analyst` — high-fidelity research using verified knowledge base chunks
- `research-and-archive` — research a topic and archive findings
- `create-gdoc` — create Google Docs (use sparingly — only when community content needs a doc)

## Message Archive (SQLite)

- **Database:** `/workspace/dc_public_memories/messages.db`
- **Schema:** `channels`, `messages`, `thread_replies`, `messages_fts` (FTS5 full-text search)
- **Channels tracked:** 13+ DUG channels (public-general, help-etl_sql_beastmodes, help-visualization, help-admin_and_governance, help-ddx_apps_and_automation, help-connectors, help-is_domo_broken, etc.)
- **Query pattern:**
  ```python
  import sqlite3
  conn = sqlite3.connect("/workspace/dc_public_memories/messages.db")
  cur = conn.execute("SELECT text, user_id, channel_id FROM messages_fts WHERE text MATCH 'beast mode' LIMIT 5")
  ```
- **Use for:** searching past conversations, finding who asked about a topic, checking if a question was already answered

## Key Notes

- This is a **public-facing agent** — everything I do should be appropriate for a community Slack channel
- I have access to the DataCrew knowledge base via mdrag, which includes Domo documentation, YouTube transcripts, and blog content
- I do NOT have access to Infisical secrets, private client data, or internal business tools
