"""Shared determinant constants for the cascading archetype engines."""

WEIGHT_FLOOR = 5.0
WEIGHT_CAP = 35.0
TIER_1_MAX = 25
TIER_2_MAX = 15

COUNTRY_INVERSE_VARS = {
    "currency_volatility",
    "property_taxation_for_foreigners",
    "interest_rate_direction",
    "corruption_perception_index",
}

CITY_INVERSE_VARS = {"supply_pipeline"}

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
        "foreign_buyer_market_share": 17,
        "interest_rate_direction": 8,
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
        "currency_volatility": 12,
        "foreign_buyer_market_share": -17,
        "interest_rate_direction": -8,
    },
    "investment_diversification": {
        "political_stability_index": 9,
        "currency_volatility": 8,
        "foreign_buyer_market_share": 8,
        "interest_rate_direction": -17,
        "corruption_perception_index": -8,
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
        "political_stability_index": 11,
        "currency_volatility": 4,
        "foreign_buyer_market_share": -11,
        "interest_rate_direction": -4,
    },
    "moderate": {},
    "opportunistic": {
        "foreign_buyer_market_share": 11,
        "interest_rate_direction": 4,
        "political_stability_index": -11,
        "currency_volatility": -4,
    },
}

CITY_BASELINE_WEIGHTS = {
    "employment_growth": 15,
    "price_appreciation_5y": 15,
    "net_migration_rate": 14,
    "rental_demand_index": 14,
    "infrastructure_pipeline": 12,
    "liquidity_indicator": 10,
    "quality_of_life_index": 10,
    "tourism_strength": 5,
    "supply_pipeline": 5,
}

CITY_TIER1_SHIFTS = {
    "capital_appreciation": {
        "infrastructure_pipeline": 12,
        "price_appreciation_5y": 8,
        "net_migration_rate": 5,
        "rental_demand_index": -13,
        "liquidity_indicator": -7,
        "quality_of_life_index": -5,
    },
    "yield_cash_flow": {
        "rental_demand_index": 13,
        "tourism_strength": 9,
        "employment_growth": 3,
        "price_appreciation_5y": -13,
        "infrastructure_pipeline": -12,
    },
    "capital_preservation": {
        "liquidity_indicator": 13,
        "employment_growth": 9,
        "supply_pipeline": 3,
        "price_appreciation_5y": -15,
        "infrastructure_pipeline": -10,
    },
    "investment_diversification": {
        "liquidity_indicator": 13,
        "employment_growth": 9,
        "supply_pipeline": 3,
        "price_appreciation_5y": -15,
        "infrastructure_pipeline": -10,
    },
    "lifestyle_end_use": {
        "quality_of_life_index": 17,
        "tourism_strength": 8,
        "rental_demand_index": -17,
        "price_appreciation_5y": -8,
    },
    "residency_citizenship": {
        "liquidity_indicator": 13,
        "quality_of_life_index": 12,
        "rental_demand_index": -13,
        "infrastructure_pipeline": -7,
        "price_appreciation_5y": -5,
    },
}

CITY_TIER2_SHIFTS = {
    "conservative": {
        "liquidity_indicator": 8,
        "employment_growth": 5,
        "supply_pipeline": 2,
        "infrastructure_pipeline": -9,
        "price_appreciation_5y": -6,
    },
    "moderate": {},
    "opportunistic": {
        "infrastructure_pipeline": 9,
        "net_migration_rate": 6,
        "liquidity_indicator": -9,
        "quality_of_life_index": -6,
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
