---
name: setup-shared-memory-access
description: >-
  Set up access to the shared multi-agent memory repo. Use when an agent needs
  to connect their MemFS to the datacrew-private-memories shared store.
metadata:
  version: 1.0.0
  updated: 2026-07-16
---

# setup-shared-memory-access

Connect an agent's environment to the shared multi-agent memory repo.

## Prerequisites

- The agent must be running on bonker (or have access to the filesystem)
- The agent must have a GitHub PAT for `jaewilson07` repos
- The agent must have `letta` CLI available for cron setup

## Steps

### 1. Clone the repo (if not already cloned)

```bash
cd /home/jaewilson07/GitHub
git clone https://github.com/jaewilson07/datacrew-private-memories.git
```

If you already have it cloned, pull latest:

```bash
cd /home/jaewilson07/GitHub/datacrew-private-memories
git pull origin main
```

### 2. Add a memory block to your MemFS

Create a system memory block that references the shared store. This goes in your
`$MEMORY_DIR/system/` directory so it's always in your context window.

Use the `memory` tool to create a file at `system/shared-memory-store.md` with:

```markdown
# Shared Memory Store

A git-versioned shared knowledge store for all DataCrew agents.

## Location

- **Local clone**: `/home/jaewilson07/GitHub/datacrew-private-memories/`
- **Remote**: `https://github.com/jaewilson07/datacrew-private-memories.git`

## Structure

- `system/` — Shared, pinned (governance, platform, Letta config)
- `reference/` — Shared, on-demand (Domo API, crew-dcs, patterns)
- `users/` — Shared (DUG community member profiles)
- `agents/<your-name>/` — Your private memory (read/write)
- `agents/<other-agents>/` — Other agents' private memory (DO NOT READ)

## Rules

1. Read from `system/`, `reference/`, `users/`, `proposals/` — shared
2. Read and write to `agents/<your-name>/` — your private memory
3. DO NOT read other agents' private directories
4. When you learn something durable, write it to the repo and push
5. Pull before working to pick up updates from other agents
```

### 3. Set up a pull cron

Pull latest changes from the shared repo periodically:

```bash
letta cron create \
  --name "shared-memory-pull" \
  --interval "30min" \
  --prompt "Pull latest from /home/jaewilson07/GitHub/datacrew-private-memories and update any shared knowledge references"
```

### 4. Populate your agent directory

Write your private memory files to `agents/<your-name>/`:

- `persona.md` — Your identity, values, working style, boundaries
- `platform.md` — Your running environment, tools, paths
- `priorities.md` — Your current priorities and commitments
- `reference/` — Your private reference docs

### 5. Push your changes

```bash
cd /home/jaewilson07/GitHub/datacrew-private-memories
git add agents/<your-name>/
git commit -m "feat: populate agents/<your-name>/ with private memory"
git push origin main
```

If push fails with permission denied, use the PAT:

```bash
source /home/jaewilson07/GitHub/.env
git push https://jaewilson07:${JAEWILSON07_GH_PAT}@github.com/jaewilson07/datacrew-private-memories.git main
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

- `description` field is required
- Use `[[path/to/file]]` for cross-references
- `kebab-case` for topics, `camelCase` for user profiles
- `index.md` in every directory with 3+ files

## Placement Test

Before adding to `system/`, ask:
1. Is it durable across many future conversations?
2. Does it affect behavior often enough to justify always-on tokens?
3. Is it global rather than specific to one agent?

If any answer is no, it goes to `reference/` or `agents/<name>/`.

## Privacy

- Privacy is by convention, not encryption
- Each agent's system prompt includes: "Do not read other agents' private directories"
- `.gitignore` excludes secrets, `.env`, conversation logs, large binaries
- Client data goes in `agents/datacrew/clients/` only — never in shared directories

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Permission denied` on push | Use `JAEWILSON07_GH_PAT` from `/home/jaewilson07/GitHub/.env` |
| `agents/<name>/` not tracked | Check `.gitignore` — `datacrew/` pattern was scoped to `/datacrew/` |
| Cron not running | Check with `letta cron list` |
| Merge conflicts | Pull first, resolve, then push |
