import sys
import os

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import streamlit as st
import pandas as pd

from simple_recommendation_engine.project_engine import rank_projects
from projects_data import PROJECTS
from weights_config import PROJECT_BASELINE_WEIGHTS
from streamlit_ui_helpers import (
    engine_score_from_breakdown,
    group_weight_log,
    weight_log_fields,
)

st.set_page_config(
    page_title="Pangaea Advisory",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp { background-color: #0A0A0A; }
</style>
""", unsafe_allow_html=True)

st.title("🏛️ Pangaea Advisory")
st.caption("Multi-layer recommendation engine — Country, City, Project Level")

tab1, tab2 = st.tabs(["How it works", "Project Preferences"])

# ─────────────────────────────────────────────────────────
# TAB 1 — Overview + navigation guide
# ─────────────────────────────────────────────────────────

with tab1:
    st.markdown("""
### How it works

**Page 1 — Country Filtering**
Answer the country hard-constraint and scoring questions.
Watch determinant weights shift and countries get ranked live.

**Page 2 — City Filtering**
Within the surviving countries from Page 1, answer 5 more questions
about lifestyle, family, and preferences. See cities ranked with
full explainability.

**Home → Project Preferences (Tab 2)**
After completing Pages 1 and 2, switch to the **Project Preferences**
tab above to rank real projects within your surviving cities.

---

Use the sidebar to navigate to **Country Filtering** and
**City Filtering** first. Then return here for project rankings.
""")

    surviving = st.session_state.get("ranked_cities", [])
    if surviving:
        st.success(
            f"✅ {len(surviving)} surviving cities loaded from city engine: "
            + ", ".join(surviving)
        )
    else:
        st.info(
            "ℹ️ No surviving cities yet — complete Country Filtering "
            "and City Filtering in the sidebar first."
        )

# ─────────────────────────────────────────────────────────
# TAB 2 — Project Preferences + Ranking
# ─────────────────────────────────────────────────────────

with tab2:

    surviving_cities = st.session_state.get("ranked_cities", [])

    if not surviving_cities:
        st.warning(
            "⚠️ No surviving cities found. Please complete "
            "**Country Filtering** and **City Filtering** in the sidebar first."
        )
        st.stop()

    st.caption(
        f"Ranking projects within: **{', '.join(surviving_cities)}**"
    )

    col_form, col_weights, col_results = st.columns([1, 1, 1.3])

    # ── Form ──────────────────────────────────────────────
    with col_form:
        st.subheader("Project Preferences")

        budget_usd = st.select_slider(
            "Budget (USD)",
            options=[150_000, 300_000, 500_000, 800_000,
                     1_000_000, 1_500_000, 3_000_000, 5_000_000,
                     10_000_000],
            format_func=lambda x: f"${x:,}",
            value=800_000,
            key="proj_budget",
        )

        ready_to_move = st.radio(
            "Ready To Move Required?",
            ["no", "yes"],
            format_func=lambda x: {"no": "No", "yes": "Yes"}[x],
            key="proj_ready",
        )

        ownership_structure = st.radio(
            "Ownership Requirement",
            ["any", "freehold_only"],
            format_func=lambda x: {
                "any": "Any (freehold or leasehold)",
                "freehold_only": "Freehold only",
            }[x],
            key="proj_ownership",
        )

        property_type_filter = st.selectbox(
            "Property Type",
            ["any", "Apartment", "Villa", "Branded", "Managed"],
            key="proj_type",
        )

        st.markdown("---")

        usage_intent = st.selectbox(
            "Usage Intent",
            ["pure_investment", "investment_occasional_use", "primary_relocation"],
            format_func=lambda x: {
                "pure_investment": "Pure Investment",
                "investment_occasional_use": "Investment + Occasional Use",
                "primary_relocation": "Primary Relocation",
            }[x],
            key="proj_usage",
        )

        holding_period = st.radio(
            "Holding Period",
            ["short_term", "medium_term", "long_term"],
            format_func=lambda x: {
                "short_term": "Short (<3 years)",
                "medium_term": "Medium (3–7 years)",
                "long_term": "Long (>7 years)",
            }[x],
            key="proj_holding",
        )

        liquidity_preference = st.radio(
            "Liquidity Preference",
            ["high_resale", "long_lockin"],
            format_func=lambda x: {
                "high_resale": "High Resale Liquidity",
                "long_lockin": "Long Lock-in Acceptable",
            }[x],
            key="proj_liquidity",
        )

        risk_appetite = st.radio(
            "Risk Appetite",
            ["conservative", "moderate", "opportunistic"],
            format_func=lambda x: x.title(),
            key="proj_risk",
        )

        investor_experience = st.radio(
            "Investor Experience",
            ["first_time", "experienced"],
            format_func=lambda x: {
                "first_time": "First International Purchase",
                "experienced": "Experienced International Investor",
            }[x],
            key="proj_experience",
        )

        prestige_sensitivity = st.radio(
            "Prestige / Brand Sensitivity",
            ["high", "medium", "low"],
            format_func=lambda x: x.title(),
            key="proj_prestige",
        )

        proximity_preference = st.radio(
            "Proximity Preference",
            ["airport_cbd_leisure", "schools_hospitals"],
            format_func=lambda x: {
                "airport_cbd_leisure": "Airport / CBD / Leisure",
                "schools_hospitals": "Schools / Hospitals",
            }[x],
            key="proj_proximity",
        )

        family_composition = st.radio(
            "Family Composition",
            ["single_couple", "family"],
            format_func=lambda x: {
                "single_couple": "Single / Couple",
                "family": "Family / Multi-generational",
            }[x],
            key="proj_family",
        )

    # ── Engine call ───────────────────────────────────────
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

    ranked_projects, elim_projects, proj_weights, proj_log, speculation_tag = rank_projects(
        project_answers, surviving_cities
    )

    st.session_state.top_projects = [
        p["project_name"] for p in ranked_projects[:5]
    ]

    # ── Weights panel ─────────────────────────────────────
    with col_weights:
        st.subheader("Determinant Weights")

        rows = []
        for det, baseline in PROJECT_BASELINE_WEIGHTS.items():
            final = proj_weights.get(det, baseline)
            delta = round(final - baseline, 1)
            rows.append({
                "Determinant": det.replace("_", " ").title(),
                "Baseline": f"{baseline}%",
                "Final": f"{final}%",
                "Δ": f"+{delta}" if delta > 0 else str(delta),
            })

        st.dataframe(
            pd.DataFrame(rows),
            hide_index=True,
            use_container_width=True,
        )

        with st.expander("📋 Why these weights changed"):
            if not proj_log:
                st.caption("No shifts applied — using baseline weights.")
            else:
                for source_label, entries in group_weight_log(proj_log).items():
                    st.markdown(f"**{source_label}**")
                    for entry in entries:
                        f = weight_log_fields(entry)
                        det = f["determinant"].replace("_", " ").title()
                        raw = f["raw"]
                        adj = f["adjusted"]
                        sign = "+" if raw > 0 else ""
                        color = "🟢" if raw > 0 else "🔴"
                        st.caption(
                            f"  {color} {det}: raw {sign}{raw} → "
                            f"adjusted {sign}{round(adj, 2)} → "
                            f"{round(f['before'], 1)}% → {round(f['after'], 1)}% post-shift → "
                            f"**{round(f['final'], 1)}% final**"
                        )
                    st.markdown("---")

    # ── Results panel ─────────────────────────────────────
    with col_results:
        st.subheader("Ranked Projects")

        if not ranked_projects:
            st.warning(
                "No projects match the current filters within surviving cities."
            )
        else:
            st.metric(
                "Projects Scored",
                f"{len(ranked_projects)} of {len(PROJECTS)}",
            )

            for p in ranked_projects[:10]:
                with st.container(border=True):
                    top = st.columns([1, 4, 2])

                    with top[0]:
                        st.markdown(f"### #{p['rank']}")

                    with top[1]:
                        flag = p.get("flag", "")
                        st.markdown(f"**{flag} {p['project_name']}**")
                        gv = " · 🥇 Golden Visa" if p.get("golden_visa") else ""
                        st.caption(
                            f"{p['city']} · {p['country']}"
                            f" · {p.get('project_stage', '')}{gv}"
                        )
                        st.caption(p.get("price_range", ""))

                    with top[2]:
                        score = p["project_score"]
                        color = (
                            "#22c55e" if score > 70
                            else "#f59e0b" if score > 50
                            else "#a0a0a0"
                        )
                        st.markdown(
                            f"<h3 style='color:{color};"
                            f"text-align:right;margin:0'>{score}</h3>",
                            unsafe_allow_html=True,
                        )

                    with st.expander("Score breakdown"):
                        for det, info in p["score_breakdown"].items():
                            eng = engine_score_from_breakdown(info)
                            st.caption(
                                f"**{det.replace('_', ' ').title()}**: "
                                f"{info['contribution']} pts  "
                                f"(engine score {eng} × "
                                f"{info['weight_pct']}% weight; "
                                f"bucket raw {info.get('bucket_score', '—')})"
                            )

                    with st.expander("Why this ranked here"):
                        if not proj_log:
                            st.caption("No weight shifts applied.")
                        else:
                            for source_label, entries in group_weight_log(proj_log).items():
                                st.markdown(f"**{source_label}**")
                                for entry in entries:
                                    f = weight_log_fields(entry)
                                    det = f["determinant"].replace("_", " ").title()
                                    raw = f["raw"]
                                    sign = "+" if raw > 0 else ""
                                    color = "🟢" if raw > 0 else "🔴"
                                    st.caption(
                                        f"  {color} {det}: "
                                        f"raw {sign}{raw} → "
                                        f"{round(f['before'], 1)}% → "
                                        f"{round(f['after'], 1)}% post-shift → "
                                        f"**{round(f['final'], 1)}% final**"
                                    )
                                st.markdown("---")

        if elim_projects:
            with st.expander(f"❌ Eliminated projects ({len(elim_projects)})"):
                for e in elim_projects:
                    flag = PROJECTS.get(
                        next(
                            (k for k, v in PROJECTS.items()
                             if v["project_name"] == e["project_name"]),
                            ""
                        ), {}
                    ).get("flag", "")
                    st.caption(
                        f"**{flag} {e['project_name']}** "
                        f"({e['city']}, {e['country']}) — {e['reason']}"
                    )
