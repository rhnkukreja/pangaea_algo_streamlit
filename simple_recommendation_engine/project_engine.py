import re
import sys
import os

# Allow imports from the repo root (projects_data, weights_config)
sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)

from projects_data import PROJECTS, get_projects_by_cities, list_determinant_keys
from simple_recommendation_engine.constants import PROJECT_INVERSE_VARS
from simple_recommendation_engine.normalization import (
    standardize_determinants,
    weighted_score,
)
from weights_config import (
    PROJECT_BASELINE_WEIGHTS,
    compute_project_weights,
    WEIGHT_FLOOR,
    WEIGHT_CAP,
)


# â”€â”€â”€ CURRENCY CONVERSION RATES (approximate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

_RATES_TO_USD = {
    "EUR": 1.08,
    "AED": 0.27,
    "THB": 0.028,
    "USD": 1.0,
}


# â”€â”€â”€ PRICE PARSER â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def _parse_min_price_usd(price_range: str) -> float | None:
    """
    Extracts the lower-bound price from a price_range string and
    converts to USD.

    Handles â‚¬ / AED / à¸¿ / $ prefixes and K / M suffixes.
    Returns None if the string cannot be parsed.

    Examples:
      "â‚¬450K â€“ â‚¬2.5M"       â†’ 486_000
      "AED 1.57M â€“ ..."     â†’ 423_900
      "à¸¿6.8M â€“ à¸¿60M"       â†’  190_400
      "$8.5M â€“ $185M"       â†’ 8_500_000
    """
    if not price_range:
        return None

    # Take only the first token (before the dash separator)
    first = re.split(r"[-\u2013\u2014]|â€“", price_range)[0].strip()

    # Detect currency
    upper = first.upper()
    if "AED" in upper:
        currency = "AED"
    elif "\u20ac" in first or "\u00e2\u201a\u00ac" in first or "EUR" in upper:
        currency = "EUR"
    elif "\u0e3f" in first or "\u00e0\u00b8\u00bf" in first or "THB" in upper:
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


# â”€â”€â”€ HARD FILTERS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def apply_project_hard_filters(
    answers: dict,
    surviving_cities: list,
) -> tuple:
    """
    Filters PROJECTS to candidates based on five hard rules:
      1. City must be in surviving_cities (from the city engine)
      2. Budget: min project price <= investor_budget Ã— 1.2 flex
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

        # Filter 1 â€” city
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

        # Filter 2 â€” budget
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

        # Filter 3 â€” ready to move
        if ready_required:
            stage = project.get("project_stage", "").lower()
            if "under construction" in stage or "off-plan" in stage or "off plan" in stage:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country": project["country"],
                    "city": project["city"],
                    "reason": (
                        "Under construction â€” investor requires ready to move"
                    ),
                })
                continue

        # Filter 4 â€” ownership
        if ownership_pref == "freehold_only":
            if project.get("ownership", "").lower() != "freehold":
                eliminated.append({
                    "project_name": project["project_name"],
                    "country": project["country"],
                    "city": project["city"],
                    "reason": "Leasehold â€” investor requires freehold",
                })
                continue

        # Filter 5 â€” property type (fuzzy match)
        if type_pref and type_pref != "any":
            project_type = project.get("project_type", "").lower()
            searchable_text = " ".join([
                project_type,
                project.get("project_name", "").lower(),
                project.get("highlight", "").lower(),
                project.get("description", "").lower(),
                " ".join(project.get("tags", [])).lower(),
            ])
            pref_lower = type_pref.lower()

            matched = (
                pref_lower in searchable_text
                or (pref_lower == "apartment" and "residential" in project_type)
                or (pref_lower == "villa" and "villa" in searchable_text)
                or (pref_lower == "branded" and "branded" in searchable_text)
                or (pref_lower == "managed" and ("managed" in searchable_text or "management" in searchable_text))
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


# â”€â”€â”€ SCORING â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def _project_scoring_values(scores: dict) -> dict:
    """
    Return determinant values in raw scoring orientation.

    Existing data stores litigation_history as a clean-record score. The
    cascading model treats litigation as inverse risk, so this converts the
    stored clean score to a risk value before inverse normalization.
    """
    oriented = dict(scores)
    if "litigation_history" in oriented:
        oriented["litigation_history"] = 10 - float(oriented["litigation_history"])
    return oriented

def score_project(
    project: dict,
    normalized_weights: dict,
    all_surviving: list,
) -> tuple:
    """
    Score one project using z-score normalization and final weighted scoring.

    The project dataset stores litigation_history as a cleanliness score
    (higher = cleaner). To keep the requested inverse-variable logic explicit
    without rewriting project data, the scoring input converts it back to a
    raw litigation-risk value before applying inverse standardization.

    Returns: (total_score: float, breakdown: dict)
    """
    det_scores = _project_scoring_values(project.get("determinant_scores", {}))
    peer_scores = [
        _project_scoring_values(p.get("determinant_scores", {}))
        for p in all_surviving
    ]
    standardized = standardize_determinants(
        det_scores,
        peer_scores,
        normalized_weights.keys(),
        inverse_vars=PROJECT_INVERSE_VARS,
    )
    total, contribution_breakdown = weighted_score(
        standardized,
        normalized_weights,
    )

    breakdown = {}

    for det, weight_pct in normalized_weights.items():
        raw_score = project.get("determinant_scores", {}).get(det, 0)
        breakdown[det] = {
            "raw": raw_score,
            "winsorized": round(standardized.get(det, 50), 2),
            "standardized": round(standardized.get(det, 50), 2),
            "weight_pct": round(weight_pct, 2),
            "contribution": contribution_breakdown.get(det, 0),
        }

    return total, breakdown


# â”€â”€â”€ RANKING PIPELINE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

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

    _, normalized_weights, weight_log = compute_project_weights(answers)

    if not surviving:
        return [], eliminated, normalized_weights, weight_log

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
