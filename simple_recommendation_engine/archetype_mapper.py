"""
archetype_mapper.py — Weight-shift helpers for the cascading archetype model.

FIX #1 APPLIED: Aggregate-first diminishing returns.
  OLD: shifts applied sequentially — order-dependent results.
  NEW: collect ALL raw shifts per determinant, sum them, apply formula ONCE.
  Formula: Adjusted_Shift = Sum_of_Raw_Shifts × (1 - Baseline_Weight / 100)
"""
from __future__ import annotations
from collections.abc import Iterable
from typing import Mapping

from simple_recommendation_engine.constants import (
    TIER_1_MAX,
    TIER_2_MAX,
    WEIGHT_CAP,
    WEIGHT_FLOOR,
)

OBJECTIVE_ALIASES = {
    "rental_yield":               "yield_cash_flow",
    "yield":                      "yield_cash_flow",
    "roi":                        "yield_cash_flow",
    "citizenship":                "residency_citizenship",
    "golden_visa":                "residency_citizenship",
    "residency":                  "residency_citizenship",
    "lifestyle":                  "lifestyle_end_use",
    "end_use":                    "lifestyle_end_use",
    "vacation_home":              "lifestyle_end_use",
    "capital_appreciation":       "capital_appreciation",
    "capital_preservation":       "capital_preservation",
    "investment_diversification": "investment_diversification",
    "yield_cash_flow":            "yield_cash_flow",
    "residency_citizenship":      "residency_citizenship",
    "lifestyle_end_use":          "lifestyle_end_use",
}


def canonical_objective(value: str | None) -> str:
    raw = value or ""
    return OBJECTIVE_ALIASES.get(raw, raw)


def _shift_items(shifts) -> list[tuple[str, float]]:
    if hasattr(shifts, "items"):
        return list(shifts.items())
    if isinstance(shifts, Iterable):
        return list(shifts)
    return []


def _normalize_with_bounds(
    weights: Mapping[str, float],
    floor: float = None,
    cap: float = None,
) -> dict[str, float]:
    """
    Proportional normalization to 100 with configurable floor and cap.
    Defaults to module-level WEIGHT_FLOOR / WEIGHT_CAP if not provided.
    """
    w_floor = floor if floor is not None else WEIGHT_FLOOR
    w_cap   = cap   if cap   is not None else WEIGHT_CAP

    remaining = set(weights)
    fixed: dict[str, float] = {}

    while remaining:
        target = 100.0 - sum(fixed.values())
        remaining_total = sum(float(weights[k]) for k in remaining) or 1.0
        proposed = {
            k: (float(weights[k]) / remaining_total) * target
            for k in remaining
        }
        newly_fixed = {k: w_floor for k, v in proposed.items() if v < w_floor}
        newly_fixed.update({k: w_cap for k, v in proposed.items() if v > w_cap})
        if not newly_fixed:
            fixed.update(proposed)
            break
        fixed.update(newly_fixed)
        remaining -= set(newly_fixed)

    normalized = {k: round(v, 2) for k, v in fixed.items()}
    residual = round(100.0 - sum(normalized.values()), 2)
    if residual:
        candidates = [
            k for k, v in normalized.items()
            if (residual > 0 and v + residual <= w_cap)
            or (residual < 0 and v + residual >= w_floor)
        ]
        if candidates:
            best = max(candidates, key=lambda k: normalized[k])
            normalized[best] = round(normalized[best] + residual, 2)

    return {k: normalized[k] for k in weights}


def apply_shifts_with_sources(
    baseline_weights: Mapping[str, float],
    sources: list[tuple[str, str, Mapping[str, float] | list[tuple[str, float]]]],
    weight_floor: float = None,
    weight_cap: float = None,
) -> tuple[dict[str, float], dict[str, float], list[dict]]:
    """
    Apply dynamic determinant shifts with aggregate-first diminishing returns.

    FIX #1: All raw shifts per determinant are summed before applying the
    diminishing returns formula. Result is order-independent.

    Args:
        baseline_weights : dict {determinant: weight} summing to 100
        sources          : list of (tier_label, source_label, shifts_dict)
        weight_floor     : override floor (default: WEIGHT_FLOOR from constants)
        weight_cap       : override cap   (default: WEIGHT_CAP from constants)

    Returns:
        (post_shift_weights, normalized_weights, log)
    """
    w_floor = weight_floor if weight_floor is not None else WEIGHT_FLOOR
    w_cap   = weight_cap   if weight_cap   is not None else WEIGHT_CAP

    baseline = {k: float(v) for k, v in baseline_weights.items()}

    # Pass 1: aggregate all raw shifts per determinant
    aggregated: dict[str, float] = {}
    shift_sources: dict[str, list[str]] = {}

    for tier_label, source_label, shifts in sources:
        if not shifts:
            continue
        for det, raw_shift in _shift_items(shifts):
            aggregated[det] = aggregated.get(det, 0.0) + float(raw_shift)
            shift_sources.setdefault(det, []).append(f"{tier_label}:{source_label}")

    # Pass 2: apply diminishing returns once per determinant on the baseline
    post_shift = dict(baseline)
    log = []

    for det, total_raw in aggregated.items():
        base_w = baseline.get(det, 0.0)
        adj = total_raw * (1.0 - base_w / 100.0)
        new_w = min(max(base_w + adj, w_floor), w_cap)

        log.append({
            "determinant":     det,
            "sources":         shift_sources.get(det, []),
            "total_raw_shift": round(total_raw, 3),
            "adjusted_shift":  round(adj, 3),
            "baseline":        round(base_w, 3),
            "post_shift":      round(new_w, 3),
        })
        post_shift[det] = new_w

    normalized = _normalize_with_bounds(post_shift, floor=w_floor, cap=w_cap)

    for entry in log:
        entry["final_weight"] = normalized.get(entry["determinant"], 0.0)

    return post_shift, normalized, log


def apply_shifts(
    baseline_weights: Mapping[str, float],
    tier1_shifts: Mapping[str, float],
    tier2_shifts: Mapping[str, float],
) -> tuple[dict[str, float], dict[str, float], list[dict]]:
    """Backward-compatible two-tier API for country and city engines."""
    return apply_shifts_with_sources(
        baseline_weights,
        [
            ("Tier 1", "Primary Objective", tier1_shifts),
            ("Tier 2", "Risk Appetite",     tier2_shifts),
        ],
    )