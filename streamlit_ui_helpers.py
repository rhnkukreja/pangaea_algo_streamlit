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
        "sources": sources,  # Include full sources list for per-tier breakdown
    }


def expand_weight_log_by_source(weight_log: list[dict], shift_tables: dict) -> dict[str, list[dict]]:
    """
    Expand weight log entries by source tier with per-source raw shifts.
    
    For entries with multiple sources, looks up the raw shift contribution
    from each source (tier) separately and creates individual entries.
    
    Args:
        weight_log: list of weight log entries with 'sources' list
        shift_tables: dict mapping source labels to their shift dicts
                     e.g. {"Tier 1: Primary Objective = Capital Appreciation": {...}}
    
    Returns:
        dict[source_label] -> list of expanded entries with per-source raw shifts
    """
    grouped: dict[str, list[dict]] = {}
    
    for entry in weight_log:
        determinant = entry.get("determinant", "")
        sources = entry.get("sources") or []
        baseline = entry.get("baseline", 0)
        
        if not sources:
            # Fallback: single entry with no source breakdown
            label = "Weight Shifts"
            grouped.setdefault(label, []).append(entry)
            continue
        
        # For each source, extract its individual raw shift and create an entry
        for source_label in sources:
            # Look up the shift value for this source
            source_shifts = shift_tables.get(source_label, {})
            raw_shift = source_shifts.get(determinant, 0)
            
            # Create a per-source entry with only that source's contribution
            per_source_entry = dict(entry)
            per_source_entry["sources"] = [source_label]
            per_source_entry["total_raw_shift"] = raw_shift
            per_source_entry["adjusted_shift"] = raw_shift * (1.0 - baseline / 100.0) if baseline else 0
            
            grouped.setdefault(source_label, []).append(per_source_entry)
    
    return grouped


def group_weight_log(weight_log: list[dict]) -> dict[str, list[dict]]:
    """
    Group log entries by survey source for expander display.
    
    Returns entries grouped by their first source label (tier heading).
    """
    grouped: dict[str, list[dict]] = {}
    for entry in weight_log:
        fields = weight_log_fields(entry)
        label = fields["source_label"] or "Weight shifts"
        grouped.setdefault(label, []).append(entry)
    return grouped
