# PeopleFinders + DataCrew | Domo — Spring 2026 Consulting Engagement

**DataCrew | Jae Wilson** jae@datacrew.space | 808-765-1506

**Prepared for:** PeopleFinders | **Date:** April 2026

## 1. Overview

This document outlines the terms, scope, and working model for a Domo consulting engagement between DataCrew (Jae Wilson, "Consultant") and PeopleFinders ("Client"). The engagement is scoped to stabilize the Client's existing Domo environment by supporting development and QA activities in the brownfield environment. Known concerns include a migration from ChargeB to Recurly, urgency from a hard PowerBI cutoff, a need to facilitate handover and enablement to a leadership team that is relatively new to Domo, build data trust in the work delivered to date, with an option to support the team on an ongoing basis.

## 2. Engagement Structure

### Option A - 40-Hour Block over 60 Days

**$250 / hour | 40-hour minimum | Hours to be consumed within 60 days of execution**

Hours are purchased as a block. Unused hours within the 60-day window do not carry forward without a written extension agreement. Additional time may be purchased at the same rate upon mutual agreement assuming similar volume.

This structure gives both parties confidence in a consistent velocity and predictable availability and delivery timeline.

The Client has the option of splitting payment into two installments, each due before work commences:

- 12 hours ($3,000 USD)
- 28 hours ($7,000 USD)

### Option B - Flexible Engagement

**$275 / hour | 15-hour minimum commitment**

Available for engagements where volume or project duration are limited. Not recommended for the initial stabilization and migration phase given the brownfield nature of the environment and the May 4th PowerBI cutoff.

Client must pay the initial invoice before work commences. Additional hours will be billed bi-weekly.

## 3. Scope of Services

### Phase 1 — Orientation and Handover (Est. 4–12 hours)

The Consultant will conduct a structured orientation of the existing Domo environment in collaboration with the Client's designated stakeholder(s). This phase is not a prerequisite to delivery — work on Phase 2 will begin concurrently as the environment is understood.

Orientation includes:

- Stakeholder meetings to document what has been built, what is in progress, and where known gaps exist
- Technical review and gap analysis of existing ETL logic and Beast Modes with a goal of understanding how to build trust and confidence in the pipelines long-term — pipeline performance optimization will be a Phase 3 goal after stabilization
- Priority will be aligning brownfield work with the previous scope of work and establishing data trust

**Working cadence during orientation:** 1–3 hours of meetings or stakeholder review per session, followed by 3–4 hours of independent work before the next touchpoint. The Client should expect to make a stakeholder available for these sessions on a reasonable schedule.

**Client responsibility:** Identify one primary stakeholder to participate in orientation sessions and serve as the primary point of contact for questions about existing logic and business rules, as well as provide a series of validation points to establish the baseline for "correct."

**Final deliverable:** Consultant delivers a model for documenting the estate and UAT metrics to serve as a baseline validation framework for existing and new data points.

### Phase 2 — Stabilization and Dashboard Delivery (Scope confirmed in Phase 1)

The breadth of deliverables will be defined and confirmed during Phase 1.

Known concerns include:

- Recurly connector wired into existing data flows
- Appropriate granularity in marketing drill-down (ad ID level)
- Affiliate dashboard delivery

### Phase 3 — Enablement and Handover (Est. 5–10 hours)

As part of this engagement, the Consultant will provide structured enablement so that the Client's internal team understands and can operate the QA process independently. Enablement is built into the working rhythm, not scheduled as a separate training block.

**Client responsibility:** The primary stakeholder will identify the users who require handover and training, and either the Consultant or the primary stakeholder will be responsible for transfer of knowledge and UAT efforts with those teams to ensure dashboard usability.

**Expected cadence:** Depends on level of effort and level of rigor required by the Client. At minimum two sessions per topic area:

- Session 1: initial handover and feedback
- Session 2: follow-up and extension

Reviewing findings, walking through logic, and confirming the Client's team is oriented to what was built and why. The goal is to ensure that each dashboard sufficiently empowers the team to address core business questions.

As dashboards and data areas clear this checkpoint, handover and the responsibility of ongoing maintenance either move to the primary stakeholder's MajorDomo persona, or the parties draft an ongoing support model with the Consultant.

## 4. QA Methodology

QA will take the form of input validation at each phase of the ETL pipeline. The objective is to identify the break point at any stage of data transformation — where data enters correctly but exits incorrectly, or where logic introduces discrepancy between source and output.

**Approach:**

- For each dataflow under review, inputs will be traced through each transformation step and compared against expected outputs
- Logic errors, join mismatches, and calculation inconsistencies will be documented with root cause and recommended fix
- A QA log will be maintained and shared with the Client as a standing deliverable

**Client responsibility:** The Client is responsible for providing a defined set of known-good values to test against — e.g., a specific date range, customer ID, or campaign where the correct answer is known. The Consultant will assist in structuring this reference set if needed.

## 5. Out of Scope

The following are not included in this engagement unless separately agreed:

- Direct communication with or handover from the current vendor (ClearSquare)
- Predictive LTV modeling or revenue forecasting (identified as a future phase)
- Snowflake-side development (adoption of Domo's Snowflake Cloud Amplifier with pushdown processing)

## 6. Terms

- **Rate and Invoicing:** Card payment via Stripe as specified in Section 2
- **Hours log:** Provided with each invoice; available on request at any time
- **NDA:** Standard mutual NDA to be executed prior to commencement
- **Start date:** Upon execution of NDA and confirmation of engagement model
