---
description: cboti Google Docs API details — how to use GoogleDoc class, Tabs.upsert, auth patterns. Read when writing to Google Docs.
---

# cboti Google Docs

## Overview

cboti is the Google Workspace integration library. It has a full markdown-to-Docs conversion pipeline.

## Key Classes

- `GoogleAuth` — OAuth, service account, and auth flow support
- `GoogleDoc` — Google Docs operations
- `GoogleDriveService` — facade for drive operations
- `GoogleSheets` — Google Sheets operations
- `GoogleClients` / `GoogleWorkspace` — higher-level clients

## Auth

```python
from cboti.integrations.google.auth import GoogleAuth
from cboti.integrations.google.drive.google_docs import GoogleDoc

auth = GoogleAuth(
    credentials_json=os.environ["GDOC_CLIENT"],
    token_json=os.environ["GDOC_TOKEN"]
)
```

## Writing to Google Docs

Use `Tabs.upsert(doc_id, title, content)` — writes markdown to a Google Doc tab. It converts markdown to proper Google Docs formatting (headings, bold, lists, tables, links).

**Never use `write_markdown_to_tab`** — it appends instead of upserting.

## Gotchas

- **Tab creation NOT supported**: Google Docs API `batchUpdate` does NOT support `createTab` requests. Tabs can only be created via the UI. Use headings and horizontal rules within existing tab instead.
- **`includeTabsContent=true` returns empty content**: Use the default (no parameter) to get actual content.
- **Insert index must be < endIndex**: To insert text at end of document, use `endIndex - 1` (not `endIndex`).
- **Use Python for content with special characters**: Bash `curl` with inline JSON fails on special characters. Use Python's `requests` library with `json.dumps()`.
- **Markdown blockquotes (`> `) are stripped in Google Docs**: Use **bold-labeled paragraphs** instead.
- **Google Doc tab IDs are document-scoped**: Always `Tabs.list(doc_id)` for the target doc first.

## Known Doc IDs

- "The Secret CFO" (AI CFO/CSO project doc): `19P6rcsZpL9qs44vYewsOikRHAxfWZ0Xfj7wx6Wtp1mg`

## Token Details

- `access_token` + `refresh_token` in `GDOC_TOKEN` env var (JSON)
- Client ID/secret in `GDOC_CLIENT` and `GDOC_CLIENT_SECRET`
- Scopes: spreadsheets, documents, drive.file, userinfo.email, openid, userinfo.profile
- Limitation: `drive.file` scope only allows access to files created/opened by this OAuth client
- Refresh: POST to `https://oauth2.googleapis.com/token` with `client_id`, `client_secret`, `refresh_token`, `grant_type=refresh_token`
- Infisical project: homeserver (`3fbb4296-d4e6-4c17-83ee-b852a57a5e50`), env: prod, path: `/datacrew`

## Repo

- Separate git repo (private) — NOT tracked by simpleDiscordBot's git
- Location: `libraries/cboti/` within the simpleDiscordBot monorepo
- Git operations: Must run from inside `libraries/cboti/`
