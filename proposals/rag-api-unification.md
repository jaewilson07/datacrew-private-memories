# Proposal: Unify RAG Backend + Wikki Frontend APIs

**Author:** datacrew-cloud  
**Date:** 2026-05-26  
**Status:** Draft  

---

## Problem

The Wikki frontend (`wikki.datacrew.space`) and the mdrag RAG backend (`mdrag.datacrew.space`) have **overlapping but inconsistent API surfaces**. The frontend proxies a subset of backend endpoints through Next.js API routes, creating a maintenance burden and feature gap:

| Issue | Detail |
|-------|--------|
| **Incomplete proxy coverage** | Wikki only proxies 11 routes. The backend exposes 40+ endpoints across 29 routers. Key missing: query, crawl, research, documents, collections, signals, sources, share, drift, browser. |
| **Path mismatch** | Wikki routes strip `/v1/` (e.g., `/api/wiki/structure` → `/api/v1/wiki/structure`). Inconsistent — some paths drop the version, others don't. Makes API discovery harder. |
| **No auth passthrough** | Wikki proxy routes add zero auth headers. The backend has `ApiKeyMiddleware` + `get_user_email` for collection access control. Wikki bypasses all of it. |
| **No MCP integration** | Agents use mdrag's MCP tools (`search_web`, `crawl_url`, `query_rag`, `save_url_to_knowledge`). Wikki has no MCP-aware proxy — agents can't use the Wikki UI surface. |
| **Duplicate wiki paths** | Backend has `/api/v1/wiki/search`, `/api/v1/wiki/compile`, `/api/v1/wiki/lint`. Wikki doesn't proxy any of these. The "wiki" in Wikki only covers structure + generate + chat + projects. |
| **org_id scoping gap** | Backend requires `org_id` for ingestion and queries. Wikki doesn't pass `org_id` — so ingested data from the UI goes to unscoped storage and becomes unqueryable. |

---

## Current State

### Backend (mdrag) — 40+ endpoints across 29 routers

| Prefix | Endpoints | Key operations |
|--------|-----------|----------------|
| `/api/v1/query` | 1 | Grounded RAG query with citations |
| `/api/v1/wiki` | 7 | Structure, generate, chat, projects, compile, search, lint |
| `/api/v1/ingest` | 7 | Web, YouTube, Circle, Drive, upload, Confluence, Jira |
| `/api/v1/jobs` | 3 | List, get status, delete |
| `/api/v1/crawl` | 2 | Single URL, deep site |
| `/api/v1/research` | 1 | Run research job |
| `/api/v1/chat` | 1 | Letta chat agent |
| `/api/v1/health` | 2 | Health, vector-db health |
| `/api/v1/documents` | 8 | CRUD, check-url, reindex, reingest, flag, collection move |
| `/api/v1/collections` | 4 | CRUD + access control |
| `/api/v1/readings` | 3 | Save, list, get |
| `/api/v1/signals` | — | Notes (replaces `/api/v1/notes`) |
| `/api/v1/mcp` | 1 | Tool discovery |
| + 16 more routers | — | Sources, share, drift, browser, analytics, admin, etc. |

### Wikki Frontend — 11 proxy routes

| Wikki Route | → Backend Endpoint | Gaps |
|-------------|-------------------|------|
| `GET /api/health` | `/api/v1/health/vector-db` | Only checks vector DB, not overall health |
| `POST /api/chat` | `/api/v1/chat/message` | No auth, no session management |
| `POST /api/ingest/web` | `/api/v1/ingest/web` | **No org_id** — data goes to unscoped storage |
| `GET /api/ingest/jobs/[id]` | `/api/v1/jobs/{id}` | OK |
| `GET /api/readings` | `/api/v1/readings` | OK |
| `GET /api/readings/[id]` | `/api/v1/readings/{id}` | OK |
| `POST /api/readings/save` | `/api/v1/readings/save` | OK |
| `POST /api/wiki/structure` | `/api/v1/wiki/structure` | OK |
| `POST /api/wiki/generate` | `/api/v1/wiki/generate` | OK (streaming) |
| `POST /api/wiki/chat` | `/api/v1/wiki/chat` | OK (streaming) |
| `GET /api/wiki/projects` | `/api/v1/wiki/projects` | OK |

---

## Proposal: Three-Phase Unification

### Phase 1: Fix the Critical Gaps (1-2 days)

**Goal:** Make existing Wikki features actually work end-to-end.

1. **Add `org_id` to all proxied requests**  
   - Default to `datacrew` (or resolve from auth context)  
   - Pass in `namespace.org_id` for ingest, `filters.org_id` for query  
   - Without this, data ingested from Wikki is unscoped and unqueryable

2. **Proxy the RAG query endpoint**  
   - Add `POST /api/query` → `POST /api/v1/query` (with `org_id` filter)  
   - This is the **most important missing proxy** — it's how agents and the UI get grounded answers

3. **Proxy wiki search**  
   - Add `GET /api/wiki/search` → `GET /api/v1/wiki/search`  
   - The wiki has a search feature that Wikki doesn't expose

4. **Fix health endpoint**  
   - Proxy `/api/v1/health` (overall health) instead of only `/api/v1/health/vector-db`

### Phase 2: Full API Passthrough (3-5 days)

**Goal:** Wikki becomes the single public API surface for mdrag. All backend endpoints accessible through Wikki's domain.

1. **Replace individual proxy routes with a catch-all proxy**  
   - Single Next.js catch-all route: `/api/v1/[...path]` → `${BACKEND_URL}/api/v1/[...path]`  
   - Preserves the `/api/v1/` prefix for consistency  
   - Eliminates the need to write a new proxy route for every backend endpoint  
   - Keep explicit routes only where transformation is needed (e.g., auth injection, org_id defaults)

2. **Add auth middleware to the proxy layer**  
   - Inject `CF-Access-Client-Id` / `CF-Access-Client-Secret` for backend calls that go through CF Access  
   - Or: since Wikki and mdrag are on the same Docker network, use `BACKEND_URL=http://rag-agent:8017` (internal) and skip CF Access entirely

3. **Add missing high-value proxies** (explicit routes with transforms):
   - `POST /api/v1/crawl/url` — single-page crawl
   - `POST /api/v1/crawl/site` — deep site crawl
   - `POST /api/v1/research` — research jobs
   - `GET /api/v1/documents` — document list
   - `GET /api/v1/collections` — collection list
   - `POST /api/v1/wiki/compile` — compile wiki articles
   - `POST /api/v1/wiki/lint` — wiki quality checks

4. **Deprecate the old `/api/` (no v1) routes**  
   - Add 301 redirects from `/api/wiki/*` → `/api/v1/wiki/*` etc.  
   - Remove the old individual proxy files once redirects are in place

### Phase 3: MCP Bridge + Agent Integration (5-7 days)

**Goal:** Agents can use Wikki as their API surface, and Wikki can trigger agent workflows.

1. **MCP proxy endpoint**  
   - `POST /api/v1/mcp/invoke` — invoke any MCP tool by name with JSON params  
   - Agents already use mdrag's MCP tools; this lets the Wikki UI do the same  
   - Returns the same 12k-char-limited responses

2. **Agent webhook integration**  
   - Wikki can configure webhooks that trigger agent actions on ingest completion  
   - e.g., "when a URL is ingested, notify the datacrew-cloud agent to update the wiki"

3. **WebSocket for real-time updates**  
   - Research jobs, ingestion jobs, and wiki compilation can push status updates to the Wikki UI  
   - Replaces the current polling pattern for job status

---

## Architecture After Unification

```
                    ┌─────────────────────────┐
                    │  wikki.datacrew.space    │
                    │  (Next.js + Caddy)       │
                    │                          │
                    │  /api/v1/* ──────────────┼── catch-all proxy
                    │  /api/v1/mcp/invoke ─────┼── MCP bridge
                    │  / (UI pages)            │
                    └──────────┬───────────────┘
                               │ Docker network
                               │ (no CF Access needed)
                    ┌──────────▼───────────────┐
                    │  mdrag backend           │
                    │  (FastAPI on :8017)      │
                    │                          │
                    │  /api/v1/query           │
                    │  /api/v1/wiki/*          │
                    │  /api/v1/ingest/*        │
                    │  /api/v1/crawl/*          │
                    │  /api/v1/research        │
                    │  /api/v1/documents/*     │
                    │  /api/v1/collections/*   │
                    │  /mcp/* (MCP protocol)   │
                    └──────────┬───────────────┘
                               │
                    ┌──────────▼───────────────┐
                    │  MongoDB + Neo4j         │
                    │  + SearXNG + Crawl4AI    │
                    └─────────────────────────┘
```

**Key change:** Wikki becomes the public API gateway. mdrag backend is only accessible internally (Docker network). CF Access service tokens are only needed for external agents hitting mdrag directly.

---

## Migration Path

| Step | Risk | Rollback |
|------|------|----------|
| Phase 1: Add org_id + query proxy | Low — additive | Remove the new routes |
| Phase 2: Catch-all proxy | Medium — could break existing UI calls | Revert to individual proxy routes (git revert) |
| Phase 3: MCP bridge | Low — new endpoint | Remove the route |

**No data migration needed.** This is purely an API routing change.

---

## Open Questions

1. **Should Wikki require user auth?** Currently it's open. If we add org_id scoping, we need to know *which* org the user belongs to. Options: (a) hardcode `datacrew` for now, (b) add CF Access auth on Wikki, (c) add a simple API key.

2. **Should the catch-all proxy use internal Docker networking?** If `BACKEND_URL=http://rag-agent:8017`, we skip CF Access entirely for Wikki→mdrag calls. This is faster and simpler but means Wikki and mdrag must be on the same Docker network.

3. **Should we deprecate direct mdrag access?** Once Wikki is the public gateway, should `mdrag.datacrew.space` become internal-only? Agents currently hit it directly with CF Access tokens. We could keep both paths alive.

---

## What This Unlocks

- **Wikki UI can query RAG** — the Ask page actually returns grounded answers
- **Wikki UI can crawl + ingest** — full research workflow from the browser
- **Wikki UI can manage documents + collections** — CRUD for the knowledge base
- **Agents get a public API surface** — MCP bridge lets any agent use Wikki as their entry point
- **One API to document** — instead of two overlapping surfaces
- **Auth is centralized** — Wikki handles auth, mdrag trusts the internal network
