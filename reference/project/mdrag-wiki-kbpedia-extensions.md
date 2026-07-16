---
description: KBpedia-inspired wiki extensions for mdrag — architecture and file locations
---
# mdrag Wiki KBpedia-Inspired Extensions

## What Was Built

Extended the mdrag wiki system with 5 new capabilities inspired by Mike Bergman's KBpedia knowledge graph and his "Cooking with Python and KBpedia" (CWPK) series.

## New Files

### Capabilities (`src/capabilities/wiki/`)
- **typology.py** — Hierarchical concept scaffolding (KBpedia's ~70 typologies)
  - `TypologyNode`, `Typology`, `TypologyResult` models
  - `TypologyWorkflow`: generate, assign_articles, detect_gaps, load
- **concepts.py** — Named entity/concept extraction (CWPK #64)
  - `ExtractedConcept` model
  - `ConceptExtractor`: extract, persist, load_concepts
- **gaps.py** — Knowledge gap detection (CWPK #26 reasoning)
  - `GapReport` model
  - `GapDetector`: detect (empty nodes, orphaned concepts, LLM suggestions)
- **bridge.py** — Cross-source bridging wiki ↔ RAG ↔ graph (CWPK #49-50)
  - `BridgeSource` model
  - `WikiBridge`: link_rag_chunks, persist_sources, load_sources, enrich_article
- **roundtrip.py** — Extract/modify/recompile wiki structure (CWPK #27)
  - `RoundtripResult` model
  - `RoundtripWorkflow`: extract_structure, apply_edits, recompile

### Vault Extensions (`src/capabilities/wiki/vault.py`)
- `typology_path(topic)` — path to `_typology.json`
- `save_typology(topic, data)` / `load_typology(topic)` — persist/load typology

### Lint Enhancement (`src/capabilities/wiki/lint.py`)
- `LintReport.gap_report` — optional GapReport field
- `LintWorkflow.run(topic, include_gaps=True)` — optional gap detection

### MCP Tools (`src/interfaces/mcp/tools/wiki/handlers.py`)
- `typology_wiki` — generate/load/assign typology
- `extract_concepts` — extract named entities from articles
- `roundtrip_wiki` — extract/apply/recompile structure
- `bridge_wiki` — link articles to RAG chunks
- `detect_gaps` — find knowledge gaps

### Tool Registry (`src/interfaces/mcp/tools/registry.py`)
- 5 new secondary-tier tools: typology_wiki, extract_concepts, roundtrip_wiki, bridge_wiki, detect_gaps

### Tests (`tests/`)
- `test_wiki_typology.py` — 11 tests
- `test_wiki_gaps.py` — 5 tests
- `test_wiki_concepts.py` — 6 tests
- `test_wiki_bridge.py` — 6 tests
- `test_wiki_roundtrip.py` — 7 tests
- Total: 35 new tests + 20 existing = 55 all passing

### Runbooks (`.agents/runbooks/wiki/`)
- compile-wiki, lint-wiki, search-wiki, render-wiki (filled in)
- typology-wiki, concepts-wiki, roundtrip-wiki, bridge-wiki, gaps-wiki (new)

## Vault Layout Extensions

```
wiki/<topic>/
  _typology.json          ← typology tree
  _concepts/
    <article-slug>.json   ← extracted concepts per article
  _sources/
    <article-slug>.json   ← RAG chunk references per article
  <article-slug>.md       ← compiled articles (unchanged)
```

## Key Design Decisions

1. Typology is optional — wiki works without it, gap detection degrades gracefully
2. Concept extraction is per-article — no cross-article entity resolution yet
3. Bridge uses MongoDB text search — requires text index on chunks collection
4. Roundtrip recompile falls back to single-article re-drafting when compile doesn't produce the target slug
5. All new MCP tools are secondary tier — not in the default agent surface
6. **All LLM operations use `letta -p` via LettaWikiClient** — no direct OpenAI dependency for wiki workflows
7. Dedicated "knowledgebase-management" conversation tracks all wiki LLM operations for auditability

## Architecture: LettaWikiClient

- `LettaWikiClient` in `src/integrations/letta/wiki_client.py`
- Uses `letta -p` (headless CLI) for all LLM calls
- `prompt()` returns plain text, `prompt_json()` returns parsed JSON
- `parse_json()` handles markdown fences + embedded JSON extraction
- Default agent: `agent-61955fc7-fd63-43c3-b955-6bd02bea6693` (wiki-operations agent — NOT the community bot agent, which has a conversational persona that overrides structured JSON prompts)
- Timeout: 180s default (some prompts can take 45-90s)

## Pipeline Test Results (Matt Berman RAG video)

- compile_wiki: 5 articles from 1 raw page
- typology_wiki: 4-node category tree
- extract_concepts: 18 named entities
- detect_gaps: 12 orphaned concepts found
- roundtrip_wiki: full structure extraction with cross-references
- bridge_wiki: requires MongoDB (not tested)
- **Missing piece**: wiki articles NOT ingested back into RAG — need compile → MongoDB ingestion loop
