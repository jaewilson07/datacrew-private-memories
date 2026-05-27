---
name: sync-memory-stores
description: >-
  Sync agent memory to all external stores (git repo + Domo fileset). Use for: "sync everything", "update memory stores", periodic sync.
metadata:
  version: 1.0.0
  updated: 2026-05-27
---

# sync-memory-stores

Unified memory sync — pushes agent memory to git repo and Domo fileset in one workflow.

## Quick Start

```bash
# Dry run (see what would be synced)
python /workspace/.agents/runbooks/sync-memory-stores/scripts/main.py --dry-run --verbose

# Real sync
python /workspace/.agents/runbooks/sync-memory-stores/scripts/main.py --verbose
```

## What it does

1. **Git sync**: Commits and pushes any changed files in `/workspace` to `datacrew-public` repo
2. **Domo sync**: Calls the existing `sync-memory-to-domo` runbook to push MemFS to Domo fileset

Both steps run independently — one failing doesn't block the other.

## Prerequisites

| Requirement | How to set |
|-------------|-----------|
| Git configured | Repo already has origin with token |
| `MEMORY_DIR` env var | Set by Letta agent runtime |
| `DOMO_INSTANCE` env var | `export DOMO_INSTANCE=domo-community` |
| `DOMO_ACCESS_TOKEN` env var | Retrieve from Infisical: `DOMO-COMMUNITY_ACCESS_TOKEN` |
| `DOMO_FILESET_ID` env var | `export DOMO_FILESET_ID=c0b71cf1-7be3-4340-b021-b3b18eab2f14` |

## Cron

Set up periodic sync via `letta cron`:

```bash
letta cron create --name "memory-stores-sync" --interval "30min" --prompt "Run /sync-memory-stores"
```

## References

- Git repo: `https://github.com/jaewilson07/datacrew-public`
- Domo sync runbook: `.agents/runbooks/sync-memory-to-domo/SKILL.md`
- Domo fileset: `c0b71cf1-7be3-4340-b021-b3b18eab2f14` on `domo-community`

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `dubious ownership` error | `git config --global --add safe.directory /workspace` |
| Push fails | Check GitHub token hasn't expired |
| Domo sync fails | See `sync-memory-to-domo` troubleshooting |
| Nothing to commit | Normal — means all memory is already synced |
