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
            "political_stability_index":        0.10,   # raw WGI 2023
            "corruption_perception_index":      50,     # raw CPI score
            "currency_volatility":              6.67,   # raw % — inverse var
            "interest_rate_direction":          2.15,    # raw continuous rate
            "foreign_buyer_market_share":       35.0,   # raw %
            "property_taxation_for_foreigners": 5.35,    # manual score — no raw equivalent
        },
        "raw_values": {
            "political_stability_index_raw": 0.10,
            "political_stability_2022": 0.24,
            "political_stability_2021": 0.11,
            "corruption_perception_index_raw": 50,
            "currency_volatility_pct": 6.67,
            "interest_rate_direction_pp": 2.15,
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
            "political_stability_index":        0.50,
            "corruption_perception_index":      56,
            "currency_volatility":              6.67,
            "interest_rate_direction":          2.15,
            "foreign_buyer_market_share":       45.75,
            "property_taxation_for_foreigners": 6.04,
        },
        "raw_values": {
            "political_stability_index_raw": 0.50,
            "political_stability_2022": 0.71,
            "political_stability_2021": 0.80,
            "corruption_perception_index_raw": 56,
            "currency_volatility_pct": 6.67,
            "interest_rate_direction_pp": 2.15,
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
            "political_stability_index":        -0.70,
            "corruption_perception_index":      33,
            "currency_volatility":              8.10,
            "interest_rate_direction":          1.00,
            "foreign_buyer_market_share":       27.5,
            "property_taxation_for_foreigners": 5.85,
        },
        "raw_values": {
            "political_stability_index_raw": -0.70,
            "political_stability_2022": -0.28,
            "political_stability_2021": -0.39,
            "corruption_perception_index_raw": 33,
            "currency_volatility_pct": 8.10,
            "interest_rate_direction_pp": 1.00,
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
            "political_stability_index":        0.80,
            "corruption_perception_index":      69,
            "currency_volatility":              0.00,
            "interest_rate_direction":          3.65,
            "foreign_buyer_market_share":       8.25    ,
            "property_taxation_for_foreigners": 0.00,
        },  
        "raw_values": {
            "political_stability_index_raw": 0.80,
            "political_stability_2022": 0.68,
            "political_stability_2021": 0.74,
            "corruption_perception_index_raw": 69,
            "currency_volatility_pct": 0.00,
            "interest_rate_direction_pp": 3.65,
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
        passthrough_vars={"foreign_buyer_market_share"},
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
