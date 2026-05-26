import ast
from pathlib import Path

source = Path(__file__).parent.joinpath("projects_data.py").read_text(encoding="utf-8")
ast.parse(source)
print("[OK] Syntax OK")

from projects_data import (
    PROJECTS,
    get_projects_by_cities,
    get_projects_by_country,
    list_determinant_keys,
)

REQUIRED_META = [
    "project_name", "country", "city", "price_range",
    "project_stage", "ownership", "project_type",
    "highlight", "description", "tags", "raw_variables",
]
VALID_COUNTRIES = {"Portugal", "UAE", "Greece", "Thailand"}
VALID_STAGES = {"Ready", "Under Construction", "Off-Plan"}
VALID_OWNERSHIP = {"freehold", "leasehold"}
VALID_TYPES = {"apartment", "villa", "branded", "managed"}
ALL_VARS = list_determinant_keys()

errors = []

for key, p in PROJECTS.items():
    for req in REQUIRED_META:
        if req not in p:
            errors.append(f"{key}: missing metadata key '{req}'")

    if p.get("country") not in VALID_COUNTRIES:
        errors.append(f"{key}: invalid country '{p.get('country')}'")

    if p.get("project_stage") not in VALID_STAGES:
        errors.append(f"{key}: invalid project_stage '{p.get('project_stage')}'")

    if p.get("ownership") not in VALID_OWNERSHIP:
        errors.append(f"{key}: invalid ownership '{p.get('ownership')}'")

    if p.get("project_type") not in VALID_TYPES:
        errors.append(f"{key}: invalid project_type '{p.get('project_type')}'")

    rv = p.get("raw_variables", {})
    for var in ALL_VARS:
        if var not in rv:
            errors.append(f"{key}: variable '{var}' missing from raw_variables entirely")

    for var, val in rv.items():
        if val is None:
            continue
        score = val["score"] if isinstance(val, dict) else val
        if score is not None and not (0 <= float(score) <= 100):
            errors.append(f"{key}.{var}: score {score} out of [0,100]")

if errors:
    print(f"\n[FAIL] VALIDATION FAILED - {len(errors)} errors:")
    for e in errors:
        print(f"  {e}")
else:
    print("[OK] All metadata and structure checks passed")

print(f"\nTotal projects: {len(PROJECTS)}")
for country in sorted(VALID_COUNTRIES):
    c = get_projects_by_country(country)
    print(f"  {country}: {len(c)} projects")

test_cities = ["Dubai", "Lisbon", "Athens", "Bangkok", "Phuket", "Porto"]
for city in test_cities:
    result = get_projects_by_cities([city])
    if result:
        print(f"  {city}: {len(result)} project(s)")

print(f"\nCoverage report ({len(ALL_VARS)} variables):")
rows = []
for key, p in PROJECTS.items():
    rv = p["raw_variables"]
    present = sum(1 for v in ALL_VARS if rv.get(v) is not None)
    null = len(ALL_VARS) - present
    pct = round(present / len(ALL_VARS) * 100, 1)
    rows.append((pct, p["project_name"], p["country"], present, null))

for pct, name, country, present, null in sorted(rows, reverse=True):
    print(f"  {name:<40} {country:<10} {present:>3}/{len(ALL_VARS)}  ({pct}%)")

print(f"\nVariables null for every property (data gaps):")
for var in ALL_VARS:
    all_null = all(p["raw_variables"].get(var) is None for p in PROJECTS.values())
    if all_null:
        print(f"  [GAP] {var}")

print("\n[OK] Validation complete")
