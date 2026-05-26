"""Shared helpers for Streamlit score / weight-log display."""


def engine_score_from_breakdown(info: dict) -> float:
    """Z-score engine index (0–100) from project score_breakdown row."""
    return info.get("engine_score", info.get("standardized", 50.0))


def weight_log_fields(entry: dict) -> dict:
    """Normalize weight-log entry keys (legacy vs archetype_mapper format)."""
    raw = entry.get("total_raw_shift", entry.get("raw_shift", 0))
    before = entry.get("baseline", entry.get("before", 0))
    after = entry.get("post_shift", entry.get("after", 0))
    final = entry.get("final_weight", after)
    sources = entry.get("sources") or []
    source_label = sources[0] if sources else entry.get("source", entry.get("tier", ""))
    return {
        "determinant": entry.get("determinant", ""),
        "raw": raw,
        "adjusted": entry.get("adjusted_shift", 0),
        "before": before,
        "after": after,
        "final": final,
        "source_label": source_label,
    }


def group_weight_log(weight_log: list[dict]) -> dict[str, list[dict]]:
    """Group log entries by survey source for expander display."""
    grouped: dict[str, list[dict]] = {}
    for entry in weight_log:
        fields = weight_log_fields(entry)
        label = fields["source_label"] or "Weight shifts"
        grouped.setdefault(label, []).append(entry)
    return grouped
