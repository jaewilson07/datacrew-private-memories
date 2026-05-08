---
description: The Domo docs knowledge store — architecture, tables, and how to query it.
---
# Domo Docs Knowledge Store

## Location
- **DB:** `/workspace/dc_public_memories/domo_docs.db` (41.9 MB)
- **Query script:** `/workspace/dc_public_memories/query_domo_docs.py`
- **Source docs:** `/workspace/domo-docs-hub/` (1,919 MDX files)

## What's In It
- **1,919 Domo docs** parsed from the domo-documentation-hub GitHub repo
- **FTS5 full-text search** across all docs
- **TF-IDF cosine similarity** (5,000 terms, 1-3grams)
- **34,969 NER entities** (connectors, features, roles, orgs)
- **7,278 internal cross-links** between docs
- **Wiki pages** generated on demand from partial hits + corrections

## Source Doc URLs
Every doc has a URL: `https://domo-support.domo.com/s/article/{doc_id}?language=en_US`
- Numeric IDs: `https://domo-support.domo.com/s/article/360043438973?language=en_US`
- Slug IDs: `https://domo-support.domo.com/s/article/Connect-AI-Tools-to-Domo-Using-MCP?language=en_US`
- **ALWAYS include source doc URLs** when answering questions from the knowledge store

## How to Query
```bash
# Hybrid search (FTS + TF-IDF, recommended)
python3 /workspace/dc_public_memories/query_domo_docs.py "beast mode case statement"

# FTS only (fast, exact keyword match)
python3 /workspace/dc_public_memories/query_domo_docs.py "SSO SAML" --mode fts

# Entity search
python3 /workspace/dc_public_memories/query_domo_docs.py "snowflake" --mode entities

# Log a query with answer quality (drives wiki generation)
python3 /workspace/dc_public_memories/query_domo_docs.py "how does sharing work" --log --quality partial

# Log with community correction
python3 /workspace/dc_public_memories/query_domo_docs.py "how does sharing work" --log --quality partial --correction "need Admin role"

# See wiki generation priorities
python3 /workspace/dc_public_memories/query_domo_docs.py --priorities
```

## Answer Quality Scale
- **confident** — Single doc nailed it, no wiki needed
- **partial** — Had to synthesize across 2+ docs → wiki page auto-generated
- **miss** — Couldn't find a good answer → flagged for external source ingestion

## Wiki Generation Logic
Wiki pages are generated when answer quality is "partial" or "miss", or when a community correction is provided. The wiki page stub is auto-created with source docs listed. The agent fills in the actual answer content. Corrections are appended over time.

## Doc Categories (by DUG question priority)
1. connector (61 question mentions)
2. visualization (60)
3. dataset (35)
4. dataflow (27)
5. beast-mode (23)
6. governance (21)
7. api (14)
8. app (12)
