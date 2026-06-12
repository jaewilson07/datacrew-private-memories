---
description: Where I run, what tools I have, and how to use them.
---
# Platform

## Running Location

- **Host:** VPS (Hostinger) — `letta-code-channels-datacrew-public` Docker container
- **Working directory:** `/workspace/datacrew`
- **Skills directory:** `/workspace/.agents/skills/` (same skills as datacrew-cloud)

## Scheduled Tasks (Cron)

- `daily-message-backup` — 08:00 UTC daily — Pull new messages from tracked Slack channels → SQLite
- `doc-sync` — 06:00 UTC daily — Sync Domo docs from GitHub → knowledge store
- `memory-reflection` — Every 6 hours — Review conversations, detect gaps, lint memory, update files

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

- **External URL:** `https://wikki.datacrew.space/mcp` — unified gateway (2026-05-27)
- **Auth:** `Authorization: Bearer dc_<token>` — dc_ JWT from `datacrew.space/account`
- **Internal URL** (from VPS Docker network): `http://mdrag:8017` — use `X-Internal-Secret` header for auth bypass
- **MCP server ID:** `mcp_server-86434654-eeb4-4e87-8993-bbe8e0db0e3b`
- **Health check:** `curl -s http://mdrag:8017/api/v1/health`
- **41 tools discovered**, 10 primary attached to agent
- **Retired:** `mdrag.datacrew.space` (301 → wikki.datacrew.space), CF Access tokens removed

### 10 Primary Tools (attached to agent)

| Tool | Purpose | Status |
|------|---------|--------|
| `search_web` | SearXNG web search | ✅ attached |
| `crawl_url` | Single-page crawl with two-pass JS detection | ✅ attached |
| `crawl_site` | BFS deep crawl up to 20 pages | ✅ attached |
| `query_rag` | Knowledge base retrieval (semantic + keyword) | ✅ attached |
| `save_url_to_knowledge` | Ingest URLs into knowledge base | ✅ attached |
| `save_text_to_knowledge` | Save raw text to knowledge base | ✅ attached |
| `query_wiki` | Search the Karpathy wiki | ✅ attached |
| `compile_wiki` | Compile raw pages into wiki articles | ✅ attached |
| `research_with_ai` | Delegate research to Deep Thought agent | ✅ attached |
| `search_graph` | Search the knowledge graph | ✅ attached |

**If auth fails (401/403):** generate a new `dc_` token at `https://datacrew.space/account`, update wherever it's stored, and re-register the MCP server with the new Bearer header. (CF Access is retired — `mdrag.datacrew.space` 301-redirects to `wikki.datacrew.space`.)
**For Domo questions:** Check local `domo_docs.db` FIRST, then `query_rag` / `crawl_url`, then web search.

## Slack API

- **Bot token env var:** `PUBLIC_DATACREW_SLACK_BOT_TOKEN`
- **App token env var:** `PUBLIC_DATACREW_SLACK_APP_TOKEN`
- **Do NOT use** `$SLACK_BOT_TOKEN` (not set) — use `$PUBLIC_DATACREW_SLACK_BOT_TOKEN`

## Sending a Voice Message / Voice Memo

I CAN reply with audio. Slack has no native voice-memo API, but I can synthesise
speech and upload it as an mp3 that Slack renders as an **inline audio player** —
functionally a voice message. One command (the `send-voice-to-slack` runbook):

```bash
python3 /workspace/datacrew/.agents/runbooks/send-voice-to-slack/scripts/main.py \
  --text "<what to say>" \
  --channel "<channel id>" \
  --thread-ts "<ts of the message I'm replying to>"
```

- Use for: "send a voice message", "reply with audio", "send a voice memo",
  "say that out loud", "voice reply".
- Defaults to the **DataCrew voice** (Fish Speech S2, `--voice alix`) and the
  community token `PUBLIC_DATACREW_SLACK_BOT_TOKEN` — both correct for the
  public DUG workspace, so I don't pass `--bot-token-env`.
- Always pass `--thread-ts` when replying in a thread.
- If TTS is unreachable, the script errors clearly — I surface that and reply
  with text meanwhile; I NEVER substitute a different voice.
- Full guide + flags: `/workspace/datacrew/.agents/runbooks/send-voice-to-slack/SKILL.md`

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

## Git Auth

- **crew-dcs** remote (`hector-dcs/crew-dcs`) is a private repo — requires `HECTOR_GH_PAT` from Infisical (hostinger VPS project, env prod, path `/datacrew`). Set in remote URL as `https://$PAT@github.com/hector-dcs/crew-dcs.git`
- All other repos use public access or embedded tokens in their remote URLs

## Infisical Access

- **URL**: `https://infisical.datacrew.space`
- **Project ID**: `de8b26a4-8d69-46fa-bb32-9715ab396d6f`
- **Org ID**: `e899ebbe-5c41-4d53-b1ce-28cd18db1987`
- **Auth**: Universal auth (client ID/secret in `/workspace/.env`)
- **Key secrets**: `DOMO-COMMUNITY_ACCESS_TOKEN`, `POSTMAN_API_KE`, `MDRAG_AGENT_CF_CLIENT_ID/SECRET`, `AUTH_SECRET`, `GDOC_CLIENT`
- **Login command**: `infisical login --method universal-auth --client-id $ID --client-secret $SECRET --domain https://infisical.datacrew.space --silent`
- **Fetch secret**: Use API directly with Bearer token (CLI login doesn't persist between commands)

## Domo Community Instance

- **Instance**: `domo-community.domo.com`
- **Token**: `DOMO-COMMUNITY_ACCESS_TOKEN` from Infisical
- **Auth class**: `DomoTokenAuth(domo_instance='domo-community', domo_access_token=...)`
- **User**: Jae Wilson (Admin, id: 1893952720)

## crew-dcs Development

- **Python**: Requires `>=3.13` (installed via uv at `.venv/`, use `export PATH="/root/.local/bin:$PATH"`)
- **crew-logger (`cl`)**: GitHub repo `hector-dcs/crew-logger` is 404. Mocked at `/tmp/cl_mock/`
- **Venv**: `.venv/bin/python` with `export PATH="/root/.local/bin:$PATH"`
- **Route verification**: 290/336 endpoints verified against domo-community (86%)
- **Pipeline output**: `.agents/runbooks/convert-bryce-apis/scripts/output/`

## crew-dcs Optimization Modules (2026-05-10)

- **`DomoDataflow/layout_optimizer.py`** — topological layout, color standardization, auto-sectioning
- **`DomoAppStudio/styling_optimizer.py`** — 4 presets (MINIMAL_LIGHT, MINIMAL_DARK, EXECUTIVE, DENSE), `optimize_app()`, `apply_style()`
- **`DomoDataset/ai_readiness_lineage.py`** — lineage auto-fill for AI Readiness context, `populate_from_lineage()`
- **Key APIs:** Lineage `GET /api/data/v1/lineage/{entity_type}/{entity_id}`, AI Readiness `GET/POST/PUT /api/ai/readiness/v1/data-dictionary/dataset/{dataset_id}`, Page Layout `GET/PUT /api/content/v4/pages/layouts/{layout_id}`
- **Domo has NO auto-arrange API** for dataflow canvas — layout must be computed client-side

## Key Notes

- This is a **public-facing agent** — everything I do should be appropriate for a community Slack channel
- I have access to the DataCrew knowledge base via mdrag (10 primary MCP tools attached, CF Access token rotated 2026-05-08)
- I have access to Infisical secrets via machine identity (client ID/secret in `/workspace/.env`)
- **Python packages:** numpy, scikit-learn, scipy available (installed via apt). No pip — use `apt-get install python3-<package>` for new packages

## Domo Python Libraries — Know the Difference

- **PyDomo** (`pip3 install pydomo`) — Domo's official Python SDK. Sync, dict-based, limited API coverage (datasets, PDP, users, groups, pages, streams, accounts). OAuth client-credentials auth.
- **crew-dcs / domoLibrary** — DataCrew's async Python library. Class-based (`DomoDataset`, `DomoCard`, `DomoPage`, `DomoDataflow`, `DomoGroup`), token auth (`DomoTokenAuth`), broader API coverage including dataflows and cards. The original name was "crew-dcs"; it was later renamed to "domoLibrary."
- **domo_python** (`pip install domo_python`) — Community package by Brock Cooper. Simple sync wrapper focused on data import/export + SFTP. Last updated 2018.
- **When someone asks about "domoLibrary" they mean crew-dcs/domoLibrary, NOT PyDomo**
