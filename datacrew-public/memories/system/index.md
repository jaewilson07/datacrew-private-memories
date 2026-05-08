---
description: Map of all memory files — what's where and when to read it.
---

# Memory Index

## Always in Context (`system/`)

### Persona — [[system/persona/identity.md]]
Who I am, who I represent, boundaries, voice

### Community — [[system/persona/community.md]]
Who I serve (DUG members), what they need

### Priorities — [[system/persona/priorities.md]]
Mission: help, share knowledge, be present

### Response Rules — [[system/support/response-rules.md]]
How to answer, when to escalate, Slack interaction rules, threading

### Hygiene — [[system/support/hygiene.md]]
Gotchas by theme: Google Docs, cboti, public agent rules

### Infrastructure — [[system/platform/infra.md]]
Where I run, MCP server, skills, tools

### Knowledge — [[system/platform/knowledge.md]]
Durable Domo platform knowledge, core concepts, deprecations

## On-Demand (read when relevant)

### Reference — [[reference/]]
API docs, endpoint details, Domo patterns. Read when a question matches a topic.

### crew-dcs Templates — [[reference/crew-dcs-templates.md]]
Reusable code snippets for common crew-dcs API tasks. Use when answering Domo API questions that can be solved with crew-dcs classes.

### Troubleshooting — [[troubleshooting/]]
Diagnostic runbooks. Read when helping debug an issue.

### Users — [[users/]]
Per-user community profiles (88 users from #domo). Read when interacting with a specific person. Contains: topics they discuss, activity patterns, title/org.

### Message Archive — `messages.db`
SQLite database at `/workspace/dc_public_memories/messages.db` with FTS5 full-text search. Contains ~327 messages from 13 DUG channels. Query with Python `sqlite3` module:
```python
import sqlite3
conn = sqlite3.connect("/workspace/dc_public_memories/messages.db")
cur = conn.execute("SELECT text, user_id FROM messages_fts WHERE text MATCH 'beast mode' LIMIT 5")
```
Channels: public-general, help-etl_sql_beastmodes, help-visualization, help-admin_and_governance, help-ddx_apps_and_automation, help-connectors, help-is_domo_broken, help-ai-agents, help-ai-chat, domo-docs, public-random, public-training_materials, help-everywhere_publish_and_distribution, help-cloud-data-warehouse
