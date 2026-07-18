# Blue Raven Solutions + DataCrew | Data Platform Consulting — Spring 2026

**DataCrew | Jae Wilson** jae@datacrew.space | 808-765-1506

**Prepared for:** Blue Raven Solutions | **Date:** May 2026

[https://blueravencorp.com/](https://blueravencorp.com/)


## 1. Overview

This document outlines the terms, scope, and working model for a data platform consulting engagement between DataCrew (Jae Wilson, "Consultant") and Blue Raven Solutions ("Client"). The engagement is structured around two service lines — report writing and enablement, and infrastructure strategy and architecture planning — to support the Client's growing analytics capabilities and ensure the data platform scales with the business.

## 2. Engagement Structure

### Service Line 1 — Report Writing and Enablement

**Option A — Monthly Retainer**

**$165 / hour | 40-hour minimum per month | Monthly commitment**

Hours are purchased as a monthly block. Unused hours within the month do not carry forward without a written extension agreement. Additional time may be purchased at the same rate upon mutual agreement.

This structure gives both parties confidence in consistent velocity, predictable availability, and a fixed monthly budget. The retainer model ensures the Consultant is available when the Client needs support — not weeks later.

**Monthly investment:** $6,600 (40 hours at $165/hr)

**Option B — Hourly Engagement**

**$195 / hour | No minimum commitment**

Available for engagements where volume or project duration are limited, or where the Client prefers flexibility over predictable monthly cost. Best suited for ad-hoc requests, one-time deliverables, or situations where monthly demand is uncertain.

Client must pay the initial invoice before work commences. Additional hours will be billed bi-weekly.

### Service Line 2 — Infrastructure Strategy and Architecture Planning

**$250 / hour | Scoped per engagement**

This service line addresses work related to strategic platform planning and architecture initatives.  Deliverables and outcomes from work billed at this rate will typically be strategic and operational guidance as opposed to a reporting asset.

Typical engagements include:

- Current-state assessment and architecture review
- Platform Integration or expansion
- Data pipeline design and optimization
- Governance framework and access model design
- Migration planning and execution strategy

**Estimate provided before work begins.** The Consultant will deliver a scoped estimate with deliverables, timeline, and total hours before any infrastructure engagement commences.

## 3. Scope of Services

### Service Line 1 — Report Writing and Enablement

#### Report Development

The Consultant will build, optimize, and maintain reports and dashboards on the Client's chosen platform. This includes:

- **Dashboard and card development** — new Domo cards, pages, and dashboards built from business requirements; executive KPI dashboards, operational scorecards, and ad-hoc analysis views
- **Data pipeline construction** — Domo connectors, Workbench configurations, Magic ETL dataflows, and MySQL/Redshift dataflows to ingest and transform source data for reporting
- **Beast Mode and calculated field development** — validated business logic in Domo Beast Modes, including complex aggregations, window functions, and conditional calculations
- **Existing report optimization** — performance tuning for slow-loading cards, upstream processing to move heavy calculations out of Beast Modes and into ETL, dataset design improvements to reduce card render time
- **Ad-hoc analysis and data exploration** — answering business questions with structured queries, interim datasets, and exploratory dashboards

#### Enablement and Knowledge Transfer

As part of this engagement, the Consultant will provide structured enablement so that the Client's internal team can operate and extend the reporting environment independently. Enablement is built into the working rhythm, not scheduled as a separate training block.

**Client responsibility:** The Client will identify the users who require handover and training. The Consultant or the Client's designated lead will be responsible for knowledge transfer to ensure the team can maintain and extend deliverables.

**Expected cadence:** At minimum two sessions per topic area:

- Session 1: initial handover and feedback
- Session 2: follow-up and extension

The goal is to ensure each report and dashboard sufficiently empowers the team to address core business questions without ongoing consultant dependency.

#### QA Methodology

QA will take the form of input validation at each phase of the data pipeline. The objective is to identify the break point at any stage of data transformation — where data enters correctly but exits incorrectly, or where logic introduces discrepancy between source and output.

**Approach:**

- For each dataflow under review, inputs will be traced through each transformation step and compared against expected outputs
- Logic errors, join mismatches, and calculation inconsistencies will be documented with root cause and recommended fix
- A QA log will be maintained and shared with the Client as a standing deliverable

**Client responsibility:** The Client is responsible for providing a defined set of known-good values to test against — e.g., a specific date range, project ID, or cost center where the correct answer is known. The Consultant will assist in structuring this reference set if needed.

### Service Line 2 — Infrastructure Strategy and Architecture Planning

#### Current-State Assessment

The Consultant will conduct a structured review of the Client's existing data infrastructure, including:

- Stakeholder interviews to document current workflows, pain points, and growth plans
- Technical review of existing data pipelines, storage, and consumption patterns
- Gap analysis between current capabilities and business requirements
- Risk identification — single points of failure, scalability constraints, governance gaps

**Deliverable:** Assessment report with findings, prioritized recommendations, and a phased roadmap for remediation.

#### Architecture Design and Planning

Based on the assessment findings, the Consultant will design target-state architecture and implementation plans:

- Platform architecture design (cloud, hybrid, or on-prem considerations)
- Data model and pipeline design for scalability
- Access control and governance framework (PDP policies, role-based access, security groups)
- Integration strategy across existing tools and data sources (SEDNA, ERP, supply chain systems)
- Migration or implementation roadmap with milestones and risk mitigation

**Deliverable:** Architecture design document with diagrams, implementation plan, and estimated effort for each phase.

## 4. Out of Scope

The following are not included in this engagement unless separately agreed:

- Direct management of the Client's internal team or hiring decisions
- Software licensing procurement or vendor contract negotiation
- Development outside the agreed platform scope
- Ongoing operational support beyond the retainer period (without renewal)
- Predictive modeling or machine learning development (identified as a future phase)

*Any work outside this scope requires a separate Change Order.*

## 5. Terms

- **Rate and Invoicing:** As specified in Section 2. Card payment via Stripe or ACH transfer.
- **Hours log:** Provided with each invoice; available on request at any time.
- **NDA:** Standard mutual NDA to be executed prior to commencement.
- **Start date:** Upon execution of NDA and confirmation of engagement model.
- **Termination:** Either party may terminate with 30 days written notice. If the Client terminates for convenience, the Client owes 50% of the remaining retainer value for the current month.
- **Intellectual Property:** Upon full payment, the Client owns all deliverables created specifically for the engagement. The Consultant retains ownership of pre-existing methodologies, frameworks, and tools. The Client receives a perpetual, non-exclusive license to use the Consultant's background IP as embedded in deliverables.
- **Limitation of Liability:** The Consultant's total liability under this engagement shall not exceed the total fees paid by the Client during the 12 months preceding the claim.
