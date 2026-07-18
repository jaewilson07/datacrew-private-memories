---
sync:
  document_id: 1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws
  tab_id: t.lpmko16pt2gq
  document_title: PeopleFinders [INTERNAL]
  tab_title: 04/20 - Intitial Call
  tab_url: https://docs.google.com/document/d/1qVfk9G5rmA7rSwBdqj2PhuMUbRsjnLU31N1G091wcws/edit?tab=t.lpmko16pt2gq
  source_modified: '2026-04-21T19:36:08.503000+00:00'
  base_revision: ALtnJHxqVJazmYZp2CzBADbFq8VzgkUc5M8fDnDpNi4la5_E_zS-Hgi3CgHAE-pZ7uHB57awxCUz00rnqnK2N1a6v0XCXbngW_RiSklcrOE
  base_sha256: 539ca4e2c376b38d0e206001379dd4b83657d73472285d676cb461cc1b4644f5
  last_synced: '2026-07-18T12:05:17Z'
  last_modified_by: alix.datacrew@gmail.com
---

# JW + PeopleFinders Introduction Call

**Date:** Monday, April 20, 2026 · 2:00 – 3:00 PM MDT **Calendar Event:** [Google Meet](https://meet.google.com/oke-jzuf-xhu) **Proposal:** [PeopleFinders Consulting Proposal](https://docs.google.com/document/d/1S8c8NAxQKPJRhCxo-B0wbQh3EtMbGIMKjT6XoPUVyvU)

## Time Tracking


| Task | Hours |
| --- | --- |
| Discovery Call | 1.0 |
| SOW / Proposal | 1.0 |
| Total | 2.0 |
## Attendees

- Jae Wilson (consultant)
- Shawn Tyler (SVP Marketing)
- Josh Chang (VP Performance Marketing)
- Rob Tulow (Head of BI) — mentioned, not present on call

## Summary

Project kickoff reviewed data infrastructure and Recurly migration goals with an established 5–10 hour weekly scope. Leadership identified critical gaps in session data and current marketing platform reporting — internal teams struggle to unify disparate data sources for accurate conversion tracking. The organization prioritizes migrating from Chargebee to Recurly by May 4, requiring 5 new dashboards. Engagement scope starts at 5–10 hours per week to stabilize Domo and validate existing data joining logic.

## Next Steps

- [Shawn Tyler] Send NDA to Jae Wilson post-meeting
- [Jae Wilson] Create proposal with consulting models and rates; send via email to Shawn Tyler and Josh

## Meeting Notes

### Company

Shawn Tyler (SVP Marketing) flagged urgent need to fix "garbage" data and visitor/session data gaps. Josh Chang (VP Performance Marketing) and Rob Tulow (Head of BI, reports to Josh, based in Denver) round out the leadership. Rob is not a Domo expert — will partner with an external consultant. They advertise heavily on Google and Bing (Search and Display); testing social channels.

### Data Platform

Marketing analytics centers on tying platform cost/clicks/impressions to customer conversions. Multiple internal revenue sources make attribution cumbersome. Billing is moving from Chargebee to Recurly by May 4 — Recurly has a native Domo connector, but migration requires joining multiple tables with complex invoice logic. PowerBI is being dropped on the same deadline, making 5 new dashboards a hard requirement. Mission-critical: drill-down dashboard + affiliate dashboard. Future work: Predictive LTV, revenue forecasting at SKU level, KPIs to ad ID level. Stack: Domo Cloud with Snowflake Amplifier (data lives in Snowflake, accessed via Domo). Quickbooks Online also in scope (status TBD).

### Data Infrastructure

No traditional data warehouse — all raw data (Google, Bing, Chargebee/Recurly, internal session data from Apollo v2) ingested into Domo. Significant joining work already done by Clear Square, but quality is unknown and needs QA. **Do NOT contact Clear Square** for a handover — they will "spook" and productivity drops to zero.

### Engagement

Starting scope: 5–10 hours/week (budget-constrained, pending Clear Square status). Immediate need: stabilize Domo, validate data joining logic, QA existing reports with Domo best practices. Long-term plan: replace Clear Square with a full-time Domo senior analyst (or ongoing consultant model). Start date is flexible but if Clear Square continues to miss (~Apr 27 decision point), Jae may be brought in immediately to hit the May 4 deadline.

## Transcript

**[00:00:00]** Introductions — Jae Wilson, Shawn Tyler; confirmed audio, pleasantries + shared sci-fi interest (Star Trek/Star Wars).

**[00:05:14]** Shawn Tyler background: SVP Marketing, urgent need to fix "garbage" data and internal visitor/session data gaps. Clear Square struggled for 4 months post-POC.

**[00:06:13]** Josh Chang joined with a 25-min hard stop. Call framed as an intro to discuss how Jae works — pricing and engagement model.

**[00:07:00]** Jae Wilson intro: Domo consultant, community contributor, 4 years at Sony.

**[00:07:52]** Company: background checks and reverse phone lookups. Primary Domo use = tying platform data (cost, clicks, impressions) to customer conversions.

**[00:08:49]** Many different internal data sources make accurate conversion tracking cumbersome.

**[00:09:37]** Advertising: Google (majority budget) + Bing; testing social. Billing: Chargebee → Recurly (native Domo connector).

**[00:10:34]** Recurly migration requires joining multiple tables with complex invoice-matching logic.

**[00:10:34 – 00:12:33]** Rob Tulow hired as Head of BI. After stabilization, two critical future projects: predictive LTV and SKU-level revenue forecasting.

**[00:11:41 – 00:43:45]** May 4 = drop-dead date. No PowerBI integration for Recurly, so they'll lose KPI visibility without replacement. 5 dashboards required; drill-down and affiliate are mission-critical.

**[00:12:33]** Want to replace PowerBI resource with a full-time Domo expert. Granular drill-down to ad ID level — Excel hits row limits.

**[00:13:51]** Domo Cloud + Snowflake Amplifier: data lives in Snowflake, accessed via Domo.

**[00:14:42]** Jae Wilson: confident Domo expert, less familiar with performance marketing specifics.

**[00:15:37 – 00:17:37]** Primary need: join data, create a "one source of truth" ETL, fix conflicting answers from different reports.

**[00:17:37]** Minimum engagement: stabilize Domo, ensure data accuracy, refine scoped reports with Domo best practices.

**[00:19:02]** Need visualizations and granular reporting to answer specific business questions.

**[00:19:58]** Long-term plan: bring in full-time Domo senior analyst.

**[00:22:07]** All raw data — marketing channels, Chargebee, Recurly, Apollo v2 session data — ingested into Domo.

**[00:24:38]** Diagrams showed significant joining work already done. Quality unknown, needs QA.

**[00:26:46]** Do NOT contact Clear Square for handover — they'll "spook" and drop to zero productivity.

**[00:29:47]** Proposal requested: a couple of models for pricing and ways of working.

**[00:32:51]** Josh Chang dropped off.

**[00:39:31]** Start date flexible; high likelihood of starting next week if Clear Square continues to miss.

**[00:40:47]** Starting bandwidth: 5–10 hours/week due to budget constraints and unclear Clear Square status.

**[00:43:45]** End of week ~Apr 27 = decision threshold. Need basic dashboards live by May 4.
