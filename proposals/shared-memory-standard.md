# Shared Memory Standard

**Author:** datacrew-cloud
**Date:** 2026-07-16
**Status:** Proposal — awaiting review from EmmaBot and Jae

---

## Purpose

This repo (`datacrew-private-memories`) is the shared durable knowledge store for DataCrew agents. It complements each agent's MemFS (live system prompt blocks) with git-versioned knowledge that benefits from history, collaboration, and curation.

## What Lives Where

| Layer | Location | Contents | Shared? |
|-------|----------|----------|---------|
| **Live system prompt** | Each agent's `$MEMORY_DIR` (MemFS) | Persona, human prefs, platform, priorities | No — private per agent |
| **Durable knowledge** (this repo) | `shared/` | Domo API docs, crew-dcs patterns, community user profiles, platform knowledge | Yes — both agents read/write |
| **Per-agent private knowledge** (this repo) | `agents/<name>/` | Agent-specific reference, articles, client data | No — private per agent |
| **Skills** (this repo) | `.agents/skills/` | Reusable agent skills | Yes — both agents can use |
| **Proposals** (this repo) | `proposals/` | Feature proposals, architecture docs | Yes — shared |

## Directory Structure

```
datacrew-private-memories/
├── README.md                        ← Repo overview + standard summary
├── AGENTS.md                        ← Repo-level guidance for both agents
├── shared/                          ← Shared memory (both agents read/write)
│   ├── reference/                   ← Domo API docs, crew-dcs patterns, etc.
│   │   ├── index.md                 ← Map of reference docs
│   │   ├── domo-api.md
│   │   ├── crew-dcs-templates.md
│   │   └── project/                 ← Project-specific reference docs
│   ├── knowledge/                   ← Durable Domo platform knowledge
│   │   ├── index.md
│   │   └── ...
│   ├── users/                       ← DUG community member profiles
│   │   ├── index.md
│   │   └── <slack-handle>.md
│   └── skills/                      ← Shared skills (both agents can use)
│       └── <skill-name>/
│           └── SKILL.md
├── agents/                          ← Per-agent private memory
│   ├── datacrew/                    ← DataCrew agent (agent-55e609e7)
│   │   ├── system/
│   │   │   ├── persona.md           ← Identity, boundaries
│   │   │   ├── priorities.md        ← Revenue, pipeline, commitments
│   │   │   └── platform.md          ← Infra, tools, paths
│   │   ├── reference/               ← Private reference docs
│   │   └── clients/                 ← Client data (never shared)
│   └── emmabot/                     ← EmmaBot agent (agent-5afcfa48)
│       ├── system/
│       │   ├── persona.md           ← Identity, boundaries
│       │   ├── priorities.md        ← Community mission
│       │   └── platform.md          ← Infra, tools
│       ├── articles/                ← Article drafts
│       └── reference/               ← EmmaBot-specific reference
├── proposals/                       ← Feature proposals (shared)
├── archives/                        ← Archived content (by month)
│   └── YYYY-MM/
└── .gitignore
```

## File Format Standard

### All memory files

```markdown
---
description: One-line summary of what this file contains and when to read it.
---

# Title

Content...
```

- **Frontmatter**: `description` field is required — it's what shows up in the agent's system prompt metadata and drives discovery.
- **Cross-references**: Use `[[path/to/file]]` links (Letta memory convention). Example: `[[shared/reference/domo-api]]`.
- **File naming**: `kebab-case` for topics (e.g., `domo-api.md`), `camelCase` for user profiles matching Slack handles (e.g., `kensie.rowell.md`).
- **Index files**: Every directory with 3+ files gets an `index.md` that maps contents with one-line descriptions.

### Index file format

```markdown
---
description: Map of all files in this directory — what's where and when to read it.
---

# <Directory Name> Index

## Topic Area 1

### [[file-name]] — Short description
When to read: trigger condition

### [[another-file]] — Short description
When to read: trigger condition
```

## Privacy Boundaries

| Directory | DataCrew | EmmaBot |
|-----------|----------|---------|
| `shared/` | Read/Write | Read/Write |
| `agents/datacrew/` | Read/Write | No access |
| `agents/emmabot/` | No access | Read/Write |
| `proposals/` | Read/Write | Read/Write |
| `.agents/skills/` | Read/Write | Read/Write |

**Enforcement**: Privacy is by convention, not by encryption. Each agent's system prompt must include a rule: "Do not read or write to other agents' private directories." The `.gitignore` excludes secrets and conversation logs.

## Sync Strategy

### MemFS vs. this repo

- **MemFS** (`$MEMORY_DIR`): Live system prompt blocks. Each agent manages their own. NOT synced to this repo.
- **This repo**: Durable knowledge. Synced via git.

### How agents sync

1. **Pull**: Before working, pull latest from `origin/main` to get shared knowledge updates.
2. **Write**: Update shared or private files as needed.
3. **Commit**: Commit changes with conventional commit messages (`feat:`, `fix:`, `docs:`, `chore:`).
4. **Push**: Push to `origin/main`.

### Curation log

Inspired by Ezra's `CURATION_LOG.md`. Each agent logs significant memory updates:

```markdown
## YYYY-MM-DD HH:MM UTC — Agent Name

- **Action**: Created/Updated/Archived <file>
- **Reason**: Why this change was made
- **Impact**: What this affects
```

## .gitignore Rules

```gitignore
# Secrets and credentials
.env
*.key
*.pem
secrets/

# Conversation logs and personal data
conversations/
logs/
*.log

# Large binaries
*.db
*.pkl

# Python cache
__pycache__/
*.pyc

# Node
node_modules/

# Letta internal
.letta/

# Temporary files
*.tmp
*.bak
.DS_Store
```

## Migration Plan

### Phase 1: Restructure (this PR)

1. Create `shared/` directory
2. Move `datacrew-public/memories/reference/` → `shared/reference/`
3. Move `datacrew-public/memories/users/` → `shared/users/`
4. Move `datacrew-public/memories/system/knowledge-store.md` → `shared/knowledge/domo-docs.md`
5. Create `agents/datacrew/` with placeholder system files
6. Move EmmaBot-specific content from `datacrew-public/memories/system/persona/` → `agents/emmabot/system/`
7. Move `datacrew-public/articles/` → `agents/emmabot/articles/`
8. Update `AGENTS.md` with new structure
9. Update `.gitignore`

### Phase 2: Content sync

1. DataCrew populates `agents/datacrew/system/` with current MemFS content
2. EmmaBot populates `agents/emmabot/system/` with her current MemFS content
3. Both agents review and curate `shared/` content

### Phase 3: Automation

1. Set up cron for periodic sync
2. Add curation log tracking
3. Add CI checks for file format compliance

## Relationship to Ezra Pattern

This standard borrows from the [ezra-memory](https://github.com/letta-ai/ezra) template:

- **Archives by month** (`archives/YYYY-MM/`) — same pattern
- **Curation log** — adapted for multi-agent use
- **Skills directory** — shared skills, not per-agent
- **`.gitignore` excludes user data** — same principle

Key differences:

- **Two agents, not curator+prime** — both DataCrew and EmmaBot are autonomous agents with read/write access to shared memory
- **Per-agent private directories** — Ezra doesn't need these because it's a single agent ecosystem; we need them because DataCrew and EmmaBot have different personas, priorities, and access levels
- **No TRAINING_PLAN.md** — our architecture is simpler (two peers, not curator+prime)

## Open Questions

1. **Should we add a third agent (build-partner/stan)?** Jae has a third agent (`agent-0604eb6c`). If so, add `agents/stan/` directory.
2. **Should shared skills be in `.agents/skills/` or `shared/skills/`?** Currently `.agents/skills/` is gitignored. If we want skills in the repo, they need to move.
3. **How often should agents sync?** Manual for now, but should we set up a cron?
4. **Should we add a CODEOWNERS file?** To enforce which agent reviews changes to which directories.
