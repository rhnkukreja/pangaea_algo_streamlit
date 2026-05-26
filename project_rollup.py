"""
project_rollup.py — Pre-Engine Data Roll-Up for the Project Engine

Converts raw individual variables (0–100 magnitude scores) into
13 sub-category bucket scores before the dynamic matching engine runs.

Architecture:
  Raw Variables (up to 25 per project)
      ↓  static internal weights
  13 Bucket Scores (0–100 each)
      ↓  dynamic investor weights
  Final Project Score

Two missing-data rules from the spec:
  PARTIAL: some variables in a bucket are null →
           redistribute their weight to present variables proportionally
  TOTAL:   all variables in a bucket are null →
           output exactly 50.0 (neutral — engine ignores this bucket)

Variable naming:
  All raw variables use snake_case keys matching the data population
  output format. Legacy 8-determinant keys are also accepted via
  LEGACY_VAR_ALIASES for backward compatibility with old projects_data.py.
"""
from __future__ import annotations
from typing import Any


# ─────────────────────────────────────────────────────────────────────────────
# STATIC INTERNAL WEIGHTS — 13 buckets × their component variables
# These never change. Shift tables in weights_config.py are separate.
# ─────────────────────────────────────────────────────────────────────────────
BUCKET_VARIABLE_MAP: dict[str, dict[str, float]] = {

    # ── MICRO MARKET (35% of engine pie) ─────────────────────────────────────
    "demand_and_liquidity": {
        "micro_market_stage":         30.0,
        "rental_absorption_velocity": 20.0,
        "resale_velocity":            20.0,
        "days_on_market":             15.0,
        "occupancy_vacancy_rate":     15.0,
    },
    "neighborhood_livability": {
        "safety_crime_index":   30.0,
        "healthcare_access":    25.0,
        "school_quality":       25.0,
        "air_quality_index":    10.0,
        "beach_coastal_access": 10.0,
    },
    "demographic_economic_strength": {
        "population_growth_rate": 60.0,
        "expat_concentration":    40.0,
    },
    "supply_pressure_risk": {           # ← INVERSE in engine
        "immediate_pipeline_risk": 60.0,
        "active_unsold_inventory": 40.0,
    },

    # ── DEVELOPER (30% of engine pie) ─────────────────────────────────────────
    "delivery_track_record": {          # ← INVERSE in engine
        "average_delay_duration":   45.0,
        "pct_projects_delivered":   35.0,
        "completion_consistency":   20.0,
    },
    "financial_credibility": {
        "escrow_quality":        35.0,
        "debt_cash_position":    30.0,
        "stalled_projects_count": 20.0,
        "presales_pct_achieved": 15.0,
    },
    "build_integrity": {
        "construction_quality": 100.0,
    },
    "legal_and_governance": {           # ← INVERSE in engine
        "litigation_history": 100.0,
    },

    # ── PROJECT (35% of engine pie) ───────────────────────────────────────────
    "exit_liquidity": {
        "average_exit_velocity": 70.0,
        "flipping_frequency":    30.0,
    },
    "comp_market_performance": {
        "comp_capital_appreciation": 50.0,
        "comp_rental_yields":        30.0,
        "comp_occupancy_rate":       20.0,
    },
    "projected_rental_yields": {
        "projected_rental_yield": 100.0,
    },
    "speculation_risk_score": {         # ← DYNAMIC tag (standard or inverse)
        "str_concentration":          45.0,
        "investor_owner_ratio":       35.0,
        "offplan_secondary_dominance": 20.0,
    },
    "infra_and_connectivity": {
        "infrastructure_proximity": 100.0,
    },
}

# All bucket keys in canonical order
ALL_BUCKETS: list[str] = list(BUCKET_VARIABLE_MAP.keys())


# ─────────────────────────────────────────────────────────────────────────────
# LEGACY VARIABLE ALIASES
# Maps old 8-determinant keys → new variable names so old projects_data.py
# entries still work without a full data migration.
# ─────────────────────────────────────────────────────────────────────────────
LEGACY_VAR_ALIASES: dict[str, str] = {
    # old key                        → new variable key
    "project_exit_liquidity":        "average_exit_velocity",
    "expected_rental_yield":         "projected_rental_yield",
    "public_infrastructure_proximity": "infrastructure_proximity",
    "delivery_history":              "pct_projects_delivered",
    "project_completion_rate":       "completion_consistency",
    "financial_strength":            "debt_cash_position",
    # construction_quality and litigation_history keep same name — no alias needed
}


def _resolve_aliases(raw_variables: dict[str, Any]) -> dict[str, Any]:
    """
    Expand legacy keys to their canonical names.
    If both old and new key exist, new key takes priority.
    """
    resolved = {}
    for k, v in raw_variables.items():
        canonical = LEGACY_VAR_ALIASES.get(k, k)
        resolved[canonical] = v
    # Original new-format keys override aliases
    for k, v in raw_variables.items():
        if k not in LEGACY_VAR_ALIASES:
            resolved[k] = v
    return resolved


def _score_value(value: Any) -> float | None:
    """
    Convert a raw_variable entry to a float score.
    Accepts:
      - Plain numeric:  {"construction_quality": 75}
      - Dict with score: {"construction_quality": {"score": 75, "source_note": "..."}}
      - None / null → returns None (triggers missing-data fallback)
    """
    if value is None:
        return None
    if isinstance(value, dict):
        v = value.get("score")
        return float(v) if v is not None else None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def rollup_bucket(
    bucket_name: str,
    raw_variables: dict[str, Any],
) -> tuple[float, dict]:
    """
    Roll up one bucket's variables into a single 0–100 bucket score.

    Args:
        bucket_name   : one of the 13 canonical bucket keys
        raw_variables : project's raw_variables dict (already alias-resolved)

    Returns:
        (bucket_score, debug_info)
          bucket_score : float in [0, 100], or 50.0 if total missing data
          debug_info   : dict with present/missing variables and their contributions
    """
    variable_weights = BUCKET_VARIABLE_MAP.get(bucket_name, {})
    if not variable_weights:
        return 50.0, {"error": f"Unknown bucket: {bucket_name}"}

    present: dict[str, tuple[float, float]] = {}   # {var: (score, weight)}
    missing: list[str] = []

    for var, weight in variable_weights.items():
        score = _score_value(raw_variables.get(var))
        if score is not None:
            present[var] = (score, weight)
        else:
            missing.append(var)

    # ── TOTAL missing data → neutral fallback ─────────────────────────────────
    if not present:
        return 50.0, {
            "bucket": bucket_name,
            "status": "total_missing",
            "score": 50.0,
            "present": {},
            "missing": missing,
        }

    # ── PARTIAL missing → redistribute weight to present variables ────────────
    total_present_weight = sum(w for _, w in present.values())

    bucket_score = 0.0
    contributions = {}

    for var, (score, original_weight) in present.items():
        # Redistribute: effective_weight = (original / sum_of_present) * 100
        effective_weight = (original_weight / total_present_weight) * 100.0
        contribution = score * (effective_weight / 100.0)
        bucket_score += contribution
        contributions[var] = {
            "score":            round(score, 2),
            "original_weight":  original_weight,
            "effective_weight": round(effective_weight, 2),
            "contribution":     round(contribution, 2),
        }

    # Clamp to [0, 100] as safety net
    bucket_score = max(0.0, min(100.0, bucket_score))

    return round(bucket_score, 2), {
        "bucket":       bucket_name,
        "status":       "partial_missing" if missing else "complete",
        "score":        round(bucket_score, 2),
        "present":      contributions,
        "missing":      missing,
        "weight_redistributed": len(missing) > 0,
    }


def rollup_project(raw_variables: dict[str, Any]) -> tuple[dict[str, float], dict]:
    """
    Roll up all 13 buckets for one project.

    Args:
        raw_variables : dict of variable_name → score (int/float/dict/null)
                        Accepts both new format and legacy 8-determinant format.

    Returns:
        (bucket_scores, debug_report)
          bucket_scores : dict {bucket_name: score}  — 13 entries, each in [0,100]
          debug_report  : full per-bucket audit trail
    """
    resolved = _resolve_aliases(raw_variables)

    bucket_scores: dict[str, float] = {}
    debug_report: dict[str, dict] = {}

    for bucket in ALL_BUCKETS:
        score, debug = rollup_bucket(bucket, resolved)
        bucket_scores[bucket] = score
        debug_report[bucket] = debug

    return bucket_scores, debug_report


def rollup_all_projects(
    projects: dict[str, dict],
) -> dict[str, dict[str, float]]:
    """
    Roll up all projects in one pass.

    Args:
        projects : PROJECTS dict from projects_data.py
                   Each entry must have a "raw_variables" key.

    Returns:
        dict {project_key: {bucket_name: score}}
    """
    results = {}
    for key, project in projects.items():
        raw = project.get("raw_variables") or project.get("determinant_scores", {})
        bucket_scores, _ = rollup_project(raw)
        results[key] = bucket_scores
    return results