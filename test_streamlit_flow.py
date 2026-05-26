#!/usr/bin/env python3
"""End-to-end smoke test for Country -> City -> Project flow."""
from __future__ import annotations

import traceback

errors: list[str] = []


def check(name: str, fn):
    try:
        fn()
        print(f"[OK] {name}")
    except Exception as e:
        errors.append(f"{name}: {e}")
        print(f"[FAIL] {name}: {e}")
        traceback.print_exc()


# ── Country ───────────────────────────────────────────────────────────────────
country_answers = {
    "primary_objective": "yield_cash_flow",
    "dtaa_required": True,
    "visa_required": "optional",
    "citizenship_required": "no",
    "budget_usd": 1000000,
    "risk_appetite": "opportunistic",
    "ownership_structure": "any",
}

ranked_countries = []
surviving_countries = []


def test_country():
    global ranked_countries, surviving_countries
    from country_engine import rank_countries

    ranked, elim, weights, log = rank_countries(country_answers)
    assert ranked, "no countries ranked"
    surviving_countries = [r["country"] for r in ranked]
    for r in ranked:
        assert "standardized_scores" in r
        assert 0 <= r["score"] <= 100
        for det, std in r["standardized_scores"].items():
            assert 0 <= std <= 100, f"{r['country']}.{det}={std}"
    ranked_countries = ranked
    print(f"     countries: {surviving_countries}, log entries: {len(log)}")
    if log:
        print(f"     log keys sample: {list(log[0].keys())}")


# ── City ──────────────────────────────────────────────────────────────────────
ranked_cities = []
surviving_cities = []


def test_city():
    global ranked_cities, surviving_cities
    from city_engine import rank_cities

    city_answers = {
        "primary_objective": "yield_cash_flow",
        "risk_appetite": "opportunistic",
    }
    ranked, weights, log = rank_cities(surviving_countries, city_answers)
    assert ranked, "no cities ranked"
    surviving_cities = [r["city"] for r in ranked]
    for r in ranked:
        assert "standardized_scores" in r
        assert 0 <= r["score"] <= 100
    ranked_cities = ranked
    print(f"     cities: {surviving_cities[:6]}..., log entries: {len(log)}")


# ── Project ───────────────────────────────────────────────────────────────────
def test_project():
    from simple_recommendation_engine.project_engine import rank_projects
    from projects_data import PROJECTS, list_determinant_keys
    from project_rollup import rollup_project

    project_answers = {
        "budget_usd": 1_000_000,
        "ready_to_move": "no",
        "ownership_structure": "any",
        "property_type_filter": "any",
        "usage_intent": "pure_investment",
        "holding_period": "medium_term",
        "liquidity_preference": "high_resale",
        "risk_appetite": "opportunistic",
        "investor_experience": "first_time",  # streamlit value
        "prestige_sensitivity": "medium",
        "proximity_preference": "airport_cbd_leisure",
        "family_composition": "single_couple",
    }

    result = rank_projects(project_answers, surviving_cities)
    assert len(result) == 5, f"expected 5 return values, got {len(result)}"
    ranked, elim, weights, log, spec_tag = result
    print(f"     ranked: {len(ranked)}, eliminated: {len(elim)}, spec_tag: {spec_tag}")
    print(f"     weight keys: {len(weights)}")

    all_vars = list_determinant_keys()
    for key, proj in list(PROJECTS.items())[:1]:
        rv = proj["raw_variables"]
        present = sum(1 for v in all_vars if rv.get(v) is not None)
        print(f"     sample {key}: {present}/{len(all_vars)} raw vars present")

    if ranked:
        p = ranked[0]
        bd = p["score_breakdown"]
        info = next(iter(bd.values()))
        print(f"     breakdown keys: {list(info.keys())}")
        # Simulate streamlit expander
        _ = info["contribution"]
        _ = info["engine_score"]  # was wrongly 'standardized'
        _ = info["weight_pct"]

        contrib_sum = sum(b["contribution"] for b in bd.values())
        assert abs(contrib_sum - p["project_score"]) < 0.1

    # Simulate weight log expander keys used in Home.py
    if log:
        entry = log[0]
        for k in ("raw_shift", "before", "after"):
            if k not in entry:
                print(f"     WARNING: weight_log missing '{k}', has {list(entry.keys())}")


def test_streamlit_imports():
    import importlib.util
    from pathlib import Path
    root = Path(__file__).parent
    for rel in [
        "streamlit_app/Home.py",
        "streamlit_app/pages/1_Country_Filtering.py",
        "streamlit_app/pages/2_City_Filtering.py",
        "streamlit_app/pages/3_Project_Engine_mapping.py",
    ]:
        path = root / rel
        source = path.read_text(encoding="utf-8")
        compile(source, str(path), "exec")


if __name__ == "__main__":
    print("=== Streamlit flow smoke test ===\n")
    check("imports compile", test_streamlit_imports)
    check("country engine (z-score)", test_country)
    check("city engine (z-score)", test_city)
    check("project engine (27 vars -> buckets -> z-score)", test_project)

    print()
    if errors:
        print(f"FAILED: {len(errors)} error(s)")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)
    print("All checks passed.")
