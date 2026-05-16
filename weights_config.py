# ─── CONSTANTS ────────────────────────────────────────────
WEIGHT_FLOOR = 5.0
WEIGHT_CAP = 35.0

# ─── INVERSE VARIABLES ────────────────────────────────────
# For these, higher raw value = worse outcome.
# They are already inverted during data normalization in the engine files.
# Tag them here for reference and validation.
INVERSE_COUNTRY_VARS = [
    "currency_volatility",
    "property_taxation_for_foreigners",
    "interest_rate_direction",
    "corruption_perception_index"
]
INVERSE_CITY_VARS = [
    "supply_pipeline"
]

# ─── COUNTRY BASELINES (must sum to 100) ──────────────────
COUNTRY_BASELINE_WEIGHTS = {
    "political_stability_index": 25,
    "currency_volatility": 20,
    "property_taxation_for_foreigners": 18,
    "interest_rate_direction": 15,
    "foreign_buyer_market_share": 12,
    "corruption_perception_index": 10
}

# ─── COUNTRY TIER 1 — Primary Objective (max ±15) ─────────
COUNTRY_TIER1_SHIFTS = {
     "capital_appreciation": {
        "foreign_buyer_market_share": 10,
        "interest_rate_direction": 5,
        "political_stability_index": -10,
        "corruption_perception_index": -5,
    },

    "yield_cash_flow": {
        "property_taxation_for_foreigners": 8,
        "currency_volatility": 7,
        "political_stability_index": -10,
        "foreign_buyer_market_share": -5,
    },

   "capital_preservation": {
    "political_stability_index": 5,
    "currency_volatility": 5,
    "foreign_buyer_market_share": -5,
    "interest_rate_direction": -10,
},

"investment_diversification": {
    "political_stability_index": 5,
    "currency_volatility": 5,
    "foreign_buyer_market_share": -5,
    "interest_rate_direction": -10,
},

    "residency_citizenship": {
        "political_stability_index": 10,
        "corruption_perception_index": 5,
        "property_taxation_for_foreigners": -10,
        "currency_volatility": -5,
    },
}

# ─── COUNTRY TIER 2 — Risk Appetite (max ±10) ─────────────
COUNTRY_TIER2_SHIFTS = {
    "conservative": {
        "political_stability_index": +7,
        "currency_volatility": +3,
        "foreign_buyer_market_share": -7,
        "interest_rate_direction": -3
    },
    "moderate": {},
    "opportunistic": {
        "foreign_buyer_market_share": +7,
        "interest_rate_direction": +3,
        "political_stability_index": -7,
        "currency_volatility": -3
    }
}

# ─── CITY BASELINES (must sum to 100) ─────────────────────
CITY_BASELINE_WEIGHTS = {
    "employment_growth": 15,
    "price_appreciation_5y": 15,
    "net_migration_rate": 14,
    "rental_demand_index": 14,
    "infrastructure_pipeline": 12,
    "liquidity_indicator": 10,
    "quality_of_life_index": 10,
    "tourism_strength": 5,
    "supply_pipeline": 5
}

# ─── CITY TIER 1 — Primary Objective (max ±15) ────────────
CITY_TIER1_SHIFTS = {
    "capital_appreciation": {
        "infrastructure_pipeline": +7,
        "price_appreciation_5y": +5,
        "net_migration_rate": +3,
        "rental_demand_index": -8,
        "liquidity_indicator": -4,
        "quality_of_life_index": -3
    },
    "yield_cash_flow": {
        "rental_demand_index": +8,
        "tourism_strength": +5,
        "employment_growth": +2,
        "price_appreciation_5y": -8,
        "infrastructure_pipeline": -7
    },
    "capital_preservation": {
        "liquidity_indicator": +8,
        "employment_growth": +5,
        "supply_pipeline": +2,
        "price_appreciation_5y": -9,
        "infrastructure_pipeline": -6
    },
    "lifestyle_end_use": {
        "quality_of_life_index": +10,
        "tourism_strength": +5,
        "rental_demand_index": -10,
        "price_appreciation_5y": -5
    },
    "residency_citizenship": {
        "liquidity_indicator": +8,
        "quality_of_life_index": +7,
        "rental_demand_index": -8,
        "infrastructure_pipeline": -4,
        "price_appreciation_5y": -3
    }
}

# ─── CITY TIER 2 — Risk Appetite (max ±10) ────────────────
CITY_TIER2_SHIFTS = {
    "conservative": {
        "liquidity_indicator": +5,
        "employment_growth": +3,
        "supply_pipeline": +2,
        "infrastructure_pipeline": -6,
        "price_appreciation_5y": -4
    },
    "moderate": {},
    "opportunistic": {
        "infrastructure_pipeline": +6,
        "net_migration_rate": +4,
        "liquidity_indicator": -6,
        "quality_of_life_index": -4
    }
}

# ─── CORE MATH FUNCTION ───────────────────────────────────


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
    "investment_diversification": "capital_appreciation",
    "yield_cash_flow":            "yield_cash_flow",
    "residency_citizenship":      "residency_citizenship",
    "lifestyle_end_use":          "lifestyle_end_use",
}


def apply_shifts(baseline_weights, tier1_shifts, tier2_shifts):
    """
    Applies Tier 1 then Tier 2 shifts using Diminishing Returns.
    Then proportionally normalizes to sum to 100.

    Rule 1: Tier 1 max ±15, Tier 2 max ±10 (enforced by the shift
            values defined above — not re-validated in code)
    Rule 2: Floor 5%, Cap 35% — enforced on every shift before normalization
    Rule 3: Adjusted Shift = Raw Shift × (1 - Current Weight / 100)
    """
    weights = {k: float(v) for k, v in baseline_weights.items()}
    log = []

    for tier_label, shifts in [("Tier 1", tier1_shifts),
                                ("Tier 2", tier2_shifts)]:
        if not shifts:
            continue

        # Positives first
        for det, raw in sorted(shifts.items(), key=lambda x: -x[1]):
            if raw <= 0:
                continue
            current = weights.get(det, 0.0)
            adjusted = raw * (1 - current / 100)
            new_val = min(max(current + adjusted, WEIGHT_FLOOR), WEIGHT_CAP)
            log.append({
                "tier": tier_label, "determinant": det,
                "raw_shift": raw, "adjusted_shift": round(adjusted, 3),
                "before": round(current, 3), "after": round(new_val, 3)
            })
            weights[det] = new_val

        # Negatives second
        for det, raw in sorted(shifts.items(), key=lambda x: x[1]):
            if raw >= 0:
                continue
            current = weights.get(det, 0.0)
            adjusted = raw * (1 - current / 100)
            new_val = min(max(current + adjusted, WEIGHT_FLOOR), WEIGHT_CAP)
            log.append({
                "tier": tier_label, "determinant": det,
                "raw_shift": raw, "adjusted_shift": round(adjusted, 3),
                "before": round(current, 3), "after": round(new_val, 3)
            })
            weights[det] = new_val

    # Proportional normalization — caps already enforced above, do not re-apply
    total = sum(weights.values())
    normalized = {
        k: round((v / total) * 100, 2)
        for k, v in weights.items()
    }

    return weights, normalized, log


def compute_country_weights(answers):
    objective = OBJECTIVE_ALIASES.get(answers.get("primary_objective", ""),
                                      answers.get("primary_objective", ""))
    risk = answers.get("risk_appetite", "moderate")
    t1 = COUNTRY_TIER1_SHIFTS.get(objective, {})
    t2 = COUNTRY_TIER2_SHIFTS.get(risk, {})
    return apply_shifts(COUNTRY_BASELINE_WEIGHTS, t1, t2)


def compute_city_weights(answers):
    objective = OBJECTIVE_ALIASES.get(answers.get("primary_objective", ""),
                                      answers.get("primary_objective", ""))
    risk = answers.get("risk_appetite", "moderate")
    t1 = CITY_TIER1_SHIFTS.get(objective, {})
    t2 = CITY_TIER2_SHIFTS.get(risk, {})
    return apply_shifts(CITY_BASELINE_WEIGHTS, t1, t2)


# ─── WINSORIZATION ────────────────────────────────────────

def winsorize(value, all_values, percentile=95):
    """
    Caps value at the 95th percentile of all_values.
    """
    if not all_values:
        return value
    sorted_vals = sorted(all_values)
    cap_idx = min(int(len(sorted_vals) * percentile / 100),
                  len(sorted_vals) - 1)
    return min(value, sorted_vals[cap_idx])


# Empty placeholder: some callers import this symbol for diagnostics.
CITY_QUESTION_DELTAS = {}


# ─── PROJECT BASELINE WEIGHTS (must sum to 100) ───────────

PROJECT_BASELINE_WEIGHTS = {
    "delivery_history": 18,
    "project_exit_liquidity": 16,
    "project_completion_rate": 15,
    "financial_strength": 15,
    "expected_rental_yield": 14,
    "public_infrastructure_proximity": 10,
    "construction_quality": 7,
    "litigation_history": 5,
}

# ─── PROJECT TIER 1 SHIFTS ────────────────────────────────

PROJECT_TIER1_USAGE_SHIFTS = {
    "pure_investment": {
        "expected_rental_yield": +8,
        "project_exit_liquidity": +7,
        "delivery_history": -6,
        "financial_strength": -5,
        "public_infrastructure_proximity": -4,
    },
    "investment_occasional_use": {
        "expected_rental_yield": +6,
        "construction_quality": +5,
        "public_infrastructure_proximity": +4,
        "project_exit_liquidity": -8,
        "financial_strength": -4,
        "delivery_history": -3,
    },
    "primary_relocation": {
        "construction_quality": +8,
        "public_infrastructure_proximity": +7,
        "expected_rental_yield": -8,
        "project_exit_liquidity": -4,
        "project_completion_rate": -3,
    },
}

PROJECT_TIER1_HOLDING_SHIFTS = {
    "short_term": {
        "project_completion_rate": +8,
        "project_exit_liquidity": +7,
        "expected_rental_yield": -8,
        "delivery_history": -4,
        "financial_strength": -3,
    },
    "medium_term": {
        "expected_rental_yield": +6,
        "project_exit_liquidity": +5,
        "project_completion_rate": +4,
        "delivery_history": -7,
        "financial_strength": -5,
        "public_infrastructure_proximity": -3,
    },
    "long_term": {
        "expected_rental_yield": +8,
        "construction_quality": +7,
        "project_exit_liquidity": -8,
        "project_completion_rate": -4,
        "public_infrastructure_proximity": -3,
    },
}

PROJECT_TIER1_LIQUIDITY_SHIFTS = {
    "high_resale": {
        "project_exit_liquidity": +10,
        "project_completion_rate": +5,
        "expected_rental_yield": -8,
        "financial_strength": -4,
        "delivery_history": -3,
    },
    "long_lockin": {
        "expected_rental_yield": +8,
        "financial_strength": +7,
        "project_exit_liquidity": -10,
        "project_completion_rate": -5,
    },
}

PROJECT_TIER1_RISK_SHIFTS = {
    "conservative": {
        "financial_strength": +6,
        "delivery_history": +5,
        "project_completion_rate": +2,
        "litigation_history": +2,
        "expected_rental_yield": -8,
        "project_exit_liquidity": -4,
        "public_infrastructure_proximity": -3,
    },
    "moderate": {},
    "opportunistic": {
        "expected_rental_yield": +8,
        "project_exit_liquidity": +7,
        "delivery_history": -8,
        "financial_strength": -4,
        "project_completion_rate": -3,
    },
}

# ─── PROJECT TIER 2 SHIFTS ────────────────────────────────

PROJECT_TIER2_EXPERIENCE_SHIFTS = {
    "first_time": {
        "delivery_history": +5,
        "project_completion_rate": +3,
        "litigation_history": +2,
        "expected_rental_yield": -6,
        "project_exit_liquidity": -4,
    },
    "experienced": {
        "expected_rental_yield": +6,
        "project_exit_liquidity": +4,
        "delivery_history": -6,
        "project_completion_rate": -4,
    },
}

PROJECT_TIER2_PRESTIGE_SHIFTS = {
    "high": {
        "construction_quality": +7,
        "delivery_history": +3,
        "expected_rental_yield": -6,
        "project_exit_liquidity": -4,
    },
    "medium": {},
    "low": {
        "expected_rental_yield": +6,
        "project_exit_liquidity": +4,
        "delivery_history": -6,
        "public_infrastructure_proximity": -4,
    },
}

PROJECT_TIER2_PROXIMITY_SHIFTS = {
    "airport_cbd_leisure": {
        "public_infrastructure_proximity": +7,
        "project_exit_liquidity": +3,
        "expected_rental_yield": -6,
        "delivery_history": -4,
    },
    "schools_hospitals": {
        "public_infrastructure_proximity": +8,
        "construction_quality": +2,
        "expected_rental_yield": -6,
        "project_exit_liquidity": -4,
    },
}

PROJECT_TIER2_FAMILY_SHIFTS = {
    "single_couple": {
        "project_exit_liquidity": +6,
        "expected_rental_yield": +4,
        "delivery_history": -5,
        "financial_strength": -5,
    },
    "family": {
        "public_infrastructure_proximity": +6,
        "construction_quality": +4,
        "project_exit_liquidity": -6,
        "expected_rental_yield": -4,
    },
}

# ─── SOURCE-GROUPED SHIFT FUNCTION ───────────────────────


def apply_shifts_with_sources(baseline_weights, tier1_sources, tier2_sources):
    """
    Applies shifts grouped by source question (list of (label, shifts_dict) tuples).
    Positives applied before negatives within each source group.
    Enforces WEIGHT_FLOOR / WEIGHT_CAP, then normalizes to 100.

    Returns: (weights, normalized, log)
    """
    weights = {k: float(v) for k, v in baseline_weights.items()}
    log = []

    for tier_label, sources in [("Tier 1", tier1_sources),
                                 ("Tier 2", tier2_sources)]:
        for source_label, shifts in sources:
            for det, raw in sorted(shifts.items(), key=lambda x: -x[1]):
                if raw <= 0:
                    continue
                current = weights.get(det, 0.0)
                adjusted = raw * (1 - current / 100)
                new_val = min(max(current + adjusted, WEIGHT_FLOOR), WEIGHT_CAP)
                log.append({
                    "source": source_label,
                    "tier": tier_label,
                    "determinant": det,
                    "raw_shift": raw,
                    "adjusted_shift": round(adjusted, 2),
                    "before": round(current, 2),
                    "after": round(new_val, 2),
                })
                weights[det] = new_val

            for det, raw in sorted(shifts.items(), key=lambda x: x[1]):
                if raw >= 0:
                    continue
                current = weights.get(det, 0.0)
                adjusted = raw * (1 - current / 100)
                new_val = min(max(current + adjusted, WEIGHT_FLOOR), WEIGHT_CAP)
                log.append({
                    "source": source_label,
                    "tier": tier_label,
                    "determinant": det,
                    "raw_shift": raw,
                    "adjusted_shift": round(adjusted, 2),
                    "before": round(current, 2),
                    "after": round(new_val, 2),
                })
                weights[det] = new_val

    total = sum(weights.values())
    normalized = {
        k: round((v / total) * 100, 2)
        for k, v in weights.items()
    }
    return weights, normalized, log


def compute_project_weights(answers):
    usage = answers.get("usage_intent", "")
    holding = answers.get("holding_period", "")
    liquidity = answers.get("liquidity_preference", "")
    risk = answers.get("risk_appetite", "moderate")
    experience = answers.get("investor_experience", "")
    prestige = answers.get("prestige_sensitivity", "medium")
    proximity = answers.get("proximity_preference", "")
    family = answers.get("family_composition", "")

    tier1_sources = []
    if usage in PROJECT_TIER1_USAGE_SHIFTS:
        tier1_sources.append((
            f"Usage Intent = {usage.replace('_', ' ').title()}",
            PROJECT_TIER1_USAGE_SHIFTS[usage],
        ))
    if holding in PROJECT_TIER1_HOLDING_SHIFTS:
        tier1_sources.append((
            f"Holding Period = {holding.replace('_', ' ').title()}",
            PROJECT_TIER1_HOLDING_SHIFTS[holding],
        ))
    if liquidity in PROJECT_TIER1_LIQUIDITY_SHIFTS:
        tier1_sources.append((
            f"Liquidity Preference = {liquidity.replace('_', ' ').title()}",
            PROJECT_TIER1_LIQUIDITY_SHIFTS[liquidity],
        ))
    if risk in PROJECT_TIER1_RISK_SHIFTS:
        tier1_sources.append((
            f"Risk Appetite = {risk.title()}",
            PROJECT_TIER1_RISK_SHIFTS[risk],
        ))

    tier2_sources = []
    if experience in PROJECT_TIER2_EXPERIENCE_SHIFTS:
        tier2_sources.append((
            f"Investor Experience = {experience.replace('_', ' ').title()}",
            PROJECT_TIER2_EXPERIENCE_SHIFTS[experience],
        ))
    if prestige in PROJECT_TIER2_PRESTIGE_SHIFTS and PROJECT_TIER2_PRESTIGE_SHIFTS[prestige]:
        tier2_sources.append((
            f"Prestige Sensitivity = {prestige.title()}",
            PROJECT_TIER2_PRESTIGE_SHIFTS[prestige],
        ))
    if proximity in PROJECT_TIER2_PROXIMITY_SHIFTS:
        tier2_sources.append((
            f"Proximity Preference = {proximity.replace('_', ' ').title()}",
            PROJECT_TIER2_PROXIMITY_SHIFTS[proximity],
        ))
    if family in PROJECT_TIER2_FAMILY_SHIFTS:
        tier2_sources.append((
            f"Family Composition = {family.replace('_', ' ').title()}",
            PROJECT_TIER2_FAMILY_SHIFTS[family],
        ))

    return apply_shifts_with_sources(
        PROJECT_BASELINE_WEIGHTS,
        tier1_sources,
        tier2_sources,
    )
