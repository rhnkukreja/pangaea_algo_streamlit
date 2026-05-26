# ─── projects_data.py ─────────────────────────────────────────────────────────
# Thailand Properties — Determinant Score Research
# Scoring date: May 2026
# Researcher notes:
#   - All continuous scores use: Score = ((Value - Min) / (Max - Min)) × 100
#   - For velocity/speed metrics (rental_absorption_velocity, resale_velocity,
#     days_on_market) where LOWER days = HIGHER magnitude:
#     Score = ((Max - Days) / (Max - Min)) × 100
#   - Categorical mappings applied per spec; engine handles sign inversion.
#   - Thailand has no mandatory RERA-style ring-fenced escrow → all Thai
#     projects scored Partial (50) for escrow_quality.
# ──────────────────────────────────────────────────────────────────────────────

THAILAND_RESEARCH = {

    # ══════════════════════════════════════════════════════════════════════════
    # 1. LAGUNA LAKELANDS — Banyan Group — Bang Tao / Laguna Phuket
    # ══════════════════════════════════════════════════════════════════════════
    "laguna_lakelands": {
        "project_name": "Laguna Lakelands",
        "developer":    "Banyan Group (Banyan Tree Holdings Ltd, SGX: B58)",
        "city":         "Phuket",
        "country":      "Thailand",
        "area":         "Bang Tao / Laguna Phuket, Thalang District",

        "raw_variables": {

            # ── GROUP 1 — DEMAND & LIQUIDITY ─────────────────────────────────

            "micro_market_stage": {
                "score": 100,
                "source_note": "Laguna Phuket is Asia's first integrated resort destination, "
                               "operational since 1992 with 30+ years of branded hotel, golf, "
                               "and residential infrastructure. Bang Tao defined as 'Established' "
                               "by CBRE Thailand H1 2025 and Colliers Thailand 2025 reports."
            },

            "rental_absorption_velocity": {
                # Bang Tao branded projects reportedly hitting capacity in <30 days for launches;
                # existing villa/condo rental absorption (days-to-let) ~60 days average.
                # Score = ((365 - 60) / (365 - 30)) × 100 = 305/335 × 100
                "score": 91.0,
                "source_note": "Colliers Thailand: 'several developments reached full capacity in "
                               "less than 30 days' in Bang Tao H1 2025. AirDNA/Airbtics 2024-25 "
                               "show Phuket average 65% occupancy; Bang Tao branded absorption "
                               "estimated ~60 days to rent based on CBRE Thailand and More Group "
                               "market reports (April 2026)."
            },

            "resale_velocity": {
                # Laguna branded villas: 'strong resale market — increasing resales after 5–7 yrs'
                # (Varsovia Estate). Luxury villa segment ~150 days average on secondary market.
                # Score = ((730 - 150) / (730 - 30)) × 100 = 580/700 × 100
                "score": 82.9,
                "source_note": "Varsovia Estate and More Group (April 2026): 'strong resale market' "
                               "for Laguna-branded properties; 5–10% price growth supports swift "
                               "secondary transactions. Estimated ~150 days avg resale time for "
                               "Laguna-area luxury villas based on bangkokpost.com resale trend data."
            },

            "days_on_market": {
                # Bang Tao luxury branded average days on market ~90 days (CBRE/More Group 2026)
                # Score = ((365 - 90) / (365 - 7)) × 100 = 275/358 × 100
                "score": 76.8,
                "source_note": "More Group Phuket Market Outlook 2026: Bang Tao 'top-end projects "
                               "still selling 2–3 units per month' in luxury bracket; avg days on "
                               "market estimated 90 days for branded resort-integrated properties."
            },

            "occupancy_vacancy_rate": {
                # Banyan Group Residences Director quoted directly in Bangkok Post:
                # 'average occupancy rate at Laguna Phuket was 80% over the past few years'
                # Score = ((80 - 50) / (100 - 50)) × 100 = 30/50 × 100
                "score": 60.0,
                "source_note": "Bangkok Post 2024: Angkana Saeloo (Director, Banyan Group Residences) "
                               "stated avg occupancy at Laguna Phuket was 80% post-pandemic, up from "
                               "70% over first 30 years. Airbtics Sept 2024–Aug 2025: Phuket STR "
                               "avg occupancy 65%; Bang Tao branded long-term higher at ~80%."
            },

            # ── GROUP 2 — NEIGHBORHOOD LIVABILITY ────────────────────────────

            "safety_crime_index": {
                # Numbeo Phuket Safety Index = 60.46 (Crime Index = 39.54); used as-is per spec.
                "score": 60.0,
                "source_note": "Numbeo 2025 (multiple comparison pages): Phuket Crime Index = 39.54, "
                               "Safety Index = 60.46. Level of crime rated 'Low' (38.22). Confirmed "
                               "via Numbeo crime comparison Bangkok vs Phuket page (accessed 2025)."
            },

            "healthcare_access": {
                # Bangkok Hospital Phuket (JCI-accredited) ~8km from Bang Tao;
                # Mission Hospital ~10km; Thalang Hospital closer. Banyan Tree has on-site medical.
                "score": 72.0,
                "source_note": "Bangkok Hospital Phuket (JCI-accredited international hospital) is "
                               "~8km from Laguna Phuket. Mission Hospital ~10km. On-site wellness "
                               "clinic within Laguna resort. Scored 72/100 on proximity+quality "
                               "composite (no A&E within walking distance, but quality is world-class)."
            },

            "school_quality": {
                # BISP (British International School Phuket) in Cherngtalay, ~3km.
                # HeadStart International School, ~5km.
                "score": 82.0,
                "source_note": "British International School Phuket (BISP) located in Cherngtalay, "
                               "~3km from Laguna Lakelands. Rated among Asia's top international "
                               "schools (CIS/FOBISIA accredited). Scored 82/100 combining proximity "
                               "and school quality."
            },

            "air_quality_index": {
                # IQAir: Phuket/Thalang AQI typically 30–42 (Good range year-round).
                # One of the best in Thailand per IQAir (coastal winds, no heavy industry).
                # Converting to cleanliness scale: 100 - (AQI/150 × 100) ≈ 74
                "score": 74.0,
                "source_note": "IQAir Thalang/Phuket page: annual avg PM2.5 ~8–12 µg/m³; current "
                               "readings 30–42 US AQI (Good). Phuket cited as 'one of the best air "
                               "quality in Thailand' (IQAir). AQI.in current reading: 36 (Good). "
                               "Converted to 0=worst/100=best scale: ~74."
            },

            "beach_coastal_access": {
                # Laguna Phuket has a dedicated Beach Club on Bang Tao Beach within the resort.
                # Walking distance from Lakelands villas to beach club: ~800m–1.2km within resort.
                # 500m–2km range → score 75
                "score": 75,
                "source_note": "Banyan Group (July 2025) press release confirms dedicated Beach Club "
                               "providing 'direct access to the famous Bang Tao Beach' within Laguna "
                               "Lakelands. Distance from resort centre to beach estimated 800m–1.2km. "
                               "500m–2km bracket → score 75 per spec."
            },

            # ── GROUP 3 — DEMOGRAPHIC & ECONOMIC STRENGTH ────────────────────

            "population_growth_rate": {
                # Macrotrends: Phuket metro 2024→2025: 455k→461k = 1.32% YoY
                # Score = ((1.32 - (-2)) / (8 - (-2))) × 100 = 3.32/10 × 100
                "score": 33.2,
                "source_note": "Macrotrends.net (2025): Phuket metro population 455,000 (2024) → "
                               "461,000 (2025), a 1.32% YoY increase. Consistent with 2022–2025 "
                               "trend of ~1.1–1.4% annual growth post-pandemic recovery."
            },

            "expat_concentration": {
                # Bang Tao/Cherngtalay: foreign buyers comprise 60%+ of real estate transactions.
                # Long-stay expat residents: substantial Russian, European, Australian communities.
                # Estimated resident expat proportion of Bang Tao area: ~20–25%.
                # Score = ((25 - 0) / (100 - 0)) × 100
                "score": 25.0,
                "source_note": "Oceanwwp.com (2025): 'foreign buyers comprising over 60% of "
                               "transactions' in Laguna area. Phuket Hotel Market Review (C9 "
                               "Hotelworks Feb 2025): Russians led arrivals with 1M+. Asia Lifestyle "
                               "Magazine (2026): Bang Tao 'rapidly growing expat community'. "
                               "Resident expat population estimated 20–25% of Bang Tao district."
            },

            # ── GROUP 4 — SUPPLY PRESSURE & RISK ─────────────────────────────

            "immediate_pipeline_risk": {
                # Colliers Thailand: 85 new projects / 5,500 units launched H1 2025 island-wide.
                # Bang Tao has 'highest pipeline of new supply in 2025–2026' (More Group 2026).
                # Within 2km of Laguna, multiple Sansiri, Origin, and branded projects underway.
                # Conservative estimate: ~1,000 units within 2km due in 24 months.
                # Score = ((1000 - 0) / (5000 - 0)) × 100
                "score": 20.0,
                "source_note": "Colliers Thailand (Nation Thailand Dec 2025): 85 new projects / "
                               "5,500 units launched H1 2025 in Bang Tao/Cherngtalay alone. More "
                               "Group (2026): 'Bang Tao has the highest pipeline of new supply in "
                               "2025–2026.' Origin, Sansiri, branded residences all under construction "
                               "in Cherngtalay corridor. Estimated ~1,000 units within 2km/24mo."
            },

            "active_unsold_inventory": {
                # Bang Tao luxury: 'absorption remains strong'; some unsold in new launches.
                # Phuket overall NOT in Bangkok's oversupply situation.
                # Estimated ~15% unsold in completed Bang Tao submarket.
                # Score = ((15 - 0) / (40 - 0)) × 100
                "score": 37.5,
                "source_note": "More Group 2026: 'top-end projects selling 2–3 units/month'. "
                               "Nation Thailand (Dec 2025): 'Bangkok facing massive oversupply "
                               "while Phuket thriving with up to 10% annual growth.' CBRE H1 2025: "
                               "strong absorption in Bang Tao villa segment. Estimated ~15% unsold "
                               "inventory in completed Bang Tao luxury submarket."
            },

            # ── GROUP 5 — DELIVERY TRACK RECORD (Banyan Group) ───────────────

            "average_delay_duration": {
                # Banyan Group: SGX-listed, 30+ years, 100 resorts delivered.
                # FY25 results show strong on-time performance; no notable delay incidents found.
                # Estimated ~3 months average (hospitality-grade precision).
                # Score = ((3 - 0) / (24 - 0)) × 100
                "score": 12.5,
                "source_note": "Banyan Group FY25 press release (March 2026): '100-resort milestone' "
                               "reached with 'disciplined expansion'. SGX-listed with institutional "
                               "oversight. Centrick/Banyan Group investor materials: 'safe, reputable "
                               "developer'. No specific delay incidents found across 20+ residential "
                               "projects. Estimated 3-month avg delay (standard construction buffer)."
            },

            "pct_projects_delivered": {
                # Banyan Group Residences: 20+ branded residences delivered across 20+ countries.
                # SGX-listed, 30-year institutional track record.
                # Estimated 95% of committed projects delivered.
                "score": 95.0,
                "source_note": "Banyan Group Newsroom / About page: portfolio spans '100 hotels and "
                               "resorts, 20+ branded residences in 20+ countries' over 30 years. "
                               "SGX listing requires quarterly reporting. Centrick: 'safe, reputable '  "
                               "developer'. No stalled residential projects found. Estimated 95% "
                               "delivery completion rate."
            },

            "completion_consistency": {
                # SGX-listed; institutional governance; 30-year unbroken track record.
                "score": 100,
                "source_note": "High: Banyan Group is SGX-listed (B58) with institutional governance, "
                               "30+ year track record, multiple award-wins as Thailand's Most Awarded "
                               "Developer (2024-25, 2025-26 Asia-Pacific Property Awards). FY25 "
                               "revenue +25%, Core Operating Profit +59%."
            },

            # ── GROUP 6 — FINANCIAL CREDIBILITY (Banyan Group) ───────────────

            "escrow_quality": {
                # Thailand has no mandatory EIR/RERA-style ring-fenced escrow.
                # Banyan Group uses phased payment structures; developer-held.
                "score": 50,
                "source_note": "Partial: Thailand does not mandate RERA-equivalent ring-fenced escrow "
                               "accounts. Laguna Lakelands payment structure described as phased "
                               "construction-linked (Varsovia Estate: 20% reservation + 30% during "
                               "construction + 50% on delivery). No independent escrow identified."
            },

            "debt_cash_position": {
                # Banyan Group FY25: Revenue S$477.4M (+25%), Core Operating Profit S$109.8M (+59%).
                # Residences revenue nearly doubled (S$197.6M). SGX-listed hospitality group.
                # Hotel operators carry asset-backed debt; Banyan is profitable but leveraged.
                # Score: moderately strong (~65/100).
                "score": 65.0,
                "source_note": "Banyan Group FY25 press release (March 2026, PR Newswire): Revenue "
                               "S$477.4M (+25%), Core Operating Profit S$109.8M (+59%), Residences "
                               "revenue S$197.6M (nearly doubled). Strong operating cash flow. SGX-"
                               "listed with institutional oversight. Hotel/resort operators typical "
                               "carry moderate leverage; no distress signals found. Score 65/100."
            },

            "stalled_projects_count": {
                # No stalled projects found across all searches.
                # Score = ((0 - 0) / (10 - 0)) × 100
                "score": 0,
                "source_note": "Comprehensive search of Banyan Group Newsroom, SGX filings, and "
                               "multiple property portals found zero stalled or abandoned residential "
                               "projects. All 20+ branded residences appear active or completed."
            },

            "presales_pct_achieved": {
                # Property card: '210 of 6,000 units' available → 5,790 sold = 96.5% presold.
                # Score = ((96.5 - 0) / (100 - 0)) × 100
                "score": 96.5,
                "source_note": "Property spec states '210 of 6,000 units' currently available for "
                               "purchase, implying 5,790 units sold/reserved = 96.5% presales "
                               "achieved across the Laguna Lakelands master development. Holiplanet "
                               "(July 2025) confirms project is 'Phuket's largest private residential "
                               "project' with strong international demand."
            },

            # ── GROUP 7 — COMP MARKET PERFORMANCE (1km radius) ───────────────

            "comp_capital_appreciation": {
                # Oceanwwp.com (2025): villa prices +12–18% YoY in 2025; luxury condos +7–10%.
                # 5-year CAGR: beachfront land +40% over 5 years = ~7% CAGR; villas ~9% CAGR.
                # Use 9% as 5-year annualised estimate for Laguna 1km comp market.
                # Score = ((9 - (-5)) / (25 - (-5))) × 100 = 14/30 × 100
                "score": 46.7,
                "source_note": "Oceanwwp.com (Nov 2025): 'villa prices increasing 12–18% year-on-year "
                               "in 2025; luxury condos 7–10%'. Showmehome.io: 'beachfront land prices "
                               "risen more than 40% over past 5 years' (~7% CAGR). Prime Property "
                               "Thailand: 'villas…steady price growth 6–9% annually'. Used 9% as "
                               "5-year annualised for Laguna 1km comp market."
            },

            "comp_rental_yields": {
                # Bangkok Post 2024 / Showmehome.io: Bang Tao 'rental yields exceed 10%'.
                # CBRE / Bamboo Routes 2025: Bang Tao gross yields typically 8–10%.
                # Use 9% gross as comp market yield.
                # Score = ((9 - 2) / (12 - 2)) × 100 = 7/10 × 100
                "score": 70.0,
                "source_note": "Bangkok Post (2024): 'prime areas near Laguna Phuket, rental yields "
                               "exceed 10%'. Showmehome.io: 'Bang Tao area…highest yields on Phuket, "
                               "typically 8–10% annually' (CBRE Thailand / Bamboo Routes 2024–25). "
                               "More Group (2026): managed condo programs deliver 7–10% gross. "
                               "Used conservative 9% gross for 1km comp market."
            },

            "comp_occupancy_rate": {
                # Banyan Group Residences Director: 80% avg occupancy at Laguna Phuket.
                # Score = ((80 - 50) / (100 - 50)) × 100
                "score": 60.0,
                "source_note": "Bangkok Post (2024): Banyan Group Residences Director: 'average "
                               "occupancy rate at Laguna Phuket was 80% over the past few years, "
                               "compared with 70% during its first 30 years.' Airbtics: Phuket "
                               "platform avg 65%; branded/managed properties perform materially higher."
            },

            # ── GROUP 8 — SPECULATION RISK ────────────────────────────────────

            "str_concentration": {
                # Airbtics (Oct 2025): 11,809 active Airbnb listings in Phuket.
                # Phuket 2026 Net Yield guide: 0% of 12,675 Airbnb listings hold hotel licence.
                # Bang Tao is highest-ADR STR zone; estimated 35–40% of units listed as STR.
                # Score = ((37 - 0) / (60 - 0)) × 100
                "score": 61.7,
                "source_note": "Airbtics (Oct 2025): 11,809 active Airbnb listings in Phuket; Bang "
                               "Tao/Cherngtalay cited as highest ADR zone (Bamboo Routes 2026: "
                               "THB 10,000–20,000/night). Aiproperty-phuket.com (May 2026): '0% of "
                               "12,675 Phuket Airbnb listings hold STR licence.' Estimated 37% of "
                               "Bang Tao units listed as STR (legal grey zone)."
            },

            "investor_owner_ratio": {
                # Oceanwwp.com: 'foreign buyers comprising over 60% of transactions' in Laguna.
                # Primarily investment-driven purchases (rental yield / capital gain).
                # Estimated ~70% investor-owned in Bang Tao submarket.
                # Score = ((70 - 0) / (100 - 0)) × 100
                "score": 70.0,
                "source_note": "Oceanwwp.com (2025): 'foreign buyers comprising over 60% of "
                               "transactions' in Laguna; purchases driven by yield/appreciation "
                               "thesis. Varsovia Estate: 'European investors positioning these as "
                               "dual-purpose assets'. High investor/owner ratio estimated ~70%."
            },

            "offplan_secondary_dominance": {
                # Bang Tao: 85 new projects launched H1 2025; majority of transactions are off-plan.
                # Hawook: 'in prime downtown areas… absorption remains strong'; Phuket skews off-plan.
                # Estimated ~65% of Bang Tao transactions are off-plan.
                # Score = ((65 - 0) / (100 - 0)) × 100
                "score": 65.0,
                "source_note": "Colliers Thailand (Nation Thailand Dec 2025): 85 new off-plan projects "
                               "/ 5,500 units launched in Bang Tao H1 2025. Phuket market is "
                               "structurally dominated by off-plan transactions vs secondary sales. "
                               "Estimated ~65% off-plan transaction dominance in Bang Tao 1km comp."
            },
        },
    },


    # ══════════════════════════════════════════════════════════════════════════
    # 2. HYTHE BY BOTANICA — Botanica Luxury Phuket — Cherngtalay
    # ══════════════════════════════════════════════════════════════════════════
    "hythe_by_botanica": {
        "project_name": "HYTHE by Botanica",
        "developer":    "Botanica Luxury Phuket Co., Ltd. (AAP Architecture Properties & Development)",
        "city":         "Phuket",
        "country":      "Thailand",
        "area":         "Cherngtalay (Choeng Thale), Bang Tao, Thalang District",

        "raw_variables": {

            # ── GROUP 1 — DEMAND & LIQUIDITY ─────────────────────────────────

            "micro_market_stage": {
                "score": 100,
                "source_note": "Cherngtalay is described as 'currently the trendiest location in "
                               "Phuket' (Sansiri strategy brief, Dec 2025) and 'currently the most "
                               "established luxury residential zone in Phuket' anchored by Porto de "
                               "Phuket, Boat Avenue, Laguna Phuket, and BISP. CBRE Thailand H1 2025 "
                               "classifies West Coast Central (Cherngtalay/Bang Tao) as established."
            },

            "rental_absorption_velocity": {
                # Cherngtalay is described as 'Demand Hotspot'; branded projects sell out fast.
                # Condo (first for Botanica) may absorb slightly slower than villas. ~75 days.
                # Score = ((365 - 75) / (365 - 30)) × 100 = 290/335 × 100
                "score": 86.6,
                "source_note": "Sansiri Phuket strategy (Dec 2025): Cherngtalay is a 'Demand Hotspot' "
                               "with 'consistent interest from both Thai and foreign investors.' "
                               "CANVAS Cherngtalay (comparable condo) reached 70% sales and moved to "
                               "move-in. Rental absorption for HYTHE units estimated ~75 days based on "
                               "sub-market dynamics (first condo product, slightly slower than villas)."
            },

            "resale_velocity": {
                # Botanica villas have proven resale; HYTHE is first condo — less secondary history.
                # Estimated 200 days for luxury condo resale in Cherngtalay.
                # Score = ((730 - 200) / (730 - 30)) × 100 = 530/700 × 100
                "score": 75.7,
                "source_note": "More Group (Apr 2026): Botanica villas show 'strong resale market' "
                               "with active secondary transactions. HYTHE as Botanica's first condo "
                               "product has limited secondary history. Estimated 200 days resale "
                               "velocity for ultra-luxury Cherngtalay condos at THB 180k/sqm."
            },

            "days_on_market": {
                # Cherngtalay luxury condos: comparable to Bang Tao ~100 days.
                # Score = ((365 - 100) / (365 - 7)) × 100 = 265/358 × 100
                "score": 74.0,
                "source_note": "Sansiri's THE BASE Cherngtalay: '90% in sales'; CANVAS Cherngtalay: "
                               "'70% in sales'. Active demand suggests days-on-market ~100 days for "
                               "new launches. Comparable luxury listings on Lazudi/Hipflat suggest "
                               "95–110 days typical for THB 25M+ condos in Cherngtalay."
            },

            "occupancy_vacancy_rate": {
                # Cherngtalay slightly below Laguna branded for rental occupancy.
                # More Group: Bang Tao/Cherngtalay 'high-season 78%'. ~78%.
                # Score = ((78 - 50) / (100 - 50)) × 100 = 28/50 × 100
                "score": 56.0,
                "source_note": "More Group (2026): Bang Tao/Cherngtalay managed branded residences "
                               "deliver '6–9% rental yields with sustained 78% high-season occupancy.' "
                               "Varsovia Estate: 'short-term rental: 55–75% average occupancy' for "
                               "Phuket villas. Used 78% as conservative branded estimate."
            },

            # ── GROUP 2 — NEIGHBORHOOD LIVABILITY ────────────────────────────

            "safety_crime_index": {
                # Same Phuket market as Laguna. Numbeo Phuket Safety Index = 60.
                "score": 60.0,
                "source_note": "Numbeo 2025: Phuket Safety Index = 60.46, Crime Index = 39.54. "
                               "Cherngtalay (within Thalang/Phuket) covered by same Numbeo dataset."
            },

            "healthcare_access": {
                # Bangkok Hospital Phuket ~8km. Same as Bang Tao area.
                "score": 72.0,
                "source_note": "Same healthcare infrastructure as Bang Tao. Bangkok Hospital Phuket "
                               "(JCI-accredited) ~8km. Botanica Hythe listing (Dwell Phuket) mentions "
                               "'international schools, shopping centres' in proximity. Score 72/100."
            },

            "school_quality": {
                # BISP is IN Cherngtalay — closer than for Laguna Lakelands.
                "score": 85.0,
                "source_note": "British International School Phuket (BISP) is located directly in "
                               "Cherngtalay, approximately 1–2km from HYTHE by Botanica. CIS and "
                               "FOBISIA accredited. Ranked among top 10 international schools in "
                               "Southeast Asia. Scored 85/100 for proximity + quality."
            },

            "air_quality_index": {
                # Same Phuket coastal air quality. Score 74.
                "score": 74.0,
                "source_note": "IQAir Thalang/Phuket: same air quality zone as Laguna Lakelands. "
                               "Annual avg AQI ~35–42 (Good). Phuket cited as 'some of the best air "
                               "quality in Thailand' (IQAir). Score 74/100 on cleanliness scale."
            },

            "beach_coastal_access": {
                # Dwell Phuket listing: 'Bangtao and Layan beaches are just a five-minute drive away'
                # ~2–3km by road. 2–5km bracket → score 50.
                "score": 50,
                "source_note": "Dwell Phuket / Home In Phuket listings: 'pristine Bangtao and Layan "
                               "beaches are just a five-minute drive away' from HYTHE. Five-minute "
                               "drive ≈ 2–3km. HYTHE is inland (part of Grand Avenue development, "
                               "not beachfront). 2–5km bracket → score 50 per spec."
            },

            # ── GROUP 3 — DEMOGRAPHIC & ECONOMIC STRENGTH ────────────────────

            "population_growth_rate": {
                # Same Phuket metro growth rate as Laguna (1.32% YoY).
                "score": 33.2,
                "source_note": "Same Phuket metro population data: Macrotrends 455k→461k (2024→2025) "
                               "= 1.32% growth. CBRE H1 2025: Phuket airport arrivals +5.6% YoY."
            },

            "expat_concentration": {
                # Cherngtalay: 'rapidly growing expat community' (Sansiri strategy brief 2025).
                # Similar to Bang Tao. ~25% resident expat concentration.
                "score": 25.0,
                "source_note": "Sansiri Phuket strategy brief (Dec 2025): Cherngtalay 'rapidly growing "
                               "expat community'. Asia Lifestyle Magazine (2026): Bang Tao/Cherngtalay "
                               "cited as expat hotspot. Resident expat share estimated 20–25% of "
                               "district population, consistent with Bang Tao (same catchment area)."
            },

            # ── GROUP 4 — SUPPLY PRESSURE & RISK ─────────────────────────────

            "immediate_pipeline_risk": {
                # Cherngtalay has HIGHER pipeline than broader Bang Tao (multiple Origin, Sansiri
                # projects in Cherngtalay corridor). Estimated 1,500 units within 2km/24 months.
                # Score = ((1500 - 0) / (5000 - 0)) × 100
                "score": 30.0,
                "source_note": "Asia Lifestyle Magazine (March 2026): So Lagoon Cherngtalay "
                               "(Origin, 511 units) received EIA approval. Sansiri Dec 2025: new "
                               "launch scheduled in Cherngtalay Soi 3 (2026). Multiple mid-rise "
                               "condo clusters under construction in Choeng Thale corridor (More Group "
                               "2026). Estimated ~1,500 units within 2km / 24 months."
            },

            "active_unsold_inventory": {
                # Slightly higher supply pipeline than Laguna zone drives slightly more inventory.
                # Estimated ~18% unsold in Cherngtalay completed submarket.
                # Score = ((18 - 0) / (40 - 0)) × 100
                "score": 45.0,
                "source_note": "CBRE Thailand H1 2025: multiple new condo launches in West Coast "
                               "Central (Cherngtalay). Sansiri: CANVAS Cherngtalay '70% in sales' "
                               "implies 30% unsold at that stage. Estimated ~18% unsold in completed "
                               "Cherngtalay luxury submarket (higher supply pipeline than Laguna core)."
            },

            # ── GROUP 5 — DELIVERY TRACK RECORD (Botanica) ───────────────────

            "average_delay_duration": {
                # Varsovia Estate: 'Botanica's developer track record (6 completed projects,
                # zero delivery delays)'. Also Dwell Phuket: '31 successful projects'.
                # Score = ((0.5 - 0) / (24 - 0)) × 100 = 0.5/24 × 100
                "score": 2.1,
                "source_note": "Varsovia Estate: 'Botanica's developer track record (six completed "
                               "Phuket projects, zero delivery delays) suggests minimal execution "
                               "risk.' Dwell Phuket (March 2026): 'nearly two decades of excellence "
                               "and over 31 successful projects'. Estimated avg delay ~0.5 months "
                               "(essentially on-time). Score = (0.5/24) × 100 = 2.1."
            },

            "pct_projects_delivered": {
                # 31 successfully developed and sold projects (Botanica website).
                # FazWaz shows multiple completed Botanica projects dating to 2010.
                "score": 98.0,
                "source_note": "Botanica Luxury Villa website: 'over 31 successfully developed and "
                               "sold projects'. FazWaz: Botanica Phase 1 completed Jun 2010; multiple "
                               "phases completed since. Tranio: Botanica Grand Avenue on track for "
                               "Sep 2026 completion. Zero failed/abandoned projects found. Score 98%."
            },

            "completion_consistency": {
                # Varsovia: 'zero delivery delays'. Dwell: '31 successful projects'. → High.
                "score": 100,
                "source_note": "High: Varsovia Estate cites 'zero delivery delays' across all "
                               "completed projects. Botanica operational since 2005, 31 delivered "
                               "projects, multiple Thailand Property Awards wins (Best Luxury Villa "
                               "Development Phuket 2018). Consistent on-time track record."
            },

            # ── GROUP 6 — FINANCIAL CREDIBILITY (Botanica) ───────────────────

            "escrow_quality": {
                # Same as all Thailand developers — no mandatory escrow regime.
                "score": 50,
                "source_note": "Partial: Thailand has no mandatory ring-fenced escrow for residential "
                               "developments. Botanica uses construction-linked payment schedules. "
                               "Grand Avenue (12B THB project including HYTHE) appears well-capitalised "
                               "but no independent third-party escrow confirmation found."
            },

            "debt_cash_position": {
                # Private company — no public financials. Strong project pipeline (12B THB Grand
                # Avenue + 18B THB second Cherngtalay project = ~30B THB active pipeline).
                # No distress signals. New 1,885 sqm HQ opened 2025. Score: 55 (no verified data).
                "score": 55.0,
                "source_note": "Botanica Luxury is privately held — no public financial disclosures. "
                               "Malay Mail (Jan 2025): 'THB 12B Grand Avenue mega-project (includes "
                               "HYTHE) + THB 18B high-end condo under development in Cherng Talay' "
                               "= ~30B THB active pipeline. New HQ opened 2025. HYTHE secured 40% "
                               "pre-launch sales. No distress signals. Score 55/100 (no public data)."
            },

            "stalled_projects_count": {
                # No stalled or abandoned Botanica projects found in any search.
                "score": 0,
                "source_note": "All searched databases (Tranio, FazWaz, LivePhuket, Botanica website) "
                               "show active/completed project pipeline. No stalled projects identified "
                               "across 31 Botanica developments. Score = 0."
            },

            "presales_pct_achieved": {
                # Property card: '21 of 276 units' available → 255 sold = 92.4% presold.
                # Malay Mail (Jan 2025) early stage: '40% pre-launch sales'. Now near completion.
                # Score = ((92.4 - 0) / (100 - 0)) × 100
                "score": 92.4,
                "source_note": "Property card states '21 of 276 units' currently available (unsold). "
                               "255/276 sold = 92.4% presales achieved. Malay Mail (Jan 2025) cited "
                               "'40% pre-launch sales' at an earlier stage, confirming strong "
                               "trajectory. Completion Dec 2026 (per spec) / Mar 2027 (per Dwell)."
            },

            # ── GROUP 7 — COMP MARKET PERFORMANCE (1km radius) ───────────────

            "comp_capital_appreciation": {
                # Same Cherngtalay/Bang Tao market as Laguna. 5-year annualised ~9%.
                "score": 46.7,
                "source_note": "Same comp market as Laguna Lakelands (Cherngtalay/Bang Tao 1km "
                               "radius). Oceanwwp.com: villas +12–18% YoY; 5-yr CAGR ~9%. "
                               "Malay Mail: 'top villas in Bang Tao reaching THB 270M'. "
                               "Score = (9+5)/30 × 100 = 46.7."
            },

            "comp_rental_yields": {
                # Same Bang Tao market. 8–10% gross yields.
                "score": 70.0,
                "source_note": "Same Bang Tao/Cherngtalay comp market. CBRE Thailand / Bamboo Routes: "
                               "8–10% gross yields. Alestriapropertycom (2025): 'Bang Tao & "
                               "Cherngtalay: year-round rental demand and some of the island's most "
                               "consistent yields.' Used 9% gross. Score = (9-2)/10 × 100 = 70.0."
            },

            "comp_occupancy_rate": {
                # Cherngtalay: ~78% managed branded occupancy (slightly below Laguna's 80%).
                # Score = ((78 - 50) / (100 - 50)) × 100
                "score": 56.0,
                "source_note": "More Group 2026: Bang Tao/Cherngtalay branded residences '78% "
                               "high-season occupancy'. Airbtics: Phuket STR median 65%; managed "
                               "properties higher. Used 78% for Cherngtalay branded comp market."
            },

            # ── GROUP 8 — SPECULATION RISK ────────────────────────────────────

            "str_concentration": {
                # Similar to Bang Tao. ~35% STR concentration in Cherngtalay.
                # Score = ((35 - 0) / (60 - 0)) × 100
                "score": 58.3,
                "source_note": "Bamboo Routes 2026: Bang Tao/Cherngtalay highest ADR in Thailand "
                               "(THB 10,000–20,000/night on STR). Airbtics: 11,809 active Phuket "
                               "listings. Thai Residential (2025): STR legally grey in Phuket. "
                               "Estimated 35% STR concentration in Cherngtalay submarket."
            },

            "investor_owner_ratio": {
                # Malay Mail 2025: Botanica targets 'high-net-worth investors'. International buyer
                # driven. ~70% investor-owned.
                "score": 70.0,
                "source_note": "Malay Mail (Jan 2025): Botanica targets 'high-net-worth investors'. "
                               "Dwell Phuket: 'turnkey-ready for the sophisticated investor'. "
                               "SunwayEstates: HYTHE positioned as investment asset. Foreign / "
                               "investor buyer majority estimated ~70%."
            },

            "offplan_secondary_dominance": {
                # Cherngtalay market: same as Bang Tao, dominated by off-plan launches 2025-26.
                "score": 65.0,
                "source_note": "Colliers Thailand: massive off-plan pipeline in Cherngtalay corridor "
                               "2025. CBRE H1 2025: 17 new condo projects launched with 3,711 units "
                               "island-wide in first half; Bang Tao/Cherngtalay dominant. Estimated "
                               "~65% off-plan transaction dominance, same as Bang Tao."
            },
        },
    },


    # ══════════════════════════════════════════════════════════════════════════
    # 3. NOBLE PLOENCHIT — Noble Development PCL — Phloen Chit, Bangkok
    # ══════════════════════════════════════════════════════════════════════════
    "noble_ploenchit": {
        "project_name": "Noble Ploenchit",
        "developer":    "Noble Development Public Company Limited (SET: NOBLE)",
        "city":         "Bangkok",
        "country":      "Thailand",
        "area":         "Phloen Chit Road, Lumphini, Pathum Wan District",

        "raw_variables": {

            # ── GROUP 1 — DEMAND & LIQUIDITY ─────────────────────────────────

            "micro_market_stage": {
                "score": 100,
                "source_note": "Ploenchit-Chidlom is Bangkok's most established luxury CBD corridor, "
                               "anchored by BTS Phloen Chit Station, Lumphini Park, major international "
                               "embassies, and premium retail. Hawook/CondoDee 2025: 'Central CBD "
                               "(Phloen Chit, Ratchadamri, Silom): luxury segment shows resilience.' "
                               "Unambiguously Established."
            },

            "rental_absorption_velocity": {
                # Ploenchit expat/executive demand: strong year-round from diplomats/MNCs.
                # Bangkok CBD luxury condos absorb in ~75 days.
                # Score = ((365 - 75) / (365 - 30)) × 100 = 290/335 × 100
                "score": 86.6,
                "source_note": "CondoDee 2025: Ploenchit-Chidlom 'consistent rental demand from "
                               "international executives and diplomats year-round'. Bangkok Residential "
                               "(2025): 'best performance from condos near BTS/MRT stations'. "
                               "Estimated ~75 days rental absorption for luxury Ploenchit corridor."
            },

            "resale_velocity": {
                # Bangkok Post 2025: Bangkok resale 'time on market averages 180–240 days' overall.
                # Premium CBD luxury (200k+ THB/sqm) slightly faster: ~150 days.
                # Score = ((730 - 150) / (730 - 30)) × 100 = 580/700 × 100
                "score": 82.9,
                "source_note": "Asia Lifestyle Magazine (Nov 2025): 'for-sale market: time-on-market "
                               "averages 180–240 days for resale units.' Bamboo Routes (Jan 2026): "
                               "premium Sukhumvit 'resale market more active due to purchase certainty.' "
                               "Ploenchit ultra-luxury segment estimated ~150 days resale velocity."
            },

            "days_on_market": {
                # Same as resale estimate. ~90 days for prime Ploenchit rentals/listings.
                # Score = ((365 - 90) / (365 - 7)) × 100 = 275/358 × 100
                "score": 76.8,
                "source_note": "Bangkok Residential (2025): 'stable rental prices; consistent yields "
                               "4–6% in prime areas.' Hawook (2025): 'in prime downtown areas like "
                               "Asok and Thonglor, absorption remains strong, clearance rates above "
                               "90%.' Days on market for Ploenchit prime estimated ~90 days."
            },

            "occupancy_vacancy_rate": {
                # Bangkok CBD luxury: expat/executive demand keeps occupancy ~80% for quality units.
                # Score = ((80 - 50) / (100 - 50)) × 100
                "score": 60.0,
                "source_note": "Bangkok Rental Market 2025 (Bangkok Residential): 'steady yields 4–6% "
                               "in prime areas'. Asia Lifestyle Magazine: 'select projects maintain "
                               "85%+ occupancy' in riverside/CBD. Estimated 80% long-term occupancy "
                               "for quality Ploenchit units targeting expat/executive segment."
            },

            # ── GROUP 2 — NEIGHBORHOOD LIVABILITY ────────────────────────────

            "safety_crime_index": {
                # Numbeo Bangkok: Crime Index 38.16, Safety Index 61.84.
                "score": 62.0,
                "source_note": "Numbeo 2025 (Bangkok crime page): Crime Index = 38.16, Safety Index "
                               "= 61.84. Level of crime: 37.92 (Low). Confirmed via Numbeo Bangkok "
                               "comparison pages (accessed 2025). Score = 61.84 rounded to 62."
            },

            "healthcare_access": {
                # Bumrungrad International Hospital (JCI, global top-10) ~1km from Ploenchit.
                # Bangkok Hospital Medical Centre ~2km. World-class cluster.
                "score": 92.0,
                "source_note": "Bumrungrad International Hospital (JCI-accredited, consistently "
                               "rated top 10 globally) located on Sukhumvit Soi 3, ~1km from "
                               "Phloen Chit Road. Bangkok Hospital Medical Centre ~2km. Exceptional "
                               "healthcare proximity + quality. Score 92/100."
            },

            "school_quality": {
                # Ruamrudee International School ~2km; St. Andrews ~3km; Bangkok Patana ~8km.
                "score": 75.0,
                "source_note": "Ruamrudee International School (WASC/CIS accredited) ~2km from "
                               "Ploenchit. St. Andrews International School Sukhumvit ~3km. Multiple "
                               "international schools accessible via BTS. Quality high; Bangkok Patana "
                               "(ranked higher) is 8km away. Composite score 75/100."
            },

            "air_quality_index": {
                # Bangkok: annual avg PM2.5 ~22.8 µg/m³ (IQAir 2019 ref). Seasonal spikes to
                # AQI 100–160 in Jan–Mar. Bangkok ranked 8th most polluted city worldwide Jan 2025.
                # Average cleanliness score ~42 on 0=worst/100=best scale.
                "score": 42.0,
                "source_note": "IQAir Bangkok: annual avg PM2.5 ~22.8 µg/m³ (2019 baseline). "
                               "Al Jazeera (Jan 2025): 'Bangkok ranked 8th most polluted city '  "
                               "worldwide; AQI hit 159'. AQI.in current: 76 (Moderate). Seasonal "
                               "spikes to 100–160 in winter. Avg annual cleanliness ~42/100."
            },

            "beach_coastal_access": {
                # Bangkok is an inland city on the Chao Phraya River. Nearest beach is Pattaya ~150km.
                "score": 0,
                "source_note": ">10km from any coastal beach. Bangkok is an inland river delta city. "
                               "Nearest beach (Pattaya) ~150km by road. Score 0 per spec (>10km = 0)."
            },

            # ── GROUP 3 — DEMOGRAPHIC & ECONOMIC STRENGTH ────────────────────

            "population_growth_rate": {
                # Bangkok metro: relatively stable growth ~0.8% per year (urban plateau).
                # Score = ((0.8 - (-2)) / (8 - (-2))) × 100 = 2.8/10 × 100
                "score": 28.0,
                "source_note": "Thailand Population 2026 (Worldometer / UN): Bangkok metro area "
                               "growth ~0.5–1% annually. Asia Lifestyle Magazine (2026): Thailand "
                               "GDP growth 2025 ~2.0%, 2026 forecast 1.6%. Bangkok is a maturing "
                               "urban centre. Population growth estimated 0.8% annual rate."
            },

            "expat_concentration": {
                # Bangkok total: 250k–300k expats / 10.5M metro = ~2.5%.
                # Ploenchit slightly higher (~5%) due to embassy district concentration.
                # Score = ((5 - 0) / (100 - 0)) × 100
                "score": 5.0,
                "source_note": "Pattaya Mail (Nov 2024): Bangkok home to '250,000–300,000 expats' "
                               "out of 10.5M metro = ~2.5%. Ploenchit/Lumphini has higher per-district "
                               "expat density (embassy district, MNC headquarters). Estimated ~5% "
                               "resident expat concentration in Ploenchit subdistrict."
            },

            # ── GROUP 4 — SUPPLY PRESSURE & RISK ─────────────────────────────

            "immediate_pipeline_risk": {
                # Asia Property Awards 2025: 'very limited plans for new project launches' in luxury.
                # Ultra-luxury CBD supply extremely constrained: ~250 units within 2km / 24 months.
                # Score = ((250 - 0) / (5000 - 0)) × 100
                "score": 5.0,
                "source_note": "Asia Property Awards (Jun 2025): 'sluggish activity will continue "
                               "through 2025 with listed developers announcing very limited plans for "
                               "new launches.' Bangkok Post (Mar 2026): 'new condo launches contracted "
                               "by 41% in 2025.' Ultra-luxury CBD supply extremely constrained; "
                               "estimated ~250 units within 2km / 24 months."
            },

            "active_unsold_inventory": {
                # Ultra-luxury Ploenchit: Asia Property Awards: 'only 168 unsold ultimate-class units
                # left across ALL Bangkok' by end Q3 2024. Very thin unsold inventory ~8% of segment.
                # Score = ((8 - 0) / (40 - 0)) × 100
                "score": 20.0,
                "source_note": "Asia Property Awards (Jun 2025): 'by end of September 2024, there "
                               "were 168 unsold ultimate-class units left to be sold across Bangkok.' "
                               "Hawook (2025): 'in prime downtown areas like Asok and Thonglor, "
                               "absorption remains strong, clearance rates above 90%.' Ultra-luxury "
                               "Ploenchit unsold inventory estimated ~8%."
            },

            # ── GROUP 5 — DELIVERY TRACK RECORD (Noble Development) ──────────

            "average_delay_duration": {
                # Noble Development: founded 1991, SET-listed, large residential portfolio.
                # Revenue miss in 2024 but delivery delays not specifically reported.
                # Listed developers in Thailand typically have ~4-month avg delays.
                # Score = ((4 - 0) / (24 - 0)) × 100
                "score": 16.7,
                "source_note": "Noble Development listed 1991; decades of residential delivery. "
                               "Bangkok Post (Nov 2024): Noble revised 2024 revenue down 18% due to "
                               "'lower-than-expected performance in low-rise housing' (not delivery "
                               "delays). No specific delivery delay incidents found in public records. "
                               "Estimated ~4-month avg delay for SET-listed Thai developers."
            },

            "pct_projects_delivered": {
                # Noble Development: SET-listed since 1991, large multi-segment portfolio.
                # Estimated 90% of committed projects delivered (some low-rise delays).
                "score": 90.0,
                "source_note": "Noble Development PCL: founded 1991, publicly listed on SET since "
                               "early 1990s. Yahoo Finance: 'operates through Condominium, House and "
                               "Land, Rental and Service segments.' Large portfolio with PWC audit. "
                               "2024 revenue shortfall (low-rise housing) noted. Estimated 90% "
                               "project delivery rate."
            },

            "completion_consistency": {
                # Noble had significant 2024 revenue miss (18% below target); listed developer
                # with some execution variability in housing. → Medium = 50.
                "score": 50,
                "source_note": "Medium: Bangkok Post (Nov 2024): Noble Development 'revised down "
                               "2024 revenue projection by 18% to 11.4B baht from initial 14B baht "
                               "following lower-than-expected performance'. CEO: 'we are bottoming "
                               "out.' Despite listed status, execution variability warrants Medium."
            },

            # ── GROUP 6 — FINANCIAL CREDIBILITY (Noble Development) ──────────

            "escrow_quality": {
                "score": 50,
                "source_note": "Partial: Thailand has no mandatory ring-fenced escrow. Noble is "
                               "SET-listed (NOBLE.BK) with PwC audit, providing higher transparency "
                               "than private developers, but no independent escrow mechanism exists "
                               "for Thai residential presales."
            },

            "debt_cash_position": {
                # Noble: revenue miss 2024, 18% shortfall. But 27B baht backlog.
                # Listed with SET; PwC audited. Some financial pressure but access to bond markets.
                # Score: 40 — weaker than Sansiri/Banyan.
                "score": 40.0,
                "source_note": "Bangkok Post (Nov 2024): Noble revised revenue down 18%; CEO said "
                               "'we are bottoming out — 2025 will be better'. 27B baht backlog noted. "
                               "Bangkok Post (Sep 2024): SET-listed developers have 314B baht in "
                               "debentures; Noble participates in this debt market. SET factsheet: "
                               "foreign ownership at 37.54%. Financial position moderate. Score 40/100."
            },

            "stalled_projects_count": {
                # No stalled Noble projects found in searches.
                "score": 0,
                "source_note": "No stalled or abandoned Noble Development projects identified across "
                               "SET filings, Bangkok Post, or property portals. SET listing provides "
                               "regulatory oversight that makes large-scale project abandonment unlikely. "
                               "Score = 0."
            },

            "presales_pct_achieved": {
                # Property card: '1,223 of 1,444 units available' → interpreted as unsold.
                # 1,444 - 1,223 = 221 sold = 15.3% presales at near-completion stage (Dec 2026).
                # Consistent with Bangkok condo oversupply (58,400 unsold units market-wide).
                # Score = ((15.3 - 0) / (100 - 0)) × 100
                "score": 15.3,
                "source_note": "Property card: '1,223 of 1,444 units available' (available for "
                               "purchase = unsold). 221 sold / 1,444 total = 15.3% presales. "
                               "CONFIDENCE FLAG: this is a high-uncertainty data point. Alternative "
                               "interpretation: 1,223 transferred = 85% sold. Chose 15.3% as most "
                               "consistent with Bangkok Post condo oversupply data (58,400 unsold "
                               "units Q4 2024) and Noble's 2024 revenue miss."
            },

            # ── GROUP 7 — COMP MARKET PERFORMANCE ────────────────────────────

            "comp_capital_appreciation": {
                # Bangkok CBD (Sukhumvit/Sathorn/Silom): +12–15% cumulative 2020–2025 = ~2.3–2.9% CAGR.
                # Ploenchit ultra-luxury: higher demand floor. Estimated ~4% annualised 5-year.
                # Score = ((4 - (-5)) / (25 - (-5))) × 100 = 9/30 × 100
                "score": 30.0,
                "source_note": "Prime Property Thailand: 'condo prices rose 12–15% cumulatively "
                               "[2020–2025], high-demand areas Sukhumvit/Sathorn/Silom climbing to "
                               "180,000–300,000 THB/sqm.' CondoDee (Jun 2025): capital appreciation "
                               "in midtown ~5.6% over 2022–2024. Ploenchit ultra-luxury: ~4% "
                               "annualised 5-year CAGR. Score = (4+5)/30 × 100 = 30.0."
            },

            "comp_rental_yields": {
                # CondoDee 2025: 'Ploenchit-Chidlom: 4.1% yield' — one of the compressed yields
                # due to high capital values.
                # Score = ((4.1 - 2) / (12 - 2)) × 100 = 2.1/10 × 100
                "score": 21.0,
                "source_note": "CondoDee (Jun 2025): 'Ploenchit-Chidlom, one of Bangkok's most "
                               "prestigious addresses… median price 15.3M THB… delivers 4.1% yield.' "
                               "Bamboo Routes 2026: 'net yields 3–5.5%… lower end reflecting premium "
                               "buildings in Thonglor or Sathorn.' Used 4.1% gross for Ploenchit "
                               "comp market. Score = (4.1-2)/10 × 100 = 21.0."
            },

            "comp_occupancy_rate": {
                # Bangkok CBD expat/executive corridor: ~80% long-term rental occupancy.
                # Score = ((80 - 50) / (100 - 50)) × 100
                "score": 60.0,
                "source_note": "Asia Lifestyle Magazine (Nov 2025): 'select projects maintain 85%+ "
                               "occupancy' in premium Bangkok districts. Bangkok Rental 2025: stable "
                               "demand in Ploenchit/Chidlom from MNC/embassy tenants. Estimated 80% "
                               "occupancy for quality units in Ploenchit comp market."
            },

            # ── GROUP 8 — SPECULATION RISK ────────────────────────────────────

            "str_concentration": {
                # Bangkok: 15,232 Airbnb listings (Airbtics Oct 2025). STR legally restricted
                # (<30-day requires hotel licence). Ploenchit is executive/corporate market —
                # lower STR penetration ~12%.
                # Score = ((12 - 0) / (60 - 0)) × 100
                "score": 20.0,
                "source_note": "Airbtics (Oct 2025): 15,232 active Bangkok Airbnb listings total. "
                               "Bamboo Routes (Jan 2026): '~17,000 active Airbnb listings in Bangkok "
                               "as of early 2026'. Ploenchit is corporate/executive long-term rental "
                               "market; STR penetration lower than Thong Lo. Estimated ~12% STR. "
                               "Score = 12/60 × 100 = 20.0."
            },

            "investor_owner_ratio": {
                # Noble Ploenchit: SET factsheet shows 37.54% foreign shareholders (investor-oriented).
                # Mixed use: some owner-occupiers in Lumphini, significant investor share. ~60%.
                # Score = ((60 - 0) / (100 - 0)) × 100
                "score": 60.0,
                "source_note": "Noble SET factsheet: 37.54% foreign shareholders. Noble Ploenchit "
                               "marketed as 'investment opportunity' with 'strong capital appreciation "
                               "and rental returns' (serve.co.th). Mix of owner-occupiers and "
                               "investors. Estimated ~60% investor-owned ratio."
            },

            "offplan_secondary_dominance": {
                # Ploenchit: Bangkok Post 2026 — 'resale market has become significantly more active.'
                # Noble Ploenchit is near-completion (Dec 2026) — secondary/ready market dominant.
                # Estimated ~30% off-plan vs secondary in the Ploenchit ultra-luxury segment.
                # Score = ((30 - 0) / (100 - 0)) × 100
                "score": 30.0,
                "source_note": "Bangkok Post (Mar 2026): 'the resale market has become significantly "
                               "more active, primarily due to purchase certainty.' Noble Ploenchit "
                               "near-completion transitions to secondary market. Off-plan dominance "
                               "is low in mature Ploenchit corridor (~30%). Score = 30.0."
            },
        },
    },


    # ══════════════════════════════════════════════════════════════════════════
    # 4. THE MONUMENT THONG LO — Sansiri PCL — Thong Lo, Bangkok
    # ══════════════════════════════════════════════════════════════════════════
    "monument_thong_lo": {
        "project_name": "The Monument Thong Lo",
        "developer":    "Sansiri Public Company Limited (SET: SIRI)",
        "city":         "Bangkok",
        "country":      "Thailand",
        "area":         "Thong Lo (Sukhumvit Soi 55), Watthana District",

        "raw_variables": {

            # ── GROUP 1 — DEMAND & LIQUIDITY ─────────────────────────────────

            "micro_market_stage": {
                "score": 100,
                "source_note": "Thong Lo is Bangkok's most prestigious lifestyle corridor, described "
                               "as 'Bangkok's most appealing avenue' by multiple sources. Completed "
                               "2019. 'Old-money Thai residences', Japanese expat hub. Hawook (2025): "
                               "'Thong Lo/Ekkamai: lifestyle appeal and walkability keep this micro-"
                               "market afloat.' Unambiguously Established."
            },

            "rental_absorption_velocity": {
                # Thong Lo: Japanese expats + executives create consistent rental demand.
                # Ultra-luxury at this price point (~30M+ THB): ~70 days to rent.
                # Score = ((365 - 70) / (365 - 30)) × 100 = 295/335 × 100
                "score": 88.1,
                "source_note": "Bamboo Routes 2026: Thong Lo highest ADR STR zone in Bangkok "
                               "(THB 4,500–8,000/night). Hawook (2025): Thong Lo 'lifestyle appeal "
                               "keeps this micro-market afloat'. 78,431 Japanese in Thailand, "
                               "59,744 in Bangkok (Wikipedia, MoFA 2022); Thong Lo is Japanese "
                               "expat hub. Ultra-luxury rental absorption estimated ~70 days."
            },

            "resale_velocity": {
                # Monument Thong Lo completed 2019. Ultra-luxury (30M–150M THB).
                # Asia Lifestyle Magazine: 'Thong Lo/Ekkamai resale units under 10M move faster.'
                # Ultra-luxury resale (30M+): slower. ~210 days.
                # Score = ((730 - 210) / (730 - 30)) × 100 = 520/700 × 100
                "score": 74.3,
                "source_note": "Asia Lifestyle Magazine (Nov 2025): 'Thong Lo/Ekkamai: resale units "
                               "under 10M THB move faster than new launches.' The Monument units at "
                               "30M–150M THB occupy a much thinner market. Estimated 210 days for "
                               "ultra-luxury secondary sale. Score = 520/700 × 100 = 74.3."
            },

            "days_on_market": {
                # Ultra-luxury segment with limited buyer pool: ~150 days.
                # Score = ((365 - 150) / (365 - 7)) × 100 = 215/358 × 100
                "score": 60.1,
                "source_note": "Keller Henson: Monument Thong Lo avg price 360,000 THB/sqm; 'ultra-"
                               "luxury' segment. Asia Lifestyle Magazine (Nov 2025): Bangkok resale "
                               "180–240 days broadly; Thong Lo ultra-luxury at 30M+ THB has narrow "
                               "buyer pool. Estimated ~150 days on market for remaining 10 units."
            },

            "occupancy_vacancy_rate": {
                # Thong Lo: strong long-term rental market for Japanese expats/executives.
                # Bamboo Routes 2026: Thong Lo net yields 'lower end' of 3–5.5% range.
                # Estimated 78% occupancy for long-term rental units.
                # Score = ((78 - 50) / (100 - 50)) × 100
                "score": 56.0,
                "source_note": "Bamboo Routes 2026: 'lower end [of 3–5.5% net yield range] reflecting "
                               "premium buildings in Thonglor.' Hawook (2025): Thong Lo 'lifestyle "
                               "appeal keeps micro-market afloat'. Estimated 78% occupancy rate for "
                               "ultra-luxury long-term rental units in Thong Lo."
            },

            # ── GROUP 2 — NEIGHBORHOOD LIVABILITY ────────────────────────────

            "safety_crime_index": {
                # Same Bangkok Numbeo safety index = 61.84.
                "score": 62.0,
                "source_note": "Numbeo 2025: Bangkok Crime Index = 38.16, Safety Index = 61.84. "
                               "Thong Lo (Watthana district) is one of Bangkok's safest residential "
                               "neighbourhoods. IQAir user: 'I feel safe walking home alone at night "
                               "on Sukhumvit.' Score = 61.84 ≈ 62."
            },

            "healthcare_access": {
                # Samitivej Hospital Sukhumvit ~800m (JCI-accredited, top Bangkok hospital).
                # Excellent healthcare proximity.
                "score": 90.0,
                "source_note": "Samitivej Hospital Sukhumvit (JCI-accredited) located ~800m from "
                               "Thong Lo BTS on Sukhumvit Soi 49. Bangkok Hospital Phrom Phong ~2km. "
                               "Sansiri/Golden Emperor: 'leading healthcare facilities' cited as Thong "
                               "Lo amenity. Excellent proximity + quality. Score 90/100."
            },

            "school_quality": {
                # Shrewsbury International School ~3km; Bangkok Patana ~7km; multiple options.
                "score": 78.0,
                "source_note": "Sansiri website: 'prestigious schools and nurseries' at Thong Lo. "
                               "Shrewsbury International School (AKA 'the Eton of Bangkok') ~3km. "
                               "NIST International School ~4km. Strong school options; Bangkok Patana "
                               "(best-ranked) at ~7km. Composite score 78/100."
            },

            "air_quality_index": {
                # Same Bangkok air quality issues as Noble Ploenchit. Score 42.
                "score": 42.0,
                "source_note": "Same Bangkok air quality dataset as Noble Ploenchit. IQAir: Bangkok "
                               "annual avg PM2.5 ~22.8 µg/m³. AQI.in current: 76 (Moderate). Seasonal "
                               "spikes to 100–160+ in winter months. Avg annual cleanliness ~42/100."
            },

            "beach_coastal_access": {
                # Same as all Bangkok properties. No beach access.
                "score": 0,
                "source_note": ">10km from any beach. Bangkok inland city. Nearest beach (Pattaya) "
                               "~150km. Score 0 per spec."
            },

            # ── GROUP 3 — DEMOGRAPHIC & ECONOMIC STRENGTH ────────────────────

            "population_growth_rate": {
                # Same Bangkok metro growth ~0.8% as Noble Ploenchit.
                "score": 28.0,
                "source_note": "Same Bangkok metro population data as Noble Ploenchit. ~0.8% annual "
                               "growth rate. Score = (0.8+2)/10 × 100 = 28.0."
            },

            "expat_concentration": {
                # Thong Lo: known Japanese expat hub. Thai MoFA: 78,431 Japanese in Thailand,
                # 59,744 in Bangkok. Thong Lo captures large share of this cohort.
                # ~6% expat resident concentration in Thong Lo district.
                "score": 6.0,
                "source_note": "Wikipedia / MoFA Japan (2022): 78,431 Japanese residents in Thailand, "
                               "59,744 in Bangkok. Thong Lo is the primary Japanese expat residential "
                               "cluster. Also significant Korean, Western expat presence. Thong Lo "
                               "district estimated ~6% expat resident concentration."
            },

            # ── GROUP 4 — SUPPLY PRESSURE & RISK ─────────────────────────────

            "immediate_pipeline_risk": {
                # Thong Lo ultra-luxury: Asia Property Awards: 'very limited plans for new launches'.
                # Sansiri 2026 plan focuses on other areas. Thong Lo ultra-luxury supply minimal.
                # Estimated ~125 units within 2km / 24 months.
                # Score = ((125 - 0) / (5000 - 0)) × 100
                "score": 2.5,
                "source_note": "Asia Property Awards (Jun 2025): 'very limited plans for new project "
                               "launches' by Thai listed developers. Bangkok Post (Mar 2026): 'new "
                               "supply launched in Greater Bangkok expected to decline further.' "
                               "Thong Lo ultra-luxury zone (360k THB/sqm) has extremely constrained "
                               "new supply. Estimated ~125 units within 2km / 24 months."
            },

            "active_unsold_inventory": {
                # The Monument itself: 10/127 units remaining = 7.9% unsold in this project.
                # Broader Thong Lo ultra-luxury: Asia Property Awards: 'only 168 unsold ultimate-"
                # class units left across all Bangkok' end Q3 2024. ~10% submarket unsold.
                # Score = ((10 - 0) / (40 - 0)) × 100
                "score": 25.0,
                "source_note": "Project card: '10 of 127 units' remaining = 7.9% project-level "
                               "unsold. Asia Property Awards (Jun 2025): only 168 ultimate-class "
                               "units unsold across all Bangkok (Q3 2024). Hawook (2025): Thong Lo "
                               "'clearance rates above 90%'. Submarket unsold estimated ~10%. "
                               "Score = 10/40 × 100 = 25.0."
            },

            # ── GROUP 5 — DELIVERY TRACK RECORD (Sansiri) ───────────────────

            "average_delay_duration": {
                # Monument Thong Lo: launched April 2016, expected completion September 2019.
                # Sansiri.com confirms project listed under 'past projects' (completed).
                # No delay reported. Sansiri: 33+ years, hundreds of projects.
                # Estimated ~2-month avg delay across Sansiri portfolio.
                # Score = ((2 - 0) / (24 - 0)) × 100
                "score": 8.3,
                "source_note": "Sansiri.com: Monument Thong Lo listed on 'sold out / past project' "
                               "page, completed ~Sep 2019 as projected (Nestopa: 'Finished in 2019 "
                               "by Sansiri'). No delay reported. Grokipedia: 'Sansiri has received "
                               "awards for excellence in architecture' and consistent delivery. "
                               "Estimated ~2-month avg delay across portfolio. Score = 2/24 × 100 = 8.3."
            },

            "pct_projects_delivered": {
                # Sansiri: 33+ years, hundreds of delivered projects, SET-listed since 1996.
                "score": 98.0,
                "source_note": "Keller Henson: 'Public listed company in the SET with over 33 years "
                               "of experience and hundreds of projects across Thailand.' Grokipedia: "
                               "'Named Best Developer at PropertyGuru Thailand Property Awards 2024.' "
                               "Sansiri has 29 sold-out projects in 2025 alone. Estimated 98% delivery "
                               "completion rate."
            },

            "completion_consistency": {
                # Sansiri: SET-listed, highest net profit among listed Thai property developers
                # (9M 2025). Monument completed on time. Decades of consistent delivery. → High.
                "score": 100,
                "source_note": "High: Bangkok Post (Jan 2026): 'Sansiri posted net profit of 3.03B "
                               "baht for 9M 2025, highest among listed property developers.' Monument "
                               "Thong Lo completed on time (2019). 'Most Powerful Brand in Real "
                               "Estate 2023'. SGX/SET-listed; institutional governance."
            },

            # ── GROUP 6 — FINANCIAL CREDIBILITY (Sansiri) ────────────────────

            "escrow_quality": {
                "score": 50,
                "source_note": "Partial: Thailand has no mandatory ring-fenced escrow. Sansiri is "
                               "SET-listed (SIRI) with PwC audit, quarterly reporting, and bond "
                               "market access — higher transparency than private developers. "
                               "No independent escrow mechanism exists for Thai residential presales."
            },

            "debt_cash_position": {
                # Sansiri Q1 2025: D/E ratio 1.99x, gearing 1.49x. Total assets 148.5B THB.
                # Revenue 39.2B THB FY2024, net profit 5.25B. Strong operations but leveraged.
                # Score: 45/100 (moderate leverage, profitable but significant debt).
                "score": 45.0,
                "source_note": "Sansiri Q1 2025 filing: 'debt-to-equity ratio 1.99x; interest-bearing "
                               "D/E (gearing) 1.49x.' Total assets 148.5B THB, total liabilities "
                               "98.9B THB. Bangkok Post (Jan 2026): 'financial position remains solid, "
                               "total assets 148B baht; bond issuances oversubscribed.' Profitable "
                               "but materially leveraged. Score 45/100."
            },

            "stalled_projects_count": {
                # No stalled Sansiri projects found. 29 projects sold out in 2025.
                "score": 0,
                "source_note": "Bangkok Post (Jan 2026): 'total of 29 projects sold out in 2025, "
                               "combined value 28.8B baht.' No stalled or abandoned Sansiri projects "
                               "found in SET filings, Bangkok Post, or property portals. Score = 0."
            },

            "presales_pct_achieved": {
                # Property card: '10 of 127 units' remaining. Monument was 'sold out' at launch
                # (Sansiri past-project page). 10 units likely re-entered market (secondary/
                # developer repurchase). 117/127 sold = 92.1%.
                # Score = ((92.1 - 0) / (100 - 0)) × 100
                "score": 92.1,
                "source_note": "Sansiri.com: Monument Thong Lo listed on 'sold out / past projects' "
                               "page. Project card: '10 of 127 units' currently available, implying "
                               "117 sold = 92.1%. Monument Sanampao (predecessor) was 'one-day sell-"
                               "out'; Monument Thong Lo launched April 2016 with strong initial "
                               "uptake (Bangkok Post 2023). Score = 92.1."
            },

            # ── GROUP 7 — COMP MARKET PERFORMANCE (1km radius) ───────────────

            "comp_capital_appreciation": {
                # Thong Lo: 'lifestyle appeal and walkability keep micro-market afloat'.
                # Bangkok CBD 5-year appreciation ~4–6%; Thong Lo ultra-luxury at 360k/sqm
                # has floor support but limited upside vs Phuket. ~5% annualised.
                # Score = ((5 - (-5)) / (25 - (-5))) × 100 = 10/30 × 100
                "score": 33.3,
                "source_note": "Prime Property Thailand: Bangkok CBD cumulative +12–15% 2020–2025 "
                               "= ~2.3–2.9% CAGR. Hawook (2025): Thong Lo 'keeps afloat'. CondoDee: "
                               "midtown cap appreciation ~5.6% over 2022–2024. Bamboo Routes 2026: "
                               "Thong Lo/Sathorn 'lower end' of yield/appreciation range. Used 5% "
                               "annualised 5-yr CAGR for Thong Lo ultra-luxury comp market."
            },

            "comp_rental_yields": {
                # Bamboo Routes 2026: 'lower end [3–5.5% net] reflecting premium buildings in Thonglor.'
                # Gross ~5–5.5% for ultra-luxury. Use 5%.
                # Score = ((5 - 2) / (12 - 2)) × 100 = 3/10 × 100
                "score": 30.0,
                "source_note": "Bamboo Routes 2026: 'lower end of 3–5.5% [net yields] reflecting "
                               "premium buildings in Thonglor'. Bangkok Rental 2025: '4–6% in prime "
                               "locations'. Gross rental yield ~5–5.5% for Thong Lo ultra-luxury. "
                               "Used 5% gross. Score = (5-2)/10 × 100 = 30.0."
            },

            "comp_occupancy_rate": {
                # Thong Lo: 78% estimated (Japanese expat + executive tenant base is consistent).
                # Score = ((78 - 50) / (100 - 50)) × 100
                "score": 56.0,
                "source_note": "Hawook (2025): Thong Lo 'lifestyle appeal keeps micro-market afloat.' "
                               "Bangkok Rental 2025: stable demand from expats in Sukhumvit corridor. "
                               "AirROI: Bangkok STR typical 46% occupancy; managed long-term higher. "
                               "Estimated 78% long-term rental occupancy for Thong Lo ultra-luxury."
            },

            # ── GROUP 8 — SPECULATION RISK ────────────────────────────────────

            "str_concentration": {
                # Thong Lo: Bamboo Routes 2026 highest Bangkok ADR (THB 4,500–8,000/night).
                # AirROI: Bangkok overall STR occupancy 44.2%. Thong Lo higher concentration (~20%).
                # Score = ((20 - 0) / (60 - 0)) × 100
                "score": 33.3,
                "source_note": "Bamboo Routes 2026: Thong Lo is Bangkok's highest ADR STR zone "
                               "(THB 4,500–8,000/night). Bamboo Routes Jan 2026: '~17,000 active "
                               "Airbnb listings in Bangkok.' Monument Thong Lo is high-value STR "
                               "target. Estimated ~20% STR concentration in Thong Lo luxury submarket."
            },

            "investor_owner_ratio": {
                # Monument Thong Lo: marketed internationally (HK investors cited in Golden Emperor).
                # Mix of owner-occupiers (Japanese community) and investors. ~50% investor.
                # Score = ((50 - 0) / (100 - 0)) × 100
                "score": 50.0,
                "source_note": "Golden Emperor (marketing materials): 'Hong Kong investors would be "
                               "interested to buy units for use as second homes or long-term investment.' "
                               "Thong Lo is also a lifestyle area with genuine owner-occupiers "
                               "(Japanese expat community). Estimated 50% investor / 50% owner ratio."
            },

            "offplan_secondary_dominance": {
                # Monument Thong Lo completed 2019. Entirely secondary market product.
                # Bangkok Post 2026: 'resale market has become significantly more active.'
                # Thong Lo overall: low off-plan activity (constrained new supply).
                # Estimated ~25% off-plan.
                # Score = ((25 - 0) / (100 - 0)) × 100
                "score": 25.0,
                "source_note": "Monument Thong Lo completed 2019 — entirely secondary market. "
                               "Bangkok Post (Mar 2026): 'resale market significantly more active.' "
                               "Thong Lo has very limited off-plan pipeline (Asia Property Awards: "
                               "'very limited new launches'). Off-plan dominance ~25% of Thong Lo "
                               "transactions. Score = 25.0."
            },
        },
    },
}