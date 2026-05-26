#!/usr/bin/env python3
"""Audit country source files and build consolidated projects_data.py."""
from __future__ import annotations

import ast
import importlib.util
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# ── Canonical variable list (31) ─────────────────────────────────────────────
ALL_VARS = [
    "micro_market_stage", "rental_absorption_velocity", "resale_velocity",
    "days_on_market", "occupancy_vacancy_rate",
    "safety_crime_index", "healthcare_access", "school_quality",
    "air_quality_index", "beach_coastal_access",
    "population_growth_rate", "expat_concentration",
    "immediate_pipeline_risk", "active_unsold_inventory",
    "average_delay_duration", "pct_projects_delivered", "completion_consistency",
    "escrow_quality", "debt_cash_position", "stalled_projects_count",
    "presales_pct_achieved",
    "comp_capital_appreciation", "comp_rental_yields", "comp_occupancy_rate",
    "projected_rental_yield", "construction_quality", "litigation_history",
    "infrastructure_proximity",
    "str_concentration", "investor_owner_ratio", "offplan_secondary_dominance",
    "average_exit_velocity", "flipping_frequency",
]

LEGACY_VAR_MAP = {
    "delivery_history": "pct_projects_delivered",
    "expected_rental_yield": "projected_rental_yield",
    "project_exit_liquidity": "average_exit_velocity",
    "financial_strength": "debt_cash_position",
    "public_infrastructure_proximity": "infrastructure_proximity",
    "project_completion_rate": "completion_consistency",
}

REQUIRED_META = [
    "project_name", "country", "city", "price_range", "project_stage",
    "ownership", "project_type", "highlight", "description", "tags", "raw_variables",
]

# Legacy key -> new key for metadata from old projects_data.py
LEGACY_PROJECT_KEYS = {
    "luxeasy_thessaloniki": "luxeasy",
    "ellinikon_marina_residences": "ellinikon",
    "amoreiras_prime": "amoreiras",
    "infante_residences": "infante",
    "laguna_lakelands": "laguna",
    "hythe_by_botanica": "hythe",
    "noble_ploenchit": "noble",
    "monument_thong_lo": "monument",
}

COUNTRY_FILES = [
    ("Greece", ROOT / "projects_data" / "projects_greece.py", "projects_data"),
    ("Portugal", ROOT / "projects_data" / "projects_portugal.py", "projects_data"),
    ("Thailand", ROOT / "projects_data" / "projects_thailand.py", "THAILAND_RESEARCH"),
    ("UAE", ROOT / "projects_data" / "projects_uae.py", "UAE_PROPERTIES_RAW"),
]

# ── Load legacy metadata from existing projects_data.py ───────────────────────
def _load_legacy_projects() -> dict:
    legacy_path = ROOT / "legacy_projects_data_backup.py"
    if not legacy_path.exists():
        raise FileNotFoundError(
            "legacy_projects_data_backup.py missing — run: "
            "git show HEAD:projects_data.py > legacy_projects_data_backup.py"
        )
    spec = importlib.util.spec_from_file_location("legacy_pd", legacy_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.PROJECTS


def _load_source_dict(path: Path, attr: str) -> dict:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, attr)


def _norm_stage(raw: str) -> str:
    s = (raw or "").strip().lower()
    if "ready" in s:
        return "Ready"
    if "off" in s and "plan" in s:
        return "Off-Plan"
    if "construction" in s:
        return "Under Construction"
    return raw or "Ready"


def _norm_ownership(raw: str) -> str:
    return (raw or "freehold").strip().lower()


def _norm_project_type(raw: str, key: str = "", tags: list | None = None) -> str:
    s = (raw or "").strip().lower()
    tag_text = " ".join(tags or []).lower()
    if key == "burj_binghatti" or "branded" in s or "branded" in tag_text:
        return "branded"
    if "villa" in s:
        return "villa"
    if "managed" in s or "resort" in s or "hospitality" in s or "mixed-use" in s:
        return "managed"
    return "apartment"


def _extract_score(val: Any) -> tuple[float | None, str | None]:
    if val is None:
        return None, None
    if isinstance(val, dict):
        sc = val.get("score")
        if sc is None:
            return None, "missing score key"
        if isinstance(sc, str):
            return None, f"score is string: {sc!r}"
        try:
            return float(sc), None
        except (TypeError, ValueError):
            return None, f"non-numeric score: {sc!r}"
    try:
        return float(val), None
    except (TypeError, ValueError):
        return None, f"non-numeric: {val!r}"


def _resolve_raw_variables(rv: dict) -> tuple[dict, list[str]]:
    """Apply legacy renames; return canonical 31-key dict."""
    renames: list[str] = []
    merged: dict[str, Any] = {}

    for k, v in rv.items():
        canon = LEGACY_VAR_MAP.get(k, k)
        if k in LEGACY_VAR_MAP:
            renames.append(f"{k} → {canon}")
        if canon in merged and k != canon:
            continue  # keep first; new key wins later
        merged[canon] = v

    # new keys override legacy aliases
    for k, v in rv.items():
        if k not in LEGACY_VAR_MAP:
            merged[k] = v

    out: dict[str, Any] = {}
    for var in ALL_VARS:
        out[var] = merged.get(var)
    return out, renames


def _format_value(val: Any, indent: str) -> str:
    if val is None:
        return "None"
    if isinstance(val, dict):
        score = val.get("score")
        note = val.get("source_note", "")
        if isinstance(note, tuple):
            note = "".join(note)
        note = note.replace("\\", "\\\\").replace('"', '\\"')
        if "\n" in note:
            # multiline — use parens concat style from source
            parts = [p.strip() for p in note.replace("\n", " ").split('"') if p.strip()]
            note_repr = '"' + note.replace('"', '\\"') + '"'
        else:
            note_repr = json_escape(note) if False else repr(note)
        lines = [
            f"{indent}{{",
            f'{indent}    "score": {score!r},',
            f'{indent}    "source_note": {note_repr},',
            f"{indent}}},",
        ]
        return "\n".join(lines)
    return repr(val) + ","


def json_escape(s: str) -> str:
    return repr(s)


def _format_raw_variables(rv: dict, base_indent: str = "        ") -> str:
    lines = [f'{base_indent}"raw_variables": {{']
    for var in ALL_VARS:
        val = rv.get(var)
        if val is None:
            lines.append(f"{base_indent}    {var!r}: None,")
        elif isinstance(val, dict):
            score = val["score"]
            note = val.get("source_note", "")
            if isinstance(note, tuple):
                note = "".join(note)
            lines.append(f"{base_indent}    {var!r}: {{")
            lines.append(f'{base_indent}        "score": {score},')
            # preserve long notes with implicit concat if needed
            note_lines = _format_source_note(note, base_indent + "        ")
            lines.append(note_lines)
            lines.append(f"{base_indent}    }},")
        else:
            lines.append(f"{base_indent}    {var!r}: {val!r},")
    lines.append(f"{base_indent}}},")
    return "\n".join(lines)


def _format_source_note(note: str, indent: str) -> str:
    """Format source_note; use paren-wrapped strings if very long."""
    if len(note) < 120 and "\n" not in note:
        return f'{indent}"source_note": {note!r},'
    # split into ~80 char chunks for readability
    return f'{indent}"source_note": {note!r},'


def _extract_raw_block_text(source: str, prop_key: str) -> str | None:
    """Extract raw_variables block text from source file preserving comments."""
    pattern = rf'"{re.escape(prop_key)}"\s*:\s*\{{'
    m = re.search(pattern, source)
    if not m:
        return None
    # find "raw_variables": {
    rv_m = re.search(r'"raw_variables"\s*:\s*\{', source[m.start():])
    if not rv_m:
        return None
    start = m.start() + rv_m.end() - 1
    depth = 0
    i = start
    while i < len(source):
        c = source[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return source[start + 1 : i]  # inner content
        i += 1
    return None


def _inject_missing_keys(rv_inner: str, present: set[str], missing: list[str]) -> str:
    """Append None entries for missing canonical keys before closing."""
    if not missing:
        return rv_inner
    additions = "\n".join(f'            "{v}": None,' for v in missing)
    return rv_inner.rstrip() + "\n\n            # ── Variables not in source research file ──\n" + additions + "\n"


def _rename_keys_in_text(rv_inner: str, renames: list[str]) -> str:
    out = rv_inner
    for old, new in LEGACY_VAR_MAP.items():
        out = re.sub(rf'"{re.escape(old)}"\s*:', f'"{new}":', out)
    return out


def main():
    legacy = _load_legacy_projects()
    audit = {
        "metadata_issues": [],
        "placeholders": [],
        "score_flags": [],
        "malformed": [],
        "renames": [],
        "coverage": [],
    }
    consolidated: list[tuple[str, str, dict]] = []  # country, key, project

    for expected_country, path, attr in COUNTRY_FILES:
        source_text = path.read_text(encoding="utf-8")
        data = _load_source_dict(path, attr)

        for key, proj in data.items():
            country = proj.get("country", "")
            if country != expected_country:
                audit["metadata_issues"].append(
                    f"{key}: country={country!r} in file for {expected_country}"
                )

            # metadata from legacy
            legacy_key = LEGACY_PROJECT_KEYS.get(key, key)
            meta_src = legacy.get(legacy_key, {})

            meta = {
                "project_name": proj.get("project_name") or meta_src.get("project_name", key),
                "country": expected_country,
                "city": meta_src.get("city") or proj.get("city", ""),
                "price_range": meta_src.get("price_range", ""),
                "project_stage": _norm_stage(meta_src.get("project_stage", proj.get("project_stage", ""))),
                "ownership": _norm_ownership(meta_src.get("ownership", "")),
                "project_type": _norm_project_type(
                    meta_src.get("project_type", ""),
                    key=key,
                    tags=meta_src.get("tags"),
                ),
                "highlight": meta_src.get("highlight", ""),
                "description": meta_src.get("description", ""),
                "tags": meta_src.get("tags", []),
            }

            # city overrides
            if key == "palmares":
                meta["city"] = "Algarve"
            elif key == "infante_residences":
                meta["city"] = "Lisbon"

            for req in REQUIRED_META:
                if req == "raw_variables":
                    continue
                if not meta.get(req):
                    if req == "tags":
                        meta[req] = []
                    else:
                        meta[req] = f"PLACEHOLDER — needs review ({key})"
                        audit["placeholders"].append(f"{key}: missing {req}, added TODO placeholder")
                        meta[f"_{req}_todo"] = True

            rv_raw = proj.get("raw_variables", {})
            rv, renames = _resolve_raw_variables(rv_raw)
            for r in renames:
                audit["renames"].append(f"{key}: {r}")

            present = {v for v in ALL_VARS if rv[v] is not None}
            nulls = len(ALL_VARS) - len(present)
            pct = round(len(present) / len(ALL_VARS) * 100, 1)
            audit["coverage"].append((pct, meta["project_name"], expected_country, len(present), nulls))

            for var in ALL_VARS:
                val = rv[var]
                if val is None:
                    continue
                score, err = _extract_score(val)
                if err:
                    audit["malformed"].append(f"{key}.{var}: {err}")
                elif score is not None and not (0 <= score <= 100):
                    audit["score_flags"].append(f"{key}.{var}: score {score} outside [0,100]")

            # extract raw block with comments
            rv_inner = _extract_raw_block_text(source_text, key)
            if rv_inner:
                rv_inner = _rename_keys_in_text(rv_inner, renames)
                missing = [v for v in ALL_VARS if v not in present and v not in rv_raw and LEGACY_VAR_MAP.get(v) not in rv_raw]
                # also check renamed
                present_in_text = set(re.findall(r'"([a-z_]+)"\s*:', rv_inner))
                still_missing = [v for v in ALL_VARS if v not in present_in_text and rv[v] is None]
                rv_inner = _inject_missing_keys(rv_inner, present_in_text, still_missing)
            else:
                rv_inner = None

            consolidated.append((expected_country, key, meta, rv, rv_inner))

    # Sort: country alpha, then city
    consolidated.sort(key=lambda x: (x[0], x[2]["city"], x[1]))

    # Write output file
    out_lines = [
        '"""',
        "projects_data.py — Consolidated project asset data for all four countries.",
        "Sources: projects_data/projects_portugal.py, projects_data/projects_uae.py,",
        "         projects_data/projects_greece.py, projects_data/projects_thailand.py",
        "",
        "Raw variables use 0–100 magnitude scoring:",
        "  Higher always means MORE of that thing, good or bad.",
        "  The engine handles inversion mathematically.",
        "  Missing variables are set to None — the engine outputs 50 (neutral) for these.",
        '"""',
        "",
        "PROJECTS = {",
    ]

    current_country = None
    for country, key, meta, rv, rv_inner in consolidated:
        if country != current_country:
            current_country = country
            out_lines.append("")
            out_lines.append(f"    # ── {country.upper()} " + "─" * (55 - len(country)))

        out_lines.append("")
        out_lines.append(f'    "{key}": {{')
        for mk in ["project_name", "country", "city", "price_range", "project_stage",
                   "ownership", "project_type", "highlight", "description"]:
            val = meta[mk]
            todo = meta.get(f"_{mk}_todo")
            suffix = "  # TODO: placeholder — verify with research team" if todo else ""
            if isinstance(val, str):
                out_lines.append(f'        "{mk}": {val!r},{suffix}')
            else:
                out_lines.append(f'        "{mk}": {val!r},')
        tags = meta["tags"]
        out_lines.append(f'        "tags": {tags!r},')

        if rv_inner:
            out_lines.append('        "raw_variables": {')
            # indent inner content
            for line in rv_inner.splitlines():
                if line.strip():
                    out_lines.append("    " + line if not line.startswith("            ") else line)
                else:
                    out_lines.append("")
            out_lines.append("        },")
        else:
            out_lines.append(_format_raw_variables(rv, "        "))
        out_lines.append("    },")

    out_lines.extend([
        "",
        "}",
        "",
        "",
        "def get_projects_by_cities(city_list: list) -> dict:",
        '    """Return only projects whose city is in city_list."""',
        "    return {k: v for k, v in PROJECTS.items() if v[\"city\"] in city_list}",
        "",
        "",
        "def get_projects_by_country(country: str) -> dict:",
        '    """Return only projects for a specific country."""',
        "    return {k: v for k, v in PROJECTS.items() if v[\"country\"] == country}",
        "",
        "",
        "def list_determinant_keys() -> list:",
        '    """Return the canonical list of 31 raw variable keys in bucket order."""',
        "    return [",
    ])
    # helper list
    groups = [
        ("# Demand & Liquidity", 0, 5),
        ("# Neighborhood Livability", 5, 10),
        ("# Demographic & Economic", 10, 12),
        ("# Supply Pressure", 12, 14),
        ("# Delivery Track Record", 14, 17),
        ("# Financial Credibility", 17, 21),
        ("# Comp Market", 21, 24),
        ("# Single-variable buckets", 24, 28),
        ("# Speculation Risk", 28, 31),
        ("# Exit Liquidity", 31, 33),
    ]
    for comment, start, end in groups:
        out_lines.append(f"        {comment}")
        chunk = ALL_VARS[start:end]
        if chunk:
            line = ", ".join(f'"{v}"' for v in chunk)
            out_lines.append(f"        {line},")
    out_lines.append("    ]")
    out_lines.append("")

    out_path = ROOT / "projects_data.py"
    out_path.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote {out_path}")

    # Print audit report
    countries = {}
    for c, k, *_ in consolidated:
        countries[c] = countries.get(c, 0) + 1

    print("\n" + "=" * 70)
    print("AUDIT REPORT")
    print("=" * 70)
    print(f"\nPROPERTIES CONSOLIDATED: {len(consolidated)} total")
    for c in sorted(countries):
        print(f"  {c}: {countries[c]} properties")

    print("\nMETADATA ISSUES:")
    if audit["metadata_issues"]:
        for x in audit["metadata_issues"]:
            print(f"  - {x}")
    else:
        print("  (none)")

    print("\nPLACEHOLDERS ADDED:")
    if audit["placeholders"]:
        for x in audit["placeholders"]:
            print(f"  - {x}")
    else:
        print("  (none — all metadata sourced from legacy projects_data.py)")

    print("\nDATA ISSUES — scores outside [0,100]:")
    if audit["score_flags"]:
        for x in audit["score_flags"]:
            print(f"  - {x}")
    else:
        print("  (none)")

    print("\nMALFORMED VARIABLES:")
    if audit["malformed"]:
        for x in audit["malformed"]:
            print(f"  - {x}")
    else:
        print("  (none)")

    print("\nLEGACY KEYS RENAMED:")
    if audit["renames"]:
        for x in audit["renames"]:
            print(f"  - {x}")
    else:
        print("  (none found in source files)")

    print("\nCOVERAGE SUMMARY (per property):")
    print(f"  {'Property':<42} {'Country':<10} {'Present':>8} {'Null':>5} {'Coverage':>8}")
    print("  " + "-" * 78)
    for pct, name, country, present, null in sorted(audit["coverage"], reverse=True):
        print(f"  {name:<42} {country:<10} {present:>3}/31   {null:>5}   {pct:>6.1f}%")

    # Coverage during consolidation
    print("\n  Per-property detail (audit step 2D):")
    for pct, name, country, present, null in sorted(audit["coverage"], reverse=True):
        print(f"  {name} | {country} | Variables present: {present} | Variables null: {null} | Coverage %: {pct}")

    return audit


if __name__ == "__main__":
    main()
