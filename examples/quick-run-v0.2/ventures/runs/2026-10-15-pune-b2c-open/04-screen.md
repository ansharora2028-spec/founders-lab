---
run_id: 2026-10-15-pune-b2c-open
agent: screener
version: 1
created: 2026-10-15T09:25:35Z
---

## Hard-constraint check
| idea | K# checked | result | reason |
|---|---|---|---|
| I01 | K1, K2, K3, K4, K5, K6, K7, K8, K9 | pass | K1 ₹199 flat per case, no capital beyond the ₹1,00,000 limit; K2 10 h/week stated; K3 uses English, Hindi, Marathi and spreadsheets; K4 relies on a third-party LLM API and WhatsApp delivery, no freelancer spend; K6 first revenue plausible but unverified; K7 individuals pay; K8 no listed category (legal-style drafting is not a K8 category, its regulatory status was not checked); K9 no full-time need. No FLEXIBLE stretch used. |
| I02 | K1, K2, K3, K4, K5, K6, K7, K8, K9 | pass | K7 residents pay a household subscription, vendors do not pay; K2 and K1 fit the stated founder plan of 1–2 societies; K6 depends on society committee approval, unverified; K8 no listed category; no FLEXIBLE stretch used. |
| I03 | K1, K2, K3, K4, K5, K6, K7, K8, K9 | pass | K1 ₹399 one-time kit, no inventory; K7 tenants pay; K3 uses English, Hindi, Marathi and Instagram marketing; K6 kit sale plausible but unverified; K8 no listed category; no FLEXIBLE stretch used. |
| user-original | — | not present | No idea with lens user-original exists. The contract records starting path c and "in their words: none", and 03-ideas.md contains I01 to I03 only. Nothing to check or score. |

## Competitors
### I01
- [C01] RegisterKaro — private online consumer complaint filing and legal notice drafting by experts; per-case price not shown on the page seen (national) [source: https://www.registerkaro.in/consumer-complaint]
- [C02] National Consumer Helpline — free government grievance channel, reachable by phone, app and WhatsApp; a substitute, not a paid competitor (national) [source: https://consumerhelpline.gov.in/public/successstorydetails/344]
- [C03] Search summary (page not opened) reports 8,919 e-commerce complaints to the National Consumer Helpline for 2025-04-25 to 2025-06-30, with e-commerce the highest sector (national) [source: https://www.storyboard18.com/amp/digital/nch-registers-highest-grievances-for-e%e2%80%91comm-resulting-in-refund-of-rs-3-69-cr-in-april-june-73341.htm, 2025-07]
- [C04] The "29% of National Consumer Helpline grievances" figure in the 03-ideas.md entry has no source in that entry. It is not used here as a fact.
- queries run: "WhatsApp consumer complaint refund drafting service India paid per case e-commerce"
- novelty: contested (one direct paid competitor found, RegisterKaro; no Pune-specific listing seen)

### I02
- [C05] Urban Company — on-demand home-service marketplace with Pune pages for electricians, professional home cleaning, RO repair and refrigerator repair (national platform) [source: https://www.urbancompany.com/quick-links/pune-electricians; https://www.urbancompany.com/quick-links/pune-professional-home-cleaning]
- [C06] Urban Company Pune society-level page for plumbing, stating a 30-day plumbing guarantee and damage protection up to INR 10,000 (search summary; page not opened) [source: https://www.urbancompany.com/pune-plumbers-mahesh-society-bibvewadi]
- [C07] The search found no WhatsApp booking channel, no bulk or subscription plan for housing societies, and no society-run vendor arrangement in Pune.
- [C08] The VouchList Mumbai model cited in 03-ideas.md was not opened and is not counted here (other city: Mumbai).
- queries run: "Pune housing society home services subscription WhatsApp vendor booking plumber electrician"
- novelty: crowded (one large platform with Pune listings across several home-service categories; the reading that it is a dominant incumbent is an inference from those listings)

### I03
- [C09] RentOk — landlord and PG-side product pages describing digital move-in checklists and deposit tracking; product marketing, not a tenant-side kit (national) [source: https://wb.rentok.com/?p=2503; https://wb.rentok.com/legal/security-deposits-in-india/]
- [C10] Move-out inspection service page, Chennai, marketing material; a different city and an inspection service, not a tenant kit (other city: Chennai) [source: https://pixel-perfect-page-450.lovable.app/inspection/move-out-inspection]
- [C11] Free practical guides on PG deposit recovery in India, describing a dated written demand, then the National Consumer Helpline (1915), then a District Consumer Commission; a 2026 guide from a non-government site (national) [source: https://righttoinformation.wiki/practical-guides/pg-coliving-security-deposit-not-returned-refund-guide]
- [C12] Rental-agreement templates are widely available free [ASSUMPTION: taken from the 03-ideas.md entry; not searched]
- queries run: "tenant rental agreement move-in condition report deposit return kit India PG tenants service"
- novelty: open (no direct tenant-side kit competitor found in Pune; the adjacent results are landlord-side or in another city). This rests on one query and is provisional.

## Scores
| idea | signal | constraint fit | novelty | unfair advantage | speed to revenue | total /25 |
|---|---|---|---|---|---|---|
| I03 | 1 | 4 | 5 | 1 | 5 | 16 |
| I01 | 2 | 4 | 3 | 1 | 3 | 13 |
| I02 | 2 | 3 | 1 | 0 | 1 | 7 |

- I03 signal 1: S07 (Pune police order, 2026-07-03, as cited in the entry) is aimed at landlords and does not show tenant pain, as the entry itself says; S08 is a single anecdote; L02 is shared with I02. One weak signal.
- I03 constraint fit 4: fits with slack; ₹399 kit, no stretch used.
- I03 novelty 5: no direct tenant-side competitor found in Pune (see C09 to C12); provisional, one query.
- I03 unfair advantage 1: Hindi and Marathi letter drafting uses the stated language skills. The user stated no unfair advantage.
- I03 speed 5: a kit can be produced quickly and a first sale is plausible within 2–4 weeks if demand exists; demand is unverified.
- I01 signal 2: four cited ids (S01, S02, S09, S04), none labelled as Pune-local in the entry; the entry says S09 prices conflict and the effect of S02 is not established.
- I01 constraint fit 4: no HARD violation and no stretch; third-party API cost is unverified but small against K1 on the stated price.
- I01 novelty 3: one direct paid competitor (C01).
- I01 unfair advantage 1: Hindi and Marathi drafting uses the stated language skills.
- I01 speed 3: first paid case is plausible, but WhatsApp delivery and API setup time are unverified, so this is within about half the K6 limit.
- I02 signal 2: two local ids (L01, L02) cited; the entry says no Pune enabling condition is verified and its only example is Mumbai (other city).
- I02 constraint fit 3: fits, but K6 depends on society committee approval, which is unverified and sits near the edge of K6.
- I02 novelty 1: crowded per C05 and C06 (inference from listings).
- I02 unfair advantage 0: no stated advantage applies.
- I02 speed 1: at the K6 limit, because each society needs committee approval before the first paid household.

## Ranking
1. I03 — 16/25
2. I01 — 13/25
3. I02 — 7/25
- rejected: none
- not scored: user-original (no such idea exists in the run)
- note: scores are for ordering only. I03 ranks first despite the weakest signal, because novelty and speed carry it. Its signal is the main open risk, and Pune demand is unverified for all three ideas.
