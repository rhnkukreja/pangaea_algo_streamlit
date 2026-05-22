import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd
from city_engine import rank_cities, CITIES
from weights_config import CITY_BASELINE_WEIGHTS

st.set_page_config(page_title="City Filtering", layout="wide")

if "surviving_countries" not in st.session_state or not st.session_state.surviving_countries:
    st.warning("⚠️ Please complete **Country Filtering** on Page 1 first.")
    st.stop()

st.title("City Filtering")
st.caption(
    f"Page 2 of 2 — Filtering cities within: **{', '.join(st.session_state.surviving_countries)}**"
)

col_form, col_weights, col_results = st.columns([1, 1, 1.2])

with col_form:
    st.subheader("Investor Profile")
    st.caption("City scoring is driven by two signals only.")

    primary_objective = st.selectbox(
        "Q1 — Primary Investment Objective",
        options=[
            "capital_appreciation",
            "yield_cash_flow",
            "capital_preservation",
            "lifestyle_end_use",
            "residency_citizenship",
        ],
        format_func=lambda x: {
            "capital_appreciation": "Capital Appreciation",
            "yield_cash_flow": "Yield / Cash Flow",
            "capital_preservation": "Capital Preservation",
            "lifestyle_end_use": "Lifestyle / End-Use",
            "residency_citizenship": "Residency / Citizenship",
        }[x],
        key="city_primary_objective",
    )

    risk_appetite = st.radio(
        "Q2 — Risk Appetite",
        options=["conservative", "moderate", "opportunistic"],
        format_func=lambda x: x.title(),
        key="city_risk_appetite",
    )

    st.markdown("---")
    st.caption(
        "ℹ️ Family composition, proximity preferences, prestige "
        "sensitivity, and lifestyle preference are collected at the "
        "survey level and will influence **Project-level filtering** "
        "in the next phase. They do not affect city scoring."
    )

city_answers = {
    "primary_objective": primary_objective,
    "risk_appetite": risk_appetite,
}

ranked_cities, normalized_weights, weight_log = rank_cities(
    st.session_state.surviving_countries,
    city_answers,
)
st.session_state.ranked_cities = [r["city"] for r in ranked_cities]

with col_weights:
    st.subheader("City-Level Weights")
    st.caption("How lifestyle answers reshape city scoring")

    rows = []
    for determinant, baseline in CITY_BASELINE_WEIGHTS.items():
        final = normalized_weights.get(determinant, 0)
        delta = round(final - baseline, 1)
        delta_str = f"+{delta}" if delta > 0 else str(delta)
        rows.append({
            "Determinant": determinant.replace("_", " ").title(),
            "Baseline": f"{baseline}%",
            "Final": f"{final}%",
            "Δ": delta_str,
        })

    df = pd.DataFrame(rows)
    st.dataframe(df, hide_index=True, use_container_width=True)

    with st.expander("📋 Why these weights changed"):
        objective_label = primary_objective.replace("_", " ").title()
        risk_label = risk_appetite.title()
        tier_to_source = {
            "Tier 1": f"Primary Objective = {objective_label}",
            "Tier 2": f"Risk Appetite = {risk_label}",
        }

        if not weight_log:
            st.caption("No shifts applied — using baseline weights.")
        else:
            grouped = {}
            for entry in weight_log:
                tier = entry.get("tier", "")
                src = tier_to_source.get(tier, tier)
                grouped.setdefault(src, []).append(entry)

            for source_label, entries in grouped.items():
                st.markdown(f"**{source_label}**")

                if not entries:
                    st.caption("  (No shifts applied)")
                else:
                    for entry in entries:
                        det = entry.get("determinant", "").replace("_", " ").title()
                        raw = entry.get("raw_shift", 0)
                        adj = entry.get("adjusted_shift", 0)
                        before = entry.get("before", 0)
                        after = entry.get("after", 0)
                        final = entry.get(
                            "final_weight",
                            normalized_weights.get(entry.get("determinant", ""), 0),
                        )
                        sign = "+" if raw > 0 else ""
                        color = "🟢" if raw > 0 else "🔴"
                        st.caption(
                            f"  {color} {det}: "
                            f"raw {sign}{raw} → "
                            f"adjusted {sign}{round(adj, 2)} → "
                            f"{round(before, 1)}% → {round(after, 1)}% raw → "
                            f"**{final}% final**"
                        )

                st.markdown("---")

with col_results:
    st.subheader("Ranked Cities")
    st.caption(
        f"{len(ranked_cities)} cities within {len(st.session_state.surviving_countries)} surviving countries"
    )

    for idx, item in enumerate(ranked_cities[:8], 1):
        with st.container(border=True):
            top = st.columns([1, 4, 2])
            with top[0]:
                st.markdown(f"### #{idx}")
            with top[1]:
                st.markdown(f"**{item['city']}**")
                st.caption(f"{item['country']}")
            with top[2]:
                score = item["score"]
                if score > 70:
                    color = "#22c55e"
                elif score > 50:
                    color = "#f59e0b"
                else:
                    color = "#a0a0a0"
                st.markdown(
                    f"<h3 style='color:{color};text-align:right;margin:0'>{score}</h3>",
                    unsafe_allow_html=True,
                )

            with st.expander("Score breakdown"):
                for determinant, contribution in item["breakdown"].items():
                    weight = normalized_weights[determinant]
                    raw_score = CITIES[item["city"]]["scores"][determinant]
                    standardized = item["standardized_scores"][determinant]
                    st.caption(
                        f"**{determinant.replace('_', ' ').title()}**: {contribution} pts"
                        f"  (standardized {round(standardized, 2)} × {weight}% weight)"
                    )

st.markdown("---")
st.info("✅ City filtering complete. Project-level filtering will be added in the next phase.")
