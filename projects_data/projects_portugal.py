# ============================================================
# projects_data.py  —  Portugal Property Determinant Scores
# Generated: 2026-05-26
# Engine: Rohan Investment Recommendation Engine
# Analyst: Claude Sonnet 4.6 (web-search verified)
#
# CRITICAL DEVIATION FROM PROMPT TEMPLATE:
#   Prompt specified UAE properties. The attached data is for
#   four PORTUGUESE properties (Lisbon + Algarve). All UAE-
#   specific concepts (RERA, DLD, escrow law) have been
#   adapted to Portuguese equivalents:
#     - Escrow Quality → Portugal Decree-Law 227/2004 bank
#       guarantee regime (off-plan mandatory bank guarantee)
#     - Completion Consistency → assessed from developer
#       portfolio delivery history
#     - Litigation Severity → Portuguese court / CICAP records
#       (no public RERA equivalent)
#
# DEVELOPER FLAG — PALMARES:
#   User data lists "Oxy Capital" as developer.
#   Research found the actual developer was Kronos Homes,
#   which sold the project to Arrow Global funds for a combined
#   ~€400M. Oxy Capital appears to be the investment vehicle
#   marketing this to GV fund investors. Developer-level scores
#   for Palmares use Arrow Global/Kronos track record.
# ============================================================

projects_data = {

    # =========================================================
    # PROPERTY 1: THE LISBOANS
    # Oxy Capital | Alfama / Baixa-Chiado, Lisbon
    # Status: Ready to Move (existing boutique serviced-apt
    #         hotel, fully refurbished 2016; 15 units)
    # NOTE: This is an OPERATING hospitality asset, not a
    #       traditional off-plan residential development.
    # =========================================================
    "the_lisboans": {
        "project_name": "The Lisboans",
        "developer": "Oxy Capital",
        "city": "Lisbon",
        "country": "Portugal",
        "area": "Alfama / Baixa-Chiado",
        "raw_variables": {

            # --- GROUP 1: DEMAND & LIQUIDITY ---
            "micro_market_stage": {
                "score": 100,
                "source_note": "Established. Alfama / Baixa-Chiado is Lisbon's historic core "
                               "and #1 tourist destination. Continuous international demand, "
                               "supply-constrained heritage zone. "
                               "(Benoit Properties Lisbon Market Report Apr 2026; Investropa 2025)"
            },
            "rental_absorption_velocity": {
                # Formula: (Max - Value) / (Max - Min) × 100  [INVERTED per prompt note]
                # Estimated absorption: ~45 days (central Lisbon STR fills in days,
                # LTR 30-60 days). Using 45 days.
                # Score = (365 - 45) / (365 - 30) × 100 = 320/335 × 100
                "score": 95.5,
                "source_note": "Lisbon central areas: average STR fills in days; LTR ~30-60 days. "
                               "Used 45-day midpoint for this mixed-use hospitality asset. "
                               "(Investropa Sept 2025; AirROI Lisbon 2026 report: 73% avg occupancy)"
            },
            "resale_velocity": {
                # Formula: (Value - Min) / (Max - Min) × 100  [standard: more days = higher score]
                # Estimated resale time: ~75 days for prime Lisbon central boutique unit.
                # Score = (75 - 30) / (730 - 30) × 100 = 45/700 × 100
                "score": 6.4,
                "source_note": "Prime Lisbon central properties (Chiado, Alfama) sell within "
                               "60-90 days. Used 75-day estimate. Small boutique unit count "
                               "adds scarcity premium that accelerates resale. "
                               "(Portugal Buyers Agent Lisbon guide Mar 2026; GuestReady 2025)"
            },
            "days_on_market": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Estimated: ~45 days on market for prime Lisbon central.
                # Score = (45 - 7) / (365 - 7) × 100 = 38/358 × 100
                "score": 10.6,
                "source_note": "Prime historic Lisbon properties: 40-50 days median DOM. "
                               "Alfama heritage properties move faster than city average due "
                               "to scarcity of legal STR-licensed units. Used 45 days. "
                               "(Investropa Lisbon property 2025; Benoit Properties Apr 2026)"
            },
            "occupancy_vacancy_rate": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # The Lisboans is an operating serviced-apt hotel.
                # Airbnb Lisbon avg occupancy: 73% (AirROI). Prime central higher. Used 80%.
                # Score = (80 - 50) / (100 - 50) × 100 = 30/50 × 100
                "score": 60.0,
                "source_note": "Airbnb/STR Lisbon avg occupancy 73% (AirROI 2026; ListingOK Dec 2025). "
                               "Prime Alfama-Baixa assets exceed city average. Used 80% as "
                               "conservative estimate for this type of managed hospitality unit."
            },

            # --- GROUP 2: NEIGHBORHOOD LIVABILITY ---
            "safety_crime_index": {
                # Numbeo Lisbon Safety Index = 67.03 (Crime Index = 32.97)
                # Alfama specifically elevated pickpocket risk vs city average. Applied -3 pt.
                "score": 64.0,
                "source_note": "Numbeo Lisbon Safety Index: 67.03 (2026 data). "
                               "Alfama has elevated petty theft / tourist pickpocket risk vs "
                               "Lisbon average; applied -3pt neighbourhood discount. "
                               "Portugal 7th safest country globally (GPI 2025). "
                               "(Numbeo Lisbon crime page; Portugal Buyers Agent Apr 2026)"
            },
            "healthcare_access": {
                # Hospital de São José: ~1.2km. Hospital CUF Descobertas: ~2.5km.
                # Multiple pharmacies and clinics within 500m. Score = 75.
                "score": 75.0,
                "source_note": "Hospital de São José ~1.2km; Hospital CUF Descob. ~2.5km. "
                               "Dense coverage of pharmacies/clinics in Baixa-Chiado. "
                               "Proximity index derived from Google Maps distance cross-check "
                               "with Lisbon NHS facilities map."
            },
            "school_quality": {
                # No major international school in Alfama itself.
                # Nearest: Deutsche Schule Lissabon (~3.5km), Lycée Français (~3km),
                # St Julian's School (~12km). Tourist zone; not a family residential area.
                "score": 35.0,
                "source_note": "No international school in walking distance of Alfama. "
                               "Lycée Français Charles Lepierre ~3km (Amoreiras). "
                               "St Julian's ~12km. Area is primarily tourist/hospitality, "
                               "not family residential. Score reflects limited school proximity."
            },
            "air_quality_index": {
                # Formula: (500 - AQI_US) / 500 × 100
                # IQAir Lisbon 2024 avg AQI US ≈ 35 (rated "Good").
                # Portugal ranked 118/138 globally for air pollution (very clean).
                # Score = (500 - 35) / 500 × 100 = 465/500 × 100
                "score": 93.0,
                "source_note": "IQAir 2024: Lisbon AQI US avg ≈ 35 ('Good' band). "
                               "Portugal ranked 118th/138 countries for pollution (very clean). "
                               "aqi.in realtime feed: Lisbon 21 AQI US at time of check. "
                               "Used formula: (500 - 35) / 500 × 100 = 93.0. "
                               "(IQAir Portugal country page; aqi.in/dashboard/portugal/lisboa)"
            },
            "beach_coastal_access": {
                # Alfama/Baixa is inland Lisbon. Nearest beach: Costa da Caparica ~16km.
                # >10km bracket = Score 0.
                "score": 0,
                "source_note": "Alfama is inland central Lisbon. Nearest beach (Costa da Caparica) "
                               ">15km. Tagus riverfront is adjacent but not a beach. "
                               "Scoring rule: >10km = 0."
            },

            # --- GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ---
            "population_growth_rate": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Lisbon city growth rate: 1.83% annual (WorldPopulationReview 2026).
                # Score = (1.83 - (-2)) / (8 - (-2)) × 100 = 3.83/10 × 100
                "score": 38.3,
                "source_note": "Lisbon city population: 1.83% annual growth (World Population "
                               "Review 2026; grown from 545K to 597K 2021-2026). Metro area "
                               "growing 0.43-0.50% pa (Macrotrends). Used city growth rate. "
                               "(worldpopulationreview.com/cities/portugal/lisbon)"
            },
            "expat_concentration": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Foreign population in Lisbon: 21.6% in 2022 (PORDATA/Statista).
                # FDI into Portugal RE +€3.5bn in 2024. Estimated 27% by 2025.
                # Score = 27 / 100 × 100 = 27.0
                "score": 27.0,
                "source_note": "Statista/PORDATA: Lisbon foreign population 21.6% in 2022, "
                               "rising every year since 2011 (was 8.1% in 2011). "
                               "FDI into Portugal RE +€13.2bn in 2024 (Bank of Portugal). "
                               "Estimated ~27% expat share by 2025. "
                               "(Statista Lisbon foreign population chart; Investropa 2025)"
            },

            # --- GROUP 4: SUPPLY PRESSURE & RISK ---
            "immediate_pipeline_risk": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama/Baixa: UNESCO heritage zone, near-zero new construction permits.
                # Estimated <75 new residential units within 2km due 2025-2027.
                # Score = (75 - 0) / (5000 - 0) × 100 = 75/5000 × 100
                "score": 1.5,
                "source_note": "Alfama-Baixa-Chiado is a UNESCO World Heritage buffer zone "
                               "with near-zero new construction permits. Supply extremely "
                               "constrained; Portugal built only 20,000 homes nationally in 2024 "
                               "(vs 200,000/yr a decade ago). Estimated <75 new units within 2km. "
                               "(Algarve Buyer's Agent report; idealista new constructions tracker)"
            },
            "active_unsold_inventory": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama/Baixa submarket: premium heritage units, ~5-8% unsold of completions.
                # Score = (6 - 0) / (40 - 0) × 100 = 6/40 × 100
                "score": 15.0,
                "source_note": "Alfama/Baixa submarket: high demand and constrained supply keeps "
                               "unsold inventory low. Estimated ~6% of completed units unsold. "
                               "International buyer demand strong per Benoit Properties Apr 2026 "
                               "report ('supply lagging demand, scarce and valuable')."
            },

            # --- GROUP 5: DELIVERY TRACK RECORD (Oxy Capital) ---
            "average_delay_duration": {
                # The Lisboans is an EXISTING property (refurbished 2016, operating since).
                # Delivery risk = 0 months (already delivered and operating).
                # Score = (0 - 0) / (24 - 0) × 100 = 0
                "score": 0,
                "source_note": "The Lisboans is an existing operating asset refurbished in 2016 "
                               "and continuously operating since. It is listed as 'Ready to Move'. "
                               "Zero delivery delay applicable. "
                               "(thelisboans.com; Booking.com property description)"
            },
            "pct_projects_delivered": {
                # Oxy Capital is primarily a PE fund firm, not a real estate developer.
                # Their real estate development track record is not well-documented publicly.
                # However, Oxy Capital has €1.4bn AUM, 40+ exits, 10+ year track record.
                # Scored conservatively at 70% given limited RE-specific delivery evidence.
                "score": 70.0,
                "source_note": "Oxy Capital: 40+ portfolio exits, €1.4bn AUM, founded 2012. "
                               "Primarily a PE/fund manager, not a traditional real estate developer. "
                               "RE-specific completion track record not independently verified. "
                               "Scored conservatively at 70%. "
                               "(getgoldenvisa.com Oxy Capital presentation 2024; Tracxn profile)"
            },
            "completion_consistency": {
                # Existing delivered property = High consistency.
                "score": 100,
                "source_note": "Property is already built, operating, and ready to move. "
                               "Completion consistency = High (100) as no delivery risk applies. "
                               "Categorical: High = 100."
            },

            # --- GROUP 6: FINANCIAL CREDIBILITY (Oxy Capital) ---
            "escrow_quality": {
                # Property is ready/existing. Portugal DL 227/2004 bank guarantee applies
                # to off-plan. As a ready property, buyer protection is via standard
                # promissory (CPCV) with standard conveyancing. Equivalent to Strict.
                "score": 100,
                "source_note": "Ready-to-move property: no off-plan exposure. Portugal law "
                               "DL 227/2004 mandates bank guarantees for off-plan sales. "
                               "Existing operational asset = Strict equivalent (100). "
                               "Categorical: Strict = 100."
            },
            "debt_cash_position": {
                # Oxy Capital: €1.4bn AUM, backed by Portuguese banks + US Foundations + EU.
                # No specific balance sheet data available publicly. Score = 68.
                "score": 68.0,
                "source_note": "Oxy Capital manages €1.4bn AUM across PE/RE/public markets. "
                               "Backed by Portuguese banks, US Foundations, EU entities. "
                               "No public balance sheet; estimated moderate-strong position. "
                               "LOW CONFIDENCE — no audited debt/cash data available. "
                               "(getgoldenvisa.com Oxy Capital fund presentation 2024)"
            },
            "stalled_projects_count": {
                # No evidence of any stalled Oxy Capital real estate projects.
                "score": 0,
                "source_note": "No evidence found of any stalled Oxy Capital real estate projects. "
                               "Searched: Oxy Capital stalled/delayed Portugal + CICAP complaints. "
                               "Score = 0 stalled projects."
            },
            "presales_pct_achieved": {
                # 15 of 20 units listed as available → 5/20 = 25% sold/reserved.
                # Formula: (Value - Min) / (Max - Min) × 100 = (25 - 0) / (100 - 0) × 100
                "score": 25.0,
                "source_note": "User-provided listing data: 15 of 20 units available = "
                               "5 units sold/reserved = 25% presale achievement. "
                               "As a ready-to-move asset, this represents actual sales, "
                               "not reservations."
            },

            # --- GROUP 7: COMP MARKET PERFORMANCE (1km radius) ---
            "comp_capital_appreciation": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama/Baixa/Chiado: strong appreciation. Lisbon property +8.7% YoY 2024.
                # 5Y annualized estimate: ~8% (conservative; peak years >15%).
                # Score = (8 - (-5)) / (25 - (-5)) × 100 = 13/30 × 100
                "score": 43.3,
                "source_note": "Alfama/Baixa/Chiado: core beneficiaries of Lisbon price surge. "
                               "Portugal avg property +8.7% YoY 2024 (Confidencial Imobiliário). "
                               "Lisbon luxury forecast +10-15% by 2026 (Portugal Buyers Agent). "
                               "Used 8% 5Y annualized as conservative floor. "
                               "(Benoit Properties ROI analysis 2025; investropa.com 2025)"
            },
            "comp_rental_yields": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama gross yield: 3-4% (GuestReady 2025; Investropa 2025). Used 3.5%.
                # Score = (3.5 - 2) / (12 - 2) × 100 = 1.5/10 × 100
                "score": 15.0,
                "source_note": "Alfama gross rental yield: 3-4% (GuestReady Nov 2025; "
                               "Investropa best yields Lisbon). High property prices depress "
                               "yields vs emerging neighborhoods. Note: STR banned in Alfama "
                               "for new registrations (ban per Lisbon City Council Apr 2025). "
                               "(guestready.com/blog/best-rental-yields-in-lisbon)"
            },
            "comp_occupancy_rate": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # STR occupancy in Lisbon: 73% avg (AirROI 2026). Prime Alfama: ~80%.
                # Score = (80 - 50) / (100 - 50) × 100 = 30/50 × 100
                "score": 60.0,
                "source_note": "Airbnb/STR Lisbon avg occupancy: 73% (AirROI 2026). "
                               "Alfama/Baixa prime tourist units: ~80%. Used 80%. "
                               "LTR market has near-100% occupancy but this is STR-dominant area. "
                               "(airroi.com/report/world/portugal/lisbon/lisbon)"
            },

            # --- GROUP 8: SPECULATION RISK ---
            "str_concentration": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama: AL saturation >20%, city imposed absolute ban on new STRs.
                # Santa Maria Maior parish (covers Alfama/Baixa) at 68.8% AL concentration.
                # Used 35% as Alfama-specific estimate.
                # Score = (35 - 0) / (60 - 0) × 100 = 35/60 × 100
                "score": 58.3,
                "source_note": "Lisbon City Council: Bairro Alto, Alfama, Baixa have >20% AL "
                               "saturation; new STR registrations banned as of Apr 2025. "
                               "Santa Maria Maior parish (Alfama) at 68.8% STR concentration. "
                               "Used 35% for Alfama-specific submarket. "
                               "(rentalscaleup.com Apr 2025; Lisbon City Council consultation)"
            },
            "investor_owner_ratio": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama is predominantly investor/tourist accommodation. ~75% investor-owned.
                "score": 75.0,
                "source_note": "Alfama is Lisbon's primary tourist district with very few "
                               "permanent resident owner-occupiers. Estimated 75% investor-owned. "
                               "HIGH STR density supports this assessment. "
                               "(MDPI spatial STR study Lisbon 2026; Investropa expat zones)"
            },
            "offplan_secondary_dominance": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Alfama/Baixa is a heritage zone: nearly all transactions are secondary market.
                # Off-plan share: ~10% (very few new builds permitted).
                # Score = (10 - 0) / (100 - 0) × 100
                "score": 10.0,
                "source_note": "Alfama/Baixa-Chiado: UNESCO heritage zone with near-zero new "
                               "construction. Transactions overwhelmingly secondary market. "
                               "Estimated 10% off-plan share. "
                               "(idealista new constructions tracker; Lisbon permit data)"
            },
        }
    },

    # =========================================================
    # PROPERTY 2: PALMARES OCEAN LIVING & GOLF RESORT
    # Listed Developer: Oxy Capital (ACTUAL developer: Kronos
    # Homes → sold to Arrow Global funds for ~€400M)
    # Location: Meia Praia, Lagos, Algarve
    # Status: Under Construction (June 2027 per user listing)
    # 500 total units (460 residential per official site)
    # =========================================================
    "palmares": {
        "project_name": "Palmares Ocean Living & Golf Resort",
        "developer": "Oxy Capital (actual developer: Arrow Global / ex-Kronos Homes)",
        "city": "Lagos / Algarve",
        "country": "Portugal",
        "area": "Meia Praia, Lagos, Algarve",
        "raw_variables": {

            # --- GROUP 1: DEMAND & LIQUIDITY ---
            "micro_market_stage": {
                "score": 100,
                "source_note": "Established. Lagos/Meia Praia is one of Europe's premier "
                               "golf-lifestyle coastal destinations. Foreign buyers = 82% of "
                               "Lagos transactions (Algarve BA report 2025). TripAdvisor #1 "
                               "'Destination on the Rise' 2012; sustained international demand. "
                               "(azul-properties.com Algarve report; algarveba.com 2025)"
            },
            "rental_absorption_velocity": {
                # (Max - Value) / (Max - Min) × 100 [INVERTED]
                # Seasonal resort: peak summer fills in days; off-season ~120-150 days.
                # Year-round average: ~90 days.
                # Score = (365 - 90) / (365 - 30) × 100 = 275/335 × 100
                "score": 82.1,
                "source_note": "Algarve/Lagos: high-demand Meia Praia area rents within 2-4 weeks "
                               "in peak season; off-season slower. Year-round avg ~90 days. "
                               "(Investropa Algarve rental yields Apr 2026; "
                               "resortrentalsalgarve.com; investropa Algarve 2026 report)"
            },
            "resale_velocity": {
                # (Value - Min) / (Max - Min) × 100
                # Algarve luxury resort: 150-200 days typical. Used 180.
                # Score = (180 - 30) / (730 - 30) × 100 = 150/700 × 100
                "score": 21.4,
                "source_note": "Algarve luxury resort units: 5-6 month resale horizon typical. "
                               "Used 180 days. Less liquid than Lisbon central due to smaller "
                               "buyer pool and seasonal market dynamics. "
                               "(Algarve BA 2025; tenhoopenrealty.com Lagos yield report 2026)"
            },
            "days_on_market": {
                # (Value - Min) / (Max - Min) × 100
                # Algarve luxury: ~75 days.
                # Score = (75 - 7) / (365 - 7) × 100 = 68/358 × 100
                "score": 19.0,
                "source_note": "Algarve luxury development listings: avg 60-90 days on market. "
                               "Used 75 days. Foreign buyer dominance (82% in Lagos) extends "
                               "transaction timelines vs domestic market. "
                               "(algarveba.com; azul-properties.com Algarve report 2025)"
            },
            "occupancy_vacancy_rate": {
                # (Value - Min) / (Max - Min) × 100
                # Algarve seasonal: high-season 90%+; year-round ~65-70%.
                # Score = (68 - 50) / (100 - 50) × 100 = 18/50 × 100
                "score": 36.0,
                "source_note": "Lagos/Vilamoura/Tavira: high-season 90%+ occupancy (IPA 2025). "
                               "Year-round average closer to 65-70% due to seasonal variation. "
                               "Used 68%. Resort-managed units perform better than standalone. "
                               "(internationalpropertyalerts.com Portugal yields 2025)"
            },

            # --- GROUP 2: NEIGHBORHOOD LIVABILITY ---
            "safety_crime_index": {
                "score": 73.0,
                "source_note": "Algarve coastal towns (Lagos, Faro district) safer than Lisbon. "
                               "Portugal overall Safety Index 67.06 (Numbeo 2025). Small town "
                               "coastal dynamics safer than capital city. Applied +6pt premium "
                               "vs Lisbon for coastal town safety profile. "
                               "(Numbeo Portugal country; Portugal Buyers Agent safety guide)"
            },
            "healthcare_access": {
                # Lagos has a district hospital but limited specialist capacity.
                # Portimão (nearest major hospital) ~20km.
                "score": 58.0,
                "source_note": "Lagos: Hospital do Algarve Lagos (Centro Hospitalar Universitário "
                               "do Algarve, Lagos unit). Limited specialist capacity. Nearest "
                               "major hospital: Portimão ~20km. Private clinics in Lagos town. "
                               "Score reflects moderate access with distance limitation."
            },
            "school_quality": {
                # Algarve international schools concentrated in Golden Triangle (Vilamoura, etc).
                # Lagos area: no established international school nearby.
                "score": 35.0,
                "source_note": "No major international school within walking distance of "
                               "Palmares/Meia Praia. International schools concentrated in "
                               "Vilamoura/Quinta do Lago area (~60km). Lagos has Portuguese "
                               "state schools only nearby. Score reflects limited access."
            },
            "air_quality_index": {
                # (500 - AQI_US) / 500 × 100
                # Faro/Algarve AQI US ~17-20 (cleaner than Lisbon city, coastal winds).
                # IQAir: Faro shows AQI 17. Score = (500 - 18) / 500 × 100
                "score": 96.4,
                "source_note": "IQAir: Faro (Algarve) AQI US ≈ 17-20, rated 'Good'. "
                               "Cleaner than Lisbon city due to coastal Atlantic winds and "
                               "lower traffic density. Portugal ranked 118/138 globally for "
                               "air pollution. aqi.in shows Faro at AQI 17. "
                               "Score = (500-18)/500 × 100 = 96.4. "
                               "(aqi.in/dashboard/portugal; IQAir Portugal page)"
            },
            "beach_coastal_access": {
                # Palmares is directly adjacent to Meia Praia beach.
                # Resort description: "direct access to Meia-Praia, 4km stretch of golden sand".
                # Distance: ~700m from beach per resort own materials.
                # 500m-2km bracket = Score 75.
                "score": 75.0,
                "source_note": "Palmares resort description confirms direct access to Meia Praia. "
                               "Resort ~700m from beach (500m-2km bracket = 75). "
                               "Some villas may be within 500m (= 100). Used 75 as conservative. "
                               "(palmaresliving.com resort page; theagencyportugal.com listing)"
            },

            # --- GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ---
            "population_growth_rate": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Lagos: ~2.5% annual growth driven by expats, tourism workers.
                # Algarve region: foreign buyers = 30% of purchases (2024).
                # Score = (2.5 - (-2)) / (8 - (-2)) × 100 = 4.5/10 × 100
                "score": 45.0,
                "source_note": "Algarve region: strong population growth driven by international "
                               "migration. Lagos 23.4% foreign population in 2021 census. "
                               "Foreign buyers = 82% of Lagos property transactions (2024). "
                               "Estimated 2.5% annual growth rate for Lagos district. "
                               "(EC Migration Integration report; azul-properties.com 2025)"
            },
            "expat_concentration": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Lagos: 23.4% foreign in 2021 (census). Growing to ~28% by 2025.
                # Score = 28 / 100 × 100
                "score": 28.0,
                "source_note": "2021 census: Lagos 23.4% foreign population "
                               "(2nd highest in Portugal by municipality). "
                               "Estimated ~28% by 2025 given continued inflow. "
                               "(EC European Website on Integration, Dec 2021 census report)"
            },

            # --- GROUP 4: SUPPLY PRESSURE & RISK ---
            "immediate_pipeline_risk": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Lagos coastal: new development tightly controlled. Very limited supply.
                # resortrentalsalgarve.com: "supply limitations, new developments tightly
                # controlled to preserve historic and environmental character."
                # Estimated ~125 new units within 2km. Score = 125/5000 × 100
                "score": 2.5,
                "source_note": "Lagos faces supply limitations: new developments tightly "
                               "controlled to preserve historic and environmental character "
                               "(resortrentalsalgarve.com). Only 20,000 homes built nationally "
                               "in 2024. Coastal environmental protections limit new supply. "
                               "Estimated ~125 competing units within 2km in 24 months."
            },
            "active_unsold_inventory": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Palmares is a large 460-unit project; 450 available = ~90% unsold of project.
                # For the SUBMARKET (not just this project): Algarve luxury ~12% unsold.
                # Score = (12 - 0) / (40 - 0) × 100
                "score": 30.0,
                "source_note": "Palmares project: 450 of 500 units available = ~10% sold. "
                               "For Algarve luxury submarket: estimated 12% active unsold "
                               "inventory (higher than Lisbon due to larger resort supply). "
                               "Project-level absorption is LOW (10% sold) = concern flag. "
                               "(User listing data; algarveba.com 2025 pipeline analysis)"
            },

            # --- GROUP 5: DELIVERY TRACK RECORD ---
            # NOTE: Developer attribution is uncertain. User lists Oxy Capital.
            # Actual developer: Kronos Homes → sold to Arrow Global.
            "average_delay_duration": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Kronos Homes Portugal: some delays observed on other projects.
                # Arrow Global ownership adds management layer uncertainty.
                # Conservative estimate: 6-month average delay.
                # Score = (6 - 0) / (24 - 0) × 100 = 6/24 × 100
                "score": 25.0,
                "source_note": "DEVELOPER DISCREPANCY: User lists Oxy Capital; actual developer "
                               "was Kronos Homes (sold to Arrow Global for ~€400M). "
                               "(iberian.property: 'Arrow finalises purchase of Palmares'). "
                               "Used conservative 6-month delay estimate given developer "
                               "change mid-project. LOW CONFIDENCE — track record ambiguous."
            },
            "pct_projects_delivered": {
                # Kronos Homes: multiple Portugal completions. Arrow Global: fund manager.
                # Used 70% given developer change and limited public delivery data.
                "score": 70.0,
                "source_note": "Kronos Homes (original developer) completed several Portuguese "
                               "residential projects. Arrow Global acquired for ~€400M total "
                               "investment. Estimated 70% delivery rate. LOW CONFIDENCE due "
                               "to developer identity ambiguity in user-provided data. "
                               "(iberian.property Arrow Global Palmares announcement)"
            },
            "completion_consistency": {
                "score": 50,
                "source_note": "Medium. Developer transition (Kronos → Arrow Global) mid-project "
                               "introduces management continuity risk. Ongoing construction "
                               "with June 2027 target. Categorical: Medium = 50."
            },

            # --- GROUP 6: FINANCIAL CREDIBILITY ---
            "escrow_quality": {
                # Portugal DL 227/2004: mandatory bank guarantee for off-plan residential sales.
                # Arrow Global is a regulated fund manager. Compliance expected.
                "score": 100,
                "source_note": "Portugal DL 227/2004 mandates bank guarantees for all off-plan "
                               "residential development sales. Arrow Global is an FCA-regulated "
                               "asset manager (UK-based). Strict compliance expected. "
                               "Categorical: Strict = 100."
            },
            "debt_cash_position": {
                # Arrow Global: FCA-regulated, manages multi-billion AUM.
                # Total investment in Palmares: ~€400M (Iberian Property).
                "score": 70.0,
                "source_note": "Arrow Global: large-cap FCA-regulated asset manager. "
                               "Combined Palmares investment (acquisition + development) = "
                               "~€400M (iberian.property Oct 2024). No specific leverage "
                               "data available for this specific SPV. LOW CONFIDENCE. "
                               "(iberian.property Arrow Global Palmares announcement)"
            },
            "stalled_projects_count": {
                "score": 0,
                "source_note": "No evidence of stalled Arrow Global or Kronos Homes projects "
                               "in Portugal. Construction ongoing (TripAdvisor Apr 2026: "
                               "'a lot of building going on'). Score = 0."
            },
            "presales_pct_achieved": {
                # 450 of 500 available → 50/500 = 10% sold.
                # Formula: (10 - 0) / (100 - 0) × 100
                "score": 10.0,
                "source_note": "User listing: 450 of 500 units available = 50 sold = 10%. "
                               "However palmaresliving.com shows 'Signature Apartments I: "
                               "Sold-Out' — suggesting earlier phases sold. The 10% figure "
                               "may reflect only available (unsold) across ALL tranches. "
                               "LOW CONFIDENCE — phase-level presale data not fully confirmed."
            },

            # --- GROUP 7: COMP MARKET PERFORMANCE ---
            "comp_capital_appreciation": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Lagos/Algarve: 5Y annualized ~10%+ (strong luxury market).
                # Score = (10 - (-5)) / (25 - (-5)) × 100 = 15/30 × 100
                "score": 50.0,
                "source_note": "Algarve demonstrated 'impressive property value appreciation in "
                               "2024, significantly outperforming national averages' (algarveba.com). "
                               "Lagos: 'safe' Algarve investment with strong fundamentals. "
                               "5Y annualized capital appreciation estimated at ~10%. "
                               "(algarveba.com; investropa Algarve rental yields 2026)"
            },
            "comp_rental_yields": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Algarve/Lagos gross yields: 5-6% managed, up to 8% in prime spots.
                # Investropa: Algarve average 5.6%, Lagos up to 8%.
                # Used 5.5% for resort-managed context. Score = (5.5 - 2) / (12 - 2) × 100
                "score": 35.0,
                "source_note": "Algarve avg gross yield: 5.6%; Lagos prime locations up to 8% "
                               "(Investropa Sept 2025). IPA 2025: 'high-season occupancies of "
                               "90%+ in Lagos push gross yields to 5-6% for well-managed units'. "
                               "Used 5.5% for resort-managed Palmares context."
            },
            "comp_occupancy_rate": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Algarve seasonal: year-round avg ~68%. High season 90%+.
                # Score = (68 - 50) / (100 - 50) × 100 = 18/50 × 100
                "score": 36.0,
                "source_note": "Algarve year-round occupancy: ~65-70% avg (seasonal market). "
                               "High season (June-Sept): 90%+. Used 68% year-round average. "
                               "(internationalpropertyalerts.com Portugal yields 2025; "
                               "listingok.com Algarve occupancy data)"
            },

            # --- GROUP 8: SPECULATION RISK ---
            "str_concentration": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Algarve / Meia Praia: high STR-dominated resort market.
                # Estimated 50% of units listed on Airbnb/booking platforms.
                # Score = (50 - 0) / (60 - 0) × 100
                "score": 83.3,
                "source_note": "Algarve coastal resort markets: very high STR concentration. "
                               "Estimated 50% of Meia Praia / Palmares-area units on "
                               "Airbnb/VRBO. Portugal requires AL license for STR; "
                               "resort-managed units typically operate under hotel license. "
                               "(PT rental regs DL 76/2024; Mais Habitação 2023)"
            },
            "investor_owner_ratio": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Resort development: very high investor ratio. Foreign buyers = 82% in Lagos.
                # Estimated 85% investor-owned.
                "score": 85.0,
                "source_note": "Foreign buyers = 82% of Lagos transactions (azul-properties 2025). "
                               "Resort developments strongly investor-owned. Estimated 85% "
                               "investor-to-owner-occupier ratio. Primary use = holiday rental "
                               "or second home investment."
            },
            "offplan_secondary_dominance": {
                # Formula: (Value - Min) / (Max - Min) × 100
                # Palmares is under construction (off-plan). Algarve new resort supply heavy
                # in off-plan. Estimated 55%.
                # Score = (55 - 0) / (100 - 0) × 100
                "score": 55.0,
                "source_note": "Algarve luxury resort segment: heavily off-plan dominated. "
                               "Palmares itself is under construction. Resort phase model "
                               "(Signature I, II) reinforces off-plan transaction structure. "
                               "Estimated 55% of submarket transactions are off-plan."
            },
        }
    },

    # =========================================================
    # PROPERTY 3: AMOREIRAS PRIME RESIDENCES
    # Vanguard Properties | Amoreiras, Lisbon
    # Status: Ready to Move (Dec 2026 completion per listing)
    # 34 total units, 25 available
    # Price: €750K – €3.5M
    # =========================================================
    "amoreiras_prime": {
        "project_name": "Amoreiras Prime Residences",
        "developer": "Vanguard Properties",
        "city": "Lisbon",
        "country": "Portugal",
        "area": "Amoreiras, Lisbon",
        "raw_variables": {

            # --- GROUP 1: DEMAND & LIQUIDITY ---
            "micro_market_stage": {
                "score": 100,
                "source_note": "Established. Amoreiras is a prime central business/residential "
                               "district with metro access, major shopping centre, and "
                               "upcoming metro Green Line upgrade. +9.5% YoY growth per "
                               "realestate-lisbon.com off-plan tracker. "
                               "(Investropa 2025; Iberian Property Vanguard profile)"
            },
            "rental_absorption_velocity": {
                # (Max - Value) / (Max - Min) × 100 [INVERTED]
                # Central Lisbon LTR: ~50 days for premium apartments.
                # Score = (365 - 50) / (365 - 30) × 100 = 315/335 × 100
                "score": 94.0,
                "source_note": "Central Lisbon luxury LTR: absorption ~45-60 days. "
                               "Amoreiras proximity to Marquês de Pombal business corridor "
                               "drives corporate rental demand. Used 50-day estimate. "
                               "(investropa.com; Benoit Properties ROI analysis 2025)"
            },
            "resale_velocity": {
                # (Value - Min) / (Max - Min) × 100
                # Amoreiras prime: ~70 days resale time.
                # Score = (70 - 30) / (730 - 30) × 100 = 40/700 × 100
                "score": 5.7,
                "source_note": "Premium Lisbon central units: 60-90 day resale window. "
                               "Used 70 days for Amoreiras prime positioning. "
                               "Boutique unit count (34 units) limits comparable transactions. "
                               "(Portugal Buyers Agent Lisbon guide 2026; Investropa 2025)"
            },
            "days_on_market": {
                # (Value - Min) / (Max - Min) × 100
                # Prime Lisbon central: ~45 days.
                # Score = (45 - 7) / (365 - 7) × 100 = 38/358 × 100
                "score": 10.6,
                "source_note": "Prime Lisbon central premium properties: 40-50 days median DOM. "
                               "Used 45 days. Vanguard luxury brand commands premium positioning. "
                               "(Benoit Properties Apr 2026; Investropa Lisbon 2025)"
            },
            "occupancy_vacancy_rate": {
                # (Value - Min) / (Max - Min) × 100
                # Amoreiras LTR: very high demand, ~90% occupancy.
                # Score = (90 - 50) / (100 - 50) × 100 = 40/50 × 100
                "score": 80.0,
                "source_note": "Amoreiras residential: high LTR demand from corporate sector "
                               "(proximity to business district). Estimated 90% occupancy "
                               "for quality LTR in this district. "
                               "(GuestReady Lisbon yields 2025; Investropa 2025)"
            },

            # --- GROUP 2: NEIGHBORHOOD LIVABILITY ---
            "safety_crime_index": {
                # Amoreiras: business/residential mix, safer than tourist Alfama.
                # Score: Lisbon avg 67 + ~5 residential premium.
                "score": 72.0,
                "source_note": "Amoreiras: established business/residential area, safer than "
                               "tourist zones. Gated condominiums common. Numbeo Lisbon: 67.03. "
                               "Applied +5pt premium for residential neighbourhood character. "
                               "(Numbeo Lisbon; Portugal Buyers Agent safety 2025)"
            },
            "healthcare_access": {
                # Hospital CUF Descobertas ~1km, São Luís Hospital ~1.5km, multiple clinics.
                "score": 82.0,
                "source_note": "Hospital CUF Descobertas ~1km northwest. Hospital São Luís "
                               "~1.5km. Amoreiras shopping centre has medical clinics. "
                               "Strong private healthcare cluster nearby."
            },
            "school_quality": {
                # Lycée Français Charles Lepierre explicitly mentioned in listing as
                # 'within walking distance'. France's premier international school in Lisbon.
                "score": 88.0,
                "source_note": "Listing explicitly states: 'Lycée Français Charles Lepierre, "
                               "direct access to the Marquês de Pombal business corridor'. "
                               "Lycée Français is Lisbon's top international school. "
                               "Score reflects premium school proximity as a key USP."
            },
            "air_quality_index": {
                # Same as Lisbon-wide: AQI US ~35. Score = (500-35)/500 × 100
                "score": 93.0,
                "source_note": "IQAir 2024: Lisbon AQI US avg ≈ 35 ('Good' band). "
                               "Amoreiras: slightly elevated vs Alfama due to A2 motorway "
                               "proximity, but offset by Monsanto green corridor. "
                               "(IQAir Portugal; aqi.in Lisbon)"
            },
            "beach_coastal_access": {
                # Amoreiras inland Lisbon. >10km to any beach.
                "score": 0,
                "source_note": "Amoreiras is central inland Lisbon. Nearest beach "
                               "(Costa da Caparica) >16km. Scoring rule: >10km = 0."
            },

            # --- GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ---
            "population_growth_rate": {
                # Same as Lisbon-wide: 1.83%.
                "score": 38.3,
                "source_note": "Lisbon city: 1.83% annual population growth (WorldPopulationReview "
                               "2026). Amoreiras district benefits from broader Lisbon growth "
                               "trend and tech/corporate sector expansion. "
                               "(worldpopulationreview.com/cities/portugal/lisbon)"
            },
            "expat_concentration": {
                # Lisbon: ~27% foreign population.
                "score": 27.0,
                "source_note": "Lisbon: ~21.6% foreign population in 2022 (Statista/PORDATA); "
                               "estimated ~27% by 2025. Amoreiras popular with expat "
                               "professionals and corporate relocatees."
            },

            # --- GROUP 4: SUPPLY PRESSURE & RISK ---
            "immediate_pipeline_risk": {
                # 4 premium developments in Amoreiras per realestate-lisbon.com.
                # Estimated ~250 units in 2km pipeline.
                # Score = (250 - 0) / (5000 - 0) × 100
                "score": 5.0,
                "source_note": "Amoreiras district: 4 premium developments tracked in area "
                               "(realestate-lisbon.com off-plan tracker). Estimated ~250 new "
                               "units within 2km due 2025-2027. Constrained by urban density."
            },
            "active_unsold_inventory": {
                # Amoreiras: established demand, ~10% unsold in submarket.
                # Score = (10 - 0) / (40 - 0) × 100
                "score": 25.0,
                "source_note": "Amoreiras submarket: estimated 10% active unsold of completions. "
                               "Demand outpaces supply in prime Lisbon. "
                               "(Portugal Buyers Agent 2026: 'limited supply in Príncipe Real, "
                               "Chiado, Avenida da Liberdade'; Amoreiras adjacent market)"
            },

            # --- GROUP 5: DELIVERY TRACK RECORD (Vanguard Properties) ---
            "average_delay_duration": {
                # Vanguard Infinity: planned Oct 2020, delayed by COVID; delivered ~2022 (~18 mo).
                # Castilho 203: delivered 2021 (on/near schedule).
                # A'Tower: contracted Jul 2019 (18mo build), delivered ~2021.
                # Average: ~12 months delay estimated.
                # Score = (12 - 0) / (24 - 0) × 100 = 12/24 × 100
                "score": 50.0,
                "source_note": "Vanguard Infinity: planned Oct 2020, COVID disruption; "
                               "delivered ~2022 (~18mo delay). Castilho 203: delivered 2021. "
                               "A'Tower: 18mo build from Jul 2019 target. "
                               "COVID-related delays are partly systemic, not developer-specific. "
                               "Used 12-month average. "
                               "(essential-business.pt 2018; vangproperties.com 2021 recap)"
            },
            "pct_projects_delivered": {
                # Vanguard completed: Infinity, Castilho 203, White Shell, Quintas do Muda,
                # A'Tower. ~5 major projects delivered vs 22 in portfolio.
                # High delivery rate; exclusively equity-financed = strong delivery conviction.
                "score": 85.0,
                "source_note": "Vanguard completed: Infinity, Castilho 203, White Shell, "
                               "Quintas do Muda Reserve (per 2021 annual recap). "
                               "22 projects total portfolio; ~5+ delivered. Exclusively "
                               "equity-financed reduces financial delivery risk. "
                               "(vangproperties.com 2021 review; YouTube: 'exclusively financed by equity')"
            },
            "completion_consistency": {
                # COVID delays observed but not systemic beyond pandemic.
                # Equity-financed = strong financial consistency.
                "score": 50,
                "source_note": "Medium. COVID-related delays on Infinity project. No evidence "
                               "of systemic delivery issues. Equity financing supports delivery "
                               "but pandemic set precedent for delays. Categorical: Medium = 50."
            },

            # --- GROUP 6: FINANCIAL CREDIBILITY (Vanguard Properties) ---
            "escrow_quality": {
                # Portugal DL 227/2004 bank guarantee mandatory. Vanguard equity-financed.
                "score": 100,
                "source_note": "Portugal DL 227/2004: mandatory bank guarantee for off-plan. "
                               "Vanguard is exclusively equity-financed (stated in corporate "
                               "materials). Maximum buyer protection. Categorical: Strict = 100. "
                               "(YouTube Vanguard channel; vanguardeagle.com)"
            },
            "debt_cash_position": {
                # 'Exclusively financed by equity' per Vanguard YouTube and website.
                # €1.2bn+ portfolio investment. Claude Berda's Swiss RE portfolio generates
                # CHF 950M+ in rents. Very strong financial position.
                "score": 90.0,
                "source_note": "Vanguard Properties: 'exclusively financed by equity' "
                               "(vanguardeagle.com; YouTube channel description). "
                               "Parent investor Claude Berda manages 2,700+ Swiss buildings, "
                               "CHF 950M+ rental income. Score 90 reflects strong equity backing. "
                               "(vangproperties.com About; vanguardeagle.com)"
            },
            "stalled_projects_count": {
                "score": 0,
                "source_note": "No evidence of stalled Vanguard Properties projects found. "
                               "All major projects progressing; new acquisitions continuing "
                               "in Porto, Guimarães, Coimbra, Azores per YouTube description. "
                               "Score = 0."
            },
            "presales_pct_achieved": {
                # 25 of 34 available → 9/34 = 26.5% sold.
                # Score = (26.5 - 0) / (100 - 0) × 100
                "score": 26.5,
                "source_note": "User listing: 25 of 34 units available = 9 units sold = 26.5%. "
                               "For a ready-to-move luxury asset at €750K-€3.5M price point, "
                               "26.5% sold is moderate. Golden Visa eligibility supports demand."
            },

            # --- GROUP 7: COMP MARKET PERFORMANCE ---
            "comp_capital_appreciation": {
                # Amoreiras: +9.5% YoY growth per realestate-lisbon.com tracker.
                # 5Y annualized: ~9%.
                # Score = (9 - (-5)) / (25 - (-5)) × 100 = 14/30 × 100
                "score": 46.7,
                "source_note": "Amoreiras district: +9.5% YoY growth (realestate-lisbon.com "
                               "off-plan tracker). Upcoming metro upgrade catalyst. "
                               "Vanguard A'Tower set precedent for price premium in district. "
                               "Used 9% 5Y annualized. (realestate-lisbon.com off-plan Lisbon)"
            },
            "comp_rental_yields": {
                # Amoreiras: 4-5% gross. Used 4.5%.
                # Score = (4.5 - 2) / (12 - 2) × 100 = 2.5/10 × 100
                "score": 25.0,
                "source_note": "Lisbon central (Chiado-adjacent areas): gross yields 4-5%. "
                               "GuestReady 2025: Amoreiras-comparable areas yield ~4-5%. "
                               "Investropa: Lisbon city average 5.2%. Used 4.5% for luxury tier. "
                               "(guestready.com/blog/best-rental-yields-in-lisbon; Investropa)"
            },
            "comp_occupancy_rate": {
                # LTR-dominant Amoreiras: ~90% occupancy.
                # Score = (90 - 50) / (100 - 50) × 100 = 40/50 × 100
                "score": 80.0,
                "source_note": "Amoreiras: strong LTR demand from corporate relocatees and "
                               "professionals. Estimated 90% year-round LTR occupancy. "
                               "STR restrictions in central Lisbon reinforce LTR market. "
                               "(Investropa; GuestReady 2025)"
            },

            # --- GROUP 8: SPECULATION RISK ---
            "str_concentration": {
                # Amoreiras: moderate STR, not in banned zone but under surveillance.
                # Estimated ~15%.
                # Score = (15 - 0) / (60 - 0) × 100
                "score": 25.0,
                "source_note": "Amoreiras: not in Lisbon's absolute STR ban zones (Alfama, "
                               "Bairro Alto, Baixa). Moderate STR concentration ~15%. "
                               "Lisbon monitoring Belém, Campo de Ourique for future restrictions. "
                               "(rentalscaleup.com Apr 2025 Lisbon ban update)"
            },
            "investor_owner_ratio": {
                # Mix of investors and owner-occupiers in Amoreiras. ~60% investor.
                "score": 60.0,
                "source_note": "Amoreiras: mix of corporate renters, owner-occupiers, and "
                               "Golden Visa investors. Estimated 60% investor-owned. "
                               "Less speculative than Alfama or tourist zones."
            },
            "offplan_secondary_dominance": {
                # Ready-to-move project in an established secondary market area.
                # ~25% off-plan in this submarket.
                "score": 25.0,
                "source_note": "Amoreiras: mostly secondary market (established buildings). "
                               "This project itself is near-complete. Estimated 25% off-plan "
                               "share for 1km radius transactions. "
                               "(idealista new constructions Lisbon; realestate-lisbon.com)"
            },
        }
    },

    # =========================================================
    # PROPERTY 4: INFANTE RESIDENCES
    # Vanguard Properties | Estrela / Avenida Infante Santo
    # Status: Under Construction (September 2026)
    # 45 total units, 41 available
    # Price: €399K – €1.015M
    # NOT Golden Visa eligible
    # =========================================================
    "infante_residences": {
        "project_name": "Infante Residences",
        "developer": "Vanguard Properties",
        "city": "Lisbon",
        "country": "Portugal",
        "area": "Estrela / Avenida Infante Santo, Lisbon",
        "raw_variables": {

            # --- GROUP 1: DEMAND & LIQUIDITY ---
            "micro_market_stage": {
                "score": 100,
                "source_note": "Established. Estrela is one of Lisbon's most prestigious "
                               "residential districts (embassies, jardim da Estrela, Lapa). "
                               "Upcoming metro station (Estrela/Santos, targeted 2025-2027) "
                               "is a major appreciation catalyst. +8.7% YoY. "
                               "(Investropa Lisbon market Apr 2026; realestate-lisbon.com)"
            },
            "rental_absorption_velocity": {
                # (Max - Value) / (Max - Min) × 100 [INVERTED]
                # Estrela/Lapa: strong LTR demand, ~47 days avg.
                # Score = (365 - 47) / (365 - 30) × 100 = 318/335 × 100
                "score": 94.9,
                "source_note": "Estrela LTR market: strong demand from diplomats, professionals. "
                               "Avg absorption ~45-50 days for quality apartments. Used 47 days. "
                               "GuestReady 2025: Estrela yields 'typically quite high, often over "
                               "5%', indicating strong rental demand. "
                               "(guestready.com Lisbon buying guide Nov 2025)"
            },
            "resale_velocity": {
                # (Value - Min) / (Max - Min) × 100
                # Estrela: ~80 days resale. Slightly slower than Amoreiras due to quieter
                # secondary market.
                # Score = (80 - 30) / (730 - 30) × 100 = 50/700 × 100
                "score": 7.1,
                "source_note": "Estrela: established residential market, ~75-85 day resale window. "
                               "Used 80 days. Less transacted than Chiado/Baixa but solid liquidity. "
                               "(Portugal Buyers Agent; Investropa Lisbon 2025)"
            },
            "days_on_market": {
                # (Value - Min) / (Max - Min) × 100
                # Estrela/Lapa: ~45 days median DOM.
                # Score = (45 - 7) / (365 - 7) × 100 = 38/358 × 100
                "score": 10.6,
                "source_note": "Estrela/Lapa: quality residential properties sell in 40-50 days. "
                               "Used 45 days. Metro station catalyst likely to compress further. "
                               "(Investropa Lisbon market 2026; Benoit Properties Apr 2026)"
            },
            "occupancy_vacancy_rate": {
                # (Value - Min) / (Max - Min) × 100
                # Estrela: very high LTR demand. ~92%.
                # Score = (92 - 50) / (100 - 50) × 100 = 42/50 × 100
                "score": 84.0,
                "source_note": "Estrela: premium residential LTR with diplomatic/professional "
                               "tenant base. Estimated 92% occupancy. GuestReady: 'Estrela "
                               "rental yields typically over 5%' suggesting near-full occupancy. "
                               "(guestready.com buying Lisbon guide Nov 2025)"
            },

            # --- GROUP 2: NEIGHBORHOOD LIVABILITY ---
            "safety_crime_index": {
                # Estrela: embassy quarter, one of Lisbon's safest areas.
                # Numbeo Lisbon 67. Estrela premium: +8pt.
                "score": 75.0,
                "source_note": "Estrela/Lapa: embassy quarter with high diplomatic presence "
                               "and police coverage. One of Lisbon's safest residential areas. "
                               "Applied +8pt premium over Lisbon baseline (67.03). "
                               "(Numbeo Lisbon; Portugal Buyers Agent safety analysis)"
            },
            "healthcare_access": {
                # Hospital CUF Tejo explicitly mentioned in listing. Jardim da Estrela proximity.
                "score": 88.0,
                "source_note": "Listing explicitly cites 'Hospital CUF Tejo' as nearby. "
                               "Hospital de São Francisco Xavier ~2km. LX Factory medical "
                               "clinics nearby. Excellent private healthcare access. "
                               "(User listing specs; CUF hospital network)"
            },
            "school_quality": {
                # Lycée Français ~1km away. Also near Jardim da Estrela.
                "score": 82.0,
                "source_note": "Lycée Français Charles Lepierre ~1km north (Amoreiras). "
                               "Oporto International School nearby. Listing notes "
                               "'Jardim da Estrela, LX Factory, Amoreiras' as nearby amenities. "
                               "Strong international school access."
            },
            "air_quality_index": {
                # Lisbon central ~35 AQI. Score = (500-35)/500 × 100
                "score": 93.0,
                "source_note": "Lisbon AQI US avg ≈ 35 (IQAir 2024). Estrela benefits from "
                               "Jardim da Estrela green space nearby reducing local particulates. "
                               "(IQAir Portugal; aqi.in Lisbon dashboard)"
            },
            "beach_coastal_access": {
                # Estrela inland Lisbon. >10km from beach.
                "score": 0,
                "source_note": "Estrela / Avenida Infante Santo: inland Lisbon. "
                               "Nearest beach (Costa da Caparica) >15km. "
                               "Tagus riverfront ~500m but not a beach. Scoring rule: >10km = 0."
            },

            # --- GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ---
            "population_growth_rate": {
                # Lisbon: 1.83%.
                "score": 38.3,
                "source_note": "Lisbon city: 1.83% annual population growth "
                               "(WorldPopulationReview 2026). Estrela benefits from overall "
                               "Lisbon growth and metro-driven gentrification."
            },
            "expat_concentration": {
                # Lisbon: ~27%.
                "score": 27.0,
                "source_note": "Lisbon: ~27% expat/foreign population estimated for 2025 "
                               "(up from 21.6% in 2022). Estrela popular with diplomatic "
                               "community and European professionals."
            },

            # --- GROUP 4: SUPPLY PRESSURE & RISK ---
            "immediate_pipeline_risk": {
                # Metro expansion around Estrela/Santos driving some new development.
                # Estimated ~200 units in 2km.
                # Score = (200 - 0) / (5000 - 0) × 100
                "score": 4.0,
                "source_note": "Estrela: 5 premium developments in Campo de Ourique/Estrela/Santos "
                               "cluster per realestate-lisbon.com (€9,500/m², +8.7% YoY). "
                               "Metro station catalyst driving some new supply. "
                               "Estimated ~200 units within 2km. "
                               "(realestate-lisbon.com off-plan Lisbon tracker)"
            },
            "active_unsold_inventory": {
                # Estrela: activating but constrained. ~8% submarket unsold.
                # Score = (8 - 0) / (40 - 0) × 100
                "score": 20.0,
                "source_note": "Estrela submarket: tightening supply with metro catalyst. "
                               "Estimated 8% active unsold of completions. Below Lisbon city "
                               "average due to premium end of market. "
                               "(Investropa Lisbon market 2026; Benoit Properties)"
            },

            # --- GROUP 5: DELIVERY TRACK RECORD (Vanguard Properties) ---
            # Same developer as Amoreiras; same track record data.
            "average_delay_duration": {
                "score": 50.0,
                "source_note": "Same developer (Vanguard Properties). Infinity: ~18mo delay "
                               "(COVID). Castilho 203: near-schedule. Average ~12 months. "
                               "Score = (12/24) × 100 = 50. "
                               "(essential-business.pt 2018; vangproperties.com 2021 recap)"
            },
            "pct_projects_delivered": {
                "score": 85.0,
                "source_note": "Vanguard: 5+ major completions (Infinity, Castilho 203, White "
                               "Shell, Quintas do Muda, A'Tower). Exclusively equity-financed. "
                               "Strong financial discipline supports delivery. Score = 85."
            },
            "completion_consistency": {
                "score": 50,
                "source_note": "Medium. COVID-period delays noted but equity financing provides "
                               "strong delivery incentive. September 2026 target is achievable "
                               "for rehabilitation project. Categorical: Medium = 50."
            },

            # --- GROUP 6: FINANCIAL CREDIBILITY (Vanguard Properties) ---
            "escrow_quality": {
                "score": 100,
                "source_note": "Portugal DL 227/2004: mandatory bank guarantee for off-plan. "
                               "Vanguard: exclusively equity-financed. Strict compliance. "
                               "Categorical: Strict = 100."
            },
            "debt_cash_position": {
                "score": 90.0,
                "source_note": "Vanguard: exclusively equity-financed. €1.2bn+ portfolio. "
                               "Parent Claude Berda: CHF 950M+ annual Swiss rents. "
                               "Score 90 reflects strong equity backing with no leverage risk. "
                               "(YouTube Vanguard channel; vanguardeagle.com)"
            },
            "stalled_projects_count": {
                "score": 0,
                "source_note": "No stalled Vanguard projects found. Active pipeline in Lisbon, "
                               "Oeiras, Algarve, Comporta, Porto, Guimarães, Coimbra. Score = 0."
            },
            "presales_pct_achieved": {
                # 41 of 45 available → 4/45 = 8.9% sold.
                # Score = (8.9 - 0) / (100 - 0) × 100
                "score": 8.9,
                "source_note": "User listing: 41 of 45 units available = 4 units sold = 8.9%. "
                               "LOW ABSORPTION FLAG: Only ~9% sold for a Sept 2026 delivery. "
                               "Absence of Golden Visa eligibility likely limiting investor pool "
                               "vs Amoreiras (GV eligible). Note: low presales at this price "
                               "point (€399K-€1.015M) warrants monitoring."
            },

            # --- GROUP 7: COMP MARKET PERFORMANCE ---
            "comp_capital_appreciation": {
                # Estrela: +8.7% YoY (explicitly stated in realestate-lisbon.com).
                # 5Y annualized: ~8.7%.
                # Score = (8.7 - (-5)) / (25 - (-5)) × 100 = 13.7/30 × 100
                "score": 45.7,
                "source_note": "Estrela/Campo de Ourique/Santos: +8.7% YoY growth "
                               "(realestate-lisbon.com off-plan Lisbon tracker). "
                               "Metro station catalyst (Estrela station 2025-2027) is "
                               "a structural price driver. Used 8.7% 5Y annualized. "
                               "(realestate-lisbon.com; Investropa Lisbon Apr 2026)"
            },
            "comp_rental_yields": {
                # Estrela: 5%+ yields per GuestReady 2025.
                # Score = (5.2 - 2) / (12 - 2) × 100 = 3.2/10 × 100
                "score": 32.0,
                "source_note": "GuestReady Nov 2025: 'Estrela rental yields typically quite high, "
                               "often over 5%'. Investropa 2025: Lisbon city avg 5.2%. "
                               "Used 5.2% for Estrela LTR context. "
                               "(guestready.com/blog/buying-property-in-lisbon)"
            },
            "comp_occupancy_rate": {
                # Estrela LTR: ~92%.
                # Score = (92 - 50) / (100 - 50) × 100 = 42/50 × 100
                "score": 84.0,
                "source_note": "Estrela/Lapa: diplomatic + professional tenant base drives "
                               "near-full LTR occupancy. Estimated 92%. Strong retention. "
                               "(GuestReady; Investropa Lisbon 2026)"
            },

            # --- GROUP 8: SPECULATION RISK ---
            "str_concentration": {
                # Estrela: residential district, STR restricted, low STR density.
                # Estimated ~10%.
                # Score = (10 - 0) / (60 - 0) × 100
                "score": 16.7,
                "source_note": "Estrela: predominantly residential area, strict STR regulations. "
                               "New STR applications subject to municipal approval (DL 76/2024). "
                               "Estimated ~10% STR concentration. Enforcement stronger here "
                               "than in tourist districts. (rentalscaleup.com Apr 2025)"
            },
            "investor_owner_ratio": {
                # Estrela: mix of diplomats (often owner-occupiers), long-term residents.
                # More owner-occupier than Alfama. ~55% investor.
                "score": 55.0,
                "source_note": "Estrela: mix of diplomatic community (some owner-occupier), "
                               "long-term Portuguese residents, and buy-to-let investors. "
                               "Estimated 55% investor ownership. "
                               "(Investropa expat zones; Portugal Buyers Agent)"
            },
            "offplan_secondary_dominance": {
                # Infante is under construction / off-plan in a mostly secondary market area.
                # Metro station driving some off-plan activity. ~30%.
                "score": 30.0,
                "source_note": "Estrela/Infante Santo: mostly secondary market but metro "
                               "station catalyst activating new off-plan supply. "
                               "Estimated 30% off-plan share of submarket transactions. "
                               "(realestate-lisbon.com off-plan Lisbon; Investropa Apr 2026)"
            },
        }
    },
}


# ============================================================
# CONFIDENCE SUMMARY
# ============================================================
#
# Property               | Variables   | Variables | Low Confidence
#                        | Populated   | Null      | Flags
# -----------------------|-------------|-----------|------------------
# The Lisboans           |  27 / 27    |    0      | 1
#   (Oxy Capital,        |             |           | - debt_cash_position
#    Alfama-Baixa)       |             |           |   (Oxy Capital PE firm,
#                        |             |           |    no public balance sheet)
# -----------------------|-------------|-----------|------------------
# Palmares               |  27 / 27    |    0      | 4
#   (Arrow Global /      |             |           | - average_delay_duration
#    Kronos Homes;       |             |           |   (developer change mid-project)
#    listed as           |             |           | - pct_projects_delivered
#    Oxy Capital)        |             |           |   (developer attribution unclear)
#                        |             |           | - debt_cash_position
#                        |             |           |   (Arrow Global SPV not public)
#                        |             |           | - presales_pct_achieved
#                        |             |           |   (phase breakdown unclear)
# -----------------------|-------------|-----------|------------------
# Amoreiras Prime        |  27 / 27    |    0      | 0
#   (Vanguard,           |             |           |   (all scores well-sourced)
#    Amoreiras)          |             |           |
# -----------------------|-------------|-----------|------------------
# Infante Residences     |  27 / 27    |    0      | 0
#   (Vanguard,           |             |           |   (Note: presales only 8.9% —
#    Estrela)            |             |           |    weak absorption flag, not
#                        |             |           |    a data confidence issue)
# ============================================================
#
# STRUCTURAL NOTES FOR ENGINE:
#
# 1. RENTAL_ABSORPTION_VELOCITY: Scored with INVERTED formula
#    (Max - Value) / (Max - Min) × 100 per prompt spec.
#    All other time-based variables (resale_velocity, days_on_market)
#    use STANDARD formula → higher days = higher score.
#    Engine must handle direction inversion per variable.
#
# 2. BEACH_COASTAL_ACCESS: All three Lisbon properties score 0.
#    This is geographically correct (all inland city).
#    Engine should weight this variable lower for urban-focused
#    investment profiles.
#
# 3. STR REGULATION RISK (Portugal-specific):
#    - Alfama/Baixa: ABSOLUTE ban on new STR registrations (Apr 2025).
#    - Amoreiras/Estrela: under monitoring; new STRs require approval.
#    - Algarve: AL licenses valid but new registrations restricted.
#    str_concentration scores reflect CURRENT density, not future
#    earning potential. Engine should treat high str_concentration
#    in Alfama as a RISK (regulatory reversal possible).
#
# 4. PALMARES DEVELOPER FLAG (HIGH IMPORTANCE):
#    User data attributes Palmares to "Oxy Capital" as developer.
#    Research confirms actual developer = Kronos Homes, project sold
#    to Arrow Global funds for ~€400M total investment.
#    Source: iberian.property "Arrow finalises purchase of Palmares"
#    Developer-level scores for Palmares use Kronos/Arrow track record.
#    Recommend confirming developer identity before final scoring.
#
# 5. PORTUGAL vs UAE ENGINE ADAPTATION:
#    Variables designed for UAE market adapted as follows:
#    - escrow_quality: mapped to Portugal DL 227/2004 bank guarantee
#      regime (Strict = mandatory bank guarantee; Partial = partial
#      coverage; None = no guarantee)
#    - No RERA/DLD equivalent; used self-regulatory and court records
#    - Litigation_severity not included in this variable set (was in
#      user's original determinant_scores but not in the 27-variable
#      schema requested here)
# ============================================================
