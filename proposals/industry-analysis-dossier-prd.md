# PRD: Industry Analysis Extension for Customer Dossier Workflow

**Status:** Draft
**Author:** IdrisBot (Build Partner)
**Created:** 2026-07-17
**Related:** `outreach-create-dossier` skill, `mdrag` library, AI CoS product architecture

---

## Problem

The current customer dossier workflow (`06_research_company.py` → `07_create_dossier.py`) researches a **company** across Slack, Vanilla Forums, and LinkedIn. It produces a Google Doc with 4 tabs: Overview, People, Org Chart, Outreach Strategy.

What's missing: **industry context**. The dossier tells you who the company is and who works there, but not what their industry looks like — KPI benchmarks, market trends, competitive landscape, operational norms. For the AI CoS consulting practice, this industry context is what makes the KPI/OKR setup pitch credible. "Your inventory turnover is 3.2x; industry median is 3.2x" requires knowing the industry benchmarks before the first call.

**The gap:** When Jae walks into a discovery interview, he needs to already know:
- What KPIs matter for this industry
- What the benchmarks are (median, top quartile, bottom quartile)
- What the industry trends are (which direction are things moving)
- What the top 10 problems are for companies like this
- What data sources exist for this industry

Currently, this research is done manually and ad-hoc. It should be systematized into the dossier pipeline.

## Goal

Extend the customer dossier workflow to produce a 5th tab — **Industry Analysis** — that aggregates industry-specific research from multiple sources, summarizes it using mdrag, and renders it alongside the existing company/people/org-chart tabs.

## Architecture

### Current Flow

```
06_research_company.py
  ├── Slack search (members, conversations)
  ├── Vanilla Forums search (CSV lookup)
  ├── LinkedIn search (via Exa API)
  ├── Persona builder (merge sources → personas)
  └── Synthesis (letta LLM fills bio fields)
      → research.json
          → 07_create_dossier.py (Google Doc with 4 tabs)
          → 09_sync_contacts.py (Google Contacts)
```

### Proposed Flow

```
06_research_company.py
  ├── [existing] Slack search
  ├── [existing] Vanilla Forums search
  ├── [existing] LinkedIn search
  ├── [existing] Persona builder
  └── [existing] Synthesis
      → research.json

06b_research_industry.py  ← NEW
  ├── Industry classification (from research.json industry field or manual override)
  ├── mdrag industry research pipeline:
  │   ├── SearXNG search (industry KPIs, benchmarks, trends)
  │   ├── Source-specific collectors (adaptors):
  │   │   ├── AlixPartners (public A&D benchmarks)
  │   │   ├── McKinsey (public industry reports)
  │   │   ├── APQC OSB (membership-gated benchmark data)
  │   │   ├── SCOR/ASCM (framework metrics)
  │   │   └── [future] industry-specific sources
  │   ├── crawl4ai scrape (for report pages)
  │   └── mdrag ingest (→ knowledge base for RAG)
  ├── mdrag summarization:
  │   ├── Query KB for industry KPIs, benchmarks, trends
  │   └── LLM synthesis → structured industry analysis
  └── → industry_research.json
      → 07_create_dossier.py (Google Doc with 5 tabs — new Industry Analysis tab)
```

### Component Breakdown

#### 1. Industry Classification (trivial)

Reads `research.json` → `industry` field. Maps to a canonical industry key:
- `aerospace-defense-supply-chain` → A&D adaptor set
- `construction` → construction adaptor set (future)
- `financial-services` → financial services adaptor set (future)
- `generic` → fallback to SearXNG-only research

If the industry field is empty or ambiguous, accept a `--industry` override flag.

#### 2. mdrag Industry Research Adaptors

Each adaptor implements the mdrag `SourceCollector` protocol:

```python
class IndustryResearchCollector(Protocol):
    """Collects industry-specific benchmark and trend data."""
    industry: str
    async def collect(self, request: IndustryResearchRequest) -> list[CollectedSource]:
        ...
```

**Adaptor: SearXNG Industry Search (baseline, always runs)**
- Source: `SearXNGClient` (already in mdrag)
- Queries: Configurable per industry. For A&D:
  - `"{industry} KPI benchmarks inventory turnover"`
  - `"{industry} supply chain metrics perfect order fulfillment"`
  - `"{industry} cash-to-cash cycle industry trends"`
  - `"{industry} top supply chain problems 2025"`
- Output: URLs → crawl4ai → markdown content → mdrag ingest

**Adaptor: AlixPartners (public, A&D-specific)**
- Source: `https://www.alixpartners.com/insights/`
- Method: SearXNG search scoped to `site:alixpartners.com` + industry keywords
- Collects: Published reports with actual benchmark numbers (inventory turnover quartiles, excess inventory)
- No auth required. Static HTML pages.

**Adaptor: McKinsey (public, cross-industry)**
- Source: `https://www.mckinsey.com/industries/`
- Method: SearXNG search scoped to `site:mckinsey.com` + industry keywords
- Collects: Industry reports, trend analyses, operational benchmark articles
- No auth required. Content behind soft paywall (free registration for full text).

**Adaptor: APQC OSB (membership-gated, future)**
- Source: `https://www.apqc.org/resources/benchmarking/open-standards-benchmarking`
- Method: API or form submission (requires membership)
- Collects: Validated peer comparison data — the gold standard
- **Phase 2**: Implement after APQC membership is secured. For now, reference the measure list URL as a data source.

**Adaptor: SCOR/ASCM (public framework, cross-industry)**
- Source: SCOR model documentation, ASCM articles
- Method: SearXNG search for SCOR metrics + industry
- Collects: Standardized metric definitions, performance tier definitions (Superior/Advantage/Parity)
- Provides the framework vocabulary even without benchmark database access.

**Industry Adaptor Registry**

```python
INDUSTRY_ADAPTORS = {
    "aerospace-defense-supply-chain": [
        SearXNGIndustryCollector,
        AlixPartnersCollector,
        McKinseyIndustryCollector,
        SCORFrameworkCollector,
    ],
    # Future industries:
    # "construction": [...],
    # "financial-services": [...],
    # "generic": [SearXNGIndustryCollector],
}
```

Each adaptor returns `list[CollectedSource]` — the same mdrag ingestion model used by existing collectors. This means all industry research content flows through the same pipeline: collect → process → store → searchable in KB.

#### 3. mdrag Summarization & Research Aggregation

After collection + ingestion, query the mdrag knowledge base to synthesize the industry analysis:

```python
# Query the KB for industry-specific content
results = await mdrag.query_rag(
    query=f"{industry} KPI benchmarks inventory turnover cash-to-cash cycle",
    source_group=f"industry-research/{industry}",
    limit=20,
)

# LLM synthesis → structured industry analysis
analysis = await synthesize_industry_analysis(
    industry=industry,
    company=company_name,
    kb_results=results,
    company_research=research_json,  # the company's own data for comparison
)
```

**Output structure (`industry_research.json`):**

```json
{
  "industry": "aerospace-defense-supply-chain",
  "company": "Blue Raven Solutions",
  "researched_at": "2026-07-17T...",
  "industry_overview": "A&D supply chain distribution...",
  "top_10_problems": [
    {"problem": "DMSMS/obsolescence management", "severity": "high", "description": "..."},
    ...
  ],
  "key_kpis": [
    {
      "name": "Inventory Turnover",
      "definition": "COGS / average inventory",
      "industry_median": "3.2x",
      "top_quartile": ">4.1x",
      "bottom_quartile": "~2.3x",
      "source": "AlixPartners 2022 A&D Inventory Study",
      "source_url": "https://www.alixpartners.com/insights/...",
      "trend": "declining"
    },
    {
      "name": "Cash-to-Cash Cycle",
      "definition": "Days inventory + Days receivables - Days payables",
      "industry_trend": "+60% over 2000-2012",
      "source": "Kinaxis / Supply Chain Insights",
      "trend": "increasing"
    },
    ...
  ],
  "benchmark_sources": [
    {"name": "AlixPartners", "type": "public", "url": "...", "notes": "A&D-specific quartile benchmarks"},
    {"name": "APQC OSB", "type": "membership", "url": "...", "notes": "Closest to Wipfli's 54K-client benchmarking"},
    {"name": "SCOR Model", "type": "framework", "url": "...", "notes": "Standardized metric definitions"}
  ],
  "industry_trends": [
    {"trend": "Reshoring and budget reallocation", "description": "...", "impact": "high"},
    {"trend": "CMMC compliance requirements", "description": "...", "impact": "medium"},
    ...
  ],
  "source_urls": ["https://...", ...]
}
```

#### 4. Dossier Tab: Industry Analysis

New tab renderer: `dossier/tabs/industry_analysis.py`

```python
class IndustryAnalysisTab:
    title = "Industry Analysis"

    def render(self, industry_research: IndustryResearch) -> str:
        # Sections:
        # 1. Industry Overview (1-2 paragraph summary)
        # 2. Top 10 Problems (table: problem, severity, description)
        # 3. Key KPIs & Benchmarks (table: KPI, definition, median, top quartile, trend, source)
        # 4. Benchmark Sources (table: source, type, url, notes)
        # 5. Industry Trends (table: trend, description, impact)
        # 6. Sources (list of URLs)
```

#### 5. Pipeline Integration

**`06b_research_industry.py`** — new script:

```bash
# Standalone (after 06_research_company.py has run)
PYTHONPATH=$SCRIPTS .venv/bin/python3 $SCRIPTS/research/06b_research_industry.py \
  --company "Blue Raven Solutions" \
  --from-research data/EXPORTS/research/blue-raven-solutions/research.json

# With industry override
PYTHONPATH=$SCRIPTS .venv/bin/python3 $SCRIPTS/research/06b_research_industry.py \
  --company "Blue Raven Solutions" \
  --industry "aerospace-defense-supply-chain"
```

**`07_create_dossier.py`** — updated to accept `--from-industry-research` flag:

```bash
PYTHONPATH=$SCRIPTS .venv/bin/python3 $SCRIPTS/output/07_create_dossier.py \
  --company "Blue Raven Solutions" \
  --from-research data/EXPORTS/research/blue-raven-solutions/research.json \
  --from-industry-research data/EXPORTS/research/blue-raven-solutions/industry_research.json
```

Tab order: Overview → People → Org Chart → **Industry Analysis** → Outreach Strategy

The Industry Analysis tab positions the outreach strategy. The Outreach Strategy tab now has industry context to draw on — the talking points can reference benchmarks and KPIs.

**`outreach-create-dossier` SKILL.md** — updated to include Step 2b (industry research between research and dossier creation).

## Implementation Phases

### Phase 1: SearXNG + Manual Industry Research (Ship in 1-2 days)

- [ ] `06b_research_industry.py` script
- [ ] SearXNG industry search adaptor (using existing `SearXNGClient`)
- [ ] Industry search query templates (per-industry YAML config)
- [ ] LLM synthesis → `industry_research.json`
- [ ] `IndustryAnalysisTab` renderer
- [ ] Update `07_create_dossier.py` to accept `--from-industry-research`
- [ ] Update `outreach-create-dossier` SKILL.md

Deliverable: Industry Analysis tab in the Google Doc dossier, populated via SearXNG search + LLM synthesis. No new mdrag adaptors needed — uses existing SearXNG + crawl4ai + mdrag ingest pipeline.

### Phase 2: Source-Specific Adaptors (Ship in 1-2 weeks)

- [ ] `AlixPartnersCollector` — SearXNG-scoped to alixpartners.com
- [ ] `McKinseyIndustryCollector` — SearXNG-scoped to mckinsey.com
- [ ] `SCORFrameworkCollector` — SearXNG-scoped to SCOR/ASCM content
- [ ] Industry adaptor registry — maps industry → collector set
- [ ] mdrag ingestion of all collector output → KB searchable
- [ ] mdrag RAG query for synthesis (replace direct LLM synthesis with KB-grounded synthesis)

Deliverable: Structured benchmark data from specific sources, ingested into mdrag KB, queryable for synthesis.

### Phase 3: APQC Integration (When membership is secured)

- [ ] `APQCCollector` — authenticated API/form submission
- [ ] Peer comparison data ingestion
- [ ] Benchmark comparison table in Industry Analysis tab

Deliverable: Validated peer comparison data — the Wipfli-competing benchmark layer.

## Data Model

### New: `IndustryResearch` dataclass

Lives in `outreach/models/industry_research.py` (shared outreach library):

```python
@dataclass
class IndustryKPI:
    name: str
    definition: str
    industry_median: str = ""
    top_quartile: str = ""
    bottom_quartile: str = ""
    trend: str = ""  # "increasing", "declining", "stable"
    source: str = ""
    source_url: str = ""

@dataclass
class IndustryProblem:
    problem: str
    severity: str = ""  # "high", "medium", "low"
    description: str = ""

@dataclass
class IndustryTrend:
    trend: str
    description: str = ""
    impact: str = ""  # "high", "medium", "low"

@dataclass
class BenchmarkSource:
    name: str
    type: str = ""  # "public", "membership", "framework"
    url: str = ""
    notes: str = ""

@dataclass
class IndustryResearch:
    industry: str
    company: str = ""
    researched_at: str = ""
    industry_overview: str = ""
    top_10_problems: list[IndustryProblem] = field(default_factory=list)
    key_kpis: list[IndustryKPI] = field(default_factory=list)
    benchmark_sources: list[BenchmarkSource] = field(default_factory=list)
    industry_trends: list[IndustryTrend] = field(default_factory=list)
    source_urls: list[str] = field(default_factory=list)

    @classmethod
    def from_json(cls, path: Path) -> IndustryResearch: ...
    def to_json(self, path: Path) -> None: ...
```

### Updated: `CompanyResearch` — no changes

The `CompanyResearch` dataclass stays as-is. `IndustryResearch` is a separate record that runs alongside it.

### Updated: `07_create_dossier.py` — accept `--from-industry-research`

The dossier creator reads both `research.json` (company) and `industry_research.json` (industry) and renders 5 tabs instead of 4.

## Industry Query Templates

Per-industry YAML config at `data/industry-queries/{industry_slug}.yaml`:

```yaml
# aerospace-defense-supply-chain.yaml
industry: "aerospace defense supply chain"
queries:
  - "{industry} KPI benchmarks inventory turnover"
  - "{industry} supply chain metrics perfect order fulfillment"
  - "{industry} cash-to-cash cycle industry trends"
  - "{industry} DMSMS obsolescence management cost"
  - "{industry} fill rate aircraft on ground AOG"
  - "{industry} customer concentration risk defense"
  - "{industry} top 10 supply chain problems 2025"
  - "{industry} industry trends reshoring CMMC"
preferred_sources:
  - domain: "alixpartners.com"
    queries:
      - "aerospace defense inventory turnover benchmark"
      - "A&D excess inventory $75 billion"
  - domain: "mckinsey.com"
    queries:
      - "aerospace defense supply chain management cash is king"
      - "aerospace defense inventory reduction"
  - domain: "apqc.org"
    queries:
      - "supply chain planning benchmarks"
      - "open standards benchmarking defense"
  - domain: "scor.ascm.org"
    queries:
      - "SCOR model perfect order fulfillment"
      - "SCOR metrics defense supply chain"
synthesis_prompt: |
  You are an industry analyst. Given the following research on {industry},
  produce a structured analysis for a company called {company}.

  Extract:
  1. Industry overview (2-3 paragraphs)
  2. Top 10 problems for companies in this industry
  3. Key KPIs with benchmarks (median, top quartile, bottom quartile) where available
  4. Industry trends (next 3 years)
  5. Benchmark sources used

  Format each KPI with: name, definition, industry_median, top_quartile,
  bottom_quartile, trend, source, source_url.

  Be specific. Use actual numbers from the research. If a benchmark isn't
  available, say "not available" — don't make up numbers.
```

## mdrag Integration Points

### Ingestion (Collection → KB)

All industry research content flows through mdrag's existing ingestion pipeline:

```python
# After each collector runs
for source in collected_sources:
    await mdrag.ingest_collector(
        collector=source,
        request=IngestRequest(
            source_group=f"industry-research/{industry}",
            source_type="web",
        ),
    )
```

This makes all industry research searchable in the mdrag KB for:
- Future dossier runs (don't re-research the same industry)
- RAG-grounded synthesis (query KB instead of raw LLM)
- Cross-company analysis (multiple companies in the same industry)

### Retrieval (KB → Synthesis)

```python
# Query KB for industry-specific content
results = await mdrag.query_rag(
    query=f"{industry} KPI benchmarks inventory turnover cash-to-cash cycle",
    source_group=f"industry-research/{industry}",
    limit=20,
)

# Use KB results as context for LLM synthesis
analysis = await synthesize_industry_analysis(
    industry=industry,
    company=company,
    kb_results=results,
    synthesis_prompt=template.synthesis_prompt,
)
```

### Deduplication

If `industry_research.json` already exists for a given industry (e.g., we already researched A&D supply chain for Blue Raven Solutions), a subsequent run for another A&D company should:
1. Skip re-crawling shared industry sources (check mdrag KB first)
2. Only run company-specific queries
3. Merge new company-specific findings with existing industry analysis

## File Structure

```
datacrew/
  projects/domo-customer-outreach/scripts/
    research/
      06_research_company.py         [existing]
      06b_research_industry.py        [NEW]
    output/
      07_create_dossier.py            [UPDATED — accept --from-industry-research]
      09_sync_contacts.py             [no changes]
    dossier/
      model.py                        [no changes]
      synthesis.py                    [no changes]
      tabs/
        overview.py                   [no changes]
        people.py                     [no changes]
        org_chart.py                  [no changes]
        outreach_strategy.py          [no changes]
        industry_analysis.py          [NEW]

  data/industry-queries/
    aerospace-defense-supply-chain.yaml  [NEW]
    # future: construction.yaml, financial-services.yaml, generic.yaml

  data/EXPORTS/research/{company_slug}/
    research.json                     [existing]
    industry_research.json            [NEW]
    personas.md                       [existing]
    org_chart.md                      [existing]

outreach/  (shared library)
  src/outreach/models/
    industry_research.py              [NEW — IndustryResearch dataclass]

mdrag/
  src/integrations/
    industry/                         [NEW — Phase 2]
      __init__.py
      base.py                         [IndustryResearchCollector protocol]
      alixpartners.py                 [AlixPartnersCollector]
      mckinsey.py                     [McKinseyIndustryCollector]
      scor.py                         [SCORFrameworkCollector]
      registry.py                     [INDUSTRY_ADAPTORS mapping]
```

## Success Criteria

1. Running `06b_research_industry.py --company "Blue Raven Solutions" --industry "aerospace-defense-supply-chain"` produces `industry_research.json` with:
   - At least 5 KPIs with benchmarks (where available)
   - At least 5 industry problems
   - At least 3 industry trends
   - At least 3 benchmark sources

2. Running `07_create_dossier.py --company "Blue Raven Solutions" --from-research ... --from-industry-research ...` produces a Google Doc with 5 tabs, where the Industry Analysis tab contains:
   - Industry overview
   - Top 10 problems table
   - Key KPIs & benchmarks table
   - Benchmark sources table
   - Industry trends table

3. The Industry Analysis tab content is specific enough that Jae can walk into a discovery interview and say "Your inventory turnover is X. Industry median is 3.2x. Top quartile is 4.1x." without doing any additional research.

4. Re-running for a second company in the same industry (e.g., another A&D supply chain company) reuses the mdrag KB content and only runs company-specific queries.

## Open Questions

1. **LLM for synthesis**: Use the existing `Synthesizer` pattern (letta CLI) or direct LLM call? The existing `Synthesizer` uses `letta -p` headless CLI. For industry research, a direct LLM call with structured output might be simpler.

2. **Industry classification**: The `research.json` `industry` field is free-text from LLM synthesis. It might say "Aerospace & Defense" or "A&D Supply Chain" or "Defense Contractor." Need a normalization step (fuzzy match to canonical industry keys).

3. **mdrag service availability**: The pipeline assumes mdrag API is running (for ingestion and RAG queries). If mdrag is down, should we fall back to direct LLM synthesis with raw search results? Or fail hard?

4. **Caching strategy**: Industry research for the same industry doesn't change week-to-week. Should we cache `industry_research.json` per industry (not per company) and only re-research if older than N days?

5. **APQC membership**: Phase 3 depends on APQC membership. Should we start the membership process now, or wait until we have a paying engagement that requires it?
