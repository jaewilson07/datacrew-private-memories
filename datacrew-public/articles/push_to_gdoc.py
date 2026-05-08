"""Push EmmaBot articles to Google Docs as tabs.

Usage: python3 push_to_gdoc.py
"""
import asyncio
import os
import sys

# Add cboti to path
sys.path.insert(0, "/workspace/libraries/cboti/src")

from cboti.integrations.google.drive.google_docs import GoogleDoc
from cboti.integrations.google.auth import GoogleAuth


def load_env_var(name: str) -> str:
    """Load an env var from .env file, handling Infisical's JSON-quoting."""
    val = os.getenv(name)
    if val:
        # Strip surrounding quotes if present
        if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            val = val[1:-1]
        return val
    # Try reading from .env
    with open("/workspace/.env") as f:
        for line in f:
            if line.startswith(f"{name}="):
                val = line.split("=", 1)[1].strip()
                # Strip surrounding quotes
                if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
                    val = val[1:-1]
                return val
    raise ValueError(f"Env var {name} not found")


async def main():
    # Load credentials
    gdoc_client = load_env_var("GDOC_CLIENT")
    gdoc_token = load_env_var("GDOC_TOKEN")

    auth = GoogleAuth(
        credentials_json=gdoc_client,
        token_json=gdoc_token,
        scopes=["https://www.googleapis.com/auth/drive"],
    )

    doc = GoogleDoc(auth)

    document_id = "1zHb6nnleJbyeOak-UxRnhXZsOxe67c6JD7zsj6dBitU"

    # Read the markdown files
    with open("/workspace/projects/articles/emma-memory-store/index.md") as f:
        tab1_content = f.read()

    with open("/workspace/projects/articles/emma-slack-training/index.md") as f:
        tab2_content = f.read()

    print("Pushing Tab 1: Building EmmaBot's Brain...")
    tab1 = await doc.Tabs.upsert(
        document_id,
        "Building EmmaBot's Brain",
        tab1_content,
        mode="replace",
    )
    print(f"  Tab 1 created: {tab1.tab_id} — '{tab1.title}'")

    print("Pushing Tab 2: Training EmmaBot...")
    tab2 = await doc.Tabs.upsert(
        document_id,
        "Training EmmaBot",
        tab2_content,
        mode="replace",
    )
    print(f"  Tab 2 created: {tab2.tab_id} — '{tab2.title}'")

    print("\nDone! Both tabs pushed to Google Doc.")
    print(f"https://docs.google.com/document/d/{document_id}/edit")


if __name__ == "__main__":
    asyncio.run(main())
