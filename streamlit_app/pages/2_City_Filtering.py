import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import pandas as pd
from city_engine import rank_cities, CITIES
from weights_config import CITY_BASELINE_WEIGHTS
from streamlit_ui_helpers import group_weight_log, weight_log_fields

# ── Display name mapping: engine key → Excel / client-facing label ────────────
CITY_DISPLAY_NAMES = {
    "population_growth":          "Population Growth Rate",
    "transaction_volume_growth":  "Transaction Volume Growth",
    "supply_pipeline":            "Supply Pipeline (5Y)",
    "employment_growth":          "Employment Growth Rate",
    "price_appreciation_5y":      "Price Appreciation (5Y)",
    "tourism_strength":           "Tourism Strength",
    "rental_demand_index":        "Rental Demand Index",
    "macro_infra_pipeline":       "Macro Infrastructure Pipeline",
    "quality_of_life_index":      "Quality of Life Index",
}

def display_name(key: str) -> str:
    """Return the client-facing display name for a determinant key."""
    return CITY_DISPLAY_NAMES.get(key, key.replace("_", " ").title())


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
            "yield_cashflow",
            "capital_preservation",
            "lifestyle",
            "residency",
        ],
        format_func=lambda x: {
            "capital_appreciation": "Capital Appreciation",
            "yield_cashflow":       "Yield / Cash Flow",
            "capital_preservation": "Capital Preservation",
            "lifestyle":            "Lifestyle / End-Use",
            "residency":            "Residency / Citizenship",
        }[x],
        key="city_primary_objective",
    )
    risk_appetite = st.radio(
        "Q2 — Risk Appetite",
        options=["conservative", "neutral", "opportunistic"],
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
            "Determinant": display_name(determinant),
            "Baseline":    f"{baseline}%",
            "Final":       f"{final}%",
            "Δ":           delta_str,
        })
    df = pd.DataFrame(rows)
    st.dataframe(df, hide_index=True, use_container_width=True)

    with st.expander("📋 Why these weights changed"):
        if not weight_log:
            st.caption("No shifts applied — using baseline weights.")
        else:
            for source_label, entries in group_weight_log(weight_log).items():
                st.markdown(f"**{source_label}**")
                for entry in entries:
                    f = weight_log_fields(entry)
                    det = display_name(f["determinant"])
                    raw = f["raw"]
                    sign = "+" if raw > 0 else ""
                    color = "🟢" if raw > 0 else "🔴"
                    st.caption(
                        f"  {color} {det}: "
                        f"raw {sign}{raw} → "
                        f"{round(f['before'], 1)}% baseline → "
                        f"**{round(f['final'], 1)}% final**"
                    )
                st.markdown("---")

with col_results:
    st.subheader("Ranked Cities")
    st.caption(
        f"{len(ranked_cities)} cities within "
        f"{len(st.session_state.surviving_countries)} surviving countries"
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
                    weight       = normalized_weights[determinant]
                    raw_score    = CITIES[item["city"]]["scores"][determinant]
                    standardized = item["standardized_scores"][determinant]
                    st.caption(
                        f"**{display_name(determinant)}**: {contribution} pts"
                        f"  (standardized {round(standardized, 2)} × {weight}% weight)"
                    )

st.markdown("---")
st.info("✅ City filtering complete. Project-level filtering will be added in the next phase.")