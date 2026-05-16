import re
import sys
import os

# Allow imports from the repo root (projects_data, weights_config)
sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)

from projects_data import PROJECTS, get_projects_by_cities, list_determinant_keys
from weights_config import (
    PROJECT_BASELINE_WEIGHTS,
    compute_project_weights,
    winsorize,
    WEIGHT_FLOOR,
    WEIGHT_CAP,
)


# ─── CURRENCY CONVERSION RATES (approximate) ──────────────

_RATES_TO_USD = {
    "EUR": 1.08,
    "AED": 0.27,
    "THB": 0.028,
    "USD": 1.0,
}


# ─── PRICE PARSER ─────────────────────────────────────────

def _parse_min_price_usd(price_range: str) -> float | None:
    """
    Extracts the lower-bound price from a price_range string and
    converts to USD.

    Handles € / AED / ฿ / $ prefixes and K / M suffixes.
    Returns None if the string cannot be parsed.

    Examples:
      "€450K – €2.5M"       → 486_000
      "AED 1.57M – ..."     → 423_900
      "฿6.8M – ฿60M"       →  190_400
      "$8.5M – $185M"       → 8_500_000
    """
    if not price_range:
        return None

    # Take only the first token (before the dash separator)
    first = price_range.split("–")[0].strip()

    # Detect currency
    upper = first.upper()
    if "AED" in upper:
        currency = "AED"
    elif "€" in first:
        currency = "EUR"
    elif "฿" in first:
        currency = "THB"
    else:
        currency = "USD"

    # Strip everything except digits, dots, K, M
    cleaned = re.sub(r"[^\d.KMkm]", "", first).upper()

    if not cleaned:
        return None

    multiplier = 1
    if cleaned.endswith("M"):
        multiplier = 1_000_000
        cleaned = cleaned[:-1]
    elif cleaned.endswith("K"):
        multiplier = 1_000
        cleaned = cleaned[:-1]

    try:
        amount = float(cleaned) * multiplier
    except ValueError:
        return None

    return amount * _RATES_TO_USD.get(currency, 1.0)


# ─── HARD FILTERS ─────────────────────────────────────────

def apply_project_hard_filters(
    answers: dict,
    surviving_cities: list,
) -> tuple:
    """
    Filters PROJECTS to candidates based on five hard rules:
      1. City must be in surviving_cities (from the city engine)
      2. Budget: min project price <= investor_budget × 1.2 flex
      3. Ready to move: if required, drop Under Construction / Off-Plan
      4. Ownership: if freehold_only, drop leasehold
      5. Property type: if specified (not "any"), must fuzzy-match

    Returns:
        (surviving: list[dict], eliminated: list[dict])
    """
    budget_usd = answers.get("budget_usd", 0)
    budget_flex = budget_usd * 1.2

    ready_required = answers.get("ready_to_move", "no") == "yes"
    ownership_pref = answers.get("ownership_structure", "any")
    type_pref = answers.get("property_type_filter", "any")

    city_set = set(surviving_cities)

    surviving = []
    eliminated = []

    for key, project in PROJECTS.items():
        p = {**project, "project_key": key}

        # Filter 1 — city
        if project["city"] not in city_set:
            eliminated.append({
                "project_name": project["project_name"],
                "country": project["country"],
                "city": project["city"],
                "reason": (
                    f"City '{project['city']}' not in surviving cities"
                    " from city engine"
                ),
            })
            continue

        # Filter 2 — budget
        if budget_usd > 0:
            min_price = _parse_min_price_usd(project.get("price_range", ""))
            if min_price is not None and min_price > budget_flex:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country": project["country"],
                    "city": project["city"],
                    "reason": (
                        f"Min price exceeds budget "
                        f"${budget_usd:,} + 20% flex"
                    ),
                })
                continue

        # Filter 3 — ready to move
        if ready_required:
            stage = project.get("project_stage", "").lower()
            if "under construction" in stage or "off-plan" in stage or "off plan" in stage:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country": project["country"],
                    "city": project["city"],
                    "reason": (
                        "Under construction — investor requires ready to move"
                    ),
                })
                continue

        # Filter 4 — ownership
        if ownership_pref == "freehold_only":
            if project.get("ownership", "").lower() != "freehold":
                eliminated.append({
                    "project_name": project["project_name"],
                    "country": project["country"],
                    "city": project["city"],
                    "reason": "Leasehold — investor requires freehold",
                })
                continue

        # Filter 5 — property type (fuzzy match)
        if type_pref and type_pref != "any":
            project_type = project.get("project_type", "").lower()
            pref_lower = type_pref.lower()

            matched = (
                pref_lower in project_type
                or (pref_lower == "apartment" and "residential" in project_type)
                or (pref_lower == "villa" and "villa" in project_type)
                or (pref_lower == "resort" and "resort" in project_type)
                or (pref_lower == "branded" and "branded" in project_type)
            )
            if not matched:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country": project["country"],
                    "city": project["city"],
                    "reason": (
                        f"Type '{project['project_type']}' doesn't match"
                        f" preference '{type_pref}'"
                    ),
                })
                continue

        surviving.append(p)

    return surviving, eliminated


# ─── SCORING ──────────────────────────────────────────────

def score_project(
    project: dict,
    normalized_weights: dict,
    all_surviving: list,
) -> tuple:
    """
    Scores one project against normalized_weights.

    All 8 determinant scores are on a 0-10 scale (higher = better).
    litigation_history is already inverted at data-entry time
    (8 = clean record, 2 = many disputes), so no inversion needed here.

    Applies 95th-percentile Winsorization across surviving projects
    before computing each contribution.

    Returns: (total_score: float, breakdown: dict)
    """
    det_scores = project.get("determinant_scores", {})
    breakdown = {}
    total = 0.0

    for det, weight_pct in normalized_weights.items():
        all_vals = [
            p.get("determinant_scores", {}).get(det, 0)
            for p in all_surviving
        ]
        raw_score = det_scores.get(det, 0)
        winsorized = winsorize(raw_score, all_vals, percentile=95)
        contribution = (winsorized / 10) * weight_pct
        breakdown[det] = {
            "raw": raw_score,
            "winsorized": round(winsorized, 2),
            "weight_pct": round(weight_pct, 2),
            "contribution": round(contribution, 2),
        }
        total += contribution

    return round(total, 2), breakdown


# ─── RANKING PIPELINE ─────────────────────────────────────

def rank_projects(
    answers: dict,
    surviving_cities: list,
) -> tuple:
    """
    Full project engine pipeline:
      1. Apply hard filters (city + 4 investor constraints)
      2. Compute dynamic weights from investor answers
      3. Score all surviving projects with winsorization
      4. Sort by score descending, attach rank

    Returns:
        (ranked, eliminated, normalized_weights, weight_log)
    """
    surviving, eliminated = apply_project_hard_filters(
        answers, surviving_cities
    )

    if not surviving:
        return [], eliminated, PROJECT_BASELINE_WEIGHTS.copy(), []

    _, normalized_weights, weight_log = compute_project_weights(answers)

    ranked = []
    for project in surviving:
        score, breakdown = score_project(
            project, normalized_weights, surviving
        )
        ranked.append({
            **project,
            "project_score": score,
            "score_breakdown": breakdown,
        })

    ranked.sort(key=lambda x: x["project_score"], reverse=True)

    for i, p in enumerate(ranked, 1):
        p["rank"] = i

    return ranked, eliminated, normalized_weights, weight_log
