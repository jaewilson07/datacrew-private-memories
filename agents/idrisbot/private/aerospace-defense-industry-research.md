# Aerospace & Defense Supply Chain Distribution — Industry Research

**Compiled:** 2026-07-18 | **By:** IdrisBot (industry-analysis skill v1) | **Method:** web_search across 10 source categories

---

## Industry Overview

Aerospace & defense supply chain distribution encompasses sourcing, distribution, obsolescence management (DMSMS), counterfeit avoidance, kitting, and logistics for government, defense, and commercial aviation customers. The industry is characterized by few large customers (high concentration), long lead times, strict regulatory compliance (ITAR, DFARS, CMMC), and significant working capital tied up in inventory.

- **US workforce:** 2.2M workers (AIA)
- **AI spending:** US A&D spending on AI/genAI expected to reach $5.8B by 2029, 3.5x 2025 levels (IDC via Deloitte)
- **Key segments:** Commercial aerospace OEMs, defense primes, Tier 1-3 suppliers, MRO, distributors, aftermarket services
- **Structure:** Consolidated at top (Boeing, Lockheed, Raytheon, Northrop, GD), fragmented at lower tiers. Distributors sit between OEMs/primes and end customers.

---

## Top 10 Problems

### 1. Excess inventory and working capital bloat
$75B in excess inventory across 59 A&D companies (AlixPartners, 2025). Inventory surged 44% ($90B) between 2018 and Q2 2025. At 6% financing cost, that's $4.5B/year in unnecessary interest. Middle-pack inventory turns dropped from 4-4.5x to 2.5-3.5x. Bottom quartile flat at ~1x.
*Source: AlixPartners "A&D has a $75 billion inventory problem" (Sep 2025)*

### 2. DMSMS / obsolescence management
Diminishing Manufacturing Sources and Material Shortages (DMSMS) is a chronic cost driver. Parts go out of production with little warning. DoD mandates DMSMS programs (DoDM 4140.01 Vol 3) but many distributors manage reactively, not proactively. Cost avoidance from proactive DMSMS management can be significant.
*Source: DoD Manual 4140.01 Vol 3, Section 9*

### 3. Supply chain fragility and disruption
64% of aerospace companies still facing supply chain disruptions (Roland Berger, 2025). Main causes: increased lead times, limited availability of raw materials and semi-finished goods. Very severe disruptions declining but concentrated at Tier-1 and Tier-3+ levels. Industry not expected to fully recover until 2026-2027.
*Source: Roland Berger "Aerospace supply chain report 2025" (Jul 2025)*

### 4. Customer concentration risk
A&D distributors typically have few large customers (defense primes, government agencies). Revenue concentration creates existential risk if a major customer cuts orders. Most distributors lack leading indicators that would warn of customer pullback before it hits the P&L.
*Source: Industry structural characteristic; Deloitte 2026 A&D Outlook*

### 5. Counterfeit parts and quality assurance
DoD mandates anti-counterfeiting programs (DoDI 4140.67, DoDM 4140.01 Vol 3 Section 5.3). Distributors must establish risk-based procedures to identify critical materiel susceptible to counterfeiting, certify authenticity of non-OEM-sourced items, and report all occurrences to GIDEP. Annual evaluation required.
*Source: DoD Manual 4140.01 Vol 3, Section 5.3*

### 6. Talent and workforce shortages
65% of aerospace companies cite personnel shortages as top challenge (Roland Berger, 2025). Skills gap widening as technological advancement outpaces workforce development. Demand shifting from general programming to multidisciplinary AI/data skills. Middle management skeptical of AI transformation.
*Source: Roland Berger 2025; Deloitte 2026 A&D Outlook*

### 7. Cash-to-cash cycle deterioration
C2C cycles have increased significantly (industry-wide trend). Working capital tied up in inventory means cash unavailable for operations, investment, or shareholder returns. Faster C2C cycle = fewer days cash is unavailable. APQC benchmarks C2C as a KPI in supply chain planning assessments.
*Source: APQC OSB (Measure ID 100395); AlixPartners inventory data*

### 8. Demand signal uncertainty and whipsaw
OEMs issue demand signals to suppliers, then replans when working capital balloons. Suppliers second-guess OEM demand, delay raw material orders, creating new bottlenecks and worsening whipsaw. Result: delayed ramp-ups, excess inventory, and clouded demand signals.
*Source: AlixPartners (Sep 2025)*

### 9. Regulatory compliance burden (ITAR, DFARS, CMMC, export controls)
Defense distributors face ITAR, DFARS, CMMC, and ongoing acquisition reforms. FY2026 NDAA made changes to reduce bureaucracy but compliance remains costly. AIA advocating for further acquisition reform in FY2027 NDAA.
*Source: AIA 2026 Legislative Priorities (Feb 2026); Deloitte 2026 A&D Outlook*

### 10. Lack of supply chain visibility across tiers
Companies struggle to see beyond Tier-1 suppliers. Best practices include supplier watchtowers, multi-tier visibility, and digital integration. 65% of aerospace companies use or plan to use AI but adoption limited to <10% of business processes. Main barriers: lack of experience (61%) and integration problems (53%).
*Source: Roland Berger 2025; Deloitte 2026 A&D Outlook*

---

## Key KPIs

### Cash-to-Cash (C2C) Cycle Time
- **SCOR ref:** AM.1.1 | **APQC ID:** 100395
- **Category:** Financial | **Priority:** Critical | **Type:** Lagging
- **Definition:** Number of days of working capital tied up in managing the supply chain. C2C = Days Inventory Outstanding + Days Sales Outstanding - Days Payable Outstanding.
- **Benchmark:** Industry trend: rising 60% over past decade. APQC benchmarks available (members-only).
- **Data source:** ERP (AR aging, AP aging, inventory levels)

### Inventory Turnover Ratio
- **SCOR ref:** AM | **APQC ID:** 103482, 100719
- **Category:** Inventory | **Priority:** Critical | **Type:** Lagging
- **Definition:** Cost of Goods Sold / Average Inventory.
- **Benchmarks:**
  - Industry median (2025): 2.5-3.5x (down from 4-4.5x in 2018-2020)
  - Top quartile: >4.1x (was >5.2x pre-crisis)
  - Bottom quartile: ~1x
  - Trend: Declining significantly. 30%+ drops for airframers, engine manufacturers, complex-systems suppliers.
- **Data source:** ERP (COGS, inventory levels)
- *Source: AlixPartners (Sep 2025)*

### Perfect Order Fulfillment
- **SCOR ref:** RL.1.1 | **APQC ID:** 101741
- **Category:** Operational | **Priority:** High | **Type:** Lagging
- **Definition:** Percentage of orders delivered on-time, in full, in correct condition, with correct documentation, to correct customer. SCOR Level 1 reliability metric.
- **Benchmark:** APQC benchmarks available (members-only). SCOR tiers: Superior (90th percentile), Advantage (midpoint), Parity (median).
- **Data source:** ERP (order data, shipment data, quality records)

### Order Fill Rate
- **SCOR ref:** RL | **APQC ID:** 101445
- **Category:** Operational | **Priority:** High | **Type:** Lagging
- **Definition:** Number of sales orders filled completely as a percentage of total sales orders.
- **Benchmark:** Cross-industry median: 94.0% (APQC OSB, n=3,218)
- **Data source:** ERP (order fulfillment data)
- *Source: APQC OSB (Measure ID 101445)*

### DMSMS Risk Exposure
- **Category:** Risk | **Priority:** Critical | **Type:** Leading
- **Definition:** Percentage of inventory at risk of obsolescence due to diminishing manufacturing sources and material shortages.
- **Benchmark:** No standardized benchmark. DoD requires DMSMS programs but doesn't publish industry-wide risk exposure data.
- **Data source:** Parts database with manufacturer EOL dates, SEDNA or equivalent supply chain intelligence platform
- *Source: DoD Manual 4140.01 Vol 3, Section 9*

### Customer Concentration Index
- **Category:** Strategic Risk | **Priority:** High | **Type:** Lagging (but can construct leading indicators)
- **Definition:** Percentage of revenue from top customer(s). High concentration = existential risk. Should include leading indicators of customer pullback (order velocity, contract modifications).
- **Benchmark:** No standardized benchmark. Structural characteristic of A&D distribution.
- **Data source:** ERP/CRM (revenue by customer, order history)

### Forecast Accuracy (MAPE)
- **APQC ID:** 100207 (national), 100210 (product family), 100215 (shipping location)
- **Category:** Planning | **Priority:** High | **Type:** Leading
- **Definition:** Mean Absolute Percentage Error of demand forecast.
- **Benchmark:** APQC benchmarks available (members-only). Critical for A&D where demand whipsaw is a major problem.
- **Data source:** Demand planning system, SEDNA or equivalent

### AOG (Aircraft on Ground) Resolution Time
- **Category:** Operational | **Priority:** High | **Type:** Lagging
- **Definition:** Average time to resolve an AOG event (when an aircraft is grounded waiting for parts). Critical urgency metric in aviation.
- **Benchmark:** No standardized industry benchmark. AOG events are high-cost, high-urgency.
- **Data source:** ERP (order timestamps for AOG-flagged orders), customer feedback

### Days Sales Outstanding (DSO)
- **SCOR ref:** AM | **APQC ID:** 100178
- **Category:** Financial | **Priority:** Medium | **Type:** Lagging
- **Definition:** Average days to collect payment after sale. Component of C2C cycle.
- **Benchmark:** APQC benchmarks available (members-only).
- **Data source:** ERP (AR aging)

### Cost of Goods Sold as % of Revenue
- **SCOR ref:** CO.1.2 | **APQC ID:** 100433
- **Category:** Financial | **Priority:** Medium | **Type:** Lagging
- **Definition:** COGS / Revenue × 100. Direct cost efficiency measure.
- **Benchmark:** APQC benchmarks available (members-only).
- **Data source:** ERP (financial data)

### Customer Retention Rate
- **APQC ID:** 104302
- **Category:** Strategic | **Priority:** Medium | **Type:** Lagging
- **Definition:** Customer retention rate over the past three reporting periods. Critical in A&D where customer relationships are long-term and high-value.
- **Benchmark:** APQC benchmarks available (members-only).
- **Data source:** CRM (customer relationship data)

---

## Industry Trends

### 1. Supply chain crisis stabilizing but not resolved
Roland Berger 2025 survey finds disruption severity decreasing and resilience increasing. 70% of companies now feel well-prepared for ramp-up (vs 50% in 2024). But 64% still facing disruptions. Full recovery not expected until 2026.
*Source: Roland Berger (Jul 2025)*
**Implication:** Window opening for distributors who can demonstrate reliability. Those still struggling will lose share to those who have stabilized.

### 2. Destocking pressure on weaker suppliers
$75B in excess inventory is driving destocking. This threatens weaker suppliers, especially in aerostructures. Prolonged production at lower rates compounds stress. Distributors with lean inventory and strong turnover will gain advantage.
*Source: AlixPartners (Sep 2025)*
**Implication:** Distributors must demonstrate inventory efficiency. Being able to show clients "your inventory turns are X vs industry median 3.2x" is a powerful sales tool.

### 3. AI adoption accelerating but uneven
65% of aerospace companies use or plan to use AI (Roland Berger). US A&D AI spending expected to reach $5.8B by 2029, 3.5x 2025 levels (IDC). But adoption limited to <10% of business processes. Barriers: lack of experience (61%), integration problems (53%). Agentic AI moving from pilot to scaled deployment in 2026.
*Source: Roland Berger 2025; Deloitte 2026 A&D Outlook*
**Implication:** AI-powered supply chain intelligence (like SEDNA) is a differentiator. But most companies are early in adoption. Distributors who can show AI-driven insights have a competitive edge.

### 4. Defense acquisition reform accelerating
FY2026 NDAA reduced bureaucracy and accelerated contracting. New Executive Order "Prioritizing the Warfighter in Defense Contracting" (Jan 2026). AIA pushing for further reform in FY2027 NDAA. OTA and commercial solutions pathways expanding access for nontraditional suppliers. "Speed to field" becoming unifying metric.
*Source: AIA (Feb 2026); Deloitte 2026 A&D Outlook*
**Implication:** Faster procurement cycles mean faster revenue recognition but also faster competitive displacement. Distributors need to be ready to respond to compressed timelines.

### 5. Aftermarket services growth
Global commercial aftermarket MRO demand growing at 3.2% CAGR (2026-2035). Engine segment share rising to 53% of total MRO demand. OEMs expanding service capabilities, targeting 40-50% capacity expansions. Legacy fleets in service longer.
*Source: Deloitte 2026 A&D Outlook (Aviation Week data)*
**Implication:** Aftermarket = recurring revenue for parts distributors. Longer fleet life means sustained demand for obsolete/hard-to-find parts. DMSMS management becomes more valuable.

### 6. Financing constraints emerging as growing concern
49% of aerospace companies cite lack of financial resources as a challenge (up from 41% in 2024). Despite improved operational readiness, financial constraints could threaten sustaining or accelerating ramp-up.
*Source: Roland Berger 2025*
**Implication:** CFOs are under pressure to optimize working capital. This is the entry point for KPI/OKR consulting — "let me show you where your cash is trapped and how to free it."

### 7. Reshoring and supply chain consolidation
US A&D companies pursuing supply chain consolidation (centralizing storage and sourcing domestically). International customers encouraging diversification. Vertical integration, expanded local footprints, multicountry manufacturing, long-dated supply contracts. Counterfeit parts and compliance driving digital visibility investments.
*Source: Deloitte 2026 A&D Outlook*
**Implication:** Domestic sourcing = opportunity for US-based distributors. But also means OEMs may bypass distributors and source directly. Value-add must be in intelligence, not just logistics.

### 8. Workforce transformation — from big data to multidisciplinary
Data analysis skills in A&D job postings projected to increase from 9% (2025) to 14% (2028). Data science from 3% to 5%. Shift from narrow expertise to integrated, multidisciplinary skill sets. Middle management resistant to AI adoption.
*Source: Deloitte 2026 A&D Outlook*
**Implication:** Small distributors (20-30 people) can't hire dedicated data scientists. But they can use AI tools and external consultants to get data capabilities without full-time hires.

---

## Benchmark Sources

### AlixPartners — Use Now (Free)
- **URL:** https://www.alixpartners.com/insights/102l6b8/ad-has-a-75-billion-inventory-problem/
- **Data:** A&D-specific inventory turnover benchmarks (median 3.2x → 2.5-3.5x, top quartile 4.1x, bottom ~1x). $75B excess inventory. $4.5B/year in interest costs. Quarterly manufacturing overview with A&D inventory turnover trends.
- **Notes:** Best free source for A&D-specific operational benchmarks. Uses S&P Capital IQ data from public filings of 59 A&D companies.

### APQC Open Standards Benchmarking (OSB) — Membership Required
- **URL:** https://www.apqc.org/osb
- **Data:** Cash-to-cash cycle time (ID 100395), Order fill rate (ID 101445, median 94.0%), Perfect order performance (ID 101741), Inventory turns (ID 103482, 100719), Forecast accuracy/MAPE (ID 100207), Customer retention (ID 104302), DSO (ID 100178), Days payable (ID 100642). Peer comparison by industry, region, company size. 2-week turnaround.
- **Notes:** Long-term play for competing with Wipfli's benchmarking. Submit client data, get peer comparison. Closest to Wipfli's 54K-client database. 61 measures in supply chain planning survey.

### SCOR Model (ASCM v14.0) — Use Now (Free with ASCM login)
- **URL:** https://scor.ascm.org
- **Data:** Standardized metric hierarchy: Level 1 (strategic) → Level 2 (diagnostic) → Level 3 (operational). 8 performance attributes: Reliability (RL), Responsiveness (RS), Agility (AG), Cost (CO), Profit (PR), Assets (AM), Environmental (EV), Social (SC). Key Level 1 metrics: Perfect Order Fulfillment (RL.1.1), Order Fulfillment Cycle Time (RS.1.1), Cash-to-Cash Cycle Time (AM.1.1), Return on Working Capital (AM.1.3).
- **Notes:** Use for metric framework credibility and standardized definitions. Performance tiers: Superior (90th percentile), Advantage (midpoint), Parity (median). v14.0 updated in 2025.

### Deloitte 2026 A&D Industry Outlook — Use Now (Free)
- **URL:** https://www.deloitte.com/us/en/insights/industry/aerospace-defense/aerospace-and-defense-industry-outlook.html
- **Data:** 5 trends: AI/agentic AI, aftermarket MRO, supply chain resilience, contracting/procurement reform, workforce transformation. A&D AI spending forecast ($5.8B by 2029). MRO demand CAGR (3.2%). Data analysis skills growth (9%→14% by 2028).
- **Notes:** Best free source for strategic trends and industry direction. Annual publication.

### Roland Berger Aerospace Supply Chain Report 2025 — Use Now (Free)
- **URL:** https://www.rolandberger.com/en/Insights/Publications/Aerospace-supply-chain-report-2025-Is-the-crisis-over.html
- **Data:** Survey of dozens of aerospace companies across UK, Germany, France. Ramp-up readiness (70% well-prepared), personnel shortages (65%), financing concerns (49%, up from 41%), disruption prevalence (64%), AI adoption (65%, limited to <10% of processes).
- **Notes:** Best source for European aerospace supply chain sentiment. Annual survey since 2023.

### Kearney — Evolution of Supply Chain Metrics in A&D — Use Now (Free)
- **URL:** https://www.kearney.com/industry/aerospace-defense/article/the-evolution-of-supply-chain-metrics-in-aerospace-and-defense
- **Data:** Framework for A&D supply chain metrics evolution: on-time delivery, schedule adherence, lead times, inventory metrics, operational throughput, quality/reliability, cash/cost metrics, risk/resilience indicators, digital/predictive metrics.
- **Notes:** Good for framing the KPI conversation with clients.

### AIA (Aerospace Industries Association) — Use Now (Free)
- **URL:** https://www.aia-aerospace.org
- **Data:** 2026 legislative priorities: stable funding, defense acquisition reform, commercial aviation safety, space capabilities, defense trade modernization. Industry size: 2.2M US workers, 300+ member companies.
- **Notes:** Use for industry context and regulatory landscape. Not a source of operational benchmarks.

### DoD Manual 4140.01 Volume 3 — Use Now (Free, Public)
- **URL:** https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/414001_vol3.PDF
- **Data:** DMSMS requirements (Section 9), materiel sourcing strategies, counterfeit materiel prevention (Section 5.3), quality programs (Section 8), supplier performance metrics. Updated Jul 2025 (Change 2).
- **Notes:** Regulatory authority for DMSMS and counterfeit avoidance.

### Gartner — Not Useful (Paid, Not A&D-Specific)
- **Notes:** Has a dynamic supply chain benchmarking database covering 7 core process areas. Can filter by industry segment (industrial, consumer, life sciences) but A&D not a specific filter. Paid consulting service, not a data product.

### Dresner Advisory Services — Not Useful (Wrong Focus)
- **Notes:** Benchmarks BI tool usage and adoption, not operational KPIs like inventory turnover or fill rate. About the BI market, not supply chain performance.

---

## Forcing Questions for Discovery Interviews

1. What's your cash-to-cash cycle time right now? If you don't know, what's the closest approximation — how many days of inventory do you carry, how long does it take customers to pay, how long do you take to pay suppliers?
2. What percentage of your inventory is at risk of DMSMS? If you don't know, how are you managing that risk today — reactively or proactively?
3. If your top customer cut orders by 50% next quarter, how fast would you know — and what would give you advance warning?
4. When was the last time you made a decision and realized later you were looking at the wrong data? What did it cost?
5. What's the one report you pull every week that you immediately regret spending time on?
6. If I gave you a magic wand and you could see one number in real-time that you can't see now, what would it be?

---

## Data Source Mapping Template

**Systems to identify:** ERP (NetSuite, SAP, Dynamics, QuickBooks), Inventory management system, Financial system (AR, AP, GL), CRM, Supply chain intelligence platform (e.g., SEDNA), Warehouse management system, Spreadsheets

**Questions per system:**
- What data does it hold?
- What format does it export?
- Does it have an API?
- Is the data manual or automated?
- What's the data quality (latency, completeness, accuracy)?
- Can Domo connect to it (native connector, API, file export, manual upload)?

---

## KPI Feasibility Matrix Template

Score each candidate KPI against 4 dimensions (1=none, 5=real-time API, clean, Domo-ready):

| KPI | Data Source Available? | Format | Quality | Domo Connectable? | Effort |
|---|---|---|---|---|---|
| Cash-to-Cash Cycle | ? | ? | ? | ? | ? |
| Fill Rate | ? | ? | ? | ? | ? |
| Inventory Turnover | ? | ? | ? | ? | ? |
| Customer Concentration | ? | ? | ? | ? | ? |
| DMSMS Risk Exposure | ? | ? | ? | ? | ? |
| AOG Resolution Time | ? | ? | ? | ? | ? |
| Forecast Accuracy | ? | ? | ? | ? | ? |

This matrix is the bridge between the interview and Domo implementation. It tells us:
- Which KPIs we can ship immediately (score 4-5)
- Which KPIs need data work first (score 2-3)
- Which KPIs are aspirational (score 1)
- The order to implement (highest feasibility first)
