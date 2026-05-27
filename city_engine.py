# Data: V2 dataset (updated)
from simple_recommendation_engine.constants import CITY_INVERSE_VARS
from simple_recommendation_engine.normalization import (
    standardize_determinants,
    weighted_score,
)
from weights_config import compute_city_weights

CITIES = {
    "Athens": {
        "country": "Greece",
        "coastal": False,
        "scores": {
            "net_migration_rate": 0.62,        # (-0.10+0.5)/6.5*10
            "employment_growth": 4.63,          # (2.80-0.9)/4.1*10
            "price_appreciation_5y": 6.18,      # (61-14)/76*10
            "liquidity_indicator": 1.76,         # (8+4.2)/69.2*10
            "tourism_strength": 6.64,            # 16.80/25.3*10
            "rental_demand_index": 10.0,         # (93.70-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 9.60,    # direct
            "supply_pipeline": 8.90,             # inverted 3.32%: raw=1.10→10-1.10
            "quality_of_life_index": 3.91,       # (129.20-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": -0.001,
            "employment_growth_rate": 0.028,
            "price_appreciation_5y": 0.61,
            "transaction_volume_growth": 0.08,
            "tourism_strength_yoy": 0.168,
            "rental_demand_index": 93.7,
            "infrastructure_pipeline": 9.6,
            "supply_pipeline_pct": 0.0332,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.29,
        },
    },
    "Piraeus": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "net_migration_rate": 0.0,           # (-0.50+0.5)/6.5*10
            "employment_growth": 3.41,           # (2.30-0.9)/4.1*10
            "price_appreciation_5y": 5.0,        # (52-14)/76*10
            "liquidity_indicator": 1.33,          # (5+4.2)/69.2*10
            "tourism_strength": 10.0,             # 25.30/25.3*10
            "rental_demand_index": 8.19,          # (86.70-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 6.0,      # direct
            "supply_pipeline": 7.08,              # inverted 6.31%: raw=2.92→10-2.92
            "quality_of_life_index": 3.91,        # (129.20-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": -0.005,
            "employment_growth_rate": 0.023,
            "price_appreciation_5y": 0.52,
            "transaction_volume_growth": 0.05,
            "tourism_strength_yoy": 0.253,
            "rental_demand_index": 86.7,
            "infrastructure_pipeline": 6.0,
            "supply_pipeline_pct": 0.0631,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.40,
        },
    },
    "Crete": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "net_migration_rate": 1.23,           # (0.30+0.5)/6.5*10
            "employment_growth": 3.41,            # (2.30-0.9)/4.1*10
            "price_appreciation_5y": 4.87,        # (51-14)/76*10
            "liquidity_indicator": 1.47,           # (6+4.2)/69.2*10
            "tourism_strength": 2.21,              # 5.60/25.3*10
            "rental_demand_index": 6.80,           # (81.30-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 10.0,      # direct
            "supply_pipeline": 9.54,               # inverted 2.26%: raw=0.46→10-0.46
            "quality_of_life_index": 3.91,         # (129.20-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.003,
            "employment_growth_rate": 0.023,
            "price_appreciation_5y": 0.51,
            "transaction_volume_growth": 0.06,
            "tourism_strength_yoy": 0.056,
            "rental_demand_index": 81.3,
            "infrastructure_pipeline": 10.0,
            "supply_pipeline_pct": 0.0226,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.19,
        },
    },
    "Mykonos": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "net_migration_rate": 3.08,            # (1.50+0.5)/6.5*10
            "employment_growth": 7.56,             # (4.00-0.9)/4.1*10
            "price_appreciation_5y": 7.37,         # (70-14)/76*10
            "liquidity_indicator": 1.76,            # (8+4.2)/69.2*10
            "tourism_strength": 6.80,               # 17.20/25.3*10
            "rental_demand_index": 4.83,            # (73.70-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 6.60,       # direct
            "supply_pipeline": 7.62,                # inverted 5.42%: raw=2.38→10-2.38
            "quality_of_life_index": 3.91,          # (129.20-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.015,
            "employment_growth_rate": 0.040,
            "price_appreciation_5y": 0.70,
            "transaction_volume_growth": 0.08,
            "tourism_strength_yoy": 0.172,
            "rental_demand_index": 73.7,
            "infrastructure_pipeline": 6.6,
            "supply_pipeline_pct": 0.0542,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.10,
        },
    },
    "Thessaloniki": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "net_migration_rate": 1.38,             # (0.40+0.5)/6.5*10
            "employment_growth": 2.68,              # (2.00-0.9)/4.1*10
            "price_appreciation_5y": 9.47,          # (86-14)/76*10
            "liquidity_indicator": 2.05,             # (10+4.2)/69.2*10
            "tourism_strength": 3.48,                # 8.80/25.3*10
            "rental_demand_index": 7.75,             # (85.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 10.0,        # direct
            "supply_pipeline": 8.50,                 # inverted 3.98%: raw=1.50→10-1.50
            "quality_of_life_index": 4.29,           # (132.60-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.004,
            "employment_growth_rate": 0.020,
            "price_appreciation_5y": 0.86,
            "transaction_volume_growth": 0.10,
            "tourism_strength_yoy": 0.088,
            "rental_demand_index": 85.0,
            "infrastructure_pipeline": 10.0,
            "supply_pipeline_pct": 0.0398,
            "quality_of_life_index": 132.6,
            "vacancy_rate": 0.42,
        },
    },
    "Lisbon": {
        "country": "Portugal",
        "coastal": False,
        "scores": {
            "net_migration_rate": 1.49,              # (0.47+0.5)/6.5*10
            "employment_growth": 3.90,               # (2.50-0.9)/4.1*10
            "price_appreciation_5y": 6.71,           # (65-14)/76*10
            "liquidity_indicator": 0.46,              # (-1.00+4.2)/69.2*10
            "tourism_strength": 2.33,                 # 5.90/25.3*10
            "rental_demand_index": 7.75,              # (85.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 10.0,         # direct
            "supply_pipeline": 9.70,                  # inverted 2.00%: raw=0.30→10-0.30
            "quality_of_life_index": 6.99,            # (157.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.0047,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.65,
            "transaction_volume_growth": -0.01,
            "tourism_strength_yoy": 0.059,
            "rental_demand_index": 85.0,
            "infrastructure_pipeline": 10.0,
            "supply_pipeline_pct": 0.020,
            "quality_of_life_index": 157.0,
            "vacancy_rate": 0.22,
        },
    },
    "Cascais": {
        "country": "Portugal",
        "coastal": True,
        "scores": {
            "net_migration_rate": 2.46,               # (1.10+0.5)/6.5*10
            "employment_growth": 3.41,                # (2.30-0.9)/4.1*10
            "price_appreciation_5y": 5.39,            # (55-14)/76*10
            "liquidity_indicator": 0.39,               # (-1.50+4.2)/69.2*10
            "tourism_strength": 2.37,                  # 6.00/25.3*10
            "rental_demand_index": 5.17,               # (75.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 4.0,           # direct
            "supply_pipeline": 10.0,                   # inverted 1.50%: raw=0→10-0
            "quality_of_life_index": 7.66,             # (163.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.011,
            "employment_growth_rate": 0.023,
            "price_appreciation_5y": 0.55,
            "transaction_volume_growth": -0.015,
            "tourism_strength_yoy": 0.060,
            "rental_demand_index": 75.0,
            "infrastructure_pipeline": 4.0,
            "supply_pipeline_pct": 0.015,
            "quality_of_life_index": 163.0,
            "vacancy_rate": 0.37,
        },
    },
    "Algarve": {
        "country": "Portugal",
        "coastal": True,
        "scores": {
            "net_migration_rate": 2.77,                # (1.30+0.5)/6.5*10
            "employment_growth": 4.63,                 # (2.80-0.9)/4.1*10
            "price_appreciation_5y": 7.37,             # (70-14)/76*10
            "liquidity_indicator": 0.68,                # (0.50+4.2)/69.2*10
            "tourism_strength": 0.24,                   # 0.60/25.3*10
            "rental_demand_index": 3.36,                # (68.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 7.0,            # direct
            "supply_pipeline": 9.09,                    # inverted 3.00%: raw=0.91→10-0.91
            "quality_of_life_index": 8.10,              # (167.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.013,
            "employment_growth_rate": 0.028,
            "price_appreciation_5y": 0.70,
            "transaction_volume_growth": 0.005,
            "tourism_strength_yoy": 0.006,
            "rental_demand_index": 68.0,
            "infrastructure_pipeline": 7.0,
            "supply_pipeline_pct": 0.030,
            "quality_of_life_index": 167.0,
            "vacancy_rate": 0.48,
        },
    },
    "Braga": {
        "country": "Portugal",
        "coastal": False,
        "scores": {
            "net_migration_rate": 3.26,                 # (1.62+0.5)/6.5*10
            "employment_growth": 3.90,                  # (2.50-0.9)/4.1*10
            "price_appreciation_5y": 6.32,              # (62-14)/76*10
            "liquidity_indicator": 0.97,                 # (2.50+4.2)/69.2*10
            "tourism_strength": 3.28,                    # 8.30/25.3*10
            "rental_demand_index": 3.88,                 # (70.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 6.0,             # direct
            "supply_pipeline": 6.97,                     # inverted 6.50%: raw=3.03→10-3.03
            "quality_of_life_index": 9.99,               # (184.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.0162,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.62,
            "transaction_volume_growth": 0.025,
            "tourism_strength_yoy": 0.083,
            "rental_demand_index": 70.0,
            "infrastructure_pipeline": 6.0,
            "supply_pipeline_pct": 0.065,
            "quality_of_life_index": 184.0,
            "vacancy_rate": 0.18,
        },
    },
    "Porto": {
        "country": "Portugal",
        "coastal": True,
        "scores": {
            "net_migration_rate": 1.35,                  # (0.38+0.5)/6.5*10
            "employment_growth": 3.17,                   # (2.20-0.9)/4.1*10
            "price_appreciation_5y": 6.32,               # (62-14)/76*10
            "liquidity_indicator": 0.82,                  # (1.50+4.2)/69.2*10
            "tourism_strength": 3.28,                     # 8.30/25.3*10
            "rental_demand_index": 5.94,                  # (78.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 10.0,             # direct
            "supply_pipeline": 9.39,                      # inverted 2.50%: raw=0.61→10-0.61
            "quality_of_life_index": 9.21,                # (177.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.0038,
            "employment_growth_rate": 0.022,
            "price_appreciation_5y": 0.62,
            "transaction_volume_growth": 0.015,
            "tourism_strength_yoy": 0.083,
            "rental_demand_index": 78.0,
            "infrastructure_pipeline": 10.0,
            "supply_pipeline_pct": 0.025,
            "quality_of_life_index": 177.0,
            "vacancy_rate": 0.20,
        },
    },
    "Phuket": {
        "country": "Thailand",
        "coastal": True,
        "scores": {
            "net_migration_rate": 2.80,                   # (1.32+0.5)/6.5*10
            "employment_growth": 4.63,                    # (2.80-0.9)/4.1*10
            "price_appreciation_5y": 3.68,                # (42-14)/76*10
            "liquidity_indicator": 1.11,                   # (3.50+4.2)/69.2*10
            "tourism_strength": 7.27,                      # 18.40/25.3*10
            "rental_demand_index": 6.98,                   # (82.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 9.20,              # direct
            "supply_pipeline": 6.06,                       # inverted 8.00%: raw=3.94→10-3.94
            "quality_of_life_index": 1.48,                 # regional avg 107.23 (N/A in dataset)
        },
        "raw_values": {
            "population_growth_rate": 0.0132,
            "employment_growth_rate": 0.028,
            "price_appreciation_5y": 0.42,
            "transaction_volume_growth": 0.035,
            "tourism_strength_yoy": 0.184,
            "rental_demand_index": 82.0,
            "infrastructure_pipeline": 9.2,
            "supply_pipeline_pct": 0.080,
            "quality_of_life_index": None,  # N/A; regional proxy 107.23 used for scoring
            "vacancy_rate": 0.22,
        },
    },
    "Bangkok": {
        "country": "Thailand",
        "coastal": False,
        "scores": {
            "net_migration_rate": 2.98,                    # (1.44+0.5)/6.5*10
            "employment_growth": 1.71,                     # (1.60-0.9)/4.1*10
            "price_appreciation_5y": 0.53,                 # (18-14)/76*10
            "liquidity_indicator": 0.0,                     # (-4.20+4.2)/69.2*10
            "tourism_strength": 4.98,                       # 12.60/25.3*10
            "rental_demand_index": 4.91,                    # (74.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 10.0,               # direct
            "supply_pipeline": 0.0,                         # inverted 18.00%: raw=10.0→10-10
            "quality_of_life_index": 0.0,                   # (93.93-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.0144,
            "employment_growth_rate": 0.016,
            "price_appreciation_5y": 0.18,
            "transaction_volume_growth": -0.042,
            "tourism_strength_yoy": 0.126,
            "rental_demand_index": 74.0,
            "infrastructure_pipeline": 10.0,
            "supply_pipeline_pct": 0.180,
            "quality_of_life_index": 93.93,
            "vacancy_rate": 0.12,
        },
    },
    "Pattaya": {
        "country": "Thailand",
        "coastal": True,
        "scores": {
            "net_migration_rate": 2.46,                     # (1.10+0.5)/6.5*10
            "employment_growth": 2.93,                      # (2.10-0.9)/4.1*10
            "price_appreciation_5y": 1.05,                  # (22-14)/76*10
            "liquidity_indicator": 0.20,                     # (-2.80+4.2)/69.2*10
            "tourism_strength": 5.61,                        # 14.20/25.3*10
            "rental_demand_index": 4.13,                     # (71.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 6.40,                # direct
            "supply_pipeline": 1.82,                         # inverted 15.00%: raw=8.18→10-8.18
            "quality_of_life_index": 0.40,                   # (97.50-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.011,
            "employment_growth_rate": 0.021,
            "price_appreciation_5y": 0.22,
            "transaction_volume_growth": -0.028,
            "tourism_strength_yoy": 0.142,
            "rental_demand_index": 71.0,
            "infrastructure_pipeline": 6.4,
            "supply_pipeline_pct": 0.150,
            "quality_of_life_index": 97.5,
            "vacancy_rate": 0.28,
        },
    },
    "Chiang Mai": {
        "country": "Thailand",
        "coastal": False,
        "scores": {
            "net_migration_rate": 2.72,                      # (1.27+0.5)/6.5*10
            "employment_growth": 0.73,                       # (1.20-0.9)/4.1*10
            "price_appreciation_5y": 0.0,                    # (14-14)/76*10
            "liquidity_indicator": 0.16,                      # (-3.10+4.2)/69.2*10
            "tourism_strength": 4.27,                         # 10.80/25.3*10
            "rental_demand_index": 3.36,                      # (68.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 7.20,                 # direct
            "supply_pipeline": 6.67,                          # inverted 7.00%: raw=3.33→10-3.33
            "quality_of_life_index": 3.45,                    # (125.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.0127,
            "employment_growth_rate": 0.012,
            "price_appreciation_5y": 0.14,
            "transaction_volume_growth": -0.031,
            "tourism_strength_yoy": 0.108,
            "rental_demand_index": 68.0,
            "infrastructure_pipeline": 7.2,
            "supply_pipeline_pct": 0.070,
            "quality_of_life_index": 125.0,
            "vacancy_rate": 0.15,
        },
    },
    "Hua Hin": {
        "country": "Thailand",
        "coastal": True,
        "scores": {
            "net_migration_rate": 1.85,                       # (0.70+0.5)/6.5*10
            "employment_growth": 0.0,                         # (0.90-0.9)/4.1*10
            "price_appreciation_5y": 0.66,                    # (19-14)/76*10
            "liquidity_indicator": 0.87,                       # (1.80+4.2)/69.2*10
            "tourism_strength": 3.36,                          # 8.50/25.3*10
            "rental_demand_index": 2.07,                       # (63.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 4.80,                  # direct
            "supply_pipeline": 7.88,                           # inverted 5.00%: raw=2.12→10-2.12
            "quality_of_life_index": 2.06,                     # (112.50-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.007,
            "employment_growth_rate": 0.009,
            "price_appreciation_5y": 0.19,
            "transaction_volume_growth": 0.018,
            "tourism_strength_yoy": 0.085,
            "rental_demand_index": 63.0,
            "infrastructure_pipeline": 4.8,
            "supply_pipeline_pct": 0.050,
            "quality_of_life_index": 112.5,
            "vacancy_rate": 0.30,
        },
    },
    "Dubai": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "net_migration_rate": 7.54,                        # (4.40+0.5)/6.5*10
            "employment_growth": 7.56,                         # (4.00-0.9)/4.1*10
            "price_appreciation_5y": 8.68,                     # (80-14)/76*10
            "liquidity_indicator": 4.36,                        # (26+4.2)/69.2*10
            "tourism_strength": 4.35,                           # 11.00/25.3*10
            "rental_demand_index": 5.94,                        # (78.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 10.0,                   # direct
            "supply_pipeline": 2.73,                            # inverted 13.50%: raw=7.27→10-7.27
            "quality_of_life_index": 10.0,                      # (184.10-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.044,
            "employment_growth_rate": 0.040,
            "price_appreciation_5y": 0.80,
            "transaction_volume_growth": 0.26,
            "tourism_strength_yoy": 0.110,
            "rental_demand_index": 78.0,
            "infrastructure_pipeline": 10.0,
            "supply_pipeline_pct": 0.135,
            "quality_of_life_index": 184.1,
            "vacancy_rate": 0.09,
        },
    },
    "Abu Dhabi": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "net_migration_rate": 6.46,                         # (3.70+0.5)/6.5*10
            "employment_growth": 8.78,                          # (4.50-0.9)/4.1*10
            "price_appreciation_5y": 6.45,                      # (63-14)/76*10
            "liquidity_indicator": 6.10,                         # (38+4.2)/69.2*10
            "tourism_strength": 5.14,                            # 13.00/25.3*10
            "rental_demand_index": 4.39,                         # (72.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 9.0,                     # direct
            "supply_pipeline": 5.45,                             # inverted 9.00%: raw=4.55→10-4.55
            "quality_of_life_index": 8.50,                       # (170.60-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.037,
            "employment_growth_rate": 0.045,
            "price_appreciation_5y": 0.63,
            "transaction_volume_growth": 0.38,
            "tourism_strength_yoy": 0.130,
            "rental_demand_index": 72.0,
            "infrastructure_pipeline": 9.0,
            "supply_pipeline_pct": 0.090,
            "quality_of_life_index": 170.6,
            "vacancy_rate": 0.07,
        },
    },
    "Sharjah": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "net_migration_rate": 4.31,                          # (2.30+0.5)/6.5*10
            "employment_growth": 3.90,                           # (2.50-0.9)/4.1*10
            "price_appreciation_5y": 2.43,                       # (32.5-14)/76*10
            "liquidity_indicator": 6.10,                          # (38+4.2)/69.2*10
            "tourism_strength": 4.35,                             # 11.00/25.3*10
            "rental_demand_index": 2.58,                          # (65.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 7.0,                      # direct
            "supply_pipeline": 6.67,                              # inverted 7.00%: raw=3.33→10-3.33
            "quality_of_life_index": 4.89,                        # (138.00-93.93)/90.17*10
        },
        "raw_values": {
            "population_growth_rate": 0.023,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.325,
            "transaction_volume_growth": 0.38,
            "tourism_strength_yoy": 0.110,
            "rental_demand_index": 65.0,
            "infrastructure_pipeline": 7.0,
            "supply_pipeline_pct": 0.070,
            "quality_of_life_index": 138.0,
            "vacancy_rate": 0.165,
        },
    },
    "Ras Al Khaimah": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "net_migration_rate": 10.0,                           # (6.00+0.5)/6.5*10 = 10.0 (max)
            "employment_growth": 10.0,                            # (5.00-0.9)/4.1*10 = 10.0 (max)
            "price_appreciation_5y": 10.0,                        # (90-14)/76*10 = 10.0 (max)
            "liquidity_indicator": 10.0,                           # (65+4.2)/69.2*10 = 10.0 (max)
            "tourism_strength": 2.77,                              # 7.00/25.3*10
            "rental_demand_index": 3.88,                           # (70.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 9.0,                       # direct
            "supply_pipeline": 0.30,                               # inverted 17.50%: raw=9.70→10-9.70
            "quality_of_life_index": 7.80,                         # regional avg 164.23 (N/A in dataset)
        },
        "raw_values": {
            "population_growth_rate": 0.060,
            "employment_growth_rate": 0.050,
            "price_appreciation_5y": 0.90,
            "transaction_volume_growth": 0.65,
            "tourism_strength_yoy": 0.070,
            "rental_demand_index": 70.0,
            "infrastructure_pipeline": 9.0,
            "supply_pipeline_pct": 0.175,
            "quality_of_life_index": None,  # N/A; UAE regional proxy 164.23 used for scoring
            "vacancy_rate": 0.11,
        },
    },
    "Ajman": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "net_migration_rate": 6.15,                            # (3.50+0.5)/6.5*10
            "employment_growth": 3.90,                             # (2.50-0.9)/4.1*10
            "price_appreciation_5y": 1.78,                         # (27.5-14)/76*10
            "liquidity_indicator": 4.65,                            # (28+4.2)/69.2*10
            "tourism_strength": 0.0,                                # no official data → 0
            "rental_demand_index": 0.0,                             # (55.00-55)/38.7*10
            "rental_yield": 0,
            "infrastructure_pipeline": 5.0,                        # direct
            "supply_pipeline": 7.27,                                # inverted 6.00%: raw=2.73→10-2.73
            "quality_of_life_index": 7.80,                          # regional avg 164.23 (N/A in dataset)
        },
        "raw_values": {
            "population_growth_rate": 0.035,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.275,
            "transaction_volume_growth": 0.28,
            "tourism_strength_yoy": None,  # no official data
            "rental_demand_index": 55.0,
            "infrastructure_pipeline": 5.0,
            "supply_pipeline_pct": 0.060,
            "quality_of_life_index": None,  # N/A; UAE regional proxy 164.23 used for scoring
            "vacancy_rate": 0.20,
        },
    },
}


def score_city(city_name, normalized_weights, candidate_cities):
    """Score a city with z-score normalization and inverse supply handling."""
    data = CITIES[city_name]
    peer_scores = [CITIES[c]["scores"] for c in candidate_cities]
    standardized = standardize_determinants(
        data["scores"],
        peer_scores,
        normalized_weights.keys(),
        inverse_vars=CITY_INVERSE_VARS,
    )
    score, breakdown = weighted_score(standardized, normalized_weights)
    return score, breakdown, standardized


def rank_cities(surviving_countries, answers):
    """
    Returns ranked cities only within the surviving countries list.
    Returns (ranked_list, normalized_weights, weight_log)
    """
    _, normalized_weights, weight_log = compute_city_weights(answers)

    candidate_cities = [
        name for name, data in CITIES.items()
        if data["country"] in surviving_countries
    ]

    ranked = []
    for city in candidate_cities:
        score, breakdown, standardized = score_city(
            city, normalized_weights, candidate_cities
        )
        ranked.append({
            "city": city,
            "country": CITIES[city]["country"],
            "score": score,
            "breakdown": breakdown,
            "standardized_scores": standardized,
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked, normalized_weights, weight_log
