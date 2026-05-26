"""
projects_data.py — Consolidated project asset data for all four countries.
Sources: projects_data/projects_portugal.py, projects_data/projects_uae.py,
         projects_data/projects_greece.py, projects_data/projects_thailand.py

Raw variables use 0–100 magnitude scoring:
  Higher always means MORE of that thing, good or bad.
  The engine handles inversion mathematically.
  Missing variables are set to None — the engine outputs 50 (neutral) for these.
"""

PROJECTS = {

    # ── GREECE ─────────────────────────────────────────────────

    "ellinikon_marina_residences": {
        "project_name": 'The Ellinikon – Marina Residences',
        "country": 'Greece',
        "city": 'Athens',
        "price_range": 'Γé¼1M ΓÇô Γé¼20M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": "Luxury waterfront living within Europe's largest urban regeneration project",
        "description": 'The Ellinikon ΓÇô Marina Residences is part of The Ellinikon masterplan, a massive urban regeneration project led by LAMDA Development. It provides luxury living on the Athens Riviera coastline, closely situated to the Ellinikon Metropolitan Park, Riviera Galleria, and local marinas.',
        "tags": ['Waterfront', 'Master-planned community', 'Under construction'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "one_athens": {
        "project_name": 'One Athens',
        "country": 'Greece',
        "city": 'Athens',
        "price_range": 'Γé¼200K ΓÇô Γé¼4.5M',
        "project_stage": 'Ready',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": 'Ready-to-move residential redevelopment in central Athens',
        "description": 'One Athens is a residential redevelopment project delivered by DIMAND. Located in Kolonaki / Athens City Centre, it offers central proximity to the Athens Concert Hall, embassies, luxury retail, and museums.',
        "tags": ['Ready to move in', 'City centre', 'Luxury retail access'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "luxeasy_thessaloniki": {
        "project_name": 'LUX&EASY Thessaloniki',
        "country": 'Greece',
        "city": 'Thessaloniki',
        "price_range": 'Γé¼120K ΓÇô Γé¼240K',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": 'High-volume branded residences with strong Greek Golden Visa pathway',
        "description": "LUX&EASY Thessaloniki is a large-scale branded residential development by NOVA CONSTRUCTIONS S.A. in Greece's second-largest city. With over 2,300 units across the Thessaloniki Metropolitan Area, the project offers the lowest entry point into the Greek Golden Visa program at Γé¼120,000 ΓÇö well below Athens pricing.",
        "tags": ['Golden Visa eligible', 'Lowest entry point', 'Central urban location', 'Family infrastructure nearby'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    # ── PORTUGAL ───────────────────────────────────────────────

    "palmares": {
        "project_name": 'Palmares Ocean Living & Golf Resort',
        "country": 'Portugal',
        "city": 'Algarve',
        "price_range": 'Γé¼199K ΓÇô Γé¼1.1M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'managed',
        "highlight": 'Golf resort residences on the Algarve coast with Golden Visa access',
        "description": "Palmares Ocean Living & Golf Resort occupies a spectacular position on the Algarve coast near Lagos, set within a world-class golf resort overlooking Meia Praia beach and the Alvor estuary. Developed by Oxy Capital, the project offers branded resort residences with full property management, rental pooling, and Golden Visa eligibility. Algarve's status as Europe's premier golf and lifestyle destination makes this a high-conviction hold for families seeking residency with strong leisure upside.",
        "tags": ['Golden Visa eligible', 'Resort lifestyle', 'Under construction upside', 'Algarve coastal'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "amoreiras_prime": {
        "project_name": 'Amoreiras Prime Residences',
        "country": 'Portugal',
        "city": 'Lisbon',
        "price_range": 'Γé¼750K ΓÇô Γé¼3.5M',
        "project_stage": 'Ready',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": "Landmark luxury development in Lisbon's most connected neighbourhood",
        "description": "Amoreiras Prime Residences is a landmark luxury development by Vanguard Properties in the heart of Lisbon's Amoreiras district ΓÇö home to the Amoreiras Shopping Centre, the Lyc├⌐e Fran├ºais Charles Lepierre, and direct access to the Marqu├¬s de Pombal business corridor. With only 34 units across a boutique building, the project offers genuine scarcity value, Golden Visa eligibility, and the Vanguard brand guarantee.",
        "tags": ['Golden Visa eligible', 'French school nearby', 'Business district access', 'Vanguard luxury brand'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "infante_residences": {
        "project_name": 'Infante Residences',
        "country": 'Portugal',
        "city": 'Lisbon',
        "price_range": 'Γé¼399K ΓÇô Γé¼1.01M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": "Rehabilitation condominium development in Lisbon's central district",
        "description": 'Infante Residences is a rehabilitation condominium development located in the Estrela / Avenida Infante Santo area of Lisbon. Developed by Vanguard Properties, the project is situated near Jardim da Estrela, LX Factory, Amoreiras, and Hospital CUF Tejo.',
        "tags": ['Central location', 'Rehabilitation project', 'Hospitals nearby'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "the_lisboans": {
        "project_name": 'The Lisboans',
        "country": 'Portugal',
        "city": 'Lisbon',
        "price_range": 'Γé¼450K ΓÇô Γé¼2.5M',
        "project_stage": 'Ready',
        "ownership": 'freehold',
        "project_type": 'managed',
        "highlight": "Premium hospitality-lifestyle residences in Lisbon's historic core",
        "description": "The Lisboans is a landmark hospitality-residential concept in Alfama, Lisbon's oldest and most iconic district. Developed by Oxy Capital, the project blends boutique hotel services with private residential ownership, offering investors a rare combination of lifestyle asset and Golden Visa eligibility. Located steps from Pra├ºa do Com├⌐rcio and the Tagus riverfront, residents enjoy 5-star amenities, concierge services, and direct access to Lisbon's most sought-after cultural and dining destinations.",
        "tags": ['Golden Visa eligible', 'Within budget', 'Schools & hospitals nearby', 'Ready to move in'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    # ── THAILAND ───────────────────────────────────────────────

    "monument_thong_lo": {
        "project_name": 'The Monument Thong Lo',
        "country": 'Thailand',
        "city": 'Bangkok',
        "price_range": 'α╕┐30M ΓÇô α╕┐150M',
        "project_stage": 'Ready',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": "Sansiri ultra-luxury in Thong Lo ΓÇö Bangkok's most prestigious lifestyle address",
        "description": "The Monument Thong Lo is Sansiri's flagship ultra-luxury residential tower on Sukhumvit 55, Bangkok's most prestigious lifestyle corridor. Thong Lo commands the highest rental rates in Bangkok from Japanese expats, senior executives, and high-net-worth short-term tenants.",
        "tags": ['Thong Lo prestige', 'Ultra-luxury', 'Sansiri flagship', 'Only 10 units remaining'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "noble_ploenchit": {
        "project_name": 'Noble Ploenchit',
        "country": 'Thailand',
        "city": 'Bangkok',
        "price_range": 'α╕┐8.5M ΓÇô α╕┐185M',
        "project_stage": 'Ready',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": 'Bangkok CBD premium residential with direct BTS access and strong resale liquidity',
        "description": "Noble Ploenchit occupies one of Bangkok's most coveted residential addresses ΓÇö Phloen Chit Road in Lumphini, Pathum Wan ΓÇö directly connected to BTS Phloen Chit Station. For yield investors, Bangkok CBD condos at this location command premium rental rates from international executives and diplomats year-round.",
        "tags": ['BTS direct access', 'Bangkok CBD', 'Premium residential asset', 'Strong resale liquidity'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "hythe_by_botanica": {
        "project_name": 'HYTHE by Botanica',
        "country": 'Thailand',
        "city": 'Phuket',
        "price_range": 'α╕┐10.8M ΓÇô α╕┐165M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'villa',
        "highlight": 'Ultra-luxury Phuket villas by Botanica with 20+ year development track record',
        "description": "HYTHE by Botanica is an ultra-luxury villa development in Cherngtalay, Phuket's most exclusive residential enclave within Laguna Phuket. Developed by Botanica Luxury ΓÇö with 20+ years and 15+ delivered projects in Phuket ΓÇö HYTHE targets high-net-worth investors seeking a trophy lifestyle asset.",
        "tags": ['Phuket luxury villas', 'Under construction upside', '20+ year track record', 'Beach club proximity'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "laguna_lakelands": {
        "project_name": 'Laguna Lakelands',
        "country": 'Thailand',
        "city": 'Phuket',
        "price_range": 'α╕┐6.8M ΓÇô α╕┐60M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'managed',
        "highlight": 'Banyan Group integrated resort residences with professional rental management',
        "description": "Laguna Lakelands is the flagship development within Laguna Phuket ΓÇö Asia's most successful integrated resort destination, developed and operated by Banyan Group over 30+ years. The mixed-use project combines villa and condo residences with a world-class golf course, beach club, spa, and hotel infrastructure.",
        "tags": ['Mixed-use yield play', 'Banyan Group managed', 'Under construction upside', 'Airport & beach access'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    # ── UAE ────────────────────────────────────────────────────

    "burj_binghatti": {
        "project_name": 'Burj Binghatti Jacob & Co Residences',
        "country": 'UAE',
        "city": 'Dubai',
        "price_range": 'AED 8.2M ΓÇô AED 752M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'branded',
        "highlight": 'Ultra-luxury branded residences in Business Bay',
        "description": 'Burj Binghatti Jacob & Co Residences is an ultra-luxury residential tower developed by Binghatti Developers in collaboration with the Jacob & Co brand. Located in Business Bay, it provides central access to Burj Khalifa, Dubai Mall, and the Dubai Opera.',
        "tags": ['Branded residences', 'Ultra-luxury', 'UAE Golden Visa'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "damac_islands": {
        "project_name": 'DAMAC Islands',
        "country": 'UAE',
        "city": 'Dubai',
        "price_range": 'AED 2.25M ΓÇô AED 9.5M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'managed',
        "highlight": 'Emerging mixed-use community with waterfront lagoons in Dubailand',
        "description": 'DAMAC Islands is an emerging mixed-use master community located in Dubailand. Developed by DAMAC Properties, the development centers around waterfront lagoons and resort amenities with strong connectivity to Emirates Road.',
        "tags": ['Waterfront community', 'Resort lifestyle', 'UAE Golden Visa'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "dubai_creek": {
        "project_name": 'Dubai Creek Harbour',
        "country": 'UAE',
        "city": 'Dubai',
        "price_range": 'AED 1.2M ΓÇô AED 15M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'managed',
        "highlight": "Emaar's massive waterfront masterplan offering strong rental yields",
        "description": 'Dubai Creek Harbour is a major master-planned community by Emaar Properties in the Ras Al Khor area. This emerging mixed-use development offers residents access to Creek Marina, Creek Beach, and the Ras Al Khor Wildlife Sanctuary.',
        "tags": ['Emaar brand', 'Waterfront', '6.5% rental yield', 'UAE Golden Visa'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "greencrest": {
        "project_name": 'Greencrest at Dubai Hills Estate',
        "country": 'UAE',
        "city": 'Dubai',
        "price_range": 'AED 1.57M ΓÇô AED 3.89M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'apartment',
        "highlight": 'Emaar luxury residences in Dubai Hills with 6.5% yield and UAE Golden Visa',
        "description": "Greencrest at Dubai Hills Estate is an Emaar Properties development within the master-planned Dubai Hills community. The project sits adjacent to King's College Hospital London Dubai, GEMS International School, and Dubai Hills Mall.",
        "tags": ['6.5% rental yield', 'UAE Golden Visa', "King's College Hospital nearby", 'Emaar brand', '0% capital gains tax'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

    "sobha_hartland": {
        "project_name": 'Sobha Hartland',
        "country": 'UAE',
        "city": 'Dubai',
        "price_range": 'AED 1.2M ΓÇô AED 85M',
        "project_stage": 'Under Construction',
        "ownership": 'freehold',
        "project_type": 'managed',
        "highlight": 'Central luxury mixed-use community in Mohammed Bin Rashid City',
        "description": 'Sobha Hartland is a master-planned development by Sobha Realty in Mohammed Bin Rashid City (MBR City), Dubai. It offers freehold ownership for foreign investors and is centrally located near Downtown Dubai, Burj Khalifa, and Hartland International School.',
        "tags": ['Central location', 'UAE Golden Visa', 'Schools nearby'],
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

            # ── Variables not in source research file ──
            "projected_rental_yield": None,
            "construction_quality": None,
            "litigation_history": None,
            "infrastructure_proximity": None,
            "average_exit_velocity": None,
            "flipping_frequency": None,
        },
    },

}


def get_projects_by_cities(city_list: list) -> dict:
    """Return only projects whose city is in city_list."""
    return {k: v for k, v in PROJECTS.items() if v["city"] in city_list}


def get_projects_by_country(country: str) -> dict:
    """Return only projects for a specific country."""
    return {k: v for k, v in PROJECTS.items() if v["country"] == country}


def list_determinant_keys() -> list:
    """Return the canonical list of 31 raw variable keys in bucket order."""
    return [
        # Demand & Liquidity
        "micro_market_stage", "rental_absorption_velocity", "resale_velocity", "days_on_market", "occupancy_vacancy_rate",
        # Neighborhood Livability
        "safety_crime_index", "healthcare_access", "school_quality", "air_quality_index", "beach_coastal_access",
        # Demographic & Economic
        "population_growth_rate", "expat_concentration",
        # Supply Pressure
        "immediate_pipeline_risk", "active_unsold_inventory",
        # Delivery Track Record
        "average_delay_duration", "pct_projects_delivered", "completion_consistency",
        # Financial Credibility
        "escrow_quality", "debt_cash_position", "stalled_projects_count", "presales_pct_achieved",
        # Comp Market
        "comp_capital_appreciation", "comp_rental_yields", "comp_occupancy_rate",
        # Single-variable buckets
        "projected_rental_yield", "construction_quality", "litigation_history", "infrastructure_proximity",
        # Speculation Risk
        "str_concentration", "investor_owner_ratio", "offplan_secondary_dominance",
        # Exit Liquidity
        "average_exit_velocity", "flipping_frequency",
    ]
