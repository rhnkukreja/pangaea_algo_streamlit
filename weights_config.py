"""Dynamic determinant weights for country, city, and project engines."""

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


PROJECT_TIER1_USAGE_SHIFTS = {
    "pure_investment": {
        "expected_rental_yield": 13,
        "project_exit_liquidity": 12,
        "delivery_history": -10,
        "financial_strength": -8,
        "public_infrastructure_proximity": -7,
    },
    "investment_occasional_use": {
        "expected_rental_yield": 10,
        "construction_quality": 8,
        "public_infrastructure_proximity": 7,
        "project_exit_liquidity": -13,
        "financial_strength": -7,
        "delivery_history": -5,
    },
    "primary_relocation": {
        "construction_quality": 13,
        "public_infrastructure_proximity": 12,
        "expected_rental_yield": -13,
        "project_exit_liquidity": -7,
        "project_completion_rate": -5,
    },
}

PROJECT_TIER1_HOLDING_SHIFTS = {
    "short_term": {
        "project_completion_rate": 13,
        "project_exit_liquidity": 12,
        "expected_rental_yield": -13,
        "delivery_history": -7,
        "financial_strength": -5,
    },
    "medium_term": {
        "expected_rental_yield": 10,
        "project_exit_liquidity": 8,
        "project_completion_rate": 7,
        "delivery_history": -12,
        "financial_strength": -8,
        "public_infrastructure_proximity": -5,
    },
    "long_term": {
        "expected_rental_yield": 13,
        "construction_quality": 12,
        "project_exit_liquidity": -13,
        "project_completion_rate": -7,
        "public_infrastructure_proximity": -5,
    },
}

PROJECT_TIER1_LIQUIDITY_SHIFTS = {
    "high_resale": {
        "project_exit_liquidity": 17,
        "project_completion_rate": 8,
        "expected_rental_yield": -13,
        "financial_strength": -7,
        "delivery_history": -5,
    },
    "long_lockin": {
        "expected_rental_yield": 13,
        "financial_strength": 12,
        "project_exit_liquidity": -17,
        "project_completion_rate": -8,
    },
}

PROJECT_TIER1_RISK_SHIFTS = {
    "conservative": {
        "financial_strength": 10,
        "delivery_history": 8,
        "project_completion_rate": 4,
        "litigation_history": 3,
        "expected_rental_yield": -13,
        "project_exit_liquidity": -7,
        "public_infrastructure_proximity": -5,
    },
    "moderate": {},
    "opportunistic": {
        "expected_rental_yield": 13,
        "project_exit_liquidity": 12,
        "delivery_history": -13,
        "financial_strength": -7,
        "project_completion_rate": -5,
    },
}

PROJECT_TIER2_EXPERIENCE_SHIFTS = {
    "first_time": {
        "delivery_history": 8,
        "project_completion_rate": 5,
        "litigation_history": 2,
        "expected_rental_yield": -9,
        "project_exit_liquidity": -6,
    },
    "experienced": {
        "expected_rental_yield": 9,
        "project_exit_liquidity": 6,
        "delivery_history": -9,
        "project_completion_rate": -6,
    },
}

PROJECT_TIER2_PRESTIGE_SHIFTS = {
    "high": {
        "construction_quality": 11,
        "delivery_history": 4,
        "expected_rental_yield": -9,
        "project_exit_liquidity": -6,
    },
    "medium": {},
    "low": {
        "expected_rental_yield": 9,
        "project_exit_liquidity": 6,
        "delivery_history": -9,
        "public_infrastructure_proximity": -6,
    },
}

PROJECT_TIER2_PROXIMITY_SHIFTS = {
    "airport_cbd_leisure": {
        "public_infrastructure_proximity": 11,
        "project_exit_liquidity": 4,
        "expected_rental_yield": -9,
        "delivery_history": -6,
    },
    "schools_hospitals": {
        "public_infrastructure_proximity": 12,
        "construction_quality": 3,
        "expected_rental_yield": -9,
        "project_exit_liquidity": -6,
    },
}

PROJECT_TIER2_FAMILY_SHIFTS = {
    "single_couple": {
        "project_exit_liquidity": 9,
        "expected_rental_yield": 6,
        "delivery_history": -8,
        "financial_strength": -7,
    },
    "family": {
        "public_infrastructure_proximity": 9,
        "construction_quality": 6,
        "project_exit_liquidity": -9,
        "expected_rental_yield": -6,
    },
}


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
    """Compute cascading city weights from objective and risk archetypes."""
    objective = canonical_objective(answers.get("primary_objective"))
    risk = answers.get("risk_appetite", "moderate")
    return apply_shifts(
        CITY_BASELINE_WEIGHTS,
        CITY_TIER1_SHIFTS.get(objective, {}),
        CITY_TIER2_SHIFTS.get(risk, {}),
    )


def compute_project_weights(answers):
    """Compute project weights from risk, usage, liquidity, and family mappings."""
    usage = answers.get("usage_intent", "")
    holding = answers.get("holding_period", "")
    liquidity = answers.get("liquidity_preference", "")
    risk = answers.get("risk_appetite", "moderate")
    experience = answers.get("investor_experience", "")
    prestige = answers.get("prestige_sensitivity", "medium")
    proximity = answers.get("proximity_preference", "")
    family = answers.get("family_composition", "")

    sources = [
        ("Tier 1", f"Usage Intent = {usage.replace('_', ' ').title()}", PROJECT_TIER1_USAGE_SHIFTS.get(usage, {})),
        ("Tier 1", f"Holding Period = {holding.replace('_', ' ').title()}", PROJECT_TIER1_HOLDING_SHIFTS.get(holding, {})),
        ("Tier 1", f"Liquidity Preference = {liquidity.replace('_', ' ').title()}", PROJECT_TIER1_LIQUIDITY_SHIFTS.get(liquidity, {})),
        ("Tier 1", f"Risk Appetite = {risk.title()}", PROJECT_TIER1_RISK_SHIFTS.get(risk, {})),
        ("Tier 2", f"Investor Experience = {experience.replace('_', ' ').title()}", PROJECT_TIER2_EXPERIENCE_SHIFTS.get(experience, {})),
        ("Tier 2", f"Prestige Sensitivity = {prestige.title()}", PROJECT_TIER2_PRESTIGE_SHIFTS.get(prestige, {})),
        ("Tier 2", f"Proximity Preference = {proximity.replace('_', ' ').title()}", PROJECT_TIER2_PROXIMITY_SHIFTS.get(proximity, {})),
        ("Tier 2", f"Family Composition = {family.replace('_', ' ').title()}", PROJECT_TIER2_FAMILY_SHIFTS.get(family, {})),
    ]
    return apply_shifts_with_sources(PROJECT_BASELINE_WEIGHTS, sources)


# Empty placeholder: some callers import this symbol for diagnostics.
CITY_QUESTION_DELTAS = {}
