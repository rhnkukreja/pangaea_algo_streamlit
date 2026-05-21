"""Hard-constraint filters shared by the recommendation engines."""

from __future__ import annotations

from typing import Mapping


def apply_country_constraints(
    countries: Mapping[str, Mapping],
    answers: Mapping,
) -> tuple[list[str], list[dict]]:
    """Apply mandatory country filters before scoring."""
    surviving = []
    eliminated = []

    for name, data in countries.items():
        dtaa_required = answers.get("dtaa_required", answers.get("tax_treaty_required", True))
        if dtaa_required and not data.get("dtaa_india", False):
            eliminated.append({"country": name, "reason": "No DTAA with India"})
            continue

        residency_objective = answers.get("primary_objective") == "residency_citizenship"
        if (
            (answers.get("visa_required") == "mandatory" or residency_objective)
            and not data.get("golden_visa_available", False)
        ):
            eliminated.append({"country": name, "reason": "Does not offer Golden Visa / residency"})
            continue

        if answers.get("citizenship_required") == "yes" and not data.get("citizenship_available", False):
            eliminated.append({"country": name, "reason": "Does not offer a citizenship pathway"})
            continue

        if (
            answers.get("ownership_structure", "any") == "freehold_only"
            and not data.get("foreign_freehold_allowed", False)
        ):
            eliminated.append({
                "country": name,
                "reason": "Investor requires freehold ownership",
            })
            continue

        surviving.append(name)

    return surviving, eliminated
