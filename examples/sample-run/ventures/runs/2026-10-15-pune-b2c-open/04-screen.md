---
run_id: 2026-10-15-pune-b2c-open
agent: screener
version: 1
created: 2026-10-15T10:00:00Z
---

## Hard-constraint check
| idea | K# checked | result | reason |
|---|---|---|---|
| I01 | K1, K2, K5, K6, K7, K9 | pass | K1: ₹499 per agreement, no stock or licence capital stated. K2: manual check with 24 h turnaround is feasible at low volume; scale beyond ~10 h/week is not shown. K5: service-only, no inventory. K6: first paid check is plausible within 3 months. K7: sold to individual tenants (B2C). K9: deliverable in spare hours. |
| I01 | K3 | pass, flag | K3 lists spreadsheets, social media and languages. The clause red-flag checklist needs legal-domain knowledge the user does not state. This is not a HARD breach on its face, but the idea depends on either a freelancer (K4 FLEXIBLE) or a checklist the user builds alone. Not scored as a stretch used. |
| I01 | K8 | pass, flag | No listed off-limits category applies. The generator notes legal-adjacent territory. [ASSUMPTION: a paid service that comments on the legal validity of a document may need licensed legal input in India; not verified by this screen.] The idea is only a registration and red-flag check, so it must not give legal advice. |
| I02 | K1, K2, K5, K6, K7, K8, K9 | pass | K1: low build cost if no-code or API tools are used. K2: daily 5-minute prompts plus a build and Instagram marketing in 10 h/week is tight but not shown to be a breach. K5: subscription, no inventory. K6: first paid subscriber plausible within 3 months if the product exists. K7: individual learners (B2C). K8: no off-limits category. K9: spare-hour product. |
| I02 | K3, K4 | pass, flag | K3 lists no coding skill. The idea requires a WhatsApp Business API integration and a speech/TTS API (Sarvam, per the ideas file). Either no-code tooling (K4 "can learn", no stretch needed) or a freelancer (K4 FLEXIBLE stretch "freelancer hiring", unlock "only within the K1 capital limit") is needed. The K1 cap on the freelancer is not yet evidenced, so the stretch is not counted as used. |
| I03 | K1, K2, K3, K5, K6, K7, K8, K9 | pass | K1: community and listing costs are low. K2: moderation and listing admin are light. K3: community administration and social marketing. K5: holds no inventory and no buyer funds are stated. K6: first paid listing plausible within weeks of launch. K7: sellers and buyers are individuals (B2C). K8: used furniture and appliances are not listed as off-limits. K9: spare-hour operation. |
| I03 | K7 (revenue model) | pass, flag | The revenue is a seller-side listing fee; buyers pay nothing. This is B2C on both sides and does not breach K7. Revenue depends on seller volume, which is untested. |

- user-original: no user-original idea was supplied. The contract records starting path c with "in their words: none", so no user-original row is scored.
- Not read by this screen, by rule: `01-local-market.md`, `02-signals.md`. Signal content is judged only from the ids and pitch in `03-ideas.md`. The ideas file cites "Rentomojo promotional material, C01" for the ₹50,000 furnishing figure. That figure and the ₹2,199/month rental anchor are not verified here.
- No idea is rejected on a HARD constraint in this screen.

## Competitors
### I01
- [C01] Surepass — paid tenant verification for Pune, plans listed from ₹79 to ₹689 including a police-verification tier, per vendor page; an identity and tenant check, not a leave-and-licence document check [source: https://surepass.io/tenant-verification/]
- [C02] AuthBridge — onboarding and authentication platform; its search summary describes a landlord-side Pune police-verification registration flow. Adjacent to the idea, not a document check for tenants [source: https://authbridge.com/?p=61226]
- [C03] Pune police digital tenant verification — free landlord-side route, with an offline paper fallback at the local police station, per a Pune guide. Free substitute for part of the service [source: https://housing.com/news/tenant-police-verification-in-pune-importance-and-process/]
- [C04] Maharashtra IGR portal — a registered agreement carries a registration number that a society member checked on the official portal. Free substitute for the registration-status step [source: https://www.punekarnews.in/pune-how-to-spot-a-fake-rent-agreement-before-it-lands-you-in-trouble/]
- [C05] Risk, not a competitor: a Pune-focused report says Maharashtra is digitising tenant verification, which could absorb part of the service [source: https://www.punekarnews.in/?p=208283]
- novelty: contested. Two adjacent vendors and two free substitutes. No direct tenant-facing agreement-check competitor with a price was found. Queries run: "rent agreement verification service Pune tenants online"; "Maharashtra IGR e-stamp registration verification online portal rent agreement check".

### I02
- [C06] Zaplingo — WhatsApp and Telegram AI tutor for conversation, pronunciation and grammar, with voice-note feedback. India pricing and language support not confirmed [source: https://callin.io/ai-tools/zaplingo]
- [C07] Supernova — AI English tutor built for Indian learners, speaking to them in Hindi, Tamil and Telugu; voice via ElevenLabs. No WhatsApp channel seen [source: https://elevenlabs.io/blog/supernova]
- [C08] SpeakX — Indian English-speaking app, Gurgaon-headquartered per search summary [source: https://westbridgecap.com/portfolio/speakx]
- [C09] Indilingo Voice — AI tutor that calls the learner's phone to practise conversation across 100+ languages [source: https://index.dodopayments.com/indilingo-voice]
- [C10] Specker.ai (Stella) — AI speaking tutor; its own posts claim 150K+ downloads, self-reported and unverified [source: https://linkedin.com/company/speckerai]
- novelty: crowded. Five direct AI spoken-English tutors are named. A Marathi-first niche is not shown to be empty, but the rubric scores it as crowded.
- queries run: "spoken English practice WhatsApp voice AI tutor India".

### I03
- [C11] OLX — a commercial blog recommends OLX as the top channel for selling used furniture in Pune and says it has the most buyers. Blog claim, unverified [source: https://knowledge.digirake.com/uncategorized/sell-old-sofa-pune]
- [C12] Facebook Marketplace and apartment, society and RWA WhatsApp groups — the same blog says these are active in Hinjewadi and Magarpatta townships [source: https://knowledge.digirake.com/uncategorized/sell-old-sofa-pune]
- [C13] Used-furniture dealers near Bohri Ali, Hadapsar and Camp — buy sofas outright and arrange pickup, per the same blog [source: https://knowledge.digirake.com/uncategorized/sell-old-sofa-pune]
- novelty: contested. Three direct channels are named; OLX could be a dominant incumbent, which would make the state crowded. Dominance is not verified. Queries run: "used furniture resale Pune tenants WhatsApp group OLX Facebook Marketplace".
- reasoning: the only source for I03 competitors is one commercial blog, and no tenant-departure board was found.

## Scores
| idea | signal | constraint fit | novelty | unfair advantage | speed to revenue | total /25 |
|---|---|---|---|---|---|---|
| I03 | 1 (L01, L03; weak, and the generator also calls it weak; no dates) | 4 (fits with slack; K7 and K5 are clean) | 3 (contested) | 0 (user stated none) | 4 (first paid listing plausible in weeks; not evidenced) | 12 |
| I01 | 2 (S06 national and L01 local; no dates; local coverage 3/10 per generator) | 2 (K3 gap needs a flexible K4 freelancer or a self-built checklist; unlock uncertain) | 3 (contested; adjacent vendors and free substitutes) | 0 (user stated none) | 4 (first paid check plausible within 3-4 weeks through a broker or society channel; not evidenced) | 11 |
| I02 | 2 (S04 and S01; no dates; S01 vendor pricing conflicts per generator) | 2 (needs no-code or a freelancer; K4 stretch unlock "within K1" uncertain) | 1 (crowded; five direct competitors) | 0 (user stated none) | 3 (product build first; within half of the 3-month limit at best) | 8 |

Scores are for ranking only. They do not indicate that any idea will pass.

## Ranking
1. I03 — 12/25 (signal 1, constraint fit 4, novelty 3, advantage 0, speed 4)
2. I01 — 11/25 (signal 2, constraint fit 2, novelty 3, advantage 0, speed 4)
3. I02 — 8/25 (signal 2, constraint fit 2, novelty 1, advantage 0, speed 3)
- tie-break notes: none needed.
- rejected: none (no HARD-constraint violation found)
- user-original: not supplied, not scored
