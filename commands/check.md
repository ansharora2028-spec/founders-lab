---
description: venture check — put YOUR idea through the full feasibility check (market research focused on it, your own local knowledge, sharpening, a full competitor and framework analysis, unit economics in three scenarios plus a simulation, blind prosecution, evidence audit, one revision round) and get a clear verdict - DO IT (with a cheap test plan for this week), LOOKS VIABLE ON PAPER (with the assumptions to confirm first), or DON'T (with the evidence and the money it saves you). Add --variants to also test up to 3 variations of your idea.
argument-hint: "\"<your idea in your own words>\" [--variants] [optional intake answers]"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *)
---

# /venture:check

The user brought their own idea and wants to know whether to do it. Give it the same full treatment generated ideas get — no shortcuts, and no easier standard because it is theirs. The builders work to make the user's idea as strong as the evidence allows, and the judges apply the same bar as always. A clear "don't" is a miss, not a disaster: it saves the user money and months, and the report says what would have to change.

(`/venture:kill "<idea>"` is the fast version: it judges the idea exactly as written, with no research or sharpening. `/venture:check` researches the market for the idea, sharpens it, models the economics, and allows one evidence-backed revision before the final verdict.)

## 0. Load the rules
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`. It overrides everything else.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md` (Conventions, Visibility matrix, run-log schema).
3. Read `ventures/LEDGER.md` if it exists. If a past run killed an idea like this one under a similar contract, tell the user in one line and which run it was, then continue (the user decides; the generator must state the material change).

## 1. Parse the arguments
Arguments: `$ARGUMENTS`
- The idea is the quoted text. If there is no quoted text, the idea is everything before `--variants` and before any intake answers. If there is no idea at all, ask: "Describe your idea in a sentence or two, in your own words."
- `--variants` present → depth mode `check+variants`; otherwise depth mode `check`.
- Anything else is pre-filled intake answers.

## 2. Intake (full constraints, no depth question)
Follow `${CLAUDE_PLUGIN_ROOT}/commands/intake.md`, with these differences:
- **Starting point** is already known: path (a), with the idea captured verbatim in the user's own words. Do not ask topic 1.
- Ask one extra question right after it, unless the idea already answers it: **"Who would pay for this, and how would you charge? (Say 'not sure' if you don't know yet.)"** Record the answer verbatim under Starting point as `how they plan to charge:`. "Not sure" is a fine answer.
- **Depth mode** is `check` or `check+variants` from §1. Do not ask topic 6.
- Ask everything else (location, target market, constraints K1–K9 with HARD/FLEXIBLE, unfair advantages) and get explicit confirmation, exactly as intake says. The non-interactive rule in intake §1 applies.
- Use a run id of `<YYYY-MM-DD>-check-<slug>`.

## 3. Run the pipeline on the idea
Follow each stage's command file exactly, with this run's id:

| # | stage | follow | what it does for the user's idea |
|---|---|---|---|
| 1 | scout | `${CLAUDE_PLUGIN_ROOT}/commands/scout.md` | researches the market for this idea (path (a) focus) — local competitors, prices, failures, regulation, demand signals |
| 2 | generate + screen + lock | `${CLAUDE_PLUGIN_ROOT}/commands/generate.md` | writes up the idea as I01, explained (how it works, need gap, how it makes money); in `check+variants`, adds up to 3 variants; screens against HARD constraints and competitors; locks kill criteria **before** any sharpening |
| 3 | forge, strategy, economics, simulation | `${CLAUDE_PLUGIN_ROOT}/commands/forge.md` | sharpens the idea (exact customer, narrowest wedge, path to first 100 customers); runs the **full framework check** independently: competitors and big players, whether you can steal their customers, your price against theirs, Porter's Five Forces, need gap, Jobs-to-be-Done, Kano, consumer behaviour, STP, bottom-up market size, Ansoff, PESTLE, 4Ps, funnel, moat and a simulated customer panel; models the unit economics; and **simulates** thousands of scenarios |
| 4 | kill | `${CLAUDE_PLUGIN_ROOT}/commands/kill.md` § A | blind prosecution against the locked criteria, evidence audit, verdict; one evidence-only revision round if the judge says REVISE; pivots as usual |
| 5 | verdict report and ledger | `${CLAUDE_PLUGIN_ROOT}/commands/blueprint.md` | `90-blueprint.md` (DO IT) or `91-nothing-passed.md` (DON'T), and the ledger |

Print a one-line progress note before each paid stage. If the user's idea is REJECTED at Screen (it breaks a HARD constraint), that is the verdict: skip to stage 5 and explain which constraint it breaks and by how much.

## 4. Final message — the verdict
Lead with the answer, in plain language:

```
Your idea: <pitch>
Verdict: DO IT — it passed | LOOKS VIABLE ON PAPER — confirm <n> things first | DON'T DO IT — it was killed | DON'T DO IT AS IS — it breaks <constraint> | DROPPED — the framework check found <reason>
Confidence: <judge's 1–10>

How it would work:   <from forge-v<n>.md / 03-ideas.md>
The need gap:        <one or two sentences, with what the evidence did or didn't show>
How it makes money:  <who pays, price, and the conservative case: cost per sale, customers needed to break even, months to first revenue>
Simulation:          <viable share>% of simulated cases break even by month <K6> within your capital; it depends most on <top 2 inputs>
Competition:         <biggest competitor, their price vs yours, and who you can win from them, from strategy-v1.md>
Why:                 <the judge's top two decisive reasons, quoted, with file refs>
```

Then:
- **LOOKS VIABLE ON PAPER** → the 2–3 assumptions to confirm first, each with how to check it cheaply and a "stop if" number, then the experiments. Say plainly: "The numbers work in most simulated cases, but nobody has yet shown that people in <town> will pay. Confirm these before you spend real money."
- **DO IT** → the 3 cheapest experiments to run this week (cost, time, success threshold) from `90-blueprint.md`, and the kill signals that should make them stop.
- **DON'T** → the estimated money and months saved (labeled ESTIMATE), what would have to be true for it to work, and whether a variant or pivot candidate did better. Suggest `/venture:check "<revised idea>" --variants` or `/venture:run` as the next step.
- For `check+variants`, a one-line verdict for each variant that was carried.
- The path to the full report and to the run folder.

Never soften a kill because the idea is the user's own. Quote verdicts as written.
