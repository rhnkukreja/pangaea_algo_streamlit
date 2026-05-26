#!/usr/bin/env python3
"""Audit sanity checks for the recommendation engine (run once, delete if desired)."""
from __future__ import annotations

import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from simple_recommendation_engine.normalization import standardize_determinants
from simple_recommendation_engine.archetype_mapper import apply_shifts_with_sources
from weights_config import compute_project_weights, resolve_speculation_tag
from project_rollup import BUCKET_VARIABLE_MAP, rollup_bucket
from simple_recommendation_engine.project_engine import rank_projects

TOL = 0.1
FAILURES: list[str] = []
PASSED: list[str] = []


def check(name: str, cond: bool, detail: str = ""):
    if cond:
        PASSED.append(name + (f" — {detail}" if detail else ""))
    else:
        FAILURES.append(name + (f"\n    {detail}" if detail else ""))


# ── A) PSI z-score test ─────────────────────────────────────────────────────
countries = {
    "Greece": 5.20,
    "Portugal": 5.80,
    "Thailand": 3.40,
    "UAE": 6.80,
}
expected_psi = {
    "Greece": 47.98,
    "Portugal": 60.11,
    "Thailand": 11.60,
    "UAE": 80.32,
}
peer_scores = [{ "political_stability_index": v } for v in countries.values()]
for name, raw in countries.items():
    scores = {"political_stability_index": raw}
    out = standardize_determinants(
        scores, peer_scores, ["political_stability_index"], set()
    )["political_stability_index"]
    exp = expected_psi[name]
    check(
        f"A) PSI {name}",
        abs(out - exp) <= TOL,
        f"got {out:.2f}, expected {exp:.2f}",
    )

# ── B) Inverse var test ─────────────────────────────────────────────────────
cv_countries = {
    "Greece": 5.55,
    "Portugal": 5.55,
    "Thailand": 4.60,
    "UAE": 10.0,
}
cv_peers = [{"currency_volatility": v} for v in cv_countries.values()]
uae_out = standardize_determinants(
    {"currency_volatility": 10.0},
    cv_peers,
    ["currency_volatility"],
    {"currency_volatility"},
)["currency_volatility"]
check(
    "B) Inverse UAE currency_volatility",
    abs(uae_out - 92.56) <= TOL,
    f"got {uae_out:.2f}, expected ~92.56 (7.44 would be double-inversion)",
)

# ── C) Order-independence ───────────────────────────────────────────────────
baseline = {"a": 50.0, "b": 50.0}
order1 = [
    ("T1", "s1", {"a": 20}),
    ("T1", "s2", {"a": -10, "b": 15}),
    ("T2", "s3", {"b": -5}),
]
order2 = [
    ("T2", "s3", {"b": -5}),
    ("T1", "s2", {"a": -10, "b": 15}),
    ("T1", "s1", {"a": 20}),
]
_, norm1, _ = apply_shifts_with_sources(baseline, order1)
_, norm2, _ = apply_shifts_with_sources(baseline, order2)
check(
    "C) Order independence",
    norm1 == norm2,
    f"order1={norm1}, order2={norm2}",
)

# ── D) Weight bounds ────────────────────────────────────────────────────────
for label, answers, expect_tag in [
    (
        "pure_investment+opportunistic",
        {
            "usage_intent": "pure_investment",
            "risk_appetite": "opportunistic",
            "holding_period": "medium_term",
            "liquidity_preference": "high_resale",
            "family_composition": "single_couple",
            "proximity_preference": "airport_cbd_leisure",
            "prestige_sensitivity": "medium",
            "investor_experience": "experienced_international",
        },
        "standard",
    ),
    (
        "primary_relocation+conservative",
        {
            "usage_intent": "primary_relocation",
            "risk_appetite": "conservative",
            "holding_period": "long_term",
            "liquidity_preference": "long_lockin",
            "family_composition": "family",
            "proximity_preference": "schools_hospitals",
            "prestige_sensitivity": "high",
            "investor_experience": "first_international",
        },
        "inverse",
    ),
]:
    _, norm, _, tag = compute_project_weights(answers)
    s = sum(norm.values())
    mn, mx = min(norm.values()), max(norm.values())
    check(
        f"D) {label} sum==100",
        abs(s - 100) < 0.02,
        f"sum={s}",
    )
    check(
        f"D) {label} floor>=2",
        mn >= 2.0 - 0.01,
        f"min={mn}",
    )
    check(
        f"D) {label} cap<=30",
        mx <= 30.0 + 0.01,
        f"max={mx}",
    )
    check(
        f"D) {label} speculation_tag",
        tag == expect_tag,
        f"got {tag}, expected {expect_tag}",
    )

# ── E) Bucket internal weights ──────────────────────────────────────────────
for bucket, vars_map in BUCKET_VARIABLE_MAP.items():
    total = sum(vars_map.values())
    check(
        f"E) {bucket} weights sum 100",
        abs(total - 100.0) < 0.001,
        f"sum={total}",
    )

# ── F) Partial missing rollup ─────────────────────────────────────────────────
score, dbg = rollup_bucket(
    "demand_and_liquidity",
    {"micro_market_stage": 100},
)
check(
    "F) Partial missing demand_and_liquidity",
    abs(score - 100.0) < 0.01,
    f"got {score}, status={dbg.get('status')}",
)

# ── G) Full pipeline integration ────────────────────────────────────────────
MOCK_PROJECTS = {
    "good": {
        "project_name": "Alpha Tower",
        "country": "UAE",
        "city": "Dubai",
        "price_range": "$500K",
        "project_stage": "Ready",
        "ownership": "freehold",
        "project_type": "Apartment",
        "raw_variables": {
            "micro_market_stage": 90,
            "rental_absorption_velocity": 85,
            "resale_velocity": 88,
            "safety_crime_index": 92,
            "population_growth_rate": 80,
            "immediate_pipeline_risk": 15,
            "average_delay_duration": 10,
            "pct_projects_delivered": 95,
            "escrow_quality": 90,
            "construction_quality": 88,
            "litigation_history": 5,
            "average_exit_velocity": 85,
            "comp_capital_appreciation": 90,
            "projected_rental_yield": 82,
            "str_concentration": 70,
            "infrastructure_proximity": 88,
        },
    },
    "mid": {
        "project_name": "Beta Residences",
        "country": "UAE",
        "city": "Dubai",
        "price_range": "$400K",
        "project_stage": "Ready",
        "ownership": "freehold",
        "project_type": "Apartment",
        "raw_variables": {
            "micro_market_stage": 60,
            "rental_absorption_velocity": 55,
            "resale_velocity": 58,
            "safety_crime_index": 65,
            "population_growth_rate": 55,
            "immediate_pipeline_risk": 40,
            "average_delay_duration": 35,
            "pct_projects_delivered": 70,
            "escrow_quality": 65,
            "construction_quality": 62,
            "litigation_history": 25,
            "average_exit_velocity": 60,
            "comp_capital_appreciation": 58,
            "projected_rental_yield": 55,
            "str_concentration": 50,
            "infrastructure_proximity": 60,
        },
    },
    "weak": {
        "project_name": "Gamma Court",
        "country": "UAE",
        "city": "Dubai",
        "price_range": "$300K",
        "project_stage": "Ready",
        "ownership": "freehold",
        "project_type": "Apartment",
        "raw_variables": {
            "micro_market_stage": 35,
            "rental_absorption_velocity": 30,
            "resale_velocity": 32,
            "safety_crime_index": 40,
            "population_growth_rate": 38,
            "immediate_pipeline_risk": 75,
            "average_delay_duration": 80,
            "pct_projects_delivered": 45,
            "escrow_quality": 40,
            "construction_quality": 38,
            "litigation_history": 70,
            "average_exit_velocity": 35,
            "comp_capital_appreciation": 32,
            "projected_rental_yield": 30,
            "str_concentration": 85,
            "infrastructure_proximity": 35,
        },
    },
}

# Patch PROJECTS for isolated test
import simple_recommendation_engine.project_engine as pe

_orig_projects = pe.PROJECTS
pe.PROJECTS = MOCK_PROJECTS

try:
    opp_answers = {
        "budget_usd": 0,
        "usage_intent": "pure_investment",
        "risk_appetite": "opportunistic",
        "holding_period": "medium_term",
        "liquidity_preference": "high_resale",
        "family_composition": "single_couple",
        "proximity_preference": "airport_cbd_leisure",
        "prestige_sensitivity": "medium",
        "investor_experience": "experienced_international",
    }
    result = rank_projects(opp_answers, ["Dubai"])
    check("G) rank_projects returns 5 values", len(result) == 5, f"len={len(result)}")
    ranked, elim, weights, log, spec_tag = result
    check("G) opportunistic speculation_tag", spec_tag == "standard", f"got {spec_tag}")
    for p in ranked:
        sc = p["project_score"]
        check(
            f"G) {p['project_name']} score in [0,100]",
            0 <= sc <= 100,
            f"score={sc}",
        )
        contrib_sum = sum(b["contribution"] for b in p["score_breakdown"].values())
        check(
            f"G) {p['project_name']} contributions sum",
            abs(contrib_sum - sc) <= 0.05,
            f"score={sc}, sum_contrib={contrib_sum}",
        )
        for bucket, bd in p["score_breakdown"].items():
            for key in ("bucket_score", "engine_score", "weight_pct", "contribution", "is_inverse"):
                if key not in bd:
                    check(f"G) breakdown keys {p['project_name']}/{bucket}", False, f"missing {key}")

    cons_answers = {**opp_answers, "risk_appetite": "conservative", "usage_intent": "primary_relocation"}
    _, _, _, _, spec_tag2 = rank_projects(cons_answers, ["Dubai"])
    check("G) conservative speculation_tag", spec_tag2 == "inverse", f"got {spec_tag2}")
finally:
    pe.PROJECTS = _orig_projects

# ── Print summary ─────────────────────────────────────────────────────────────
print("=" * 60)
print(f"PASSED: {len(PASSED)}")
for p in PASSED:
    print(f"  OK  {p}")
print()
print(f"FAILED: {len(FAILURES)}")
for f in FAILURES:
    print(f"  FAIL  {f}")
print("=" * 60)
sys.exit(1 if FAILURES else 0)
