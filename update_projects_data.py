"""
Patches projects_data.py — replaces raw_variables for the 15 Excel projects
while preserving all metadata (project_name, price_range, tags, etc.)
and leaving sobha_hartland untouched.
"""
import pandas as pd
import importlib.util
import sys

sys.path.insert(0, ".")

def load_mod(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

EXCEL_TO_VAR = {
    "Micro Market Classification (30%)":                   "micro_market_stage",
    "Rental Absorption Velocity (20%)":                    "rental_absorption_velocity",
    "Days-on-Market (15%)":                                "days_on_market",
    "Occupancy / Vacancy Rates (15%)":                     "occupancy_vacancy_rate",
    "Resale Velocity (20%)":                               "resale_velocity",
    "Safety (30%)":                                        "safety_crime_index",
    "Air Quality (10%)":                                   "air_quality_index",
    "Healthcare Access (25%)":                             "healthcare_access",
    "School Quality (25%)":                                "school_quality",
    "Beach/Coastal Access (10%)":                          "beach_coastal_access",
    "Population Growth (60%)":                             "population_growth_rate",
    "Expat Concentration (40%)":                           "expat_concentration",
    "Active Unsold Inventory (40%)":                       "active_unsold_inventory",
    "Immediate Pipeline Risk (60%)":                       "immediate_pipeline_risk",
    "% Projects Delivered (35%)":                          "pct_projects_delivered",
    "Average Delay Duration (45%)":                        "average_delay_duration",
    "Completion Consistency (20%)":                        "completion_consistency",
    "Debt/Cash Position (30%)":                            "debt_cash_position",
    "Stalled Projects (20%)":                              "stalled_projects_count",
    "Project-level Escrow / Ring-fence (35%)":             "escrow_quality",
    "Pre-sales % Achieved (15%)":                          "presales_pct_achieved",
    "Construction Quality (100%)":                         "construction_quality",
    "Litigation History (100%)":                           "litigation_history",
    "Average Exit Velocity (70%)":                         "average_exit_velocity",
    "Flipping Frequency (30%)":                            "flipping_frequency",
    "Projected Rental Yield (100%)":                       "projected_rental_yield",
    "Infrastructure Proximity (1, 3, 5 Mi radius) (100%)": "infrastructure_proximity",
    "Capital Appreciation (1km radius comps) (50%)":       "comp_capital_appreciation",
    "Rental Yields (1km radius comps) (30%)":              "comp_rental_yields",
    "Occupancy/Vacancy Rates (20%)":                       "comp_occupancy_rate",
    "Investor-to-Owner Occupier Ratio (35%)":              "investor_owner_ratio",
    "Off-Plan vs Secondary Buyer Dominance (20%)":         "offplan_secondary_dominance",
    "Short-Term Rental Concentration (%) (45%)":           "str_concentration",
}

PROJECT_MAPPING = {
    "Burj Binghatti Jacob & Co Residences": "burj_binghatti",
    "DAMAC Islands":                         "damac_islands",
    "Dubai Creek Harbour":                   "dubai_creek",
    "Greencrest at Dubai Hills Estate":      "greencrest",
    "Noble Ploenchit":                       "noble_ploenchit",
    "The Monument Thong Lo":                 "monument_thong_lo",
    "HYTHE by Botanica":                     "hythe_by_botanica",
    "Laguna Lakelands":                      "laguna_lakelands",
    "One Athens":                            "one_athens",
    "LUX&EASY Thessaloniki":                 "luxeasy_thessaloniki",
    "Palmares Ocean Living & Golf Resort":   "palmares",
    "Amoreiras Prime Residences":            "amoreiras_prime",
    "Infante Residences":                    "infante_residences",
    "The Lisboans":                          "the_lisboans",
}

VAR_ORDER = list(EXCEL_TO_VAR.values())

# ── Parse Excel ────────────────────────────────────────────────────────────────
df = pd.read_excel(
    r"C:\Users\rhnku\Downloads\project_scores.xlsx",
    sheet_name="Database for Engine",
    header=None,
)
subvar_names = list(df.iloc[3, 2:])

excel_scores = {}
for i, row in df.iterrows():
    if i >= 4 and pd.notna(row[1]):
        proj_name = str(row[1]).strip()
        proj_key = PROJECT_MAPPING.get(proj_name)
        if proj_key is None and "ellinikon" in proj_name.lower():
            proj_key = "ellinikon_marina_residences"
        if proj_key is None:
            continue
        scores = {}
        for j, col_name in enumerate(subvar_names):
            var_name = EXCEL_TO_VAR.get(col_name)
            if var_name:
                val = row[j + 2]
                scores[var_name] = round(float(val), 4) if pd.notna(val) else None
        excel_scores[proj_key] = scores

# ── Load existing consolidated data ───────────────────────────────────────────
import projects_data as pd_mod

def raw_score(v):
    return v.get("score") if isinstance(v, dict) else v

sobha_raw = {
    k: raw_score(v)
    for k, v in pd_mod.PROJECTS["sobha_hartland"]["raw_variables"].items()
}

# ── Code generation ────────────────────────────────────────────────────────────
def fmt(v):
    if v is None:
        return "None"
    f = float(v)
    return str(int(f)) if f == int(f) else str(f)

def raw_block(scores, pad="            "):
    return "\n".join(f'{pad}"{var}": {fmt(scores.get(var))},' for var in VAR_ORDER)

def raw_block_plain(scores, pad="            "):
    return "\n".join(f'{pad}"{k}": {fmt(v)},' for k, v in scores.items())

def repr_val(v):
    if isinstance(v, list):
        items = ", ".join(repr(i) for i in v)
        return f"[{items}]"
    return repr(v)

def proj_entry(key, proj, scores, plain=False):
    meta_keys = [k for k in proj if k != "raw_variables"]
    meta_lines = "\n".join(f'        "{k}": {repr_val(proj[k])},' for k in meta_keys)
    rv = raw_block_plain(scores) if plain else raw_block(scores)
    return (
        f'    "{key}": {{\n'
        f'{meta_lines}\n\n'
        f'        "raw_variables": {{\n'
        f'{rv}\n'
        f'        }},\n'
        f'    }},'
    )

# ── Build file content ─────────────────────────────────────────────────────────
PROJ_ORDER = [
    "ellinikon_marina_residences", "one_athens", "luxeasy_thessaloniki",
    "palmares", "amoreiras_prime", "infante_residences", "the_lisboans",
    "monument_thong_lo", "noble_ploenchit", "hythe_by_botanica", "laguna_lakelands",
    "burj_binghatti", "damac_islands", "dubai_creek", "greencrest", "sobha_hartland",
]

entries = []
for key in PROJ_ORDER:
    proj = pd_mod.PROJECTS[key]
    if key == "sobha_hartland":
        entries.append(proj_entry(key, proj, sobha_raw, plain=True))
    else:
        entries.append(proj_entry(key, proj, excel_scores[key]))

content = (
    '"""\n'
    "projects_data.py — Consolidated project asset data for all four countries.\n"
    "Sources: project_scores.xlsx (Database for Engine tab) — June 2026 update.\n"
    "All raw_variables are 0-100 magnitude scores. Engine handles inversion.\n"
    '"""\n\n'
    "PROJECTS = {\n\n"
    + "\n\n".join(entries)
    + "\n\n}\n"
)

with open("projects_data.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Written: projects_data.py")
print(f"Projects updated: {len(excel_scores)}")
print(f"Projects preserved (sobha): 1")
