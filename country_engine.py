# Data: V2 dataset (updated)
from simple_recommendation_engine.constants import COUNTRY_INVERSE_VARS
from simple_recommendation_engine.hard_constraints import apply_country_constraints
from simple_recommendation_engine.normalization import (
    standardize_determinants,
    weighted_score,
)
from weights_config import compute_country_weights

COUNTRIES = {
    "Greece": {
        "region": "Europe",
        "citizenship_available": True,
        "golden_visa_available": True,
        "dtaa_india": True,
        "foreign_freehold_allowed": True,
        "min_program_investment_usd": 250000,
        "scores": {
            "political_stability_index": 5.20,   # trend=0.10-0.11=-0.01 → adj=0.099 → (0.099+2.5)/5*10
            "corruption_perception_index": 5.0,   # 50/10
            "currency_volatility": 5.55,          # (15-6.67)/15*10
            "interest_rate_direction": 3.13,       # (2.00-1.25)/(3.65-1.25)*10
            "foreign_buyer_market_share": 2.30,   # 17.0/74*10
            "property_taxation_for_foreigners": 4.0,
        },
        "raw_values": {
            "political_stability_index_raw": 0.10,
            "political_stability_2022": 0.24,
            "political_stability_2021": 0.11,
            "corruption_perception_index_raw": 50,
            "currency_volatility_pct": 6.67,
            "interest_rate_direction_pp": 0.00,
            "interest_rate_direction_continuous": 2.0,
            "foreign_buyer_market_share_pct": 17.0,
            "tax_summary": "Annual Holding Tax ~0.1–1.2% ENFIA, Rental Income Tax 15–45%, Transaction Tax ~3%, Exit Tax 15%",
        },
    },
    "Portugal": {
        "region": "Europe",
        "citizenship_available": True,
        "golden_visa_available": True,
        "dtaa_india": True,
        "foreign_freehold_allowed": True,
        "min_program_investment_usd": 250000,
        "scores": {
            "political_stability_index": 5.94,   # trend=0.50-0.80=-0.30 → adj=0.47 → (0.47+2.5)/5*10
            "corruption_perception_index": 5.6,   # 56/10
            "currency_volatility": 5.55,          # (15-6.67)/15*10
            "interest_rate_direction": 3.13,       # (2.00-1.25)/(3.65-1.25)*10
            "foreign_buyer_market_share": 3.73,   # 27.6/74*10
            "property_taxation_for_foreigners": 5.0,
        },
        "raw_values": {
            "political_stability_index_raw": 0.50,
            "political_stability_2022": 0.71,
            "political_stability_2021": 0.80,
            "corruption_perception_index_raw": 56,
            "currency_volatility_pct": 6.67,
            "interest_rate_direction_pp": 0.00,
            "interest_rate_direction_continuous": 2.0,
            "foreign_buyer_market_share_pct": 27.6,
            "tax_summary": "Annual Holding Tax ~0.3–0.8%, Rental Income Tax 28%, Transaction Tax ~6–7.5%, Exit Tax 28%",
        },
    },
    "Thailand": {
        "region": "Asia",
        "citizenship_available": False,
        "golden_visa_available": True,
        "dtaa_india": True,
        "foreign_freehold_allowed": False,
        "min_program_investment_usd": 100000,
        "scores": {
            "political_stability_index": 3.54,   # trend=-0.70-(-0.39)=-0.31 → adj=-0.731 → (-0.731+2.5)/5*10
            "corruption_perception_index": 3.3,   # 33/10
            "currency_volatility": 4.60,          # (15-8.10)/15*10
            "interest_rate_direction": 0.0,       # (1.25-1.25)/(3.65-1.25)*10
            "foreign_buyer_market_share": 1.28,   # 9.5/74*10
            "property_taxation_for_foreigners": 6.0,
        },
        "raw_values": {
            "political_stability_index_raw": -0.70,
            "political_stability_2022": -0.28,
            "political_stability_2021": -0.39,
            "corruption_perception_index_raw": 33,
            "currency_volatility_pct": 8.10,
            "interest_rate_direction_pp": -0.75,
            "interest_rate_direction_continuous": 1.25,
            "foreign_buyer_market_share_pct": 9.5,
            "tax_summary": "Annual Holding Tax ~0.02–0.3%, Rental Income Tax up to 35%, Transaction Tax ~2–6%, Exit Tax depends on structure",
        },
    },
    "UAE": {
        "region": "Middle East",
        "citizenship_available": False,
        "golden_visa_available": True,
        "dtaa_india": True,
        "foreign_freehold_allowed": True,
        "min_program_investment_usd": 545000,
        "scores": {
            "political_stability_index": 6.61,   # trend=0.80-0.74=+0.06 → adj=0.806 → (0.806+2.5)/5*10
            "corruption_perception_index": 6.9,   # 69/10
            "currency_volatility": 10.0,          # (15-0.00)/15*10
            "interest_rate_direction": 10.0,      # (3.65-1.25)/(3.65-1.25)*10
            "foreign_buyer_market_share": 10.0,   # 74.0/74*10
            "property_taxation_for_foreigners": 10.0,
        },
        "raw_values": {
            "political_stability_index_raw": 0.80,
            "political_stability_2022": 0.68,
            "political_stability_2021": 0.74,
            "corruption_perception_index_raw": 69,
            "currency_volatility_pct": 0.00,
            "interest_rate_direction_pp": -0.75,
            "interest_rate_direction_continuous": 3.65,
            "foreign_buyer_market_share_pct": 74.0,
            "tax_summary": "Annual Holding Tax 0%, Rental Income Tax 0%, Transaction Tax ~4% transfer fee, Exit Tax 0%",
        },
    },
}


def apply_country_hard_filters(answers):
    """Apply country hard constraints before determinant scoring."""
    return apply_country_constraints(COUNTRIES, answers)


def score_country(country_name, normalized_weights, all_countries_data):
    """
    Score a country using z-score normalization and weighted scoring.

    Inverse determinants are oriented before z-scoring, then z values are
    winsorized to -2..+2 and converted using 50 + (z x 25).
    """
    data = COUNTRIES[country_name]
    peer_scores = [COUNTRIES[c]["scores"] for c in all_countries_data]
    standardized = standardize_determinants(
        data["scores"],
        peer_scores,
        normalized_weights.keys(),
        inverse_vars=COUNTRY_INVERSE_VARS,
    )
    score, breakdown = weighted_score(standardized, normalized_weights)
    return score, breakdown, standardized


def rank_countries(answers):
    """
    Full country pipeline:
    1. Apply hard filters
    2. Compute weights from answers
    3. Score and rank surviving countries
    Returns (ranked_list, eliminated, normalized_weights, weight_log)
    """
    surviving, eliminated = apply_country_hard_filters(answers)
    _, normalized_weights, weight_log = compute_country_weights(answers)

    ranked = []
    for country in surviving:
        score, breakdown, standardized = score_country(
            country, normalized_weights, surviving
        )
        ranked.append({
            "country": country,
            "score": score,
            "breakdown": breakdown,
            "standardized_scores": standardized,
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked, eliminated, normalized_weights, weight_log
