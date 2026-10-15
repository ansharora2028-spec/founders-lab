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
6. **Depth mode** — `quick` (generate 3, carry 1 forward; cheapest), `standard` (generate 8, carry 3; default), `deep` (generate 12, carry 5; most expensive). Default to `standard` if they have no preference.

Infer the local search language(s) and currency from the location and target market; state them in the read-back so the user can correct them.

## 3. Read back and confirm
Read the whole contract back as a compact table. Ask: "Is this contract correct? Only you can change it after this point." Apply corrections and read back again until the user explicitly confirms. Do not proceed without explicit confirmation (or the non-interactive rule in §1).

## 4. Create the run
1. Run `date -u +%Y-%m-%dT%H:%M:%SZ` and use it for the date in the run id and every timestamp below. `run_id` = `<YYYY-MM-DD>-<slug>`, where the slug is 2–4 kebab-case words from location and path (e.g. `2026-01-31-pune-b2c-open`). If the folder exists, append `-2`, `-3`…
2. `mkdir -p ventures/runs/<run_id>/ideas`
3. Write `ventures/runs/<run_id>/00-contract.md` in the schema.
4. Write `ventures/runs/<run_id>/run-log.md` in the schema, with the depth mode, `pivots used: 0/2`, the start time, and a Stages row `intake — contract confirmed`.
5. If `ventures/LEDGER.md` does not exist, create it containing only the line `# venture ledger` and a blank line.

## 5. Report
Tell the user the run id and folder, and the next step: `/venture:scout` (or that `/venture:run` will continue automatically).
