---
description: venture intake — capture starting point, location, target market, constraints (HARD/FLEXIBLE), unfair advantages and depth mode, confirm them with the user, and write 00-contract.md for a new run.
argument-hint: "[optional: anything you already want to tell intake, e.g. 'Pune, India; ₹1L hard; 10 hrs/week; B2C; no idea yet; quick']"
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion, Bash(mkdir *), Bash(date *)
---

# /venture:intake

You are the main session of the venture pipeline. Only you talk to the user.

## 0. Load the rules
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md` and follow it for the rest of this command.
2. Read the `00-contract.md` and `run-log.md` sections of `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`.
3. If `ventures/LEDGER.md` exists in the current project directory, read it. If a past run has the same location, mention it in one line ("Your ledger has N past runs for <city>; ideas that died there won't be regenerated without a material change.").

## 1. Pre-filled answers
Arguments given to this command: `$ARGUMENTS`

If the arguments already answer some intake topics, use those answers and do not ask those questions again. Ask only for what is missing or ambiguous.

**Non-interactive sessions** (for example `claude -p`, where you cannot get a reply): if the arguments answer every required topic, treat the arguments as the user's confirmed contract, record `how: arguments (non-interactive)` in the Confirmation section, and continue. If a required topic is missing and you cannot ask, stop and print exactly which topics are missing. Never invent a constraint.

## 2. Ask, one topic at a time, in this order
Use the AskUserQuestion tool where it is available; otherwise ask in plain chat and wait for the answer. Ask **one topic per turn**.

1. **Starting point** — (a) I have a specific idea, (b) I have a space or industry in mind, (c) I have nothing yet. If (a) or (b), ask them to describe it and capture it **in their own words**, verbatim.
2. **Location** — the city and country they are based in.
3. **Target market** — local (their city), national, a specific other country, or online/global. Point out that this can differ from where they live.
4. **Constraints** — for each item, capture a value and whether it is **HARD** or **FLEXIBLE**. If FLEXIBLE, capture the **stretch range** and the **condition that unlocks it** (example: "₹2L, can stretch to ₹5L if payback < 6 months"). You may group 2–3 related items per question to keep it short, but every item needs an answer:
   - K1 capital available
   - K2 hours per week
   - K3 skills they have; K4 skills they can hire or learn
   - K5 risk appetite (low / medium / high) and what they cannot afford to lose
   - K6 time to first revenue
   - K7 B2B, B2C, or either
   - K8 off-limits categories (ethical, personal, legal)
   - K9 anything else they want to add
   If the user gives a value without saying HARD or FLEXIBLE, ask. If they don't know, default to HARD and tell them.
5. **Unfair advantages** — industry access, a community, distribution, a family business, rare skills. Optional, but explain that it matters. "None" is a valid answer.
6. **Depth mode** — `quick` (generate 3, carry 2 forward; cheapest), `standard` (generate 8, carry 3; default), `deep` (generate 12, carry 5; most expensive). Default to `standard` if they have no preference. (When called from `/venture:check`, the depth mode is `check` or `check+variants` and this question is skipped.)

7. **What you know about your town**: the founder knowledge questionnaire (§2b).

Infer the local search language(s) and currency from the location and target market; state them in the read-back so the user can correct them.

## 2b. Founder knowledge questionnaire
The founder lives in this market and knows things no search engine does. Ask for **observations, not opinions**. "Will people pay?" gets an optimistic yes; "what did you last pay?" gets a fact. Tell the founder: "These help the research a lot, especially in smaller towns. Skip anything you don't know. A guess is fine if you say it's a guess."

Ask in 2–3 short batches (AskUserQuestion where available). For every number, ask for a **range** (low / likely / high) and **how they know**: `counted` (they saw or counted it), `heard` (someone told them) or `guess`.

**About the town (always):**
1. Roughly how many people live in your town or area, and how many households or students are within 3 km of where you'd start?
2. Who are the people you'd most likely sell to: age group, typical monthly income, salaried, business or farming families?
3. What do people in your town travel to a bigger city to buy, or order online because it isn't available locally?
4. Which big national brands or apps are *not* available or don't work well in your town (for example Urban Company, Blinkit, Swiggy, Lenskart, Cult.fit, PhysicsWallah centres)?
5. How do people find services there: word of mouth, WhatsApp groups, local Instagram pages, a shopkeeper's recommendation, newspapers? Which local groups are you in, and roughly how many members do they have?
6. How do people pay: cash, UPI, credit (udhaar)? When do they have money (salary date, harvest, festival or wedding seasons)?
7. What do local rent (a small room or shop) and a helper's monthly wage cost?
8. What do people around you complain about most in services or products they already pay for?

**About the idea (only when there is one, as in `/venture:check` or path (a)):**
9. What do the people you'd sell to pay *today* for this job or the nearest alternative, and how much? Give real examples: what you, your family or friends paid.
10. Name 2–3 competitors or alternatives near you: their price, and the main complaint you've heard about each.
11. How many potential customers could you personally reach in the first month (contacts, groups, shops, schools)?
12. Anything else about your town that would make this work or fail?

Write the answers to `00-founder-knowledge.md` in the schema, verbatim, with each number's range and how-known tag. "Skipped" is a valid answer. **Never fill in an answer the founder didn't give.** In a non-interactive session, use any answers given in the arguments and mark the rest `not asked (non-interactive)`.

## 3. Read back and confirm
Read the whole contract back as a compact table. Ask: "Is this contract correct? Only you can change it after this point." Apply corrections and read back again until the user explicitly confirms. Do not proceed without explicit confirmation (or the non-interactive rule in §1).

## 4. Create the run
1. Run `date -u +%Y-%m-%dT%H:%M:%SZ` and use it for the date in the run id and every timestamp below. `run_id` = `<YYYY-MM-DD>-<slug>`, where the slug is 2–4 kebab-case words from location and path (e.g. `2026-01-31-pune-b2c-open`). If the folder exists, append `-2`, `-3`…
2. `mkdir -p ventures/runs/<run_id>/ideas`
3. Write `ventures/runs/<run_id>/00-contract.md` and `ventures/runs/<run_id>/00-founder-knowledge.md` in the schema.
4. Write `ventures/runs/<run_id>/run-log.md` in the schema, with the depth mode, `pivots used: 0/2`, the start time, and a Stages row `intake — contract confirmed`.
5. If `ventures/LEDGER.md` does not exist, create it containing only the line `# venture ledger` and a blank line.
6. If a city memory file `ventures/cities/<city-slug>.md` exists for the target market's city, note it in the run-log Stages row (scouts, the generator and the strategist will read it).

## 5. Report
Tell the user the run id and folder, and the next step: `/venture:scout` (or that `/venture:run` will continue automatically).
