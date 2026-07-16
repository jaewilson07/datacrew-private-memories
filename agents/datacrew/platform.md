---
description: DataCrew agent platform config — where it runs, tools, paths, services. Read when working on infrastructure.
---

# DataCrew Platform

## Running Location

- **Host**: bonker — native Linux box (Ubuntu 26.04 LTS, kernel 7.0.0-22-generic, x86_64)
- **NOT WSL2, NOT Docker container, NOT Hostinger VPS** — those are retired
- **Working directory**: `/home/jaewilson07/GitHub/`

## Key Services on bonker

| Service | Container | Port | Purpose |
|---------|-----------|------|---------|
| mdrag API | mdrag-local | 8017 | Knowledge base, RAG, wiki |
| mdrag RQ worker | mdrag-rq-local + mdrag-rq-graph | — | Background jobs |
| gateway | gateway | 7630 | Chat + embeddings (qwen3-embedding-8b, 4096-dim) |
| wikki | wiki | 3000 | Wiki frontend |
| neo4j | neo4j | — | Knowledge graph for mdrag |
| paperclip | paperclip | 3100 | Agent orchestration |
| letta-bridge | letta-bridge | 8089 | Paperclip-Letta bridge |
| AdventureWorks (Postgres) | adventureworks | 5433 | Sample database (postgres db, user: postgres, pw: AdventureWorks1!) |
| AdventureWorks (MSSQL) | — | 1433 | Data warehouse sample (FactFinance, DimAccount) |

## Remote GPU Box

- **cubby**: 192.168.1.153
- vLLM on port 8000 (qwen-vl-abliterated, qwen3.5-9b, qwen3-embedding-8b)
- Voice-gateway STT: `http://cubby.lan:8885/v1/audio/transcriptions`
- Voice-gateway TTS: `http://cubby.lan:8885/v1/audio/speech`

## Key Paths

| Path | Purpose |
|------|---------|
| `/home/jaewilson07/GitHub/homeserver/` | Homeserver repo (infra, Docker, configs) |
| `/home/jaewilson07/GitHub/mdrag/` | mdrag repo (RAG, knowledge base) |
| `/home/jaewilson07/GitHub/datacrew/` | DataCrew platform repo |
| `/home/jaewilson07/GitHub/homeserver/.env` | Environment file with secrets |
| `/home/jaewilson07/GitHub/homeserver/apps/gateway/src/config.vps.yaml` | Gateway config |

## Infisical

- Self-hosted at `infisical.datacrew.space`
- Homeserver project: `3fbb4296-d4e6-4c17-83ee-b852a57a5e50` (env: prod, path: `/datacrew`)
- crew-dcs project: `de8b26a4-8d69-46fa-bb32-9715ab396d6f` (env: prod, path: `/`)
- Machine identity auth: `INFISICAL_CLIENT_ID` + `INFISICAL_CLIENT_SECRET`

## Letta

- Cloud Letta: `https://letta.datacrew.space`
- Letta CLI: `~/.local/bin/letta` (v0.28.9)
- Agent ID: `agent-55e609e7-2a76-4400-a510-fa8b96c47aa3`
- Gateway provider: `gateway/qwen3.5-9b` via `https://mermaid-api.datacrew.space/v1`

## Slack

- Service: `letta-datacrew.service` (systemd user service)
- Config: `/home/jaewilson07/GitHub/homeserver/apps/letta-code-channels-datacrew-public/`
- Routing: `/home/jaewilson07/.letta/channels/slack/routing.yaml`
- Accounts: `/home/jaewilson07/.letta/channels/slack/accounts.json`
- Workspace: domo_user_group (T012H3JSC83)
- Jae's user ID: U08L4B485B4

## Letta Dream (AGENTS.md Maintenance)

- Cron: `dream-agents-md` (ID: `17585887`) — Fridays at 10am MDT
- Runs `letta dream --to` on mdrag and datacrew AGENTS.md files
