"""Small data cleaning helpers (no external deps).

Functions operate on lists of dictionaries (rows) to keep examples lightweight.
"""
from typing import List, Dict, Iterable


def drop_missing_rows(rows: Iterable[Dict], required_fields: Iterable[str]) -> List[Dict]:
    """Return rows that contain all required_fields with non-empty values."""
    out = []
    for r in rows:
        ok = True
        for f in required_fields:
            if f not in r or r[f] is None or str(r[f]).strip() == "":
                ok = False
                break
        if ok:
            out.append(dict(r))
    return out


def normalize_column(rows: Iterable[Dict], column: str) -> List[Dict]:
    """Normalize numeric column to range [0,1]. Non-numeric values are left unchanged."""
    vals = []
    for r in rows:
        try:
            v = float(r.get(column, 0))
            vals.append(v)
        except Exception:
            pass
    if not vals:
        return [dict(r) for r in rows]
    lo, hi = min(vals), max(vals)
    if hi == lo:
        return [dict(r, **{column: 0.0}) for r in rows]
    out = []
    for r in rows:
        new = dict(r)
        try:
            v = float(r.get(column, 0))
            new[column] = (v - lo) / (hi - lo)
        except Exception:
            pass
        out.append(new)
    return out


if __name__ == "__main__":
    sample = [
        {"id": "1", "name": "Alice", "score": "85"},
        {"id": "2", "name": "Bob", "score": "92"},
        {"id": "3", "name": "", "score": "78"},
    ]
    print("Original:", sample)
    kept = drop_missing_rows(sample, ["id", "name"])
    print("After drop_missing_rows:", kept)
    norm = normalize_column(kept, "score")
    print("After normalize_column(score):", norm)
