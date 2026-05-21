"""Small scoring data helpers for project-level responses."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class ScoreResult:
    """Container for a final weighted score and determinant breakdown."""

    score: float
    breakdown: Mapping[str, object]
