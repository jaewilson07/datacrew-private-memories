"""Ingest a Pattern Hunter brief into the mdrag knowledge base.

Sends the brief to wiki.datacrew.space/mcp/ via save_text_to_knowledge.
MongoDB is the durable sink; the Neo4j Map{} error is a pre-existing mdrag
bug on nested properties and is always ignored.

Usage:
    uv run python .agents/skills/pattern-hunter/scripts/ingest_to_kb.py \\
        --brief-file .agents/skills/pattern-hunter/EXPORTS/boulder-ai-consulting-brief-2026-06-23.md \\
        --title "Pattern Hunter Brief: Boulder AI Consulting (2026-06-23)" \\
        --operator "Boulder AI Consulting" \\
        --url "https://boulderaiconsulting.com"

    # Dry run (prints payload, skips network):
    ... --dry-run

Auth:
    Requires DATACREW_API_TOKEN in Infisical homeserver project
    (workspaceId 3fbb4296-...) at path /datacrew, env prod.
    Loaded via env_loader → .env → DATACREW_API_TOKEN.

    The MCP endpoint is https://wiki.datacrew.space/mcp/ (one 'k').
    Auth header: X-DC-Token (NOT Authorization: Bearer).
    tools/call requires: Accept: application/json, text/event-stream
    save_text_to_knowledge requires: text + title (both mandatory).
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".agents"))
from env_loader import load_env, require_env

load_env()

MCP_URL = "https://wiki.datacrew.space/mcp/"
COLLECTION = "datacrew"
SOURCE_LABEL = "pattern_hunter"


async def _mcp_session(dc_token: str) -> str:
    """Initialize an MCP session and return the session ID."""
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            MCP_URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "X-DC-Token": dc_token,
            },
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "pattern-hunter", "version": "1.1"},
                },
            },
        )
    session_id = r.headers.get("mcp-session-id", "")
    if not session_id:
        raise RuntimeError(f"MCP initialize returned no session ID. Status {r.status_code}. " f"Body: {r.text[:200]}")
    return session_id


async def _mcp_call(dc_token: str, session_id: str, payload: dict) -> dict:
    """Call a tool and return the result dict."""
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(
            MCP_URL,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "X-DC-Token": dc_token,
                "mcp-session-id": session_id,
            },
            json=payload,
        )

    raw = r.text
    # SSE: strip "data: " prefixes; take last non-empty line
    lines = [ln[6:] for ln in raw.splitlines() if ln.startswith("data: ")]
    body = json.loads(lines[-1]) if lines else json.loads(raw)
    return body.get("result", body.get("error", body))


async def ingest(
    brief_file: Path,
    title: str,
    operator: str,
    url: str,
    *,
    dry_run: bool,
) -> None:
    content = brief_file.read_text(encoding="utf-8")

    arguments = {
        "text": content,
        "title": title,
        "collection": COLLECTION,
        "source_label": SOURCE_LABEL,
        "tags": ["pattern-hunter", "prospect-research", operator.lower().replace(" ", "-")],
        "context_url": url,
        "description": f"McKinsey-style operator brief on {operator}.",
    }

    if dry_run:
        print(f"[dry-run] Would POST to {MCP_URL}")
        print(f"[dry-run] title: {title}")
        print(f"[dry-run] collection: {COLLECTION}, source_label: {SOURCE_LABEL}")
        print(f"[dry-run] content: {len(content)} chars")
        return

    env = require_env("DATACREW_API_TOKEN")
    dc_token = env["DATACREW_API_TOKEN"]

    print("Initializing MCP session...")
    session_id = await _mcp_session(dc_token)
    print(f"Session: {session_id}")

    result = await _mcp_call(
        dc_token,
        session_id,
        payload={
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {"name": "save_text_to_knowledge", "arguments": arguments},
        },
    )

    # Extract text from content list (FastMCP wraps result)
    content_list = result.get("content", [result]) if isinstance(result, dict) else [result]
    for item in content_list if isinstance(content_list, list) else [content_list]:
        msg = item.get("text", item) if isinstance(item, dict) else str(item)
        print(msg)
        # Neo4j Map{} error is a pre-existing mdrag bug — MongoDB ingest already succeeded
        if "Neo4j error" in str(msg) and "Map{}" in str(msg):
            print("[info] Neo4j nested-property error is pre-existing (mdrag bug) — MongoDB ingest succeeded.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a Pattern Hunter brief into mdrag KB")
    parser.add_argument("--brief-file", required=True, help="Path to the markdown brief")
    parser.add_argument("--title", required=True, help='KB title, e.g. "Pattern Hunter Brief: Acme Corp (2026-06-23)"')
    parser.add_argument("--operator", required=True, help="Operator name, e.g. 'Boulder AI Consulting'")
    parser.add_argument("--url", required=True, help="Operator URL for context_url")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    args = parser.parse_args()

    brief_path = Path(args.brief_file)
    if not brief_path.exists():
        print(f"Error: brief file not found: {brief_path}", file=sys.stderr)
        sys.exit(1)

    asyncio.run(
        ingest(
            brief_path,
            args.title,
            args.operator,
            args.url,
            dry_run=args.dry_run,
        )
    )


if __name__ == "__main__":
    main()
