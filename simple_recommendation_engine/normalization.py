"""Normalization and final scoring helpers."""

from __future__ import annotations

from math import sqrt
from typing import Iterable, Mapping, Sequence


def z_score(value: float, population: Sequence[float]) -> float:
    """Calculate a population z-score, returning 0 for empty or flat data."""
    values = [float(v) for v in population]
    if not values:
        return 0.0

    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    std_dev = sqrt(variance)
    if std_dev == 0:
        return 0.0
    return (float(value) - mean) / std_dev


def winsorize_z(value: float, lower: float = -2.0, upper: float = 2.0) -> float:
    """Winsorize a z-score between lower and upper bounds."""
    return max(lower, min(upper, value))


def engine_score_from_z(value: float) -> float:
    """Convert winsorized z-score to engine score: 50 + (z x 25)."""
    return 50 + (winsorize_z(value) * 25)


def standardize_value(value: float, population: Sequence[float], inverse: bool = False) -> float:
    """Orient, z-score, winsorize, and convert a raw determinant value."""
    oriented_value = -float(value) if inverse else float(value)
    oriented_population = [-float(v) for v in population] if inverse else list(population)
    return engine_score_from_z(z_score(oriented_value, oriented_population))


def standardize_determinants(
    item_scores: Mapping[str, float],
    peer_scores: Iterable[Mapping[str, float]],
    determinants: Iterable[str],
    inverse_vars: set[str] | frozenset[str] | None = None,
) -> dict[str, float]:
    """Standardize all requested determinants for one item against its peers."""
    inverse_vars = inverse_vars or set()
    peers = list(peer_scores)
    standardized = {}

    for determinant in determinants:
        population = [
            float(scores.get(determinant, 0))
            for scores in peers
        ]
        standardized[determinant] = standardize_value(
            float(item_scores.get(determinant, 0)),
            population,
            inverse=determinant in inverse_vars,
        )

    return standardized


def weighted_score(
    standardized_scores: Mapping[str, float],
    normalized_weights: Mapping[str, float],
) -> tuple[float, dict[str, float]]:
    """Calculate final score as sum(normalized weight x standardized score)."""
    total = 0.0
    breakdown = {}

    for determinant, weight_pct in normalized_weights.items():
        determinant_score = float(standardized_scores.get(determinant, 50))
        contribution = determinant_score * (float(weight_pct) / 100)
        breakdown[determinant] = round(contribution, 2)
        total += contribution

    return round(total, 2), breakdown


def winsorize(value: float, all_values: Sequence[float], percentile: int = 95) -> float:
    """Backward-compatible value winsorizer for older imports and diagnostics."""
    if not all_values:
        return value
    sorted_values = sorted(float(v) for v in all_values)
    cap_idx = min(int(len(sorted_values) * percentile / 100), len(sorted_values) - 1)
    return min(float(value), sorted_values[cap_idx])
