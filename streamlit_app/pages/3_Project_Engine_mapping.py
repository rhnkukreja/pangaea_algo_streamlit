import streamlit as st
import sys
import os

_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.insert(0, _ROOT)

import pandas as pd

from simple_recommendation_engine.project_engine import rank_projects
from projects_data import PROJECTS
from weights_config import PROJECT_BASELINE_WEIGHTS

st.set_page_config(
    page_title="Project Engine Mapping",
    layout="wide",
)

# =========================================================
# VALIDATION
# =========================================================

if (
    "surviving_countries" not in st.session_state
    or not st.session_state.surviving_countries
):
    st.warning("⚠️ Please complete Country Filtering first.")
    st.stop()

# =========================================================
# SURVIVING CITIES
# Prefer ranked_cities set by city engine;
# fall back to all cities within surviving countries.
# =========================================================

if st.session_state.get("ranked_cities"):
    surviving_cities = st.session_state.ranked_cities
else:
    surviving_cities = list({
        p["city"]
        for p in PROJECTS.values()
        if p["country"] in st.session_state.surviving_countries
    })

# =========================================================
# PAGE HEADER
# =========================================================

st.title("Project Engine Mapping")
st.caption(
    "Page 3 of 3 — Dynamic project ranking "
    "using the Cascading Archetype Model"
)
st.caption(f"Cities in scope: **{', '.join(sorted(surviving_cities))}**")

# =========================================================
# LAYOUT
# =========================================================

BUDGET_OPTIONS = [
    150_000, 300_000, 500_000, 800_000,
    1_000_000, 1_500_000, 3_000_000,
    5_000_000, 10_000_000,
]

col_form, col_weights, col_results = st.columns([1, 1, 1.2])

# =========================================================
# INVESTOR PROFILE FORM
# =========================================================

with col_form:

    st.subheader("Investor Profile")

    budget_usd = st.select_slider(
        "Budget (USD)",
        options=BUDGET_OPTIONS,
        format_func=lambda x: f"${x:,}",
        value=800_000,
        key="project_budget",
    )

    ready_to_move = st.radio(
        "Ready To Move Required?",
        ["no", "yes"],
        format_func=lambda x: {"yes": "Yes", "no": "No"}[x],
    )

    ownership_structure = st.radio(
        "Ownership Requirement",
        ["any", "freehold_only"],
        format_func=lambda x: {
            "freehold_only": "Freehold Only",
            "any": "Any",
        }[x],
    )

    property_type_filter = st.selectbox(
        "Property Type",
        ["any", "Apartment", "Villa", "Resort", "Branded", "Mixed-use"],
    )

    st.markdown("---")

    usage_intent = st.selectbox(
        "Usage Intent",
        [
            "pure_investment",
            "investment_occasional_use",
            "primary_relocation",
        ],
        format_func=lambda x: {
            "pure_investment": "Pure Investment",
            "investment_occasional_use": "Investment + Occasional Use",
            "primary_relocation": "Primary Relocation",
        }[x],
    )

    holding_period = st.radio(
        "Holding Period",
        ["short_term", "medium_term", "long_term"],
        format_func=lambda x: {
            "short_term": "Short (<3 years)",
            "medium_term": "Medium (3–7 years)",
            "long_term": "Long (>7 years)",
        }[x],
    )

    liquidity_preference = st.radio(
        "Liquidity Preference",
        ["high_resale", "long_lockin"],
        format_func=lambda x: {
            "high_resale": "High Resale Liquidity",
            "long_lockin": "Long Lock-in Acceptable",
        }[x],
    )

    risk_appetite = st.radio(
        "Risk Appetite",
        ["conservative", "moderate", "opportunistic"],
        format_func=lambda x: x.title(),
    )

    investor_experience = st.radio(
        "Investor Experience",
        ["first_time", "experienced"],
        format_func=lambda x: {
            "first_time": "First International Purchase",
            "experienced": "Experienced International Investor",
        }[x],
    )

    prestige_sensitivity = st.radio(
        "Prestige / Brand Sensitivity",
        ["high", "medium", "low"],
        format_func=lambda x: x.title(),
    )

    proximity_preference = st.radio(
        "Proximity Preference",
        ["airport_cbd_leisure", "schools_hospitals"],
        format_func=lambda x: {
            "airport_cbd_leisure": "Airport / CBD / Leisure",
            "schools_hospitals": "Schools / Hospitals",
        }[x],
    )

    family_composition = st.radio(
        "Family Composition",
        ["single_couple", "family"],
        format_func=lambda x: {
            "single_couple": "Single / Couple",
            "family": "Family / Multi-generational",
        }[x],
    )

# =========================================================
# ANSWERS
# =========================================================

project_answers = {
    "budget_usd": budget_usd,
    "ready_to_move": ready_to_move,
    "ownership_structure": ownership_structure,
    "property_type_filter": property_type_filter,
    "usage_intent": usage_intent,
    "holding_period": holding_period,
    "liquidity_preference": liquidity_preference,
    "risk_appetite": risk_appetite,
    "investor_experience": investor_experience,
    "prestige_sensitivity": prestige_sensitivity,
    "proximity_preference": proximity_preference,
    "family_composition": family_composition,
}

# =========================================================
# ENGINE EXECUTION
# =========================================================

(
    ranked_projects,
    eliminated_projects,
    normalized_weights,
    weight_log,
) = rank_projects(project_answers, surviving_cities)

# =========================================================
# WEIGHTS PANEL
# =========================================================

with col_weights:

    st.subheader("Determinant Weights")

    rows = []
    for determinant, baseline in PROJECT_BASELINE_WEIGHTS.items():
        final = normalized_weights.get(determinant, 0)
        delta = round(final - baseline, 1)
        delta_str = f"+{delta}" if delta > 0 else str(delta)
        rows.append({
            "Determinant": determinant.replace("_", " ").title(),
            "Baseline": f"{baseline}%",
            "Final": f"{final}%",
            "Δ": delta_str,
        })

    st.dataframe(
        pd.DataFrame(rows),
        hide_index=True,
        use_container_width=True,
    )

    with st.expander("📋 Why these weights changed"):

        if not weight_log:
            st.caption("No shifts applied — using baseline weights.")
        else:
            grouped = {}
            for entry in weight_log:
                src = entry.get("source", entry.get("tier", ""))
                grouped.setdefault(src, []).append(entry)

            for source_label, entries in grouped.items():
                st.markdown(f"**{source_label}**")
                for entry in entries:
                    det = entry["determinant"].replace("_", " ").title()
                    raw = entry["raw_shift"]
                    adj = entry["adjusted_shift"]
                    before = entry["before"]
                    after = entry["after"]
                    sign = "+" if raw > 0 else ""
                    color = "🟢" if raw > 0 else "🔴"
                    st.caption(
                        f"  {color} {det}: "
                        f"raw {sign}{raw} → "
                        f"adjusted {sign}{round(adj, 2)} → "
                        f"{round(before, 1)}% → **{round(after, 1)}%**"
                    )
                st.markdown("---")

# =========================================================
# RESULTS PANEL
# =========================================================

with col_results:

    st.subheader("Ranked Projects")

    st.caption(
        f"{len(ranked_projects)} of {len(PROJECTS)} "
        "projects survived filtering"
    )

    for item in ranked_projects:

        with st.container(border=True):

            top = st.columns([1, 4, 2])

            with top[0]:
                st.markdown(f"### #{item['rank']}")

            with top[1]:
                flag = item.get("flag", "")
                st.markdown(f"**{flag} {item['project_name']}**")
                gv = " · 🥇 GV" if item.get("golden_visa") else ""
                st.caption(
                    f"{item['city']} · {item['country']}"
                    f" · {item.get('project_stage', '')}{gv}"
                )
                st.caption(item.get("price_range", ""))

            with top[2]:
                score = item["project_score"]
                if score > 70:
                    color = "#22c55e"
                elif score > 50:
                    color = "#f59e0b"
                else:
                    color = "#a0a0a0"
                st.markdown(
                    f"<h3 style='color:{color};"
                    f"text-align:right;"
                    f"margin:0'>{score}</h3>",
                    unsafe_allow_html=True,
                )

            with st.expander("Score breakdown"):
                for det, info in item["score_breakdown"].items():
                    st.caption(
                        f"**{det.replace('_', ' ').title()}**: "
                        f"{info['contribution']} pts "
                        f"(raw {info['raw']}/10 × "
                        f"{info['weight_pct']}% weight)"
                    )

    if eliminated_projects:
        with st.expander(
            f"❌ Eliminated Projects ({len(eliminated_projects)})"
        ):
            for item in eliminated_projects:
                proj_key = next(
                    (k for k, v in PROJECTS.items()
                     if v["project_name"] == item["project_name"]),
                    ""
                )
                flag = PROJECTS.get(proj_key, {}).get("flag", "")
                st.caption(
                    f"**{flag} {item['project_name']}** "
                    f"({item.get('city', '')} · "
                    f"{item.get('country', '')}) — {item['reason']}"
                )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
st.success("✅ Project Engine Mapping Complete")
