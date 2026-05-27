#!/usr/bin/env python3
"""Sync agent memory to all external stores.

Orchestrates:
1. Git sync — commit and push changes in /workspace to datacrew-public repo
2. Domo sync — push MemFS files to Domo fileset via existing runbook

Usage:
    python main.py [--dry-run] [--verbose] [--git-only] [--domo-only]
"""

from __future__ import annotations

import argparse
import asyncio
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE_DIR = Path("/workspace")
MEMORY_DIR = Path(os.environ.get("MEMORY_DIR", ""))
DOMO_SYNC_SCRIPT = WORKSPACE_DIR / ".agents/runbooks/sync-memory-to-domo/scripts/main.py"


# ---------------------------------------------------------------------------
# Git sync
# ---------------------------------------------------------------------------


def git_sync(dry_run: bool = False, verbose: bool = False) -> dict:
    """Commit and push changes in the workspace repo.

    Returns a dict with counts: {committed, pushed, errors}.
    """
    result = {"committed": 0, "pushed": 0, "errors": 0, "files": []}

    # Ensure safe.directory is set
    subprocess.run(
        ["git", "config", "--global", "--add", "safe.directory", str(WORKSPACE_DIR)],
        capture_output=True,
    )

    # Check for changes
    status_result = subprocess.run(
        ["git", "-C", str(WORKSPACE_DIR), "status", "--porcelain"],
        capture_output=True,
        text=True,
    )

    if status_result.returncode != 0:
        print(f"ERROR: git status failed: {status_result.stderr}")
        result["errors"] = 1
        return result

    changed_files = [
        line.strip() for line in status_result.stdout.strip().split("\n") if line.strip()
    ]

    if not changed_files:
        if verbose:
            print("Git: No changes to commit")
        return result

    result["files"] = changed_files
    if verbose:
        print(f"Git: {len(changed_files)} changed files:")
        for f in changed_files:
            print(f"  {f}")

    if dry_run:
        print("Git: [DRY RUN] Would commit and push")
        result["committed"] = len(changed_files)
        return result

    # Stage all changes
    stage_result = subprocess.run(
        ["git", "-C", str(WORKSPACE_DIR), "add", "-A"],
        capture_output=True,
        text=True,
    )
    if stage_result.returncode != 0:
        print(f"ERROR: git add failed: {stage_result.stderr}")
        result["errors"] = 1
        return result

    # Commit
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    commit_message = f"sync: memory update ({timestamp})"

    commit_result = subprocess.run(
        ["git", "-C", str(WORKSPACE_DIR), "commit", "-m", commit_message],
        capture_output=True,
        text=True,
    )
    if commit_result.returncode != 0:
        # Could be "nothing to commit" — check if that's the case
        if "nothing to commit" in commit_result.stdout:
            if verbose:
                print("Git: Nothing to commit")
            return result
        print(f"ERROR: git commit failed: {commit_result.stderr}")
        result["errors"] = 1
        return result

    result["committed"] = len(changed_files)
    if verbose:
        print(f"Git: Committed {result['committed']} files")

    # Push
    push_result = subprocess.run(
        ["git", "-C", str(WORKSPACE_DIR), "push", "origin", "main"],
        capture_output=True,
        text=True,
    )
    if push_result.returncode != 0:
        print(f"ERROR: git push failed: {push_result.stderr}")
        result["errors"] = 1
        return result

    result["pushed"] = result["committed"]
    if verbose:
        print(f"Git: Pushed to origin/main")

    return result


# ---------------------------------------------------------------------------
# Domo sync
# ---------------------------------------------------------------------------


def domo_sync(dry_run: bool = False, verbose: bool = False) -> dict:
    """Run the existing sync-memory-to-domo script.

    Returns a dict with counts: {uploaded, skipped, errors, total}.
    """
    if not DOMO_SYNC_SCRIPT.exists():
        print(f"ERROR: Domo sync script not found: {DOMO_SYNC_SCRIPT}")
        return {"uploaded": 0, "skipped": 0, "errors": 1, "total": 0}

    if verbose:
        print("Domo: Starting sync...")

    # Run as subprocess to avoid import issues
    cmd = [sys.executable, str(DOMO_SYNC_SCRIPT)]
    if dry_run:
        cmd.append("--dry-run")
    if verbose:
        cmd.append("--verbose")

    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if verbose and result.stdout:
        print(result.stdout)
    
    if result.returncode != 0:
        print(f"ERROR: Domo sync failed: {result.stderr}")
        return {"uploaded": 0, "skipped": 0, "errors": 1, "total": 0}

    # Parse output for counts (format: "Sync complete: X uploaded, Y unchanged, Z errors")
    # Default to success counts if parsing fails
    return {"uploaded": 0, "skipped": 0, "errors": 0, "total": 0, "success": True}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main_sync(
    dry_run: bool = False,
    verbose: bool = False,
    git_only: bool = False,
    domo_only: bool = False,
) -> dict:
    """Run all sync steps and return combined results."""
    results = {"git": None, "domo": None}

    print(f"=== Memory Stores Sync {'[DRY RUN]' if dry_run else ''} ===\n")

    # Git sync
    if not domo_only:
        print("[1/2] Git sync...")
        results["git"] = git_sync(dry_run=dry_run, verbose=verbose)
        print()

    # Domo sync
    if not git_only:
        print("[2/2] Domo sync...")
        results["domo"] = domo_sync(dry_run=dry_run, verbose=verbose)
        print()

    # Summary
    print("=== Summary ===")
    if results["git"]:
        git = results["git"]
        print(f"Git: {git.get('committed', 0)} committed, {git.get('pushed', 0)} pushed, {git.get('errors', 0)} errors")
    if results["domo"]:
        domo = results["domo"]
        print(f"Domo: {domo.get('uploaded', 0)} uploaded, {domo.get('skipped', 0)} skipped, {domo.get('errors', 0)} errors")

    return results


def main():
    parser = argparse.ArgumentParser(description="Sync agent memory to all external stores")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be synced without making changes")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed progress")
    parser.add_argument("--git-only", action="store_true", help="Only run git sync")
    parser.add_argument("--domo-only", action="store_true", help="Only run Domo sync")
    args = parser.parse_args()

    result = main_sync(
        dry_run=args.dry_run,
        verbose=args.verbose,
        git_only=args.git_only,
        domo_only=args.domo_only,
    )

    # Exit with error if any step failed
    has_errors = any(
        r and r.get("errors", 0) > 0 for r in result.values() if r
    )
    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
