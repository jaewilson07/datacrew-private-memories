---
description: Durable Domo platform knowledge — architecture, deprecations, key concepts.
---

# Domo Knowledge

This file holds durable Domo platform knowledge that's always in context. For detailed reference material, see [[reference/]].

## Core Concepts

- **Datasets** — the fundamental data unit in Domo. Fed by connectors, SQL, or APIs
- **Cards** — visualizations on a dataset. Live in pages/dashboards
- **Beast Modes** — calculated columns/measures written in SQL-like syntax, scoped to a card
- **Dataflows** — ETL pipelines: MySQL, Redshift, Magic ETL, Python, R
- **App Studio** — build custom apps on top of Domo datasets
- **Governance** — PDP policies, roles, card-level permissions

## Key APIs

- **Domo API** — `api.domo.com/v1/...` (datasets, users, pages, etc.)
- **Domo App API** — for App Studio custom interactions
- **Lineage API** — `GET /api/data/v1/lineage/{entity_type}/{entity_id}?traverseUp=true&traverseDown=true`
- **AI Readiness API** — `GET/POST/PUT /api/ai/readiness/v1/data-dictionary/dataset/{dataset_id}`
- **Page Layout API** — `GET/PUT /api/content/v4/pages/layouts/{layout_id}`
- **AppStudio API** — `GET/PUT /api/content/v1/dataapps/{appstudio_id}`
- **See [[reference/domo-api.md]] for endpoint details**

## Deprecations & Changes

- **Domo has NO auto-arrange API** for dataflow canvas — layout must be computed client-side
- *(Track known deprecations here as they come up)*
