"""Upsert a Pattern Hunter brief as a tab in the shared Pattern Hunter GDoc.

Tab title = "<operator-slug> <YYYY-MM-DD>" (max 50 chars, auto-truncated).
If the doc doesn't exist yet, pass --create-doc to create and share it.

Usage:
    uv run python .agents/skills/pattern-hunter/scripts/publish_to_gdoc.py \\
        --brief-file .agents/skills/pattern-hunter/EXPORTS/summit-ai-consultants-brief-2026-06-23.md \\
        --tab-title "Summit AI 2026-06-23"

    # Create the doc on first run:
    uv run python .agents/skills/pattern-hunter/scripts/publish_to_gdoc.py \\
        --brief-file ... --tab-title "..." --create-doc

    # Dry run:
    uv run python .agents/skills/pattern-hunter/scripts/publish_to_gdoc.py \\
        --brief-file ... --tab-title "..." --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

# ── env_loader (monorepo root .agents/) ──────────────────────────────────────
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".agents"))
from env_loader import load_env, require_env

load_env()

# ── cboti imports (after env is loaded) ──────────────────────────────────────
from cboti.integrations.google.drive.service import GoogleDriveService  # noqa: E402

SHARE_EMAIL = "jae@datacrew.space"
DOC_TITLE = "Pattern Hunter — Prospect Research"
ENV_DOC_ID_KEY = "PATTERN_HUNTER_DOC_ID"


async def _get_or_create_doc(
    service: GoogleDriveService,
    doc_id: str | None,
    *,
    create: bool,
    dry_run: bool,
) -> str:
    if doc_id:
        return doc_id

    env_doc_id = os.getenv(ENV_DOC_ID_KEY, "").strip()
    if env_doc_id:
        return env_doc_id

    if not create:
        print(
            f"Error: no --doc-id and {ENV_DOC_ID_KEY} not set.\n"
            "Run with --create-doc to create the document on first use,\n"
            f"then set {ENV_DOC_ID_KEY}=<id> in your .env.",
            file=sys.stderr,
        )
        sys.exit(1)

    if dry_run:
        print(f"[dry-run] Would create GDoc: '{DOC_TITLE}' and share with {SHARE_EMAIL}")
        return "(dry-run-doc-id)"

    doc = await service.api.create_document(DOC_TITLE)
    new_id = doc.id
    await service.api.share_file(new_id, SHARE_EMAIL, role="writer")
    url = f"https://docs.google.com/document/d/{new_id}/edit"
    print(f"Created doc: {DOC_TITLE}")
    print(f"URL: {url}")
    print(f"\nAdd to your .env:\n  {ENV_DOC_ID_KEY}={new_id}\n")
    return new_id


async def publish(
    brief_file: Path,
    tab_title: str,
    doc_id: str | None,
    *,
    create_doc: bool,
    dry_run: bool,
) -> None:
    content = brief_file.read_text(encoding="utf-8")

    if dry_run:
        resolved_doc_id = doc_id or os.getenv(ENV_DOC_ID_KEY, "(unset)")
        print(f"[dry-run] Doc ID: {resolved_doc_id}")
        print(f"[dry-run] Would upsert tab: '{tab_title}' (mode=replace)")
        print(f"   Content preview ({len(content)} chars):")
        print("   " + content[:300].replace("\n", "\n   ") + ("…" if len(content) > 300 else ""))
        return

    env = require_env("GDOC_CLIENT", "GDOC_TOKEN")

    service = GoogleDriveService(
        credentials_json=env["GDOC_CLIENT"],
        token_json=env["GDOC_TOKEN"],
    )

    resolved_doc_id = await _get_or_create_doc(service, doc_id, create=create_doc, dry_run=dry_run)

    tab_id = await service.docs_api.create_tab_with_content(
        resolved_doc_id,
        tab_title,
        content,
        mode="replace",
    )

    url = f"https://docs.google.com/document/d/{resolved_doc_id}/edit"
    print(f"Tab '{tab_title}' upserted — tabId: {tab_id}")
    print(f"Doc: {url}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Upsert a Pattern Hunter brief as a GDoc tab")
    parser.add_argument(
        "--brief-file",
        required=True,
        help="Path to the markdown brief (e.g. EXPORTS/summit-ai-2026-06-23.md)",
    )
    parser.add_argument(
        "--tab-title",
        required=True,
        help='Tab display name, e.g. "Summit AI 2026-06-23" (max 50 chars)',
    )
    parser.add_argument(
        "--doc-id",
        default=None,
        help=f"Google Doc ID (overrides {ENV_DOC_ID_KEY} env var)",
    )
    parser.add_argument(
        "--create-doc",
        action="store_true",
        help="Create the Pattern Hunter doc if it doesn't exist yet",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing to Google Docs",
    )
    args = parser.parse_args()

    brief_path = Path(args.brief_file)
    if not brief_path.exists():
        print(f"Error: brief file not found: {brief_path}", file=sys.stderr)
        sys.exit(1)

    asyncio.run(
        publish(
            brief_path,
            args.tab_title,
            args.doc_id,
            create_doc=args.create_doc,
            dry_run=args.dry_run,
        )
    )


if __name__ == "__main__":
    main()
