# Blue Raven Solutions — Discovery Interview Guide

**Created:** 2026-07-17
**Engagement Mode:** SCOPE HOLD (maximum rigor on existing plan)
**Phase:** Discovery
**Artifact Type:** Interview guide + KPI/OKR design framework

---

## Pre-Interview Brief

### Company: Blue Raven Solutions
- **Industry:** Aerospace & Defense supply chain distribution
- **Size:** 20-30 employees (LinkedIn), 51-200 (TheOrg)
- **HQ:** Morristown, NJ
- **Structure:** Unified from Crestwood Technology Group (CTG) + Triman Industries
- **Funding:** $500M total (1 round)
- **Platform:** SEDNA (proprietary supply chain intelligence — demand forecasting, predictive insights)
- **Customers:** Government, defense, commercial aviation (program managers, fleet operators)
- **Key services:** Distribution, strategic sourcing, obsolescence/DMSMS management, counterfeit avoidance, kitting, inventory, logistics
- **Website:** blueravencorp.com

### Contact: Ryan LeBon, CFO
- Ex-Deloitte (audit manager, large public registrants)
- Ex-GE (senior controller, Water & Process Technologies)
- Ex-Aquatrols (CFO, PE-backed specialty chemicals — led efficiency projects)
- CPA, Villanova
- At Blue Raven since December 2019 (6+ years)

### Industry Context (from research)
- A&D Cash-to-Cash (C2C) cycles increased 60% (2000-2012) — working capital is the #1 financial issue
- Inventory is climbing (just-in-case, not just-in-time) — carrying costs are significant
- DMSMS/obsolescence management is a major cost driver — proactive management can save millions (Keyport: $225M cost avoidance in 18 months)
- Defense contracts are fixed-price with tight margins — cost control is critical
- Customer concentration is high (few large defense customers) — risk management is key
- Industry is moving from retrospective KPIs to real-time, predictive indicators
- AI-driven predictive analytics can improve demand forecasting by up to 40% and predict supplier defaults with 70-90% precision

### Industry KPI Reference

**Financial:**
- Cash-to-Cash (C2C) cycle
- Days Working Capital
- EBITDA Margin / Operating margin
- Revenue per employee
- Customer Concentration Index

**Inventory:**
- Inventory Turnover Ratio
- Aging inventory / Days of Inventory
- Inventory carrying cost
- Obsolescence rate / DMSMS risk exposure
- Fill rate / Perfect Order Fulfillment

**Operational:**
- On-Time Delivery Rate (OTD)
- Order Cycle Time
- AOG (Aircraft on Ground) resolution time
- Supplier quality rating
- Counterfeit avoidance rate
- Compliance rate (ITAR, DFARS, CMMC)

**Strategic:**
- Contract backlog / pipeline
- Cost avoidance (from DMSMS management)
- SEDNA platform utilization / forecast accuracy

---

## The Interview Flow (6 stages, ~45 minutes)

*Updated after Wipfli Prime Growth System comparison — added Stage 3: Data Source Mapping and KPI Feasibility Matrix to address the Domo implementation requirement.*

### Stage 1: Context Setting (5 min)
**Goal:** Warm up, understand the business model, establish rapport.

**Opening:**
"Ryan, walk me through how Blue Raven Solutions makes money. Not the pitch — the actual mechanics. A customer needs a part. What happens next? Where does the margin come from?"

**Follow-up:**
"You consolidated CTG and Triman under one brand. What did that change about how you measure success? Are there metrics you used to track at CTG or Triman that don't make sense anymore — or new ones the combined company needs?"

**STOP Gate 1:** "Here's what I'm hearing: [paraphrase business model]. Did I get that right? What am I missing?"

---

### Stage 2: Current State — The Status Quo (10 min)
**Goal:** What are they tracking now? What's the workaround?
**Forcing Question:** Q2 (Status Quo)

**Questions:**
1. "Walk me through a typical Monday morning. What numbers do you look at first? What report would you be lost without?"
2. "What's the one report you pull every week that you immediately regret spending time on? The one that takes effort but doesn't change any decisions?"
3. "You've got SEDNA — your proprietary supply chain intelligence platform. It does demand forecasting and predictive insights. How much of what SEDNA tells you actually drives decisions? Is it 'we check it daily and act on it' or 'we check it monthly and it's mostly confirmation'?"
4. "When you're making inventory decisions — what to buy, what to hold, what to let go obsolete — what numbers are you looking at? Is it gut feel, a spreadsheet, SEDNA, or something else?"

**STOP Gate 2:** "So today, you're tracking [list what they track] but you're NOT tracking [list gaps]. And the decisions that hurt the most are [list]. Right?"

---

### Stage 3: Data Source Mapping (10 min) — NEW
**Goal:** Understand what data exists, where it lives, what format it's in, and whether Domo can connect to it. This is the bridge between the interview and the Domo implementation.
**Wipfli Parallel:** Component 7 (Technology Optimization and Alignment) — "We work to understand all existing data sources."

**Questions:**
1. "What ERP or inventory management system do you use? NetSuite? SAP? Dynamics? QuickBooks? Something else?"
2. "SEDNA — what data goes in, what comes out, and can it be accessed via API or export? Is it a SaaS platform or on-prem?"
3. "Financial system — what do you use for AR, AP, general ledger? Same as the ERP or separate?"
4. "Do you have a CRM? How do you track customer orders and pipeline?"
5. "Where does inventory data live? Warehouse management system? Spreadsheets? SEDNA?"
6. "If I needed to build a dashboard showing cash-to-cash cycle, could you give me AR aging, AP aging, and inventory levels by SKU? In what format? CSV export? API? Manual pull?"
7. "If I needed fill rate, do you have order data and shipment data? Where? Can they be joined?"
8. "If I needed DMSMS risk exposure, do you have parts data with manufacturer EOL dates? Or would we need to source that externally?"
9. "What's manual vs. automated? What's in someone's head vs. in a system? What's in a spreadsheet that should be in a system?"

**STOP Gate 3:** "So your data sources are [list systems]. The KPIs we can calculate from existing data right now are [list]. The KPIs that need new data collection or manual entry are [list]. Right?"

---

### Stage 4: The Gap — What's Costing You (10 min)
**Goal:** Surface the pain. What decisions are they making blind?
**Forcing Question:** Q4 (Narrowest Wedge)

**Questions:**
1. "If I gave you a magic wand and you could see one number in real-time that you can't see now, what would it be? Not a dashboard — one number that would change how you run the business this week."
2. "When was the last time you made a decision and realized later you were looking at the wrong data? What happened? What did it cost?"
3. "Obsolescence is a big deal in your world. What percentage of your inventory is at risk of DMSMS — parts going out of production? Do you know? If you don't know, how are you managing that risk today?"
4. "Aircraft-on-ground events — when a customer needs a part to keep a fleet flying. How do you track your response time? What's the cost of an AOG you can't fulfill — both the lost revenue and the relationship damage?"
5. "Defense supply chain means a few large customers. What's your customer concentration? If your top customer cut orders by 50% next quarter, how fast would you know — and what would give you advance warning?"

**STOP Gate 4:** "The three biggest gaps I'm hearing are: [list]. The one that costs you the most is [pick one]. Is that right? Or is there something else you're not telling me?"

---

### Stage 5: Strategic Priority (5 min)
**Goal:** What's the engagement type? Growth, optimization, or preparation?

**Questions:**
1. "Are you trying to grow, optimize, or prepare for something? Scale up, tighten margins, get ready for acquisition, win a new contract — what's the actual priority for the next 12 months?"
2. "If this engagement only does one thing for you, what would make you say 'that was worth every penny'? Not a list — one thing."
3. "You're a CFO. You've been at Deloitte, GE, Aquatrols. You know what good financial reporting looks like. What's the gap between what you have now and what you'd want if you were reporting to a board or preparing for an audit?"

**STOP Gate 5:** "So the priority is [pick one: growth/optimization/preparation]. The success metric for this engagement is [one thing]. Everything else is secondary. Agreed?"

---

### Stage 6: Future-Fit (5 min)
**Goal:** What happens when the world changes?
**Forcing Question:** Q6 (Future-Fit)

**Questions:**
1. "Defense procurement is shifting — reshoring, budget reallocation, CMMC compliance. Which of your current metrics will matter MORE in 3 years, and which will matter less?"
2. "If you doubled in size in 18 months — new contracts, new divisions, new people — what would break first? Your data, your processes, or your people?"

**STOP Gate 6:** "Here's what I've got: [full summary]. Here's what I think matters most: [the one thing]. Before I go design KPIs and OKRs, is there anything I'm missing? Anything you didn't say because you thought I wouldn't understand?"

---

## Post-Interview: Premise Challenge

After the interview, present these as falsifiable statements. Ryan must agree or disagree. Every accepted premise becomes load-bearing for the KPI/OKR design.

**PREMISES:**
1. "Your biggest gap is connecting SEDNA's supply chain insights to financial impact — you can see what's happening in the supply chain but not what it's doing to margin and cash flow." — Agree/Disagree?
2. "You're managing obsolescence risk reactively, not proactively — you find out a part is going out of production when a customer needs it, not before." — Agree/Disagree?
3. "Customer concentration is the #1 existential risk to the business, and you don't have a leading indicator that would tell you if a major customer is pulling back." — Agree/Disagree?
4. "At 20-30 people, your biggest constraint isn't data — it's decision speed. You need fewer, better metrics that you can act on daily, not a comprehensive dashboard that takes a week to digest." — Agree/Disagree?

---

## Post-Interview: KPI Feasibility Matrix — NEW

For each candidate KPI from the alternatives, score against 4 dimensions to determine implementability in Domo.

**Scoring:** 1 (no data / not accessible) to 5 (real-time API, clean, Domo-ready)

| KPI | Data Source | Format | Quality | Domo Connectable? | Feasibility Score | Effort |
|---|---|---|---|---|---|---|
| Cash-to-Cash Cycle | ? (AR + AP + Inventory from ERP?) | ? | ? | ? | ? / 20 | ? |
| Fill Rate | ? (Orders + Shipments from ERP?) | ? | ? | ? | ? / 20 | ? |
| Inventory Turnover | ? (Inventory from ERP?) | ? | ? | ? | ? / 20 | ? |
| Customer Concentration | ? (Revenue by customer from ERP/CRM?) | ? | ? | ? | ? / 20 | ? |
| DMSMS Risk Exposure | ? (Parts data + EOL dates — exists?) | ? | ? | ? | ? / 20 | ? |

**Interpretation:**
- **Score 16-20:** Ship immediately. Data exists, is accessible, and Domo can connect.
- **Score 11-15:** Ship with minor data work. May need a new connector, data cleaning, or manual export.
- **Score 6-10:** Needs data infrastructure work before KPI is measurable. Flag as Phase 2.
- **Score 1-5:** Aspirational. Data doesn't exist or isn't accessible. Flag as Phase 3 or drop.

**Output:** A prioritized implementation roadmap based on data feasibility, not just business priority. The KPIs with the highest feasibility scores go into Domo first — even if they're not the most strategically important — because they prove value quickly and build momentum.

---

## Post-Interview: Alternatives Generation

Based on the accepted premises, present 3 KPI/OKR approaches:

### Approach A: Minimal Viable (5 Core KPIs)
**Effort: S | Risk: Low**

Five KPIs on a single dashboard, reviewed weekly:
1. **Cash-to-Cash Cycle** — the A&D industry's most critical financial metric (up 60% industry-wide)
2. **Fill Rate** (perfect order fulfillment) — operational health
3. **Inventory Turnover** — inventory efficiency (the industry's biggest cost)
4. **Customer Concentration Index** — top customer revenue % + leading indicators of pullback
5. **DMSMS Risk Exposure** — % of inventory at obsolescence risk

**Pros:** Fast to implement. Forces prioritization. Ryan can act on these immediately.
**Cons:** Doesn't cover everything. May miss strategic metrics for growth.
**Reuses:** SEDNA data for #3 and #5. Existing financial data for #1 and #4.

### Approach B: Ideal Architecture (Full OKR Cascade)
**Effort: L | Risk: Medium**

OKR cascade from company → department → individual:
- **Company O:** "Achieve 95% fill rate while reducing cash-to-cash cycle by 15%"
  - **KR1:** Fill rate → 95% (from current baseline)
  - **KR2:** C2C cycle → reduced by 15%
  - **KR3:** DMSMS cost avoidance → $X (proactive vs. reactive)
  - **KR4:** Customer concentration → top customer < 40% of revenue
- **Department Os:** Operations (fill rate, AOG response), Finance (C2C, margin per contract), Sales (pipeline, backlog)
- **Individual KRs:** Each person has 2-3 metrics tied to their department's O

**Pros:** Comprehensive. Aligns everyone. Creates accountability.
**Cons:** Heavy. Takes time to implement. May be overkill for 20-30 people.
**Reuses:** SEDNA data for operational KRs. Financial system for finance KRs.

### Approach C: Creative/Lateral (Customer-Facing KPI Layer)
**Effort: M | Risk: Medium**

Don't track YOUR KPIs — track your CUSTOMERS' KPIs and become their data layer:
1. **Fleet Readiness Impact** — how many AOG events you resolved and average resolution time
2. **Cost Avoidance for Customer** — how much you saved them by proactively managing obsolescence
3. **Supply Chain Risk Score** — a composite score you give each customer showing their exposure
4. **Parts Availability Promise** — your fill rate commitment vs. actual, per customer

**Pros:** Makes Blue Raven indispensable. Turns data into a competitive advantage. Differentiates from every other distributor.
**Cons:** Requires more sophisticated data infrastructure. May be ahead of what Ryan needs. Shifts focus from internal management to customer-facing.
**Reuses:** SEDNA platform (already has supply chain intelligence). Just needs to be repackaged and presented differently.

---

## The Assignment

After the interview, the next step is NOT to build the dashboard. It's three concrete actions:

"Ryan, I need three things:

1. **A system list** — every system you use (ERP, inventory, financial, CRM, SEDNA, spreadsheets). For each, tell me: what data it holds, what format it exports, and whether it has an API.

2. **Sample data** — your last 3 months of data from whatever system holds your inventory and financials. Whatever format you have it in — CSV, Excel, PDF, doesn't matter.

3. **A 10-minute call with your operations person** — not you. The person who actually handles inventory and orders day-to-day. I need to ask them what data exists on the warehouse floor that doesn't make it to your desk.

I'll come back in 48 hours with two things:
- A **KPI Feasibility Matrix** showing which of the 5-10 KPIs we can measure right now from existing data vs. which need data work first
- A **mockup** of what your top 5 KPIs would look like in Domo, using your actual data

If you look at it and say 'I'd use this every day,' we talk about building it for real. If you say 'nice but not what I need,' we've wasted 48 hours, not 3 months."

---

## Methodology Notes

- **Forcing Questions Used:** Q2 (Status Quo), Q4 (Narrowest Wedge), Q6 (Future-Fit) — smart routing for a company with paying customers
- **STOP Gates:** 6 gates, one after each stage
- **Premise Challenge:** 4 falsifiable premises presented after interview
- **KPI Feasibility Matrix:** NEW — maps each candidate KPI to data source, scores feasibility, produces prioritized implementation roadmap
- **Alternatives Generation:** 3 approaches (minimal viable, ideal architecture, creative/lateral)
- **Industry Scaffolding:** A&D-specific KPIs from research (C2C, DMSMS, AOG, fill rate, customer concentration)
- **Wipfli Comparison:** Added Stage 3 (Data Source Mapping) and KPI Feasibility Matrix after comparing to Wipfli's Prime Growth System — specifically Component 7 (Technology Optimization and Alignment) and their "understand all existing data sources" methodology
- **Artifact Handoff:** This interview guide → KPI Feasibility Matrix → KPI/OKR design document → Domo dashboard mockup → implementation plan

## Wipfli Prime Growth System Comparison

### What This Guide Does That Wipfli Would Do
- Structured assessment with stages (Wipfli: Prime Rapid Assessment)
- Industry-specific knowledge (Wipfli: industry-specific assessment modules)
- Gap identification (Wipfli: "identify gaps, misalignments, opportunities")
- Executive conversation first (Wipfli: "starts with a conversation with your executive team")
- Roadmap/recommendations (Wipfli: "collaborate on a prime roadmap")
- Operational excellence focus (Wipfli: Component 5)
- Financial foundation focus (Wipfli: Component 6)
- Data source mapping (Wipfli: Component 7 — "understand all existing data sources")

### What This Guide Does NOT Do (By Design)
- **Leadership/People/Culture assessment** (Wipfli components 2-4): Not relevant for a KPI/OKR + Domo engagement. That's organizational development.
- **Benchmarking against industry peers:** Wipfli has 54K clients' worth of data. Directional benchmarks from research only.
- **Workshop facilitation:** Post-assessment phase. The interview comes first.
- **Multi-stakeholder interviews:** The Assignment requests a 10-minute call with the operations person, but the main interview is with the CFO. Wipfli would do 6+ executive interviews. This is a narrower engagement.

### Wipfli's Seven Components (for reference)
1. Compelling Vision and Plan → Stage 5 (Strategic Priority)
2. Transformational Leadership → Not covered (org development)
3. Engaged People → Not covered (org development)
4. Brand Messaging → Not covered (not relevant)
5. Operational Excellence → Stages 2, 4 (well covered)
6. Strong Financial Foundation → Stage 2, KPI selection (well covered)
7. Technology Optimization → Stage 3 (Data Source Mapping) — added after comparison
