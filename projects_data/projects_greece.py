# ─── GREECE PROPERTIES — RAW VARIABLE SCORES ──────────────────────────────────
# Generated: 2026-05-26
# Scoring engine: magnitude-only (0–100). Engine handles inversion.
# All continuous scores use: Score = ((Value - Min) / (Max - Min)) × 100
# Time-based absorption/velocity variables invert at definition level
#   (lower days = faster = higher magnitude), per spec annotation.
# Null = no reliable data found after exhaustive search.
# ──────────────────────────────────────────────────────────────────────────────

projects_data = {

    # ══════════════════════════════════════════════════════════════════════════
    # PROPERTY 1 — LUX&EASY THESSALONIKI
    # Developer: NOVA CONSTRUCTIONS S.A.
    # Location: Thessaloniki Metropolitan Area, Greece
    # Stage: Under Construction → March 2027
    # Price: €120K–€240K | 2,300 units | 2,141 currently available (~159 sold)
    # ══════════════════════════════════════════════════════════════════════════
    "luxeasy_thessaloniki": {
        "project_name": "LUX&EASY Thessaloniki",
        "developer": "NOVA CONSTRUCTIONS S.A.",
        "city": "Thessaloniki",
        "country": "Greece",
        "area": "Thessaloniki Metropolitan Area",
        "raw_variables": {

            # ── GROUP 1: DEMAND & LIQUIDITY ───────────────────────────────────

            "micro_market_stage": {
                "score": 75,
                "source_note": "Thessaloniki is 'Activating': prices up 12.1% YoY (Q3 2024, Rethinking The Future), properties selling in 45–60 days in central districts, growing foreign investor activity but not yet mature Established market. Strong momentum but structural vacancy historically present. (Investropa June 2025, The Luxury Playbook July 2025)"
            },

            "rental_absorption_velocity": {
                # Value ≈ 60 days (central Thessaloniki). Formula (inverse): ((Max - Value) / (Max - Min)) × 100
                # = ((365 - 60) / (365 - 30)) × 100 = 305/335 × 100 = 91.0
                "score": 91.0,
                "source_note": "Central Thessaloniki properties absorbing in 45–60 days rental market per The Luxury Playbook (July 2025). Used 60 days for metro-wide blended estimate given project spread across entire metropolitan area."
            },

            "resale_velocity": {
                # Value ≈ 90 days. ((730 - 90) / (730 - 30)) × 100 = 640/700 × 100 = 91.4
                "score": 91.4,
                "source_note": "Thessaloniki central market selling in ~45–60 days (The Luxury Playbook 2025). Used conservative 90-day estimate for a metro-wide new-build development to account for non-prime unit locations. LUX&EASY is spread across the full metropolitan area."
            },

            "days_on_market": {
                # Value ≈ 60 days. ((365 - 60) / (365 - 7)) × 100 = 305/358 × 100 = 85.2
                "score": 85.2,
                "source_note": "Thessaloniki residential listings absorbing in 45–60 days in active 2025 market per The Luxury Playbook (July 2025) and Ellas Estate (Aug 2025). Used 60-day midpoint."
            },

            "occupancy_vacancy_rate": {
                # STR occupancy 62% (Airbtics 2024/25), long-term vacancy very low (constrained supply).
                # Blended estimate: ~80%. ((80 - 50) / (100 - 50)) × 100 = 30/50 × 100 = 60.0
                "score": 60.0,
                "source_note": "STR (Airbnb) occupancy 62% per Airbtics (Sep 2024–Aug 2025, 2,921 listings). Long-term rental vacancy very low given constrained supply and student/professional demand (Investropa June 2025). Blended 80% occupancy estimate."
            },

            # ── GROUP 2: NEIGHBORHOOD LIVABILITY ─────────────────────────────

            "safety_crime_index": {
                # Numbeo Safety Index Thessaloniki = 48.06. Score = as-is per spec ("score AS-IS, not inverted").
                "score": 48.06,
                "source_note": "Numbeo Crime/Safety Comparison Tool (current data, cross-confirmed via Greek Reporter Oct 2025 and Greek Herald Oct 2025): Thessaloniki Safety Index = 48.06, Crime Index = 51.94. 'Moderate Crime' bracket. Variable spec says use safety scale as-is."
            },

            "healthcare_access": {
                # Major teaching hospitals present (AHEPA University Hospital, Papageorgiou General Hospital).
                # Metro-wide location means distances vary 0.5–5km. Score ~70.
                "score": 70,
                "source_note": "Thessaloniki has AHEPA University Hospital (top-tier teaching hospital), Papageorgiou General Hospital, and Ippokrateio General Hospital. Metro-wide development means unit proximity varies; central units within 1–2km of major facilities. Scored 70/100 for good city-level access without guarantee of proximity for all 2,300 units."
            },

            "school_quality": {
                # Thessaloniki has Anatolia College (one of Greece's top private schools), Aristotle University area.
                # International school quality not at Athens level. Score ~58.
                "score": 58,
                "source_note": "Thessaloniki has Anatolia College (IB programme, established private school) and several private Greek schools. Aristotle University of Thessaloniki creates educational ecosystem. No major international school rated comparably to Athens Campion/ACS. Scored 58/100 reflecting solid but not premium international schooling."
            },

            "air_quality_index": {
                # Thessaloniki annual PM2.5 ≈ 18.8 μg/m³ (IQAir Greece page). Converting to 100=cleanest:
                # Score = ((50 - 18.8) / 50) × 100 = 31.2/50 × 100 = 62.4
                "score": 62.4,
                "source_note": "IQAir Greece page: Thessaloniki annual average PM2.5 = 18.8 μg/m³ (2019 benchmark data, corroborated by 'Moderate' AQI classification in 2021 at US AQI 65). Winter heating season drives peak levels. Conversion formula: ((50 - PM2.5) / 50) × 100. Score = 62.4 (moderate air quality, worse than coastal Athens)."
            },

            "beach_coastal_access": {
                # Thessaloniki sits on the Thermaic Gulf with a famous seafront promenade (Nea Paralia).
                # Central urban units: ~500m–2km from seafront. Metro-wide spread means some units farther.
                # Using 75 for majority of centrally-located units (500m–2km bracket = 75 per spec).
                "score": 75,
                "source_note": "Thessaloniki's Nea Paralia (New Waterfront) is a major seafront promenade stretching 3.5km along the Thermaic Gulf. Central urban units within 500m–2km of the waterfront (score 75 per spec bracket). Outer metro-area units could be 5–10km from coast, but LUX&EASY markets central/semi-central locations. Assigned 75 reflecting primary project positioning."
            },

            # ── GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ─────────────────────

            "population_growth_rate": {
                # Thessaloniki metro 2024: 815,000 — flat (0% vs 2023). 2023: 0.12% increase.
                # Value ≈ 0.12%. ((0.12 - (-2)) / (8 - (-2))) × 100 = 2.12/10 × 100 = 21.2
                "score": 21.2,
                "source_note": "MacroTrends (2026 data): Thessaloniki metro population 815,000 in 2024 = 0% growth from 2023. 2023 was 0.12% growth from 2022. Greece overall has -0.47% growth rate (Demographics of Greece, Wikipedia 2025). Used 0.12% as best recent annual estimate. Low but not negative."
            },

            "expat_concentration": {
                # Thessaloniki growing expat community but smaller than Athens. ~4–6% foreign nationals.
                # ((5 - 0) / (100 - 0)) × 100 = 5.0
                "score": 5.0,
                "source_note": "No direct city-level expat % data found for Thessaloniki. Greece-wide foreign nationals ~8.4% (Wikipedia Demographics of Greece). Thessaloniki has lower expat concentration than Athens due to fewer diplomatic/corporate presences. Growing Golden Visa investor interest noted (Investropa 2025). Estimated 5% based on national baseline adjusted downward for non-capital city."
            },

            # ── GROUP 4: SUPPLY PRESSURE & RISK ──────────────────────────────

            "immediate_pipeline_risk": {
                # LUX&EASY itself is 2,300 units across the metro. Per 2km radius, spread reduces concentration.
                # Limited other major new construction in Thessaloniki (limited supply per market reports).
                # Estimate ~400 units within 2km of any given LUX&EASY cluster within 24 months.
                # ((400 - 0) / (5000 - 0)) × 100 = 8.0
                "score": 8.0,
                "source_note": "Thessaloniki is characterised by 'limited new construction' per Investropa (June 2025). The LUX&EASY project itself (2,300 units spread across metro) is the dominant new supply. Within any 2km radius of individual LUX&EASY clusters, pipeline estimated at ~300–500 units over 24 months. Thessaloniki new supply growing 22.87% in STR listings (Airbtics 2025) but physical residential pipeline constrained."
            },

            "active_unsold_inventory": {
                # LUX&EASY is under construction (not yet completed). Focus on completed submarket stock.
                # Thessaloniki market described as "inventory constrained" with limited unsold stock.
                # Estimated ~12% unsold of completed units in the broader submarket.
                # ((12 - 0) / (40 - 0)) × 100 = 30.0
                "score": 30.0,
                "source_note": "Variable measures completed units in submarket currently unsold (not this project, which is under construction). Thessaloniki market described as having constrained inventory and strong absorption (The Luxury Playbook July 2025, Investropa June 2025). Estimated ~12% unsold of completed stock. Note: LUX&EASY project itself has ~93% unsold (2,141 of 2,300 available) — separately flagged in presales_pct_achieved."
            },

            # ── GROUP 5: DELIVERY TRACK RECORD ───────────────────────────────

            "average_delay_duration": {
                # NOVA CONSTRUCTIONS: AA credit rating, KPMG audited, ISO certified.
                # Multiple completed projects on website (Hilton Garden Inn, EDEN Residence, BRIDGE Residence, etc.).
                # No public record of delays found. Conservative estimate: ~3 months.
                # ((3 - 0) / (24 - 0)) × 100 = 12.5
                "score": 12.5,
                "source_note": "NOVA CONSTRUCTIONS S.A. holds AA credit rating and has KPMG auditing. Projects page shows multiple completed developments (Hilton Garden Inn Athens Syggrou Ave, EDEN Residence Gerakas, OASIS Residence Glyfada, BRIDGE Residence Drosia, etc.) without public reports of material delays. No litigation or stalled-project news found. Conservative 3-month average delay estimate based on typical Greek small-to-mid developer construction buffer."
            },

            "pct_projects_delivered": {
                # NOVA shows completed projects on their website across residential and hospitality.
                # Based on project listing (completed vs under construction), ~85–90% delivery rate.
                # ((88 - 0) / (100 - 0)) × 100 = 88.0
                "score": 88.0,
                "source_note": "NOVA CONSTRUCTIONS projects page (novaconstructionssa.com/projects) lists multiple completed projects (Hilton Garden Inn, Eden Residence, OASIS Residence, BRIDGE Residence, Piraeus properties) alongside current under-construction pipeline. Estimated 85–90% delivery rate based on ratio of completed to announced projects. No failed or abandoned projects identified."
            },

            "completion_consistency": {
                # No evidence of delays or inconsistency. AA credit. 'High' = 100.
                "score": 100,
                "source_note": "NOVA CONSTRUCTIONS holds AA credit rating (novaconstructionssa.com), is KPMG audited, ISO certified, and has a vertically integrated team ('all sectors in-house'). Multiple completed projects found. No public delay complaints or legal issues identified. Classified as 'High' consistency."
            },

            # ── GROUP 6: FINANCIAL CREDIBILITY ───────────────────────────────

            "escrow_quality": {
                # Greece has no RERA/UAE-equivalent statutory escrow for off-plan.
                # Greek law requires notarised preliminary contracts (symvoleografiki) and building permits,
                # providing partial buyer protection but not strict escrowed funds.
                "score": 50,
                "source_note": "Greece does not operate a statutory escrow system equivalent to UAE RERA. Off-plan protection comes through notarised preliminary contracts (symvoleografiki praxeis) and bank guarantees where applicable. NOVA's KPMG auditing and AA credit provide additional credibility. Classified as 'Partial' per scoring dictionary = 50."
            },

            "debt_cash_position": {
                # NOVA is privately held, unfunded (Tracxn), AA credit rating. Small/mid developer.
                # AA credit indicates low debt risk. No balance sheet publicly available.
                # Estimated ~62/100 (solid for private Greek developer, but limited transparency).
                "score": 62,
                "source_note": "NOVA CONSTRUCTIONS S.A. holds AA credit rating (AHK Greece member page) and is KPMG audited. Tracxn confirms no external equity funding raised (bootstrapped). Financial statements not publicly available (private company). AA rating implies healthy debt/cash position; estimated 62/100 reflecting strong rating signal without full balance sheet access."
            },

            "stalled_projects_count": {
                # 0 stalled projects found. ((0 - 0) / (10 - 0)) × 100 = 0.0
                "score": 0.0,
                "source_note": "No stalled projects identified in web searches across NOVA CONSTRUCTIONS project pages, Greek property media, or construction databases. All listed projects appear active or completed. Score = 0 (no stalled projects detected)."
            },

            "presales_pct_achieved": {
                # 2,141 of 2,300 units listed as 'Available' = ~159 sold = 6.9% sold/reserved.
                # For March 2027 completion, this is a very low presales rate.
                # ((6.9 - 0) / (100 - 0)) × 100 = 6.9
                "score": 6.9,
                "source_note": "Spec sheet states '2,141 of 2,300 units available' = 159 units sold/reserved = 6.9% presales achieved. Completion target March 2027. This is a LOW presales rate for a project with ~10 months to delivery. RED FLAG: Either the marketing is nascent for this tranche, or absorption is slower than expected for a 2,300-unit mass development. Cross-verify with developer before proceeding."
            },

            # ── GROUP 7: COMP MARKET PERFORMANCE ─────────────────────────────

            "comp_capital_appreciation": {
                # Thessaloniki prices up 83.5% since 2019 (6 years) = ~10.7% annualized.
                # But recent: 12.1% in Q3 2024. Use 5-year = ~11%.
                # ((11 - (-5)) / (25 - (-5))) × 100 = 16/30 × 100 = 53.3
                "score": 53.3,
                "source_note": "Thessaloniki property prices up 83.5% since 2019 per Investropa (June 2025) = ~10.7% annualized over 6 years. Q3 2024 YoY growth = 12.1% (Rethinking The Future, Nov 2025). Bank of Greece confirms 8.8% annual growth rate for Thessaloniki (Astons Greece, Jan 2026). Used 11% as 5-year CAGR estimate. Formula: ((11-(-5))/(25-(-5)))×100 = 53.3."
            },

            "comp_rental_yields": {
                # Multiple sources: 6.5–9% (Luxury Playbook), 4–7% (Investropa), ~6% (Ellas Estate).
                # Central areas with student demand at upper end. Use 7% midpoint.
                # ((7 - 2) / (12 - 2)) × 100 = 5/10 × 100 = 50.0
                "score": 50.0,
                "source_note": "Gross rental yields in Thessaloniki: 6.5–9% per The Luxury Playbook (Jul 2025), 4–7% central per Investropa (Jun 2025), ~6% average per Ellas Estate (Aug 2025), 6–8% per Astons Greece (Jan 2026). Used 7% midpoint. Strong student/professional demand supports yields. Formula: ((7-2)/(12-2))×100 = 50.0."
            },

            "comp_occupancy_rate": {
                # STR: 62% (Airbtics 2024/25). Long-term rentals: very high demand, ~3–5% vacancy.
                # Blended estimate: ~80%. ((80 - 50) / (100 - 50)) × 100 = 60.0
                "score": 60.0,
                "source_note": "Airbtics (Sep 2024–Aug 2025): 62% avg STR occupancy for Thessaloniki (2,921 listings). Long-term rental vacancy extremely low due to student housing shortage (10% rent jump in 2024, Investropa). Blended occupancy estimate 80% combining both segments. Formula: ((80-50)/(100-50))×100 = 60.0."
            },

            # ── GROUP 8: SPECULATION RISK ─────────────────────────────────────

            "str_concentration": {
                # 3,064 active Airbnb listings (AirROI Nov 2025) in Thessaloniki Municipal Unit.
                # City population ~350K (municipal). Housing stock ~150K–200K units estimated.
                # 3,064 / 175,000 ≈ 1.75%. BUT: academic context (217% growth since 2019) suggests higher
                # concentration in central areas. Central submarket ~8–10%.
                # Use 8%. ((8 - 0) / (60 - 0)) × 100 = 13.3
                "score": 13.3,
                "source_note": "AirROI (Nov 2025): 3,064 active Airbnb listings in Thessaloniki Municipal Unit. Article notes 217% increase in Airbnb listings 2019–2023 (Blackinvestor360.com May 2025) with concentration near Aristotle University campus. Central concentration estimated ~8–10% of residential stock. Broader metro lower. Used 8% for LUX&EASY submarket. Formula: ((8-0)/(60-0))×100 = 13.3."
            },

            "investor_owner_ratio": {
                # Strong investor activity. Golden Visa buyers, domestic investors.
                # Greece-wide: ~40% of transactions are foreign buyers (Investropa).
                # Thessaloniki: ~35–45% investor ownership in new stock.
                # ((40 - 0) / (100 - 0)) × 100 = 40.0
                "score": 40.0,
                "source_note": "Foreign buyers represent ~40% of purchases in Greece generally (Investropa Jun 2025). Thessaloniki attracting growing domestic and international investor base. Golden Visa requirement now €800K (same as Athens since 2024), reducing price arbitrage advantage. Estimated 40% investor/owner ratio for new LUX&EASY-type stock based on market composition data."
            },

            "offplan_secondary_dominance": {
                # Greece market still recovery-phase; off-plan growing but not dominant.
                # Estimate ~30–35% of transactions are off-plan in Thessaloniki.
                # ((33 - 0) / (100 - 0)) × 100 = 33.0
                "score": 33.0,
                "source_note": "No direct data on off-plan vs secondary split for Thessaloniki found. Greek market historically secondary-dominant post-crisis. With recovery phase and new projects like LUX&EASY, off-plan growing but secondary transactions still dominant. Estimated ~33% off-plan concentration based on market context (Investropa, Astons Greece 2025 data)."
            },
        }
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PROPERTY 2 — ONE ATHENS
    # Developer: DIMAND S.A.
    # Location: Kolonaki / Athens City Centre, Athens
    # Stage: Ready to Move (spec says completion March 2027 — treated as near-delivered)
    # Price: €200K–€4.5M | 200 units | 180 currently available (~20 sold)
    # ══════════════════════════════════════════════════════════════════════════
    "one_athens": {
        "project_name": "One Athens",
        "developer": "DIMAND S.A.",
        "city": "Athens",
        "country": "Greece",
        "area": "Kolonaki / Athens City Centre",
        "raw_variables": {

            # ── GROUP 1: DEMAND & LIQUIDITY ───────────────────────────────────

            "micro_market_stage": {
                # Kolonaki is Athens' prime luxury neighbourhood. Fully established.
                "score": 100,
                "source_note": "Kolonaki is Athens' most established luxury residential neighbourhood — home to embassies, luxury retail, and the Concert Hall. Property prices €5,400–€6,150/sqm (Investropa 2026). Classified 'Established' = 100. Source: Investropa Athens Housing Prices (Apr 2026), Wikipedia Kolonaki article."
            },

            "rental_absorption_velocity": {
                # Kolonaki commands premium tenants (executives, diplomats). ~30–40 days absorption.
                # ((365 - 35) / (365 - 30)) × 100 = 330/335 × 100 = 98.5
                "score": 98.5,
                "source_note": "Kolonaki has among Athens' highest rental demand — executives, diplomats, expats, and high-income professionals. Athens market sells in ~58 days overall (Immigrantinvest Aug 2025); Kolonaki rentals absorb faster given prestige. Used 35-day absorption estimate. Formula: ((365-35)/(365-30))×100 = 98.5."
            },

            "resale_velocity": {
                # Kolonaki luxury resale: slower than mid-market due to high price point, but strong demand.
                # ~70–80 days. ((730 - 75) / (730 - 30)) × 100 = 655/700 × 100 = 93.6
                "score": 93.6,
                "source_note": "Athens market: homes selling in ~58 days on average (Immigrantinvest Aug 2025). Kolonaki luxury at €200K–€4.5M has narrower buyer pool but strong demand. Used 75-day resale estimate. Formula: ((730-75)/(730-30))×100 = 93.6."
            },

            "days_on_market": {
                # Athens average ~58 days. Kolonaki premium units may sit slightly longer.
                # ((365 - 62) / (365 - 7)) × 100 = 303/358 × 100 = 84.6
                "score": 84.6,
                "source_note": "Athens residential properties average ~58 days on market (Immigrantinvest Aug 2025, Immigrantinvest.com). Kolonaki premium units attract premium buyers — slightly longer than city average. Used 62-day estimate. Formula: ((365-62)/(365-7))×100 = 84.6."
            },

            "occupancy_vacancy_rate": {
                # Athens central vacancy rate ~3.9% (Investropa June 2025). Occupancy = 96.1%.
                # ((96 - 50) / (100 - 50)) × 100 = 46/50 × 100 = 92.0
                "score": 92.0,
                "source_note": "Athens central districts vacancy rate 3.9% (Investropa June 2025: 'renting exposes you to rising costs—rents have increased significantly in central districts with only 3.9% vacancy rates'). Colonaki occupancy = ~96%. Formula: ((96-50)/(100-50))×100 = 92.0."
            },

            # ── GROUP 2: NEIGHBORHOOD LIVABILITY ─────────────────────────────

            "safety_crime_index": {
                # Athens Safety Index = 44.89 (Numbeo current comparison data).
                "score": 44.89,
                "source_note": "Numbeo Crime Comparison Tool (Athens vs Thessaloniki, current data May 2026): Athens Crime Index = 55.11, Safety Index = 44.89. Corroborated by Greek Reporter (Oct 2025): Athens scored 55.3 on 2025 Numbeo Crime Index. Variable spec: use safety scale as-is. Kolonaki itself is one of Athens' safer neighborhoods (diplomatic/upscale area) but city-level index applied."
            },

            "healthcare_access": {
                # Evaggelismos General Hospital is IN Kolonaki (one of Greece's largest public hospitals).
                # Multiple private clinics and medical centres walking distance. Score ~88.
                "score": 88,
                "source_note": "Evaggelismos General Hospital (Υποδιοίκηση Νοσοκομείων Αθηνών) is located directly in Kolonaki at Ipsilandou 45 — walking distance from the neighbourhood. Additionally, multiple premium private clinics (Mitera, Hygeia Hospital 3km away) and specialist practices throughout Kolonaki. Top-tier healthcare access for any Athens district."
            },

            "school_quality": {
                # Athens College (Κολλέγιο Αθηνών) in Psychiko (~4km), Campion School (~8km),
                # British Council-linked schools, Athens Montessori. Kolonaki has private tutoring centres.
                "score": 75,
                "source_note": "Athens has multiple top international/private schools: Athens College (IB, ~4km from Kolonaki), Campion School (British curriculum, ~8km), St Catherine's British Embassy School (~5km), ACS Athens (American curriculum, ~15km). Kolonaki proximity to diplomatic quarter supports demand from expat families. Scored 75/100 reflecting strong but not best-in-Europe provision."
            },

            "air_quality_index": {
                # Athens annual PM2.5 ~12–15 μg/m³ (current AQI readings 33–46 'Good' to 'Moderate').
                # Using PM2.5 ~13 μg/m³: ((50 - 13) / 50) × 100 = 37/50 × 100 = 74.0
                "score": 74.0,
                "source_note": "AQI.in (Apr 2026): Athens current AQI ~33 (Good), PM2.5 ~8 μg/m³. AQICN Athens data: AQI ~46. IQAir Greece page: Athens generally better air than Thessaloniki. Annual PM2.5 estimated at ~13 μg/m³ for Athens metro. Conversion: ((50-13)/50)×100 = 74.0. City-centre vehicle traffic increases pollution vs coastal areas."
            },

            "beach_coastal_access": {
                # Kolonaki to nearest beach: Piraeus/Faliro ~10km, Glyfada ~14km.
                # >10km = score 0 per spec bracket.
                "score": 0,
                "source_note": "Kolonaki is a landlocked city-centre neighbourhood on Mount Lycabettus slopes. Nearest beaches: Piraeus/Kastella ~10km, Faliro Bay ~11km, Glyfada ~14km. Per spec: >10km = 0. No coastal access."
            },

            # ── GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ─────────────────────

            "population_growth_rate": {
                # Athens metro: slightly positive population growth. ~0.5% annual estimate.
                # ((0.5 - (-2)) / (8 - (-2))) × 100 = 2.5/10 × 100 = 25.0
                "score": 25.0,
                "source_note": "Greece overall population: -0.47% (Wikipedia Demographics of Greece 2025 est.). Athens metro benefits from domestic migration (brain drain from provinces) and foreign immigration partially offsetting national decline. Athens metro estimated ~0.5% positive growth based on urbanization patterns. Greece net migration rate: +1.1 migrants/1,000 (Wikipedia 2024 est.). Formula: ((0.5-(-2))/(8-(-2)))×100 = 25.0."
            },

            "expat_concentration": {
                # Kolonaki: diplomatic quarter, home to embassies, expat executives.
                # Athens-wide foreign buyers ~40% of transactions. Resident expat population ~10–12%.
                # ((11 - 0) / (100 - 0)) × 100 = 11.0
                "score": 11.0,
                "source_note": "Foreign buyers represent ~40% of Athens residential purchases (Investropa June 2025, Benoit Properties Dec 2025). Kolonaki hosts numerous embassies and diplomatic residences, attracting a permanent expat professional class. Resident expat concentration estimated ~11% (above Athens average due to diplomatic/corporate presence). Formula: ((11-0)/(100-0))×100 = 11.0."
            },

            # ── GROUP 4: SUPPLY PRESSURE & RISK ──────────────────────────────

            "immediate_pipeline_risk": {
                # Kolonaki is a fully built-up historic urban neighbourhood. Minimal new construction.
                # Heritage restrictions, dense plot coverage limit development.
                # Estimate ~30–50 units within 2km within 24 months.
                # ((40 - 0) / (5000 - 0)) × 100 = 0.8
                "score": 0.8,
                "source_note": "Kolonaki is a dense, historic, fully built-out neighbourhood with minimal vacant land for new development. Athens Luxury Playbook (Apr 2026) notes 'genuine scarcity of new stock' in central districts. STR ban since Jan 2025 (extended through 2026) prevents new conversions. Estimated ~40 new units within 2km over 24 months. Formula: ((40-0)/(5000-0))×100 = 0.8. Effectively zero supply pressure."
            },

            "active_unsold_inventory": {
                # Central Athens has very low completed unsold stock (3.9% vacancy rate, strong absorption).
                # ~10% unsold completed units estimated in Kolonaki submarket.
                # ((10 - 0) / (40 - 0)) × 100 = 25.0
                "score": 25.0,
                "source_note": "Athens central vacancy 3.9% (Investropa June 2025). One Athens spec shows 180/200 units still available — but this is a new project awaiting buyers, not unsold completed secondary stock. For the broader Kolonaki submarket of completed units, estimated ~10% unsold based on tight vacancy data. Formula: ((10-0)/(40-0))×100 = 25.0. ⚠️ Note: One Athens project itself has only 10% sold — low absorption flagged separately under presales."
            },

            # ── GROUP 5: DELIVERY TRACK RECORD (DIMAND) ──────────────────────

            "average_delay_duration": {
                # DIMAND: 15+ year track record, listed on ATHEX, EBRD partner, LEED Gold certified.
                # Known for 'delivering on time, within budget' (dimand.gr). ~2–3 month average delay.
                # ((2.5 - 0) / (24 - 0)) × 100 = 10.4
                "score": 10.4,
                "source_note": "DIMAND S.A. states on website: 'committed to generate added value...delivering the projects on time, within budget.' Listed on Athens Stock Exchange (ATHEX). EBRD notes 'solid development and investment record' in €71.5M JV case study. DIMAND developed Greece's first LEED Gold building (Karela Office Park). No public delay complaints found. Used ~2.5 months average delay estimate. Formula: ((2.5-0)/(24-0))×100 = 10.4."
            },

            "pct_projects_delivered": {
                # DIMAND founded 2005, 15+ years, listed company with multiple completed projects
                # (Karela Office Park, Moxy Athens City, AGEMAR HQ, Cosmote TV HQ, Piraeus Tower in progress).
                # ~95% delivery rate estimate.
                # ((95 - 0) / (100 - 0)) × 100 = 95.0
                "score": 95.0,
                "source_note": "DIMAND S.A. (LinkedIn/dimand.gr): founded 2005, developed 40% of all LEED-certified buildings in Greece, delivered multiple landmark projects (Karela Office Park LEED Gold, Moxy Athens City LEED Gold hotel, AGEMAR/Angelicoussis HQ LEED Platinum). EBRD partner since early investment phase. No abandoned/failed projects in public record. Estimated 95% delivery rate based on portfolio evidence."
            },

            "completion_consistency": {
                # DIMAND's entire brand built on on-time, on-budget delivery. Listed company accountability.
                "score": 100,
                "source_note": "DIMAND S.A. listed on ATHEX (public accountability), EBRD-backed JV partner, 'best-in-class local developer' per EBRD case study, 15+ years consistent delivery. 'High' completion consistency = 100 per scoring dictionary."
            },

            # ── GROUP 6: FINANCIAL CREDIBILITY ───────────────────────────────

            "escrow_quality": {
                # Same as LUX&EASY: Greece lacks statutory off-plan escrow.
                "score": 50,
                "source_note": "Greece has no UAE RERA-equivalent statutory escrow for off-plan sales. Protection comes via notarised preliminary contracts and DIMAND's status as a listed company on ATHEX (regulatory disclosure requirements apply). DIMAND's EBRD partnership and public listing provide stronger buyer assurance than private developers. Still classified 'Partial' = 50 as statutory escrow framework absent."
            },

            "debt_cash_position": {
                # DIMAND is listed on ATHEX, EBRD €71.5M JV investment, active in multiple large projects.
                # Public company with regular financial disclosures. Medium leverage expected.
                # Score ~72.
                "score": 72,
                "source_note": "DIMAND S.A. listed on Athens Stock Exchange with regular financial reporting. EBRD invested €71.5M in JV partnership. Multiple simultaneous active projects (Piraeus Tower, Syngrou Avenue Office Buildings) suggest access to institutional finance. No balance sheet figures found in public sources for standalone company financials. Estimated 72/100 reflecting listed-company governance and institutional backing."
            },

            "stalled_projects_count": {
                # 0 stalled projects found. Score = 0.
                "score": 0.0,
                "source_note": "No stalled DIMAND projects identified. All referenced projects (Piraeus Tower, Moxy Athens City, Syngrou Ave offices) are active. Score = 0."
            },

            "presales_pct_achieved": {
                # 180 of 200 units available = 20 sold/reserved = 10% presales.
                # ⚠️ This is 'Ready to Move' status — very concerning if only 10% sold at delivery.
                # ((10 - 0) / (100 - 0)) × 100 = 10.0
                "score": 10.0,
                "source_note": "Spec sheet: '180 of 200 units available' = ~20 units sold/reserved = 10% presales. Project labelled 'Ready to Move' with March 2027 completion. ⚠️ RED FLAG: Only 10% sold at a project described as ready-to-move is unusually low for a central Athens location. Possible explanations: (1) marketing just launched, (2) premium price range (€200K–€4.5M) narrows buyer pool, (3) Kolonaki STR ban since Jan 2025 eliminated yield investors. Requires agent verification."
            },

            # ── GROUP 7: COMP MARKET PERFORMANCE ─────────────────────────────

            "comp_capital_appreciation": {
                # Athens 5-year annualized: prices up 32–35% from 2018–2022 + continued growth.
                # 2024: 7.6–8.6% YoY. 5-year CAGR ~9–10%.
                # ((9.5 - (-5)) / (25 - (-5))) × 100 = 14.5/30 × 100 = 48.3
                "score": 48.3,
                "source_note": "Athens property 5-year appreciation: Bank of Greece confirms 8.7% increase in 2024, Q2 2025 +7.3% YoY (Astons Greece Jan 2026). 2018–2022 saw 32–35% cumulative gains. 5-year CAGR estimated at ~9.5% annualized. Kolonaki specifically: prices at €5,400–€6,150/sqm (Investropa Apr 2026), among highest in Greece. Formula: ((9.5-(-5))/(25-(-5)))×100 = 48.3."
            },

            "comp_rental_yields": {
                # Kolonaki known for LOWEST yields in Athens due to high acquisition costs.
                # 3.5–4.5% per Investropa. Use 4%.
                # ((4 - 2) / (12 - 2)) × 100 = 2/10 × 100 = 20.0
                "score": 20.0,
                "source_note": "Investropa (Jun 2025): 'Kolonaki, Plaka, and Kifisia typically deliver 3.5% to 4.5% gross yields due to premium positioning and high acquisition costs.' STR ban since Jan 2025 eliminates short-term rental upside for new purchasers. Used 4% gross yield. Formula: ((4-2)/(12-2))×100 = 20.0. Lowest yield neighbourhood in Athens."
            },

            "comp_occupancy_rate": {
                # Long-term: ~96% occupancy (3.9% vacancy). Premium units well-occupied.
                # ((96 - 50) / (100 - 50)) × 100 = 46/50 × 100 = 92.0
                "score": 92.0,
                "source_note": "Athens central vacancy rate 3.9% (Investropa June 2025) = 96.1% occupancy. Kolonaki as Athens' premier address commands essentially full occupancy for quality stock. Formula: ((96-50)/(100-50))×100 = 92.0."
            },

            # ── GROUP 8: SPECULATION RISK ─────────────────────────────────────

            "str_concentration": {
                # Kolonaki STR ban since Jan 2025, extended through 2026.
                # Legacy licensed STRs represent ~15% of stock (before ban).
                # Active licensed concentration now frozen and declining.
                # ((15 - 0) / (60 - 0)) × 100 = 25.0
                "score": 25.0,
                "source_note": "STR ban in Kolonaki effective Jan 1, 2025, extended through Dec 2026 (Investropa Apr 2026, Rethinking The Future Nov 2025). No new AMA registration numbers being issued for Kolonaki (1st–3rd municipal districts). Legacy licensed STRs active but declining as leases roll off. Pre-ban Athens had ~18,000 listings across the city. Kolonaki legacy STR concentration estimated ~15%. Formula: ((15-0)/(60-0))×100 = 25.0."
            },

            "investor_owner_ratio": {
                # Foreign buyers ~40% of Athens transactions. Kolonaki: diplomatic/corporate expat buyers.
                # Higher investor ratio vs residential buyer given STR ban eliminating yield play.
                # Estimate ~50% investor.
                # ((50 - 0) / (100 - 0)) × 100 = 50.0
                "score": 50.0,
                "source_note": "Foreign buyers ~40% of Athens transactions (Investropa Jun 2025). Kolonaki's diplomatic quarter and luxury positioning attracts high investor/second-home buyer concentration. With STR ban, pure yield investors replaced by buy-to-hold capital appreciation investors. Estimated 50% investor ratio. Formula: ((50-0)/(100-0))×100 = 50.0."
            },

            "offplan_secondary_dominance": {
                # One Athens is a redevelopment (converted building). Athens market has growing off-plan
                # segment. Central Athens: ~30–35% off-plan of total transactions.
                # ((32 - 0) / (100 - 0)) × 100 = 32.0
                "score": 32.0,
                "source_note": "Athens market has growing off-plan segment but remains secondary-transaction dominant. Central districts (Kolonaki, Koukaki) see primarily secondary and redevelopment stock. Estimate ~32% off-plan dominance for Kolonaki submarket based on overall Athens recovery-market trends. No direct Kolonaki-specific off-plan data found."
            },
        }
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PROPERTY 3 — THE ELLINIKON – MARINA RESIDENCES
    # Developer: LAMDA Development S.A.
    # Location: Elliniko / Agios Kosmas Marina, Athens
    # Stage: Under Construction | Original completion June 2026 → actual ~2027
    # Price: €1M–€20M | 200 units | 178 currently available (~22 sold/reserved)
    # ══════════════════════════════════════════════════════════════════════════
    "ellinikon_marina_residences": {
        "project_name": "The Ellinikon – Marina Residences",
        "developer": "LAMDA Development S.A.",
        "city": "Athens",
        "country": "Greece",
        "area": "Elliniko / Agios Kosmas Marina, Athens Riviera",
        "raw_variables": {

            # ── GROUP 1: DEMAND & LIQUIDITY ───────────────────────────────────

            "micro_market_stage": {
                # Ellinikon is a brand-new district on a former airport. Strong pre-sales momentum
                # (85–93% reservation rate at Little Athens sub-zone) but no operational track record.
                # New urban zone with commercial activity beginning 2027–2028. 'Activating' = 75.
                "score": 75,
                "source_note": "Ellinikon is a new urban district under construction on the former Athens International Airport (6km² site). Little Athens sub-zone has 85% sold/reserved (Feb 2026, LAMDA annual results). Riviera Galleria opening 2027, Marina operational 2027–2028. No existing residential community yet operational. Classified 'Activating' = 75: strong demand signals but not yet an established living/rental ecosystem."
            },

            "rental_absorption_velocity": {
                # Projected once operational. Athens Riviera coastal premium property demand is strong.
                # Luxury coastal €1M+ rentals: ~45–60 days absorption estimated.
                # ((365 - 50) / (365 - 30)) × 100 = 315/335 × 100 = 94.0
                "score": 94.0,
                "source_note": "Projected post-completion rental absorption for Athens Riviera coastal luxury property. Athens overall market: ~58 days (Immigrantinvest 2025). Ellinikon luxury coastal positioning targets UHNWI and executive renters with limited comparable supply. Used 50-day conservative estimate given ultra-luxury (€1M+ entry) buyer/renter pool. Formula: ((365-50)/(365-30))×100 = 94.0. NOTE: forward estimate only — no live rental data for this new district."
            },

            "resale_velocity": {
                # Ultra-luxury (€1M–€20M) resale: narrow buyer pool, but premium assets hold well.
                # Athens Riviera ~90–120 days. Used 120 days.
                # ((730 - 120) / (730 - 30)) × 100 = 610/700 × 100 = 87.1
                "score": 87.1,
                "source_note": "Athens Riviera luxury properties: still relatively liquid given strong foreign buyer demand (~40% of Athens transactions are foreign, Investropa Jun 2025). Ellinikon Marina at €1M–€20M has a narrower buyer pool. Used 120-day resale velocity estimate for ultra-luxury coastal. Formula: ((730-120)/(730-30))×100 = 87.1. NOTE: No live resale data exists for Ellinikon — entire district still under construction."
            },

            "days_on_market": {
                # Projected future metric. Athens average 58 days. Premium Riviera: ~80 days.
                # ((365 - 80) / (365 - 7)) × 100 = 285/358 × 100 = 79.6
                "score": 79.6,
                "source_note": "Athens average days on market ~58 days (Immigrantinvest Aug 2025). Athens Riviera premium addresses historically command faster absorption due to scarcity value, but ultra-luxury €1M+ narrows pool. Used 80 days as forward estimate. Formula: ((365-80)/(365-7))×100 = 79.6."
            },

            "occupancy_vacancy_rate": {
                # Projected post-completion. Athens Riviera coastal demand strong. ~85% occupancy projected
                # for luxury long-term rental. STR in this area not subject to Athens ban.
                # ((85 - 50) / (100 - 50)) × 100 = 35/50 × 100 = 70.0
                "score": 70.0,
                "source_note": "Projected post-completion occupancy. Ellinikon zone is outside Athens 1st–3rd municipal districts STR ban. Athens Riviera coastal luxury in Glyfada/Voula achieves ~85%+ occupancy (strong domestic and international demand). Conservative 85% estimate for new Ellinikon area given lack of established community and current STR growth trajectory. Formula: ((85-50)/(100-50))×100 = 70.0."
            },

            # ── GROUP 2: NEIGHBORHOOD LIVABILITY ─────────────────────────────

            "safety_crime_index": {
                # Elliniko municipality (south Athens suburb): significantly safer than city centre.
                # Numbeo doesn't have Elliniko-specific data; Athens Safety = 44.89.
                # South suburbs estimated ~55–60 (upscale residential, lower crime than centre).
                "score": 57,
                "source_note": "Elliniko is a southern Athens suburb (Elliniko-Argyroupoli municipality), well removed from the central Athens areas driving the lower Numbeo safety score of 44.89. South Athenian suburbs are consistently safer per resident reports (Numbeo Athens city page comments confirm '95% of Athens is safe'). Estimated 57/100 for Elliniko — between Athens central and rural safety levels. No Elliniko-specific Numbeo data available."
            },

            "healthcare_access": {
                # Nearest major hospitals: Asklepion General Hospital Voula (~4km), Metropolitan Hospital
                # Nea Faliro (~7km), and private Hygeia/Mitera group clinics. Good access.
                "score": 70,
                "source_note": "Nearest hospitals: Asklepion General Hospital in Voula (~4km south), Metropolitan Hospital in Nea Faliro (~7km north). Private hospital groups (Hygeia, Mitera) accessible within 15–20 min drive. Ellinikon masterplan includes healthcare facilities in later phases. Current healthcare access scored 70/100 — good suburban access but not Kolonaki-level proximity."
            },

            "school_quality": {
                # South Athens: Byron College (~5km), Glyfada-area private schools, ACS Athens (~12km).
                "score": 63,
                "source_note": "South Athens private/international schools: Byron College in Glyfada (~5km), British School of Athens Glyfada branch (~6km), ACS Athens (American Community Schools, ~12km via Attiki Odos). Ellinikon masterplan includes education facilities in later phases. Scored 63/100 — solid international school access within commutable distance."
            },

            "air_quality_index": {
                # Coastal Elliniko/Agios Kosmas: sea breeze, low traffic, cleaner than city centre.
                # Annual PM2.5 estimated ~9–10 μg/m³. ((50 - 9.5) / 50) × 100 = 40.5/50 × 100 = 81.0
                "score": 81.0,
                "source_note": "Elliniko is a coastal zone on the Saronic Gulf with consistent sea breezes, significantly reducing PM2.5 levels vs city centre (Athens city AQI ~40 vs coastal estimate ~25–30). Annual PM2.5 estimated ~9–10 μg/m³ based on coastal Athens measurements (below WHO 10 μg/m³ threshold). Conversion: ((50-9.5)/50)×100 = 81.0. Best air quality of the three properties analysed."
            },

            "beach_coastal_access": {
                # Marina Residences are adjacent to Agios Kosmas Marina with direct beach access.
                # <500m to beach per project description (waterfront position). Score = 100.
                "score": 100,
                "source_note": "The Ellinikon Marina Residences are directly adjacent to Agios Kosmas Marina on the Saronic Gulf coastline. The Ellinikon masterplan includes 'over half a mile of pristine beach' (Robb Report Dec 2025, The Life of Luxury Nov 2025). Riviera Galleria is also adjacent to the marina area. Per spec: <500m to beach = 100. Score = 100."
            },

            # ── GROUP 3: DEMOGRAPHIC & ECONOMIC STRENGTH ─────────────────────

            "population_growth_rate": {
                # Ellinikon municipality: expected significant population growth as masterplan delivers
                # 9,000+ residential units by 2030. But current Elliniko-Argyroupoli municipality
                # growth tracks broader Athens pattern (~0.5%).
                # ((0.5 - (-2)) / (8 - (-2))) × 100 = 25.0
                "score": 25.0,
                "source_note": "Elliniko-Argyroupoli municipality currently tracks Athens metro growth (~0.5%). The Ellinikon masterplan will deliver 9,000 residential units and attract 1M+ annual visitors (Athens Times Mar 2026), substantially increasing local population from ~2030. Current baseline: standard Athens 0.5% growth estimate. Formula: ((0.5-(-2))/(8-(-2)))×100 = 25.0."
            },

            "expat_concentration": {
                # Ellinikon specifically targets international buyers (40% of Athens transactions are foreign).
                # Luxury positioning and Athens Riviera lifestyle attract affluent expat/international buyers.
                # Estimated 15–20% expat concentration once populated.
                # ((17 - 0) / (100 - 0)) × 100 = 17.0
                "score": 17.0,
                "source_note": "Ellinikon's luxury price point (€1M–€20M) and Athens Riviera positioning targets high-net-worth international buyers. LAMDA notes 'rich foreign buyers' as key demand driver (National Herald Mar 2025). Foreign buyers ~40% of broader Athens transactions (Investropa). Estimated 17% expat concentration among eventual Ellinikon Marina residents — above Athens average due to ultra-luxury positioning. Formula: ((17-0)/(100-0))×100 = 17.0."
            },

            # ── GROUP 4: SUPPLY PRESSURE & RISK ──────────────────────────────

            "immediate_pipeline_risk": {
                # Ellinikon masterplan = 9,000 residential units total. Within 2km of Marina Residences:
                # Little Athens (1,200 units), Coastal Front (315 units), Riviera Tower (~200 units),
                # plus ~300 more releasing in 2026. All within the Ellinikon masterplan boundary.
                # ~1,500–2,000 units within 2km over 24 months.
                # ((1800 - 0) / (5000 - 0)) × 100 = 36.0
                "score": 36.0,
                "source_note": "Ellinikon masterplan encompasses 9,000 residential units across the 6km² site. Within 2km of the Marina Residences: Little Athens (~1,200 units, majority sold), Coastal Front (315 units sold out), Riviera Tower (~200 units), plus ~300–450 new units releasing to market in 2026 (Athens Times Mar 2026). Estimated ~1,800 units within 2km under construction/releasing over 24 months. Formula: ((1800-0)/(5000-0))×100 = 36.0."
            },

            "active_unsold_inventory": {
                # Ellinikon is entirely under construction — no completed units in this submarket yet.
                # For broader Athens Riviera coastal submarket (Glyfada, Voula, Vouliagmeni):
                # Strong demand, limited completed inventory. ~15% unsold of completed.
                # ((15 - 0) / (40 - 0)) × 100 = 37.5
                "score": 37.5,
                "source_note": "No completed Ellinikon residential units yet — district is entirely under construction. For broader Athens Riviera submarket (Glyfada, Voula, Vouliagmeni), demand outpaces supply with strong foreign buyer activity. Estimated ~15% unsold of completed stock in the coastal luxury segment. Note: Ellinikon Little Athens itself shows 85–93% presale absorption (LAMDA FY2025 results) suggesting very low unsold risk once delivered. Formula: ((15-0)/(40-0))×100 = 37.5."
            },

            # ── GROUP 5: DELIVERY TRACK RECORD (LAMDA DEVELOPMENT) ───────────

            "average_delay_duration": {
                # Documented: Riviera Tower ~4 months delay (Q1 2025 results).
                # Phase 1 overall: 12–18 months from original 2021–2025 plan (Axia Research).
                # COVID contributed, but structural delays also evident. Average ~6–8 months.
                # ((7 - 0) / (24 - 0)) × 100 = 29.2
                "score": 29.2,
                "source_note": "LAMDA Q1 2025 results: 'projects facing delays of around 4 months include infrastructure works by AVAX and the Riviera Tower by BOUYGUES-AKTOR.' Edison/Axia research: original Phase 1 timelines 2021–2025 now shifted to end-2026, = 12–18 months overall delay. Mikrometoxos.gr (Nov 2024): delays attributed to 'shortage of construction crews.' COVID impact acknowledged. Used 7-month average delay estimate. Formula: ((7-0)/(24-0))×100 = 29.2."
            },

            "pct_projects_delivered": {
                # LAMDA has delivered: The Mall Athens, Mediterranean Cosmos, Golden Hall, Designer Outlet Athens,
                # Hilton Garden Inn Athens (via JV). Ellinikon is its biggest project and first residential delivery.
                # Existing mall/hotel portfolio delivered successfully. ~85% delivery rate on past projects.
                # ((85 - 0) / (100 - 0)) × 100 = 85.0
                "score": 85.0,
                "source_note": "LAMDA Development S.A. (ATHEX-listed) has successfully delivered 4 operating shopping centres (The Mall Athens, Mediterranean Cosmos, Golden Hall, Designer Outlet Athens) and marina operations (LAMDA semi-annual report H1 2025). Ellinikon represents its first large-scale residential delivery. Past portfolio delivery rate estimated ~85% based on operating asset track record. Formula: ((85-0)/(100-0))×100 = 85.0."
            },

            "completion_consistency": {
                # Multiple documented delays. COVID factor + labour shortage. Not consistently on-time.
                # 'Medium' = 50.
                "score": 50,
                "source_note": "Documented construction delays across multiple Ellinikon components: Riviera Tower (4 months), infrastructure (4 months), Little Athens (minor delays from Urban Planning Regulation disputes). Phase 1 overall delayed ~12–18 months from original plan (Axia Research). Labour shortage is systemic. Classified 'Medium' = 50 per scoring dictionary. LAMDA actively accelerating in 2025–2026 with €500M annual investment pace."
            },

            # ── GROUP 6: FINANCIAL CREDIBILITY ───────────────────────────────

            "escrow_quality": {
                # Greece: no statutory escrow. LAMDA is ATHEX-listed public company.
                # Notarised preliminary contracts and strong public accountability, but not strict escrow.
                "score": 50,
                "source_note": "Greece has no RERA-equivalent statutory escrow framework. LAMDA is listed on ATHEX with full regulatory disclosure, audited accounts, and €292M+ in dedicated Ellinikon cash reserves (FY2024 results). No bank debt used for Ellinikon project despite €232M committed credit line (FY2024 press release). These protections surpass standard 'Partial' but formal escrow mechanism absent. Classified 'Partial' = 50."
            },

            "debt_cash_position": {
                # LAMDA: €292M cash allocated to Ellinikon at end 2024, €402M cash H1 2025.
                # No bank debt drawn on Ellinikon despite €232M committed credit line.
                # Secured revenues €2.2B to date. Total portfolio value €3.8B.
                # Very strong. Score ~87.
                "score": 87,
                "source_note": "LAMDA FY2024: 'Total cash balance allocated to Ellinikon Project = €292M; no bank loans utilised for Ellinikon Project.' LAMDA H1 2025: €402M cash balance. Total secured revenues €2.2B (ProtoThema Dec 2025). FY2025: consolidated net profit €91M (+1.9x), portfolio value €3.8B (Athens Times Mar 2026). Debt-free for Ellinikon specifically. Formula: scored 87/100 reflecting excellent cash position with modest group-level leverage from operating mall assets."
            },

            "stalled_projects_count": {
                # No stalled Ellinikon projects. All components progressing (some delayed but not stalled).
                "score": 0.0,
                "source_note": "No stalled Ellinikon projects identified. All components progressing: Riviera Tower (44th floor reached Mar 2026), Riviera Galleria (steel framework being erected), infrastructure works continuing. Score = 0."
            },

            "presales_pct_achieved": {
                # Marina Residences specific: 22 of 200 sold = 11%.
                # Note: broader Ellinikon (Little Athens) has 85–93% presales — much stronger.
                # Marina Residences at €1M–€20M is a distinct ultra-luxury product with narrow buyer pool.
                # ((11 - 0) / (100 - 0)) × 100 = 11.0
                "score": 11.0,
                "source_note": "Spec sheet: '178 of 200 units available' = 22 sold/reserved = 11% presales. ⚠️ NOTE: This is the Marina Residences sub-product (€1M–€20M) — distinct from Little Athens (€8,500/sqm avg, 85–93% presold per LAMDA FY2024/2025 reports). Ultra-luxury price range narrows buyer pool significantly. Contrast: Coastal Front (315 units) = 100% sold; Little Athens = 85% sold. Marina Residences represents the most exclusive and least-absorbed component of Ellinikon to date."
            },

            # ── GROUP 7: COMP MARKET PERFORMANCE ─────────────────────────────

            "comp_capital_appreciation": {
                # Athens Riviera: Edison Research cites ~11% annual appreciation for residential
                # over 6 years. Ellinikon area (Elliniko, Glyfada): exceptional growth post-project announcement.
                # ((11 - (-5)) / (25 - (-5))) × 100 = 16/30 × 100 = 53.3
                "score": 53.3,
                "source_note": "Edison Group (Feb 2026): Athens residential properties increased ~11% per year over last 6 years. Ellinikon area (Elliniko, Glyfada) exceeding Athens average due to masterplan impact. Investropa (Apr 2026): 'southern suburbs and Athens Riviera experiencing exceptional growth due to The Ellinikon Megaproject.' Luxury Athens Riviera prices ~€7,300/sqm avg (Astons Greece), Little Athens prices reached €8,500/sqm (Greek City Times May 2025). Used 11% 5-year CAGR. Formula: ((11-(-5))/(25-(-5)))×100 = 53.3."
            },

            "comp_rental_yields": {
                # Athens Riviera coastal: 4.5–6% per Investropa. Global Property Guide Q4 2024: avg 4.99%.
                # Ultra-luxury at €1M+ will be at lower end (5%). ((5 - 2) / (12 - 2)) × 100 = 30.0
                "score": 30.0,
                "source_note": "Global Property Guide Q4 2024: Athens gross rental yields average 4.99%. Investropa (Jun 2025): 'suburban developments and newer properties in areas like Agios Dimitrios and southern Athens average 4.5%–6%.' Astons Greece (Jan 2026): 'average rental yield 4.5% per year across the country.' Ultra-luxury €1M+ properties yield lower rates (capital appreciation-driven). Used 5% as conservative midpoint. Formula: ((5-2)/(12-2))×100 = 30.0."
            },

            "comp_occupancy_rate": {
                # Athens Riviera projected strong occupancy for luxury coastal.
                # Ellinikon zone outside STR ban — can operate short-term rental.
                # ~85% blended LT/ST occupancy projected.
                # ((85 - 50) / (100 - 50)) × 100 = 35/50 × 100 = 70.0
                "score": 70.0,
                "source_note": "Athens Riviera luxury coastal properties: strong demand from both residents and tourist STR (Ellinikon zone is OUTSIDE the Athens 1st–3rd district STR ban). Projected 85% blended occupancy based on Athens Riviera comparable markets (Glyfada, Voula). STR occupancy in similar coastal areas: 60–70% (Airbtics data for Glyfada-adjacent coastal properties). Formula: ((85-50)/(100-50))×100 = 70.0. Forward estimate only."
            },

            # ── GROUP 8: SPECULATION RISK ─────────────────────────────────────

            "str_concentration": {
                # Elliniko is OUTSIDE Athens 1st–3rd municipal district STR ban.
                # Strong STR potential. Athens has ~18,000 listings (Investropa Apr 2026).
                # Elliniko/Agios Kosmas growing STR hub. Estimate ~18–22% STR concentration.
                # ((20 - 0) / (60 - 0)) × 100 = 33.3
                "score": 33.3,
                "source_note": "Elliniko municipality is OUTSIDE the Athens STR ban zone (ban covers 1st, 2nd, 3rd municipal districts: Kolonaki, Koukaki, etc.). Strong STR potential once Ellinikon delivers. Athens has ~18,000 active STR listings (Investropa Apr 2026). Elliniko coastal area projected to become a high STR concentration zone given marina lifestyle positioning. Estimated 20% STR concentration (growing). Formula: ((20-0)/(60-0))×100 = 33.3."
            },

            "investor_owner_ratio": {
                # Ultra-luxury €1M–€20M means very high investor/second-home buyer ratio.
                # Foreign buyers ~40% of Athens transactions; for luxury Ellinikon: ~70–75% investor/second-home.
                # ((72 - 0) / (100 - 0)) × 100 = 72.0
                "score": 72.0,
                "source_note": "Foreign buyers represent ~40% of Athens transactions broadly (Investropa Jun 2025). For Ellinikon Marina at €1M–€20M: high-net-worth buyers primarily acquiring as second homes/investment. LAMDA CEO confirms 'rich foreign buyers' as key demand driver. Estimated 72% investor/second-home ratio for this ultra-luxury waterfront product. Formula: ((72-0)/(100-0))×100 = 72.0."
            },

            "offplan_secondary_dominance": {
                # Ellinikon is 100% off-plan (under construction). No secondary transactions possible yet.
                # Entire zone is pre-delivery off-plan. Score = 100 (capped).
                "score": 100,
                "source_note": "The Ellinikon is entirely under construction — no completed secondary market exists. All transactions are off-plan pre-sales. 100% off-plan dominance for this district. Formula: ((100-0)/(100-0))×100 = 100. NOTE: Will normalise post-delivery as secondary resales begin."
            },
        }
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ⚠️  PROPERTY 4 — NOT PROVIDED
    # The request specified 4 Greece properties but only 3 were attached.
    # Please supply the 4th property spec for scoring.
    # ══════════════════════════════════════════════════════════════════════════
}


# ──────────────────────────────────────────────────────────────────────────────
# CONFIDENCE SUMMARY TABLE
# ──────────────────────────────────────────────────────────────────────────────
#
# Property                          | Populated | Null | Low Confidence Flags
# ──────────────────────────────────|-----------|------|────────────────────────────────────────────────────────
# LUX&EASY Thessaloniki             |    25     |  0   | expat_concentration (no city-level data; national estimate used)
# (NOVA CONSTRUCTIONS S.A.)         |           |      | presales_pct_achieved ⚠️ 6.9% — VERIFY interpretation of "available"
#                                   |           |      | immediate_pipeline_risk (metro-wide project; 2km radius estimate)
#                                   |           |      | offplan_secondary_dominance (no direct Thessaloniki data)
#                                   |           |      | average_delay_duration (no public delay record; conservative estimate)
#                                   |           |      | str_concentration (estimated from listing count vs housing stock)
# ──────────────────────────────────|-----------|------|────────────────────────────────────────────────────────
# One Athens                        |    25     |  0   | presales_pct_achieved ⚠️ 10% — "Ready to Move" with 90% unsold: RED FLAG
# (DIMAND S.A.)                     |           |      | comp_capital_appreciation (5yr CAGR estimated; Bank of Greece data used)
#                                   |           |      | str_concentration (legacy pre-ban estimate; ban reduced active listings)
#                                   |           |      | population_growth_rate (Athens metro estimate; no city-district level data)
#                                   |           |      | debt_cash_position (DIMAND listed but no standalone financials found)
# ──────────────────────────────────|-----------|------|────────────────────────────────────────────────────────
# The Ellinikon – Marina Residences |    25     |  0   | rental_absorption_velocity ⚠️ FORWARD ESTIMATE — no existing rental market
# (LAMDA Development S.A.)          |           |      | resale_velocity ⚠️ FORWARD ESTIMATE — no secondary market yet
# (LAMDA Development S.A.)          |           |      | days_on_market ⚠️ FORWARD ESTIMATE — district not yet operational
#                                   |           |      | occupancy_vacancy_rate ⚠️ FORWARD ESTIMATE — no live data
#                                   |           |      | presales_pct_achieved ⚠️ 11% for Marina Residences; broader Ellinikon at 85–93%
#                                   |           |      | comp_rental_yields (no Marina Residences-specific rental comparables)
#                                   |           |      | safety_crime_index (Athens city-level used; Elliniko suburb likely higher)
# ──────────────────────────────────|-----------|------|────────────────────────────────────────────────────────
# Property 4                        |     —     |  —   | NOT PROVIDED — please attach property spec
# ──────────────────────────────────────────────────────────────────────────────
#
# CRITICAL FLAGS (engine-level attention):
#
# 1. LUX&EASY PRESALES (6.9%): 2,141 of 2,300 units available with March 2027 completion.
#    Either: (a) unit count = total available for purchase (not just unsold), or
#    (b) absorption is very weak for a mass-market development. Verify with NOVA directly.
#
# 2. ONE ATHENS PRESALES (10%) + YIELD COMPRESSION (20.0): "Ready to Move" with 90% unsold
#    in a premium market + STR ban killing yield investors = serious demand question.
#    DIMAND's institutional quality de-risks delivery but not absorption.
#
# 3. ELLINIKON MARINA ALL-FORWARD DATA: Groups 1 and 7 scores are projected, not historical.
#    The engine should treat Ellinikon as a forward-looking bet with high uncertainty bands.
#    The broader Ellinikon project has excellent fundamentals (LAMDA financial strength = 87,
#    presales at Little Athens = 85–93%) but Marina Residences specifically (€1M–€20M) shows
#    only 11% absorption — consistent with ultra-luxury illiquidity, not project failure.
#
# 4. ESCROW QUALITY (all = 50): All three properties score 'Partial' as Greece has no
#    statutory escrow equivalent to UAE RERA. This is a market-wide structural characteristic,
#    not project-specific risk differentiation.
