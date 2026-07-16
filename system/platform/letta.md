---
description: Letta platform knowledge — agent IDs, CLI, API, known issues. Shared across all agents.
---

# Letta Platform

## Agents

| Agent | ID | Role | Slack |
|-------|----|------|-------|
| DataCrew | `agent-55e609e7-2a76-4400-a510-fa8b96c47aa3` | Business operations, infrastructure | @U0AQ7N23LKT |
| IdrisBot (build-partner) | `agent-0604eb6c-85b1-46f9-9c13-fb147d85bf2a` | Consulting/build partner | @U0BHRTU63E1 |
| EmmaBot | `agent-5afcfa48-81d3-430f-87fe-0a814fecff7e` | Public Domo community bot | @U0B35MJ9540 |

## Letta Server

- Cloud Letta: `https://letta.datacrew.space`
- Letta CLI: `~/.local/bin/letta` (v0.28.9)
- Rate limits: 10,000 per 4-hour window, 25,000 per day
- Minimum $1 credit balance required

## Gateway Provider

- Provider name: `gateway` (registered on Letta Cloud API)
- Base URL: `https://mermaid-api.datacrew.space/v1`
- API key: `no-key-required`
- Models: `qwen3.5-9b`, `qwen-vl-abliterated`, `qwen3-embedding-8b`
- Usage: `letta -m gateway/qwen3.5-9b`
- Chat completions require cubby (GPU box) to be up

## Known Issues

- **`send_message` approval**: All agents need `send_message` approval disabled via `PATCH /v1/agents/{id}/tools/approval/send_message` with `{"requires_approval": false}`
- **Agent stuck on "requires_approval"**: Reset messages with `PATCH /v1/agents/{id}/reset-messages` body `{"add_default_initial_messages": false}`, then resend
- **Creating new agents**: Default `system` field contains generic base instructions that override persona memory blocks. PATCH the `system` field to make persona take effect
- **Conversations API**: Returns `AsyncStream`, not `LettaResponse`. Iterate the stream to extract `AssistantMessage` content
