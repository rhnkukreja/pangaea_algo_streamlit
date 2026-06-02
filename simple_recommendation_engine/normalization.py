"""
normalization.py — Pangaea Advisory Recommendation Engine
Track B: Data Standardization + Track C: Convergence

KEY ARCHITECTURE DECISION:
  All raw data is stored as pure MAGNITUDE (0–100 scale).
  Higher always means "more of that thing" — good or bad.
  Examples:
    Construction Delay: 100 = maximum delay (bad)
    Rental Yield:       100 = maximum yield  (good)
    Litigation Risk:    100 = maximum risk   (bad)

  Inversion is handled HERE at the engine score step via bifurcation:
    STANDARD vars: Engine_Score = 50 + (z × 25)  → high raw = high score
    INVERSE vars:  Engine_Score = 50 - (z × 25)  → high raw = low score

  DO NOT pre-flip data before passing to these functions.
  DO NOT store "clean record" proxies — store raw risk magnitude.
"""


def standardize_determinants(scores, peer_scores, determinants, inverse_vars, passthrough_vars=None):
    """
    Track B: Z-score standardization with winsorization and engine score mapping.

    Args:
        scores           : dict {determinant: value} for the entity being scored.
        peer_scores      : list of dicts — ALL peers in the surviving group,
                           INCLUDING the entity being scored itself.
                           ⚠️  Omitting self from peer_scores shifts μ and breaks z-scores.
        determinants     : list/iterable of determinant keys to process.
        inverse_vars     : set of determinant keys where high raw value = bad outcome.
                           These get Engine_Score = 50 - (z × 25) instead of 50 + (z × 25).
                           Pass set() if all variables are already correctly oriented.
        passthrough_vars : set of determinant keys whose scores dict value is used
                           directly as the engine score, skipping z-score normalization.

    Returns:
        dict {determinant: engine_score}
        Each engine_score is a float in [0, 100].
        Returns 50.0 (neutral) for any determinant with insufficient peer data.
    """
    if passthrough_vars is None:
        passthrough_vars = set()

    result = {}

    for det in determinants:
        if det in passthrough_vars:
            result[det] = max(0.0, min(100.0, scores.get(det, 50.0)))
            continue
        # ── Collect peer values (self must be included in peer_scores) ──────
        all_vals = [p[det] for p in peer_scores if det in p and p[det] is not None]

        # ── Fix #3: Zero-variance / insufficient data fallback ───────────────
        if len(all_vals) < 2:
            result[det] = 50.0
            continue

        # ── Z-score (population std — no Bessel correction) ──────────────────
        n = len(all_vals)
        mu = sum(all_vals) / n
        sigma = (sum((x - mu) ** 2 for x in all_vals) / n) ** 0.5

        # Fix #3: zero-variance guard
        if sigma == 0:
            result[det] = 50.0
            continue

        self_val = scores.get(det)
        if self_val is None:
            result[det] = 50.0
            continue

        z = (self_val - mu) / sigma

        # ── Winsorize ─────────────────────────────────────────────────────────
        z = max(-2.0, min(2.0, z))

        # ── Fix #4: Bifurcated engine score mapping ───────────────────────────
        # STANDARD: high raw = good outcome → high score
        # INVERSE:  high raw = bad outcome  → low score
        if det in inverse_vars:
            engine_score = 50.0 - (z * 25.0)
        else:
            engine_score = 50.0 + (z * 25.0)

        # Final clamp — mathematically redundant after winsorization
        # but acts as a safety net for floating point edge cases
        result[det] = max(0.0, min(100.0, engine_score))

    return result


def weighted_score(standardized, normalized_weights):
    """
    Track C: Dot product convergence.

    Args:
        standardized       : dict {determinant: engine_score}  each in [0, 100]
        normalized_weights : dict {determinant: weight_pct}    must sum to 100
                             (or sum to 1.0 — both formats handled below)

    Returns:
        (final_score, breakdown)
          final_score : float in [0, 100]
          breakdown   : dict {determinant: contribution}
                        contribution = (engine_score / 100) × weight_pct

    Fix #5 note: dividing engine_score by 100 before multiplying by weight_pct
    ensures the final score lands in [0, 100] not [0, 10000].
    """
    # Auto-detect weight format: if weights sum to ~1.0, scale to 100
    weight_sum = sum(normalized_weights.values())
    scale = 100.0 if weight_sum <= 1.01 else 1.0

    total = 0.0
    breakdown = {}

    for det, weight_pct in normalized_weights.items():
        engine_score = standardized.get(det, 50.0)
        # Fix #5: divide by 100 so (engine_score/100) × weight_pct → [0, 100]
        contribution = (engine_score / 100.0) * (weight_pct * scale)
        breakdown[det] = round(contribution, 2)
        total += contribution

    return round(total, 2), breakdown


def winsorize(z: float, floor: float = -2.0, ceiling: float = 2.0) -> float:
    """
    Clamp a z-score to [floor, ceiling].
    Exported for use in archetype_mapper and other modules.
    """
    return max(floor, min(ceiling, z))