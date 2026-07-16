---
description: crew-dcs repo details, conventions, and API patterns. Read when working with Domo APIs or crew-dcs library.
---

# crew-dcs

## Repo Details

- **Repo**: `github.com/hector-dcs/crew-dcs` (private)
- **Access**: Use `HECTOR_GH_PAT` from Infisical (homeserver project, `/datacrew` path)
- **Local clone**: `/tmp/crew-dcs/`
- **Package manager**: `uv` (run `uv sync` then `uv run python` or `uv run pytest`)

## Structure

- `src/crew_dcs/routes/<domain>/` — folder modules for complex APIs
- `src/crew_dcs/classes/Domo<Entity>/` — entity classes
- `tests/unit/routes/<domain>/` — tests

## Route Pattern

- `@gd.route_function` + `@log_call` decorators
- Async, `DomoAuth` first param
- `RouteContext` for config
- Returns `ResponseGetData`

## Domo Auth

| Auth Type | Header | Fields |
|-----------|--------|--------|
| DomoTokenAuth | `{"x-domo-developer-token": token}` | `domo_access_token`, `domo_instance` |
| DomoDeveloperAuth | `{"Authorization": "bearer {token}"}` | `domo_client_id`, `domo_client_secret`, `domo_instance` |

## Key Domo Instances

| Instance | Token Name | Notes |
|----------|-----------|-------|
| domo-community | `DOMO_COMMUNITY_ACCESS_TOKEN` | Data CRUD + alerts work. Objectives return 400. |
| datacrew-space | `DATACREW-SPACE_DOMO-ACCESS-TOKEN` | Dataset CRUD, upload, search. Card creation works. |

## Card Creation Body Format (CRITICAL — PR #1467)

The `PUT /content/v3/cards/kpi` endpoint has DIFFERENT body formats for GET vs CREATE:
- **GET**: `formulas`, `annotations`, `conditionalFormats` are arrays
- **CREATE**: Must be objects with change-tracking sub-keys:
  - `formulas`: `{"dsUpdated": [], "dsDeleted": [], "card": [...]}`
  - `annotations`: `{"new": [], "modified": [], "deleted": []}`
  - `conditionalFormats`: `{"card": [...], "datasource": []}`

## Dashboard/Page Creation API

1. `POST /content/v1/pages` with `{"parentPageId": 0, "title": "..."}` → returns `pageId`
2. `PUT /content/v1/cards/bulk/pages` with `{"cardIds": [...], "destinationPageIds": [pageId]}` → adds cards
3. `POST /content/v4/pages/layouts` with `{"pageUrn": str(pageId), ...}` → creates layout
4. `PUT /content/v4/pages/layouts/{layoutId}` (with writelock) → reposition cards

Layout ID is DIFFERENT from page ID. Standard grid is 60 units wide.

## Known Issues

- **`looper()` session poisoning (Issue #1464 — OPEN)**: Creates temporary httpx session, mutates shared `RouteContext`, then closes session. Poisons context for subsequent calls.
- **Convenience function session lifecycle (Issue #1466 — OPEN)**: Filed proposal for auto-managing httpx session lifecycle.
- **`upload_dataframe` bug (FIXED — PR #1465)**: Used `create_res.response.get("id")` but API returns `{"dataSource": {"dataSourceId": "..."}}`.
- **`set_dataset_tags` bug (FIXED — PR #1465)**: Called `res.set_response()` which doesn't exist. Fixed to direct attribute assignment.
- **httpx session management**: Must pass explicit `httpx.AsyncClient` session via `RouteContext(session=session)`. Without it, each call creates/closes its own session.

## Chart Type Builders (PR #1468)

19 chart type builders in `kpi_builder.py`. Key gotcha: `badge_waterfall` does NOT exist as a Domo chartType — waterfall builder uses `badge_vert_bar` as substitute.

## Alert Builder API

`POST /api/social/v4/alerts` creates alerts. 4 types: SUMMARY_NUMBER, AGGREGATION, ANY_ROW, COLUMN. COLUMN alerts require `GREATER_THAN_EQUAL` operation (not `CHANGES_BY`).
