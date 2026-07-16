---
description: mdrag footguns, chronic failures, and things to watch out for. Read before working with mdrag API or MCP tools.
---

# mdrag Gotchas

## ColoredLogger Format Args (FIXED)

ColoredLogger from crew-logger (`cl` package) does NOT support `%s`/`%d`/`%r` format args. Only accepts a single string message.

- **Wrong**: `logger.info("Detected URL: %s", url)` → crashes with `TypeError`
- **Right**: `logger.info(f"Detected URL: {url}")`
- **Fixed in**: PR #357 + PR #358 (49 files, 216 calls)
- **If new logger calls are added**: ALWAYS use f-strings, never format args

## Embedding Endpoint (RESOLVED 2026-06-30)

- **Status: WORKING** — Gateway serves `qwen3-embedding-8b` (4096-dim)
- Gateway endpoint: `http://localhost:7630/v1/embeddings` with model `qwen3-embedding-8b`

## Docker Container Updates

After code changes, copy updated source into containers and restart:
```bash
docker cp /home/jaewilson07/GitHub/mdrag/src mdrag-local:/app/src
docker restart mdrag-local mdrag-rq-local
```
Health check: `curl -s -o /dev/null -w "%{http_code}" http://localhost:8017/api/v1/health`

## save_text_to_knowledge Missing org_id (FIXED — 2026-07-13)

`save_text_to_knowledge` MCP tool didn't store `org_id`. Search tools filter by `org_id` (fail-closed), so content was unfindable.
- **Fixed in**: PR #507 + PR #585

## MCP save_text_to_knowledge / save_url_to_knowledge 401 Error (2026-07-13)

MCP tools return 401 "Bearer token required" from internal RAG API. MCP session init works, `crawl_url` works, but save tools fail.
- **Workaround**: Save research as local files in project `.agents/research/` folders

## REST API Behind CF Access (2026-07-01)

REST API at `mdrag.datacrew.space/api/v1/*` 301-redirects to `wiki.datacrew.space/api/v1/*` which is behind Cloudflare Access. Blocks all programmatic API access except `/api/v1/health`.
- **Workaround**: Use MCP endpoint at `wiki.datacrew.space/mcp/` with `X-DC-Token` header

## MCP Access from Letta Agent Environment

1. **Get session ID**: POST to `https://wiki.datacrew.space/mcp/` with `X-DC-Token: $DATACREW_API_TOKEN` header. First request returns 400 with `mcp-session-id` in response headers.
2. **Initialize**: POST `initialize` JSON-RPC with `Mcp-Session-Id` + `X-DC-Token` headers
3. **Call tools**: POST `tools/call` with same headers
4. **Key tools**: `save_url_to_knowledge`, `save_text_to_knowledge`, `query_rag`, `search_web`, `crawl_url`, `crawl_site`, `unified_search_knowledge_base`
5. **Collection**: `"datacrew"` (collection_id: `6a274087d4b0a3ad1b028ae8`, org_id: `datacrew`)

## Google Sheet/Docs auth — FIXED (2026-07-14)

- `GDOC_TOKEN` in homeserver `.env` has valid OAuth token with refresh_token
- Scopes: spreadsheets, documents, drive.file, userinfo.email, openid, userinfo.profile
- Limitation: `drive.file` scope only allows access to files created/opened by this OAuth client
- Refresh: POST to `https://oauth2.googleapis.com/token` with client_id, client_secret, refresh_token, grant_type=refresh_token

## Whisper STT on Cubby — Garbled Output (2026-07-13)

Whisper model on cubby can produce garbled, repetitive output. Cannot reliably transcribe Jae's audio clips.
- **Workaround**: Ask Jae to type key points when transcription is garbled
