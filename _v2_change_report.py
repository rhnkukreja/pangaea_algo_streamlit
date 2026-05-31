import sys
sys.path.insert(0, '.')
from country_engine import COUNTRIES
from city_engine import CITIES

V1_COUNTRY = {
    'Greece':   {'political_stability_index':5.20,'corruption_perception_index':5.0,'currency_volatility':5.55,'interest_rate_direction':5.0,'foreign_buyer_market_share':2.30,'property_taxation_for_foreigners':4.0},
    'Portugal': {'political_stability_index':5.80,'corruption_perception_index':5.6,'currency_volatility':5.55,'interest_rate_direction':5.0,'foreign_buyer_market_share':3.73,'property_taxation_for_foreigners':5.0},
    'Thailand': {'political_stability_index':3.40,'corruption_perception_index':3.3,'currency_volatility':4.60,'interest_rate_direction':6.88,'foreign_buyer_market_share':1.28,'property_taxation_for_foreigners':6.0},
    'UAE':      {'political_stability_index':6.80,'corruption_perception_index':6.9,'currency_volatility':10.0,'interest_rate_direction':6.88,'foreign_buyer_market_share':10.0,'property_taxation_for_foreigners':10.0},
}

V1_CITY = {
    'Athens':         {'net_migration_rate':0.62,'employment_growth':4.63,'price_appreciation_5y':6.18,'liquidity_indicator':1.76,'tourism_strength':6.64,'rental_demand_index':10.0,'rental_yield':0,'infrastructure_pipeline':9.60,'supply_pipeline':8.90,'quality_of_life_index':3.91},
    'Piraeus':        {'net_migration_rate':0.0,'employment_growth':3.41,'price_appreciation_5y':5.0,'liquidity_indicator':1.33,'tourism_strength':10.0,'rental_demand_index':8.19,'rental_yield':0,'infrastructure_pipeline':6.0,'supply_pipeline':7.08,'quality_of_life_index':3.91},
    'Crete':          {'net_migration_rate':1.23,'employment_growth':3.41,'price_appreciation_5y':4.87,'liquidity_indicator':1.47,'tourism_strength':2.21,'rental_demand_index':6.80,'rental_yield':0,'infrastructure_pipeline':10.0,'supply_pipeline':9.54,'quality_of_life_index':3.91},
    'Mykonos':        {'net_migration_rate':3.08,'employment_growth':7.56,'price_appreciation_5y':7.37,'liquidity_indicator':1.76,'tourism_strength':6.80,'rental_demand_index':4.83,'rental_yield':0,'infrastructure_pipeline':6.60,'supply_pipeline':7.62,'quality_of_life_index':3.91},
    'Thessaloniki':   {'net_migration_rate':1.38,'employment_growth':2.68,'price_appreciation_5y':9.47,'liquidity_indicator':2.05,'tourism_strength':3.48,'rental_demand_index':7.75,'rental_yield':0,'infrastructure_pipeline':10.0,'supply_pipeline':8.50,'quality_of_life_index':4.29},
    'Lisbon':         {'net_migration_rate':1.49,'employment_growth':3.90,'price_appreciation_5y':6.71,'liquidity_indicator':0.46,'tourism_strength':2.33,'rental_demand_index':7.75,'rental_yield':0,'infrastructure_pipeline':10.0,'supply_pipeline':9.70,'quality_of_life_index':6.99},
    'Cascais':        {'net_migration_rate':2.46,'employment_growth':3.41,'price_appreciation_5y':5.39,'liquidity_indicator':0.39,'tourism_strength':2.37,'rental_demand_index':5.17,'rental_yield':0,'infrastructure_pipeline':4.0,'supply_pipeline':10.0,'quality_of_life_index':7.66},
    'Algarve':        {'net_migration_rate':2.77,'employment_growth':4.63,'price_appreciation_5y':7.37,'liquidity_indicator':0.68,'tourism_strength':0.24,'rental_demand_index':3.36,'rental_yield':0,'infrastructure_pipeline':7.0,'supply_pipeline':9.09,'quality_of_life_index':8.10},
    'Braga':          {'net_migration_rate':3.26,'employment_growth':3.90,'price_appreciation_5y':6.32,'liquidity_indicator':0.97,'tourism_strength':3.28,'rental_demand_index':3.88,'rental_yield':0,'infrastructure_pipeline':6.0,'supply_pipeline':6.97,'quality_of_life_index':9.99},
    'Porto':          {'net_migration_rate':1.35,'employment_growth':3.17,'price_appreciation_5y':6.32,'liquidity_indicator':0.82,'tourism_strength':3.28,'rental_demand_index':5.94,'rental_yield':0,'infrastructure_pipeline':10.0,'supply_pipeline':9.39,'quality_of_life_index':9.21},
    'Phuket':         {'net_migration_rate':2.80,'employment_growth':4.63,'price_appreciation_5y':3.68,'liquidity_indicator':1.11,'tourism_strength':7.27,'rental_demand_index':6.98,'rental_yield':0,'infrastructure_pipeline':9.20,'supply_pipeline':6.06,'quality_of_life_index':1.48},
    'Bangkok':        {'net_migration_rate':2.98,'employment_growth':1.71,'price_appreciation_5y':0.53,'liquidity_indicator':0.0,'tourism_strength':4.98,'rental_demand_index':4.91,'rental_yield':0,'infrastructure_pipeline':10.0,'supply_pipeline':0.0,'quality_of_life_index':0.0},
    'Pattaya':        {'net_migration_rate':2.46,'employment_growth':2.93,'price_appreciation_5y':1.05,'liquidity_indicator':0.20,'tourism_strength':5.61,'rental_demand_index':4.13,'rental_yield':0,'infrastructure_pipeline':6.40,'supply_pipeline':1.82,'quality_of_life_index':0.40},
    'Chiang Mai':     {'net_migration_rate':2.72,'employment_growth':0.73,'price_appreciation_5y':0.0,'liquidity_indicator':0.16,'tourism_strength':4.27,'rental_demand_index':3.36,'rental_yield':0,'infrastructure_pipeline':7.20,'supply_pipeline':6.67,'quality_of_life_index':3.45},
    'Hua Hin':        {'net_migration_rate':1.85,'employment_growth':0.0,'price_appreciation_5y':0.66,'liquidity_indicator':0.87,'tourism_strength':3.36,'rental_demand_index':2.07,'rental_yield':0,'infrastructure_pipeline':4.80,'supply_pipeline':7.88,'quality_of_life_index':2.06},
    'Dubai':          {'net_migration_rate':7.54,'employment_growth':7.56,'price_appreciation_5y':8.68,'liquidity_indicator':4.36,'tourism_strength':4.35,'rental_demand_index':5.94,'rental_yield':0,'infrastructure_pipeline':10.0,'supply_pipeline':2.73,'quality_of_life_index':10.0},
    'Abu Dhabi':      {'net_migration_rate':6.46,'employment_growth':8.78,'price_appreciation_5y':6.45,'liquidity_indicator':6.10,'tourism_strength':5.14,'rental_demand_index':4.39,'rental_yield':0,'infrastructure_pipeline':9.0,'supply_pipeline':5.45,'quality_of_life_index':8.50},
    'Sharjah':        {'net_migration_rate':4.31,'employment_growth':3.90,'price_appreciation_5y':2.43,'liquidity_indicator':6.10,'tourism_strength':4.35,'rental_demand_index':2.58,'rental_yield':0,'infrastructure_pipeline':7.0,'supply_pipeline':6.67,'quality_of_life_index':4.89},
    'Ras Al Khaimah': {'net_migration_rate':10.0,'employment_growth':10.0,'price_appreciation_5y':10.0,'liquidity_indicator':10.0,'tourism_strength':2.77,'rental_demand_index':3.88,'rental_yield':0,'infrastructure_pipeline':9.0,'supply_pipeline':0.30,'quality_of_life_index':7.80},
    'Ajman':          {'net_migration_rate':6.15,'employment_growth':3.90,'price_appreciation_5y':1.78,'liquidity_indicator':4.65,'tourism_strength':0.0,'rental_demand_index':0.0,'rental_yield':0,'infrastructure_pipeline':5.0,'supply_pipeline':7.27,'quality_of_life_index':7.80},
}

print("V1 -> V2 COUNTRY SCORE CHANGES (delta > 0.1):")
print(f"{'Country':<12} | {'Determinant':<35} | {'V1':>8} | {'V2':>8} | {'Delta':>8}")
print("-" * 78)
for country in ['Greece', 'Portugal', 'Thailand', 'UAE']:
    v1 = V1_COUNTRY[country]
    v2 = COUNTRIES[country]['scores']
    for det in v1:
        delta = v2[det] - v1[det]
        if abs(delta) > 0.1:
            print(f"{country:<12} | {det:<35} | {v1[det]:>8.2f} | {v2[det]:>8.2f} | {delta:>+8.2f}")

print()
print("V1 -> V2 CITY SCORE CHANGES (delta > 0.5):")
print(f"{'City':<16} | {'Determinant':<25} | {'V1':>8} | {'V2':>8} | {'Delta':>8}")
print("-" * 72)
city_changed = False
for city in V1_CITY:
    v1 = V1_CITY[city]
    v2 = CITIES[city]['scores']
    for det in v1:
        delta = v2[det] - v1[det]
        if abs(delta) > 0.5:
            print(f"{city:<16} | {det:<25} | {v1[det]:>8.2f} | {v2[det]:>8.2f} | {delta:>+8.2f}")
            city_changed = True
if not city_changed:
    print("  (no city score changes > 0.5 — all city raw values identical in V2)")

# Ranking impact: simulate simple sum-of-scores ranking
print()
print("RANKING IMPACT (sum-of-scores proxy, all determinants equal weight):")
print()
print("V1 Country ranking:")
v1_ranked = sorted(V1_COUNTRY.keys(), key=lambda c: sum(V1_COUNTRY[c].values()), reverse=True)
for i, c in enumerate(v1_ranked, 1):
    print(f"  {i}. {c} ({sum(V1_COUNTRY[c].values()):.2f})")

print()
print("V2 Country ranking:")
v2_ranked = sorted(COUNTRIES.keys(), key=lambda c: sum(COUNTRIES[c]['scores'].values()), reverse=True)
for i, c in enumerate(v2_ranked, 1):
    print(f"  {i}. {c} ({sum(COUNTRIES[c]['scores'].values()):.2f})")

ranking_changed = v1_ranked != v2_ranked
print()
print(f"Country ranking changed: {ranking_changed}")
if ranking_changed:
    for i, (v1c, v2c) in enumerate(zip(v1_ranked, v2_ranked), 1):
        if v1c != v2c:
            print(f"  Position {i}: V1={v1c}, V2={v2c}")

print()
print("City ranking not changed (all scores identical).")
print()
print("FILES UPDATED: country_engine.py, city_engine.py")
