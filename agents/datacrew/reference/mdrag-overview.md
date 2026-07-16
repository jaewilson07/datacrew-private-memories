---
description: mdrag project overview — knowledge base, RAG, wiki, and API services. Read when working with mdrag subsystems.
---

# mdrag Overview

DataCrew's knowledge base and RAG system. Ingests content (YouTube, web, documents), generates embeddings for vector search, and provides wiki generation and chat capabilities.

## Key Subsystems

- **Readings service**: `/api/v1/readings/save` — ingests URLs, extracts content, generates summaries
- **RAG**: Vector store ingestion using embeddings — working as of 2026-06-30 (gateway serves `qwen3-embedding-8b`, 4096-dim)
- **Wiki**: `/api/v1/wiki/` — structure generation, page generation, chat, search, lint, compile
- **MCP tools**: `/mcp/` — calendar, civitai, hallucination, rag, research, second_brain, web, wiki

## Entry Points

- API main: `src/interfaces/api/main.py`
- Readings service: `src/interfaces/api/services/readings.py`
- Wiki service: `src/interfaces/api/services/wiki.py`
- Wiki router: `src/interfaces/api/routers/wiki/router.py`

## Karpathy Second Brain Gap Analysis (2026-06-21)

mdrag already has ~60% of the Karpathy LLM-wiki pattern:
- `CompileWorkflow` (raw → wiki compilation) ✅
- `LintWorkflow` (health checks: stubs, broken backlinks, inconsistencies) ✅
- `ConceptExtractor` (named entity extraction) ✅
- `GapDetector` (missing coverage) ✅
- `WikiVault` (raw/ + wiki/ dirs, master index, git commit) ✅
- `[[backlinks]]` cross-referencing ✅
- Second brain document annotations ✅

**5 gaps to close (priority order):**
1. Anti-evaporation loop — chat answers must file back as wiki pages
2. Incremental compilation — update only affected pages, not full recompile
3. Source provenance — add `source_files: [list]` to article frontmatter
4. Index-first query navigation — load master index + relevant articles instead of vector search
5. Automated periodic health checks — cron `LintWorkflow` + `GapDetector`

## Links

- [[agents/datacrew/reference/mdrag-gotchas]] — Known footguns and edge cases
- Repo: `/home/jaewilson07/GitHub/mdrag/`
