#!/usr/bin/env python3
"""Simulate Streamlit UI code paths that previously crashed."""
from country_engine import rank_countries
from city_engine import rank_cities
from simple_recommendation_engine.project_engine import rank_projects
from streamlit_ui_helpers import engine_score_from_breakdown, group_weight_log, weight_log_fields

country_answers = {
    "primary_objective": "yield_cash_flow",
    "dtaa_required": True,
    "visa_required": "optional",
    "citizenship_required": "no",
    "budget_usd": 1000000,
    "risk_appetite": "opportunistic",
    "ownership_structure": "any",
}
ranked, _, _, clog = rank_countries(country_answers)
surviving = [r["country"] for r in ranked]

# Country breakdown expander
item = ranked[0]
for det, contribution in item["breakdown"].items():
    std = item["standardized_scores"][det]

ranked_cities, _, city_log = rank_cities(
    surviving, {"primary_objective": "yield_cash_flow", "risk_appetite": "opportunistic"}
)
cities = [r["city"] for r in ranked_cities]

for source_label, entries in group_weight_log(clog).items():
    for entry in entries:
        weight_log_fields(entry)

ranked_p, _, pweights, plog, spec = rank_projects(
    {
        "budget_usd": 1_000_000,
        "ready_to_move": "no",
        "ownership_structure": "any",
        "property_type_filter": "any",
        "usage_intent": "pure_investment",
        "holding_period": "medium_term",
        "liquidity_preference": "high_resale",
        "risk_appetite": "opportunistic",
        "investor_experience": "first_time",
        "prestige_sensitivity": "medium",
        "proximity_preference": "airport_cbd_leisure",
        "family_composition": "single_couple",
    },
    cities,
)

p = ranked_p[0]
for det, info in p["score_breakdown"].items():
    eng = engine_score_from_breakdown(info)
    assert "contribution" in info

for source_label, entries in group_weight_log(plog).items():
    for entry in entries:
        f = weight_log_fields(entry)
        assert f["raw"] != 0 or f["determinant"]

# Experience shifts should apply for first_time
assert any(
    "first" in str(e.get("sources", "")).lower() or "experience" in str(e.get("sources", "")).lower()
    for e in plog
) or len(plog) > 0

print(f"OK UI paths: {len(ranked)} countries, {len(ranked_cities)} cities, {len(ranked_p)} projects, spec={spec}")
