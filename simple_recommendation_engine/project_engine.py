"""
project_engine.py — Project Asset Scoring Engine

Pipeline:
  1. Hard filters  (city cascade + budget / ownership / type)
  2. Data roll-up  (raw variables → 13 bucket scores via project_rollup)
  3. Weight compute (investor survey → dynamic bucket weights + speculation tag)
  4. Z-score standardization across surviving peer group
  5. Weighted dot product → final score [0–100]

KEY CHANGES FROM V1:
  - _project_scoring_values() removed — no more litigation flip hack.
    Raw magnitude is stored directly (0=no risk, 100=max risk).
    Inversion handled in normalization via 50-(z×25) for inverse buckets.
  - score_project() now calls rollup_project() first to convert raw
    variables → 13 bucket scores before z-scoring.
  - compute_project_weights() now returns 4 values (added speculation_tag).
  - rank_projects() now returns 5 values (added speculation_tag).
  - Dynamic speculation_risk_score tag: INVERSE or STANDARD per investor profile.
"""
from __future__ import annotations
import re
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)

from projects_data import PROJECTS, get_projects_by_cities, list_determinant_keys
from simple_recommendation_engine.normalization import (
    standardize_determinants,
    weighted_score,
)
from weights_config import (
    PROJECT_BASELINE_WEIGHTS,
    compute_project_weights,
    WEIGHT_FLOOR,
    WEIGHT_CAP,
    PROJECT_WEIGHT_FLOOR,
    PROJECT_WEIGHT_CAP,
)
from project_rollup import rollup_project


# ── Static inverse buckets — always inverted regardless of investor profile ───
# speculation_risk_score is NOT here — it's dynamic (see _build_inverse_vars)
_STATIC_INVERSE_BUCKETS: frozenset[str] = frozenset({
    "supply_pressure_risk",    # high pipeline = worse market for buyer
    "delivery_track_record",   # high delay = worse developer
    "legal_and_governance",    # high litigation = worse developer
})


def _build_inverse_vars(speculation_tag: str) -> frozenset[str]:
    """
    Build the full inverse_vars set for a given investor profile.
    Static inverse buckets are always included.
    speculation_risk_score is added only when tag == "inverse".
    """
    inv = set(_STATIC_INVERSE_BUCKETS)
    if speculation_tag == "inverse":
        inv.add("speculation_risk_score")
    return frozenset(inv)


# ─────────────────────────────────────────────────────────────────────────────
# CURRENCY CONVERSION (unchanged from v1)
# ─────────────────────────────────────────────────────────────────────────────
_RATES_TO_USD = {
    "EUR": 1.08,
    "AED": 0.27,
    "THB": 0.028,
    "USD": 1.0,
}


def _parse_min_price_usd(price_range: str) -> float | None:
    """
    Extract lower-bound price from a price_range string and convert to USD.
    Handles €/AED/฿/$ prefixes and K/M suffixes.
    Returns None if unparseable.
    """
    if not price_range:
        return None
    first = re.split(r"[-\u2013\u2014]|–", price_range)[0].strip()
    upper = first.upper()
    if "AED" in upper:
        currency = "AED"
    elif "\u20ac" in first or "EUR" in upper:
        currency = "EUR"
    elif "\u0e3f" in first or "THB" in upper:
        currency = "THB"
    else:
        currency = "USD"
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


# ─────────────────────────────────────────────────────────────────────────────
# HARD FILTERS (unchanged from v1 — solid as-is)
# ─────────────────────────────────────────────────────────────────────────────
def apply_project_hard_filters(
    answers: dict,
    surviving_cities: list,
) -> tuple[list[dict], list[dict]]:
    """
    Binary filters applied before scoring.
    Failure on any rule → immediate drop.

    Rules:
      1. City must be in surviving_cities (from city engine)
      2. Budget: min price <= investor_budget × 1.2
      3. Ready to move: drop Under Construction / Off-Plan if required
      4. Ownership: drop leasehold if freehold_only
      5. Property type: fuzzy match if specified

    Returns:
        (surviving, eliminated)
    """
    budget_usd    = answers.get("budget_usd", 0)
    budget_flex   = budget_usd * 1.2
    ready_required = answers.get("ready_to_move", "no") == "yes"
    ownership_pref = answers.get("ownership_structure", "any")
    type_pref      = answers.get("property_type_filter", "any")
    city_set       = set(surviving_cities)

    surviving  = []
    eliminated = []

    for key, project in PROJECTS.items():
        p = {**project, "project_key": key}

        # 1 — city cascade
        if project["city"] not in city_set:
            eliminated.append({
                "project_name": project["project_name"],
                "country":      project["country"],
                "city":         project["city"],
                "reason":       f"City '{project['city']}' not in surviving cities",
            })
            continue

        # 2 — budget
        if budget_usd > 0:
            min_price = _parse_min_price_usd(project.get("price_range", ""))
            if min_price is not None and min_price > budget_flex:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country":      project["country"],
                    "city":         project["city"],
                    "reason":       f"Min price exceeds budget ${budget_usd:,} + 20% flex",
                })
                continue

        # 3 — ready to move
        if ready_required:
            stage = project.get("project_stage", "").lower()
            if "under construction" in stage or "off-plan" in stage or "off plan" in stage:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country":      project["country"],
                    "city":         project["city"],
                    "reason":       "Under construction — investor requires ready to move",
                })
                continue

        # 4 — ownership
        if ownership_pref == "freehold_only":
            if project.get("ownership", "").lower() != "freehold":
                eliminated.append({
                    "project_name": project["project_name"],
                    "country":      project["country"],
                    "city":         project["city"],
                    "reason":       "Leasehold — investor requires freehold",
                })
                continue

        # 5 — property type (fuzzy)
        if type_pref and type_pref != "any":
            project_type    = project.get("project_type", "").lower()
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
                or (pref_lower == "villa"     and "villa"       in searchable_text)
                or (pref_lower == "branded"   and "branded"     in searchable_text)
                or (pref_lower == "managed"   and ("managed" in searchable_text
                                                    or "management" in searchable_text))
            )
            if not matched:
                eliminated.append({
                    "project_name": project["project_name"],
                    "country":      project["country"],
                    "city":         project["city"],
                    "reason":       f"Type '{project['project_type']}' doesn't match '{type_pref}'",
                })
                continue

        surviving.append(p)

    return surviving, eliminated


# ─────────────────────────────────────────────────────────────────────────────
# SCORING
# ─────────────────────────────────────────────────────────────────────────────
def _get_bucket_scores(project: dict) -> dict[str, float]:
    """
    Get 13 bucket scores for one project.
    Prefers pre-computed bucket_scores if present (cached from a prior rollup),
    otherwise runs rollup_project() on the raw_variables / determinant_scores.
    """
    if "bucket_scores" in project:
        return project["bucket_scores"]

    raw = project.get("raw_variables") or project.get("determinant_scores", {})
    bucket_scores, _ = rollup_project(raw)
    return bucket_scores


def score_project(
    project: dict,
    normalized_weights: dict,
    all_surviving: list,
    speculation_tag: str = "standard",
) -> tuple[float, dict]:
    """
    Score one project against its surviving peer group.

    Track B: Z-score each bucket score across peers → engine scores
    Track C: Weighted dot product → final score [0–100]

    Args:
        project           : single project dict (must include raw_variables
                            or determinant_scores or pre-computed bucket_scores)
        normalized_weights: 13-bucket weights summing to 100
        all_surviving     : all projects in the peer group (self included)
        speculation_tag   : "standard" or "inverse" — controls whether
                            speculation_risk_score is penalized for high values

    Returns:
        (total_score, breakdown)
    """
    inverse_vars = _build_inverse_vars(speculation_tag)

    # Roll up this project's raw variables → 13 bucket scores
    this_bucket_scores = _get_bucket_scores(project)

    # Roll up ALL peers → peer bucket scores for z-scoring
    peer_bucket_scores = [_get_bucket_scores(p) for p in all_surviving]

    # Track B: standardize
    standardized = standardize_determinants(
        scores      = this_bucket_scores,
        peer_scores = peer_bucket_scores,
        determinants= list(normalized_weights.keys()),
        inverse_vars= inverse_vars,
    )

    # Track C: converge
    total, contribution_breakdown = weighted_score(standardized, normalized_weights)

    # Build detailed breakdown for UI
    breakdown = {}
    for bucket, weight_pct in normalized_weights.items():
        breakdown[bucket] = {
            "bucket_score":  round(this_bucket_scores.get(bucket, 50.0), 2),
            "engine_score":  round(standardized.get(bucket, 50.0), 2),
            "weight_pct":    round(weight_pct, 2),
            "contribution":  contribution_breakdown.get(bucket, 0),
            "is_inverse":    bucket in inverse_vars,
        }

    return total, breakdown


# ─────────────────────────────────────────────────────────────────────────────
# RANKING PIPELINE
# ─────────────────────────────────────────────────────────────────────────────
def rank_projects(
    answers: dict,
    surviving_cities: list,
) -> tuple[list, list, dict, list, str]:
    """
    Full project engine pipeline.

    Steps:
      1. Hard filters  → surviving, eliminated
      2. Weight compute → normalized_weights + speculation_tag
      3. Pre-roll-up all survivors (one pass — avoids repeated rollup per project)
      4. Score each survivor against the peer group
      5. Sort descending, attach rank

    Returns:
        (ranked, eliminated, normalized_weights, weight_log, speculation_tag)

    ⚠️  BREAKING CHANGE from v1: now returns 5 values instead of 4.
        Update any callers that unpack exactly 4:
          OLD: ranked, elim, weights, log = rank_projects(...)
          NEW: ranked, elim, weights, log, spec_tag = rank_projects(...)
    """
    surviving, eliminated = apply_project_hard_filters(answers, surviving_cities)

    # compute_project_weights now returns 4 values (added speculation_tag)
    _, normalized_weights, weight_log, speculation_tag = compute_project_weights(answers)

    if not surviving:
        return [], eliminated, normalized_weights, weight_log, speculation_tag

    # Pre-compute bucket scores for all survivors in one pass
    # Caches result on each project dict to avoid re-rolling up per score call
    for project in surviving:
        if "bucket_scores" not in project:
            project["bucket_scores"] = _get_bucket_scores(project)

    # Score every survivor against the full peer group
    ranked = []
    for project in surviving:
        score, breakdown = score_project(
            project            = project,
            normalized_weights = normalized_weights,
            all_surviving      = surviving,
            speculation_tag    = speculation_tag,
        )
        ranked.append({
            **project,
            "project_score":    score,
            "score_breakdown":  breakdown,
            "speculation_tag":  speculation_tag,
        })

    ranked.sort(key=lambda x: x["project_score"], reverse=True)
    for i, p in enumerate(ranked, 1):
        p["rank"] = i

    return ranked, eliminated, normalized_weights, weight_log, speculation_tag