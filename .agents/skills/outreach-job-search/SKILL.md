---
name: outreach-job-search
description: >
  Run the DataCrew job search scoring pipeline: scrape recent jobs, filter via L1
  keyword scoring and L2 Ollama LLM scoring, then post the top results as a formatted
  digest to Slack. Use for: "/outreach/job-search", "run job search", "score jobs",
  "job digest", "find jobs".
metadata:
  version: 1.0.0
  updated: 2026-05-29
---

# outreach-job-search

Run the job search scoring pipeline and post a digest of top results to Slack.

## When to Use

- User says `/outreach/job-search`
- User asks to run job scoring, find jobs, or post a job digest
- User wants to see what new Domo/data platform jobs are available

## Steps

### Step 1: Verify environment

Confirm required env vars are set in the **current shell** (not in .env files — the pipeline reads from the environment directly):

```bash
# Check Slack token — accepts either name
echo "${DATACREW_SLACK_BOT_TOKEN:-${JOB_SEARCH_SLACK_BOT_TOKEN:-MISSING}}" | cut -c1-12

# Confirm Ollama is reachable (default endpoint is hardcoded in the script)
curl -s --connect-timeout 5 http://ollama.jaewilson07.twingate.com:11434/api/tags | python3 -c "import json,sys; tags=json.load(sys.stdin); print([m['name'] for m in tags.get('models',[])])" 2>&1 | head -1
```

If Ollama is unreachable, stop — L2 scoring requires the local GPU endpoint via Twingate.

### Step 2: Scrape fresh jobs (run once per day or if DB is stale)

`run_scoring.py` reads from the local DB (`data/EXPORTS/job_search.db`). It only needs to be
populated once per day. Skip this step if you can confirm the DB was scraped today.

```bash
cd /workspace/datacrew/projects/job-search

# Check when the DB was last populated
.venv/bin/python3 -c "
import sqlite3; conn=sqlite3.connect('data/EXPORTS/job_search.db')
cur=conn.cursor(); cur.execute('SELECT COUNT(*), MAX(fetched_at) FROM jobs')
count, latest = cur.fetchone(); print(f'Jobs: {count}, latest: {latest}')
"

# If more than 24 hours old, scrape fresh data (takes ~8 min)
JOB_SEARCH_SLACK_BOT_TOKEN=$DATACREW_SLACK_BOT_TOKEN \
PYTHONPATH=src:/workspace/datacrew \
.venv/bin/python3 -m job_search 2>&1 | tail -5
```

The scrape step may fail at the Google Sheets sync at the end (if GDOC credentials aren't set) —
that's OK, all job data is saved to the DB before that step.

### Step 3: Run the scoring pipeline

```bash
cd /workspace/datacrew/projects/job-search

DATACREW_SLACK_BOT_TOKEN=$DATACREW_SLACK_BOT_TOKEN \
JOB_SEARCH_SLACK_CHANNEL_ID=C0B23VA3CJY \
PYTHONPATH=src:/workspace/datacrew \
.venv/bin/python3 run_scoring.py
```

**What `run_scoring.py` does (reads DB, does NOT scrape):**
1. **L1 (KeywordScorer)** — Fast regex filter: seniority + hard_blocks cut noise
2. **L2 (LettaScorer w/ Ollama backend)** — Local LLM scoring via `qwen3.5:9b`
3. **L3 (LettaScorer via Letta Cloud)** — Apply-worthy ranking (skipped if no agent ID)
4. **Post** — Format results into tiered Slack digest (high/mid tier threads)

### Step 4: Verify Slack post

After the pipeline completes, confirm the digest was posted to `#datacrew-customer-outreach` (C0B23VA3CJY).

## CLI Commands

```bash
# Full pipeline (score + post)
cd /workspace/datacrew/projects/job-search
JOB_SEARCH_SLACK_BOT_TOKEN=$DATACREW_SLACK_BOT_TOKEN \
JOB_SEARCH_SLACK_CHANNEL_ID=C0B23VA3CJY \
PYTHONPATH=src:/workspace/datacrew \
.venv/bin/python3 run_scoring.py --yolo

# Score only (no Slack post) — not yet supported; comment out the Slack posting block manually if needed
# DATACREW_SLACK_BOT_TOKEN=$DATACREW_SLACK_BOT_TOKEN \
# JOB_SEARCH_SLACK_CHANNEL_ID=C0B23VA3CJY \
# PYTHONPATH=src:/workspace/datacrew \
# .venv/bin/python3 run_scoring.py
```

## Pipeline Architecture

| Layer | Scorer | Method | Speed |
|-------|--------|--------|-------|
| L1 | KeywordScorer | Regex: seniority + hard_blocks | Fast |
| L2 | LettaScorer (Ollama backend) | Local LLM (`qwen3.5:9b`, set in `datacrew/config.yaml`) | ~30s/job |
| L3 | LettaScorer | Letta API (fallback, credits exhausted) | N/A |

**Profile:** `profiles/jae-consultant-fte.yaml`
- `must_have_any: ["domo"]`
- `seniority: [senior, principal, staff, director, lead, manager, architect, consultant, engineer, analyst, developer]`
- `comp_min: $130k FTE`

**Database:** `data/EXPORTS/job_search.db` — persisted jobs, deduped by URL

## Environment Variables

| Variable | Source | Purpose |
|----------|--------|---------|
| `DATACREW_SLACK_BOT_TOKEN` | `datacrew/.env` | Slack bot token (xoxb-) |
| `OLLAMA_BASE_URL` | `datacrew/.env` or default | Ollama endpoint for L2 scoring |
| `JOB_SEARCH_SLACK_BOT_TOKEN` | Set from `DATACREW_SLACK_BOT_TOKEN` | Pipeline Slack auth |
| `JOB_SEARCH_SLACK_CHANNEL_ID` | Hardcoded `C0B23VA3CJY` | Target Slack channel |

## Key IDs

| Resource | ID |
|----------|-----|
| Slack Channel | `C0B23VA3CJY` (#datacrew-customer-outreach) |
| Job DB | `data/EXPORTS/job_search.db` |
| Profile | `profiles/jae-consultant-fte.yaml` |

## Gotchas

- **Use `--yolo` for autonomous runs** — the pipeline is designed for hands-off execution
- **Use `SlackJobPoster` for ALL Slack formatting** — never create duplicate Block Kit formatting (gotcha #72)
- **Post to `C0B23VA3CJY`** — NOT `C0AR7M4M0V9` (old channel)
- **Empty `seniority: []` in profile causes noise** — always validate the profile has meaningful filters (gotcha #73)
- **L3 LettaScorer credits exhausted** — don't enable unless credits are refreshed
- **Ollama must be reachable before running** — Step 1 checks this; if curl fails, stop (VPS can't reach it — L2 requires the local GPU via Twingate)
- **sentence-transformers removed** — no more OOM/disk-full failures from torch
- **Use `.venv/bin/python3` directly** — NOT `uv run` (30+ sec resolver overhead)

## Related

- `datacrew/projects/job-search/` — pipeline source code
- `skills/outreach-create-dossier/SKILL.md` — dossier creation for top-tier companies
- `skills/mdrag-mcp/SKILL.md` — mdrag MCP for web research
