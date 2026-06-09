"""Shared determinant constants for the cascading archetype engines."""

WEIGHT_FLOOR = 5.0
WEIGHT_CAP = 35.0
TIER_1_MAX = 25
TIER_2_MAX = 15

COUNTRY_INVERSE_VARS = {
    "currency_volatility",
    "property_taxation_for_foreigners",
    "interest_rate_direction",
}

CITY_INVERSE_VARS = {
    "supply_pipeline",
    "vacancy_rate",
}

COUNTRY_BASELINE_WEIGHTS = {
    "political_stability_index": 25,
    "currency_volatility": 20,
    "property_taxation_for_foreigners": 18,
    "interest_rate_direction": 15,
    "foreign_buyer_market_share": 12,
    "corruption_perception_index": 10,
}

COUNTRY_TIER1_SHIFTS = {
    "capital_appreciation": {
        "property_taxation_for_foreigners": 17,
        "currency_volatility": 8,
        "political_stability_index": -17,
        "corruption_perception_index": -8,
    },
    "yield_cash_flow": {
        "property_taxation_for_foreigners": 13,
        "currency_volatility": 12,
        "political_stability_index": -17,
        "foreign_buyer_market_share": -8,
    },
    "capital_preservation": {
        "political_stability_index": 13,
        "foreign_buyer_market_share": 12,
        "property_taxation_for_foreigners": -17,
        "interest_rate_direction": -8,
    },
    "investment_diversification": {
        "political_stability_index": 13,
        "foreign_buyer_market_share": 12,
        "property_taxation_for_foreigners": -17,
        "interest_rate_direction": -8,
    },
    "residency_citizenship": {
        "political_stability_index": 17,
        "corruption_perception_index": 8,
        "property_taxation_for_foreigners": -17,
        "currency_volatility": -8,
    },
}

COUNTRY_TIER2_SHIFTS = {
    "conservative": {
        "foreign_buyer_market_share": 8,
        "political_stability_index": 7,
        "property_taxation_for_foreigners": -10,
        "interest_rate_direction": -5,
    },
    "moderate": {},
    "opportunistic": {
        "property_taxation_for_foreigners": 10,
        "currency_volatility": 5,
        "foreign_buyer_market_share": -10,
        "interest_rate_direction": -5,
    },
}

CITY_BASELINE_WEIGHTS = {
    "employment_growth":          12,
    "population_growth":          12,
    "price_appreciation_5y":      12,
    "rental_demand_index":        12,
    "macro_infra_pipeline":       10,
    "transaction_volume_growth":  10,
    "quality_of_life_index":      10,
    "tourism_strength":            8,
    "supply_pipeline":             7,
    "vacancy_rate":                7,
}

CITY_TIER1_SHIFTS = {
    "capital_appreciation": {
        "macro_infra_pipeline":      10,
        "price_appreciation_5y":      8,
        "population_growth":          7,
        "rental_demand_index":       -10,
        "transaction_volume_growth": -8,
        "quality_of_life_index":     -7,
    },
    "yield_cashflow": {
        "rental_demand_index":        10,
        "tourism_strength":            8,
        "employment_growth":           7,
        "price_appreciation_5y":     -12,
        "macro_infra_pipeline":       -8,
        "population_growth":          -5,
    },
    "capital_preservation": {
        "transaction_volume_growth":  10,
        "employment_growth":           8,
        "vacancy_rate":                7,
        "price_appreciation_5y":     -13,
        "macro_infra_pipeline":       -8,
        "tourism_strength":           -4,
    },
    "lifestyle": {
        "quality_of_life_index":      12,
        "tourism_strength":            8,
        "population_growth":           5,
        "rental_demand_index":        -13,
        "price_appreciation_5y":      -8,
        "transaction_volume_growth":  -4,
    },
    "residency": {
        "transaction_volume_growth":  12,
        "quality_of_life_index":       8,
        "employment_growth":           5,
        "rental_demand_index":        -12,
        "macro_infra_pipeline":       -8,
        "price_appreciation_5y":      -5,
    },
}

CITY_TIER2_SHIFTS = {
    "conservative": {
        "transaction_volume_growth":   6,
        "vacancy_rate":                5,
        "supply_pipeline":             4,
        "macro_infra_pipeline":       -8,
        "price_appreciation_5y":      -7,
    },
    "neutral": {},
    "opportunistic": {
        "macro_infra_pipeline":        8,
        "population_growth":           7,
        "transaction_volume_growth":  -8,
        "vacancy_rate":               -7,
    },
}

# AFTER — 13 new bucket keys
PROJECT_BASELINE_WEIGHTS = {
    "demand_and_liquidity":          12.25,
    "neighborhood_livability":        8.75,
    "demographic_economic_strength":  7.00,
    "supply_pressure_risk":           7.00,
    "delivery_track_record":         10.50,
    "financial_credibility":          7.50,
    "build_integrity":                7.50,
    "legal_and_governance":           4.50,
    "exit_liquidity":                  8.75,
    "comp_market_performance":         8.75,
    "projected_rental_yields":         7.00,
    "speculation_risk_score":          7.00,
    "infra_and_connectivity":          3.50,
}
