"""Weight-shift helpers for the cascading archetype model."""

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
    "rental_yield": "yield_cash_flow",
    "yield": "yield_cash_flow",
    "roi": "yield_cash_flow",
    "citizenship": "residency_citizenship",
    "golden_visa": "residency_citizenship",
    "residency": "residency_citizenship",
    "lifestyle": "lifestyle_end_use",
    "end_use": "lifestyle_end_use",
    "vacation_home": "lifestyle_end_use",
    "capital_appreciation": "capital_appreciation",
    "capital_preservation": "capital_preservation",
    "investment_diversification": "investment_diversification",
    "yield_cash_flow": "yield_cash_flow",
    "residency_citizenship": "residency_citizenship",
    "lifestyle_end_use": "lifestyle_end_use",
}


def canonical_objective(value: str | None) -> str:
    """Map UI objective values to engine archetype keys."""
    raw = value or ""
    return OBJECTIVE_ALIASES.get(raw, raw)


def _shift_items(shifts) -> list[tuple[str, float]]:
    """Return shift entries while preserving duplicate determinant shifts."""
    if hasattr(shifts, "items"):
        return list(shifts.items())
    if isinstance(shifts, Iterable):
        return list(shifts)
    return []


def _normalize_with_bounds(weights: Mapping[str, float]) -> dict[str, float]:
    """Normalize to 100 while preserving determinant floor and cap bounds."""
    remaining = set(weights)
    fixed = {}

    while remaining:
        target = 100.0 - sum(fixed.values())
        remaining_total = sum(float(weights[key]) for key in remaining) or 1.0
        proposed = {
            key: (float(weights[key]) / remaining_total) * target
            for key in remaining
        }

        newly_fixed = {
            key: WEIGHT_FLOOR
            for key, value in proposed.items()
            if value < WEIGHT_FLOOR
        }
        newly_fixed.update({
            key: WEIGHT_CAP
            for key, value in proposed.items()
            if value > WEIGHT_CAP
        })

        if not newly_fixed:
            fixed.update(proposed)
            break

        fixed.update(newly_fixed)
        remaining -= set(newly_fixed)

    normalized = {
        determinant: round(value, 2)
        for determinant, value in fixed.items()
    }

    residual = round(100.0 - sum(normalized.values()), 2)
    if residual:
        candidates = [
            key for key, value in normalized.items()
            if (
                (residual > 0 and value + residual <= WEIGHT_CAP)
                or (residual < 0 and value + residual >= WEIGHT_FLOOR)
            )
        ]
        if candidates:
            key = max(candidates, key=lambda item: normalized[item])
            normalized[key] = round(normalized[key] + residual, 2)

    return {key: normalized[key] for key in weights}


def apply_shifts_with_sources(
    baseline_weights: Mapping[str, float],
    sources: list[tuple[str, str, Mapping[str, float] | list[tuple[str, float]]]],
) -> tuple[dict[str, float], dict[str, float], list[dict]]:
    """
    Apply dynamic determinant shifts with diminishing returns.

    Adjusted Shift = Raw Shift x (1 - Current Weight / 100)
    Tier 1 sources use max impact 25; Tier 2 sources use max impact 15.
    Buckets are clamped to the 5-35 range before final normalization.
    """
    weights = {key: float(value) for key, value in baseline_weights.items()}
    log = []
    shift_entries = []

    for tier_label, source_label, shifts in sources:
        if not shifts:
            continue

        for determinant, raw_shift in _shift_items(shifts):
            shift_entries.append((
                tier_label,
                source_label,
                determinant,
                float(raw_shift),
            ))

    ordered_entries = [
        *sorted(
            [entry for entry in shift_entries if entry[3] > 0],
            key=lambda item: -item[3],
        ),
        *sorted(
            [entry for entry in shift_entries if entry[3] < 0],
            key=lambda item: item[3],
        ),
    ]

    for tier_label, source_label, determinant, raw_shift in ordered_entries:
        current = weights.get(determinant, 0.0)
        adjusted_shift = raw_shift * (1 - current / 100)
        shifted = current + adjusted_shift
        new_weight = min(max(shifted, WEIGHT_FLOOR), WEIGHT_CAP)
        max_impact = TIER_1_MAX if tier_label == "Tier 1" else TIER_2_MAX

        log.append({
            "tier": tier_label,
            "source": source_label,
            "max_impact": max_impact,
            "determinant": determinant,
            "raw_shift": raw_shift,
            "adjusted_shift": round(adjusted_shift, 3),
            "before": round(current, 3),
            "after": round(new_weight, 3),
        })
        weights[determinant] = new_weight

    normalized = _normalize_with_bounds(weights)
    for entry in log:
        determinant = entry["determinant"]
        entry["final_weight"] = normalized.get(determinant, 0)
    return weights, normalized, log


def apply_shifts(
    baseline_weights: Mapping[str, float],
    tier1_shifts: Mapping[str, float],
    tier2_shifts: Mapping[str, float],
) -> tuple[dict[str, float], dict[str, float], list[dict]]:
    """Backward-compatible two-tier shift API used by country and city pages."""
    return apply_shifts_with_sources(
        baseline_weights,
        [
            ("Tier 1", "Primary Objective", tier1_shifts),
            ("Tier 2", "Risk Appetite", tier2_shifts),
        ],
    )
