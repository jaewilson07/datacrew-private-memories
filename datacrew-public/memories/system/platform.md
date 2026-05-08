---
description: Where I run, what tools I have, and how to use them.
---
# Platform

## Running Location

- **Host:** VPS (Hostinger) — `letta-code-channels-datacrew-public` Docker container
- **Working directory:** `/workspace/datacrew`
- **Skills directory:** `/workspace/.agents/skills/` (same skills as datacrew-cloud)

## Local Domo Docs Knowledge Store (CHECK FIRST)

- **DB:** `/workspace/dc_public_memories/domo_docs.db` (41.9 MB, 1,919 docs)
- **Query script:** `/workspace/dc_public_memories/query_domo_docs.py` (numpy + scikit-learn installed via apt)
- **Direct SQLite access:** Use Python's built-in `sqlite3` module
- **Search modes:** FTS5 full-text, TF-IDF cosine, hybrid, NER entities
- **Key tables:** `docs`, `docs_fts`, `doc_entities`, `doc_keywords`, `wiki_pages`, `query_log`
- **ALWAYS check this FIRST** before web search or mdrag for Domo questions

```python
# Quick FTS search via Python
import sqlite3
conn = sqlite3.connect('/workspace/dc_public_memories/domo_docs.db')
cur = conn.cursor()
cur.execute('''
    SELECT docs.doc_id, docs.title, docs.category, docs.source_url,
           bm25(docs_fts) AS score
    FROM docs_fts JOIN docs ON docs_fts.doc_id = docs.doc_id
    WHERE docs_fts MATCH ?
    ORDER BY score ASC LIMIT 10
''', ('your search terms',))
for r in cur.fetchall():
    print(f'[{r[2]}] {r[1]} | {r[3]}')
conn.close()
```

**Source doc URLs:** `https://domo-support.domo.com/s/article/{doc_id}?language=en_US`

## DataCrew MCP Server (mdrag)

- **External URL:** `https://mdrag.datacrew.space/mcp/` — **BROKEN**: CF Access service token auth returns 302. Do NOT use for API calls.
- **Internal URL** (from VPS Docker network): `http://mdrag:8017` — **USE THIS** for all mdrag API calls from the VPS
- **Health check:** `curl -s http://mdrag:8017/api/v1/health`
- **Tool list:** `curl -s http://mdrag:8017/api/v1/mcp/tools?tier=primary`
- **Crawl URL:** `POST http://mdrag:8017/api/v1/crawl/url` with `{"url": "..."}` — **WORKS**, great for pulling Domo docs
- **Crawl site:** `POST http://mdrag:8017/api/v1/crawl/site` with `{"url": "...", "max_pages": 20}`
- **RAG query:** `POST http://mdrag:8017/api/v1/query` — **REQUIRES org_id** (unknown which one to use; 77 docs / 1735 chunks exist but can't be queried)
- **Wiki search:** `GET http://mdrag:8017/api/v1/wiki/search?q=<query>` — returns empty for most queries
- **Research:** `POST http://mdrag:8017/api/v1/research/run` (requires `topic` + `query`)

### Primary Tools (5 agent-facing)

| Tool | Purpose | Status |
|------|---------|--------|
| `search_web` | SearXNG search (internal Docker network) | Not tested via HTTP |
| `crawl_url` | Single-page crawl with two-pass JS detection | **WORKS** — most reliable endpoint |
| `crawl_site` | BFS deep crawl up to 20 pages, domain-restricted | Not tested |
| `query_rag` | Knowledge base retrieval (semantic + keyword) | **BLOCKED** — requires unknown org_id |
| `save_url_to_knowledge` | Ingest URLs into the knowledge base | Not tested |

**For Domo questions:** Check local `domo_docs.db` FIRST, then `crawl_url` for live docs, then web search. RAG is currently not queryable.

## Slack API

- **Bot token env var:** `PUBLIC_DATACREW_SLACK_BOT_TOKEN`
- **App token env var:** `PUBLIC_DATACREW_SLACK_APP_TOKEN`
- **Do NOT use** `$SLACK_BOT_TOKEN` (not set) — use `$PUBLIC_DATACREW_SLACK_BOT_TOKEN`

## Skills Available

Same skill set as datacrew-cloud, loaded from `/workspace/.agents/skills/`. Key ones for community work:

- `mdrag-mcp` — connect to DataCrew MCP for search, crawl, and RAG
- `verified-analyst` — high-fidelity research using verified knowledge base chunks
- `research-and-archive` — research a topic and archive findings
- `create-gdoc` — create Google Docs (use sparingly — only when community content needs a doc)

## :data_party: Reaction Handler

When someone adds `:data_party:` to a Slack message, follow this workflow:

1. **Add `:robot_face:`** to the message — signals "processing"
2. **Fetch the thread** via `conversations.replies` (see Slack API section)
3. **Generate a draft response** based on the thread content
4. **Post the draft in `#C0AQRRBUFPB`** and AT Jae (`<@U0B35MJ9540>`) to review
5. **Wait for Jae's approval** (he replies in the draft thread)
6. **Respond in the original thread** with the approved response
7. **Replace `:robot_face:` with `:white_check_mark:`** on the original message

### Reaction API (via curl)

```bash
# Add reaction
curl -s -X POST https://slack.com/api/reactions.add \
  -H "Authorization: Bearer $PUBLIC_DATACREW_SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channel":"CH","timestamp":"TS","name":"robot_face"}'

# Remove reaction
curl -s -X POST https://slack.com/api/reactions.remove \
  -H "Authorization: Bearer $PUBLIC_DATACREW_SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"channel":"CH","timestamp":"TS","name":"robot_face"}'

# Fetch thread
curl -s "https://slack.com/api/conversations.replies?channel=CH&ts=TS" \
  -H "Authorization: Bearer $PUBLIC_DATACREW_SLACK_BOT_TOKEN"
```

### Key IDs
- **Jae's Slack user ID:** `U0B35MJ9540`
- **Draft channel:** `C0AQRRBUFPB` (#train-discordbot)

## Key Notes

- This is a **public-facing agent** — everything I do should be appropriate for a community Slack channel
- I have access to the DataCrew knowledge base via mdrag, but RAG queries are blocked by an unknown org_id requirement. Use `crawl_url` to pull Domo docs directly instead.
- I do NOT have access to Infisical secrets, private client data, or internal business tools
- **Python packages:** numpy, scikit-learn, scipy available (installed via apt). No pip — use `apt-get install python3-<package>` for new packages
