# datacrew-private-memories

Shared durable knowledge store for DataCrew agents. Complements each agent's MemFS (live system prompt blocks) with git-versioned knowledge that benefits from history, collaboration, and curation.

## Structure

```
datacrew-private-memories/
├── system/                          ← Shared, always-pinned (all agents read)
│   ├── index.md                     ← Memory routing map
│   ├── platform/                    ← Shared platform knowledge
│   └── governance.md                ← Who can write where, placement test
├── reference/                       ← Shared, on-demand (all agents can read)
│   ├── index.md
│   ├── domo/                        ← Domo-specific reference
│   ├── patterns/                    ← Generalized lessons
│   └── project/                     ← Project-specific reference docs
├── users/                           ← Per-user profiles (loaded on demand)
├── agents/                          ← Per-agent private namespace
│   ├── datacrew/                    ← DataCrew agent (agent-55e609e7)
│   ├── idrisbot/                    ← IdrisBot agent (agent-0604eb6c)
│   └── emmabot/                     ← EmmaBot agent (agent-5afcfa48)
├── proposals/                       ← Feature proposals (shared)
├── archives/                        ← Archived content (by month)
└── .gitignore
```

## File Format

All memory files use markdown with YAML frontmatter:

```markdown
---
description: One-line summary of what this file contains and when to read it.
---

# Title

Content...
```

- **Frontmatter**: `description` field is required
- **Cross-references**: `[[path/to/file]]` links (Letta memory convention)
- **File naming**: `kebab-case` for topics, `camelCase` for user profiles matching Slack handles
- **Index files**: Every directory with 3+ files gets an `index.md`

## Placement Test

Before adding anything to `system/`, ask:

1. Is it durable across many future conversations?
2. Does it affect behavior often enough to justify always-on tokens?
3. Is it global rather than specific to one agent/user/incident?

If any answer is no, it goes to `reference/` or `agents/<name>/`.

## Privacy Boundaries

| Directory | DataCrew | IdrisBot | EmmaBot |
|-----------|----------|----------|---------|
| `system/` | Read/Write | Read/Write | Read/Write |
| `reference/` | Read/Write | Read/Write | Read/Write |
| `users/` | Read/Write | Read/Write | Read/Write |
| `agents/datacrew/` | Read/Write | No access | No access |
| `agents/idrisbot/` | No access | Read/Write | No access |
| `agents/emmabot/` | No access | No access | Read/Write |
| `proposals/` | Read/Write | Read/Write | Read/Write |

Privacy is by convention, not encryption. Each agent's system prompt includes: "Do not read or write to other agents' private directories."

## Sync Strategy

- **MemFS** (`$MEMORY_DIR`): Live system prompt blocks. Each agent manages their own. NOT synced to this repo.
- **This repo**: Durable knowledge. Synced via git.
- **Pull** before working, **commit** with conventional messages, **push** to `origin/main`.

## Related

- [[proposals/shared-memory-standard]] — Original proposal
- Template: [letta-ai/ezra](https://github.com/letta-ai/ezra)
