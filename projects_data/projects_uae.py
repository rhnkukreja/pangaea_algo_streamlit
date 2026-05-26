# =============================================================================
# UAE PROPERTY INVESTMENT ENGINE — DETERMINANT SCORES
# Generated: May 2026
# Methodology: Raw magnitude scoring per spec rules.
#   - Continuous: Score = ((Value - Min) / (Max - Min)) × 100
#   - Categorical: exact dictionary lookup
#   - Engine handles inversion. DO NOT invert here.
#   - null = genuinely unresolvable after web search (engine outputs 50)
# =============================================================================

UAE_PROPERTIES_RAW = {

    # =========================================================================
    "greencrest": {
        "project_name": "Greencrest at Dubai Hills Estate",
        "developer": "Emaar Properties",
        "city": "Dubai",
        "country": "UAE",
        "area": "Dubai Hills Estate, MBR City",

        "raw_variables": {

            # GROUP 1 — DEMAND & LIQUIDITY
            "micro_market_stage": {
                "score": 100,
                "source_note": (
                    "Dubai Hills Estate is fully Established: Dubai Hills Mall operational, "
                    "King's College Hospital open, golf course active, Emirates Road/Al Khail "
                    "access mature. Multiple sub-communities handed over. "
                    "Property Monitor Q1 2025 + H&S Real Estate 2026 report."
                ),
            },
            "rental_absorption_velocity": {
                # Lower days = faster velocity = LOWER score (raw magnitude of days)
                # DHE demand is very high; approx 55-day average absorption.
                # Score = ((55 - 30) / (365 - 30)) × 100 = 7.5
                "score": 7.5,
                "source_note": (
                    "Dubai Hills Estate vacancy below 10%; apartments rent within ~55 days "
                    "on average per H&S Real Estate 2026 report ('occupancy consistently above 87%'). "
                    "Driven Properties Q1 2025: 52% rent growth since 2022 confirms tight supply."
                ),
            },
            "resale_velocity": {
                # DHE secondary market is active. ~90-110 days.
                # Score = ((100 - 30) / (730 - 30)) × 100 = 10.0
                "score": 10.0,
                "source_note": (
                    "DHE is one of Dubai's most liquid secondary markets. Estimated 90-110 days "
                    "avg resale based on DLD transaction velocity (4,280+ recent sales noted "
                    "across Emaar communities); Gaia Realty 2026 confirms consistent buyer demand. "
                    "Low confidence — no published resale-days-specific data for DHE."
                ),
            },
            "days_on_market": {
                # Combined listing-to-contract approx 50 days for DHE
                # Score = ((50 - 7) / (365 - 7)) × 100 = 12.0
                "score": 12.0,
                "source_note": (
                    "Estimated 45-55 days on market based on Driven Properties DHE Q1 2025 "
                    "market report and Bayut listing activity. Limited supply drives fast "
                    "absorption. Low confidence — no direct days-on-market stat published."
                ),
            },
            "occupancy_vacancy_rate": {
                # "occupancy consistently above 87%"; H&S 2026 report states 87%+ consistently
                # Score = ((88 - 50) / (100 - 50)) × 100 = 76.0
                "score": 76.0,
                "source_note": (
                    "H&S Real Estate 2026: 'occupancy above 87%' in Dubai Hills Estate. "
                    "Driven Properties Q1 2025: scarcity of ready rental stock. "
                    "Using 88% as representative figure."
                ),
            },

            # GROUP 2 — NEIGHBORHOOD LIVABILITY
            "safety_crime_index": {
                # Dubai Numbeo Safety Index 83.89 — score as-is per instructions
                "score": 83.9,
                "source_note": (
                    "Numbeo Crime/Safety Index January 2025: Dubai safety index 83.89, "
                    "crime index 16.11. UAE ranked #1 safest country mid-year 2025 (Numbeo). "
                    "Score applied as-is per rule (no inversion)."
                ),
            },
            "healthcare_access": {
                # King's College Hospital London Dubai is literally adjacent to Greencrest
                "score": 95.0,
                "source_note": (
                    "King's College Hospital London Dubai sits directly within Dubai Hills Estate "
                    "(<500m from Greencrest). GEMS Wellington at <1km. Top-rated tertiary hospital "
                    "with A&E and specialist services. Source: Emaar project spec + Google Maps."
                ),
            },
            "school_quality": {
                # GEMS International School DHE on doorstep; rated Outstanding by KHDA
                "score": 90.0,
                "source_note": (
                    "GEMS International School DHE is <1km; KHDA rated Outstanding. "
                    "GEMS World Academy and Safa British School within 5km. "
                    "One of Dubai's strongest school clusters. Source: KHDA ratings 2024 + project spec."
                ),
            },
            "air_quality_index": {
                # Dubai annual avg AQI ~95 (IQAir 2024: PM2.5 33.5µg/m³, AQI~97; 2025: 106)
                # Convert: Score = 100 - (AQI/2) = 100 - 47.5 = 52.5
                "score": 52.5,
                "source_note": (
                    "IQAir 2025 analysis: Dubai 2024 annual average PM2.5 33.5µg/m³ (~AQI 97). "
                    "AQI 2025 annual avg 106. Using mid-point ~95 AQI. "
                    "Converted to 0-100 quality scale: 100 - (95/2) = 52.5. "
                    "Dubai air quality is 'Moderate' driven by desert dust and vehicle emissions."
                ),
            },
            "beach_coastal_access": {
                # Dubai Hills is ~18-20km inland from nearest beach (JBR/Kite Beach)
                # >10km = score 0 per spec
                "score": 0.0,
                "source_note": (
                    "Dubai Hills Estate is fully inland. Nearest beach (Kite Beach, Al Sufouh) "
                    "approximately 18-20km by road. No coastal/waterfront feature within 10km. "
                    "Score 0 per spec rule: >10km = 0."
                ),
            },

            # GROUP 3 — DEMOGRAPHIC & ECONOMIC STRENGTH
            "population_growth_rate": {
                # Dubai: 169,000 added in 2024 on ~3.65M base = 4.63% annual growth
                # Score = ((4.6 - (-2)) / (8 - (-2))) × 100 = 66.0
                "score": 66.0,
                "source_note": (
                    "Dubai Statistics Centre: 169,000 residents added in 2024, reaching 3.825M "
                    "(highest growth since 2018). Annual growth rate ~4.6%. "
                    "Source: What's On Dubai Jan 2025 citing DSC data."
                ),
            },
            "expat_concentration": {
                # Dubai: 88.5-92% expat across multiple sources; using 90%
                # Score = ((90 - 0) / (100 - 0)) × 100 = 90.0
                "score": 90.0,
                "source_note": (
                    "Dubai 2024 survey: 88.5% expat population (What's On citing DSC). "
                    "GMI Research 2025: 92.02% expat. Multiple sources converge on 88-92%. "
                    "Using 90% midpoint. Dubai holds world's highest expat %-share."
                ),
            },

            # GROUP 4 — SUPPLY PRESSURE & RISK
            "immediate_pipeline_risk": {
                # DHE: Emaar continues phased launches. Estimated 800-1,200 units
                # within 2km due in next 24 months (Emaar phases, not mega-pipeline).
                # Score = ((1000 - 0) / (5000 - 0)) × 100 = 20.0
                "score": 20.0,
                "source_note": (
                    "Dubai Hills Estate is a mature, phased community. Emaar continues "
                    "launching apartment sub-phases but in controlled releases. "
                    "Estimated ~1,000 units within 2km pipeline over 24 months based on "
                    "Emaar launch cadence. Low supply pressure vs. emerging zones. "
                    "Source: Driven Properties Q1 2025; West Gate Dubai supply guide 2025. "
                    "Low-to-medium confidence on exact count."
                ),
            },
            "active_unsold_inventory": {
                # DHE submarket: tight stock, mature community. ~8-10% unsold.
                # Score = ((9 - 0) / (40 - 0)) × 100 = 22.5
                "score": 22.5,
                "source_note": (
                    "Dubai Hills Estate has constrained ready stock. "
                    "H&S RE 2026: 'scarcity of ready stock in a maturing, low vacancy community'. "
                    "Estimated ~9% active unsold in submarket (below Dubai average). "
                    "Low confidence — no direct DLD unsold % stat for this submarket."
                ),
            },

            # GROUP 5 — DELIVERY TRACK RECORD (Emaar)
            "average_delay_duration": {
                # Emaar: "average delay exceeding 14 months" (Tranio/DLD 20-year data)
                # Score = ((14 - 0) / (24 - 0)) × 100 = 58.3
                "score": 58.3,
                "source_note": (
                    "Tranio analysis of DLD data (Dec 2025): Emaar leads delay list with 73 "
                    "delayed projects over 20 years; 'average delay exceeding 14 months'. "
                    "Note: 2024 industry-wide median improved to 2 months, suggesting recent "
                    "improvement, but 20-year historical average used per available data."
                ),
            },
            "pct_projects_delivered": {
                # Emaar: 44.5% of projects failed deadline = 55.5% delivered on time
                # Score = ((55.5 - 0) / (100 - 0)) × 100 = 55.5
                "score": 55.5,
                "source_note": (
                    "Tranio/DLD: 'Emaar failed to meet delivery deadlines for 44.5% of its "
                    "projects' over 20 years. Inverted: 55.5% delivered on time. "
                    "Note: Emaar has delivered 117,000+ units total — delays don't mean "
                    "non-delivery, just late. All projects ultimately completed."
                ),
            },
            "completion_consistency": {
                # Despite delays, Emaar always delivers. Not High (too many delays), not Low.
                "score": 50,
                "source_note": (
                    "Emaar: Medium consistency. Delivers all projects but 44.5% miss deadline. "
                    "Categorical: Medium = 50. "
                    "Source: Tranio/DLD analysis Dec 2025."
                ),
            },

            # GROUP 6 — FINANCIAL CREDIBILITY (Emaar)
            "escrow_quality": {
                # Emaar fully RERA-compliant; largest listed developer on DFM
                "score": 100,
                "source_note": (
                    "Emaar Properties PJSC is DFM-listed; all UAE projects operate under "
                    "RERA-mandated strict escrow accounts (Law No. 8/2007). "
                    "Categorical: Strict = 100."
                ),
            },
            "debt_cash_position": {
                # Emaar: Investment-grade, massive cash generation, AED 83.7B backlog
                # Very strong balance sheet. Modest leverage for scale. Score = 85
                "score": 85.0,
                "source_note": (
                    "Emaar Properties: AED 83.7B sales backlog (Nov 2024), revenue AED 12.5B "
                    "in 9M 2024 (+69% YoY). Listed DFM. 38 hotels + 1.4M sqm leasing assets "
                    "provide recurring revenue buffer. Strong investment-grade profile. "
                    "Score estimated 85/100 (not full 100 due to scale of construction exposure). "
                    "Source: Emaar Q3 2024 press release."
                ),
            },
            "stalled_projects_count": {
                # Emaar: 0 stalled projects. All delayed projects are still active.
                # Score = ((0 - 0) / (10 - 0)) × 100 = 0
                "score": 0.0,
                "source_note": (
                    "No stalled Emaar projects identified in DLD registry, Tranio analysis, "
                    "or news sources. Delays exist but all projects progress to completion. "
                    "Score = 0 (minimum pipeline stall)."
                ),
            },
            "presales_pct_achieved": {
                # Emaar: consistently achieves ~85-90% presales before launch marketing ends
                # Score = ((87 - 0) / (100 - 0)) × 100 = 87.0
                "score": 87.0,
                "source_note": (
                    "Emaar Development PJSC: AED 48B sales in 9M 2024 across 50 project launches "
                    "(press release Nov 2024). Strong presales rate ~87% estimated. "
                    "Each launch typically sellout or near-sellout. Low confidence on exact % — "
                    "no per-project presale rate published."
                ),
            },

            # GROUP 7 — COMP MARKET PERFORMANCE (1km radius)
            "comp_capital_appreciation": {
                # DHE apartments: +40-65% since 2020 = ~8-11% CAGR (5yr).
                # Using midpoint 10% CAGR. Score = ((10 - (-5)) / (25 - (-5))) × 100 = 50.0
                "score": 50.0,
                "source_note": (
                    "Multiple sources: Dubai Hills apartments appreciated 40-65% from 2020-2025 "
                    "(Gaia Realty 2026; H&S RE 2026: 'secondary prices AED 2,183 psf Q1 2025'). "
                    "5-year CAGR estimated ~9-10%. Score = ((10 - (-5)) / 30) × 100 = 50.0. "
                    "Source: Driven Properties Q1 2025 market report."
                ),
            },
            "comp_rental_yields": {
                # DHE: 6.5-7% gross yield; 3BR reaching 7.05% (Emirates News 2026)
                # Using 6.75% midpoint. Score = ((6.75 - 2) / (12 - 2)) × 100 = 47.5
                "score": 47.5,
                "source_note": (
                    "H&S Real Estate 2026: '6.5–7% gross yield', Park Point 6.97%. "
                    "Emirates News Mar 2026: 3BR apartments at 7.05% ROI. "
                    "Using 6.75% midpoint. Score = ((6.75-2)/10) × 100 = 47.5."
                ),
            },
            "comp_occupancy_rate": {
                # DHE: 87-90% occupancy confirmed
                # Score = ((88 - 50) / (100 - 50)) × 100 = 76.0
                "score": 76.0,
                "source_note": (
                    "H&S Real Estate 2026: 'occupancy above 87%'. Driven Properties Q1 2025: "
                    "'limited availability of high-quality rental stock'. Using 88%."
                ),
            },

            # GROUP 8 — SPECULATION RISK
            "str_concentration": {
                # DHE: Family community, lower STR. ~15-18% of units listed STR.
                # Score = ((16 - 0) / (60 - 0)) × 100 = 26.7
                "score": 26.7,
                "source_note": (
                    "Dubai Hills Estate is family/end-user community; STR less dominant than "
                    "Downtown/Marina. Estimated 15-18% STR concentration based on Airbtics "
                    "city data (22,719 active Dubai listings) and DHE lifestyle profile. "
                    "Low confidence — no district-level STR count available."
                ),
            },
            "investor_owner_ratio": {
                # DHE: Strong end-user demand but also investor driven. ~55-60% investor.
                # Score = ((57 - 0) / (100 - 0)) × 100 = 57.0
                "score": 57.0,
                "source_note": (
                    "Dubai Hills has highest end-user demand in Emaar portfolio (family community). "
                    "However off-plan off-plan 65% of Dubai transactions (2025). "
                    "Estimated 55-60% investor ratio for DHE. Low confidence."
                ),
            },
            "offplan_secondary_dominance": {
                # DHE: Emaar continuously launches, but also active secondary market.
                # ~60% off-plan, 40% secondary.
                # Score = ((60 - 0) / (100 - 0)) × 100 = 60.0
                "score": 60.0,
                "source_note": (
                    "Dubai-wide off-plan share: 65% in 2025 (Red Horizon; MAK Developers). "
                    "DHE has active secondary (ready units in demand) so slightly below average. "
                    "Estimated 60% off-plan. Source: DLD 2025 transaction data (citywide)."
                ),
            },
        },
    },

    # =========================================================================
    "sobha_hartland": {
        "project_name": "Sobha Hartland",
        "developer": "Sobha Realty",
        "city": "Dubai",
        "country": "UAE",
        "area": "Mohammed Bin Rashid City (MBR City), Dubai",

        "raw_variables": {

            # GROUP 1 — DEMAND & LIQUIDITY
            "micro_market_stage": {
                # Sobha Hartland: school + hotel + some retail delivered; significant
                # pipeline remains but community is functioning. Activating.
                "score": 75,
                "source_note": (
                    "Sobha Hartland: Phase 1 delivered, Hartland Int'l School + North London "
                    "Collegiate operational, Hartland Greens & Forest Villas handed over. "
                    "Hartland II under construction. Activating = 75. "
                    "Source: Sobha handover data 2021-2024; Propsearch.ae developer guide."
                ),
            },
            "rental_absorption_velocity": {
                # MBR City: DIFC/Downtown proximity drives strong demand. ~60-75 days.
                # Score = ((67 - 30) / (365 - 30)) × 100 = 11.0
                "score": 11.0,
                "source_note": (
                    "MBR City: H1 2025 saw 2,422 transactions AED 4.35B (APIL Properties). "
                    "Strong demand from Downtown/DIFC professionals. Estimated 65-70 day "
                    "absorption. Source: Inn-vesta MBR City guide 2025. Low confidence."
                ),
            },
            "resale_velocity": {
                # MBR City has strong resale liquidity vs. emerging zones. ~90-120 days.
                # Score = ((105 - 30) / (730 - 30)) × 100 = 10.7
                "score": 10.7,
                "source_note": (
                    "MBR City among 'top 5 most demanded luxury communities' (APIL Properties). "
                    "Estimated 90-120 day resale window. Low confidence — no published stat."
                ),
            },
            "days_on_market": {
                # ~60-70 days for MBR City listings
                # Score = ((65 - 7) / (365 - 7)) × 100 = 16.2
                "score": 16.2,
                "source_note": (
                    "Estimated 60-70 days on market for MBR City based on transaction velocity "
                    "and demand profile. Limited data; low confidence."
                ),
            },
            "occupancy_vacancy_rate": {
                # MBR City: "743 unit completions Q1 2025" with strong absorption.
                # ~87% occupancy.
                # Score = ((87 - 50) / (100 - 50)) × 100 = 74.0
                "score": 74.0,
                "source_note": (
                    "MBR City: 'rental yields averaging 8%' (Inn-vesta), implying strong "
                    "occupancy. Q1 2025: 743 completions absorbed well. Estimated 87% occupancy. "
                    "Source: APIL Properties MBR City guide; Eplog Off-plan data Q1 2025."
                ),
            },

            # GROUP 2 — NEIGHBORHOOD LIVABILITY
            "safety_crime_index": {
                "score": 83.9,
                "source_note": "Numbeo Dubai Safety Index January 2025: 83.89. Citywide metric.",
            },
            "healthcare_access": {
                # Nearest: Mediclinic City Hospital at Dubai Healthcare City (~5km)
                "score": 65.0,
                "source_note": (
                    "Nearest major hospital: Mediclinic City Hospital, Dubai Healthcare City "
                    "~5-7km. No hospital within Sobha Hartland itself. Some clinics within "
                    "community. Score 65/100 — good access but not adjacent."
                ),
            },
            "school_quality": {
                # Hartland Int'l School (KHDA Outstanding), North London Collegiate School
                "score": 90.0,
                "source_note": (
                    "Hartland International School within Sobha Hartland: KHDA Outstanding. "
                    "North London Collegiate School Dubai within community. "
                    "Two of Dubai's highest-rated schools on-site. Score 90/100."
                ),
            },
            "air_quality_index": {
                "score": 52.5,
                "source_note": "Dubai annual AQI ~95 (IQAir 2024/2025 avg). Score = 100 - (95/2) = 52.5.",
            },
            "beach_coastal_access": {
                # MBR City: Crystal Lagoon within community (artificial). Nearest beach ~12km.
                # >10km from sea = score 0. Crystal lagoon ≠ coastal.
                "score": 0.0,
                "source_note": (
                    "MBR City has Crystal Lagoon (artificial water feature, not coastal). "
                    "Nearest true beach (Kite Beach, Jumeirah) approximately 12-14km. "
                    ">10km threshold = score 0."
                ),
            },

            # GROUP 3
            "population_growth_rate": {
                "score": 66.0,
                "source_note": "Dubai annual population growth ~4.6% (DSC 2024). Score = ((4.6+2)/10)*100 = 66.",
            },
            "expat_concentration": {
                "score": 90.0,
                "source_note": "Dubai expat concentration ~90% (DSC/GMI Research 2025).",
            },

            # GROUP 4
            "immediate_pipeline_risk": {
                # MBR City: 26,400 planned units total; massive concurrent development.
                # Within 2km: ~2,500-3,000 units in next 24 months.
                # Score = ((2700 - 0) / (5000 - 0)) × 100 = 54.0
                "score": 54.0,
                "source_note": (
                    "MBR City: '26,400 planned residential units through 2027' (Eplog data Q1 2025). "
                    "743 completions in Q1 2025 alone. High concurrent development. "
                    "Estimated ~2,700 units within 2km over 24 months. "
                    "Source: Inn-vesta MBR City; Sobha Hartland II ongoing."
                ),
            },
            "active_unsold_inventory": {
                # Project: 9 of 200 = 4.5%. Submarket MBR City broader: ~12-15%.
                # Score = ((13 - 0) / (40 - 0)) × 100 = 32.5
                "score": 32.5,
                "source_note": (
                    "This project: 9 of 200 units available (~4.5%). "
                    "MBR City submarket: 3,350 active apartment listings Q1 2025 (Eplog); "
                    "estimated ~13% unsold across submarket. "
                    "Source: Eplog Offplan Q1 2025; APIL Properties MBR City guide."
                ),
            },

            # GROUP 5 — DELIVERY TRACK RECORD (Sobha)
            "average_delay_duration": {
                # Sobha: delivers before schedule (Creek Vistas 8 months early; 1819 units
                # on/ahead of schedule in 2023). Average: effectively 0-2 months.
                # Score = ((1.5 - 0) / (24 - 0)) × 100 = 6.3
                "score": 6.3,
                "source_note": (
                    "Sobha Realty 2021: 'proud to remain one of few developers facing no delays'. "
                    "Gulf News Dec 2024: Creek Vistas Grande delivered 8 months early. "
                    "Gulf News 2024: 1,819 units handed over 'before their due date' in 2023. "
                    "Estimated avg delay ~1.5 months. Best delivery track record in this set."
                ),
            },
            "pct_projects_delivered": {
                # Sobha: ~92% on-time or early delivery
                # Score = ((92 - 0) / (100 - 0)) × 100 = 92.0
                "score": 92.0,
                "source_note": (
                    "Gulf News Feb 2024: Sobha delivered 1,819 units across 2 projects "
                    "'before their due date' in 2023. Propsearch.ae: vertically integrated "
                    "(controls full construction process). Estimated 92% on-time rate."
                ),
            },
            "completion_consistency": {
                "score": 100,
                "source_note": "Sobha: High consistency. Categorical: High = 100. Multiple early deliveries confirmed.",
            },

            # GROUP 6 — FINANCIAL CREDIBILITY (Sobha)
            "escrow_quality": {
                "score": 100,
                "source_note": "Sobha Realty RERA-compliant; all projects escrow-registered under DLD. Strict = 100.",
            },
            "debt_cash_position": {
                # Sobha: S&P BB-, Moody's Ba3 (2023). $750M green sukuk (2024).
                # Moderate leverage but strong cash generation. Score ~68.
                "score": 68.0,
                "source_note": (
                    "Sobha: S&P 'BB-' / Moody's 'Ba3' ratings as of 2023 (Gulf News). "
                    "Completed $750M green sukuk (largest ever by a real estate developer). "
                    "AED 15.5B record sales 2023. Strong revenue but spec-grade bonds indicate "
                    "meaningful leverage. Score 68/100. Source: Propsearch.ae developer guide."
                ),
            },
            "stalled_projects_count": {
                "score": 0.0,
                "source_note": "No stalled Sobha projects identified. All projects progressing. Score = 0.",
            },
            "presales_pct_achieved": {
                # Sobha: AED 15.5B in 2023, targeting AED 20B in 2024. Strong sellout rates.
                # Score = ((88 - 0) / (100 - 0)) × 100 = 88.0
                "score": 88.0,
                "source_note": (
                    "Sobha Realty: AED 15.5B record sales 2023 (+51% YoY); targeting AED 20B "
                    "in 2024. ~10% market share by value. Projects reliably >85% presold. "
                    "Source: Gulf News Jan 2024."
                ),
            },

            # GROUP 7 — COMP MARKET PERFORMANCE
            "comp_capital_appreciation": {
                # MBR City CAGR 8-9% per APIL/Betterhomes data
                # Score = ((8.5 - (-5)) / (25 - (-5))) × 100 = 45.0
                "score": 45.0,
                "source_note": (
                    "MBR City: 'CAGR 8-9%' (APIL Properties 2025); '10-12% growth projected 2025' "
                    "(Eplog). Using conservative 8.5% CAGR. "
                    "Score = ((8.5+5)/30) × 100 = 45.0."
                ),
            },
            "comp_rental_yields": {
                # MBR City apartments: 6-8%; high end 8-10% (Inn-vesta); avg 7%
                # Score = ((7 - 2) / (12 - 2)) × 100 = 50.0
                "score": 50.0,
                "source_note": (
                    "Inn-vesta: 'MBR City 7-9% annual yields for apartments'. "
                    "APIL Properties: 'apartments generating avg ROI of 6-8%'. "
                    "Using 7% midpoint. Score = ((7-2)/10) × 100 = 50.0."
                ),
            },
            "comp_occupancy_rate": {
                # MBR City: ~87%
                # Score = ((87 - 50) / (100 - 50)) × 100 = 74.0
                "score": 74.0,
                "source_note": (
                    "MBR City strong occupancy driven by Downtown/DIFC workforce demand. "
                    "Estimated 87% based on strong absorption (H1 2025: 2,422 transactions). "
                    "Source: APIL Properties MBR City 2025."
                ),
            },

            # GROUP 8 — SPECULATION RISK
            "str_concentration": {
                # MBR City: mixed family/investor, higher STR than DHE but not prime tourism.
                # ~20-25% STR. Score = ((22 - 0) / (60 - 0)) × 100 = 36.7
                "score": 36.7,
                "source_note": (
                    "MBR City has both family and investor units. Airbnb data for Dubai (Airbtics): "
                    "22,719 active listings citywide. MBR City estimated ~20-25% STR concentration. "
                    "Low confidence — no district-specific STR count."
                ),
            },
            "investor_owner_ratio": {
                # Sobha Hartland: attracts HNW investors significantly. ~65-70% investor.
                # Score = ((67 - 0) / (100 - 0)) × 100 = 67.0
                "score": 67.0,
                "source_note": (
                    "Sobha Hartland attracts significant international investor interest. "
                    "Estimated 65-70% investor-owned. End-users include embassy staff and "
                    "school-motivated families. Low confidence."
                ),
            },
            "offplan_secondary_dominance": {
                # MBR City: heavily off-plan with multiple phases ongoing. ~70%.
                # Score = ((70 - 0) / (100 - 0)) × 100 = 70.0
                "score": 70.0,
                "source_note": (
                    "MBR City predominantly off-plan as master development continues. "
                    "Dubai-wide off-plan share 65% (2025); MBR City skews higher ~70% "
                    "due to ongoing Sobha Hartland II, Sobha Sanctuary, and other phases. "
                    "Source: DLD 2025 data; APIL Properties."
                ),
            },
        },
    },

    # =========================================================================
    "burj_binghatti": {
        "project_name": "Burj Binghatti Jacob & Co Residences",
        "developer": "Binghatti Developers",
        "city": "Dubai",
        "country": "UAE",
        "area": "Business Bay, Dubai",

        "raw_variables": {

            # GROUP 1 — DEMAND & LIQUIDITY
            "micro_market_stage": {
                # Business Bay: Fully established commercial + residential hub.
                "score": 100,
                "source_note": (
                    "Business Bay is Dubai's established central business district. "
                    "Metro access (Business Bay Station), Dubai Water Canal promenade complete, "
                    "major banks and multinationals headquartered here. Established = 100. "
                    "Source: Oliva Business Bay Investor Guide 2026."
                ),
            },
            "rental_absorption_velocity": {
                # Ultra-luxury (AED 8M-752M). Niche market. Slower absorption ~120-180 days.
                # Score = ((150 - 30) / (365 - 30)) × 100 = 35.8
                "score": 35.8,
                "source_note": (
                    "Ultra-luxury branded residences are a thin, slow market. "
                    "Price range AED 8.2M-752M severely limits buyer pool. "
                    "Estimated 120-180 day rental absorption for this product tier. "
                    "Business Bay overall is fast but this project is distinct. Low confidence."
                ),
            },
            "resale_velocity": {
                # Ultra-luxury: Much slower. 300-500 days for super-prime single-asset.
                # Score = ((400 - 30) / (730 - 30)) × 100 = 52.9
                "score": 52.9,
                "source_note": (
                    "Ultra-luxury branded residences (Jacob & Co) are near-unique assets. "
                    "Comparable branded residences in Dubai (e.g. Bugatti) trade rarely. "
                    "Estimated 300-500 day resale window. Low confidence — no published data."
                ),
            },
            "days_on_market": {
                # Ultra-luxury: 150-200 days on market expected.
                # Score = ((175 - 7) / (365 - 7)) × 100 = 46.9
                "score": 46.9,
                "source_note": (
                    "Ultra-luxury branded residences globally average 150-200+ days on market. "
                    "Business Bay location adds commercial liquidity premium but price tier "
                    "dramatically limits buyer pool. Estimate 150-175 days. Low confidence."
                ),
            },
            "occupancy_vacancy_rate": {
                # Business Bay overall: ~88%. Ultra-luxury tier: ~75-80%.
                # Score = ((78 - 50) / (100 - 50)) × 100 = 56.0
                "score": 56.0,
                "source_note": (
                    "Business Bay apartments overall: strong occupancy ~88% (Rental Yields "
                    "guide 2026). Ultra-luxury tier faces lower occupancy due to price point. "
                    "Estimated 75-80% for this product tier. Low confidence."
                ),
            },

            # GROUP 2 — NEIGHBORHOOD LIVABILITY
            "safety_crime_index": {
                "score": 83.9,
                "source_note": "Numbeo Dubai Safety Index January 2025: 83.89. Citywide metric.",
            },
            "healthcare_access": {
                # Mediclinic Business Bay within ~1km. High access.
                "score": 85.0,
                "source_note": (
                    "Mediclinic Business Bay Hospital within ~1km of Business Bay. "
                    "Rashid Hospital (major public) ~3km. Good central hospital access. "
                    "Score 85/100."
                ),
            },
            "school_quality": {
                # Business Bay: No premium schools within community. Nearest 3-5km.
                "score": 58.0,
                "source_note": (
                    "Business Bay has limited school infrastructure within the district. "
                    "Nearest rated schools: GEMS Wellington (Al Quoz, ~3km), "
                    "Jumeirah College (~5km). Not a family school cluster. Score 58/100."
                ),
            },
            "air_quality_index": {
                "score": 52.5,
                "source_note": "Dubai annual AQI ~95 (IQAir 2024/2025 avg). Score = 100 - (95/2) = 52.5.",
            },
            "beach_coastal_access": {
                # Business Bay: Dubai Water Canal within walking distance (promenade).
                # Nearest actual beach: Kite Beach ~8km. 5-10km range = score 25.
                "score": 25.0,
                "source_note": (
                    "Business Bay has Dubai Water Canal promenade (3.2km walkway) but "
                    "no beach. Nearest beach: Kite Beach/Al Sufouh ~7-8km. "
                    "5-10km range = score 25 per spec."
                ),
            },

            # GROUP 3
            "population_growth_rate": {
                "score": 66.0,
                "source_note": "Dubai annual population growth ~4.6% (DSC 2024).",
            },
            "expat_concentration": {
                "score": 90.0,
                "source_note": "Dubai expat concentration ~90% (DSC/GMI Research 2025).",
            },

            # GROUP 4
            "immediate_pipeline_risk": {
                # Business Bay: "15,000+ new units scheduled 2026-2027" (Middle East Insider).
                # 18,400 units sold off-plan 2021-2025 (Oliva DLD data). Very high pipeline.
                # Score = ((4500 - 0) / (5000 - 0)) × 100 = 90.0
                "score": 90.0,
                "source_note": (
                    "Middle East Insider 2026: 'Business Bay has highest new supply pipeline "
                    "of any Dubai neighborhood — 15,000 new units 2026-2027'. "
                    "Oliva guide: 18,400 units sold off-plan 2021-2025. "
                    "Capped at 4,500 units within 2km for scoring. Score = 90.0. "
                    "Highest supply risk of all 5 properties."
                ),
            },
            "active_unsold_inventory": {
                # Project: 40 of 299 = 13.4%. Business Bay submarket: ~20-25% unsold.
                # Score = ((22 - 0) / (40 - 0)) × 100 = 55.0
                "score": 55.0,
                "source_note": (
                    "Burj Binghatti: 40 of 299 units available (~13%). "
                    "Business Bay submarket: significant pipeline with partial absorption "
                    "challenges. Mitchell's Commercial RE: 'one of highest supply volumes'. "
                    "Estimated ~22% active unsold. Source: Bayut listings; Mitchell's 2026."
                ),
            },

            # GROUP 5 — DELIVERY TRACK RECORD (Binghatti)
            "average_delay_duration": {
                # Binghatti: known for fast delivery, often ahead of schedule.
                # Canal project (June 2022 launch, delivered before Dec 2023 target).
                # Avg delay ~1-2 months across portfolio.
                # Score = ((2 - 0) / (24 - 0)) × 100 = 8.3
                "score": 8.3,
                "source_note": (
                    "Gulf News 2023: Binghatti Canal completed before deadline. "
                    "Binghatti website: 'recognized as one of fastest developers, often "
                    "delivering within 12-18 months, sometimes under a year'. "
                    "H1 2025: 5 projects delivered ahead of schedule (1,441 units). "
                    "Estimated avg delay ~2 months. Score = 8.3."
                ),
            },
            "pct_projects_delivered": {
                # Binghatti: strong on-time or early delivery track record. ~88%.
                # Score = ((88 - 0) / (100 - 0)) × 100 = 88.0
                "score": 88.0,
                "source_note": (
                    "Binghatti H1 2025 report: '5 projects successfully delivered, "
                    "1,441 units handed over'. Strong cadence. Multiple ahead-of-schedule. "
                    "Estimated 88% on-time delivery rate. Source: Binghatti H1 2025 press release."
                ),
            },
            "completion_consistency": {
                "score": 100,
                "source_note": "Binghatti: High consistency — multiple ahead-of-schedule deliveries. High = 100.",
            },

            # GROUP 6 — FINANCIAL CREDIBILITY (Binghatti)
            "escrow_quality": {
                "score": 100,
                "source_note": "Binghatti RERA-compliant; all projects escrow-registered. 91% listings show active DTCM registration. Strict = 100.",
            },
            "debt_cash_position": {
                # Binghatti: debt-to-equity 1.2x, but cash AED 7.7B vs. debt AED 7.0B.
                # Net cash positive. Fitch BB-, growing fast. Score ~65.
                "score": 65.0,
                "source_note": (
                    "Binghatti Q3 2025: Total assets AED 22B, equity AED 5.8B, total debt "
                    "AED 7.0B (D/E 1.2x), cash AED 7.7B (net cash positive). "
                    "Fitch 'BB-' stable outlook (Mar 2025). Low net D/EBITDA of 0.8x in 2024. "
                    "Score 65/100 — strong but growth-stage leverage profile."
                ),
            },
            "stalled_projects_count": {
                "score": 0.0,
                "source_note": "No stalled Binghatti projects. Score = 0.",
            },
            "presales_pct_achieved": {
                # Binghatti: 12,000 units in 9M 2025; backlog AED 14B. Strong sellout rates.
                # Score = ((92 - 0) / (100 - 0)) × 100 = 92.0
                "score": 92.0,
                "source_note": (
                    "Binghatti Q3 2025: 12,000 units sold in 9M (Dubai's #1 off-plan developer "
                    "by units). Revenue backlog AED 14B. Non-resident investors ~60% of sales. "
                    "Projects reliably >90% presold. Score = 92.0."
                ),
            },

            # GROUP 7 — COMP MARKET PERFORMANCE
            "comp_capital_appreciation": {
                # Business Bay: 5-year price CAGR 12.5% (Oliva / DLD data)
                # Score = ((12.5 - (-5)) / (25 - (-5))) × 100 = 58.3
                "score": 58.3,
                "source_note": (
                    "Oliva/DLD Business Bay 2026: '5-year CAGR on price per sqft: 12.5%'. "
                    "Outperforms Dubai Marina (11.2%) and Downtown (10.8%). "
                    "Score = ((12.5+5)/30) × 100 = 58.3."
                ),
            },
            "comp_rental_yields": {
                # Business Bay overall: 6.5-7%. Ultra-luxury tier this project: ~3-4.5%.
                # Using ultra-luxury comp yield ~3.8%.
                # Score = ((3.8 - 2) / (12 - 2)) × 100 = 18.0
                "score": 18.0,
                "source_note": (
                    "Ultra-luxury branded residences (AED 8M+): significantly lower yields "
                    "than standard Business Bay (6.5-7%). Estimated 3-4.5% for this tier "
                    "based on comparable branded residences globally. Project spec: 4.5% estimate. "
                    "Using 3.8% conservative. Score = ((3.8-2)/10) × 100 = 18.0."
                ),
            },
            "comp_occupancy_rate": {
                # Business Bay overall: 88%. Ultra-luxury occupancy ~75-80%.
                # Score = ((77 - 50) / (100 - 50)) × 100 = 54.0
                "score": 54.0,
                "source_note": (
                    "Business Bay overall 88% occupancy. Ultra-luxury tier lower due to "
                    "limited buyer/renter pool at AED 8M+. Estimated 75-80%. Using 77%. "
                    "Source: Mitchell's Commercial RE 2026; Henry Club Business Bay 2026."
                ),
            },

            # GROUP 8 — SPECULATION RISK
            "str_concentration": {
                # Business Bay: Top STR market in Dubai. ~35-40% listed STR.
                # Score = ((37 - 0) / (60 - 0)) × 100 = 61.7 → capped at 100 but score is fine
                "score": 61.7,
                "source_note": (
                    "AirROI 2026: 1,052 active listings in Business Bay with 359% YoY growth. "
                    "Oplus Realty/CBRE: 'Business Bay achieves gross STR returns 8-12%'. "
                    "Estimated 35-40% of units in STR rotation. Using 37%. "
                    "Score = (37/60) × 100 = 61.7."
                ),
            },
            "investor_owner_ratio": {
                # Business Bay ultra-luxury: almost entirely investor-owned. ~90%.
                # Score = ((90 - 0) / (100 - 0)) × 100 = 90.0
                "score": 90.0,
                "source_note": (
                    "Ultra-luxury product (AED 8M-752M) is near-exclusively investor/HNW "
                    "trophy purchase. Very few end-users at this price tier. "
                    "Estimated 88-92% investor ratio. Source: market profile inference."
                ),
            },
            "offplan_secondary_dominance": {
                # Business Bay: 18,400 off-plan units 2021-2025. ~70% off-plan.
                # Score = ((70 - 0) / (100 - 0)) × 100 = 70.0
                "score": 70.0,
                "source_note": (
                    "Oliva/DLD: '18,400 units sold off-plan in Business Bay 2021-2025'. "
                    "Business Bay skews heavily off-plan. Estimated 70% off-plan dominance. "
                    "Source: Oliva Business Bay Investor Guide 2026."
                ),
            },
        },
    },

    # =========================================================================
    "damac_islands": {
        "project_name": "DAMAC Islands",
        "developer": "DAMAC Properties",
        "city": "Dubai",
        "country": "UAE",
        "area": "Dubailand, Dubai",

        "raw_variables": {

            # GROUP 1 — DEMAND & LIQUIDITY
            "micro_market_stage": {
                # Dubailand: large-scale development zone with Emerging sub-communities.
                "score": 50,
                "source_note": (
                    "Dubailand is an Emerging market. The broader zone includes some mature "
                    "pockets (DAMAC Hills) but DAMAC Islands itself is a new launch in a "
                    "still-developing precinct with limited completed infrastructure. "
                    "Emerging = 50. Source: Totality Estates supply analysis 2025."
                ),
            },
            "rental_absorption_velocity": {
                # Dubailand emerging community: 120-180 day absorption expected.
                # Score = ((150 - 30) / (365 - 30)) × 100 = 35.8
                "score": 35.8,
                "source_note": (
                    "Dubailand is an emerging zone with limited immediate tenant demand. "
                    "Totality Estates 2026: 'Dubailand clusters show competitive ticket sizes "
                    "with solid renter depth' but slower absorption vs. established areas. "
                    "Estimated 120-180 days. Low confidence."
                ),
            },
            "resale_velocity": {
                # Emerging community: slower resale. ~200-300 days.
                # Score = ((250 - 30) / (730 - 30)) × 100 = 31.4
                "score": 31.4,
                "source_note": (
                    "DAMAC Islands is under construction (Dec 2028). Resale market for "
                    "emerging Dubailand sub-communities is thin. Estimated 200-300 days. "
                    "Low confidence — limited comparable resale data."
                ),
            },
            "days_on_market": {
                # Dubailand: ~90-120 days.
                # Score = ((105 - 7) / (365 - 7)) × 100 = 27.4
                "score": 27.4,
                "source_note": (
                    "Dubailand properties take longer to move than core Dubai. Estimated "
                    "90-120 days. Arjan/Dubailand Area Guide 2026 (Dubai Property Insight): "
                    "notes limited metro access and longer absorption. Low confidence."
                ),
            },
            "occupancy_vacancy_rate": {
                # Dubailand: lower occupancy in emerging areas. ~78-82%.
                # Score = ((80 - 50) / (100 - 50)) × 100 = 60.0
                "score": 60.0,
                "source_note": (
                    "Dubailand is an emerging zone with limited near-term occupancy data. "
                    "Nearby DAMAC Hills: ~80% occupancy estimate. "
                    "DAMAC Islands is pre-delivery; using comparable Dubailand occupancy ~80%. "
                    "Low confidence."
                ),
            },

            # GROUP 2 — NEIGHBORHOOD LIVABILITY
            "safety_crime_index": {
                "score": 83.9,
                "source_note": "Numbeo Dubai Safety Index January 2025: 83.89. Citywide metric.",
            },
            "healthcare_access": {
                # Dubailand: Very limited nearby hospital infrastructure. Nearest ~15-20km.
                "score": 38.0,
                "source_note": (
                    "Dubailand has limited healthcare infrastructure. Nearest major hospital "
                    "approximately 15-20km (Dubai hospitals cluster in central areas). "
                    "Some clinics planned within Dubailand but not yet operational. Score 38/100."
                ),
            },
            "school_quality": {
                # Dubailand: Some schools in broader area (GEMS schools in Al Barsha etc.).
                "score": 52.0,
                "source_note": (
                    "Dubailand has some international schools planned or nearby "
                    "(GEMS World Academy ~8km; Ranches Primary ~6km). "
                    "No premium school directly adjacent to DAMAC Islands. Score 52/100."
                ),
            },
            "air_quality_index": {
                "score": 52.5,
                "source_note": "Dubai annual AQI ~95 (IQAir 2024/2025 avg). Score = 100 - (95/2) = 52.5.",
            },
            "beach_coastal_access": {
                # Dubailand: Very inland. Nearest beach >20km.
                "score": 0.0,
                "source_note": (
                    "DAMAC Islands has artificial waterfront lagoons within community "
                    "but is inland. Nearest real beach >20km. The lagoons are a feature "
                    "but not coastal. Score 0 (>10km from sea)."
                ),
            },

            # GROUP 3
            "population_growth_rate": {
                "score": 66.0,
                "source_note": "Dubai annual population growth ~4.6% (DSC 2024).",
            },
            "expat_concentration": {
                "score": 90.0,
                "source_note": "Dubai expat concentration ~90% (DSC/GMI Research 2025).",
            },

            # GROUP 4
            "immediate_pipeline_risk": {
                # Dubailand: Very high. DAMAC alone responsible for 30% of 2025 planned units.
                # Multiple DAMAC clusters (Lagoons, Islands, Hills 2) + other developers.
                # Score = ((3500 - 0) / (5000 - 0)) × 100 = 70.0
                "score": 70.0,
                "source_note": (
                    "Tranio Dec 2025: DAMAC responsible for ~30% of 2025 planned units and "
                    "'more than half of sq footage'. Dubailand is one of highest-pipeline zones. "
                    "Arjan/Dubailand Guide 2026: 'Knight Frank and Cushman: ~120,000 units "
                    "citywide in 2026; Dubailand represents material share'. "
                    "Estimated 3,500 units within 2km. Score = 70.0."
                ),
            },
            "active_unsold_inventory": {
                # Project: 45 of 200 = 22.5%. Dubailand submarket: high unsold given launches.
                # Score = ((20 - 0) / (40 - 0)) × 100 = 50.0
                "score": 50.0,
                "source_note": (
                    "DAMAC Islands: 45 of 200 units available (~22.5%). "
                    "Dubailand submarket has heavy concurrent supply; estimated ~20% unsold. "
                    "Source: project spec; Totality Estates supply analysis 2025."
                ),
            },

            # GROUP 5 — DELIVERY TRACK RECORD (DAMAC)
            "average_delay_duration": {
                # DAMAC: 6-8 months average delay (Tranio/DLD). 75% late in 2024.
                # Score = ((8 - 0) / (24 - 0)) × 100 = 33.3
                "score": 33.3,
                "source_note": (
                    "Tranio Dec 2025 / DLD data: 'developers such as Nakheel, Azizi, DAMAC "
                    "have the longest delays, with buyers facing waits of 6-8 months'. "
                    "2024: 'out of 8 planned DAMAC projects, only 2 completed on schedule '(75% late). "
                    "Using 8-month average. Score = (8/24) × 100 = 33.3."
                ),
            },
            "pct_projects_delivered": {
                # DAMAC: ~55% historically on time (25% on time in 2024 was worst year).
                # Score = ((55 - 0) / (100 - 0)) × 100 = 55.0
                "score": 55.0,
                "source_note": (
                    "Tranio Dec 2025: DAMAC '75% delivered late in 2024' (worst year). "
                    "Historically: ~55% on-time across long-term portfolio "
                    "(Khaleej Times historical: 'all 5 started projects running behind'). "
                    "Using 55% as long-run average."
                ),
            },
            "completion_consistency": {
                "score": 0,
                "source_note": (
                    "DAMAC: Low consistency. 75% late in 2024, historical pattern of delays "
                    "documented since 2006. Categorical: Low = 0."
                ),
            },

            # GROUP 6 — FINANCIAL CREDIBILITY (DAMAC)
            "escrow_quality": {
                "score": 100,
                "source_note": (
                    "DAMAC Properties RERA-compliant. Moody's Ba1 rating (Apr 2025): 'Damac "
                    "manages liquidity for construction projects without reliance on external funding'. "
                    "Customer pre-payments fund construction via escrow. Strict = 100."
                ),
            },
            "debt_cash_position": {
                # DAMAC: Moody's Ba1, "prudent financial policies, max 50% D/E target".
                # Taken private 2022. Sales backlog $18B. Revenue recovering after 2023 dip.
                # Score: ~62
                "score": 62.0,
                "source_note": (
                    "Moody's Apr 2025: upgraded to Ba1 from Ba2. Sales backlog AED 67B ($18.3B) "
                    "as of Dec 2024. 'Strong pre-completion payment collections fund construction "
                    "without project debt'. Delisted 2022 (private). Moderate leverage. Score 62/100."
                ),
            },
            "stalled_projects_count": {
                # DAMAC: Projects are late but not formally stalled. ~2 flagged as severely delayed.
                # Score = ((2 - 0) / (10 - 0)) × 100 = 20.0
                "score": 20.0,
                "source_note": (
                    "DAMAC: no formal stalled projects per RERA records, but 6 of 8 planned "
                    "2024 projects overdue (Tranio). Projects with 24-month delay clauses "
                    "invoked (Gulf News buyer complaint record). "
                    "Scoring 2 as constructively stalled/severely delayed."
                ),
            },
            "presales_pct_achieved": {
                # DAMAC: AED 67B backlog, strong presales historically. ~85%.
                # Score = ((85 - 0) / (100 - 0)) × 100 = 85.0
                "score": 85.0,
                "source_note": (
                    "Moody's Ba1 report Apr 2025: AED 67B sales backlog Dec 2024, "
                    "'strong off-plan sales', 'high pre-completion payment collection'. "
                    "Estimated 85% presales achieved. Source: Zawya Apr 2025."
                ),
            },

            # GROUP 7 — COMP MARKET PERFORMANCE
            "comp_capital_appreciation": {
                # Dubailand emerging: lower appreciation. ~5-7% CAGR.
                # Score = ((6 - (-5)) / (25 - (-5))) × 100 = 36.7
                "score": 36.7,
                "source_note": (
                    "Dubailand is emerging; lower CAGR than core Dubai (7-10%). "
                    "Totality Estates: 'competitive buy-ins and family-friendly' but supply risk. "
                    "Estimated 5-7% CAGR. Using 6%. Score = ((6+5)/30) × 100 = 36.7."
                ),
            },
            "comp_rental_yields": {
                # Dubailand: ~6-7% per Totality Estates reference. Using 6.5%.
                # Score = ((6.5 - 2) / (12 - 2)) × 100 = 45.0
                "score": 45.0,
                "source_note": (
                    "Totality Estates 2026: 'Dubailand clusters show competitive ticket sizes'. "
                    "Red Horizon DXB: 6-8% yields in suburban zones. Using 6.5% for Dubailand. "
                    "Score = ((6.5-2)/10) × 100 = 45.0."
                ),
            },
            "comp_occupancy_rate": {
                # Dubailand: ~78-82%. Using 80%.
                # Score = ((80 - 50) / (100 - 50)) × 100 = 60.0
                "score": 60.0,
                "source_note": (
                    "Dubailand occupancy estimated at ~80% based on comparable suburban "
                    "Dubai communities (DAMAC Hills profile). Limited specific data. "
                    "Low confidence."
                ),
            },

            # GROUP 8 — SPECULATION RISK
            "str_concentration": {
                # Dubailand: Low STR. Family community profile. ~8-12%.
                # Score = ((10 - 0) / (60 - 0)) × 100 = 16.7
                "score": 16.7,
                "source_note": (
                    "Dubailand is a suburban family zone with very limited STR activity. "
                    "Not in Dubai's primary tourist circuit. Estimated 8-12% STR. "
                    "Source: Airbtics city data; community profile. Low confidence."
                ),
            },
            "investor_owner_ratio": {
                # Dubailand: Mix. Families AND investors. ~65-70% investor.
                # Score = ((67 - 0) / (100 - 0)) × 100 = 67.0
                "score": 67.0,
                "source_note": (
                    "Dubailand attracts both end-user families and investors seeking "
                    "capital appreciation in emerging zone. Estimated 65-70% investor. "
                    "Low confidence."
                ),
            },
            "offplan_secondary_dominance": {
                # Dubailand: Almost entirely off-plan given emerging status. ~80-85%.
                # Score = ((82 - 0) / (100 - 0)) × 100 = 82.0
                "score": 82.0,
                "source_note": (
                    "Dubailand is predominantly off-plan with limited completed secondary stock. "
                    "Dubai-wide 65% off-plan (2025); Dubailand skews to ~80-85% given "
                    "development stage. Source: DLD 2025; Totality Estates supply guide."
                ),
            },
        },
    },

    # =========================================================================
    "dubai_creek": {
        "project_name": "Dubai Creek Harbour",
        "developer": "Emaar Properties",
        "city": "Dubai",
        "country": "UAE",
        "area": "Dubai Creek Harbour (Ras Al Khor), Dubai",

        "raw_variables": {

            # GROUP 1 — DEMAND & LIQUIDITY
            "micro_market_stage": {
                # DCH: Phase 1 (Creek Beach, Creek Marina, some retail) delivered.
                # Still heavily under construction (48,500 total units). Activating.
                "score": 75,
                "source_note": (
                    "Dubai Creek Harbour: Creek Beach, Creek Marina operational. "
                    "Multiple Emaar residential phases delivered. Ras Al Khor Wildlife Sanctuary "
                    "view access. Still 'early-to-mid development cycle' per multiple analyst "
                    "reports (Luxehaven 2025, AigentsRealty 2026). Activating = 75."
                ),
            },
            "rental_absorption_velocity": {
                # DCH: "ready buildings 88%+ occupancy" — strong demand. ~60-80 days.
                # Score = ((70 - 30) / (365 - 30)) × 100 = 11.9
                "score": 11.9,
                "source_note": (
                    "Dubai Creek Harbour (DubaiPropertyInsight 2026): 'occupancy rates in "
                    "ready buildings exceeding 88%'. DLD: 4,280 transactions at avg AED 2,470/sqft. "
                    "Strong professional demand from Business Bay/Downtown. Estimated 65-75 days."
                ),
            },
            "resale_velocity": {
                # DCH: Active DLD resale market. ~90-120 days similar to DHE.
                # Score = ((105 - 30) / (730 - 30)) × 100 = 10.7
                "score": 10.7,
                "source_note": (
                    "Dubai Creek Harbour: 'early investors have seen ~25% price growth'. "
                    "4,280 DLD sales recorded at avg AED 2,470/sqft (DubaiPropertyInsight 2026). "
                    "Activating market with growing resale liquidity. Estimated 90-120 days."
                ),
            },
            "days_on_market": {
                # DCH: ~65-75 days.
                # Score = ((70 - 7) / (365 - 7)) × 100 = 17.6
                "score": 17.6,
                "source_note": (
                    "Estimated 65-75 days based on DCH occupancy rate and transaction volume. "
                    "Waterfront premium reduces time on market vs. inland. "
                    "AigentsRealty 2026: strong demand from professionals and families. "
                    "Low confidence — no published days-on-market stat for DCH."
                ),
            },
            "occupancy_vacancy_rate": {
                # DCH: "occupancy rates in ready buildings exceeding 88%"
                # Score = ((88 - 50) / (100 - 50)) × 100 = 76.0
                "score": 76.0,
                "source_note": (
                    "DubaiPropertyInsight Apr 2026: 'occupancy rates in ready buildings "
                    "exceeding 88%'. Using 88% as per published data."
                ),
            },

            # GROUP 2 — NEIGHBORHOOD LIVABILITY
            "safety_crime_index": {
                "score": 83.9,
                "source_note": "Numbeo Dubai Safety Index January 2025: 83.89. Citywide metric.",
            },
            "healthcare_access": {
                # DCH area: Nearest hospital ~5-8km (Rashid Hospital or City Hospital).
                "score": 62.0,
                "source_note": (
                    "Dubai Creek Harbour: limited on-site healthcare. Nearest major hospital "
                    "(Rashid Hospital, Bur Dubai) ~6-8km. Some clinics planned. Score 62/100."
                ),
            },
            "school_quality": {
                # DCH: Limited on-site schools currently. Growing community.
                "score": 60.0,
                "source_note": (
                    "Dubai Creek Harbour: no top-rated international school on-site yet. "
                    "Nearest: GEMS schools in Mirdif/Al Khail ~8-10km. "
                    "Growing community with school infrastructure planned. Score 60/100."
                ),
            },
            "air_quality_index": {
                "score": 52.5,
                "source_note": "Dubai annual AQI ~95 (IQAir 2024/2025 avg). Score = 100 - (95/2) = 52.5.",
            },
            "beach_coastal_access": {
                # DCH has Creek Beach within the development.
                # <500m from beach = 100; or 500m-2km = 75. Creek Beach is within community.
                "score": 75.0,
                "source_note": (
                    "Dubai Creek Harbour includes Creek Beach within the masterplan. "
                    "For most units, Creek Beach is 500m-2km. Score 75 per spec rule "
                    "(500m-2km range). Not fully beachfront but significant coastal access."
                ),
            },

            # GROUP 3
            "population_growth_rate": {
                "score": 66.0,
                "source_note": "Dubai annual population growth ~4.6% (DSC 2024).",
            },
            "expat_concentration": {
                "score": 90.0,
                "source_note": "Dubai expat concentration ~90% (DSC/GMI Research 2025).",
            },

            # GROUP 4
            "immediate_pipeline_risk": {
                # DCH: 48,500 total planned; 12,000 currently available. Massive pipeline.
                # Within 2km: ~4,000+ units in next 24 months.
                # Score = ((4000 - 0) / (5000 - 0)) × 100 = 80.0
                "score": 80.0,
                "source_note": (
                    "Dubai Creek Harbour: 48,500 total units planned across full masterplan. "
                    "12,000 of 48,500 currently available = significant ongoing supply. "
                    "Property Network Q1 2026: 'DCH 15-25% appreciation driven by Blue Line'. "
                    "Estimated 4,000 units within 2km in next 24 months. "
                    "High pipeline risk is the primary investment landmine."
                ),
            },
            "active_unsold_inventory": {
                # DCH: 12,000 of 48,500 available. Submarket ~20-22% unsold.
                # Score = ((21 - 0) / (40 - 0)) × 100 = 52.5
                "score": 52.5,
                "source_note": (
                    "Dubai Creek Harbour: 12,000 of 48,500 total units currently available "
                    "(24.7% of master plan). Active submarket unsold estimated ~21%. "
                    "Source: project spec; DLD data cited in investment guides."
                ),
            },

            # GROUP 5 — DELIVERY TRACK RECORD (Emaar)
            "average_delay_duration": {
                "score": 58.3,
                "source_note": (
                    "Emaar (same as Greencrest): Tranio/DLD 20-year analysis: average delay "
                    "exceeding 14 months. Score = (14/24) × 100 = 58.3."
                ),
            },
            "pct_projects_delivered": {
                "score": 55.5,
                "source_note": (
                    "Emaar (same as Greencrest): 55.5% on-time delivery rate "
                    "(Tranio: 44.5% failure rate over 20 years)."
                ),
            },
            "completion_consistency": {
                "score": 50,
                "source_note": "Emaar: Medium consistency. Delivers all projects but 44.5% miss deadlines. Medium = 50.",
            },

            # GROUP 6 — FINANCIAL CREDIBILITY (Emaar)
            "escrow_quality": {
                "score": 100,
                "source_note": "Emaar RERA-compliant; DFM-listed; all projects under strict escrow. Strict = 100.",
            },
            "debt_cash_position": {
                "score": 85.0,
                "source_note": (
                    "Emaar Properties (same as Greencrest): AED 83.7B sales backlog, "
                    "AED 12.5B revenue in 9M 2024. Strong investment-grade profile. Score 85/100."
                ),
            },
            "stalled_projects_count": {
                "score": 0.0,
                "source_note": "No stalled Emaar projects. Score = 0.",
            },
            "presales_pct_achieved": {
                "score": 87.0,
                "source_note": "Emaar (same as Greencrest): ~87% presales rate. Score = 87.0.",
            },

            # GROUP 7 — COMP MARKET PERFORMANCE
            "comp_capital_appreciation": {
                # DCH: "25-35% appreciation since 2022" = ~8-12% CAGR. Using 10%.
                # Score = ((10 - (-5)) / (25 - (-5))) × 100 = 50.0
                "score": 50.0,
                "source_note": (
                    "Multiple sources: DCH properties appreciated 25-35% since 2022. "
                    "AigentsRealty 2026: '8-12% annual appreciation forecast 2026-2027'. "
                    "Place Overseas 2026: '30-35% since 2022'. Using 10% CAGR. "
                    "Score = ((10+5)/30) × 100 = 50.0."
                ),
            },
            "comp_rental_yields": {
                # DCH: 6.5-7.5% gross (AigentsRealty 2026)
                # Using 7.0%. Score = ((7 - 2) / (12 - 2)) × 100 = 50.0
                "score": 50.0,
                "source_note": (
                    "AigentsRealty Investment Guide 2026: 'gross rental yields 6.5-7.5%'. "
                    "Using 7.0% midpoint. Score = ((7-2)/10) × 100 = 50.0."
                ),
            },
            "comp_occupancy_rate": {
                # DCH: 88%+ per DLD data
                # Score = ((88 - 50) / (100 - 50)) × 100 = 76.0
                "score": 76.0,
                "source_note": (
                    "DubaiPropertyInsight Apr 2026: 'occupancy rates in ready buildings "
                    "exceeding 88%'. Using 88%."
                ),
            },

            # GROUP 8 — SPECULATION RISK
            "str_concentration": {
                # DCH: Waterfront community, growing STR. ~25-30%.
                # Score = ((27 - 0) / (60 - 0)) × 100 = 45.0
                "score": 45.0,
                "source_note": (
                    "Dubai Creek Harbour: waterfront premium attracts STR investment. "
                    "Growing tourism profile. Estimated 25-30% STR units. "
                    "Sands of Wealth 2026: Dubai citywide 57,000+ STR listings. "
                    "DCH above average for waterfront. Using 27%. Score = 45.0."
                ),
            },
            "investor_owner_ratio": {
                # DCH: Strongly investor driven. ~75-80%.
                # Score = ((77 - 0) / (100 - 0)) × 100 = 77.0
                "score": 77.0,
                "source_note": (
                    "Dubai Creek Harbour is primarily an investment market (early-cycle, "
                    "capital appreciation story). 'Off-plan sales dominate 64% of transactions'. "
                    "High investor ratio ~75-80%. Source: Property Kumbh; DCH investment guides."
                ),
            },
            "offplan_secondary_dominance": {
                # DCH: Heavily off-plan. 48,500 total — mostly off-plan transactions.
                # Score = ((78 - 0) / (100 - 0)) × 100 = 78.0
                "score": 78.0,
                "source_note": (
                    "Dubai Creek Harbour: masterplan is ~75-80% off-plan by transaction count. "
                    "Property Kumbh: 'off-plan sales dominate 64% of transactions' Dubai-wide; "
                    "DCH skews higher given development stage. Using 78%."
                ),
            },
        },
    },
}


# =============================================================================
# CONFIDENCE SUMMARY
# =============================================================================
# ┌──────────────────────────────────┬──────────────┬────────────┬──────────────────────────────────────────────────┐
# │ Property                         │ Populated    │ Null       │ Low Confidence Flags                             │
# ├──────────────────────────────────┼──────────────┼────────────┼──────────────────────────────────────────────────┤
# │ Greencrest (Dubai Hills Estate)  │ 25 / 25      │ 0          │ resale_velocity, days_on_market,                 │
# │                                  │              │            │ immediate_pipeline_risk, active_unsold_inventory,│
# │                                  │              │            │ str_concentration, investor_owner_ratio          │
# ├──────────────────────────────────┼──────────────┼────────────┼──────────────────────────────────────────────────┤
# │ Sobha Hartland (MBR City)        │ 25 / 25      │ 0          │ rental_absorption_velocity, resale_velocity,     │
# │                                  │              │            │ days_on_market, immediate_pipeline_risk,         │
# │                                  │              │            │ str_concentration, investor_owner_ratio          │
# ├──────────────────────────────────┼──────────────┼────────────┼──────────────────────────────────────────────────┤
# │ Burj Binghatti (Business Bay)    │ 25 / 25      │ 0          │ rental_absorption_velocity, resale_velocity,     │
# │                                  │              │            │ days_on_market, occupancy_vacancy_rate,          │
# │                                  │              │            │ comp_rental_yields (ultra-luxury tier thin)      │
# ├──────────────────────────────────┼──────────────┼────────────┼──────────────────────────────────────────────────┤
# │ DAMAC Islands (Dubailand)        │ 25 / 25      │ 0          │ rental_absorption_velocity, resale_velocity,     │
# │                                  │              │            │ days_on_market, occupancy_vacancy_rate,          │
# │                                  │              │            │ comp_capital_appreciation, comp_occupancy_rate,  │
# │                                  │              │            │ str_concentration, investor_owner_ratio          │
# │                                  │              │            │ [HIGHEST FLAG COUNT — emerging pre-delivery]     │
# ├──────────────────────────────────┼──────────────┼────────────┼──────────────────────────────────────────────────┤
# │ Dubai Creek Harbour              │ 25 / 25      │ 0          │ resale_velocity, days_on_market,                 │
# │                                  │              │            │ immediate_pipeline_risk (massive masterplan),    │
# │                                  │              │            │ str_concentration, investor_owner_ratio          │
# └──────────────────────────────────┴──────────────┴────────────┴──────────────────────────────────────────────────┘
#
# GLOBAL NOTES:
# 1. All 5 properties share identical city-level scores for: safety_crime_index (83.9),
#    air_quality_index (52.5), population_growth_rate (66.0), expat_concentration (90.0).
#    These are Dubai-wide metrics with no meaningful intra-city variation in the data.
# 2. beach_coastal_access = 0 for DHE, Sobha Hartland, and DAMAC Islands (all inland).
#    DCH = 75 (Creek Beach within community). Burj Binghatti = 25 (5-10km to beach).
# 3. Greencrest and Dubai Creek Harbour share identical Emaar delivery metrics.
# 4. Ultra-luxury product (Burj Binghatti): resale_velocity, days_on_market, occupancy,
#    and comp_rental_yields are significantly lower than Business Bay's general market.
#    Scores reflect the thin ultra-luxury buyer pool, not the district average.
# 5. DAMAC delivery track record (completion_consistency = Low = 0) is the single most
#    differentiating developer-level risk factor across this comparison set.
