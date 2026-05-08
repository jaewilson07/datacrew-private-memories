# datacrew-public-workspace

Workspace for the **datacrew-public** agent — the public-facing DataCrew bot in
the Domo User Group Slack community. This agent answers questions about Domo,
helps community members, and surfaces DataCrew content.

## What This Agent Is

- **Public-facing**: lives in the Domo User Group Slack, anyone can DM it
- **Community-oriented**: helps Domo users, answers questions, shares knowledge
- **Boundaried**: no access to private pipeline, rates, financials, or client data
- **Knowledge-driven**: uses the knowledge-base and libraries to provide accurate answers

## Workspace Structure

```
/workspace/
├── AGENTS.md              ← You are here
├── datacrew-public/       ← Agent knowledge base & scripts
│   ├── articles/          ← Article drafts (markdown)
│   ├── memories/         ← System memory, reference docs, user profiles
│   ├── query_domo_docs.py← Domo docs query utility
│   └── sync_domo_docs.py ← Domo docs sync utility
├── dc_public_memories/    ← Letta memory FS (git-synced, DO NOT commit)
├── domo-developer-portal/← Domo API docs (separate repo, DO NOT commit)
├── domo-docs-hub/         ← Domo KB docs (separate repo, DO NOT commit)
└── libraries/
    ├── cboti/             ← Google Workspace integration library
    ├── crew-dcs/          ← Domo Python SDK
    └── mdrag/             ← MCP server (search, crawl, RAG)
```

## Libraries

### cboti (`libraries/cboti/`)

Google Workspace integration library — Docs, Sheets, Drive, Contacts, Auth.
Used for writing content to Google Docs, reading spreadsheets, etc.

Key patterns:
- `Tabs.upsert(doc_id, title, content)` — write to Google Doc tabs (never `write_markdown_to_tab`, it appends)
- Markdown blockquotes (`> `) are stripped in Google Docs — use **bold-labeled paragraphs** instead
- Google Doc tab IDs are document-scoped — always `Tabs.list(doc_id)` for the target doc first

### mdrag (`libraries/mdrag/`)

DataCrew MCP server — web search, crawl, RAG, knowledge management.
Available at `https://mdrag.datacrew.space/mcp/` (36 tools).

Primary agent-facing tools:
- `search_web` — SearXNG search
- `crawl_url` — single page crawl
- `crawl_site` — BFS deep crawl up to 20 pages
- `query_rag` — knowledge base retrieval
- `save_url_to_knowledge` — ingest URLs into knowledge base

## Knowledge Base (`datacrew-public/`)

The agent's knowledge base lives in `datacrew-public/`:
- `articles/` — Article drafts in markdown (lightning talk format)
- `memories/reference/` — Curated reference content (Domo API patterns, DCS templates, etc.)
- `memories/users/` — DUG community member profiles
- `memories/system/` — System memory, persona, platform config, response rules
- `query_domo_docs.py` / `sync_domo_docs.py` — Utilities for querying and syncing Domo docs

## Hard Rules

1. **Never share private information** — no client names, rates, pipeline details, or financial data
2. **Never claim Domopalooza speaking** — MCPs vs Skills is a YouTube video + article, NOT a stage appearance
3. **Use mdrag for research** — don't fall back to generic web search when mdrag has the capability
4. **Check runbooks before implementing** — always look in `.agents/runbooks/` and `.agents/skills/` first
5. **Fail hard, fail loud** — never swallow exceptions or gracefully skip errors
6. **No `TYPE_CHECKING`** — refactor for separation of concerns instead
7. **No naked `except`** — always catch specific exceptions
8. **Use `uv`** — never `pip`
9. **Config in `config.yaml`** — `.env`/Infisical for secrets only
10. **Never use standard `logging`** — use `async ColoredLogger` from `utils.logging`

## Creating New Skills/Runbooks

Use the seeded skills to scaffold new ones:

```bash
# Create a new skill
mkdir -p .agents/skills/<name>/{references,assets,scripts,EXPORTS}
cp .agents/skills/create-skill/assets/SKILL.md.template .agents/skills/<name>/SKILL.md

# Create a new runbook
mkdir -p .agents/runbooks/<verb-noun>/{scripts,references,assets}
```

Verb-first naming for runbooks. Crosslink, don't copy.
