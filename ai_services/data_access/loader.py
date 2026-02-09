"""
In-memory SQLite database initialization and seed data loading.

Loads the schema from backend/db/schema.sql and seeds three tables:
  - products   (from ai_services/data/products.jsonl)
  - contracts  (from ai_services/data/contracts.jsonl)
  - inventory  (from ai_services/data/inventory.jsonl)
"""

import json
import sqlite3
from pathlib import Path

_AI_SERVICES_ROOT = Path(__file__).resolve().parent.parent
_PROJECT_ROOT = _AI_SERVICES_ROOT.parent

SCHEMA_PATH = _PROJECT_ROOT / "backend" / "db" / "schema.sql"
PRODUCTS_PATH = _AI_SERVICES_ROOT / "data" / "products.jsonl"
CONTRACTS_PATH = _AI_SERVICES_ROOT / "data" / "contracts.jsonl"
INVENTORY_PATH = _AI_SERVICES_ROOT / "data" / "inventory.jsonl"


def _load_jsonl(conn: sqlite3.Connection, table: str, path: Path) -> None:
    """Load a JSONL file into the given SQLite table."""
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            cols = ", ".join(row.keys())
            vals = ", ".join(f":{k}" for k in row.keys())
            conn.execute(
                f"INSERT INTO {table} ({cols}) VALUES ({vals})", row
            )


def init_db() -> sqlite3.Connection:
    """
    Create an in-memory SQLite database, apply the schema,
    and seed all tables with mock data.

    Returns a ready-to-query connection with Row factory enabled.
    """
    conn = sqlite3.connect(":memory:", check_same_thread=False)

    conn.executescript(SCHEMA_PATH.read_text())

    _load_jsonl(conn, "products", PRODUCTS_PATH)
    _load_jsonl(conn, "contracts", CONTRACTS_PATH)
    _load_jsonl(conn, "inventory", INVENTORY_PATH)
    conn.commit()

    conn.row_factory = sqlite3.Row
    return conn


# Module-level singleton — initialized once on first import
db = init_db()
