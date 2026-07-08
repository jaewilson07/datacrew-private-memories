"""env_loader — 3-tier .env resolver for monorepo root agent scripts.

This file lives at <monorepo_root>/.agents/env_loader.py.
For root-level skills/runbooks/tests, LIBRARY_ROOT == MONOREPO_ROOT.

Priority (last wins / highest precedence):
  1. <monorepo_root>/.env              — shared baseline secrets
  2. <monorepo_root>/.env.local        — optional local overrides
  3. <monorepo_root>/.agents/tests/.env — test-only ephemeral overrides

Usage (import at the top of every root .agents script):

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent / ".agents"))
    from env_loader import load_env, MONOREPO_ROOT

    load_env()  # always call before any other import that reads env-vars

Notes:
  - Each .env file is optional; missing files are silently skipped.
  - load_env() is idempotent — safe to call multiple times.
  - Never commit real .env files; commit .env.example instead.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from dotenv import load_dotenv as _load_dotenv
except ImportError:
    raise ImportError("python-dotenv is required. Add it to your pyproject.toml or run: " "uv add python-dotenv")

# ── Path resolution ───────────────────────────────────────────────────────────
# This file lives at:  <monorepo_root>/.agents/env_loader.py
# So parent == .agents/, parent.parent == <monorepo_root>/

_ENV_LOADER_DIR: Path = Path(__file__).resolve().parent  # .agents/
MONOREPO_ROOT: Path = _ENV_LOADER_DIR.parent  # <monorepo_root>/
LIBRARY_ROOT: Path = MONOREPO_ROOT  # same for root scripts

# ── 3-tier load ───────────────────────────────────────────────────────────────

_LOADED: bool = False


def load_env(
    *,
    override: bool = True,
    include_mdrag: bool = False,
    include_datacrew: bool = False,
) -> None:
    """Load .env files in priority order (highest priority loads last).

    Args:
        override: When True (default), later files override earlier ones.
        include_mdrag: When True, add libraries/mdrag/.env as an early
                       tier (provides MONGODB_URI without Letta vars).
        include_datacrew: When True, add datacrew/.env as the
                          final override tier (cloud Letta vars win).
    """
    global _LOADED
    if _LOADED:
        return

    tiers: list[Path] = []

    if include_mdrag:
        tiers.append(MONOREPO_ROOT / "libraries" / "mdrag" / ".env")

    tiers += [
        MONOREPO_ROOT / ".env",  # shared baseline
        MONOREPO_ROOT / ".env.local",  # optional local overrides
        _ENV_LOADER_DIR / "tests" / ".env",  # test override
    ]

    if include_datacrew:
        tiers.append(MONOREPO_ROOT / "datacrew" / ".env")

    loaded: list[Path] = []
    for env_path in tiers:
        if env_path.exists():
            _load_dotenv(env_path, override=override)
            loaded.append(env_path)

    if not loaded:
        import warnings

        warnings.warn(
            "env_loader: no .env files found in any of:\n" + "\n".join(f"  {p}" for p in tiers),
            stacklevel=2,
        )

    _LOADED = True


def require_env(*keys: str) -> dict[str, str]:
    """Assert that all named env-vars are set after load_env().

    Returns a dict of {key: value}.
    Raises EnvironmentError listing all missing keys.
    """
    load_env()
    missing = [k for k in keys if not os.getenv(k)]
    if missing:
        raise EnvironmentError(f"env_loader: required env vars not set: {', '.join(missing)}")
    return {k: os.environ[k] for k in keys}
