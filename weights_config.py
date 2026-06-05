"""
weights_config.py — Dynamic determinant weights for all three engines.

PROJECT ENGINE CHANGE:
  Old: 8 flat determinants (delivery_history, expected_rental_yield, etc.)
  New: 13 sub-category buckets mapped from Ridhima's spec:

  MICRO MARKET (35% total):
    demand_and_liquidity          12.25%
    neighborhood_livability        8.75%
    demographic_economic_strength  7.00%
    supply_pressure_risk           7.00%  ← INVERSE

  DEVELOPER (30% total):
    delivery_track_record         10.50%  ← INVERSE
    financial_credibility          7.50%
    build_integrity                7.50%
    legal_and_governance           4.50%  ← INVERSE

  PROJECT (35% total):
    exit_liquidity                 8.75%
    comp_market_performance        8.75%
    projected_rental_yields        7.00%
    speculation_risk_score         7.00%  ← DYNAMIC (STANDARD or INVERSE)
    infra_and_connectivity         3.50%

  Project engine floor/ceiling: 2% / 30% (different from country/city 5%/35%)

SPECULATION RISK TAG:
  Determines whether speculation_risk_score is treated as STANDARD or INVERSE
  in Track B normalization. Resolved via:
    1. Usage Intent sets the initial tag
    2. Risk Appetite overrides if it fires a tag
  compute_project_weights() returns the resolved tag as a third value.
"""
from simple_recommendation_engine.archetype_mapper import (
    apply_shifts,
    apply_shifts_with_sources,
    canonical_objective,
)
from simple_recommendation_engine.constants import (
    CITY_BASELINE_WEIGHTS,
    CITY_TIER1_SHIFTS,
    CITY_TIER2_SHIFTS,
    COUNTRY_BASELINE_WEIGHTS,
    COUNTRY_TIER1_SHIFTS,
    COUNTRY_TIER2_SHIFTS,
    PROJECT_BASELINE_WEIGHTS,
    WEIGHT_CAP,
    WEIGHT_FLOOR,
)
from simple_recommendation_engine.normalization import winsorize

# ── Project-engine specific bounds (different from country/city) ──────────────
PROJECT_WEIGHT_FLOOR = 2.0
PROJECT_WEIGHT_CAP   = 30.0

# ─────────────────────────────────────────────────────────────────────────────
# TIER 1 SHIFTS — Core Investment Mechanics (max ±25 points)
# Keys map to the 13 new sub-category bucket names
# ─────────────────────────────────────────────────────────────────────────────

# 1. Usage Intent
PROJECT_TIER1_USAGE_SHIFTS = {
    "pure_investment": {
        "projected_rental_yields":  13,
        "comp_market_performance":  12,
        "neighborhood_livability": -15,
        "infra_and_connectivity":  -10,
    },
    "investment_occasional_use": {
        "neighborhood_livability":   10,
        "projected_rental_yields":    8,
        "infra_and_connectivity":     7,
        "comp_market_performance":  -12,
        "speculation_risk_score":   -13,
    },
    "primary_relocation": {
        "neighborhood_livability":   15,
        "infra_and_connectivity":    10,
        "projected_rental_yields":  -15,
        "exit_liquidity":           -10,
    },
}

# Speculation Risk tag per usage intent
# Risk Appetite overrides this — see _RISK_SPECULATION_TAG below
_USAGE_SPECULATION_TAG = {
    "pure_investment":          "standard",
    "investment_occasional_use": "inverse",
    "primary_relocation":       "inverse",
}

# 2. Risk Appetite
PROJECT_TIER1_RISK_SHIFTS = {
    "conservative": {
        "delivery_track_record":    10,
        "financial_credibility":     8,
        "legal_and_governance":      7,
        "comp_market_performance":  -15,
        "supply_pressure_risk":     -10,
    },
    "moderate": {},
    "opportunistic": {
        "comp_market_performance":   13,
        "projected_rental_yields":   12,
        "delivery_track_record":    -15,
        "legal_and_governance":     -10,
    },
}

# Risk Appetite overrides Speculation Risk tag when it fires
_RISK_SPECULATION_TAG = {
    "conservative":  "inverse",
    "moderate":      None,        # no override — usage intent tag stands
    "opportunistic": "standard",
}

# ─────────────────────────────────────────────────────────────────────────────
# TIER 2 SHIFTS — Tactical Preferences (max ±15 points)
# ─────────────────────────────────────────────────────────────────────────────

# 3. Holding Period
PROJECT_TIER2_HOLDING_SHIFTS = {
    "short_term": {
        "exit_liquidity":           10,
        "demand_and_liquidity":      5,
        "projected_rental_yields": -10,
        "build_integrity":          -5,
    },
    "medium_term": {},   # balanced — no shifts
    "long_term": {
        "build_integrity":           9,
        "demographic_economic_strength": 6,
        "exit_liquidity":          -10,
        "speculation_risk_score":   -5,
    },
}

# 4. Liquidity Preference
PROJECT_TIER2_LIQUIDITY_SHIFTS = {
    "high_resale": {
        "exit_liquidity":           10,
        "demand_and_liquidity":      5,
        "build_integrity":          -8,
        "financial_credibility":    -7,
    },
    "long_lockin": {
        "comp_market_performance":   8,
        "delivery_track_record":     7,
        "exit_liquidity":          -15,
    },
}

# 5. Family Composition
PROJECT_TIER2_FAMILY_SHIFTS = {
    "family": {
        "neighborhood_livability":  10,
        "infra_and_connectivity":    5,
        "exit_liquidity":          -10,
        "speculation_risk_score":   -5,
    },
    "single_couple": {
        "speculation_risk_score":   10,
        "demand_and_liquidity":      5,
        "neighborhood_livability": -15,
    },
}

# 6. Proximity Preference
PROJECT_TIER2_PROXIMITY_SHIFTS = {
    "airport_cbd_leisure": {
        "infra_and_connectivity":   15,
        "neighborhood_livability": -10,
        "build_integrity":          -5,
    },
    "schools_hospitals": {
        "neighborhood_livability":  15,
        "infra_and_connectivity":  -10,
        "exit_liquidity":           -5,
    },
}

# 7. Prestige / Brand Sensitivity
PROJECT_TIER2_PRESTIGE_SHIFTS = {
    "high": {
        "build_integrity":          10,
        "financial_credibility":     5,
        "projected_rental_yields": -10,
        "speculation_risk_score":   -5,
    },
    "medium": {},
    "low": {},
}

# 8. Investor Experience Level
PROJECT_TIER2_EXPERIENCE_SHIFTS = {
    "first_international": {
        "delivery_track_record":    10,
        "legal_and_governance":      5,
        "speculation_risk_score":  -10,
        "comp_market_performance":  -5,
    },
    "domestic_only": {
        "build_integrity":           8,
        "financial_credibility":     7,
        "speculation_risk_score":   -8,
        "supply_pressure_risk":     -7,
    },
    "experienced_international": {
        "comp_market_performance":  10,
        "exit_liquidity":            5,
        "delivery_track_record":   -10,
        "neighborhood_livability":  -5,
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# WEIGHT COMPUTE FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def compute_country_weights(answers):
    """Compute cascading country weights from objective and risk archetypes."""
    objective = canonical_objective(answers.get("primary_objective"))
    risk = answers.get("risk_appetite", "moderate")
    return apply_shifts(
        COUNTRY_BASELINE_WEIGHTS,
        COUNTRY_TIER1_SHIFTS.get(objective, {}),
        COUNTRY_TIER2_SHIFTS.get(risk, {}),
    )


def compute_city_weights(answers):
    """Simple additive city weights: baseline + T1 + T2 → clamp(5,35) → renormalize."""
    objective = answers.get("primary_objective", "")
    risk = answers.get("risk_appetite", "neutral")

    t1_shifts = CITY_TIER1_SHIFTS.get(objective, {})
    t2_shifts = CITY_TIER2_SHIFTS.get(risk, {})

    weights = {k: float(v) for k, v in CITY_BASELINE_WEIGHTS.items()}
    for key, shift in t1_shifts.items():
        weights[key] = weights[key] + float(shift)
    for key, shift in t2_shifts.items():
        weights[key] = weights[key] + float(shift)

    for key in weights:
        weights[key] = max(5.0, min(35.0, weights[key]))

    total = sum(weights.values())
    normalized = {k: round(weights[k] / total * 100, 2) for k in weights}
    residual = round(100.0 - sum(normalized.values()), 2)
    if residual:
        best = max(normalized, key=lambda k: normalized[k])
        normalized[best] = round(normalized[best] + residual, 2)

    # Build log for UI display (raw == adjusted — no diminishing returns)
    log = []
    for det in set(t1_shifts) | set(t2_shifts):
        base = float(CITY_BASELINE_WEIGHTS.get(det, 0))
        t1 = float(t1_shifts.get(det, 0))
        t2 = float(t2_shifts.get(det, 0))
        total_raw = t1 + t2
        sources = []
        if t1:
            sources.append(f"Tier 1:{objective}")
        if t2:
            sources.append(f"Tier 2:{risk}")
        log.append({
            "determinant":    det,
            "sources":        sources,
            "total_raw_shift": total_raw,
            "adjusted_shift":  total_raw,
            "baseline":        base,
            "post_shift":      max(5.0, min(35.0, base + total_raw)),
            "final_weight":    normalized.get(det, base),
        })

    return weights, normalized, log


def resolve_speculation_tag(usage: str, risk: str) -> str:
    """
    Resolve the Speculation Risk dynamic tag.

    Priority:
      1. Risk Appetite overrides if it fires a non-None tag
      2. Usage Intent sets the fallback

    Returns: "standard" or "inverse"
    """
    # Risk Appetite override takes priority
    risk_tag = _RISK_SPECULATION_TAG.get(risk)
    if risk_tag is not None:
        return risk_tag
    # Fall back to Usage Intent tag
    return _USAGE_SPECULATION_TAG.get(usage, "standard")


def _reapply_project_bounds(weights: dict) -> dict:
    """
    Re-clamp and re-normalize weights to project-specific bounds (2%/30%).
    Called after apply_shifts_with_sources which uses the global 5%/35% bounds.
    """
    # Clamp to project bounds
    clamped = {
        k: min(max(v, PROJECT_WEIGHT_FLOOR), PROJECT_WEIGHT_CAP)
        for k, v in weights.items()
    }
    # Proportional re-normalize to 100
    total = sum(clamped.values()) or 1.0
    normalized = {k: round((v / total) * 100, 2) for k, v in clamped.items()}
    # Fix floating point residual
    residual = round(100.0 - sum(normalized.values()), 2)
    if residual:
        best = max(normalized, key=lambda k: normalized[k])
        normalized[best] = round(normalized[best] + residual, 2)
    return normalized


def compute_project_weights(answers: dict) -> tuple[dict, dict, list, str]:
    """
    Compute project weights from all 8 investor survey dimensions.

    Returns:
        (post_shift_weights, normalized_weights, log, speculation_tag)
          post_shift_weights : weights after shifts + initial clamp
          normalized_weights : final weights summing to 100 (project 2%/30% bounds)
          log                : per-determinant audit trail
          speculation_tag    : "standard" or "inverse" for speculation_risk_score
    """
    usage     = answers.get("usage_intent", "")
    risk      = answers.get("risk_appetite", "moderate")
    holding   = answers.get("holding_period", "")
    liquidity = answers.get("liquidity_preference", "")
    family    = answers.get("family_composition", "")
    proximity = answers.get("proximity_preference", "")
    prestige  = answers.get("prestige_sensitivity", "medium")
    # Streamlit UI uses short keys; shift tables use canonical keys
    _experience_aliases = {
        "first_time": "first_international",
        "experienced": "experienced_international",
    }
    experience = _experience_aliases.get(
        answers.get("investor_experience", ""),
        answers.get("investor_experience", ""),
    )

    sources = [
        # Tier 1
        (
            "Tier 1",
            f"Usage Intent = {usage.replace('_', ' ').title()}",
            PROJECT_TIER1_USAGE_SHIFTS.get(usage, {}),
        ),
        (
            "Tier 1",
            f"Risk Appetite = {risk.title()}",
            PROJECT_TIER1_RISK_SHIFTS.get(risk, {}),
        ),
        # Tier 2
        (
            "Tier 2",
            f"Holding Period = {holding.replace('_', ' ').title()}",
            PROJECT_TIER2_HOLDING_SHIFTS.get(holding, {}),
        ),
        (
            "Tier 2",
            f"Liquidity Preference = {liquidity.replace('_', ' ').title()}",
            PROJECT_TIER2_LIQUIDITY_SHIFTS.get(liquidity, {}),
        ),
        (
            "Tier 2",
            f"Family Composition = {family.replace('_', ' ').title()}",
            PROJECT_TIER2_FAMILY_SHIFTS.get(family, {}),
        ),
        (
            "Tier 2",
            f"Proximity Preference = {proximity.replace('_', ' ').title()}",
            PROJECT_TIER2_PROXIMITY_SHIFTS.get(proximity, {}),
        ),
        (
            "Tier 2",
            f"Prestige Sensitivity = {prestige.title()}",
            PROJECT_TIER2_PRESTIGE_SHIFTS.get(prestige, {}),
        ),
        (
            "Tier 2",
            f"Investor Experience = {experience.replace('_', ' ').title()}",
            PROJECT_TIER2_EXPERIENCE_SHIFTS.get(experience, {}),
        ),
    ]

    post_shift, normalized, log = apply_shifts_with_sources(
        PROJECT_BASELINE_WEIGHTS, sources,
        weight_floor=PROJECT_WEIGHT_FLOOR,
        weight_cap=PROJECT_WEIGHT_CAP,
    )

    for entry in log:
        entry["final_weight"] = normalized.get(entry["determinant"], 0.0)

    speculation_tag = resolve_speculation_tag(usage, risk)

    return post_shift, normalized, log, speculation_tag


# Retained for backward-compatible imports by diagnostics pages
CITY_QUESTION_DELTAS = {}