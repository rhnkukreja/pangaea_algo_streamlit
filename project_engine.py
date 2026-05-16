# =========================================================
# PROJECT ENGINE
# Cascading Archetype Model
# =========================================================

PROJECTS = {

    "Palm Residences": {

        "country": "UAE",
        "city": "Dubai",

        "price": 850000,
        "status": "ready",
        "ownership": "freehold",
        "property_type": "Apartment",

        "scores": {
            "delivery_history": 9,
            "project_exit_liquidity": 8,
            "project_completion_rate": 9,
            "financial_strength": 8,
            "expected_rental_yield": 7,
            "public_infrastructure_proximity": 9,
            "construction_quality": 9,
            "litigation_history": 9,
        },
    },

    "Marina Heights": {

        "country": "UAE",
        "city": "Dubai",

        "price": 650000,
        "status": "offplan",
        "ownership": "freehold",
        "property_type": "Apartment",

        "scores": {
            "delivery_history": 8,
            "project_exit_liquidity": 9,
            "project_completion_rate": 8,
            "financial_strength": 8,
            "expected_rental_yield": 9,
            "public_infrastructure_proximity": 10,
            "construction_quality": 8,
            "litigation_history": 8,
        },
    },

    "Lisbon Grand Park": {

        "country": "Portugal",
        "city": "Lisbon",

        "price": 1200000,
        "status": "ready",
        "ownership": "freehold",
        "property_type": "Villa",

        "scores": {
            "delivery_history": 9,
            "project_exit_liquidity": 7,
            "project_completion_rate": 8,
            "financial_strength": 9,
            "expected_rental_yield": 6,
            "public_infrastructure_proximity": 9,
            "construction_quality": 9,
            "litigation_history": 9,
        },
    },

    "Bangkok Riverside": {

        "country": "Thailand",
        "city": "Bangkok",

        "price": 450000,
        "status": "offplan",
        "ownership": "leasehold",
        "property_type": "Managed",

        "scores": {
            "delivery_history": 7,
            "project_exit_liquidity": 8,
            "project_completion_rate": 7,
            "financial_strength": 7,
            "expected_rental_yield": 9,
            "public_infrastructure_proximity": 8,
            "construction_quality": 7,
            "litigation_history": 8,
        },
    },
}

# =========================================================
# BASELINE WEIGHTS
# =========================================================

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

# =========================================================
# TIER 1 SHIFT TABLES
# =========================================================

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
    "opportunistic": {
        "expected_rental_yield": +8,
        "project_exit_liquidity": +7,
        "delivery_history": -8,
        "financial_strength": -4,
        "project_completion_rate": -3,
    },
}

# =========================================================
# TIER 2 SHIFT TABLES
# =========================================================

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
    "low": {
        "expected_rental_yield": +6,
        "project_exit_liquidity": +4,
        "delivery_history": -6,
        "public_infrastructure_proximity": -4,
    },
    "medium": {},
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

# =========================================================
# WEIGHT_FLOOR / WEIGHT_CAP
# =========================================================

WEIGHT_FLOOR = 5.0
WEIGHT_CAP = 35.0

# =========================================================
# SHIFT FUNCTION (source-grouped)
# =========================================================

def apply_shifts_with_sources(
    baseline_weights,
    tier1_sources,
    tier2_sources,
):
    weights = {k: float(v) for k, v in baseline_weights.items()}
    log = []

    for tier_label, sources in [
        ("Tier 1", tier1_sources),
        ("Tier 2", tier2_sources),
    ]:
        for source_label, shifts in sources:
            for det, raw in sorted(
                shifts.items(), key=lambda x: -x[1]
            ):
                if raw <= 0:
                    continue
                current = weights.get(det, 0.0)
                adjusted = raw * (1 - current / 100)
                new_val = min(
                    max(current + adjusted, WEIGHT_FLOOR),
                    WEIGHT_CAP,
                )
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

            for det, raw in sorted(
                shifts.items(), key=lambda x: x[1]
            ):
                if raw >= 0:
                    continue
                current = weights.get(det, 0.0)
                adjusted = raw * (1 - current / 100)
                new_val = min(
                    max(current + adjusted, WEIGHT_FLOOR),
                    WEIGHT_CAP,
                )
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


# =========================================================
# WEIGHT ENGINE
# =========================================================

def compute_project_weights(answers):

    usage = answers.get("usage_intent", "")
    holding = answers.get("holding_period", "")
    liquidity = answers.get("liquidity_preference", "")
    risk = answers.get("risk_appetite", "")

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

    experience = answers.get("investor_experience", "")
    prestige = answers.get("prestige_sensitivity", "medium")
    proximity = answers.get("proximity_preference", "")
    family = answers.get("family_composition", "")

    tier2_sources = []

    if experience in PROJECT_TIER2_EXPERIENCE_SHIFTS:
        tier2_sources.append((
            f"Investor Experience = {experience.replace('_', ' ').title()}",
            PROJECT_TIER2_EXPERIENCE_SHIFTS[experience],
        ))

    if prestige in PROJECT_TIER2_PRESTIGE_SHIFTS:
        shifts = PROJECT_TIER2_PRESTIGE_SHIFTS[prestige]
        if shifts:
            tier2_sources.append((
                f"Prestige Sensitivity = {prestige.title()}",
                shifts,
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

    _, normalized_weights, weight_log = apply_shifts_with_sources(
        PROJECT_BASELINE_WEIGHTS,
        tier1_sources,
        tier2_sources,
    )

    return normalized_weights, weight_log


# =========================================================
# PROJECT RANKING ENGINE
# =========================================================

def rank_projects(
    surviving_countries,
    answers,
):

    normalized_weights, weight_log = (
        compute_project_weights(answers)
    )

    ranked = []

    eliminated = []

    # =====================================================
    # HARD FILTERS
    # =====================================================

    for project_name, project_data in PROJECTS.items():

        if (
            project_data["country"]
            not in surviving_countries
        ):
            continue

        # -------------------------------------------------
        # Budget Filter
        # -------------------------------------------------

        budget_limit = answers["budget"] * 1.2

        if project_data["price"] > budget_limit:

            eliminated.append({
                "project": project_name,
                "reason": "Budget exceeded",
            })

            continue

        # -------------------------------------------------
        # Status Filter
        # -------------------------------------------------

        if (
            answers["ready_to_move"] == "yes"
            and project_data["status"] != "ready"
        ):

            eliminated.append({
                "project": project_name,
                "reason": "Not ready to move",
            })

            continue

        # -------------------------------------------------
        # Ownership Filter
        # -------------------------------------------------

        if (
            answers["ownership_required"]
            == "freehold"
            and project_data["ownership"]
            != "freehold"
        ):

            eliminated.append({
                "project": project_name,
                "reason": "Leasehold property",
            })

            continue

        # -------------------------------------------------
        # Property Type Filter
        # -------------------------------------------------

        if (
            project_data["property_type"]
            != answers["property_type"]
        ):

            eliminated.append({
                "project": project_name,
                "reason": "Property type mismatch",
            })

            continue

        # =================================================
        # SCORING
        # =================================================

        total_score = 0

        breakdown = {}

        for determinant, weight in normalized_weights.items():

            raw_score = (
                project_data["scores"][determinant]
            )

            contribution = round(
                raw_score * (weight / 10),
                2,
            )

            breakdown[determinant] = contribution

            total_score += contribution

        ranked.append({

            "project": project_name,

            "country": project_data["country"],

            "city": project_data["city"],

            "score": round(total_score, 1),

            "breakdown": breakdown,
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    return (
        ranked,
        eliminated,
        normalized_weights,
        weight_log,
    )