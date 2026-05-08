---
description: Domo API endpoints, patterns, and authentication.
---

# Domo API Reference

*Placeholder — to be populated with API endpoint details, auth patterns, and common call examples.*

## Authentication

- Access token via `POST /oauth/token` with client_id/client_secret
- Token scoped to the instance, expires after ~1 hour

## Key Endpoints

- **Datasets:** `GET /v1/datasets/{id}` — metadata, schema, data
- **Users:** `GET /v1/users/{id}` — user profile, roles
- **Pages:** `GET /v1/pages/{id}` — page/collection structure
- **Cards:** `GET /v1/cards/{id}` — card metadata

*Expand with specific patterns as they come up in community questions.*
