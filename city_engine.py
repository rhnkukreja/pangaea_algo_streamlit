# Data: V2 dataset (updated)
from simple_recommendation_engine.normalization import weighted_score
from weights_config import compute_city_weights

CITIES = {
    "Athens": {
        "country": "Greece",
        "coastal": False,
        "scores": {
            "population_growth": 23.10,        # V2 z-score engine score (raw: 23.10%)
            "employment_growth": 52.10,          # V2 z-score engine score (raw: 52.10%)
            "price_appreciation_5y": 62.05,      # V2 z-score engine score (raw: 61.00%)
            "transaction_volume_growth": 45.13,         # (8+4.2)/69.2*10
            "tourism_strength": 77.94,            # V2 z-score engine score (raw: 77.94%)
            "rental_demand_index": 100.00,         # V2 z-score engine score (raw index: 100.00)
            "macro_infra_pipeline": 72.64,    # V2 z-score engine score (raw: 72.64)
            "supply_pipeline": 69.35,             # V2 z-score engine score (raw: 69.35%) — inverse var
            "vacancy_rate": 40.71,               # V2 z-score engine score (raw: 29.00%) — inverse var
            "quality_of_life_index": 40.39,       # V2 z-score engine score (raw index: 129.20)
        },
        "raw_values": {
            "population_growth_rate": -0.001,
            "employment_growth_rate": 0.028,
            "price_appreciation_5y": 0.61,
            "transaction_volume_growth": 0.08,
            "tourism_strength_yoy": 0.168,
            "rental_demand_index": 93.7,
            "macro_infra_pipeline": 9.6,
            "supply_pipeline_pct": 0.0332,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.29,
        },
    },
    "Piraeus": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "population_growth": 16.80,           # V2 z-score engine score (raw: 16.80%)
            "employment_growth": 39.73,           # V2 z-score engine score (raw: 39.73%)
            "price_appreciation_5y": 51.52,        # V2 z-score engine score (raw: 52.00%)
            "transaction_volume_growth": 40.9,          # (5+4.2)/69.2*10
            "tourism_strength": 100.00,             # V2 z-score engine score (raw: 100.00%)
            "rental_demand_index": 88.09,          # V2 z-score engine score (raw index: 88.09)
            "macro_infra_pipeline": 27.61,      # V2 z-score engine score (raw: 27.61)
            "supply_pipeline": 54.20,              # V2 z-score engine score (raw: 54.20%) — inverse var
            "vacancy_rate": 17.89,               # V2 z-score engine score (raw: 40.00%) — inverse var
            "quality_of_life_index": 40.39,        # V2 z-score engine score (raw index: 129.20)
        },
        "raw_values": {
            "population_growth_rate": -0.005,
            "employment_growth_rate": 0.023,
            "price_appreciation_5y": 0.52,
            "transaction_volume_growth": 0.05,
            "tourism_strength_yoy": 0.253,
            "rental_demand_index": 86.7,
            "macro_infra_pipeline": 6.0,
            "supply_pipeline_pct": 0.0631,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.40,
        },
    },
    "Crete": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "population_growth": 29.40,           # V2 z-score engine score (raw: 29.40%)
            "employment_growth": 39.73,            # V2 z-score engine score (raw: 39.73%)
            "price_appreciation_5y": 50.35,        # V2 z-score engine score (raw: 51.00%)
            "transaction_volume_growth": 42.31,           # (6+4.2)/69.2*10
            "tourism_strength": 30.43,              # V2 z-score engine score (raw: 30.43%)
            "rental_demand_index": 73.43,           # V2 z-score engine score (raw index: 73.43)
            "macro_infra_pipeline": 77.64,      # V2 z-score engine score (raw: 77.64)
            "supply_pipeline": 74.72,               # V2 z-score engine score (raw: 74.72%) — inverse var
            "vacancy_rate": 61.47,               # V2 z-score engine score (raw: 19.00%) — inverse var
            "quality_of_life_index": 40.39,         # V2 z-score engine score (raw index: 129.20)
        },
        "raw_values": {
            "population_growth_rate": 0.003,
            "employment_growth_rate": 0.023,
            "price_appreciation_5y": 0.51,
            "transaction_volume_growth": 0.06,
            "tourism_strength_yoy": 0.056,
            "rental_demand_index": 81.3,
            "macro_infra_pipeline": 10.0,
            "supply_pipeline_pct": 0.0226,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.19,
        },
    },
    "Mykonos": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "population_growth": 48.28,            # V2 z-score engine score (raw: 48.28%)
            "employment_growth": 81.80,             # V2 z-score engine score (raw: 81.80%)
            "price_appreciation_5y": 72.58,         # V2 z-score engine score (raw: 70.00%)
            "transaction_volume_growth": 45.13,            # (8+4.2)/69.2*10
            "tourism_strength": 79.62,               # V2 z-score engine score (raw: 79.62%)
            "rental_demand_index": 52.79,            # V2 z-score engine score (raw index: 52.79)
            "macro_infra_pipeline": 35.11,       # V2 z-score engine score (raw: 35.11)
            "supply_pipeline": 58.71,                # V2 z-score engine score (raw: 58.71%) — inverse var
            "vacancy_rate": 7.51,               # V2 z-score engine score (raw: 10.00%) — inverse var
            "quality_of_life_index": 40.39,          # V2 z-score engine score (raw index: 129.20)
        },
        "raw_values": {
            "population_growth_rate": 0.015,
            "employment_growth_rate": 0.040,
            "price_appreciation_5y": 0.70,
            "transaction_volume_growth": 0.08,
            "tourism_strength_yoy": 0.172,
            "rental_demand_index": 73.7,
            "macro_infra_pipeline": 6.6,
            "supply_pipeline_pct": 0.0542,
            "quality_of_life_index": 129.2,
            "vacancy_rate": 0.10,
        },
    },
    "Thessaloniki": {
        "country": "Greece",
        "coastal": True,
        "scores": {
            "population_growth": 30.98,             # V2 z-score engine score (raw: 30.98%)
            "employment_growth": 32.31,              # V2 z-score engine score (raw: 32.31%)
            "price_appreciation_5y": 58.54,          # V2 z-score engine score (raw: 58.00%)
            "transaction_volume_growth": 47.94,             # (10+4.2)/69.2*10
            "tourism_strength": 44.00,                # V2 z-score engine score (raw: 44.00%)
            "rental_demand_index": 83.47,             # V2 z-score engine score (raw index: 83.47)
            "macro_infra_pipeline": 77.64,        # V2 z-score engine score (raw: 77.64)
            "supply_pipeline": 66.01,                 # V2 z-score engine score (raw: 66.01%) — inverse var
            "vacancy_rate": 13.74,                # V2 z-score engine score (raw: 42.00%) — inverse var
            "quality_of_life_index": 43.45,           # V2 z-score engine score (raw index: 132.60)
        },
        "raw_values": {
            "population_growth_rate": 0.004,
            "employment_growth_rate": 0.020,
            "price_appreciation_5y": 0.58,
            "transaction_volume_growth": 0.10,
            "tourism_strength_yoy": 0.088,
            "rental_demand_index": 85.0,
            "macro_infra_pipeline": 10.0,
            "supply_pipeline_pct": 0.0398,
            "quality_of_life_index": 132.6,
            "vacancy_rate": 0.42,
        },
    },
    "Lisbon": {
        "country": "Portugal",
        "coastal": False,
        "scores": {
            "population_growth": 32.08,              # V2 z-score engine score (raw: 32.08%)
            "employment_growth": 44.68,               # V2 z-score engine score (raw: 44.68%)
            "price_appreciation_5y": 66.73,           # V2 z-score engine score (raw: 65.00%)
            "transaction_volume_growth": 32.43,              # (-1.00+4.2)/69.2*10
            "tourism_strength": 31.71,                 # V2 z-score engine score (raw: 31.71%)
            "rental_demand_index": 83.47,              # V2 z-score engine score (raw index: 83.47)
            "macro_infra_pipeline": 77.64,         # V2 z-score engine score (raw: 77.64)
            "supply_pipeline": 76.04,                  # V2 z-score engine score (raw: 76.04%) — inverse var
            "vacancy_rate": 55.24,               # V2 z-score engine score (raw: 22.00%) — inverse var
            "quality_of_life_index": 65.41,            # V2 z-score engine score (raw index: 157.00)
        },
        "raw_values": {
            "population_growth_rate": 0.0047,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.65,
            "transaction_volume_growth": -0.01,
            "tourism_strength_yoy": 0.059,
            "rental_demand_index": 85.0,
            "macro_infra_pipeline": 10.0,
            "supply_pipeline_pct": 0.020,
            "quality_of_life_index": 157.0,
            "vacancy_rate": 0.22,
        },
    },
    "Cascais": {
        "country": "Portugal",
        "coastal": True,
        "scores": {
            "population_growth": 41.98,               # V2 z-score engine score (raw: 41.98%)
            "employment_growth": 39.73,                # V2 z-score engine score (raw: 39.73%)
            "price_appreciation_5y": 55.03,            # V2 z-score engine score (raw: 55.00%)
            "transaction_volume_growth": 31.73,               # (-1.50+4.2)/69.2*10
            "tourism_strength": 32.13,                  # V2 z-score engine score (raw: 32.13%)
            "rental_demand_index": 56.32,               # V2 z-score engine score (raw index: 56.32)
            "macro_infra_pipeline": 2.61,           # V2 z-score engine score (raw: 2.61)
            "supply_pipeline": 78.57,                   # V2 z-score engine score (raw: 78.57%) — inverse var
            "vacancy_rate": 24.11,               # V2 z-score engine score (raw: 37.00%) — inverse var
            "quality_of_life_index": 70.82,             # V2 z-score engine score (raw index: 163.00)
        },
        "raw_values": {
            "population_growth_rate": 0.011,
            "employment_growth_rate": 0.023,
            "price_appreciation_5y": 0.55,
            "transaction_volume_growth": -0.015,
            "tourism_strength_yoy": 0.060,
            "rental_demand_index": 75.0,
            "macro_infra_pipeline": 4.0,
            "supply_pipeline_pct": 0.015,
            "quality_of_life_index": 163.0,
            "vacancy_rate": 0.37,
        },
    },
    "Algarve": {
        "country": "Portugal",
        "coastal": True,
        "scores": {
            "population_growth": 45.13,                # V2 z-score engine score (raw: 45.13%)
            "employment_growth": 52.10,                 # V2 z-score engine score (raw: 52.10%)
            "price_appreciation_5y": 72.58,             # V2 z-score engine score (raw: 70.00%)
            "transaction_volume_growth": 34.56,                # (0.50+4.2)/69.2*10
            "tourism_strength": 9.23,                   # V2 z-score engine score (raw: 9.23%)
            "rental_demand_index": 37.32,                # V2 z-score engine score (raw index: 37.32)
            "macro_infra_pipeline": 40.11,            # V2 z-score engine score (raw: 40.11)
            "supply_pipeline": 70.97,                    # V2 z-score engine score (raw: 70.97%) — inverse var
            "vacancy_rate": 1.29,                # V2 z-score engine score (raw: 48.00%) — inverse var
            "quality_of_life_index": 74.41,              # V2 z-score engine score (raw index: 167.00)
        },
        "raw_values": {
            "population_growth_rate": 0.013,
            "employment_growth_rate": 0.028,
            "price_appreciation_5y": 0.70,
            "transaction_volume_growth": 0.005,
            "tourism_strength_yoy": 0.006,
            "rental_demand_index": 68.0,
            "macro_infra_pipeline": 7.0,
            "supply_pipeline_pct": 0.030,
            "quality_of_life_index": 167.0,
            "vacancy_rate": 0.48,
        },
    },
    "Braga": {
        "country": "Portugal",
        "coastal": False,
        "scores": {
            "population_growth": 50.16,                 # V2 z-score engine score (raw: 50.16%)
            "employment_growth": 44.68,                  # V2 z-score engine score (raw: 44.68%)
            "price_appreciation_5y": 63.22,              # V2 z-score engine score (raw: 62.00%)
            "transaction_volume_growth": 37.38,                 # (2.50+4.2)/69.2*10
            "tourism_strength": 41.88,                    # V2 z-score engine score (raw: 41.88%)
            "rental_demand_index": 42.76,                 # V2 z-score engine score (raw index: 42.76)
            "macro_infra_pipeline": 27.61,             # V2 z-score engine score (raw: 27.61)
            "supply_pipeline": 53.24,                     # V2 z-score engine score (raw: 53.24%) — inverse var
            "vacancy_rate": 63.54,               # V2 z-score engine score (raw: 18.00%) — inverse var
            "quality_of_life_index": 89.70,               # V2 z-score engine score (raw index: 184.00)
        },
        "raw_values": {
            "population_growth_rate": 0.0162,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.62,
            "transaction_volume_growth": 0.025,
            "tourism_strength_yoy": 0.083,
            "rental_demand_index": 70.0,
            "macro_infra_pipeline": 6.0,
            "supply_pipeline_pct": 0.065,
            "quality_of_life_index": 184.0,
            "vacancy_rate": 0.18,
        },
    },
    "Porto": {
        "country": "Portugal",
        "coastal": True,
        "scores": {
            "population_growth": 30.66,                  # V2 z-score engine score (raw: 30.66%)
            "employment_growth": 37.26,                   # V2 z-score engine score (raw: 37.26%)
            "price_appreciation_5y": 63.22,               # V2 z-score engine score (raw: 62.00%)
            "transaction_volume_growth": 35.97,                  # (1.50+4.2)/69.2*10
            "tourism_strength": 41.88,                     # V2 z-score engine score (raw: 41.88%)
            "rental_demand_index": 64.47,                  # V2 z-score engine score (raw index: 64.47)
            "macro_infra_pipeline": 77.64,             # V2 z-score engine score (raw: 77.64)
            "supply_pipeline": 73.51,                      # V2 z-score engine score (raw: 73.51%) — inverse var
            "vacancy_rate": 59.39,               # V2 z-score engine score (raw: 20.00%) — inverse var
            "quality_of_life_index": 83.40,                # V2 z-score engine score (raw index: 177.00)
        },
        "raw_values": {
            "population_growth_rate": 0.0038,
            "employment_growth_rate": 0.022,
            "price_appreciation_5y": 0.62,
            "transaction_volume_growth": 0.015,
            "tourism_strength_yoy": 0.083,
            "rental_demand_index": 78.0,
            "macro_infra_pipeline": 10.0,
            "supply_pipeline_pct": 0.025,
            "quality_of_life_index": 177.0,
            "vacancy_rate": 0.20,
        },
    },
    "Phuket": {
        "country": "Thailand",
        "coastal": True,
        "scores": {
            "population_growth": 45.44,                   # V2 z-score engine score (raw: 45.44%)
            "employment_growth": 52.10,                    # V2 z-score engine score (raw: 52.10%)
            "price_appreciation_5y": 39.82,                # V2 z-score engine score (raw: 42.00%)
            "transaction_volume_growth": 38.78,                   # (3.50+4.2)/69.2*10
            "tourism_strength": 84.71,                      # V2 z-score engine score (raw: 84.71%)
            "rental_demand_index": 75.33,                   # V2 z-score engine score (raw index: 75.33)
            "macro_infra_pipeline": 67.64,              # V2 z-score engine score (raw: 67.64)
            "supply_pipeline": 45.64,                       # V2 z-score engine score (raw: 45.64%) — inverse var
            "vacancy_rate": 55.24,               # V2 z-score engine score (raw: 22.00%) — inverse var
            "quality_of_life_index": 20.62,                 # V2 z-score engine score (raw index: 107.23) (proxy)
        },
        "raw_values": {
            "population_growth_rate": 0.0132,
            "employment_growth_rate": 0.028,
            "price_appreciation_5y": 0.42,
            "transaction_volume_growth": 0.035,
            "tourism_strength_yoy": 0.184,
            "rental_demand_index": 82.0,
            "macro_infra_pipeline": 9.2,
            "supply_pipeline_pct": 0.080,
            "quality_of_life_index": None,  # N/A; regional proxy 107.23 used for scoring
            "vacancy_rate": 0.22,
        },
    },
    "Bangkok": {
        "country": "Thailand",
        "coastal": False,
        "scores": {
            "population_growth": 47.33,                    # V2 z-score engine score (raw: 47.33%)
            "employment_growth": 22.41,                     # V2 z-score engine score (raw: 22.41%)
            "price_appreciation_5y": 11.74,                 # V2 z-score engine score (raw: 18.00%)
            "transaction_volume_growth": 0.0,                     # (-4.20+4.2)/69.2*10
            "tourism_strength": 60.11,                       # V2 z-score engine score (raw: 60.11%)
            "rental_demand_index": 53.61,                    # V2 z-score engine score (raw index: 53.61)
            "macro_infra_pipeline": 77.64,               # V2 z-score engine score (raw: 77.64)
            "supply_pipeline": 0.00,                         # V2 z-score engine score (raw: 0.00%) — inverse var (winsorized)
            "vacancy_rate": 75.99,               # V2 z-score engine score (raw: 12.00%) — inverse var
            "quality_of_life_index": 8.64,                   # V2 z-score engine score (raw index: 93.93)
        },
        "raw_values": {
            "population_growth_rate": 0.0144,
            "employment_growth_rate": 0.016,
            "price_appreciation_5y": 0.18,
            "transaction_volume_growth": -0.042,
            "tourism_strength_yoy": 0.126,
            "rental_demand_index": 74.0,
            "macro_infra_pipeline": 10.0,
            "supply_pipeline_pct": 0.180,
            "quality_of_life_index": 93.93,
            "vacancy_rate": 0.12,
        },
    },
    "Pattaya": {
        "country": "Thailand",
        "coastal": True,
        "scores": {
            "population_growth": 41.98,                     # V2 z-score engine score (raw: 41.98%)
            "employment_growth": 34.78,                      # V2 z-score engine score (raw: 34.78%)
            "price_appreciation_5y": 16.42,                  # V2 z-score engine score (raw: 22.00%)
            "transaction_volume_growth": 0.20,                     # (-2.80+4.2)/69.2*10
            "tourism_strength": 66.89,                        # V2 z-score engine score (raw: 66.89%)
            "rental_demand_index": 45.47,                     # V2 z-score engine score (raw index: 45.47)
            "macro_infra_pipeline": 32.61,                # V2 z-score engine score (raw: 32.61)
            "supply_pipeline": 10.17,                         # V2 z-score engine score (raw: 10.17%) — inverse var
            "vacancy_rate": 42.79,               # V2 z-score engine score (raw: 28.00%) — inverse var
            "quality_of_life_index": 11.87,                   # V2 z-score engine score (raw index: 97.50)
        },
        "raw_values": {
            "population_growth_rate": 0.011,
            "employment_growth_rate": 0.021,
            "price_appreciation_5y": 0.22,
            "transaction_volume_growth": -0.028,
            "tourism_strength_yoy": 0.142,
            "rental_demand_index": 71.0,
            "macro_infra_pipeline": 6.4,
            "supply_pipeline_pct": 0.150,
            "quality_of_life_index": 97.5,
            "vacancy_rate": 0.28,
        },
    },
    "Chiang Mai": {
        "country": "Thailand",
        "coastal": False,
        "scores": {
            "population_growth": 44.66,                      # V2 z-score engine score (raw: 44.66%)
            "employment_growth": 12.53,                       # V2 z-score engine score (raw: 12.53%)
            "price_appreciation_5y": 7.05,                    # V2 z-score engine score (raw: 14.00%)
            "transaction_volume_growth": 0.16,                      # (-3.10+4.2)/69.2*10
            "tourism_strength": 52.48,                         # V2 z-score engine score (raw: 52.48%)
            "rental_demand_index": 37.32,                      # V2 z-score engine score (raw index: 37.32)
            "macro_infra_pipeline": 42.61,                 # V2 z-score engine score (raw: 42.61)
            "supply_pipeline": 50.71,                          # V2 z-score engine score (raw: 50.71%) — inverse var
            "vacancy_rate": 69.77,               # V2 z-score engine score (raw: 15.00%) — inverse var
            "quality_of_life_index": 36.61,                    # V2 z-score engine score (raw index: 125.00)
        },
        "raw_values": {
            "population_growth_rate": 0.0127,
            "employment_growth_rate": 0.012,
            "price_appreciation_5y": 0.14,
            "transaction_volume_growth": -0.031,
            "tourism_strength_yoy": 0.108,
            "rental_demand_index": 68.0,
            "macro_infra_pipeline": 7.2,
            "supply_pipeline_pct": 0.070,
            "quality_of_life_index": 125.0,
            "vacancy_rate": 0.15,
        },
    },
    "Hua Hin": {
        "country": "Thailand",
        "coastal": True,
        "scores": {
            "population_growth": 35.69,                       # V2 z-score engine score (raw: 35.69%)
            "employment_growth": 5.10,                         # V2 z-score engine score (raw: 5.10%)
            "price_appreciation_5y": 12.91,                    # V2 z-score engine score (raw: 19.00%)
            "transaction_volume_growth": 0.87,                       # (1.80+4.2)/69.2*10
            "tourism_strength": 42.73,                          # V2 z-score engine score (raw: 42.73%)
            "rental_demand_index": 23.76,                       # V2 z-score engine score (raw index: 23.76)
            "macro_infra_pipeline": 12.61,                  # V2 z-score engine score (raw: 12.61)
            "supply_pipeline": 60.84,                           # V2 z-score engine score (raw: 60.84%) — inverse var
            "vacancy_rate": 38.64,               # V2 z-score engine score (raw: 30.00%) — inverse var
            "quality_of_life_index": 25.36,                     # V2 z-score engine score (raw index: 112.50)
        },
        "raw_values": {
            "population_growth_rate": 0.007,
            "employment_growth_rate": 0.009,
            "price_appreciation_5y": 0.19,
            "transaction_volume_growth": 0.018,
            "tourism_strength_yoy": 0.085,
            "rental_demand_index": 63.0,
            "macro_infra_pipeline": 4.8,
            "supply_pipeline_pct": 0.050,
            "quality_of_life_index": 112.5,
            "vacancy_rate": 0.30,
        },
    },
    "Dubai": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "population_growth": 93.88,                        # V2 z-score engine score (raw: 93.88%)
            "employment_growth": 81.80,                         # V2 z-score engine score (raw: 81.80%)
            "price_appreciation_5y": 84.29,                     # V2 z-score engine score (raw: 80.00%)
            "transaction_volume_growth": 70.49,                        # (26+4.2)/69.2*10
            "tourism_strength": 53.33,                           # V2 z-score engine score (raw: 53.33%)
            "rental_demand_index": 64.47,                        # V2 z-score engine score (raw index: 64.47)
            "macro_infra_pipeline": 77.64,                   # V2 z-score engine score (raw: 77.64)
            "supply_pipeline": 17.77,                            # V2 z-score engine score (raw: 17.77%) — inverse var
            "vacancy_rate": 82.22,               # V2 z-score engine score (raw: 9.00%) — inverse var
            "quality_of_life_index": 89.79,                      # V2 z-score engine score (raw index: 184.10)
        },
        "raw_values": {
            "population_growth_rate": 0.044,
            "employment_growth_rate": 0.040,
            "price_appreciation_5y": 0.80,
            "transaction_volume_growth": 0.26,
            "tourism_strength_yoy": 0.110,
            "rental_demand_index": 78.0,
            "macro_infra_pipeline": 10.0,
            "supply_pipeline_pct": 0.135,
            "quality_of_life_index": 184.1,
            "vacancy_rate": 0.09,
        },
    },
    "Abu Dhabi": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "population_growth": 82.88,                         # V2 z-score engine score (raw: 82.88%)
            "employment_growth": 94.17,                          # V2 z-score engine score (raw: 94.17%)
            "price_appreciation_5y": 64.39,                      # V2 z-score engine score (raw: 63.00%)
            "transaction_volume_growth": 87.39,                         # (38+4.2)/69.2*10
            "tourism_strength": 61.81,                            # V2 z-score engine score (raw: 61.81%)
            "rental_demand_index": 48.18,                         # V2 z-score engine score (raw index: 48.18)
            "macro_infra_pipeline": 65.14,                     # V2 z-score engine score (raw: 65.14)
            "supply_pipeline": 40.57,                             # V2 z-score engine score (raw: 40.57%) — inverse var
            "vacancy_rate": 86.37,               # V2 z-score engine score (raw: 7.00%) — inverse var
            "quality_of_life_index": 77.66,                       # V2 z-score engine score (raw index: 170.60)
        },
        "raw_values": {
            "population_growth_rate": 0.037,
            "employment_growth_rate": 0.045,
            "price_appreciation_5y": 0.63,
            "transaction_volume_growth": 0.38,
            "tourism_strength_yoy": 0.130,
            "rental_demand_index": 72.0,
            "macro_infra_pipeline": 9.0,
            "supply_pipeline_pct": 0.090,
            "quality_of_life_index": 170.6,
            "vacancy_rate": 0.07,
        },
    },
    "Sharjah": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "population_growth": 60.84,                          # V2 z-score engine score (raw: 60.84%)
            "employment_growth": 44.68,                           # V2 z-score engine score (raw: 44.68%)
            "price_appreciation_5y": 28.70,                       # V2 z-score engine score (raw: 32.50%)
            "transaction_volume_growth": 87.39,                          # (38+4.2)/69.2*10
            "tourism_strength": 53.33,                             # V2 z-score engine score (raw: 53.33%)
            "rental_demand_index": 29.18,                          # V2 z-score engine score (raw index: 29.18)
            "macro_infra_pipeline": 40.11,                      # V2 z-score engine score (raw: 40.11)
            "supply_pipeline": 50.71,                              # V2 z-score engine score (raw: 50.71%) — inverse var
            "vacancy_rate": 66.65,               # V2 z-score engine score (raw: 16.50%) — inverse var
            "quality_of_life_index": 48.31,                        # V2 z-score engine score (raw index: 138.00)
        },
        "raw_values": {
            "population_growth_rate": 0.023,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.325,
            "transaction_volume_growth": 0.38,
            "tourism_strength_yoy": 0.110,
            "rental_demand_index": 65.0,
            "macro_infra_pipeline": 7.0,
            "supply_pipeline_pct": 0.070,
            "quality_of_life_index": 138.0,
            "vacancy_rate": 0.165,
        },
    },
    "Ras Al Khaimah": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "population_growth": 100.00,                           # V2 z-score engine score (raw: 100.00%)
            "employment_growth": 100.00,                            # V2 z-score engine score (raw: 100.00%)
            "price_appreciation_5y": 95.99,                        # V2 z-score engine score (raw: 90.00%)
            "transaction_volume_growth": 100.0,                           # (65+4.2)/69.2*10 = 10.0 (max)
            "tourism_strength": 36.36,                              # V2 z-score engine score (raw: 36.36%)
            "rental_demand_index": 42.76,                           # V2 z-score engine score (raw index: 42.76)
            "macro_infra_pipeline": 65.14,                       # V2 z-score engine score (raw: 65.14)
            "supply_pipeline": 0.00,                               # V2 z-score engine score (raw: 0.00%) — inverse var (winsorized)
            "vacancy_rate": 78.07,               # V2 z-score engine score (raw: 11.00%) — inverse var
            "quality_of_life_index": 71.93,                         # V2 z-score engine score (raw index: 164.23) (proxy)
        },
        "raw_values": {
            "population_growth_rate": 0.060,
            "employment_growth_rate": 0.050,
            "price_appreciation_5y": 0.90,
            "transaction_volume_growth": 0.65,
            "tourism_strength_yoy": 0.070,
            "rental_demand_index": 70.0,
            "macro_infra_pipeline": 9.0,
            "supply_pipeline_pct": 0.175,
            "quality_of_life_index": None,  # N/A; UAE regional proxy 164.23 used for scoring
            "vacancy_rate": 0.11,
        },
    },
    "Ajman": {
        "country": "UAE",
        "coastal": True,
        "scores": {
            "population_growth": 79.72,                            # V2 z-score engine score (raw: 79.72%)
            "employment_growth": 44.68,                             # V2 z-score engine score (raw: 44.68%)
            "price_appreciation_5y": 22.85,                         # V2 z-score engine score (raw: 27.50%)
            "transaction_volume_growth": 73.31,                            # (28+4.2)/69.2*10
            "tourism_strength": 6.68,                                # V2 z-score engine score (raw: 6.68%) (no data → 0)
            "rental_demand_index": 2.03,                             # V2 z-score engine score (raw index: 2.03)
            "macro_infra_pipeline": 15.11,                        # V2 z-score engine score (raw: 15.11)
            "supply_pipeline": 55.77,                                # V2 z-score engine score (raw: 55.77%) — inverse var
            "vacancy_rate": 59.39,               # V2 z-score engine score (raw: 20.00%) — inverse var
            "quality_of_life_index": 71.93,                          # V2 z-score engine score (raw index: 164.23) (proxy)
        },
        "raw_values": {
            "population_growth_rate": 0.035,
            "employment_growth_rate": 0.025,
            "price_appreciation_5y": 0.275,
            "transaction_volume_growth": 0.28,
            "tourism_strength_yoy": None,  # no official data
            "rental_demand_index": 55.0,
            "macro_infra_pipeline": 5.0,
            "supply_pipeline_pct": 0.060,
            "quality_of_life_index": None,  # N/A; UAE regional proxy 164.23 used for scoring
            "vacancy_rate": 0.20,
        },
    },
}


def score_city(city_name, normalized_weights):
    """Score a city using its pre-calibrated V2 scores directly."""
    scores = CITIES[city_name]["scores"]
    score, breakdown = weighted_score(scores, normalized_weights)
    return score, breakdown, scores


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
        score, breakdown, standardized = score_city(city, normalized_weights)
        ranked.append({
            "city": city,
            "country": CITIES[city]["country"],
            "score": score,
            "breakdown": breakdown,
            "standardized_scores": standardized,
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked, normalized_weights, weight_log
