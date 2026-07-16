---
description: Shared infrastructure knowledge — where services run, what's available, network topology.
---

# Infrastructure

## Host Machine

- **bonker**: Native Linux box (Ubuntu 26.04 LTS, kernel 7.0.0-22-generic, x86_64)
- Running natively on the host (not Docker container, not WSL2)
- Docker installed for running services

## Key Services

| Service | Container | Port | Network | Purpose |
|---------|-----------|------|---------|---------|
| mdrag API | mdrag-local | 8017 | — | Knowledge base, RAG, wiki |
| mdrag RQ worker | mdrag-rq-local | — | — | Background jobs |
| gateway | gateway | 7630 | ai-network | Chat + embeddings proxy |
| wikki | wiki | 3000 | ai-network | Wiki frontend |
| neo4j | neo4j | — | — | Knowledge graph for mdrag |
| paperclip | paperclip | 3100 | ai-network | Agent orchestration |
| letta-bridge | letta-bridge | 8089 | ai-network | Paperclip-Letta bridge |
| AdventureWorks (Postgres) | adventureworks | 5433 | — | Sample database |
| AdventureWorks (MSSQL) | — | 1433 | — | Data warehouse sample |

## Remote GPU Box

- **cubby**: 192.168.1.153
- vLLM on port 8000 (chat + embeddings)
- Gateway on port 7630 routes to vLLM
- Voice-gateway STT: `http://cubby.lan:8885/v1/audio/transcriptions`
- Voice-gateway TTS: `http://cubby.lan:8885/v1/audio/speech`

## Docker Network

- ai-network: 172.19.0.0/16

## Key Paths

- Homeserver repo: `/home/jaewilson07/GitHub/homeserver/`
- mdrag repo: `/home/jaewilson07/GitHub/mdrag/`
- datacrew repo: `/home/jaewilson07/GitHub/datacrew/`
- Environment file: `/home/jaewilson07/GitHub/homeserver/.env`

## Infisical

- Self-hosted at `infisical.datacrew.space`
- Homeserver project: `3fbb4296-d4e6-4c17-83ee-b852a57a5e50` (env: prod, path: `/datacrew`)
- Machine identity auth: `INFISICAL_CLIENT_ID` + `INFISICAL_CLIENT_SECRET`
