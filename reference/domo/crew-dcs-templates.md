---
description: Reusable code templates for common crew-dcs API tasks. Use when answering Domo API questions that can be solved with crew-dcs classes.
---

# crew-dcs Code Templates

## Style Rules

- **Always use classes over routes** — `DomoDataset`, `DomoDatasets`, etc. NOT `dataset_routes.search_datasets()`
- **Assume `.env` is already loaded** — no `load_dotenv`, no `Path` boilerplate
- **Type-annotate the return variable** — `datasets: list[DomoDataset] = await DomoDatasets(auth=auth).get()` so people know what they're getting back
- **Minimal code** — least amount necessary to demonstrate the pattern

## Template: Retrieve All Datasets

```python
"""Retrieve all datasets from a Domo instance."""

import asyncio
import os

from crew_dcs.auth import DomoTokenAuth
from crew_dcs.classes.DomoDataset import DomoDataset, DomoDatasets

auth = DomoTokenAuth(
    domo_instance=os.environ["DOMO_INSTANCE"],
    domo_access_token=os.environ["DOMO_ACCESS_TOKEN"],
)


async def main():
    datasets: list[DomoDataset] = await DomoDatasets(auth=auth).get()

    for ds in datasets:
        print(f"- {ds.name}  (id: {ds.id})")

    print(f"\nTotal: {len(datasets)}")


if __name__ == "__main__":
    asyncio.run(main())
```

**Variations:**
- Filter by name: `datasets: list[DomoDataset] = await DomoDatasets(auth=auth).get(search_text="keyword")`
- Filter by provider: `datasets: list[DomoDataset] = await DomoDatasets(auth=auth).get(data_provider_type="MySQL")`
- Hydrate schedules: `datasets: list[DomoDataset] = await DomoDatasets(auth=auth).get(hydrate_schedule_state=True)`

## Template: Get a Single Dataset by ID

```python
"""Retrieve a single dataset by ID."""

import asyncio
import os

from crew_dcs.auth import DomoTokenAuth
from crew_dcs.classes.DomoDataset import DomoDataset

auth = DomoTokenAuth(
    domo_instance=os.environ["DOMO_INSTANCE"],
    domo_access_token=os.environ["DOMO_ACCESS_TOKEN"],
)


async def main():
    dataset: DomoDataset = await DomoDataset.get_by_id(auth=auth, dataset_id="DATASET_ID")
    print(f"Name: {dataset.name}")
    print(f"Rows: {dataset.row_count}")
    print(f"Type: {dataset.data_provider_type}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Template: Query Dataset Data

```python
"""Query data from a dataset."""

import asyncio
import os

from crew_dcs.auth import DomoTokenAuth
from crew_dcs.classes.DomoDataset import DomoDataset

auth = DomoTokenAuth(
    domo_instance=os.environ["DOMO_INSTANCE"],
    domo_access_token=os.environ["DOMO_ACCESS_TOKEN"],
)


async def main():
    dataset: DomoDataset = await DomoDataset.get_by_id(auth=auth, dataset_id="DATASET_ID")
    await dataset.Data.query()
    print(dataset.Data.df)


if __name__ == "__main__":
    asyncio.run(main())
```

## Key Classes Reference

| Class | Module | Purpose |
|-------|--------|---------|
| `DomoTokenAuth` | `crew_dcs.auth` | Token-based auth |
| `DomoDatasets` | `crew_dcs.classes.DomoDataset` | Search/list multiple datasets |
| `DomoDataset` | `crew_dcs.classes.DomoDataset` | Single dataset operations |
| `DomoDatasetView` | `crew_dcs.classes.DomoDataset` | Dataset view operations |
| `DomoDataflow` | `crew_dcs.classes.DomoDataflow` | Dataflow operations |
| `DomoCard` | `crew_dcs.classes.DomoCard` | Card operations |
| `DomoPage` | `crew_dcs.classes.DomoPage` | Page operations |
| `DomoGroup` | `crew_dcs.classes.DomoGroup` | Group operations |
