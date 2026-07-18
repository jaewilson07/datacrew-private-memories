---
sync:
  document_id: 1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws
  tab_id: t.vwlls0wz1gw5
  document_title: PeopleFinders [INTERNAL]
  tab_title: Tech Stack
  tab_url: https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.vwlls0wz1gw5
  source_modified: '2026-04-21T19:36:08.503000+00:00'
  base_revision: ALtnJHxqVJazmYZp2CzBADbFq8VzgkUc5M8fDnDpNi4la5_E_zS-Hgi3CgHAE-pZ7uHB57awxCUz00rnqnK2N1a6v0XCXbngW_RiSklcrOE
  base_sha256: 65b80d0254420beedbc0c4ad0aaf063c0e4db8261b843b6af5d40f90a26d8431
  last_synced: '2026-07-18T12:05:17Z'
  last_modified_by: alix.datacrew@gmail.com
---

# Tech Stack

## Domo

- **Domo Cloud instance**
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq)
- **Snowflake Amplifier configured**
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq) [00:13:51]
- **Data lives in Snowflake, accessed via Domo**
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq)
- **Dropping PowerBI by May 4**
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq) [00:11:41]

## Data Sources

- **Google Ads** — Active, majority of ad spend
- **Bing Ads** — Active, secondary channel
- **Social** — Testing, not yet primary
- **Chargebee** — Migrating → Recurly by May 4
- **Recurly** — Incoming, native Domo connector
- **Apollo v2** — Active, session data source
- **Quickbooks Online** — TBD, in scope, status unclear

## Data Architecture

Data Sources (Google, Bing, Chargebee/Recurly, Apollo v2)

        │

        ▼

Snowflake (DWH) — All raw data stored here

        │

        ▼ (Snowflake Amplifier)

Domo Cloud — ETL, Dashboards, Reporting

        │

        └── 5 new dashboards needed by May 4

## Dashboards Required (by May 4)

- **Drill-down** — 🔴 Mission-critical, not started
- **Affiliate** — 🔴 Mission-critical, not started
- **TBD #3** — Required, not started
- **TBD #4** — Required, not started
- **TBD #5** — Required, not started

## Future Tech Goals

- **Predictive LTV modeling** — Post-stabilization
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq) [00:10:34]
- **SKU-level revenue forecasting** — Post-stabilization
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq) [00:10:34]
- **Ad ID level drill-down** — Excel hits row limits
  - Source: [2026-04-20 Initial Call](https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq) [00:12:33]

*Last updated: 2026-04-20*
